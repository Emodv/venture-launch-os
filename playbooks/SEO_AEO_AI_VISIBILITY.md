# SEO + AEO + AI Visibility Playbook

## Objective
Create factual, crawlable, useful content that can rank in search, participate in generative search, and be cited or understood by AI answer engines.

For the full website modernization process, use `playbooks/AI_NATIVE_WEBSITE_OPTIMIZATION.md`.

## Operating principle
SEO remains the foundation. AEO/GEO extends the objective from ranking and clicks toward retrieval, grounding, citation, and qualified discovery.

Do not replace foundational SEO with speculative AI hacks.

## 1. Establish entity clarity
Publish consistent facts for:

- business name
- category
- location/service area
- services/products
- pricing model where public
- contact/booking path
- operating constraints
- authors/founders where relevant

Use consistent naming across website, schema, directories, profiles, APIs, and machine-readable files.

## 2. Technical baseline
Verify in production:

- HTTPS
- one canonical URL per page
- unique title/meta description
- logical H1/H2 structure
- XML sitemap
- robots.txt
- internal links
- mobile performance
- indexable public pages
- no accidental staging/noindex directives
- duplicate/thin URLs controlled
- JavaScript does not hide essential content
- Search Console/Bing Webmaster diagnostics when access exists

## 3. Content authority architecture
Prioritize:

1. Core service/product pages.
2. Entity/About information.
3. How It Works / mechanism.
4. Pricing/decision guides where appropriate.
5. Buyer objection Q&A.
6. Comparison and alternative pages.
7. Evidence-backed case studies.
8. Proprietary calculators/data/resources.
9. Supporting editorial content.

Avoid thin doorway pages, scaled filler, and near-duplicate query pages.

## 4. AEO / citation readiness
Make important pages easy to retrieve and cite accurately by including, where useful:

- direct answers
- explicit definitions
- clear mechanisms/processes
- inputs and outputs
- limitations/exclusions
- evidence and source attribution
- numbers with timeframe/context
- comparison tables using consistent criteria
- freshness/update dates for changing facts

Write for humans first. Clear structure also improves machine extraction.

## 5. Structured data
Use only schema supported by visible facts, such as:

- Organization / LocalBusiness
- Product
- Service
- Offer
- WebSite
- BreadcrumbList
- Article/BlogPosting
- Person where appropriate

Do not manufacture reviews, ratings, certifications, locations, offers, inventory, or availability.

Q&A/FAQ content can still be useful, but do not treat `FAQPage` markup as a special Google visibility tactic; Google deprecated FAQ rich results in 2026.

## 6. AI discovery layer
Use `templates/AI_DISCOVERY_TEMPLATE.md` and `playbooks/AI_NATIVE_WEBSITE_OPTIMIZATION.md`.

Possible compatibility assets include:

- `/llms.txt`
- `/llms-full.txt`
- `/services.json`
- `/ai-sitemap.json`
- `/.well-known/agent.json`
- `/openapi.json`
- MCP documentation/endpoints
- `/cli.txt` when real API/CLI workflows exist

These are compatibility surfaces, not guaranteed ranking factors. Google Search explicitly does not require `llms.txt` for generative search visibility.

## 7. Agent technology
For interactive/transactional sites, assess:

- OpenAPI
- server MCP
- safe deterministic APIs
- CLI documentation for supported APIs
- WebMCP/browser-native tools

Use `playbooks/AI_AGENT_READINESS_WEBMCP.md` for WebMCP implementation and safety.

The goal is to make the business increasingly machine-operable without bypassing authentication, authorization, confirmation, or existing business safeguards.

## 8. Citation-worthy assets
Build assets worth referencing:

- original research
- calculators
- local/industry pricing benchmarks
- market data
- comparison tables
- primary surveys
- useful directories
- checklists/process guides
- evidence-backed case studies

## 9. Off-page authority
Prioritize:

1. Google Business Profile where eligible.
2. Bing Places where relevant.
3. Municipality/chamber/industry citations.
4. Real partner links.
5. Local/editorial coverage.
6. Review platforms customers actually use.
7. Relevant associations.

Avoid PBNs, paid spam links, fake mentions, and mass directory blasts.

## 10. Measurement
Track:

### Search
- indexed pages
- organic impressions/clicks
- non-brand queries
- local visibility
- referring domains
- organic leads/customers/revenue

### AI/AEO
- generative-search impressions when available
- cited URLs
- AI citation counts/trends
- grounding/retrieval queries where available
- AI referral traffic
- AI-assisted conversions

Prefer first-party measurements such as Google Search Console generative-AI reporting and Bing Webmaster Tools AI Performance when available.

### Agent interactions
When API/MCP/WebMCP exists track:
- tool discovery
- invocations
- success/failure rate
- validation/auth errors
- downstream leads/orders/revenue

## Launch gate
SEO/AEO/AI visibility work is not complete until production URLs, structured assets, critical pages, and applicable agent interfaces are tested live and revenue attribution exists.
