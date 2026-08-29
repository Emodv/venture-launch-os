from __future__ import annotations

import argparse
import asyncio
import json
import os
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from agent import analyze_venture, looks_like_url, merge_analysis, normalized_url
from agent_economy import (
    AgentCapabilityRequest,
    AgentJourneyStage,
    BusinessAgentProfile,
    BuyerAgentContext,
    NegotiationPolicy,
    PrincipalType,
    VLA_AGENT_IDENTITY,
    agent_readiness_score,
    discovery_questions,
    evaluate_fit,
)
from model_gateway import provider_status
from persistence import load_state, save_state
from state import VentureState

app = FastAPI(title="Venture Launch Agent", version="0.3.0")


class LaunchRequest(BaseModel):
    input: str = Field(min_length=2, description="Plain-English venture idea or an existing business URL")
    mode: Literal["auto", "greenfield", "existing_business"] = "auto"


class ExistingBusinessRequest(BaseModel):
    url: str = Field(min_length=4)


class BuyerContextRequest(BaseModel):
    principal_type: PrincipalType = PrincipalType.UNKNOWN
    objective: str = ""
    stage: AgentJourneyStage = AgentJourneyStage.RESEARCH
    geography: str | None = None
    budget_min: float | None = None
    budget_max: float | None = None
    currency: str | None = None
    timing: str | None = None
    requirements: list[str] = Field(default_factory=list)
    evidence_required: list[str] = Field(default_factory=list)

    def to_domain(self) -> BuyerAgentContext:
        return BuyerAgentContext(
            principal_type=self.principal_type,
            objective=self.objective,
            stage=self.stage,
            geography=self.geography,
            budget_min=self.budget_min,
            budget_max=self.budget_max,
            currency=self.currency,
            timing=self.timing,
            requirements=tuple(self.requirements),
            evidence_required=tuple(self.evidence_required),
        )


class BusinessProfileRequest(BaseModel):
    category: str
    supported_use_cases: list[str] = Field(default_factory=list)
    geographies: list[str] = Field(default_factory=list)
    pricing_summary: str | None = None
    refund_policy_summary: str | None = None
    response_time_summary: str | None = None
    evidence: list[dict[str, str]] = Field(default_factory=list)
    actions: list[str] = Field(default_factory=list)
    transaction_methods: list[str] = Field(default_factory=list)
    constraints: list[str] = Field(default_factory=list)

    def to_domain(self) -> BusinessAgentProfile:
        return BusinessAgentProfile(
            category=self.category,
            supported_use_cases=tuple(self.supported_use_cases),
            geographies=tuple(self.geographies),
            pricing_summary=self.pricing_summary,
            refund_policy_summary=self.refund_policy_summary,
            response_time_summary=self.response_time_summary,
            evidence=tuple(self.evidence),
            actions=tuple(self.actions),
            transaction_methods=tuple(self.transaction_methods),
            constraints=tuple(self.constraints),
        )


class AgentFitRequest(BaseModel):
    buyer: BuyerContextRequest
    business: BusinessProfileRequest
    requested_capabilities: list[str] = Field(default_factory=list)


class NegotiationRequest(BaseModel):
    proposed_price: float = Field(gt=0)
    currency: str
    list_price: float | None = Field(default=None, gt=0)
    minimum_price: float | None = Field(default=None, gt=0)
    maximum_discount_pct: float = Field(default=0, ge=0, le=100)
    approval_required_below: float | None = Field(default=None, gt=0)
    refundable: bool | None = None
    refund_policy_summary: str | None = None


def state_from_request(request: LaunchRequest) -> VentureState:
    mode = request.mode
    if mode == "auto":
        mode = "existing_business" if looks_like_url(request.input) else "greenfield"

    if mode == "existing_business":
        url = normalized_url(request.input)
        return VentureState(
            idea=f"Transform existing business website: {url}",
            entry_mode="existing_business",
            website_url=url,
            status="audit_pending",
        )

    return VentureState(idea=request.input, entry_mode="greenfield", status="discovery")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "vla", "version": "0.3.0"}


@app.get("/agent")
def agent_identity() -> dict:
    return {
        **VLA_AGENT_IDENTITY,
        "version": "0.3.0",
        "journey_stages": [stage.value for stage in AgentJourneyStage],
        "providers": provider_status(),
    }


