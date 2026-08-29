# Marketing Operating System Knowledge Layer

## Mission
Convert historical operating experience into a compounding decision system.

The system should learn four distinct forms of knowledge:

1. **Declarative knowledge** — what metrics, channels, tools, platforms, and concepts mean.
2. **Procedural knowledge** — how to audit, optimize, migrate, launch, report, and scale.
3. **Conditional knowledge** — when to use one tactic versus another.
4. **Outcome knowledge** — what happened after the decision and under which business conditions.

The moat comes primarily from conditional + outcome knowledge.

## Decision memory unit
The atomic unit is not a document. It is a Decision Event:

`Context -> Evidence -> Diagnosis -> Decision -> Action -> Outcome -> Learning`

Example shape:
- Context: lead volume dropped
- Evidence: traffic/clicks stable, same landing pages receiving traffic
- Diagnosis: acquisition may not be the primary failure point
- Decision: verify call tracking/forms before increasing spend
- Action: inspect numbers, forms, routing, analytics
- Outcome: recorded privately
- Learning: distinguish traffic problems from conversion/measurement problems

## Knowledge hierarchy

### Layer 1 — Source Evidence
Authorized Gmail, Drive, GA4, GSC, Ads, CRM, reports, proposals, notes.

### Layer 2 — Client Timeline
Chronological reconstruction of what happened.

### Layer 3 — Decision Events
Structured operator decisions extracted from the timeline.

### Layer 4 — Client Case Model
Audience, channel, economics, actions, outcomes, failures.

### Layer 5 — Cross-Client Patterns
Repeated patterns across comparable cases.

### Layer 6 — Marketing Doctrine
Durable operating principles with confidence labels.

### Layer 7 — VLA Policy
High-confidence doctrine becomes default runtime behavior.

## Why old history matters
Older evidence reveals which principles persisted before current tools and AI terminology existed.

If the same decision pattern appears in 2018, 2023, and 2026, it is more likely to be an enduring operating principle rather than a temporary tactic.

Examples of cross-era principles already supported by historical evidence:
- obtain measurement/access before major optimization
- preserve organic ranking pages during migrations
- use SEO keyword intelligence to seed PPC tests
- diagnose conversion/tracking when traffic exists but leads disappear
- adjust geography based on observed quality/performance
- prefer dedicated landing pages for distinct intent
- test before scaling
- pause/cancel vendors or initiatives that cannot show meaningful progress
- report against business targets and funnel quality rather than raw activity
- favor mobile usability when mobile dominates traffic

## Versioning doctrine
The system must allow doctrine to evolve.

Each principle should store:
- doctrine_id
- statement
- status
- first_seen
- last_confirmed
- supporting_case_count
- supporting_era_count
- contradicting_case_count
- current_platform_validation_required
- confidence

## Anti-overfitting rules
Do not turn one historical preference into a universal rule.

Examples:
- a particular backlink quantity is not doctrine
- a particular SEO plugin is not doctrine
- a universal domain-vs-subdomain preference is not doctrine
- a specific CPC target is not doctrine
- an old keyword-density/readability plugin score is not doctrine

Extract the higher-level reasoning instead.

## Contradiction resolver
When two past decisions conflict, compare:
- business model
- site authority
- age of domain
- conversion history
- geography
- customer value
- technical constraints
- measurement quality
- migration risk
- available budget
- platform era

Then formulate the conditional rule.

## Operator-style retrieval
When VLA faces a new problem, retrieve knowledge in this order:

1. Current business first-party truth
2. Current business constraints and economics
3. Comparable historical Decision Events
4. High-confidence Marketing Doctrine
5. Current external platform/rule verification
6. Generic marketing knowledge only when the above are insufficient

## Learning objective
VLA should increasingly answer not only:

> What is best practice?

but:

> In situations materially similar to this one, what did we observe, what decision was made, what happened afterward, and what should we do differently now?

That is the compounding operating-system moat.
