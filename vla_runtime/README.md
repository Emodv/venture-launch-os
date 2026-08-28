# VLA Runtime v0.2

Runnable OpenAI Agents SDK prototype for Venture Launch Agent.

## Two entry modes

### Mode A — Greenfield Venture
Input a plain-English business idea. VLA researches and structures the zero-to-one venture path.

### Mode B — Existing Business Transformation
Input an existing business URL. VLA performs a public-site/public-web audit, requests relevant first-party data access, builds a preservation map, recommends upgrade vs progressive modernization vs controlled rebuild, and assesses AI-agent readiness.

The Mode B principle is: **preserve before replacing**.

## What it does

- auto-detects idea vs URL input
- uses a single VLA orchestrator
- performs live web research through OpenAI hosted web search
- returns structured ICP, market, offer, economics, bottleneck, priorities, blockers and approvals
- for existing businesses returns:
  - public site audit
  - first-party data access plan
  - preservation map
  - transformation strategy
  - AI-agent readiness assessment
- persists Venture State as JSON
- supports resume by venture ID
- exposes CLI and HTTP API
- enforces an approval classification layer

## Existing-business data rule

VLA never asks for a Google password or raw credentials.

After the public audit it should request official authorization to relevant first-party properties when available, such as:

- Google Analytics 4
- Google Search Console
- Google Business Profile
- Google Ads
- Merchant Center
- other relevant analytics/CRM/revenue systems

Until that data is actually connected, historical traffic, ranking, conversion and revenue conclusions remain unverified.

## Run

From `vla_runtime/`:

```bash
uv sync
cp .env.example .env.local
# set OPENAI_API_KEY securely in your environment
```

Greenfield:

```bash
uv run python main.py "A mobile dog grooming service in Toronto"
```

Existing business:

```bash
uv run python main.py "https://example.com"
```

Explicit mode:

```bash
uv run python main.py "example.com" --mode existing_business
```

For HTTP mode:

```bash
PORT=8000 uv run python main.py
```

Endpoints:

- `GET /health`
- `POST /ventures` with `{ "input": "idea or URL", "mode": "auto" }`
- `POST /transform` with `{ "url": "https://example.com" }`
- `GET /ventures/{venture_id}`
- `POST /ventures/{venture_id}/resume`

## Mode B transformation sequence

`URL -> public audit -> first-party data access -> preservation map -> upgrade/rebuild decision -> SEO/AEO -> entity/schema -> AI discovery -> API/CLI/MCP -> WebMCP -> verification -> measurement`

When rebuilding, VLA must protect valuable URLs, redirects, canonical intent, internal-link equity, analytics, conversion tracking and high-value content.

## Current boundary

v0.2 ships the dual-mode reasoning, state, audit, preservation and transformation contract.

The next adapter layer connects authorized first-party analytics/search sources and account-side execution systems. Account authorization must use official OAuth/connector flows; credentials are never stored in source control.

## Tests

```bash
pytest -q evals/test_approvals.py evals/test_entry_modes.py
```

GitHub Actions also compiles the runtime and runs these regression tests on runtime changes.