@app.post("/agent/discover")
def agent_discover(request: BuyerContextRequest) -> dict:
    context = request.to_domain()
    return {
        "stage": context.stage.value,
        "questions": discovery_questions(context),
        "privacy_rule": "Ask for commercial intent and constraints, not unnecessary principal identity.",
    }


@app.post("/agent/evaluate")
def agent_evaluate(request: AgentFitRequest) -> dict:
    profile = request.business.to_domain()
    capability_request = AgentCapabilityRequest(
        buyer=request.buyer.to_domain(),
        requested_capabilities=tuple(request.requested_capabilities),
    )
    response = evaluate_fit(profile, capability_request)
    return {
        "supported": response.supported,
        "matched_use_cases": response.matched_use_cases,
        "matched_geographies": response.matched_geographies,
        "pricing_summary": response.pricing_summary,
        "refund_policy_summary": response.refund_policy_summary,
        "response_time_summary": response.response_time_summary,
        "evidence": response.evidence,
        "available_actions": response.available_actions,
        "limitations": response.limitations,
        "next_questions": response.next_questions,
        "agent_readiness": agent_readiness_score(profile),
    }


@app.post("/agent/negotiate")
def agent_negotiate(request: NegotiationRequest) -> dict:
    policy = NegotiationPolicy(
        currency=request.currency,
        list_price=request.list_price,
        minimum_price=request.minimum_price,
        maximum_discount_pct=request.maximum_discount_pct,
        refundable=request.refundable,
        refund_policy_summary=request.refund_policy_summary,
        approval_required_below=request.approval_required_below,
    )
    decision = policy.decision(request.proposed_price)
    return {
        "decision": decision.value,
        "proposed_price": request.proposed_price,
        "currency": request.currency,
        "refund_policy_summary": request.refund_policy_summary,
        "rule": "VLA may negotiate only inside explicit business authority; otherwise escalate.",
    }


@app.post("/ventures")
async def create_venture(request: LaunchRequest) -> dict:
    state = state_from_request(request)
    analysis = await analyze_venture(state)
    merged = merge_analysis(state, analysis)
    save_state(merged, os.getenv("VLA_STATE_DIR", "./data/ventures"))
    return merged.model_dump()


@app.post("/transform")
async def transform_existing_business(request: ExistingBusinessRequest) -> dict:
    url = normalized_url(request.url)
    state = VentureState(
        idea=f"Transform existing business website: {url}",
        entry_mode="existing_business",
        website_url=url,
        status="audit_pending",
    )
    analysis = await analyze_venture(state)
    merged = merge_analysis(state, analysis)
    save_state(merged, os.getenv("VLA_STATE_DIR", "./data/ventures"))
    return merged.model_dump()


@app.get("/ventures/{venture_id}")
def get_venture(venture_id: str) -> dict:
    try:
        state = load_state(venture_id, os.getenv("VLA_STATE_DIR", "./data/ventures"))
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail="venture not found") from exc
    return state.model_dump()


@app.post("/ventures/{venture_id}/resume")
async def resume_venture(venture_id: str) -> dict:
    try:
        state = load_state(venture_id, os.getenv("VLA_STATE_DIR", "./data/ventures"))
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail="venture not found") from exc
    analysis = await analyze_venture(state)
    merged = merge_analysis(state, analysis)
    save_state(merged, os.getenv("VLA_STATE_DIR", "./data/ventures"))
    return merged.model_dump()


async def run_cli(value: str, mode: str = "auto") -> None:
    request = LaunchRequest(input=value, mode=mode)
    state = state_from_request(request)
    analysis = await analyze_venture(state)
    merged = merge_analysis(state, analysis)
    path = save_state(merged, os.getenv("VLA_STATE_DIR", "./data/ventures"))
    print(json.dumps({"venture_id": merged.venture_id, "state_path": path, "state": merged.model_dump()}, indent=2))


def cli() -> None:
    parser = argparse.ArgumentParser(description="Venture Launch Agent v0.3")
    parser.add_argument("input", help="Plain-English business idea OR existing business URL")
    parser.add_argument(
        "--mode",
        choices=["auto", "greenfield", "existing_business"],
        default="auto",
        help="Entry mode. Auto treats URL-like inputs as existing businesses.",
    )
    args = parser.parse_args()
    asyncio.run(run_cli(args.input, args.mode))


if __name__ == "__main__":
    if os.getenv("PORT"):
        import uvicorn

        uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ["PORT"]))
    else:
        cli()
