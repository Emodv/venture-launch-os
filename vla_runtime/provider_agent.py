from __future__ import annotations

import ipaddress
import socket
from urllib.parse import urlparse

import httpx
from agents import Agent, Runner, function_tool

from agent import (
    INSTRUCTIONS,
    LaunchAnalysis,
    approval_class_for,
)
from intelligence import knowledge_is_privacy_safe, sanitize_historical_knowledge
from model_gateway import Provider, agent_model_id, configured_primary_provider
from state import VentureState


def _public_http_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.hostname:
            return False
        host = parsed.hostname
        addresses = socket.getaddrinfo(host, None)
        for item in addresses:
            ip = ipaddress.ip_address(item[4][0])
            if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
                return False
        return True
    except Exception:
        return False


@function_tool
def fetch_public_webpage(url: str) -> str:
    """Fetch a public HTTP/HTTPS webpage for VLA analysis.

    Use this only for publicly reachable business/research pages. Private, local,
    loopback, link-local, and reserved network destinations are blocked. The tool
    returns a bounded text/HTML snapshot and does not authenticate to websites.
    """
    if not _public_http_url(url):
        return "BLOCKED: URL is not a permitted public HTTP/HTTPS destination."
    try:
        response = httpx.get(
            url,
            timeout=12.0,
            follow_redirects=True,
            headers={"User-Agent": "VLA/0.4 public-audit"},
        )
        response.raise_for_status()
        content_type = response.headers.get("content-type", "")
        if not any(kind in content_type for kind in ("text/", "application/json", "application/ld+json")):
            return f"UNSUPPORTED_CONTENT_TYPE: {content_type}"
        text = response.text
        return text[:30000]
    except Exception as exc:
        return f"FETCH_FAILED: {type(exc).__name__}"


def build_provider_agent(provider: Provider | None = None) -> Agent:
    provider = provider or configured_primary_provider()
    if provider == Provider.OPENAI:
        raise ValueError("provider_agent is for non-OpenAI providers; use the default VLA agent path")
    model = agent_model_id(provider)
    if not model:
        raise RuntimeError(f"No agent model configured for provider {provider.value}")
    return Agent(
        name="Venture Launch Agent",
        instructions=(
            INSTRUCTIONS
            + "\n\nMODEL-PROVIDER NOTE\n"
            + "You are still VLA. The underlying model provider does not change VLA identity, policy, memory, privacy, or authority. "
            + "Use fetch_public_webpage for public-site evidence when needed. Do not claim broad web search coverage when only direct public-page fetching was performed."
        ),
        model=model,
        tools=[fetch_public_webpage, approval_class_for],
        output_type=LaunchAnalysis,
    )


def _benchmark_note(state: VentureState) -> str:
    if not state.historical_benchmark_context:
        return ""
    safe_context = sanitize_historical_knowledge(state.historical_benchmark_context)
    if not knowledge_is_privacy_safe(safe_context):
        return ""
    return (
        "\nPrivate anonymized historical benchmark context is available in Venture State. "
        "Use it conservatively, never infer or reconstruct identity, and report sample size/confidence.\n"
        + str(safe_context)
    )


def _prompt_for(state: VentureState) -> str:
    benchmark_note = _benchmark_note(state)
    if state.entry_mode == "existing_business":
        return f"""
Transform this existing business using Venture Launch OS Mode B.
Website URL: {state.website_url}
Set entry_mode to exactly "existing_business" and website_url to exactly "{state.website_url}".
Use fetch_public_webpage on the website when useful. Do not pretend to have GA4, Search Console, Ads, CRM, revenue, or broad search-engine evidence unless supplied.
Return public_site_audit, data_access, preservation_map, transformation_strategy, ai_agent_readiness, audience-first GTM, prompt/topic fan-out, citation/brand gaps, historical_benchmark_context when safe, current bottleneck, and no more than three priorities.
Also assess AI Agent Optimization: entity clarity, geography, pricing, policies/refunds, evidence, response expectations, agent-readable actions, negotiation readiness, and transaction readiness.
{benchmark_note}
"""
    return (
        "Launch this venture using Venture Launch OS Mode A. Set entry_mode to exactly 'greenfield'. "
        "Define valuable audiences before keyword research. Map both the human principal and likely AI-agent intermediary. "
        "Create prompt/topic fan-out, discovery surfaces, AI Agent Optimization requirements, and the fastest credible path to qualified opportunity and revenue. "
        "Use privacy-safe historical benchmark evidence conservatively.\n\n"
        + state.idea
        + benchmark_note
    )


async def analyze_venture_with_provider(
    state: VentureState,
    provider: Provider | None = None,
) -> LaunchAnalysis:
    provider = provider or configured_primary_provider()
    agent = build_provider_agent(provider)
    result = await Runner.run(agent, _prompt_for(state))
    return result.final_output
