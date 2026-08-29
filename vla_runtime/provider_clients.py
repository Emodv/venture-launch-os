from __future__ import annotations

import os
from typing import Any

from model_gateway import DEFAULTS, Provider


def create_provider_client(provider: Provider) -> Any:
    """Instantiate a configured provider client.

    Provider SDK imports are lazy so VLA can run with only the providers enabled for
    a deployment. Secrets come from environment variables and must never be logged or
    persisted into Venture State.
    """
    config = DEFAULTS[provider]
    api_key = os.getenv(config.api_key_env)
    if not api_key:
        raise RuntimeError(f"Missing required environment variable: {config.api_key_env}")
    if not config.model:
        raise RuntimeError(f"Missing required environment variable: {config.model_env}")

    if provider == Provider.OPENAI:
        from openai import OpenAI

        return OpenAI(api_key=api_key)

    if provider == Provider.ANTHROPIC:
        from anthropic import Anthropic

        return Anthropic(api_key=api_key)

    if provider == Provider.GEMINI:
        from google import genai

        return genai.Client(api_key=api_key)

    if provider == Provider.XAI:
        from openai import OpenAI

        return OpenAI(api_key=api_key, base_url=config.base_url)

    raise ValueError(f"Unsupported provider: {provider}")


def provider_runtime_config(provider: Provider) -> dict[str, str | None]:
    config = DEFAULTS[provider]
    return {
        "provider": provider.value,
        "model": config.model or None,
        "base_url": config.base_url,
    }
