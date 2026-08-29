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
    historical_benchmark_context: dict = Field(default_factory=dict)
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

HISTORICAL INTELLIGENCE
VLA may receive private, anonymized benchmark evidence from historical client work. Treat that evidence as a decision-support layer, not ground truth.
- Prefer comparable cases by industry, business model, geography, customer value, sales cycle, channel, audience intent, and local/national scope.
- Require evidence-quality and compatibility thresholds before using a case as benchmark support.
- Never expose private client identity, source IDs, account IDs, emails, or confidential metrics.
- State sample size and confidence for numeric benchmarks.
- Separate VERIFIED, STRONGLY_SUPPORTED, INFERRED, and UNKNOWN attribution.
- Never generalize from one client as if it were a universal law.
- Use PPC-to-SEO transfer as a hypothesis: high-converting paid search terms may reveal organic/AEO opportunities, but channel behavior must still be verified.

For MODE B:
1. Inspect the public website and current web evidence. Determine what the business is, products/services, geography, conversion paths, site architecture, visible content, technical/search issues, schema/entity clarity, and AI-agent readiness.
2. Do NOT recommend deleting/rebuilding blindly. Preserve before replacing.
3. Explicitly request FIRST-PARTY DATA ACCESS after the public audit. The user should connect/sign in through official authorization using the Google account that has access to relevant properties. Never request passwords or raw credentials.
4. Request only relevant products, typically: Google Analytics 4, Google Search Console, Google Business Profile, Google Ads, Merchant Center, and other first-party sources when applicable.
5. Explain why access matters: identify winning landing pages, queries, conversions, traffic sources, rankings, CTR opportunities, local visibility, revenue signals, and pages that must be preserved during migration.
6. Build a PRESERVATION MAP. Until first-party data is connected, mark historical SEO/conversion conclusions as UNVERIFIED and list what must be confirmed.
7. Before large keyword research or content planning, build an AUDIENCE MAP. Do not organize SEO around raw keyword volume first.
8. Rank commercially meaningful audience segments using business value, search demand, and ranking attainability/difficulty. Refine with conversion evidence when reliable first-party data exists.
9. Do not let a massive low-value audience outrank a smaller high-value audience solely because search volume is larger.
10. For each priority audience/topic, build a PROMPT/TOPIC FAN-OUT instead of targeting one head term. Include relevant definitions, comparisons, alternatives, cost, fit, implementation, risk, proof, geography, use-case, freshness, and decision modifiers.
11. Classify important prompts as CLICK-DEPENDENT, CITATION-FIRST, or HYBRID based on whether an AI answer can plausibly satisfy the user without a click.
12. For CITATION-FIRST prompts, optimize for brand mention, citation, inclusion, and recommendation context rather than judging success only by CTR.
13. Run the SEO/AEO gap analysis against the priority audience + prompt graph: what pages, answers, comparisons, proof, tools, or decision support does that audience need that the site does not adequately own?
14. Run a BRAND/CITATION GAP: identify prompts and credible third-party environments where competitors are present/mentioned but the brand is absent.
15. Evaluate AEO citation readiness using three planning levers: CONSENSUS, FRESHNESS, and AUTHORITY. Treat these as heuristics, not guarantees.
16. Structure important answer content for reuse: BLUF when appropriate, atomic sections, descriptive headings, explicit entities, simple declarative sentences, lists/tables, evidence, limitations, and numbers with timeframe/context.
17. Use the same audience + prompt graph for off-site authority: relevant editorial publications, communities, partners, YouTube, podcasts, and research/data assets. Do not manufacture mentions or spam UGC.
18. Audit robots/CDN/WAF rules for accidental blocking of relevant search/AI crawlers. Before changing production crawler policy, verify current official crawler documentation and the owner's content-use preferences. Never weaken security just to allow bots.
19. After data is available, prioritize opportunities such as:
   - high-impression / low-CTR queries and pages inside priority audiences
   - positions roughly 4–20 with realistic upside and strong business fit
   - pages already producing qualified organic leads or revenue
   - smaller topics/services with disproportionate conversion quality
   - high-traffic landing pages with weak conversion or poor audience fit
   - underserved high-value audience segments
   - citation gaps around high-value prompts
   - stale high-authority pages that need substantive refresh
   - decaying pages or lost queries worth recovering
20. Explicitly identify high-volume audiences/keywords that should NOT be chased because business value or fit is weak.
21. Choose one transformation path:
   A. upgrade in place
   B. progressive modernization
   C. controlled rebuild + migration
   Base the decision on business value, technical constraints, SEO risk, speed, cost, and maintainability.
