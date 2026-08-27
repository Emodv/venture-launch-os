# Venture Launch Agent v0.2

## Goal
Upgrade VLA from planning to closed-loop execution.

Core loop:

observe -> diagnose -> plan -> authorize -> execute -> verify -> measure -> learn -> update state -> continue

## Planner
Create at most three active priorities. Each action must include objective, value, probability, speed, effort, risk, cost, tool, success metric, kill criteria, and verification method.

## Executor
Use narrow adapters for research, GitHub, deployment, database, CRM, prospect research, analytics, search diagnostics, payments, and advertising. A tool response is not proof of success.

## Verifier
Every material action needs evidence. Examples: open the production site after deployment; write then read a database record; retrieve a CRM record after creation; confirm a transaction in the payment system.

Use: VERIFIED, FAILED, PARTIAL, BLOCKED, NOT_APPLICABLE.

## Critic
Before costly or consequential work, challenge the plan:
- Is this the current bottleneck?
- Is there a faster route to revenue?
- What assumption is weakest?
- Is the result measurable?
- Can it be reversed?
- Is there a cheaper experiment?

Reject cosmetic work when a higher-value economic action exists.

## Memory
Maintain current Venture State plus append-only Event Memory for decisions, actions, evidence, spend, leads, objections, experiments, wins, losses, and lessons.

## Economic policy
Primary metrics:
1. time to first qualified opportunity
2. time to first paying customer
3. contribution margin
4. CAC and payback
5. repeat/retention when applicable

Default ranking: value x probability x speed / effort. Fatal constraints override scoring.

## Continuation rule
After every action, determine the highest-value executable next action. If policy permits it, continue without requiring another founder prompt.

## Approval classes
Autonomous: research, analysis, code, non-destructive repo changes, technical SEO, analytics setup, CRM/database setup, prospect research, QA, content drafting, reversible optimization.

Preauthorized: deploy or publish, routine CRM changes, and campaign adjustments only inside an already approved policy or budget.

Explicit approval: purchases, material spend, contracts, regulated representations, destructive actions, sensitive disclosure, or irreversible infrastructure changes.

## First-customer mode
For a new venture with no customers prioritize narrow ICP, concrete offer, credible conversion surface, demand/prospect discovery, direct acquisition testing, rapid response to intent, and learning. Do not wait for perfect SEO or a large content library.

## Adapter contract
Every adapter declares inputs, approval class, side-effect flag, cost if any, result, verification method, and idempotency behavior when relevant.

## Stop conditions
Stop only when no valuable executable action remains, a required approval blocks the critical path, access is genuinely unavailable, legal/regulatory judgment is required, or evidence supports pausing/killing the venture.

## v0.2 success criteria
A test venture must show: conversational idea input, state creation, priorities, one real action, independent verification, event logging, state update, automatic next-action selection, correct approval handling, and plan change after failure.
