from __future__ import annotations

import os

from agents import Agent, Runner, WebSearchTool, function_tool
from pydantic import BaseModel, Field

from approvals import classify_action
from state import VentureState


class Priority(BaseModel):
    action: str
    value: int = Field(ge=1, le=10)
    probability: int = Field(ge=1, le=10)
    speed: int = Field(ge=1, le=10)
    effort: int = Field(ge=1, le=10)
    reason: str


class LaunchAnalysis(BaseModel):
    status: str
    thesis: dict
    icp: dict
    market: dict
    offer: dict
    economics: dict
    gtm: dict
    current_bottleneck: str
    top_priorities: list[Priority]
    blockers: list[dict] = Field(default_factory=list)
    approvals_required: list[dict] = Field(default_factory=list)


@function_tool
def approval_class_for(action_type: str) -> str:
    """Return the VLA approval class for a proposed action type."""
    return classify_action(action_type).value


INSTRUCTIONS = """
You are Venture Launch Agent (VLA), the autonomous execution layer for Venture Launch OS.
Your objective is to minimize time from idea to first qualified opportunity, first paying customer, and positive contribution economics.

For each new idea:
1. Understand the problem, customer, alternatives, geography, demand, business model, acquisition path, fulfillment path, and biggest risk.
2. Use web search for current market, competitor, pricing, and regulatory evidence when useful.
3. Define a narrow initial ICP and a concrete offer.
4. Separate facts, estimates, assumptions, and unknowns. Never invent customer proof, revenue, domain ownership, deployment status, partnerships, or regulatory approval.
5. Identify the single current bottleneck.
6. Rank no more than three next actions using value, probability, speed, and effort.
7. Prefer first-revenue experiments over cosmetic work.
8. Flag purchases, material spend, legal commitments, destructive actions, and sensitive disclosures for explicit approval.
9. Do not claim execution occurred when you only recommended it.
10. Return structured output matching LaunchAnalysis.

The first run is discovery and GTM prioritization. Connected side-effect tools are added incrementally after this core loop is proven.
"""


def build_agent() -> Agent:
    return Agent(
        name="Venture Launch Agent",
        instructions=INSTRUCTIONS,
        model=os.getenv("VLA_MODEL", "gpt-5.6"),
        tools=[WebSearchTool(search_context_size="medium"), approval_class_for],
        output_type=LaunchAnalysis,
    )


async def analyze_venture(state: VentureState) -> LaunchAnalysis:
    agent = build_agent()
    prompt = (
        "Launch this venture using Venture Launch OS. "
        "Treat the following as the founder's casual idea statement:\n\n"
        + state.idea
    )
    result = await Runner.run(agent, prompt)
    return result.final_output


def merge_analysis(state: VentureState, analysis: LaunchAnalysis) -> VentureState:
    state.status = analysis.status
    state.thesis = analysis.thesis
    state.icp = analysis.icp
    state.market = analysis.market
    state.offer = analysis.offer
    state.economics = analysis.economics
    state.gtm = analysis.gtm
    state.current_bottleneck = analysis.current_bottleneck
    state.top_priorities = [item.model_dump() for item in analysis.top_priorities]
    state.blockers = analysis.blockers
    state.approvals_required = analysis.approvals_required
    state.mark_updated()
    return state
