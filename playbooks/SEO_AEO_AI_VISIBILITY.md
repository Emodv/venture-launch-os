# SEO + AEO + AI Visibility Playbook

## Objective
Create factual, crawlable, useful content that can rank in search, participate in generative search, and be cited or understood by AI answer engines.

For the full website modernization process, use `playbooks/AI_NATIVE_WEBSITE_OPTIMIZATION.md`.
For audience prioritization, use `playbooks/AUDIENCE_FIRST_SEO.md`.
For prompt/query fan-out and citation strategy, use `playbooks/AEO_QUERY_FANOUT_CITATION_ENGINE.md`.

## Operating principle
SEO remains the foundation. AEO/GEO extends the objective from ranking and clicks toward retrieval, grounding, citation, and qualified discovery.

Do not replace foundational SEO with speculative AI hacks.
Do not start with keyword volume. Start with commercially meaningful audience segments, then size search demand and opportunity within those segments.
Do not stop at one head term. Map the related prompts, subquestions, comparisons, entities, and decision modifiers that an AI system may retrieve around the topic.

## 0. Audience-first prioritization
Before large-scale keyword research, define and rank audience segments.

Use three primary dimensions:

1. business value
2. search demand
3. ranking attainability / difficulty

When reliable first-party conversion data exists, include conversion evidence as a refining factor.

A smaller, high-value audience should outrank a massive low-value segment when the expected economic outcome is stronger.

For each SEO/AEO roadmap, explicitly state which high-volume audiences/keywords will NOT be prioritized and why.

## 1. Query fan-out and AI satisfiability
For every priority audience/topic, build a Prompt/Topic Graph rather than a flat keyword list.

Include where relevant:

- core question
- definitions
- alternatives
- comparisons
- pricing/cost
- pros/cons
- eligibility/fit
- implementation/how-to
- risks/limitations
- proof/reviews
- geographic variants
- role/industry/use-case modifiers
- freshness/current-year modifiers
- brand-vs-brand queries
- decision prompts such as best, top, worth it, should I, which

Classify important prompts using an AI satisfiability filter:

- CLICK-DEPENDENT — the answer usually requires a visit/action
- CITATION-FIRST — an AI answer can plausibly satisfy the user without a click; optimize for brand mention/citation/inclusion
- HYBRID — optimize for both citation and downstream click/conversion

Do not judge CITATION-FIRST topics only by CTR.

## 2. Establish entity clarity
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

## 3. Technical baseline
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
- CDN/WAF/Cloudflare rules do not unintentionally block relevant search/AI crawlers

Before changing crawler policy, verify current official documentation and the site owner's preferences. Do not weaken security to gain crawler access.

## 4. Content authority architecture
Build the content architecture around priority audiences and prompt clusters, not a generic keyword list.

Prioritize:

1. Core service/product pages for the highest-value audience segments.
2. Entity/About information.
3. How It Works / mechanism.
4. Pricing/decision guides where appropriate.
5. Buyer objection Q&A.
6. Comparison and alternative pages.
7. Evidence-backed case studies.
8. Proprietary calculators/data/resources.
9. Supporting editorial content.

Avoid thin doorway pages, scaled filler, and near-duplicate query pages. Consolidate related prompts into strong canonical resources.

## 5. Audience + citation gap analysis
Run content/search gaps against the priority audience and prompt graph.

Ask:

- What does this audience need to know before buying?
- Which questions/queries/prompts do they use?
- Which high-value needs do competitors answer better?
- Which prompts mention/cite competitors but not the brand?
- Which third-party publications or communities shape the category?
- Which existing pages already have authority but need improvement?
- Which proof, comparisons, tools, or decision support are missing?
- Which pages get traffic from the wrong audience?

Prefer filling high-value audience/citation gaps over copying every competitor keyword.

## 6. AEO / citation readiness
Make important pages easy to retrieve and cite accurately.

Use three citation-probability levers as planning heuristics:

### Consensus
Build consistent factual entity/positioning across credible owned and third-party sources.

### Freshness
Keep changing facts, comparisons, prices/data, and important pages substantively reviewed and current. Do not update dates without a real review/update.

### Authority
Build traditional SEO authority, useful editorial references, expert authorship, original research/data, evidence-backed case studies, and coherent internal topic architecture.

