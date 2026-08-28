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
