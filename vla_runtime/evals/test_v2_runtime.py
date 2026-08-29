from integration_registry import IntegrationStatus, REGISTRY, may_execute_third_party
from main import LaunchRequest, state_from_request
from v2_agent_team import AgentRole, WorkItem, WorkStatus, heartbeat_assignments
from v2_api import bootstrap_v2_state
from v2_pipelines import PipelineKind, pipeline_for


def test_greenfield_bootstraps_v2_team_and_pipeline() -> None:
    state = state_from_request(LaunchRequest(input="A new service business"))
    assert state.pipeline_kind == PipelineKind.LAUNCH.value
    assert state.pipeline_phase == "validate"
    assert "director" in state.specialist_team
    assert "growth_marketer" in state.specialist_team


def test_existing_business_uses_transformation_pipeline() -> None:
    state = state_from_request(LaunchRequest(input="https://example.com"))
    assert state.pipeline_kind == PipelineKind.TRANSFORM.value
    assert state.pipeline_phase == "audit"
    assert pipeline_for(PipelineKind.TRANSFORM)[0].owner == AgentRole.STRATEGIST


def test_heartbeat_routes_class_c_to_director_for_approval() -> None:
    queue = [
        WorkItem(
            work_id="safe",
            title="Audit landing page",
            owner=AgentRole.GROWTH,
            value=7,
            probability=8,
            speed=8,
            effort=2,
            approval_class="A",
        ),
        WorkItem(
            work_id="spend",
            title="Increase ad spend",
            owner=AgentRole.GROWTH,
            value=10,
            probability=7,
            speed=7,
            effort=2,
            approval_class="C",
        ),
    ]
    assignments = heartbeat_assignments(queue)
    assert queue[0].status == WorkStatus.READY
    assert queue[1].status == WorkStatus.APPROVAL_REQUIRED
    assert assignments[AgentRole.GROWTH][0].work_id == "safe"
    assert assignments[AgentRole.DIRECTOR][0].work_id == "spend"


def test_priority_score_rewards_speed_not_slowness() -> None:
    fast = WorkItem("fast", "fast", AgentRole.ANALYST, value=5, probability=5, speed=9, effort=2)
    slow = WorkItem("slow", "slow", AgentRole.ANALYST, value=5, probability=5, speed=2, effort=2)
    assert fast.priority_score > slow.priority_score


def test_third_party_code_is_not_auto_trusted() -> None:
    assert REGISTRY
    assert all(item.status != IntegrationStatus.VERIFIED or item.security_reviewed for item in REGISTRY)
    assert not may_execute_third_party("opensoul")
    assert not may_execute_third_party("Merlin")


def test_bootstrap_preserves_existing_venture_fields() -> None:
    state = state_from_request(LaunchRequest(input="A venture"))
    state.thesis = {"keep": "this"}
    state = bootstrap_v2_state(state)
    assert state.thesis == {"keep": "this"}
