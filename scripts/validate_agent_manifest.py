#!/usr/bin/env python3
"""Validate VLA agent capability manifests and enforce readiness invariants."""
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "templates" / "AGENT_CAPABILITY_MANIFEST.schema.json"
DEFAULT_MANIFEST = ROOT / "templates" / "agent.example.json"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def origin(url: str) -> tuple[str, str, int | None]:
    parsed = urlparse(url)
    return parsed.scheme, parsed.hostname or "", parsed.port


def main() -> None:
    manifest_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MANIFEST
    schema = json.loads(SCHEMA_PATH.read_text())
    manifest = json.loads(manifest_path.read_text())

    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(manifest), key=lambda e: list(e.absolute_path))
    if errors:
        for error in errors:
            path = ".".join(str(p) for p in error.absolute_path) or "$"
            print(f"{path}: {error.message}", file=sys.stderr)
        raise SystemExit(1)

    verified = set(manifest["verification"]["verified_actions"])
    action_ids = {action["id"] for action in manifest["actions"]}
    unknown = verified - action_ids
    if unknown:
        fail(f"verified_actions contains unknown action IDs: {sorted(unknown)}")

    production_actions = [a for a in manifest["actions"] if a["readiness"] == "production_verified"]
    production = {a["id"] for a in production_actions}
    if production != verified:
        fail(
            "production_verified actions must exactly match verification.verified_actions; "
            f"production={sorted(production)}, verified={sorted(verified)}"
        )

    if production and not manifest["verification"]["last_verified_at"]:
        fail("production_verified actions require verification.last_verified_at")

    venture_origin = origin(manifest["venture"]["canonical_url"])
    for action in production_actions:
        probe = action.get("verification_probe")
        if not probe:
            fail(f"production_verified action '{action['id']}' requires a non-mutating verification_probe")
        if origin(probe["url"]) != venture_origin:
            fail(f"verification_probe for '{action['id']}' must be same-origin as venture.canonical_url")
        if action["consequence"] != "read_only" and action["method"] == "GET":
            fail(f"state-changing action '{action['id']}' must not advertise GET as its action method")

    print(f"PASS: {manifest_path} validates against VLA agent capability contract")


if __name__ == "__main__":
    main()
