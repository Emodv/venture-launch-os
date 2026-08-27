# Venture Launch OS

## Purpose
Turn a raw business idea or client brief into a live, measurable, revenue-ready operating system with minimal user input.

This skill is for local services, SMBs, agencies, marketplaces, lead-generation businesses, concierge services, SaaS-lite offers, and other businesses where speed to market matters more than perfect initial architecture.

## Primary objective
Go from **idea → validated offer → brand/domain → live website → backend/database → analytics → SEO/AEO/AI visibility → CRM/funnel → outreach/off-page SEO → first customers → operating metrics → iteration**.

Optimize for:
1. Fastest path to revenue.
2. Low fixed cost before validation.
3. Mobile-first conversion.
4. Search + LLM/AI-agent discoverability.
5. Reusable systems and automation.
6. Measurable unit economics.

## Minimum input required from user
Accept a rough brief. Do not demand a perfect business plan.

Required only when genuinely blocking:
- Business idea / problem being solved.
- Geography or target market, if location-dependent.
- Existing assets, if any: domain, repo, brand, accounts.
- Material legal/regulated constraints if known.

Everything else should be inferred, researched, estimated, or marked `[PLACEHOLDER]` until evidence exists.

## Default execution mode
Act as an execution partner, not a consultant.

- Do not stop at recommendations when tools permit execution.
- Do not repeatedly ask permission for reversible, low-risk actions already within scope.
- Verify completion before claiming completion.
- When blocked by credentials, billing, legal approval, unavailable integrations, or irreversible/high-risk actions, report the blocker clearly and continue all independent work.
- Prefer shipping a lean revenue-validating version over building a large app.

---

# Phase 1 — Business evaluation

## 1. Define the thesis
Produce:
- One-sentence business model.
- Target customer.
- Core problem.
- Why now.
- Revenue model.
- Expected gross margin model.
- Competitive wedge.
- What must be true for this to work.

## 2. Score the opportunity
Score 1–10:
- Customer pain.
- Market demand.
- Competition / supply gap.
- Gross margin potential.
- Recurrence.
- Speed to first revenue.
- Capital intensity.
- Operational complexity.
- Differentiation.
- Scalability.

Return an overall score and explicitly identify the largest weakness.

## 3. Solve the largest weakness first
Do not optimize the easy parts while a fatal constraint remains.

Examples:
- Weak margin → change fulfillment model.
- High CAC → narrow geography/ICP.
- No differentiation → build stronger offer or distribution wedge.
- Operational risk → partner instead of owning infrastructure.

---

# Phase 2 — Business model and offer

## 4. Build the offer
Create:
- Core service/product.
- Entry offer.
- Upsells.
- Recurring/repeat mechanism.
- Guarantee / risk reversal where appropriate.
- Minimum order / pricing floors to protect unit economics.

The offer should answer:
- Why buy?
- Why now?
- Why from us?
- Why not the traditional alternative?

## 5. Build the unit economics model
Estimate and label assumptions:
- Average order value.
- Cost of fulfillment.
- Payment fees.
- Delivery / logistics.
- Refund / support allowance.
- Contribution margin.
- CAC ceiling.
- Payback period.
- LTV assumptions.

Do not scale paid acquisition until contribution margin is plausibly positive.

---

# Phase 3 — Market and competitor research

## 6. Map competitors and substitutes
Research:
- Direct competitors.
- Traditional substitutes.
- DIY alternative.
- Aggregators/marketplaces.
- Pricing norms.
- Reviews and recurring complaints.
- Local market gaps.

Look for structural opportunities, not just weaker websites.

## 7. Select launch market
For local businesses rank candidate cities/areas by:
- Demand.
- Population / business density.
- Existing providers.
- Competitive weakness.
- Fulfillment distance.
- Customer affluence where relevant.
- Route density / logistics.
- Search demand.

Operate in 1–2 focused markets first even if SEO pages cover more cities.

---

# Phase 4 — Brand, domain and positioning

## 8. Create brand system
Build:
- Name shortlist if needed.
- Domain strategy.
- Positioning statement.
- Tagline.
- Tone.
- Visual direction.

