# Venture Launch Agent (VLA) v0.1 — Build Specification

## Objective

Build the smallest real autonomous agent that can take a conversational business idea, create persistent Venture State, run Venture Launch OS, and advance the venture toward its first qualified opportunity.

## Input

Minimum required input:

```json
{
  "idea": "plain-English description"
}
```

Optional:

- geography
- existing name/domain
- existing repo/site
- budget
- connected accounts/tools
- constraints

Do not require a business plan.

## v0.1 orchestration

Use one primary orchestrator.

The orchestrator should:

1. Parse the idea.
2. Create Venture State.
3. Run Phase 0 discovery.
4. Identify missing material facts.
5. Research market/competitors.
6. Score opportunity and fatal constraints.
7. Build ICP, offer, pricing/economic hypotheses.
8. Establish name/domain path.
9. Establish technical launch path.
10. Build or update the conversion surface when tools permit.
11. Create initial content/search foundation.
12. Select the fastest credible acquisition channel.
13. Build an initial prospect/demand queue.
14. Execute authorized actions.
15. Record outcomes and next bottleneck.

## Tool interface categories

VLA should use narrow, explicit tool functions rather than arbitrary side effects.

### Research
- web_search
- competitor_lookup
- domain_check
- business/regulatory_lookup

### Build
- github_repo/file actions
- deployment actions
- database/schema actions
- environment configuration
- site QA

### Revenue
- CRM create/update
- prospect search/enrichment
- email/outreach
- advertising platform actions
- payment/customer lookup

### Measurement
- analytics query
- CRM pipeline query
- revenue/payment query
- search/indexing diagnostics

## Approval middleware

Every tool action must be classified:

- `AUTONOMOUS`
- `PREAUTHORIZED`
- `EXPLICIT_APPROVAL`

Before executing a side effect, VLA should check the action class against the venture/user authorization policy.

## Run state machine

```text
NEW_IDEA
  ↓
DISCOVERY
  ↓
VALIDATED_TO_BUILD | PIVOT_REQUIRED | REJECTED
  ↓
FOUNDATION
  ↓
LIVE
  ↓
ACQUIRING
  ↓
OPPORTUNITY_FOUND
  ↓
CUSTOMER_WON
  ↓
OPERATING
  ↓
OPTIMIZING / SCALING
```

A venture can move backward when evidence invalidates assumptions.

## Economic objective function

At every iteration choose the next action that best improves:

- probability of first qualified opportunity
- probability of first revenue
- expected contribution margin
- learning velocity

while minimizing:

- fixed cost
- irreversible commitments
- time to feedback
- founder attention

## Required observability

Every run should record:

- timestamp
- venture_id
- objective
- action/tool
- input summary
- action status
- verification evidence
- output
- state changes
- spend/cost if any
- next decision

## v0.1 success criteria

The prototype is successful when it can demonstrate this path on a test venture:

1. Accept one casual idea statement.
2. Create valid Venture State.
3. Produce a researched ICP and offer.
4. Identify and score the next highest-value actions.
5. Create/update venture assets through at least one connected execution tool.
6. Produce an acquisition-ready prospect or demand plan.
7. Respect approval gates.
8. Resume from saved state.
9. Never claim unverified execution.
10. Pass evals for missing evidence, blockers, unsafe spend, and false completion claims.

## v0.1 non-goals

Do not initially build:

- a swarm of specialist agents
- complex multi-agent negotiation
- autonomous large-budget ad management
- autonomous legal commitments
- autonomous purchases
- unnecessary custom infrastructure

Prove one orchestrator can reliably drive the workflow first.

## Evaluation cases

Minimum eval suite:

1. Local service idea with no name/domain.
2. B2B agency/service idea.
3. SaaS-lite idea.
4. Weak idea with bad unit economics.
5. Regulated idea requiring escalation.
6. Existing domain/repo supplied.
7. Tool unavailable mid-run.
8. Purchase required.
9. User provides unsupported performance claim.
10. Resume an existing venture from stored state.

Grade:

- factual discipline
- correct tool selection
- approval policy
- progress despite blockers
- economic prioritization
- state integrity
- verification behavior
- first-opportunity focus

## Product boundary

Venture Launch OS remains the source of operating policy.

VLA v0.1 is the software runtime that interprets and executes that policy against a venture's persistent state and connected tools.
