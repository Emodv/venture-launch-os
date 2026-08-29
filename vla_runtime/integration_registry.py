from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class IntegrationStatus(str, Enum):
    VERIFIED = "verified"
    CANDIDATE = "candidate"
    BLOCKED = "blocked"
    REJECTED = "rejected"
    UNVERIFIED = "unverified"


@dataclass(frozen=True)
class IntegrationRecord:
    name: str
    source: str
    purpose: str
    status: IntegrationStatus
    notes: str
    license_verified: bool = False
    security_reviewed: bool = False
    pinned_revision: str | None = None


REGISTRY: tuple[IntegrationRecord, ...] = (
    IntegrationRecord(
        "opensoul",
        "https://github.com/iamevandrake/opensoul",
        "Reference architecture for Director/Strategist/Creative/Producer/Growth/Analyst marketing-agent organization and scheduled heartbeats.",
        IntegrationStatus.CANDIDATE,
        "Public repository located. Use as inspiration or adapter only after dependency/security review; do not make VLA state or doctrine depend on it.",
        license_verified=True,
    ),
    IntegrationRecord(
        "openclaw-marketing-skills",
        "https://github.com/davidpc007/openclaw-marketing-skills",
        "Candidate reusable marketing skills and connector patterns across CRO, SEO, paid media, email, content and analytics.",
        IntegrationStatus.CANDIDATE,
        "Public repository located. Skill count/version can change; import only reviewed, non-duplicative capabilities.",
    ),
    IntegrationRecord(
        "SearchAtlas MCP Agent",
        "https://github.com/Search-Atlas-Group/MCP-agent",
        "Candidate omni-channel marketing MCP for SEO/GEO/ads/local/content/digital-PR workflows.",
        IntegrationStatus.CANDIDATE,
        "Public repository located. Tool-count claims must be verified from the pinned revision before relying on them.",
    ),
    IntegrationRecord(
        "AgentNet",
        "https://github.com/oxgeneral/agentnet",
        "Experimental agent discovery/referral network.",
        IntegrationStatus.CANDIDATE,
        "Public repository located. Treat external rankings/credits/reputation as untrusted signals until independently verified.",
    ),
    IntegrationRecord(
        "Forge MCP",
        "https://github.com/pm577/forge-mcp",
        "Candidate portable agent reputation protocol.",
        IntegrationStatus.CANDIDATE,
        "Repository appears in public GitHub indexing, but production use requires direct repository/license/security review and identity-model evaluation.",
    ),
    IntegrationRecord(
        "Merlin",
        "https://github.com/oathgames/Merlin",
        "Proposed autonomous marketing integration from VLA 2.0 specification.",
        IntegrationStatus.UNVERIFIED,
        "Do not integrate until repository identity, license, active maintenance, capabilities and security posture are verified.",
    ),
    IntegrationRecord(
        "growth-agent-mcp",
        "https://github.com/sergeykwon/growth-agent-mcp",
        "Proposed growth playbook MCP from VLA 2.0 specification.",
        IntegrationStatus.UNVERIFIED,
        "Do not rely on claimed playbook counts until repository and revision are verified.",
    ),
    IntegrationRecord(
        "agent-reputation-mcp-server",
        "https://github.com/AiAgentKarl/agent-reputation-mcp-server",
        "Proposed agent reputation source.",
        IntegrationStatus.UNVERIFIED,
        "Author has multiple agent-infrastructure MCP repositories, but this exact repository/capability was not sufficiently verified for integration.",
    ),
    IntegrationRecord(
        "agent-trust",
        "https://github.com/nia-agent-cyber/agent-trust",
        "Proposed trust/attestation source from VLA 2.0 specification.",
        IntegrationStatus.UNVERIFIED,
        "Do not integrate blockchain identity or trust attestations until repository, privacy, custody, legal and revocation semantics are reviewed.",
    ),
)


def approved_integrations() -> tuple[IntegrationRecord, ...]:
    return tuple(item for item in REGISTRY if item.status == IntegrationStatus.VERIFIED)


def integration_candidates() -> tuple[IntegrationRecord, ...]:
    return tuple(item for item in REGISTRY if item.status == IntegrationStatus.CANDIDATE)


def may_execute_third_party(name: str) -> bool:
    """Only fully verified integrations may be enabled for autonomous production execution."""
    for item in REGISTRY:
        if item.name.lower() == name.lower():
            return item.status == IntegrationStatus.VERIFIED and item.security_reviewed and bool(item.pinned_revision)
    return False
