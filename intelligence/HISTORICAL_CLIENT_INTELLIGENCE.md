# Historical Client Intelligence Layer

## Objective
Turn years of historical SEO, PPC, analytics, local, ecommerce, proposal, and client-decision evidence into a proprietary VLA learning system.

This layer is designed to answer a harder question than "what should we do?":

> Across comparable businesses, what patterns have repeatedly produced qualified demand, conversions, revenue, search visibility, and durable authority — and under what conditions?

## Privacy boundary
The public Venture Launch OS repository MUST NOT contain raw client data, Gmail message IDs, Google Drive file IDs, account IDs, API credentials, personally identifiable customer data, confidential revenue figures, or client-private strategy documents.

Public repo contents may include:
- schemas
- scoring logic
- ingestion contracts
- anonymized examples
- benchmark methodology
- tests with synthetic fixtures

Private historical evidence belongs in an authorized private data store such as a private Supabase project, private database, or controlled Google Workspace destination.

## Source classes
Historical evidence can come from:

1. Google Search Console
   - queries
   - pages
   - clicks
   - impressions
   - CTR
   - average position

2. Google Analytics / GA4
   - landing pages
   - acquisition source
   - sessions/users
   - engagement
   - key events/conversions
   - attributed revenue when available

3. Google Ads
   - campaigns
   - ad groups
   - search terms
   - keywords
   - spend
   - CPC
   - conversions
   - CPA / ROAS

4. Google Business Profile / Merchant Center
   - profile/search visibility
   - calls/actions
   - product/ecommerce performance

5. SEO operations
   - keyword plans
   - backlinks
   - technical audits
   - content plans
   - landing-page maps
   - migrations/redesigns

6. Strategy and decision context
   - proposals
   - client emails
   - campaign briefs
   - meeting notes
   - launch calendars
   - implementation plans

7. Outcome evidence
   - leads
   - qualified leads
   - customers
   - revenue
   - customer value
   - retention
   - known failures

## Canonical client intelligence record
Each historical client should normalize into one record with these major sections:

- identity
- business_context
- audience_map
- source_inventory
- seo
- ppc
- analytics
- local_and_commerce
- strategy
- experiments
- outcomes
- learnings
- data_quality

Client identity should use a private stable client_id. The public system should never require the real business name.

## Data Quality Score
Score each client from 0–100 using evidence completeness, not perceived success.

### Dimensions
- Business context: 10
- Search Console / organic evidence: 15
- GA4 / analytics evidence: 15
- Google Ads / paid evidence: 15
- Landing-page / content mapping: 10
- Strategy / implementation context: 10
- Outcome / conversion evidence: 15
- Time-series depth: 5
- Cross-source joinability: 5

### Interpretation
- 0–29: weak anecdotal evidence
- 30–49: partial historical record
- 50–69: usable case study
- 70–84: strong benchmark candidate
- 85–100: gold-standard learning case

High scores do not imply good marketing performance. They mean the case is reliable enough to learn from.

## Cross-source join key
The highest-value relationship is:

`Audience -> Query/Search Term -> Landing Page -> Session/Click -> Lead -> Qualified Lead -> Customer -> Revenue`

When exact joins are not possible, preserve the uncertainty level:
- VERIFIED
- STRONGLY_SUPPORTED
- INFERRED
- UNKNOWN

Never collapse inferred attribution into verified attribution.

## SEO/PPC crossover intelligence
Use paid-search evidence to improve organic prioritization.

Examples:
- paid search term converts well but organic coverage is weak -> SEO/AEO opportunity
- organic query drives traffic but paid term shows poor commercial quality -> deprioritize vanity traffic
- paid landing page converts strongly -> candidate organic/service-page pattern
- expensive high-converting CPC cluster -> possible organic moat opportunity

This does not mean PPC conversion automatically proves SEO intent will behave identically. Treat channel transfer as a hypothesis and verify.

## Experiment reconstruction
For each material historical change, create an experiment record:

- hypothesis
- date_range
- audience
- channel
- action
- affected_pages_or_campaigns
- baseline
- observed_result
- outcome_metric
- confidence
- confounders
- learning
- reusable_pattern

Examples:
- landing-page rebuild
- new service-area pages
- keyword/ad-group restructure
- bidding change
- content cluster launch
- backlink campaign
- technical migration
- seasonal geo-targeted campaign

## Cross-client benchmark engine
Aggregate only compatible cases.

Segment benchmarks by dimensions such as:
- industry
- B2B vs B2C
- local vs national
- lead generation vs ecommerce
- geography
- average customer value
- sales-cycle length
- channel
- audience intent

Do not create one universal SEO/PPC benchmark across incomparable businesses.

Potential benchmark outputs:
- conversion quality by audience/query class
- paid-to-organic opportunity gaps
- landing-page patterns associated with stronger conversion
- query positions where incremental organic gains paid off
- content formats associated with citations or leads
- backlink/authority patterns by vertical
- time-to-impact distributions
- typical failure modes

## First 10-client workflow
1. Search connected Gmail and Drive for candidate clients.
2. Build a source inventory for each candidate.
3. Score data quality.
4. Select top 10 by evidence richness and strategic diversity.
5. Reconstruct the top 3 end-to-end.
6. Extract reusable patterns only where evidence supports them.
7. Store case-level evidence privately.
8. Feed validated learnings into VLA benchmark retrieval.

## Runtime behavior
When VLA evaluates a new venture or existing business, it may retrieve comparable historical patterns only when:
- the comparison dimensions are materially similar
- evidence quality clears the configured threshold
- private client identity is not exposed
- any numeric benchmark includes sample size and confidence

VLA should prefer statements like:

> In 4 comparable local-service cases with strong evidence, service-specific landing pages produced higher qualified-lead rates than broad informational traffic.

and avoid:

> This always works.

## Moat
The defensible asset is not the raw files themselves. It is the accumulated, evidence-linked map of:

`audience -> intent -> acquisition -> page/offer -> conversion -> economics -> experiment -> outcome`

combined across years of real operating history.
