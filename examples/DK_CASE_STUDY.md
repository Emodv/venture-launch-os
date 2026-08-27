# DK / Dry Kleaning — Venture Launch OS Reference Implementation

## Purpose
DK is the first reference implementation of Venture Launch OS. It shows how a local-service idea can become a measurable operating system without starting with heavy owned infrastructure.

Source implementation: `Emodv/dk-platform`

## Initial thesis
A pickup-and-delivery cleaning concierge can reduce customer friction by making quoting and service discovery digital while using partner fulfillment rather than buying a traditional dry-cleaning store before demand is proven.

## Strategic decisions

### 1. Avoid premature infrastructure
The initial model prioritizes partner processing and variable-cost fulfillment rather than buying a store, fleet, or plant.

### 2. Revenue-first mobile experience
The website is designed around a fast quote/booking path rather than a brochure-only homepage.

### 3. Structured service and geography architecture
DK uses dedicated service pages and local pages so humans, search engines, and AI systems can understand what is offered and where.

### 4. Backend-style public interfaces
The implementation includes machine-readable endpoints and files for service-area lookup and estimated quoting.

### 5. Truth boundaries for agents
Pricing, booking, and availability are explicitly labelled so an AI agent cannot turn an estimate into a confirmed commercial promise.

## Technical pattern extracted

### Human-facing layer

- mobile-first homepage
- quote interface
- service pages
- geography pages
- guides/resources
- booking/contact path

### Search/discovery layer

- `sitemap.xml`
- `robots.txt`
- service/location internal linking
- structured content
- guides and comparison/pricing content

### AI/agent layer

- `llms.txt`
- `llms-full.txt`
- `services.json`
- `ai-sitemap.json`
- `/.well-known/agent.json`
- `openapi.json`
- MCP-compatible endpoint
- CLI/curl documentation

### API layer

- service-area/availability lookup
- estimated quote endpoint
- MCP JSON-RPC endpoint

## Important reusable lesson
The valuable asset is not the DK design or dry-cleaning pricing. It is the architecture:

`idea → lean offer → mobile funnel → structured data → safe public APIs → search/AI discovery → lead capture → operating loop`

Each new venture should reuse the pattern while replacing all DK-specific claims, geography, pricing, services, and economics with evidence for the new business.

## What DK proves

DK demonstrates that Venture Launch OS can produce more than a landing page. The output can include:

- a production website
- conversion funnel
- service catalog
- geographic expansion architecture
- machine-readable business identity
- quote logic
- availability logic
- agent-safe policies
- SEO/AEO foundation
- reusable operating workflows

## What remains venture-specific
Never copy these blindly from DK:

- prices
- margins
- service area
- fulfillment partners
- delivery promises
- certifications
- customer proof
- legal/compliance requirements

Mark unknown facts `[PLACEHOLDER]` until verified.

## Reference checklist for future launches

A future venture should be considered structurally comparable to DK when it has:

- [ ] clear economic thesis
- [ ] validated or explicitly hypothesized offer
- [ ] production domain
- [ ] source-controlled repository
- [ ] live mobile-first funnel
- [ ] central lead/order persistence
- [ ] analytics and attribution
- [ ] service/product catalog
- [ ] SEO technical baseline
- [ ] structured data
- [ ] AI discovery files
- [ ] safe public APIs where useful
- [ ] CRM/notification workflow
- [ ] GTM channel test
- [ ] unit-economics measurement
- [ ] weekly bottleneck review
