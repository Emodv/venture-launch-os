# Existing Business Data Onboarding

## Purpose
When VLA receives an existing business URL, public website analysis is only the first layer. Before recommending a rebuild, migration, SEO strategy, or content expansion, VLA should request access to the business's first-party performance data when available.

The objective is to preserve and compound existing SEO and conversion value rather than make decisions from the public website alone.

## Entry flow

`URL → public audit → request first-party access → analyze performance → preserve winners → identify gaps → upgrade/rebuild decision → migration/optimization plan`

## Step 1 — Public URL audit first
VLA should begin immediately from the supplied URL and should not block the initial audit while waiting for account access.

Inspect where possible:
- site architecture
- indexed/crawlable pages
- sitemap and robots
- canonicals
- content and entity coverage
- structured data
- conversion journeys
- mobile UX/performance
- AI/agent readiness
- public backlinks/citations when available
- obvious technical issues

## Step 2 — Ask for first-party Google access
After the public scan, explain that better decisions can be made using the business's real historical data.

Preferred user-facing request:

> I can already audit the public website. To make sure we preserve what is already working, sign in with the Google account that has access to your website's Google products and authorize the available properties. If you have Google Analytics (GA4), Google Search Console, Google Business Profile, Google Ads, Merchant Center, or other relevant Google properties, connecting them lets me see the site's actual search, traffic and conversion history before I recommend changes.

Do not ask the user to share passwords. Use OAuth/official account authorization where supported. Request only the scopes required for the analysis or approved execution.

## Step 3 — Prioritize connected data

### Google Search Console
Analyze where available:
- queries
- pages
- clicks
- impressions
- CTR
- average position
- country/device
- indexing/coverage
- sitemap status
- Core Web Vitals where exposed
- generative AI visibility/performance where available

Use the data to identify:
- pages already winning
- queries ranking near page-one/top positions
- high-impression low-CTR opportunities
- pages losing visibility
- content clusters with demonstrated demand
- queries with no strong matching landing page
- URLs that must be preserved during migration

### Google Analytics 4
Analyze where available:
- landing pages
- traffic sources
- engagement
- conversion/key events
- lead or ecommerce paths
- device/geography
- organic landing-page quality
- assisted conversion behavior when available

Do not optimize only for traffic. Prefer pages and queries that contribute to qualified leads, customers, revenue, or another agreed business outcome.

### Google Business Profile
When relevant to a local business, inspect available business/location performance and ensure identity, location, hours, services and website data are consistent.

### Google Ads
When authorized and relevant, use paid-search data as additional demand intelligence: converting search themes, landing pages, geographies and commercial intent. Do not assume paid and organic performance are interchangeable.

### Merchant Center
For commerce businesses, use available product/feed data to understand products, eligibility, coverage and consistency with website structured data.

## Step 4 — Build the Preservation Map
Before changing URLs or replacing the website, create a preservation map for valuable assets.

For each important existing URL record where evidence exists:
- URL
- primary topic/entity
- organic queries
- impressions/clicks
- conversions/revenue contribution
- backlinks/citations when available
- replacement URL if changing
- canonical decision
- redirect requirement
- content to preserve
- content to improve

Never delete or materially change a proven page solely because the design is old.

## Step 5 — Double down on demonstrated demand
Use first-party evidence to decide what to expand.

Examples:
- strengthen a page already ranking for valuable queries
- create a dedicated landing page when one page ranks weakly for several distinct high-value intents
- build supporting content around a proven topic cluster
- improve title/snippet alignment for high-impression low-CTR pages
- add original Q&A, comparisons, case studies, calculators or evidence around topics already attracting qualified users
- improve conversion UX on organic landing pages with strong traffic but weak outcomes

Avoid creating dozens of near-duplicate pages simply because query variations exist.

## Step 6 — Decide Upgrade vs Rebuild
Choose based on evidence.

### Upgrade in place
Prefer when the current CMS/codebase is maintainable and important SEO equity can be improved without replacement.

### Progressive modernization
Prefer when valuable pages/URLs should remain while sections, templates, backend capabilities and agent technology are modernized incrementally.

### Controlled rebuild/migration
Prefer when the existing technology meaningfully blocks performance, security, conversion, maintainability, structured data, or agent readiness.

A rebuild must include URL mapping, redirects, canonicals, metadata/content preservation, analytics continuity, Search Console continuity, sitemap updates and post-launch monitoring.

## Step 7 — Add AI-native layers
After preservation decisions, apply:
- `SEO_AEO_AI_VISIBILITY.md`
- `AI_NATIVE_WEBSITE_OPTIMIZATION.md`
- `AI_AGENT_READINESS_WEBMCP.md`

This may include schema/entity improvements, answer/citation authority, machine-readable assets, APIs, CLI documentation, MCP and WebMCP where appropriate.

## Step 8 — Baseline before launch
Record pre-change baselines so VLA can determine whether the transformation helped or harmed the business.

Track where available:
- organic clicks/impressions
- valuable query positions
- indexed valuable URLs
- organic conversions/revenue
- top landing pages
- AI citations/visibility where available
- leads/customer outcomes

## Step 9 — Post-migration verification
After deployment verify:
- redirects
- canonical URLs
- sitemap
- robots/noindex
- analytics events
- Search Console/indexing
- priority URL availability
- structured data
- conversion flows
- agent interfaces
- performance

Watch proven pages and queries closely after migration. If performance deteriorates, diagnose before continuing large-scale changes.

## Permission principle
First-party access is optional but high-value. VLA should clearly explain why access helps, request it through supported authorization flows, and continue with public evidence if the user declines or lacks access.

Never request or store a user's Google password.

## Core rule
For an existing business, the website is not a blank canvas. Historical search, traffic, conversion, customer and authority data are business assets. VLA must discover and preserve those assets before transformation, then use them to decide where to double down.