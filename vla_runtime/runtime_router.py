from __future__ import annotations

from agent import analyze_venture as analyze_with_openai
from model_gateway import Provider, configured_primary_provider
from provider_agent import analyze_venture_with_provider
from state import VentureState


async def analyze_venture(state: VentureState):
    """Run the persistent VLA agent on the configured intelligence provider.

    The OpenAI path preserves the existing hosted-tool implementation. Non-OpenAI
    providers run the same VLA policy and structured output through the Agents SDK
    Any-LLM adapter with VLA-owned local tools.
    """
    provider = configured_primary_provider()
    if provider == Provider.OPENAI:
        return await analyze_with_openai(state)
    return await analyze_venture_with_provider(state, provider)
