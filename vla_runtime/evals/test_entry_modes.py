from main import LaunchRequest, state_from_request
from agent import LaunchAnalysis, looks_like_url, merge_analysis, normalized_url


def test_detects_existing_business_url() -> None:
    assert looks_like_url("example.com")
    assert looks_like_url("https://example.com")
    state = state_from_request(LaunchRequest(input="https://example.com"))
    assert state.entry_mode == "existing_business"
    assert state.website_url == "https://example.com"
    assert state.status == "audit_pending"


def test_detects_greenfield_idea() -> None:
    state = state_from_request(
        LaunchRequest(input="A pickup and delivery laundry service for busy families")
    )
    assert state.entry_mode == "greenfield"
    assert state.website_url is None
    assert state.status == "discovery"


def test_explicit_mode_overrides_auto_detection() -> None:
    state = state_from_request(
        LaunchRequest(input="example.com", mode="greenfield")
    )
    assert state.entry_mode == "greenfield"


def test_normalizes_url() -> None:
    assert normalized_url("example.com") == "https://example.com"
    assert normalized_url("https://example.com") == "https://example.com"


def test_existing_business_mode_cannot_be_downgraded_by_model_default() -> None:
    state = state_from_request(LaunchRequest(input="https://example.com"))
    analysis = LaunchAnalysis(
        entry_mode="greenfield",
        status="audited",
        thesis={},
        icp={},
        market={},
        offer={},
        economics={},
        gtm={},
        public_site_audit={"status": "complete"},
        data_access={"ga4": "requested"},
        preservation_map={"historical_data": "unverified"},
        transformation_strategy={"path": "progressive_modernization"},
        ai_agent_readiness={"score": 40},
        current_bottleneck="first-party data access",
        top_priorities=[],
    )
    merged = merge_analysis(state, analysis)
    assert merged.entry_mode == "existing_business"
    assert merged.website_url == "https://example.com"
