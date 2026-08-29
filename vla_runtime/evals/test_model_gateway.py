from model_gateway import ModelTask, Provider, eligible_providers, select_provider


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
