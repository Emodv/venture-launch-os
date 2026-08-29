from model_gateway import Provider
from provider_agent import _public_http_url, build_provider_agent


def test_public_fetch_blocks_local_networks() -> None:
    assert not _public_http_url("http://127.0.0.1:8000")
    assert not _public_http_url("http://localhost:8000")
    assert not _public_http_url("file:///etc/passwd")


def test_provider_agent_requires_non_openai_provider(monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    try:
        build_provider_agent(Provider.OPENAI)
    except ValueError as exc:
        assert "non-OpenAI" in str(exc)
    else:
        raise AssertionError("OpenAI must stay on the established default VLA agent path")


def test_provider_agent_uses_configured_any_llm_route(monkeypatch) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    monkeypatch.setenv("VLA_ANTHROPIC_AGENT_MODEL", "any-llm/anthropic/current-model")
    agent = build_provider_agent(Provider.ANTHROPIC)
    assert agent.name == "Venture Launch Agent"
    assert str(agent.model) == "any-llm/anthropic/current-model"
