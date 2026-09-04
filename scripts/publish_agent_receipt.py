#!/usr/bin/env python3
"""Publish a validated VLA verification receipt into a deployable well-known path.

This script is intentionally platform-neutral: it validates the receipt against the
manifest's advertised verification contract, then copies it to a static output tree.
A deployment adapter (Vercel, Netlify, S3, etc.) can publish that tree without the
verifier needing production credentials.
"""
import hashlib
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

DEFAULT_MANIFEST = Path("templates/agent.example.json")
DEFAULT_RECEIPT = Path("artifacts/agent-verification-receipt.json")
DEFAULT_OUTPUT_ROOT = Path("artifacts/agent-publication")


def canonical_json(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    manifest_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MANIFEST
    receipt_path = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_RECEIPT
    output_root = Path(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_OUTPUT_ROOT

    manifest = json.loads(manifest_path.read_text())
    receipt = json.loads(receipt_path.read_text())
    verification = manifest.get("verification") or {}
    receipt_url = verification.get("receipt_url")
    if not receipt_url:
        fail("manifest verification.receipt_url is required")

    canonical = urlparse(manifest["venture"]["canonical_url"])
    advertised = urlparse(receipt_url)
    if (advertised.scheme, advertised.hostname, advertised.port) != (canonical.scheme, canonical.hostname, canonical.port):
        fail("receipt_url must be same-origin as venture.canonical_url")
    if advertised.scheme != "https":
        fail("receipt_url must use HTTPS")
    if advertised.path != "/.well-known/agent-verification.json":
        fail("receipt_url must use /.well-known/agent-verification.json")

    expected_hash = receipt.get("receipt_sha256")
    unsigned = dict(receipt)
    unsigned.pop("receipt_sha256", None)
    actual_hash = hashlib.sha256(canonical_json(unsigned).encode("utf-8")).hexdigest()
    if not expected_hash or expected_hash != actual_hash:
        fail("receipt_sha256 does not match receipt contents")
    if receipt.get("venture_id") != manifest["venture"]["id"]:
        fail("receipt venture_id does not match manifest")
    if receipt.get("canonical_url") != manifest["venture"]["canonical_url"]:
        fail("receipt canonical_url does not match manifest")
    if receipt.get("schema_version") != verification.get("receipt_schema_version"):
        fail("receipt schema_version does not match manifest")
    if not receipt.get("passed"):
        fail("refusing to publish a failed verification receipt")

    destination = output_root / ".well-known" / "agent-verification.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"Publishable receipt written to {destination}")


if __name__ == "__main__":
    main()
