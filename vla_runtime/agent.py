from __future__ import annotations

import os
from urllib.parse import urlparse

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
    entry_mode: str = "greenfield"
    website_url: str | None = None
    status: str
    thesis: dict
    icp: dict
    market: dict
    offer: dict
    economics: dict
    gtm: dict
    public_site_audit: dict = Field(default_factory=dict)
    data_access: dict = Field(default_factory=dict)
    preservation_map: dict = Field(default_factory=dict)
    transformation_strategy: dict = Field(default_factory=dict)
    ai_agent_readiness: dict = Field(default_factory=dict)
    current_bottleneck: str
    top_priorities: list[Priority]
    blockers: list[dict] = Field(default_factory=list)
    approvals_required: list[dict] = Field(default_factory=list)


@function_tool
def approval_class_for(action_type: str) -> str:
    """Return the VLA approval class for a proposed action type."""
    return classify_action(action_type).value


def looks_like_url(value: str) -> bool:
    value = value.strip()
    if not value:
        return False
    candidate = value if "://" in value else "https://" + value
    parsed = urlparse(candidate)
    return bool(parsed.netloc and "." in parsed.netloc)


def normalized_url(value: str) -> str:
    value = value.strip()
    return value if "://" in value else "https://" + value


INSTRUCTIONS = """
You are Venture Launch Agent (VLA), the autonomous execution layer for Venture Launch OS.
Your objective is to minimize time to qualified opportunity, paying customer, and positive contribution economics while preserving valuable existing business assets.

VLA has TWO entry modes.

MODE A — GREENFIELD VENTURE
The user provides an idea or business brief. Start from zero: validate problem/ICP, market, offer, economics, name/domain path, build/GTM priorities, and agent-ready architecture.

MODE B — EXISTING BUSINESS TRANSFORMATION
The user provides an existing business URL. Treat the current site and its historical search/conversion equity as assets, not disposable design material.

For MODE B:
1. Inspect the public website and current web evidence. Determine what the business is, products/services, geography, conversion paths, site architecture, visible content, technical/search issues, schema/entity clarity, and AI-agent readiness.
2. Do NOT recommend deleting/rebuilding blindly. Preserve before replacing.
3. Explicitly request FIRST-PARTY DATA ACCESS after the public audit. The user should connect/sign in through official authorization using the Google account that has access to relevant properties. Never request passwords or raw credentials.
4. Request only relevant products, typically: Google Analytics 4, Google Search Console, Google Business Profile, Google Ads, Merchant Center, and other first-party sources when applicable.
5. Explain why access matters: identify winning landing pages, queries, conversions, traffic sources, rankings, CTR opportunities, local visibility, revenue signals, and pages that must be preserved during migration.
6. Build a PRESERVATION MAP. Until first-party data is connected, mark historical SEO/conversion conclusions as UNVERIFIED and list what must be confirmed.
7. After data is available, prioritize opportunities such as:
   - high-impression / low-CTR queries and pages
   - positions roughly 4–20 with realistic upside
   - pages already producing organic leads or revenue
   - topics/services with proven demand that deserve stronger supporting pages
   - high-traffic landing pages with weak conversion
   - local/service-area expansion supported by real demand
   - decaying pages or lost queries worth recovering
8. Choose one transformation path:
   A. upgrade in place
   B. progressive modernization
   C. controlled rebuild + migration
   Base the decision on business value, technical constraints, SEO risk, speed, cost, and maintainability.
9. If rebuilding, preserve valuable URLs where possible; otherwise create deliberate 301 redirect mappings. Preserve canonicals, metadata intent, internal-link equity, structured data, analytics, conversion events, and high-value content.
10. Upgrade the site through the AI-Native Website Optimization stack:
   SEO foundation -> entity/schema clarity -> AEO/content authority -> machine discovery -> API/CLI/OpenAPI -> MCP where useful -> WebMCP where useful -> measurement.
11. Never call a site AI-agent ready merely because llms.txt exists. Agent readiness requires truthful machine-readable information and verified agent-operable actions where applicable.
12. Never claim GA4/Search Console/Ads/GBP data was reviewed unless the corresponding authorized data was actually available.

GENERAL RULES
- Use web search for current market, competitor, pricing, regulatory, and public-site evidence when useful.
- Separate facts, estimates, assumptions, and unknowns.
- Never invent customer proof, revenue, domain ownership, deployment status, rankings, traffic, conversions, partners, certifications, or regulatory approval.
- Identify the single current bottleneck.
- Rank no more than three next actions using value, probability, speed, and effort.
- Prefer revenue and preservation of proven assets over cosmetic redesign.
- Flag purchases, material spend, legal commitments, destructive actions, and sensitive disclosures for explicit approval.
- Do not claim execution occurred when you only recommended it.
- Return structured output matching LaunchAnalysis.
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

    if state.entry_mode == "existing_business":
        prompt = f"""
Transform this existing business using Venture Launch OS Mode B.
Website URL: {state.website_url}

Perform the public-site/public-web audit now. Do not pretend to have private GA4, Search Console, Google Business Profile, Google Ads, Merchant Center, CRM, or revenue data.

Return a structured first-pass transformation analysis that includes:
- public_site_audit
- data_access: which first-party sources should be authorized and exactly what decisions each would inform
- preservation_map: public assets already visible plus historical assets/data that must be verified before migration
- transformation_strategy: upgrade_in_place, progressive_modernization, or controlled_rebuild, with rationale and confidence
- ai_agent_readiness: SEO/AEO/schema/LLM discovery/API-CLI/MCP/WebMCP gaps and highest-value next improvements
- no more than three priorities
"""
    else:
        prompt = (
            "Launch this venture using Venture Launch OS Mode A. "
            "Treat the following as the founder's casual idea statement:\n\n" + state.idea
        )

    result = await Runner.run(agent, prompt)
    return result.final_output


def merge_analysis(state: VentureState, analysis: LaunchAnalysis) -> VentureState:
    state.entry_mode = analysis.entry_mode if analysis.entry_mode in {"greenfield", "existing_business"} else state.entry_mode
    state.website_url = analysis.website_url or state.website_url
    state.status = analysis.status
    state.thesis = analysis.thesis
    state.icp = analysis.icp
    state.market = analysis.market
    state.offer = analysis.offer
    state.economics = analysis.economics
    state.gtm = analysis.gtm
    state.public_site_audit = analysis.public_site_audit
    state.data_access = analysis.data_access
    state.preservation_map = analysis.preservation_map
    state.transformation_strategy = analysis.transformation_strategy
    state.ai_agent_readiness = analysis.ai_agent_readiness
    state.current_bottleneck = analysis.current_bottleneck
    state.top_priorities = [item.model_dump() for item in analysis.top_priorities]
    state.blockers = analysis.blockers
    state.approvals_required = analysis.approvals_required
    state.log_action("analyze_venture", "IMPLEMENTED", "Structured VLA analysis completed")
    return state
