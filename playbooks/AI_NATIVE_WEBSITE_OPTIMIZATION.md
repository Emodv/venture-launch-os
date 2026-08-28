# AI-Native Website Optimization — SEO + AEO + Agent Technology

## Mission
Upgrade any existing or new website so it is optimized for both the current search web and the emerging agentic web.

The goal is not to add fashionable AI files. The goal is to make a business:

1. discoverable by search engines,
2. understandable and citation-worthy for answer engines/LLMs,
3. machine-readable by compatible agents,
4. safely actionable by AI agents when the business has workflows worth exposing,
5. measurable across search, AI citations, agent use, leads, customers, and revenue.

This process is the default VLA workflow when a user asks to improve SEO, AEO/GEO, AI visibility, LLM visibility, or make a website AI-agent ready.

---

# Core architecture

Use this order. Do not skip foundations to chase experimental AI tactics.

`SEO foundation → Entity clarity → AEO/content authority → Machine discovery → API/CLI/MCP → WebMCP → Measurement & iteration`

A website can be strong in one layer and weak in another. VLA must score each layer separately.

---

# Layer 1 — Search Foundation

## Objective
Make the site easy to crawl, index, understand, and rank in conventional and generative search systems.

## Audit
Verify in production:

- HTTPS
- canonical URLs
- indexability/noindex state
- robots.txt
- XML sitemap
- internal linking
- unique page titles
- useful meta descriptions
- one clear primary topic per important page
- logical headings
- mobile usability
- Core Web Vitals/page performance where measurable
- JavaScript rendering does not hide important content
- duplicate/thin URLs controlled
- redirects and broken links
- image/video discoverability when relevant
- Search Console ownership/coverage when access exists
- Bing Webmaster Tools when useful
- IndexNow when useful for frequently updated sites

## XML sitemap
The XML sitemap is a search discovery asset. Keep it current, canonical, and limited to URLs the business actually wants indexed.

Do not confuse XML sitemap with AI-specific compatibility assets.

---

# Layer 2 — Entity + Semantic Clarity

## Objective
Make it unambiguous who the company is, what it sells, whom it serves, where it operates, and what facts are safe to state.

## Required entity facts where applicable

- canonical business name
- alternate/brand name
- business category
- products/services
- geography/service area
- contact and conversion path
- public pricing or pricing method
- operating constraints
- founder/team/authorship where relevant
- credentials/certifications only when verified
- policies/terms relevant to purchase or use

Keep these consistent across pages, structured data, profiles, directories, APIs, and machine-readable files.

## Structured data
Use truthful Schema.org/JSON-LD that matches visible page content.

Typical types:

- Organization
- LocalBusiness where factual
- Product
- Service
- Offer
- WebSite
- BreadcrumbList
- Article/BlogPosting where appropriate
- Person where relevant and factual

Do not manufacture ratings, reviews, certifications, prices, locations, inventory, or availability.

FAQ/Q&A content remains useful for humans and retrieval systems, but do not treat FAQPage markup as a special Google AI-ranking tactic. Google deprecated FAQ rich results in 2026.

---

# Layer 3 — AEO / Citation-Ready Content

## Objective
Create original, authoritative information that search and answer systems can retrieve, ground on, summarize, and cite accurately.

SEO remains the foundation. AEO/GEO is not a replacement for SEO.

## Content Authority Stack
Prioritize:

1. Entity/About page
2. Product/service pages
3. How It Works / mechanism page
4. Pricing/decision information where publishable
5. Buyer objection Q&A
6. Comparison/alternative pages
7. Evidence-backed case studies
8. Original research, data, calculators, benchmarks, directories, or tools
9. Supporting editorial/blog content

## AEO writing standard
Every important commercial/authority page should make the following easy to extract:

- direct answer to the page's core question
- explicit definitions where needed
- clear mechanism/process
- inputs and outputs
- limitations
- eligibility/exclusions
- numbers with context and timeframe
- evidence/source attribution
- comparisons using consistent dimensions
- date freshness when facts change
- named entity relationships

Use clear headings, tables, short direct answers, and structured lists when they improve human comprehension. Do not create unnatural fragments solely for AI systems.

## Originality rule
Prefer non-commodity information:

- founder/operator expertise
- real process details
- proprietary numbers/data
- real examples
- customer objections
- failures and lessons
- local/vertical expertise
- original comparisons
- primary research

Do not mass-generate hundreds of near-duplicate pages or rewrite commodity internet knowledge merely to target query variations.

## Case-study standard
If evidence exists, include:

- business/segment
- starting state
- geography
- timeframe
- budget/resources
- intervention
- measurable outcome
- what failed
- limitations
- what would be changed next

Never invent customer proof.

---

# Layer 4 — AI / Agent Discovery Assets

## Objective
Provide optional machine-readable compatibility surfaces for agents and systems that consume them.

Implement only when maintainable and truthful.

Possible assets:

- `/llms.txt`
- `/llms-full.txt`
- `/services.json` or `/products.json`
- `/ai-sitemap.json`
- `/.well-known/agent.json`
- `/openapi.json`
- `/mcp.txt` or equivalent MCP documentation
- `/cli.txt` when an actual public/API workflow exists

## Important truth
These assets are not guaranteed ranking factors.

Google Search explicitly states that `llms.txt` and other special AI text/markup files are not required for Google generative search and are ignored for Google ranking/visibility. Maintain them for compatible agents/services, not as a Google ranking hack.

## AI sitemap
An AI-oriented sitemap/catalog may provide richer metadata than XML for compatible consumers, for example:

- canonical URL
- content/entity type
- title
- concise description
- last updated
- primary entity
- service/product relationship
- structured data endpoint
- action/API relationship

Keep it derived from real canonical content so it cannot drift into a second inconsistent source of truth.

