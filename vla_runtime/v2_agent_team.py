from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class AgentRole(str, Enum):
    DIRECTOR = "director"
    STRATEGIST = "strategist"
    PRODUCER = "producer"
    GROWTH = "growth_marketer"
    CREATIVE = "creative"
    ANALYST = "analyst"
    OPERATIONS = "operations"


class WorkStatus(str, Enum):
    QUEUED = "queued"
    READY = "ready"
    RUNNING = "running"
    BLOCKED = "blocked"
    APPROVAL_REQUIRED = "approval_required"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass(frozen=True)
class AgentSpec:
    role: AgentRole
    mission: str
    capabilities: tuple[str, ...]
    default_cost_tier: str = "standard"


DEFAULT_TEAM: dict[AgentRole, AgentSpec] = {
    AgentRole.DIRECTOR: AgentSpec(
        AgentRole.DIRECTOR,
        "Own business outcome, coordinate specialists, allocate budget, and select the highest-value next action.",
        ("strategy", "prioritization", "delegation", "governance", "budget_allocation", "verification"),
        "frontier",
    ),
    AgentRole.STRATEGIST: AgentSpec(
        AgentRole.STRATEGIST,
        "Research the market, audience, competitors, offer, positioning, and business model.",
        ("market_research", "audience_intelligence", "icp", "competitive_analysis", "offer", "pricing", "unit_economics"),
    ),
    AgentRole.PRODUCER: AgentSpec(
        AgentRole.PRODUCER,
        "Turn strategy into publishable content, pages, campaigns, and reusable business assets.",
        ("content", "landing_pages", "editorial_calendar", "publishing", "content_operations"),
    ),
    AgentRole.GROWTH: AgentSpec(
        AgentRole.GROWTH,
        "Own acquisition and discovery across SEO, AEO, GEO, AAO, paid media, email, and growth experiments.",
        ("seo", "aeo", "geo", "aao", "ppc", "email", "social", "cro", "experimentation"),
    ),
    AgentRole.CREATIVE: AgentSpec(
        AgentRole.CREATIVE,
        "Own brand, messaging, visual direction, ad concepts, and conversion-oriented creative.",
        ("brand", "messaging", "copy", "creative_direction", "ad_creative"),
    ),
    AgentRole.ANALYST: AgentSpec(
        AgentRole.ANALYST,
        "Measure source-to-revenue performance, diagnose bottlenecks, and turn evidence into decisions.",
        ("analytics", "attribution", "roi", "funnel_analysis", "benchmarking", "experiment_analysis"),
        "cheap_listener",
    ),
    AgentRole.OPERATIONS: AgentSpec(
        AgentRole.OPERATIONS,
        "Execute approved operational changes, maintain integrations, route leads, and verify completion.",
        ("crm", "integrations", "deployment", "lead_routing", "payments", "fulfillment", "qa"),
    ),
}


@dataclass
class WorkItem:
    work_id: str
    title: str
    owner: AgentRole
    status: WorkStatus = WorkStatus.QUEUED
    value: int = 1
    probability: int = 1
    speed: int = 1
    effort: int = 1
    approval_class: str = "A"
    depends_on: tuple[str, ...] = ()
    evidence: list[str] = field(default_factory=list)
    result: dict[str, Any] = field(default_factory=dict)

    @property
    def priority_score(self) -> float:
        # Higher speed means faster time-to-impact. Never divide by speed.
        return (self.value * self.probability * self.speed) / max(self.effort, 1)


def ready_work(queue: list[WorkItem]) -> list[WorkItem]:
    completed = {item.work_id for item in queue if item.status == WorkStatus.COMPLETED}
    ready: list[WorkItem] = []
    for item in queue:
        if item.status not in {WorkStatus.QUEUED, WorkStatus.READY}:
            continue
        if all(dep in completed for dep in item.depends_on):
            ready.append(item)
    return sorted(ready, key=lambda item: item.priority_score, reverse=True)


def heartbeat_assignments(queue: list[WorkItem]) -> dict[AgentRole, list[WorkItem]]:
    """Return work specialists may execute on this heartbeat.

    Class C work is surfaced to the Director as approval-required rather than executed.
    The heartbeat itself is deterministic; actual execution happens through governed tools.
    """
    assignments: dict[AgentRole, list[WorkItem]] = {role: [] for role in AgentRole}
    for item in ready_work(queue):
        if item.approval_class.upper() == "C":
            item.status = WorkStatus.APPROVAL_REQUIRED
            assignments[AgentRole.DIRECTOR].append(item)
        else:
            item.status = WorkStatus.READY
            assignments[item.owner].append(item)
    return assignments
