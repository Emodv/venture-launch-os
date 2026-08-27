# Analytics, Attribution + Production QA Playbook

## Objective
Make the launch measurable, debuggable, and verifiable before scaling acquisition.

## Measurement hierarchy
Track business outcomes, not only traffic.

Minimum events where applicable:

- page_view
- primary_cta_click
- form_or_quote_start
- step_complete
- form_or_quote_complete
- lead_created
- booking_created
- checkout_started
- purchase/payment_success
- qualified
- won
- lost
- refund/cancel

## Attribution
Persist when available:

- source
- medium
- campaign
- content/creative
- term/query where available
- landing page
- referrer
- first-touch timestamp
- lead/customer ID

Preserve attribution into the CRM/database rather than leaving it only in browser analytics.

## KPI ladder
Report:

`traffic → engaged/started → lead/quote → qualified/booked → won → revenue → contribution margin`

Calculate where possible:

- conversion rate by stage
- CAC
- cost per qualified opportunity
- AOV/ACV
- gross contribution
- LTV
- payback
- repeat/retention

## Data quality rules
Before using a metric to make decisions:

- verify event fires once when intended
- exclude obvious test/internal traffic where practical
- confirm IDs/values/currency
- reconcile revenue with payment/accounting source when material
- label estimated metrics

## Production QA
Test the production URL, not only preview/local.

### Functional
- navigation
- CTA
- forms/quotes
- validation
- successful submission
- persistence
- CRM/notifications
- payment path
- error states

### Mobile
Test at 375px, 390px, and 430px first:

- no overflow
- readable type
- tap targets
- keyboard/form behavior
- sticky UI does not hide content
- carousel/swipe works
- primary CTA remains obvious

### Search
Verify:

- 200 status on canonical pages
- canonical tags
- titles/descriptions
- sitemap.xml
- robots.txt
- indexability/noindex
- internal links
- structured data is syntactically valid and factual

### AI/machine-readable
Verify all intended files resolve and contain production values:

- llms.txt
- services/data catalogs
- agent manifest
- OpenAPI
- MCP docs/endpoint if implemented
- AI sitemap if used

These are machine-consumption aids, not guaranteed ranking factors.

### Performance/reliability
Check:

- core pages load acceptably on mobile
- images/assets are optimized
- no obvious runtime/console errors
- API failure modes are handled
- monitoring/logging exists when business risk justifies it

## Verification status
Every milestone must be one of:

- VERIFIED
- IMPLEMENTED, NOT VERIFIED
- BLOCKED
- NOT APPLICABLE

Never use “done” when verification has not occurred.
