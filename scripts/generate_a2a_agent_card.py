#!/usr/bin/env python3
"""Generate a deployable A2A v1 Agent Card from a VLA venture manifest.

The manifest remains the source of truth: advertised skills are derived only from
explicit venture actions, preventing capability drift between VLA and A2A discovery.

Usage:
  python scripts/generate_a2a_agent_card.py [manifest] [output_root]

Default output:
  artifacts/agent-publication/.well-known/agent-card.json
"""
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

DEFAULT_MANIFEST = Path("templates/agent.example.json")
DEFAULT_OUTPUT_ROOT = Path("artifacts/agent-publication")


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    manifest_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MANIFEST
    output_root = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUTPUT_ROOT

    try:
        manifest = json.loads(manifest_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"manifest is not valid JSON: {exc}")

    venture = manifest.get("venture") or {}
    canonical_url = venture.get("canonical_url")
    parsed = urlparse(canonical_url or "")
    if parsed.scheme != "https" or not parsed.netloc:
        fail("venture.canonical_url must be an absolute HTTPS URL")

    actions = manifest.get("actions") or []
    skills = []
    for action in actions:
        action_id = action.get("id")
        purpose = action.get("purpose")
        endpoint = action.get("endpoint")
        readiness = action.get("readiness")
        if not action_id or not purpose or not endpoint:
            fail("every advertised action requires id, purpose, and endpoint")
        endpoint_url = urlparse(endpoint)
        if endpoint_url.scheme != "https" or endpoint_url.netloc != parsed.netloc:
            fail(f"action {action_id} endpoint must be same-origin HTTPS")
        # Do not advertise actions explicitly marked unavailable.
        if readiness in {"unavailable", "disabled"}:
            continue
        skills.append({
            "id": action_id,
            "name": action_id.replace("-", " ").replace("_", " ").title(),
            "description": f"{purpose}. Readiness: {readiness or 'unspecified'}.",
            "tags": [purpose, "vla"],
            "examples": [f"Perform the {purpose} action for {venture.get('name', 'this venture')}."]
        })

    if not skills:
        fail("refusing to publish an Agent Card with no available skills")

    base = canonical_url.rstrip("/")
    card = {
        "name": venture.get("name") or venture.get("id"),
        "description": venture.get("description") or "VLA-powered venture",
        "version": "1.0.0",
        "protocolVersion": "1.0",
        "url": f"{base}/a2a",
        "preferredTransport": "JSONRPC",
        "additionalInterfaces": [{"url": f"{base}/a2a", "transport": "JSONRPC"}],
        "capabilities": {
            "streaming": False,
            "pushNotifications": False,
            "stateTransitionHistory": True
        },
        "defaultInputModes": ["application/json", "text/plain"],
        "defaultOutputModes": ["application/json", "text/plain"],
        "skills": skills
    }

    destination = output_root / ".well-known" / "agent-card.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(card, indent=2) + "\n")
    print(f"A2A Agent Card written to {destination} with {len(skills)} skill(s)")


if __name__ == "__main__":
    main()
