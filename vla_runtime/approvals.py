from __future__ import annotations

from enum import StrEnum


class ApprovalClass(StrEnum):
    AUTONOMOUS = "AUTONOMOUS"
    PREAUTHORIZED = "PREAUTHORIZED"
    EXPLICIT_APPROVAL = "EXPLICIT_APPROVAL"


EXPLICIT_ACTIONS = {
    "purchase",
    "material_spend",
    "sign_agreement",
    "legal_commitment",
    "destructive_action",
    "sensitive_disclosure",
}

PREAUTHORIZED_ACTIONS = {
    "publish_content",
    "deploy_code",
    "send_outreach",
    "routine_followup",
    "campaign_change_within_budget",
}


def classify_action(action_type: str) -> ApprovalClass:
    if action_type in EXPLICIT_ACTIONS:
        return ApprovalClass.EXPLICIT_APPROVAL
    if action_type in PREAUTHORIZED_ACTIONS:
        return ApprovalClass.PREAUTHORIZED
    return ApprovalClass.AUTONOMOUS


def may_execute(action_type: str, preauthorized: set[str] | None = None) -> bool:
    classification = classify_action(action_type)
    if classification == ApprovalClass.AUTONOMOUS:
        return True
    if classification == ApprovalClass.PREAUTHORIZED:
        return action_type in (preauthorized or set())
    return False
