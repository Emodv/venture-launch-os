#!/usr/bin/env python3
"""Install validated VLA agent-publication artifacts into a deployable static directory.

Platform-neutral by design: run after publish_agent_receipt.py and before the host's
normal deployment step. No deployment credentials are required by this script.

Usage:
  python scripts/install_agent_publication.py [publication_root] [static_root]

Examples:
  python scripts/install_agent_publication.py artifacts/agent-publication public
  python scripts/install_agent_publication.py artifacts/agent-publication static
"""
import json
import shutil
import sys
from pathlib import Path

DEFAULT_PUBLICATION_ROOT = Path("artifacts/agent-publication")
DEFAULT_STATIC_ROOT = Path("public")
RECEIPT_RELATIVE = Path(".well-known/agent-verification.json")


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    publication_root = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PUBLICATION_ROOT
    static_root = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_STATIC_ROOT
    source = publication_root / RECEIPT_RELATIVE
    destination = static_root / RECEIPT_RELATIVE

    if not source.is_file():
        fail(f"publication artifact missing: {source}")

    try:
        receipt = json.loads(source.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"publication artifact is not valid JSON: {exc}")

    if receipt.get("passed") is not True or not receipt.get("receipt_sha256"):
        fail("publication artifact must be a passed, hash-bound verification receipt")

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)

    installed = json.loads(destination.read_text())
    if installed != receipt:
        fail("installed receipt differs from validated publication artifact")

    print(f"Installed agent verification receipt at {destination}")


if __name__ == "__main__":
    main()
