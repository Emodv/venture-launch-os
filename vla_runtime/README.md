# VLA Runtime v0.4

Venture Launch Agent (VLA) is the persistent autonomous business-growth agent for Venture Launch OS.

VLA owns the mission, Venture State, decision policy, privacy rules, business permissions, agent-to-agent contract, and learning loop. Model providers are replaceable intelligence substrates beneath VLA.

## Core principle

**Persistent VLA, replaceable models.**

VLA preserves the system already built. v0.4 adds multi-provider orchestration without deleting the established OpenAI path.

Supported provider classes:

- OpenAI
- Anthropic Claude
- Google Gemini
- xAI Grok

The OpenAI path retains the existing hosted-tool implementation. Claude, Gemini, and Grok can run the same VLA policy and structured-output contract through the OpenAI Agents SDK Any-LLM adapter when explicitly configured.

## Configure the VLA intelligence provider

Set:

```bash
VLA_PROVIDER=openai   # openai | anthropic | gemini | xai | auto
```

OpenAI can use the SDK default model or an explicit model:

```bash
OPENAI_API_KEY=
VLA_OPENAI_AGENT_MODEL=
```

For non-OpenAI providers, configure the provider key and a full Any-LLM model route. VLA deliberately does not hard-code provider-specific current/future model IDs.

```bash
ANTHROPIC_API_KEY=
VLA_ANTHROPIC_AGENT_MODEL=any-llm/anthropic/<current-model-id>

GEMINI_API_KEY=
VLA_GEMINI_AGENT_MODEL=any-llm/gemini/<current-model-id>

XAI_API_KEY=
VLA_XAI_AGENT_MODEL=any-llm/xai/<current-model-id>
```

`VLA_PROVIDER=auto` chooses the first configured provider satisfying the VLA orchestration requirements.

Provider secrets are never returned by `/agent`, stored in Venture State, or committed.

## Provider execution behavior

### OpenAI
Uses the established VLA agent path, including OpenAI-hosted web search plus VLA function tools.

### Claude / Gemini / Grok
Uses the same VLA identity, doctrine, privacy policy, structured `LaunchAnalysis`, approval tool, state model, and execution loop through the Agents SDK Any-LLM route.

For public-site inspection, the non-OpenAI path uses VLA's own bounded `fetch_public_webpage` tool. It blocks loopback/private/link-local/reserved destinations and does not authenticate to websites.

VLA does **not** claim broad search-engine research when only direct webpage fetching occurred.

## Two venture entry modes

### Mode A — Greenfield Venture
Input a plain-English business idea. VLA researches and structures the zero-to-one venture path.

### Mode B — Existing Business Transformation
Input an existing business URL. VLA audits the public business surface, requests relevant first-party data access, builds a preservation map, recommends upgrade vs progressive modernization vs controlled rebuild, and assesses AI-agent readiness.

The Mode B principle is: **preserve before replacing**.

## Agent-economy role

VLA helps a business become:

`discoverable -> understandable -> trustworthy -> recommendable -> negotiable -> transactable`

VLA distinguishes between:

1. the human/organizational principal with the commercial need; and
2. the AI agent acting on that principal's behalf.

It asks for decision-relevant intent and constraints, not unnecessary identity.

Agent journey stages:

`research -> compare -> negotiate -> transact -> fulfillment`

## AI Agent Optimization (AAO)

VLA's agent-readiness layer evaluates whether a business exposes enough truthful structured information for another agent to evaluate it, including:

- category/entity clarity
- supported use cases
- geography
- pricing
- refund/cancellation policy
- response time
- evidence/provenance
- available actions
- transaction methods
- constraints

The readiness score is an internal diagnostic, not a claim of a universal external AI ranking.

## Agent-to-agent API

### `GET /agent`
Returns VLA identity, supported journey stages, and non-secret provider configuration status.

### `POST /agent/discover`
Accepts buyer-agent context and returns missing commercial-intent questions.

### `POST /agent/evaluate`
Evaluates a buyer-agent request against a business-agent profile and returns fit, geography/use-case matches, pricing/policy/evidence, actions, limitations, and internal agent-readiness score.

### `POST /agent/negotiate`
Evaluates a proposed price against explicit commercial authority and returns:

- `allowed`
- `approval_required`
- `rejected`

VLA never invents authority to discount, change policy, sign agreements, or transact outside explicit business rules.

## Existing-business data rule

VLA never asks for a Google password or raw credentials.

After the public audit it should request official authorization to relevant first-party properties when available, such as:

- Google Analytics 4
- Google Search Console
- Google Business Profile
- Google Ads
- Merchant Center
- CRM/revenue systems

Until data is actually connected, historical traffic, ranking, conversion and revenue conclusions remain unverified.

## Privacy-first learning

Historical client evidence may teach VLA operating patterns, but reusable knowledge must be anonymized. Client names, people, domains, emails, account/property IDs, CRM/source IDs, private URLs, credentials, and re-identifying combinations are prohibited from reusable intelligence.

The moat is decision/outcome knowledge, not customer data.

## Run

From `vla_runtime/`:

```bash
uv sync
cp .env.example .env.local
```

Greenfield:

```bash
uv run python main.py "A mobile dog grooming service in Toronto"
```

Existing business:

```bash
uv run python main.py "https://example.com"
```

HTTP mode:

```bash
PORT=8000 uv run python main.py
```

## All endpoints

- `GET /health`
- `GET /agent`
- `POST /agent/discover`
- `POST /agent/evaluate`
- `POST /agent/negotiate`
- `POST /ventures`
- `POST /transform`
- `GET /ventures/{venture_id}`
- `POST /ventures/{venture_id}/resume`

## Tests

```bash
pytest -q \
  evals/test_approvals.py \
  evals/test_entry_modes.py \
  evals/test_intelligence.py \
  evals/test_agent_economy.py \
  evals/test_model_gateway.py \
  evals/test_provider_agent.py
```

GitHub Actions compiles the runtime and runs this regression suite on runtime changes.

## v0.4 release boundary

Shipped in code:

- all prior VLA/Venture Launch OS behavior preserved
- persistent VLA product identity
- greenfield and existing-business reasoning contracts
- privacy-safe historical intelligence
- 2027+ marketing/agent-economy doctrine
- agent-to-agent discovery/evaluation/negotiation API
- AI Agent Optimization readiness model
- provider-neutral model registry
- runtime provider router
- OpenAI established orchestrator path preserved
- Claude/Gemini/Grok same-agent orchestration through configurable Any-LLM routes
- bounded public-webpage tool for non-OpenAI site audits
- private-network/SSRF protections on public-page fetching
- regression coverage for provider configuration and safety

Still separate from this code-only release:

- real provider API credentials and live-provider smoke tests
- production deployment
- authenticated commerce/payment execution
- standardized external A2A transport interoperability
- live benchmark-based model auto-routing