Default visual principle:
- premium, simple, high contrast, fast-loading, mobile-first.
- avoid visual clutter and template-like stock aesthetics.

## 9. Domain selection rules
Prefer:
1. memorable brand `.com` or local ccTLD.
2. short, easy spelling.
3. no legacy toxicity.
4. no unnecessary hyphens.
5. strong brandability over keyword stuffing.

If evaluating aged domains, check reputation/backlinks/toxicity before recommending.

---

# Phase 5 — Website and funnel

## 10. Ship revenue-first MVP
Default stack unless a better connected tool exists:
- GitHub for source control.
- Vercel for deployment.
- Supabase for database/backend.
- Stripe for payment when appropriate.
- HubSpot or equivalent CRM when available.

Do not build a native app before demand is proven.

## 11. Mobile-first UX
Assume most local-service traffic is mobile unless evidence says otherwise.

Design rules:
- 320–430px first.
- Large tap targets.
- One clear CTA per screen.
- Centered copy when visually stronger.
- High contrast: dark background → light text; light background → dark text.
- No accidental horizontal page scrolling.
- Horizontal swipe/scroll-snap for selection interfaces.
- Minimal form fields.
- Progressive disclosure.

## 12. Core funnel
Default funnel:

Traffic → landing page → eligibility/fit check → instant quote or offer → contact/booking → payment/authorization where appropriate → confirmation.

Every step must have an event/metric.

## 13. Conversion copy
Keep copy concrete.

Homepage must communicate:
- What it is.
- Who it is for.
- Main benefit.
- How it works.
- Price/quote path.
- Location/availability.
- CTA.

Delete fluff aggressively.

---

# Phase 6 — Backend and operational system

## 14. Central data model
At minimum create structured records for:
- leads/customers.
- source/UTM attribution.
- geography.
- requested service/product.
- status/stage.
- estimated value.
- notes.
- timestamps.

Common pipeline:
`new → contacted → qualified → booked → won/lost`

Add `waitlist` if geography/capacity is not active.

## 15. Backend requirements
- Server-side validation.
- Bot/spam protection.
- Central persistence; never rely on browser local storage for business-critical leads.
- Safe API boundaries.
- Logging.
- Idempotency where payment/order actions require it.
- Security/RLS checks after database changes.

## 16. CRM and notifications
When available:
- sync new leads to CRM.
- notify operator instantly.
- log source and campaign.
- automate acknowledgement.
- create follow-up tasks/stages.

---

# Phase 7 — SEO, AEO and AI-agent visibility

## 17. Technical SEO baseline
Every launch should include:
- canonical URLs.
- unique title/meta description.
- sitemap.xml.
- robots.txt.
- internal linking.
- descriptive headings.
- fast mobile performance.
- city/service landing pages where justified.

Avoid thin doorway pages. Pages need unique local/service value.

## 18. Structured data
Use appropriate Schema.org types:
- Organization / LocalBusiness where factual.
- Service.
- Offer where real.
- FAQPage when visible FAQ exists.
- WebSite.
- BreadcrumbList for deeper structures.

Never put unsupported claims in schema.

## 19. AI/LLM discovery package
Default machine-readable layer:
- `/llms.txt`
- `/services.json` or equivalent structured catalog.
- `/.well-known/agent.json`
- `/openapi.json` when APIs exist.
- `/mcp.txt` when an MCP endpoint exists.
- `/cli.txt` with curl examples when useful.
- public, deterministic availability/quote endpoints when safe.

Robots should not accidentally block major AI/search crawlers if discovery is desired.

## 20. Agent safety rules
Machine-readable docs must tell agents:
- what they may state as fact.
- what is only an estimate.
- what requires confirmation.
- not to invent pricing, availability, partners, timelines, or completed bookings.

---

# Phase 8 — Local and off-page SEO

## 21. Citation and entity building
Prioritize:
- Google Business Profile when eligible.
- local municipality/business directories.
- chambers of commerce.
- industry directories.
- local press.
- trusted review platforms.

Avoid low-quality mass directory blasts.

## 22. Link acquisition
Highest-value link types:
1. local authority links.
2. genuine partner links.
3. local PR/editorial coverage.
4. useful data/resources worth citing.
5. associations and industry bodies.