22. If rebuilding, preserve valuable URLs where possible; otherwise create deliberate 301 redirect mappings. Preserve canonicals, metadata intent, internal-link equity, structured data, analytics, conversion events, and high-value content.
23. Upgrade the site through the AI-Native Website Optimization stack:
   Audience Map -> Prompt Fan-Out -> SEO foundation -> entity/schema clarity -> AEO/citation engine -> machine discovery -> API/CLI/OpenAPI -> MCP where useful -> WebMCP where useful -> measurement.
24. Never call a site AI-agent ready merely because llms.txt exists. Agent readiness requires truthful machine-readable information and verified agent-operable actions where applicable.
25. Never claim GA4/Search Console/Ads/GBP data was reviewed unless the corresponding authorized data was actually available.
26. Track AI visibility separately from SEO: observable brand mentions, cited URLs, competitor citation share where measurable, AI referrals, self-reported AI attribution, and crawler activity. Bot visits are not proof of citation.
27. When historical benchmark evidence is available, include a concise historical_benchmark_context describing comparable-case count, quality/confidence, reusable patterns, known failure modes, and which recommendations were influenced by prior evidence.

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

    benchmark_note = ""
    if state.historical_benchmark_context:
        benchmark_note = (
            "\nPrivate anonymized historical benchmark context is available in Venture State. "
            "Use it conservatively, do not expose identities, and report sample size/confidence.\n"
            + str(state.historical_benchmark_context)
        )

    if state.entry_mode == "existing_business":
        prompt = f"""
Transform this existing business using Venture Launch OS Mode B.
Website URL: {state.website_url}
Set entry_mode to exactly "existing_business" and website_url to exactly "{state.website_url}".

Perform the public-site/public-web audit now. Do not pretend to have private GA4, Search Console, Google Business Profile, Google Ads, Merchant Center, CRM, or revenue data.

Return a structured first-pass transformation analysis that includes:
- public_site_audit
- data_access: which first-party sources should be authorized and exactly what decisions each would inform
- preservation_map: public assets already visible plus historical assets/data that must be verified before migration
- transformation_strategy: upgrade_in_place, progressive_modernization, or controlled_rebuild, with rationale and confidence
- ai_agent_readiness: SEO/AEO/schema/LLM discovery/API-CLI/MCP/WebMCP gaps and highest-value next improvements
- in market/gtm, include an audience-first plan with priority audiences, business value, demand, attainability, what NOT to chase, and audience/content gaps
- include a prompt/topic fan-out for the highest-value audience, classify major prompts as CLICK-DEPENDENT/CITATION-FIRST/HYBRID, identify likely citation/brand gaps, and assess consensus/freshness/authority weaknesses
- historical_benchmark_context when comparable private historical evidence exists
- no more than three priorities
{benchmark_note}
"""
    else:
        prompt = (
            "Launch this venture using Venture Launch OS Mode A. "
            "Set entry_mode to exactly 'greenfield'. "
            "Before keyword research, define commercially meaningful audience segments and rank them by business value, search demand and attainability. "
            "For the highest-value audience, create a prompt/topic fan-out instead of targeting a single head term, classify major prompts as CLICK-DEPENDENT, CITATION-FIRST, or HYBRID, and build SEO/AEO around topic-wide relevance, citation readiness, and qualified business value. "
            "Use any private anonymized historical benchmark evidence conservatively and report sample size/confidence. "
            "Treat the following as the founder's casual idea statement:\n\n" + state.idea + benchmark_note
        )

    result = await Runner.run(agent, prompt)
    return result.final_output


def merge_analysis(state: VentureState, analysis: LaunchAnalysis) -> VentureState:
    # Entry mode is determined by deterministic request routing. Model output must not
    # downgrade an existing-business transformation back to greenfield.
    if state.entry_mode != "existing_business" and analysis.entry_mode == "existing_business":
        state.entry_mode = "existing_business"
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
    if analysis.historical_benchmark_context:
        state.historical_benchmark_context = analysis.historical_benchmark_context
    state.current_bottleneck = analysis.current_bottleneck
    state.top_priorities = [item.model_dump() for item in analysis.top_priorities]
    state.blockers = analysis.blockers
    state.approvals_required = analysis.approvals_required
    state.log_action("analyze_venture", "IMPLEMENTED", "Structured VLA analysis completed")
    return state
