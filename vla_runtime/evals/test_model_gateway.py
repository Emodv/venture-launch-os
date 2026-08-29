from model_gateway import (
    ModelTask,
    Provider,
    agent_model_id,
    configured_primary_provider,
    eligible_providers,
    provider_available,
    select_provider,
)


def test_gateway_knows_all_provider_classes_without_configuration() -> None:
    providers = eligible_providers(ModelTask(kind="reasoning"), require_configuration=False)
    assert Provider.OPENAI in providers
    assert Provider.ANTHROPIC in providers
    assert Provider.GEMINI in providers
    assert Provider.XAI in providers


def test_remote_mcp_capability_filter() -> None:
    providers = eligible_providers(
        ModelTask(kind="agent_tooling", requires_remote_mcp=True),
        require_configuration=False,
    )
    assert Provider.OPENAI in providers
    assert Provider.GEMINI in providers
    assert Provider.ANTHROPIC not in providers
    assert Provider.XAI not in providers


def test_preferred_provider_selected_when_eligible() -> None:
    provider = select_provider(
        ModelTask(kind="research"),
        preferred=Provider.XAI,
        require_configuration=False,
    )
    assert provider == Provider.XAI


def test_openai_is_available_with_key_even_without_explicit_model(monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.delenv("VLA_OPENAI_AGENT_MODEL", raising=False)
    monkeypatch.delenv("VLA_OPENAI_MODEL", raising=False)
    assert provider_available(Provider.OPENAI)


def test_non_openai_requires_explicit_agent_route(monkeypatch) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    monkeypatch.delenv("VLA_ANTHROPIC_AGENT_MODEL", raising=False)
    assert not provider_available(Provider.ANTHROPIC)
    monkeypatch.setenv("VLA_ANTHROPIC_AGENT_MODEL", "any-llm/anthropic/current-model")
    assert provider_available(Provider.ANTHROPIC)
    assert agent_model_id(Provider.ANTHROPIC) == "any-llm/anthropic/current-model"


def test_configured_primary_provider(monkeypatch) -> None:
    monkeypatch.setenv("VLA_PROVIDER", "gemini")
    monkeypatch.setenv("GEMINI_API_KEY", "test-key")
    monkeypatch.setenv("VLA_GEMINI_AGENT_MODEL", "any-llm/gemini/current-model")
    assert configured_primary_provider() == Provider.GEMINI
