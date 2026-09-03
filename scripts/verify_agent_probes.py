#!/usr/bin/env python3
"""Safely verify production agent capability probes and emit a durable receipt."""
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

DEFAULT_MANIFEST = Path("templates/agent.example.json")
DEFAULT_RECEIPT = Path("artifacts/agent-verification-receipt.json")


def origin(url: str):
    p = urlparse(url)
    return p.scheme, p.hostname or "", p.port


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def canonical_json(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def main() -> None:
    manifest_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MANIFEST
    receipt_path = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_RECEIPT
    manifest = json.loads(manifest_path.read_text())
    canonical_origin = origin(manifest["venture"]["canonical_url"])
    results = []

    production = [a for a in manifest.get("actions", []) if a.get("readiness") == "production_verified"]
    for action in production:
        probe = action.get("verification_probe") or {}
        url = probe.get("url")
        expected = probe.get("expected_status")
        if not url or expected is None:
            fail(f"{action['id']}: missing verification_probe url/expected_status")
        if origin(url) != canonical_origin:
            fail(f"{action['id']}: probe must be same-origin as canonical_url")
        if urlparse(url).scheme != "https":
            fail(f"{action['id']}: probe must use HTTPS")

        status = None
        error = None
        try:
            req = Request(url, method="GET", headers={"User-Agent": "VLA-Agent-Readiness-Verifier/1.1"})
            with urlopen(req, timeout=10) as response:
                status = response.status
        except HTTPError as exc:
            status = exc.code
        except (URLError, TimeoutError) as exc:
            error = str(exc)

        passed = status == expected
        results.append({
            "action_id": action["id"],
            "probe_url": url,
            "expected_status": expected,
            "observed_status": status,
            "passed": passed,
            "error": error,
        })

    manifest_sha256 = hashlib.sha256(canonical_json(manifest).encode("utf-8")).hexdigest()
    receipt = {
        "schema_version": "1.1",
        "venture_id": manifest["venture"]["id"],
        "canonical_url": manifest["venture"]["canonical_url"],
        "manifest_sha256": manifest_sha256,
        "source_revision": os.getenv("GITHUB_SHA"),
        "verified_at": datetime.now(timezone.utc).isoformat(),
        "production_actions_checked": len(production),
        "passed": all(r["passed"] for r in results),
        "results": results,
    }
    receipt["receipt_sha256"] = hashlib.sha256(canonical_json(receipt).encode("utf-8")).hexdigest()

    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))
    print(f"Receipt written to {receipt_path}", file=sys.stderr)
    if not receipt["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
