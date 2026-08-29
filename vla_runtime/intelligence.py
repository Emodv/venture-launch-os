from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Mapping


QUALITY_WEIGHTS: dict[str, int] = {
    "business_context": 10,
    "search_console": 15,
    "analytics": 15,
    "paid_search": 15,
    "landing_page_mapping": 10,
    "strategy_context": 10,
    "outcome_evidence": 15,
    "time_series_depth": 5,
    "cross_source_joinability": 5,
}


FORBIDDEN_KNOWLEDGE_KEYS = {
    "name",
    "person_name",
    "contact_name",
    "company",
    "company_name",
    "client",
    "client_name",
    "domain",
    "url",
    "website",
    "email",
    "phone",
    "address",
    "customer_id",
    "account_id",
    "property_id",
    "crm_id",
    "message_id",
    "file_id",
    "source_id",
    "password",
    "token",
    "api_key",
    "secret",
    "credential",
}

IDENTIFIER_PATTERNS = (
    re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    re.compile(r"https?://\S+", re.IGNORECASE),
    re.compile(r"\b\d{3}[-. ]?\d{3}[-. ]?\d{4}\b"),
)


@dataclass(frozen=True)
class DataQualityResult:
    total: int
    classification: str
    weighted_components: dict[str, int]


def classify_quality(total: int) -> str:
    if total < 30:
        return "weak"
    if total < 50:
        return "partial"
    if total < 70:
        return "usable"
    if total < 85:
        return "strong"
    return "gold_standard"


def score_data_quality(completeness: Mapping[str, float | int]) -> DataQualityResult:
    """Score historical client evidence from 0-100.

    `completeness` values are normalized between 0 and 1 for each supported
    dimension. Missing dimensions score zero. Values outside 0..1 are clamped.
    The function scores evidence completeness, not campaign success.
    """
    weighted: dict[str, int] = {}
    for key, weight in QUALITY_WEIGHTS.items():
        raw = float(completeness.get(key, 0))
        normalized = max(0.0, min(1.0, raw))
        weighted[key] = round(normalized * weight)

    total = sum(weighted.values())
    return DataQualityResult(
        total=total,
        classification=classify_quality(total),
        weighted_components=weighted,
    )


def benchmark_eligible(
    quality_score: int,
    sample_compatibility: float,
    minimum_quality: int = 70,
    minimum_compatibility: float = 0.65,
) -> bool:
    """Return whether a historical case is safe to use as benchmark evidence."""
    compatibility = max(0.0, min(1.0, sample_compatibility))
    return quality_score >= minimum_quality and compatibility >= minimum_compatibility


def attribution_label(has_direct_join: bool, has_multi_source_support: bool) -> str:
    """Conservative attribution label for cross-source historical evidence."""
    if has_direct_join:
        return "VERIFIED"
    if has_multi_source_support:
        return "STRONGLY_SUPPORTED"
    return "INFERRED"


def _safe_key(key: str) -> bool:
    normalized = key.strip().lower()
    return normalized not in FORBIDDEN_KNOWLEDGE_KEYS and not any(
        term in normalized
        for term in (
            "email",
            "phone",
            "address",
            "password",
            "secret",
            "token",
            "credential",
            "account_id",
            "customer_id",
            "property_id",
            "message_id",
            "file_id",
            "source_id",
        )
    )


def _redact_string(value: str) -> str:
    redacted = value
    for pattern in IDENTIFIER_PATTERNS:
        redacted = pattern.sub("[REDACTED]", redacted)
    return redacted


def sanitize_historical_knowledge(value: Any) -> Any:
    """Remove direct identifiers before historical evidence enters reusable knowledge.

    This is a deterministic guardrail, not a substitute for source authorization or
    human/privacy review. Public/shared knowledge should contain generalized patterns,
    not client identity, contact data, source IDs, credentials, or identifying URLs.
    """
    if isinstance(value, Mapping):
        return {
            str(key): sanitize_historical_knowledge(item)
            for key, item in value.items()
            if _safe_key(str(key))
        }
    if isinstance(value, list):
        return [sanitize_historical_knowledge(item) for item in value]
    if isinstance(value, tuple):
        return tuple(sanitize_historical_knowledge(item) for item in value)
    if isinstance(value, str):
        return _redact_string(value)
    return value


def knowledge_is_privacy_safe(value: Any) -> bool:
    """Return False when reusable knowledge still contains obvious identifiers."""
    if isinstance(value, Mapping):
        for key, item in value.items():
            if not _safe_key(str(key)):
                return False
            if not knowledge_is_privacy_safe(item):
                return False
        return True
    if isinstance(value, (list, tuple)):
        return all(knowledge_is_privacy_safe(item) for item in value)
    if isinstance(value, str):
        return all(pattern.search(value) is None for pattern in IDENTIFIER_PATTERNS)
    return True
