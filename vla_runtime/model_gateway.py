from __future__ import annotations

import os
from dataclasses import dataclass
from enum import Enum


class Provider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GEMINI = "gemini"
    XAI = "xai"


@dataclass(frozen=True)
class ProviderConfig:
    provider: Provider
    model: str
    api_key_env: str
    base_url: str | None = None
    supports_tools: bool = True
    supports_structured_output: bool = True
    supports_remote_mcp: bool = False


DEFAULTS: dict[Provider, ProviderConfig] = {
    Provider.OPENAI: ProviderConfig(
        provider=Provider.OPENAI,
        model=os.getenv("VLA_OPENAI_MODEL", "gpt-5.6"),
        api_key_env="OPENAI_API_KEY",
        supports_remote_mcp=True,
    ),
    Provider.ANTHROPIC: ProviderConfig(
        provider=Provider.ANTHROPIC,
        model=os.getenv("VLA_ANTHROPIC_MODEL", "claude-opus-5"),
        api_key_env="ANTHROPIC_API_KEY",
    ),
    Provider.GEMINI: ProviderConfig(
        provider=Provider.GEMINI,
        model=os.getenv("VLA_GEMINI_MODEL", "gemini-3.7-flash"),
        api_key_env="GEMINI_API_KEY",
        supports_remote_mcp=True,
    ),
    Provider.XAI: ProviderConfig(
        provider=Provider.XAI,
        model=os.getenv("VLA_XAI_MODEL", "grok-4.6"),
        api_key_env="XAI_API_KEY",
        base_url="https://api.x.ai/v1",
    ),
}


@dataclass(frozen=True)
class ModelTask:
    kind: str
    requires_tools: bool = False
    requires_structured_output: bool = False
    requires_remote_mcp: bool = False
    high_risk: bool = False


def provider_available(provider: Provider) -> bool:
    config = DEFAULTS[provider]
    return bool(os.getenv(config.api_key_env))


def eligible_providers(task: ModelTask, require_key: bool = True) -> list[Provider]:
    eligible: list[Provider] = []
    for provider, config in DEFAULTS.items():
        if require_key and not provider_available(provider):
            continue
        if task.requires_tools and not config.supports_tools:
            continue
        if task.requires_structured_output and not config.supports_structured_output:
            continue
        if task.requires_remote_mcp and not config.supports_remote_mcp:
            continue
        eligible.append(provider)
    return eligible


def select_provider(
    task: ModelTask,
    preferred: Provider | None = None,
    require_key: bool = True,
) -> Provider:
    """Select an eligible provider without coupling VLA doctrine to one model.

    This is deliberately deterministic. Quality/cost/latency routing can later be
    supplied by the model-evaluation registry, while business policy remains stable.
    """
    eligible = eligible_providers(task, require_key=require_key)
    if preferred is not None and preferred in eligible:
        return preferred
    if not eligible:
        raise RuntimeError("No configured model provider satisfies this task")
    return eligible[0]


def model_descriptor(provider: Provider) -> dict[str, str | bool | None]:
    config = DEFAULTS[provider]
    return {
        "provider": config.provider.value,
        "model": config.model,
        "api_key_env": config.api_key_env,
        "base_url": config.base_url,
        "supports_tools": config.supports_tools,
        "supports_structured_output": config.supports_structured_output,
        "supports_remote_mcp": config.supports_remote_mcp,
    }
