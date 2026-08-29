from agent_economy import (
    AgentCapabilityRequest,
    AgentJourneyStage,
    BusinessAgentProfile,
    BuyerAgentContext,
    NegotiationDecision,
    NegotiationPolicy,
    PrincipalType,
    VLA_AGENT_IDENTITY,
    agent_readiness_score,
    discovery_questions,
    evaluate_fit,
)


def test_vla_has_persistent_agent_identity() -> None:
    assert VLA_AGENT_IDENTITY["short_name"] == "VLA"
    assert "AI agents" in VLA_AGENT_IDENTITY["mission"]


def test_discovery_questions_avoid_identity() -> None:
    context = BuyerAgentContext()
    questions = discovery_questions(context)
    joined = " ".join(questions).lower()
    assert "name" not in joined
    assert "principal" in joined
    assert "outcome" in joined


def test_business_agent_fit_uses_intent_and_geography() -> None:
    profile = BusinessAgentProfile(
        category="professional service",
        supported_use_cases=("business advisory",),
        geographies=("Toronto, Ontario",),
        pricing_summary="Fixed-fee consultation",
        refund_policy_summary="Subject to published cancellation policy",
        response_time_summary="Typically within one business day",
        evidence=({"type": "credential", "value": "verified"},),
        actions=("request_consultation",),
    )
    buyer = BuyerAgentContext(
        principal_type=PrincipalType.BUSINESS,
        objective="business advisory",
        stage=AgentJourneyStage.COMPARE,
        geography="Toronto",
    )
    result = evaluate_fit(profile, AgentCapabilityRequest(buyer=buyer))
    assert result.supported
    assert result.matched_use_cases == ["business advisory"]
    assert result.available_actions == ["request_consultation"]


def test_negotiation_policy_distinguishes_authority_from_rejection() -> None:
    policy = NegotiationPolicy(
        currency="CAD",
        list_price=1000,
        minimum_price=800,
        maximum_discount_pct=5,
        approval_required_below=900,
    )
    assert policy.decision(975) == NegotiationDecision.ALLOWED
    assert policy.decision(925) == NegotiationDecision.APPROVAL_REQUIRED
    assert policy.decision(850) == NegotiationDecision.APPROVAL_REQUIRED
    assert policy.decision(700) == NegotiationDecision.REJECTED


def test_agent_readiness_is_internal_score() -> None:
    profile = BusinessAgentProfile(
        category="local service",
        geographies=("Toronto",),
        pricing_summary="From CAD 100",
        refund_policy_summary="Published policy",
        response_time_summary="Same business day",
        evidence=({"type": "policy", "value": "public"},),
        actions=("request_quote",),
    )
    score = agent_readiness_score(profile)
    assert score["total"] == 100
