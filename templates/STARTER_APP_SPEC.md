# Starter Application Specification

## Objective
Define the reusable production skeleton that an AI agent can clone or reproduce for a new venture without rebuilding basic infrastructure from zero.

## Required capabilities

### Frontend
- mobile-first layout
- Quiet Luxury / Quiet Power design defaults
- centralized content where appropriate
- configurable hero/value proposition
- service/product sections
- progressive conversion flow
- carousel component for suitable multi-option content
- FAQ/Q&A blocks
- case-study/comparison content blocks
- responsive navigation
- accessible states

### Lead/conversion
- step-based lead/quote form
- server-side validation
- anti-spam protection
- success/error states
- attribution capture
- database persistence
- configurable notification hook

### Data model
At minimum:

- leads/customers
- source/UTM fields
- geography
- requested product/service
- stage/status
- estimated value
- timestamps
- notes

### Analytics
Provide event hooks for:

- primary CTA
- funnel start
- step completion
- form/quote completion
- lead creation
- booking/purchase when applicable

### SEO
- canonical metadata
- title/meta templates
- sitemap
- robots
- structured data helpers
- breadcrumbs where needed
- service/location page template

### AI discovery
Configurable generation for:

- llms.txt
- services.json
- `/.well-known/agent.json`
- openapi.json when APIs exist
- AI sitemap if useful

### APIs
Reusable safe patterns for:

- availability/eligibility
- quote/estimate
- lead submission
- health/status where useful

Every commercial API must distinguish estimates from confirmed commitments.

### Deployment
Target GitHub + Vercel by default with:

- environment variable documentation
- `.env.example`
- build scripts
- production-domain configuration instructions
- no secrets committed

## Venture configuration
A future starter should centralize business-specific facts in a small configuration surface, such as:

- business name
- domain
- geography
- contact
- services
- prices or pricing model
- colors/type choices if customized
- social links
- legal links
- analytics IDs
- API feature flags

## Safety rule
The starter may provide placeholders and code patterns, but must never ship DK-specific pricing, customer data, providers, credentials, reviews, guarantees, service areas, or unverifiable claims into a new venture.

## Definition of success
A new business should be able to move from approved venture configuration to a deployable MVP primarily through configuration and content replacement rather than re-architecting the entire stack.