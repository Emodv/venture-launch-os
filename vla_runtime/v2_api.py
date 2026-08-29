from __future__ import annotations

import os
from dataclasses import asdict

from fastapi import APIRouter, HTTPException

from integration_registry import REGISTRY, approved_integrations, integration_candidates
from persistence import load_state, save_state
from state import VentureState, now_iso
from v2_agent_team import DEFAULT_TEAM, AgentRole, WorkItem, WorkStatus, heartbeat_assignments
from v2_pipelines import PipelineKind, pipeline_for

router = APIRouter(prefix="/v2", tags=["vla-2"])


def bootstrap_v2_state(state: VentureState) -> VentureState:
    kind = PipelineKind.TRANSFORM if state.entry_mode == "existing_business" else PipelineKind.LAUNCH
    phases = pipeline_for(kind)
    state.pipeline_kind = kind.value
    if not state.pipeline_phase:
        state.pipeline_phase = phases[0].phase_id
    if not state.specialist_team:
        state.specialist_team = {
            role.value: {
                "mission": spec.mission,
                "capabilities": list(spec.capabilities),
                "default_cost_tier": spec.default_cost_tier,
            }
            for role, spec in DEFAULT_TEAM.items()
        }
    state.integration_state = {
        "verified_count": len(approved_integrations()),
        "candidate_count": len(integration_candidates()),
        "policy": "third-party code may execute autonomously only after license/security review and revision pinning",
    }
    state.mark_updated()
    return state


def _work_item(raw: dict) -> WorkItem:
    return WorkItem(
        work_id=str(raw["work_id"]),
        title=str(raw["title"]),
        owner=AgentRole(str(raw["owner"])),
        status=WorkStatus(str(raw.get("status", "queued"))),
        value=int(raw.get("value", 1)),
        probability=int(raw.get("probability", 1)),
        speed=int(raw.get("speed", 1)),
        effort=int(raw.get("effort", 1)),
        approval_class=str(raw.get("approval_class", "A")),
        depends_on=tuple(raw.get("depends_on", [])),
        evidence=list(raw.get("evidence", [])),
        result=dict(raw.get("result", {})),
    )


@router.get("/team")
def team() -> dict:
    return {
        "director": AgentRole.DIRECTOR.value,
        "agents": {
            role.value: {
                "mission": spec.mission,
                "capabilities": list(spec.capabilities),
                "default_cost_tier": spec.default_cost_tier,
            }
            for role, spec in DEFAULT_TEAM.items()
        },
    }


@router.get("/pipelines")
def pipelines() -> dict:
    return {
        kind.value: [
            {
                "phase_id": phase.phase_id,
                "title": phase.title,
                "owner": phase.owner.value,
                "exit_criteria": list(phase.exit_criteria),
                "approval_sensitive": phase.approval_sensitive,
            }
            for phase in pipeline_for(kind)
        ]
        for kind in PipelineKind
    }


@router.get("/integrations")
def integrations() -> dict:
    return {
        "policy": "VLA owns the architecture. Third-party projects are adapters/capability sources, never the source of Venture State or doctrine.",
        "integrations": [
            {
                "name": item.name,
                "source": item.source,
                "purpose": item.purpose,
                "status": item.status.value,
                "license_verified": item.license_verified,
                "security_reviewed": item.security_reviewed,
                "pinned_revision": item.pinned_revision,
                "notes": item.notes,
            }
            for item in REGISTRY
        ],
    }


@router.post("/ventures/{venture_id}/heartbeat")
def heartbeat(venture_id: str) -> dict:
    state_dir = os.getenv("VLA_STATE_DIR", "./data/ventures")
    try:
        state = load_state(venture_id, state_dir)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail="venture not found") from exc

    bootstrap_v2_state(state)
    queue = [_work_item(item) for item in state.work_queue]
    assignments = heartbeat_assignments(queue)
    state.work_queue = [asdict(item) for item in queue]
    state.heartbeat_state = {
        "last_heartbeat": now_iso(),
        "assignments": {
            role.value: [item.work_id for item in items]
            for role, items in assignments.items()
            if items
        },
    }
    for item in assignments[AgentRole.DIRECTOR]:
        if item.status == WorkStatus.APPROVAL_REQUIRED:
            state.approvals_required.append(
                {"work_id": item.work_id, "title": item.title, "approval_class": item.approval_class}
            )
    state.log_action("v2_heartbeat", "IMPLEMENTED", "Work queue evaluated and assignments updated")
    save_state(state, state_dir)
    return state.heartbeat_state
