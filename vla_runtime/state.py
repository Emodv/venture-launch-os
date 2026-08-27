from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class VentureState(BaseModel):
    venture_id: str = Field(default_factory=lambda: str(uuid4()))
    idea: str
    status: str = "idea"
    created_at: str = Field(default_factory=now_iso)
    updated_at: str = Field(default_factory=now_iso)
    thesis: dict[str, Any] = Field(default_factory=dict)
    icp: dict[str, Any] = Field(default_factory=dict)
    offer: dict[str, Any] = Field(default_factory=dict)
    economics: dict[str, Any] = Field(default_factory=dict)
    gtm: dict[str, Any] = Field(default_factory=dict)
    blockers: list[dict[str, Any]] = Field(default_factory=list)
    current_bottleneck: str | None = None
    top_priorities: list[dict[str, Any]] = Field(default_factory=list)
