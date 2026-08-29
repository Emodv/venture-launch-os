# VLA Runtime v0.3

Venture Launch Agent (VLA) is the persistent autonomous business-growth agent for Venture Launch OS.

VLA owns the mission, Venture State, decision policy, privacy rules, business permissions, agent-to-agent contract, and learning loop. Model providers are replaceable intelligence substrates beneath VLA.

## Core principle

**Persistent VLA, replaceable models.**

Current provider registry supports configuration for:

- OpenAI
- Anthropic Claude
- Google Gemini
- xAI Grok

The current primary orchestrator is implemented with the OpenAI Agents SDK. Claude, Gemini, and Grok have provider adapters/model-gateway support for progressive multi-provider execution; they are not yet claimed as fully equivalent orchestrator runtimes.

## Two venture entry modes

### Mode A — Greenfield Venture
Input a plain-English business idea. VLA researches and structures the zero-to-one venture path.

### Mode B — Existing Business Transformation
Input an existing business URL. VLA performs a public-site/public-web audit, requests relevant first-party data access, builds a preservation map, recommends upgrade vs progressive modernization vs controlled rebuild, and assesses AI-agent readiness.

The Mode B principle is: **preserve before replacing**.

## Agent-economy role

VLA is designed to help a business become:

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

## Model gateway

Provider/model IDs are configured by environment rather than hard-coded into doctrine:

```bash
OPENAI_API_KEY=
VLA_OPENAI_MODEL=

ANTHROPIC_API_KEY=
VLA_ANTHROPIC_MODEL=

GEMINI_API_KEY=
VLA_GEMINI_MODEL=

XAI_API_KEY=
VLA_XAI_MODEL=
```

Provider secrets are never returned by `/agent`, stored in Venture State, or committed.

Optional provider SDKs can be installed with:

```bash
pip install -e '.[anthropic]'
pip install -e '.[gemini]'
pip install -e '.[xai]'
pip install -e '.[all-providers]'
```

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

Configure an OpenAI model/key for the current primary orchestrator, then:

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
  evals/test_model_gateway.py
```

GitHub Actions compiles the runtime and runs the same regression suite on runtime changes.

## Current release boundary

v0.3 ships:

- persistent VLA product identity
- greenfield and existing-business reasoning contracts
- privacy-safe historical intelligence
- 2027+ marketing/agent-economy doctrine
- provider-neutral model registry
- OpenAI/Claude/Gemini/Grok client adapters
- agent intent discovery
- business fit evaluation
- agent-readiness scoring
- bounded negotiation decisions
- HTTP agent-to-agent surface

Not yet verified/complete:

- production deployment
- equivalent full autonomous orchestrator loops on all four model providers
- authenticated commerce/payment execution
- standardized external A2A transport interoperability
- live provider benchmark-based auto-routing
