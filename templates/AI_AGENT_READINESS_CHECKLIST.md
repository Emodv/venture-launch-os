# AI Agent Readiness Checklist

Use this for every new venture and every existing website modernization.

## Search Discovery
- [ ] `sitemap.xml` valid and current
- [ ] `robots.txt` intentional
- [ ] canonical URLs correct
- [ ] important pages indexable
- [ ] descriptive titles/headings
- [ ] strong internal linking

## Semantic Clarity
- [ ] Organization/LocalBusiness schema where factual
- [ ] Service/Product/Offer schema where factual
- [ ] WebSite/Breadcrumb schema where useful
- [ ] clear About/entity page
- [ ] explicit How It Works
- [ ] buyer objection Q&A
- [ ] structured service/product data

## AI / Machine Discovery
- [ ] `llms.txt` when useful
- [ ] `llms-full.txt` when useful
- [ ] `services.json` or equivalent
- [ ] `ai-sitemap.json` when useful
- [ ] agent manifest when useful
- [ ] OpenAPI spec if public APIs exist
- [ ] server MCP docs/endpoint if genuinely implemented

## WebMCP
- [ ] audit primary user journeys for agent-operable actions
- [ ] identify top-value tool candidates
- [ ] use current `document.modelContext` specification
- [ ] feature-detect support
- [ ] narrow stable tool names
- [ ] explicit input schemas
- [ ] structured deterministic results
- [ ] reuse validated application logic
- [ ] classify read/reversible/sensitive actions
- [ ] enforce authentication/authorization
- [ ] confirmation for sensitive commitments
- [ ] duplicate/idempotency protection where needed
- [ ] test valid/invalid inputs
- [ ] test errors/cancellation where applicable
- [ ] verify production behavior

## Truth & Safety
- [ ] estimates remain estimates
- [ ] availability is not invented
- [ ] booking/order state is explicit
- [ ] no invented reviews/certifications/partners
- [ ] no permission bypass
- [ ] agent cannot perform more than authorized human workflow

## Verification
- [ ] tools discoverable in supported test environment
- [ ] tool schemas inspect correctly
- [ ] at least one real end-to-end tool invocation verified when WebMCP is implemented
- [ ] human UI remains functional and accessible
- [ ] readiness score recorded

## Score
- Search discovery: /15
- Entity/schema clarity: /15
- Structured content/data: /15
- Agent discovery assets: /10
- WebMCP actionable coverage: /20
- Reliability/validation: /10
- Security/permissions: /10
- Production verification: /5

**Total: /100**
