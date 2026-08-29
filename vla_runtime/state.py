from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, Field


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class VentureState(BaseModel):
    venture_id: str = Field(default_factory=lambda: str(uuid4()))
    idea: str
    entry_mode: Literal["greenfield", "existing_business"] = "greenfield"
    website_url: str | None = None
    status: str = "idea"
    created_at: str = Field(default_factory=now_iso)
    updated_at: str = Field(default_factory=now_iso)

    thesis: dict[str, Any] = Field(default_factory=dict)
    icp: dict[str, Any] = Field(default_factory=dict)
    market: dict[str, Any] = Field(default_factory=dict)
    offer: dict[str, Any] = Field(default_factory=dict)
    economics: dict[str, Any] = Field(default_factory=dict)
    assets: dict[str, Any] = Field(default_factory=dict)
    gtm: dict[str, Any] = Field(default_factory=dict)
    operations: dict[str, Any] = Field(default_factory=dict)
    outcomes: dict[str, Any] = Field(default_factory=dict)
    learnings: list[dict[str, Any]] = Field(default_factory=list)

    # Existing-business transformation state.
    public_site_audit: dict[str, Any] = Field(default_factory=dict)
    data_access: dict[str, Any] = Field(default_factory=dict)
    preservation_map: dict[str, Any] = Field(default_factory=dict)
    transformation_strategy: dict[str, Any] = Field(default_factory=dict)
    ai_agent_readiness: dict[str, Any] = Field(default_factory=dict)

    # Cross-venture historical intelligence. Raw client evidence is never stored here.
    historical_benchmark_context: dict[str, Any] = Field(default_factory=dict)
    comparable_case_ids: list[str] = Field(default_factory=list)

    # VLA 2.0 autonomous operating state. These are VLA-owned abstractions and do not
    # depend on a specific third-party agent framework.
    pipeline_kind: str | None = None
    pipeline_phase: str | None = None
    specialist_team: dict[str, Any] = Field(default_factory=dict)
    work_queue: list[dict[str, Any]] = Field(default_factory=list)
    heartbeat_state: dict[str, Any] = Field(default_factory=dict)
    model_routing: dict[str, Any] = Field(default_factory=dict)
    integration_state: dict[str, Any] = Field(default_factory=dict)
    experiments: list[dict[str, Any]] = Field(default_factory=list)
    decision_memory: list[dict[str, Any]] = Field(default_factory=list)
    outcome_memory: list[dict[str, Any]] = Field(default_factory=list)

    blockers: list[dict[str, Any]] = Field(default_factory=list)
    approvals_required: list[dict[str, Any]] = Field(default_factory=list)
    current_bottleneck: str | None = None
    top_priorities: list[dict[str, Any]] = Field(default_factory=list)
    action_log: list[dict[str, Any]] = Field(default_factory=list)

    def mark_updated(self) -> None:
        self.updated_at = now_iso()

    def log_action(self, action: str, status: str, evidence: str | None = None) -> None:
        self.action_log.append(
            {
                "timestamp": now_iso(),
                "action": action,
                "status": status,
                "evidence": evidence,
            }
        )
        self.mark_updated()

    def record_decision(self, decision: dict[str, Any]) -> None:
        self.decision_memory.append({"timestamp": now_iso(), **decision})
        self.mark_updated()

    def record_outcome(self, outcome: dict[str, Any]) -> None:
        self.outcome_memory.append({"timestamp": now_iso(), **outcome})
        self.mark_updated()
