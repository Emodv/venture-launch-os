from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from v2_agent_team import AgentRole


class PipelineKind(str, Enum):
    TRANSFORM = "existing_business_transformation"
    LAUNCH = "greenfield_launch"


@dataclass(frozen=True)
class PipelinePhase:
    phase_id: str
    title: str
    owner: AgentRole
    exit_criteria: tuple[str, ...]
    approval_sensitive: bool = False


TRANSFORMATION_PIPELINE: tuple[PipelinePhase, ...] = (
    PipelinePhase(
        "audit",
        "Deep audit and preservation map",
        AgentRole.STRATEGIST,
        (
            "public business surface inventoried",
            "current conversion paths mapped",
            "first-party data access requirements identified",
            "preservation map created",
        ),
    ),
    PipelinePhase(
        "modernize",
        "AI-agent-era modernization",
        AgentRole.GROWTH,
        (
            "SEO/AEO/GEO/AAO gaps prioritized",
            "entity, geography, pricing, policy and evidence surfaces defined",
            "upgrade vs progressive modernization vs controlled rebuild selected",
            "migration protections defined when applicable",
        ),
    ),
    PipelinePhase(
        "agent_commerce",
        "Agent commerce enablement",
        AgentRole.OPERATIONS,
        (
            "A2A discovery/evaluation interface available",
            "commercial authority policy defined",
            "negotiation actions bounded",
            "transaction path identified or explicitly marked not applicable",
        ),
        approval_sensitive=True,
    ),
    PipelinePhase(
        "operate",
        "Continuous growth operation",
        AgentRole.DIRECTOR,
        (
            "measurement loop active",
            "work queue prioritized",
            "experiments recorded",
            "verified outcomes feed privacy-safe learning",
        ),
    ),
)


GREENFIELD_PIPELINE: tuple[PipelinePhase, ...] = (
    PipelinePhase(
        "validate",
        "Ideation, audience and economics validation",
        AgentRole.STRATEGIST,
        (
            "priority audience defined",
            "problem and alternatives assessed",
            "offer hypothesis defined",
            "unit economics assumptions recorded",
        ),
    ),
    PipelinePhase(
        "infrastructure",
        "Business infrastructure",
        AgentRole.OPERATIONS,
        (
            "brand and conversion surface specified",
            "Venture State initialized",
            "analytics/CRM/payment requirements defined",
            "deployment plan defined",
        ),
        approval_sensitive=True,
    ),
    PipelinePhase(
        "launch_prep",
        "Discovery and launch preparation",
        AgentRole.GROWTH,
        (
            "SEO/AEO/GEO/AAO foundation defined",
            "priority acquisition channel selected",
            "content and landing-page plan aligned to audience intent",
            "measurement events defined",
        ),
    ),
    PipelinePhase(
        "acquire",
        "Launch and first-customer acquisition",
        AgentRole.DIRECTOR,
        (
            "credible acquisition surface live or ready",
            "first acquisition experiment initiated when authorized",
            "lead routing/follow-up path defined",
            "qualified opportunity and customer outcomes tracked separately",
        ),
        approval_sensitive=True,
    ),
    PipelinePhase(
        "learn",
        "Learning and iteration",
        AgentRole.ANALYST,
        (
            "experiment result recorded",
            "current bottleneck updated",
            "next actions reprioritized",
            "privacy-safe reusable learning extracted when supported",
        ),
    ),
)


def pipeline_for(kind: PipelineKind) -> tuple[PipelinePhase, ...]:
    if kind == PipelineKind.TRANSFORM:
        return TRANSFORMATION_PIPELINE
    return GREENFIELD_PIPELINE
