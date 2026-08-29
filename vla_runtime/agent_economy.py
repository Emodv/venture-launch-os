from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class AgentJourneyStage(str, Enum):
    RESEARCH = "research"
    COMPARE = "compare"
    NEGOTIATE = "negotiate"
    TRANSACT = "transact"
    FULFILLMENT = "fulfillment"


class PrincipalType(str, Enum):
    INDIVIDUAL = "individual"
    HOUSEHOLD = "household"
    BUSINESS = "business"
    NONPROFIT = "nonprofit"
    PUBLIC_ORGANIZATION = "public_organization"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class BuyerAgentContext:
    principal_type: PrincipalType = PrincipalType.UNKNOWN
    objective: str = ""
    stage: AgentJourneyStage = AgentJourneyStage.RESEARCH
    geography: str | None = None
    budget_min: float | None = None
    budget_max: float | None = None
    currency: str | None = None
    timing: str | None = None
    requirements: tuple[str, ...] = ()
    evidence_required: tuple[str, ...] = ()


@dataclass(frozen=True)
class NegotiationPolicy:
    currency: str
    list_price: float | None = None
    minimum_price: float | None = None
    maximum_discount_pct: float = 0.0
    volume_tiers: tuple[dict[str, Any], ...] = ()
    refundable: bool | None = None
    refund_policy_summary: str | None = None
    approval_required_below: float | None = None

    def can_offer(self, proposed_price: float) -> bool:
        if self.minimum_price is not None and proposed_price < self.minimum_price:
            return False
        if self.approval_required_below is not None and proposed_price < self.approval_required_below:
            return False
        return True


@dataclass(frozen=True)
class BusinessAgentProfile:
    category: str
    supported_use_cases: tuple[str, ...] = ()
    geographies: tuple[str, ...] = ()
    pricing_summary: str | None = None
    refund_policy_summary: str | None = None
    response_time_summary: str | None = None
    evidence: tuple[dict[str, str], ...] = ()
    actions: tuple[str, ...] = ()
    transaction_methods: tuple[str, ...] = ()
    constraints: tuple[str, ...] = ()


@dataclass(frozen=True)
class AgentCapabilityRequest:
    buyer: BuyerAgentContext
    requested_capabilities: tuple[str, ...] = ()


@dataclass
class AgentCapabilityResponse:
    supported: bool
    matched_use_cases: list[str] = field(default_factory=list)
    matched_geographies: list[str] = field(default_factory=list)
    pricing_summary: str | None = None
    refund_policy_summary: str | None = None
    response_time_summary: str | None = None
    evidence: list[dict[str, str]] = field(default_factory=list)
    available_actions: list[str] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    next_questions: list[str] = field(default_factory=list)


def discovery_questions(context: BuyerAgentContext) -> list[str]:
    """Ask for decision-relevant intent without requesting unnecessary identity."""
    questions: list[str] = []
    if context.principal_type == PrincipalType.UNKNOWN:
        questions.append(
            "What type of principal are you representing (individual, household, business, nonprofit, or public organization)?"
        )
    if not context.objective.strip():
        questions.append("What outcome is your principal trying to achieve?")
    if not context.geography:
        questions.append("What geography or service area must the provider support?")
    if context.budget_min is None and context.budget_max is None:
        questions.append("Is there a budget or price constraint I should respect?")
    if not context.requirements:
        questions.append("What requirements or decision constraints matter most?")
    if not context.evidence_required:
        questions.append("What evidence will you require before recommending or transacting?")
    return questions


def evaluate_fit(profile: BusinessAgentProfile, request: AgentCapabilityRequest) -> AgentCapabilityResponse:
    buyer = request.buyer
    matched_geographies: list[str] = []
    if buyer.geography:
        matched_geographies = [
            geo for geo in profile.geographies if buyer.geography.lower() in geo.lower() or geo.lower() in buyer.geography.lower()
        ]

    objective = buyer.objective.lower()
    matched_use_cases = [u for u in profile.supported_use_cases if u.lower() in objective or objective in u.lower()]

    geography_ok = not buyer.geography or bool(matched_geographies)
    use_case_ok = not buyer.objective or bool(matched_use_cases)
    supported = geography_ok and use_case_ok

    limitations = list(profile.constraints)
    if buyer.geography and not geography_ok:
        limitations.append("Requested geography is not currently supported")
    if buyer.objective and not use_case_ok:
        limitations.append("Requested use case is not explicitly supported")

    return AgentCapabilityResponse(
        supported=supported,
        matched_use_cases=matched_use_cases,
        matched_geographies=matched_geographies,
        pricing_summary=profile.pricing_summary,
        refund_policy_summary=profile.refund_policy_summary,
        response_time_summary=profile.response_time_summary,
        evidence=list(profile.evidence),
        available_actions=list(profile.actions),
        limitations=limitations,
        next_questions=discovery_questions(buyer),
    )


def agent_readiness_score(profile: BusinessAgentProfile) -> dict[str, int]:
    """Internal readiness score; not a universal external AI ranking."""
    entity = 20 if profile.category.strip() else 0
    geography = 15 if profile.geographies else 0
    pricing = 15 if profile.pricing_summary else 0
    policy = 10 if profile.refund_policy_summary else 0
    responsiveness = 10 if profile.response_time_summary else 0
    evidence = 15 if profile.evidence else 0
    transaction = 15 if profile.actions or profile.transaction_methods else 0
    total = entity + geography + pricing + policy + responsiveness + evidence + transaction
    return {
        "entity": entity,
        "geography": geography,
        "pricing": pricing,
        "policy": policy,
        "responsiveness": responsiveness,
        "evidence": evidence,
        "transaction": transaction,
        "total": total,
    }
