# Venture State Schema

Venture Launch Agent (VLA) should maintain one persistent state object per venture.

## Core identity

```json
{
  "venture_id": "[UUID]",
  "name": "[PLACEHOLDER]",
  "domain": "[PLACEHOLDER]",
  "status": "idea|validation|building|live|acquiring|operating|scaling|paused",
  "created_at": "[ISO_DATETIME]",
  "updated_at": "[ISO_DATETIME]"
}
```

## Required state domains

### Thesis
- problem
- target_customer
- why_now
- proposed_solution
- differentiation
- must_be_true

### ICP
- segment
- geography
- company/person attributes
- pain
- trigger/intent signal
- exclusions
- estimated value

### Market
- competitors
- substitutes
- pricing norms
- demand evidence
- regulatory notes

### Offer
- core offer
- entry offer
- pricing
- upsells
- recurrence
- risk reversal
- proof/evidence

### Economics
- AOV/ACV
- variable cost
- contribution margin
- CAC
- CAC ceiling
- payback
- LTV
- assumptions

### Assets
- brand
- domain
- repository
- deployment
- database
- CRM
- payments
- analytics

### GTM
- channels
- prospects
- campaigns
- outreach
- content
- SEO
- partnerships

### Operations
- funnel stages
- fulfillment workflow
- vendors/partners
- capacity
- service levels
- exceptions

### Outcomes
- leads
- qualified opportunities
- customers
- revenue
- refunds/cancellations
- contribution profit

### Learning
- experiments
- hypotheses
- failures
- wins
- objections
- insights
- decisions

### Control
- current_bottleneck
- top_priorities
- blockers
- approvals_required
- last_verified_at

## State update rules

1. Do not overwrite known facts with assumptions.
2. Label values as `fact`, `estimate`, `assumption`, or `unknown` when provenance matters.
3. Preserve important decision history.
4. Store evidence/source references when available.
5. Every campaign, outreach action, deployment, and material experiment should have an observable status.
6. Economic outcomes should be linked back to acquisition source whenever possible.
7. VLA should be able to resume a venture from state without requiring the founder to repeat the original brief.

## Recommended experiment object

```json
{
  "experiment_id": "[UUID]",
  "hypothesis": "[TEXT]",
  "channel": "[TEXT]",
  "start_date": "[DATE]",
  "success_metric": "[TEXT]",
  "kill_criteria": "[TEXT]",
  "result": "[TEXT]",
  "decision": "iterate|scale|pause|kill",
  "learning": "[TEXT]"
}
```

## Recommended opportunity object

```json
{
  "opportunity_id": "[UUID]",
  "account": "[TEXT]",
  "contact": "[TEXT]",
  "source": "[TEXT]",
  "intent_signal": "[TEXT]",
  "estimated_value": 0,
  "stage": "identified|contacted|replied|qualified|meeting|proposal|won|lost",
  "next_action": "[TEXT]",
  "next_action_at": "[ISO_DATETIME]",
  "revenue": 0
}
```

The implementation may use SQL tables rather than one JSON object, but the conceptual state model must remain intact.
