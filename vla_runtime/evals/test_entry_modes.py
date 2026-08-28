from main import LaunchRequest, state_from_request
from agent import looks_like_url, normalized_url


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
