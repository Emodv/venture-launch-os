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
    model_env: str
    api_key_env: str
    base_url: str | None = None
    supports_tools: bool = True
    supports_structured_output: bool = True
    supports_remote_mcp: bool = False

    @property
    def model(self) -> str:
        return os.getenv(self.model_env, "").strip()


DEFAULTS: dict[Provider, ProviderConfig] = {
    Provider.OPENAI: ProviderConfig(
        provider=Provider.OPENAI,
        model_env="VLA_OPENAI_MODEL",
        api_key_env="OPENAI_API_KEY",
        supports_remote_mcp=True,
    ),
    Provider.ANTHROPIC: ProviderConfig(
        provider=Provider.ANTHROPIC,
        model_env="VLA_ANTHROPIC_MODEL",
        api_key_env="ANTHROPIC_API_KEY",
    ),
    Provider.GEMINI: ProviderConfig(
        provider=Provider.GEMINI,
        model_env="VLA_GEMINI_MODEL",
        api_key_env="GEMINI_API_KEY",
        supports_remote_mcp=True,
    ),
    Provider.XAI: ProviderConfig(
        provider=Provider.XAI,
        model_env="VLA_XAI_MODEL",
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
    return bool(os.getenv(config.api_key_env) and config.model)


def eligible_providers(task: ModelTask, require_configuration: bool = True) -> list[Provider]:
    eligible: list[Provider] = []
    for provider, config in DEFAULTS.items():
        if require_configuration and not provider_available(provider):
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
    require_configuration: bool = True,
) -> Provider:
    """Select an eligible provider without coupling VLA doctrine to one model."""
    eligible = eligible_providers(task, require_configuration=require_configuration)
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
        "model_env": config.model_env,
        "api_key_env": config.api_key_env,
        "base_url": config.base_url,
        "supports_tools": config.supports_tools,
        "supports_structured_output": config.supports_structured_output,
        "supports_remote_mcp": config.supports_remote_mcp,
    }


def provider_status() -> list[dict[str, str | bool | None]]:
    """Return non-secret provider configuration status for diagnostics."""
    rows: list[dict[str, str | bool | None]] = []
    for provider, config in DEFAULTS.items():
        rows.append(
            {
                "provider": provider.value,
                "configured": provider_available(provider),
                "model": config.model or None,
                "supports_tools": config.supports_tools,
                "supports_structured_output": config.supports_structured_output,
                "supports_remote_mcp": config.supports_remote_mcp,
            }
        )
    return rows