Create a backlink/outreach pipeline with:
- target.
- domain.
- contact.
- opportunity type.
- market.
- authority tier.
- expected value.
- status.
- next follow-up date.

## 23. Linkable assets
Examples:
- local pricing guides.
- service comparison guides.
- calculators.
- market data.
- city/service directories.
- proprietary benchmark reports.

Build assets that humans and AI systems can cite.

---

# Phase 9 — Go-to-market

## 24. Fastest-cash channels first
Prioritize channels by value × probability × speed ÷ effort.

Typical local-business order:
1. Google Search / Maps.
2. Meta local ads.
3. community groups.
4. partnerships/referrals.
5. local SEO.
6. earned PR.
7. broader content/SEO.

## 25. Paid acquisition test
Before scale define:
- target geography.
- high-intent keywords/audiences.
- offer.
- landing page.
- conversion event.
- CAC ceiling.
- kill criteria.

Do not optimize for clicks. Optimize for booked/won customers and contribution margin.

## 26. Outreach
Use connected tools to:
- find partners.
- identify decision makers.
- draft/send partnership pitches when authorized.
- track replies and statuses.

Good outreach should create one of:
- fulfillment capacity.
- distribution.
- backlinks/authority.
- referrals.
- revenue.

---

# Phase 10 — Operations and learning loop

## 27. Pilot operating model
Minimize fixed cost.

Prefer:
- partners over owned infrastructure.
- scheduled routes over expensive on-demand fulfillment.
- manual exception handling before custom automation.

Automate only after a workflow repeats enough to justify it.

## 28. Measure the funnel
Minimum KPIs:
- visitors.
- quote starts.
- quote completions.
- leads.
- booked customers.
- won customers.
- CAC.
- AOV.
- fulfillment cost.
- contribution margin/order.
- repeat rate.
- refund/claim rate.

## 29. Weekly decision loop
Every review should answer:
1. What generated revenue?
2. What blocked conversion?
3. What is the bottleneck now?
4. What should be killed?
5. What should be automated?
6. What asset compounds if built once?

Do not allow more than 3 major priorities at once.

---

# Deliverables checklist

A successful run should produce as many of these as the business needs:

- Business evaluation and score.
- Vision/mission/positioning.
- Offer and pricing hypothesis.
- Competitor/market analysis.
- Brand/domain decision.
- GitHub repository.
- Live production website.
- Mobile-first funnel.
- Backend/database.
- Lead/order pipeline.
- Analytics/events.
- CRM integration.
- Payment integration where appropriate.
- Local/service landing pages.
- sitemap.xml + robots.txt.
- schema markup.
- llms.txt.
- services catalog/API.
- OpenAPI/MCP/agent discovery layer when useful.
- content/SEO assets.
- off-page SEO pipeline.
- provider/partner outreach.
- GTM plan.
- KPI dashboard/query.
- prioritized next actions.

---

# Decision rules

## Build vs. buy
Use existing services if they save time and do not destroy margin/control.

## Own infrastructure only when justified
Do not buy stores, equipment, fleets, or heavy software before demand supports them.

## Revenue before elegance
A simple system that closes 10 customers is more valuable than a perfect system with none.

## Geography density over premature expansion
Local marketplaces and delivery businesses win with route/customer density.

## SEO quality over volume
No PBNs, spam backlinks, thin doorway pages, or mass-generated filler content.

## AI visibility must be factual
Machine-readable content should be more structured, not more exaggerated.

---

# Required reporting format

At meaningful milestones report:

## Outcome
What was actually completed and verified.

## Current bottleneck
The single biggest constraint to revenue.

## Metrics
Current known funnel/business metrics.

## Opportunity score
For next actions score:
- Value.
- Probability.
- Speed.
- Effort.

## Top 3 next measurable actions
Only the highest-impact three.

---

# Shortcut invocation

When the user says something like:

> “Launch this idea using Venture Launch OS: [idea]”

or

> “Use the same system we used for DK.”

interpret that as permission to run this entire framework autonomously, using available connected tools, while escalating only true blockers or high-risk/irreversible decisions.