These levers increase the quality of the information environment; they do not guarantee citations.

## 7. AI-reusable writing standard
For priority pages:

- use BLUF (Bottom Line Up Front) when a direct answer is expected;
- answer one coherent sub-question per atomic section;
- use descriptive headings;
- use simple declarative sentences where clarity benefits;
- state entities explicitly instead of relying on ambiguous pronouns;
- use lists for enumerations and tables for consistent comparisons;
- include limitations/exclusions;
- include evidence/source attribution;
- give numbers with geography/timeframe/context;
- surface the answer before long background sections.

Write for humans first. Do not keyword-stuff or make prose unnatural for machines.

## 8. Structured data
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

## 9. AI discovery layer
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

These are compatibility surfaces, not guaranteed ranking factors.

## 10. Agent technology
For interactive/transactional sites, assess:

- OpenAPI
- server MCP
- safe deterministic APIs
- CLI documentation for supported APIs
- WebMCP/browser-native tools

Use `playbooks/AI_AGENT_READINESS_WEBMCP.md` for WebMCP implementation and safety.

The goal is to make the business increasingly machine-operable without bypassing authentication, authorization, confirmation, or existing business safeguards.

## 11. Citation-worthy assets
Build assets worth referencing for the target audience:

- original research
- calculators
- local/industry pricing benchmarks
- market data
- comparison tables
- primary surveys
- useful directories
- checklists/process guides
- evidence-backed case studies

## 12. Audience map → PR / community / YouTube
Use the same priority-audience + prompt map to drive authority building outside the site.

Choose:

- research topics
- surveys
- data stories
- expert commentary
- publications
- journalists
- industry partners
- authentic Reddit/Quora participation where appropriate
- YouTube topics/search opportunities
- podcasts/webinars

based on whether they influence the priority audience.

For YouTube, when relevant:
- answer high-value prompt clusters directly;
- state the answer early;
- use clear titles and chapters;
- provide accurate descriptions/links;
- consider a supporting webpage/transcript;
- keep factual content current.

The objective is not generic backlinks or manufactured mentions. It is credible authority and distribution in the environments that shape decisions.

## 13. Off-page authority
Prioritize:

1. Google Business Profile where eligible.
2. Bing Places where relevant.
3. Municipality/chamber/industry citations.
4. Real partner links.
5. Local/editorial coverage.
6. Review platforms customers actually use.
7. Relevant associations.
8. Relevant editorial/community/video surfaces from the priority Prompt Graph.

Avoid PBNs, paid spam links, fake mentions, sockpuppets, synthetic community posts, and mass directory blasts.

## 14. Measurement
Track traffic and rankings by audience/segment where possible, not only sitewide totals.

### Search
- indexed pages
- organic impressions/clicks
- non-brand queries
- audience/segment traffic
- qualified organic leads
- conversion rate by landing page/segment
- revenue/customer value by organic segment where attributable
- local visibility
- referring domains

### AI/AEO
- priority prompt/topic coverage
- observable brand mentions
- cited URLs
- competitor citation share where measurable
- grounding/retrieval queries where available
- AI referral traffic
- AI-assisted conversions
- self-reported attribution including AI assistant/search options
- crawler/bot activity where server/CDN logs exist

Bot visits are access/retrieval signals, not proof that a citation occurred.

Prefer first-party measurements such as Google Search Console, GA4, server/CDN logs, CRM/revenue outcomes, and Bing Webmaster Tools when available.

### Agent interactions
When API/MCP/WebMCP exists track:
- tool discovery
- invocations
- success/failure rate
- validation/auth errors
- downstream leads/orders/revenue

## Existing-business rule
For Mode B transformations, do not finalize the SEO/AEO roadmap before requesting relevant first-party data access.

Sequence:

`public audit → first-party data → Preservation Map → Audience Map → Prompt/Topic Fan-Out → demand sizing → audience/citation gap analysis → roadmap/migration`

Preserve URLs that generate valuable qualified traffic/conversion even when raw traffic is modest.

## Launch gate
SEO/AEO/AI visibility work is not complete until production URLs, structured assets, critical pages, applicable agent interfaces, crawler-access policy, prompt/citation measurement, and audience/economic measurement are tested live.
