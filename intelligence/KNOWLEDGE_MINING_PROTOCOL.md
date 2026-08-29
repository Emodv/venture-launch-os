# Historical Marketing Knowledge Mining Protocol

## Goal
Continuously convert authorized historical Gmail and Google Drive material into reusable VLA decision knowledge without copying private client data into the public repository.

## What to mine
Prioritize evidence that reveals judgment, not just activity:

1. Access and onboarding requests
2. SEO/PPC audits
3. optimization instructions
4. migration/redesign decisions
5. campaign change notes
6. monthly/quarterly reporting
7. landing-page recommendations
8. keyword/search-term analysis
9. client feedback on lead quality
10. vendor/team management
11. pause/cancel/scale decisions
12. postmortems and project outcomes

## Time-depth strategy
Mine by era so the system can distinguish enduring principles from obsolete tactics:

- Era A: 2015–2018
- Era B: 2019–2022
- Era C: 2023–2024
- Era D: 2025–present

A rule becomes stronger when it appears independently across multiple eras.

## Extraction record
For every decision-bearing source, extract privately:

- source_id
- source_type
- date
- client_id
- channel
- problem
- available_evidence
- decision
- action
- expected_outcome
- observed_outcome
- business_context
- confidence
- doctrine_candidates
- obsolete_tactic_flag

## Pattern scoring
A doctrine candidate is scored using:

- recurrence across clients
- recurrence across eras
- evidence quality
- observed business outcome
- consistency with current platform realities

Suggested status:

### REPEATED_PATTERN
Appears across multiple clients and/or eras and remains operationally sound.

### CASE_PATTERN
Strong single/few-case evidence; useful conditionally.

### CURRENT_HYPOTHESIS
Plausible but needs more evidence.

### RETIRED
Historically used, but current evidence/platform rules make it inappropriate as a default.

## Contradictions are valuable
Do not hide contradictions.

When historical recommendations conflict:
1. preserve both decisions
2. reconstruct the context and data available at the time
3. identify what changed
4. extract the higher-level decision rule

Example:
Two different domain-migration recommendations may not be inconsistent if one property had strong standalone equity and the other did not.

The doctrine should learn:
> choose architecture based on evidence, migration risk, authority, topical fit, and business value — not a universal preference for standalone domains or subdomains.

## Tactics vs principles
Separate:

### Enduring principles
- preserve proven equity
- validate tracking
- diagnose funnel stage before changing spend
- optimize to qualified business outcomes
- test before scaling

### Time-bound tactics
- specific SEO plugin preferences
- keyword-density conventions
- old bidding strategies
- obsolete rich-result tactics
- platform-specific hacks

Only enduring principles should automatically influence future VLA decisions. Time-bound tactics require current verification.

## Privacy
Never store publicly:
- raw Gmail IDs
- Drive IDs
- passwords
- API keys
- account/customer IDs
- identifiable customer records
- confidential pricing/revenue unless anonymized and explicitly permitted

Private evidence should be referenced through internal opaque IDs.

## Output layers
The mining process should produce:

1. Client Case Records — private
2. Decision Events — private
3. Experiment/Outcome Records — private
4. Anonymized Benchmarks — restricted/derived
5. Marketing Doctrine — reusable operating knowledge
6. VLA Runtime Rules — only high-confidence principles

## Runtime use
VLA should retrieve doctrine in this order:

1. current first-party evidence for this business
2. business-specific context
3. comparable historical cases
4. repeated doctrine principles
5. current external/platform verification where needed

Historical doctrine must never override stronger current first-party evidence.
