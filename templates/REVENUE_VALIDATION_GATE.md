# Venture Launch OS — Revenue Validation Gate

## Purpose
Prevent VLA from over-investing in build, SEO, content, automation, or polish before a venture has evidence that a real customer will pay.

The default objective of a new venture is not "launch the website." It is **obtain the cheapest credible evidence of demand, then reach first revenue**.

## Gate 0 — Economic hypothesis
Before substantial build work, record:

- ICP / buyer:
- Pain / job-to-be-done:
- Trigger that makes the problem urgent:
- Offer:
- Price or price range:
- Expected gross margin / contribution margin:
- Primary acquisition channel:
- Expected customer value / LTV (estimate allowed, label it):
- Maximum acceptable CAC (estimate allowed, label it):
- Fastest credible path to a paid transaction:

Unknowns are allowed. Invented numbers are not.

## Gate 1 — Demand evidence
Choose the cheapest test appropriate to the venture. Examples:

- direct outreach to qualified buyers
- paid pilot / preorder / deposit
- quote or booking request
- marketplace listing
- search-demand validation
- small paid-search test
- partnership / referral test
- manual concierge delivery before automation

Track actual evidence:

| Metric | Result |
|---|---|
| Qualified prospects contacted / reached | |
| Positive replies | |
| Calls / demos / quote requests | |
| Purchase intent events | |
| Paid customers / deposits | |
| Revenue | |
| CAC / acquisition cost | |
| Objections / failure reasons | |

## Gate 2 — Decision
Classify the venture after the first meaningful test:

### SCALE
Verified paid demand or unusually strong buying evidence + plausible economics. Increase acquisition and automate repeated work.

### ITERATE
Some demand exists, but offer, pricing, ICP, channel, conversion, or fulfillment needs correction. Run the smallest next test.

### HOLD
Evidence is insufficient and the next test is currently blocked. Preserve work; do not continue polishing.

### KILL
Repeated credible tests show weak demand or structurally unattractive economics. Stop consuming attention and capital.

## Build-budget rule
Before first revenue, prefer the smallest implementation capable of testing the commercial hypothesis. Defer features that do not materially improve:

1. ability to transact or capture a qualified lead,
2. trust required for conversion,
3. measurement/attribution,
4. fulfillment reliability,
5. discovery by the chosen acquisition channel.

SEO/AEO/GEO infrastructure can be installed early when inexpensive and reusable, but large content programs should not substitute for demand validation.

## First-Revenue SLA
Every venture must maintain:

- `first_revenue_target_date`
- `next_revenue_test`
- `test_owner`
- `expected_cost`
- `success_threshold`
- `actual_result`
- `decision: SCALE | ITERATE | HOLD | KILL`

If a venture has no active revenue test, VLA should treat that as a launch blocker unless the venture is explicitly infrastructure/research-only.

## Agent rule
When choosing between two next actions, prefer the action that produces **higher-quality commercial evidence per dollar and per human hour**. Do not confuse traffic, pages published, impressions, rankings, commits, or feature count with validated demand.
