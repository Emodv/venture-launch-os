# VLA Runtime v0.1

Runnable OpenAI Agents SDK prototype for Venture Launch Agent.

## What it does

- accepts one plain-English business idea
- uses a single VLA orchestrator
- performs live web research through OpenAI hosted web search
- returns structured ICP, market, offer, economics, bottleneck, priorities, blockers and approvals
- persists Venture State as JSON
- supports resume by venture ID
- exposes CLI and HTTP API
- enforces an approval classification layer

## Run

From `vla_runtime/`:

```bash
uv sync
cp .env.example .env.local
# set OPENAI_API_KEY securely in your environment
uv run python main.py "A mobile dog grooming service in Toronto"
```

For HTTP mode:

```bash
PORT=8000 uv run python main.py
```

Endpoints:

- `GET /health`
- `POST /ventures` with `{ "idea": "..." }`
- `GET /ventures/{venture_id}`
- `POST /ventures/{venture_id}/resume`

## v0.1 boundary

This version proves the core agent loop: idea → research → structured venture state → persistence → resume → approval discipline.

It does not yet perform irreversible or account-side effects such as buying domains, sending outreach, deploying sites, or spending ad budget. Those are the next connected tool adapters and remain governed by `AUTONOMOUS_EXECUTION.md`.

## Tests

```bash
uv run pytest evals/test_approvals.py
```

The model-backed cases in `evals/cases.jsonl` are the next-stage workflow eval set.
