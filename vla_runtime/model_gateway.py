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
    agent_model_env: str
    api_key_env: str
    base_url: str | None = None
    supports_tools: bool = True
    supports_structured_output: bool = True
    supports_remote_mcp: bool = False

    @property
    def model(self) -> str:
        return os.getenv(self.model_env, "").strip()

    @property
    def agent_model(self) -> str:
        return os.getenv(self.agent_model_env, "").strip()


DEFAULTS: dict[Provider, ProviderConfig] = {
    Provider.OPENAI: ProviderConfig(
        provider=Provider.OPENAI,
        model_env="VLA_OPENAI_MODEL",
        agent_model_env="VLA_OPENAI_AGENT_MODEL",
        api_key_env="OPENAI_API_KEY",
        supports_remote_mcp=True,
    ),
    Provider.ANTHROPIC: ProviderConfig(
        provider=Provider.ANTHROPIC,
        model_env="VLA_ANTHROPIC_MODEL",
        agent_model_env="VLA_ANTHROPIC_AGENT_MODEL",
        api_key_env="ANTHROPIC_API_KEY",
    ),
    Provider.GEMINI: ProviderConfig(
        provider=Provider.GEMINI,
        model_env="VLA_GEMINI_MODEL",
        agent_model_env="VLA_GEMINI_AGENT_MODEL",
        api_key_env="GEMINI_API_KEY",
        supports_remote_mcp=True,
    ),
    Provider.XAI: ProviderConfig(
        provider=Provider.XAI,
        model_env="VLA_XAI_MODEL",
        agent_model_env="VLA_XAI_AGENT_MODEL",
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
    has_key = bool(os.getenv(config.api_key_env))
    if provider == Provider.OPENAI:
        return has_key
    return bool(has_key and config.agent_model)


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
    eligible = eligible_providers(task, require_configuration=require_configuration)
    if preferred is not None and preferred in eligible:
        return preferred
    if not eligible:
        raise RuntimeError("No configured model provider satisfies this task")
    return eligible[0]


def configured_primary_provider(require_configuration: bool = True) -> Provider:
    requested = os.getenv("VLA_PROVIDER", "openai").strip().lower()
    if requested == "auto":
        return select_provider(
            ModelTask(kind="vla_orchestration", requires_tools=True, requires_structured_output=True),
            require_configuration=require_configuration,
        )
    try:
        provider = Provider(requested)
    except ValueError as exc:
        raise RuntimeError(f"Unsupported VLA_PROVIDER: {requested}") from exc
    if require_configuration and not provider_available(provider):
        config = DEFAULTS[provider]
        requirements = [config.api_key_env]
        if provider != Provider.OPENAI:
            requirements.append(config.agent_model_env)
        raise RuntimeError(
            f"Provider {provider.value} is not configured; check: {', '.join(requirements)}"
        )
    return provider


def agent_model_id(provider: Provider) -> str | None:
    config = DEFAULTS[provider]
    if provider == Provider.OPENAI:
        return config.agent_model or config.model or os.getenv("VLA_MODEL", "").strip() or None
    return config.agent_model or None


def model_descriptor(provider: Provider) -> dict[str, str | bool | None]:
    config = DEFAULTS[provider]
    return {
        "provider": config.provider.value,
        "model": config.model,
        "agent_model": config.agent_model,
        "model_env": config.model_env,
        "agent_model_env": config.agent_model_env,
        "api_key_env": config.api_key_env,
        "base_url": config.base_url,
        "supports_tools": config.supports_tools,
        "supports_structured_output": config.supports_structured_output,
        "supports_remote_mcp": config.supports_remote_mcp,
        "configured": provider_available(provider),
    }


def provider_status() -> list[dict[str, str | bool | None]]:
    return [model_descriptor(provider) for provider in Provider]