---

# Layer 5 — CLI + API + MCP

## Objective
Turn the business from content that an agent can read into capabilities that an agent/application can call.

Not every website needs this layer. Use it when users/agents benefit from deterministic business operations.

## API first
Where the business exposes deterministic operations, prefer a documented API boundary with:

- explicit request schemas
- explicit response schemas
- authentication where required
- validation
- structured errors
- idempotency for sensitive/repeated actions
- rate limits where appropriate
- truthful state/status fields

Examples:

- search catalog
- check service area
- get estimate
- check availability
- create lead
- request consultation
- create cart
- retrieve order/account-safe information

## OpenAPI
If public/partner APIs genuinely exist, publish and maintain an OpenAPI definition.

OpenAPI should describe the real production API, not fictional endpoints created for AI visibility.

## CLI
A CLI or `/cli.txt` is a compatibility/documentation surface, not an SEO ranking technique.

Use CLI guidance when it materially helps developers/agents invoke real supported APIs. Include safe examples, required inputs, authentication method, response expectations, and limitations.

Never place secrets in CLI documentation.

## Server MCP
Expose MCP when a direct agent-to-service interface is valuable.

Current MCP implementations should follow the current official specification, authorization model, and SDK guidance rather than stale protocol assumptions.

Good MCP tools are:

- narrow
- deterministic
- clearly named
- schema-defined
- permission-aware
- observable
- honest about estimates/confirmation states

Do not expose a broad `run-business` style tool.

---

# Layer 6 — WebMCP / Browser-Native Agent Actions

Use `playbooks/AI_AGENT_READINESS_WEBMCP.md`.

## Objective
Allow compatible browser agents to discover and invoke valuable website actions without guessing at buttons/DOM structure.

Map important user journeys to candidate tools.

Examples:

- `check-service-area`
- `get-quote-estimate`
- `find-product`
- `check-availability`
- `request-consultation`
- `create-lead`

Use the current WebMCP specification and feature detection.

Current WebMCP centers on browser-mediated tooling through `document.modelContext` and supports imperative tools as well as a declarative path for suitable forms.

## Safety
WebMCP must never bypass the normal business permission model.

Classify actions as:

- READ
- REVERSIBLE ACTION
- SENSITIVE/COMMITTING ACTION

Authentication, authorization, confirmation, payment protections, legal consent, and idempotency must remain intact.

Reuse the same validated business logic as the human UI.

---

# Layer 7 — Measurement

## Search metrics
Track:

- indexed pages
- crawl/index errors
- organic impressions
- organic clicks
- non-brand queries
- rankings/visibility where useful
- local visibility
- referring domains
- organic leads
- organic customers/revenue

## AI/AEO metrics
Where first-party platforms expose them, track:

- generative search impressions
- AI-cited URLs
- citation counts/trends
- grounding/retrieval queries
- AI referral traffic
- assisted conversions from AI channels
- branded/non-branded AI discovery tests as directional diagnostics

Google Search Console generative-AI reporting and Bing Webmaster Tools AI Performance should be preferred over unsupported third-party claims when available.

## Agent metrics
For API/MCP/WebMCP tools track:

- tool discovery
- tool invocation
- success/failure rate
- validation errors
- authorization failures
- completion rate
- downstream lead/order/revenue
- duplicate/idempotency events
- human-confirmation rate for sensitive actions

---

# VLA Existing-Website Upgrade Workflow

When the user says "make this site AI-ready" or equivalent:

1. Inventory the site and its money-making user journeys.
2. Audit Layer 1 search foundation.
3. Audit Layer 2 entity/schema clarity.
4. Audit Layer 3 content/citation readiness.
5. Audit Layer 4 machine-discovery assets.
6. Audit Layer 5 API/CLI/MCP opportunities.
7. Audit Layer 6 WebMCP opportunities.
8. Measure current Layer 7 visibility and attribution.
9. Score the gaps by economic value × probability × speed ÷ effort.
10. Fix fatal crawl/index/entity issues first.
11. Upgrade high-value commercial/authority content.
12. Add compatible machine-readable assets.
13. Add API/OpenAPI/MCP/CLI only where real operations justify them.
14. Add WebMCP for high-value browser actions where supported and safe.
15. Test production behavior end to end.
16. Submit/update indexing/discovery mechanisms where appropriate.
17. Record baseline metrics.
18. Re-measure, learn, and iterate.

Do not let experimental agent technology delay foundational SEO or the revenue path.

---

# AI-Native Website Score — 100 points

- Search/crawl/index foundation: 20
- Entity + structured-data clarity: 15
- AEO/content authority/citation readiness: 20
- Machine-readable discovery: 10
- API/OpenAPI/CLI/MCP readiness: 10
- WebMCP/browser-agent readiness: 10
- Trust, safety, permissions, truthfulness: 10
- Measurement + production verification: 5

Score states:

- 0–39: Legacy Web
- 40–59: Search Ready
- 60–74: AI Discoverable
- 75–89: Agent Ready
- 90–100: AI-Native / Agent-Operable

Do not award points for files that exist but are stale, false, unsupported, or unverified.

---

# Completion standard

A website is not "AI-ready" because it has schema or `llms.txt`.

An AI-native website should, where applicable:

- be crawlable and indexable,
- clearly define its entities and offers,
- contain original citation-worthy information,
- expose machine-readable facts consistently,
- offer safe deterministic API/MCP/agent actions when useful,
- expose browser-native WebMCP actions when justified,
- preserve human UX/accessibility,
- measure both search and AI/agent outcomes,
- tie visibility to qualified leads, customers, and revenue.

The economic objective is not AI visibility for its own sake. It is greater qualified discovery, lower friction for humans and agents, and more measurable business outcomes.