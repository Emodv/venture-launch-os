# AI Agent Readiness + WebMCP

## Purpose
Make every applicable Venture Launch OS website understandable, discoverable, and operable by modern AI agents.

This playbook covers four layers:

1. Search discovery — XML sitemap, canonical URLs, robots, structured internal linking.
2. Machine-readable understanding — Schema.org, services/catalog JSON, llms.txt, llms-full.txt, agent manifest/OpenAPI/MCP docs where useful.
3. Browser-native agent actuation — WebMCP tools and declarative forms.
4. Verification — prove agents can discover, invoke, and safely complete allowed actions.

## Current WebMCP source of truth
Use the Web Machine Learning Community Group WebMCP specification/repository as the primary reference:

- https://github.com/webmachinelearning/webmcp
- https://webmachinelearning.github.io/webmcp/

Treat older community WebMCP implementations as historical/reference material only unless they explicitly track the current specification.

As of August 2026, WebMCP is a Community Group draft/proposal rather than a finalized W3C Recommendation. Implement progressively and avoid claiming universal browser/agent support.

## What WebMCP does
WebMCP lets a webpage expose structured client-side tools that compatible AI agents can discover and invoke through the browser instead of guessing how to click through the DOM.

Current imperative API centers on:

`document.modelContext.registerTool()`

A tool should define:

- stable name
- plain-language description
- JSON-compatible input schema
- deterministic execution callback
- structured return value

The browser mediates discovery and execution.

There is also a declarative path for suitable HTML forms so standard user actions can be represented as tools without replacing the human UI.

## VLA Agent-Ready Website Standard
For every new website, and for existing-site modernization work, VLA should assess and implement the applicable layers below.

### Layer 1 — Search-readable
Required where applicable:

- valid `sitemap.xml`
- correct canonical URLs
- intentional `robots.txt`
- indexable primary content
- descriptive page titles/headings
- internal links between important entities/pages
- no accidental noindex or crawler blocks

### Layer 2 — Semantically machine-readable
Required where factual and useful:

- Schema.org JSON-LD
- Organization or LocalBusiness identity
- products/services/offers when real
- WebSite/BreadcrumbList
- structured service/catalog data
- clear How It Works mechanism
- buyer Q&A
- entity/About information

Optional compatibility assets:

- `/llms.txt`
- `/llms-full.txt`
- `/services.json`
- `/ai-sitemap.json`
- `/.well-known/agent.json`
- `/openapi.json`
- MCP documentation/endpoints when they genuinely exist

These improve machine legibility for compatible consumers. Do not describe them as guaranteed search ranking factors.

### Layer 3 — Agent-operable with WebMCP
Identify the highest-value actions an agent should be able to perform on behalf of a user.

Examples:

#### Local/service business
- check service area
- check availability
- calculate estimate
- request quote
- select service
- create lead
- schedule consultation

#### Ecommerce
- search products
- get product details
- check inventory
- add/remove cart item
- apply valid promotion
- initiate checkout

#### SaaS/B2B
- search documentation
- calculate plan/fit
- request demo
- create trial
- schedule meeting
- retrieve account-safe information after authentication

Do not expose an action merely because the UI has a button. Expose actions that create material user value and can be implemented safely and deterministically.

## WebMCP tool design rules

### 1. One job per tool
Prefer narrow names such as:

- `check-service-area`
- `get-quote-estimate`
- `find-product`
- `request-consultation`

Avoid vague names such as `do-action` or `manage-business`.

### 2. Describe outcomes, not implementation
Tool descriptions should state exactly what the user will receive and any limitations.

### 3. Structured inputs
Use explicit schemas, required fields, enums, bounds, and human-readable descriptions.

### 4. Structured outputs
Return stable structured results where possible, including identifiers/status and explicit caveats.

### 5. Reuse real application logic
The WebMCP execution callback should call the same validated application/service logic used by the human interface. Do not maintain a separate, inconsistent agent-only business process.

### 6. Truth boundaries
If price is estimated, return `estimated`.
If availability requires confirmation, return that state.
If an order/booking is not final, never imply confirmation.

### 7. Authentication and authorization
Respect the user's existing authenticated browser context. Never use WebMCP to bypass permission checks.

### 8. Side-effect classification
Classify tools internally as:

- READ — information retrieval only
- REVERSIBLE ACTION — forms/cart/navigation or other reversible state
- SENSITIVE ACTION — payment, booking commitment, subscription, deletion, legal/financial commitment

Sensitive actions require appropriate confirmation/approval UX and normal application safeguards.

### 9. Idempotency
For payments, bookings, orders, or repeated submissions, implement duplicate protection/idempotency where relevant.

### 10. Cancellation/error behavior
Long-running operations should handle cancellation when supported and return clear structured failures rather than ambiguous success.

## Basic imperative implementation pattern

```js
if (document.modelContext?.registerTool) {
  await document.modelContext.registerTool({
    name: "check-service-area",
    description: "Check whether the business currently serves a postal code.",
    inputSchema: {
      type: "object",
      properties: {
        postalCode: {
          type: "string",
          description: "Customer postal code"
        }
      },
      required: ["postalCode"]
    },
    async execute({ postalCode }) {
      const result = await checkServiceArea(postalCode);
      return {
        content: [{
          type: "text",
          text: JSON.stringify(result)
        }]
      };
    }
  });
}
```

Use feature detection because browser support is evolving.

## Declarative WebMCP
When an existing form already accurately represents a safe action, prefer progressive enhancement rather than rebuilding the workflow solely for agents.

Keep forms:

- semantically labeled
- validated
- accessible
- explicit about action/result
- aligned with the underlying business operation

Follow the current WebMCP declarative specification rather than stale community syntax.

## WebMCP is not the same as MCP
Keep these concepts distinct:

- MCP: an agent/application connects to tools/resources exposed by a server/service.
- WebMCP: a webpage exposes tools inside a browser context for compatible agents/co-browsing.

A venture may benefit from both.

Example:

- WebMCP lets an agent operate the live website using the user's browser/session.
- Server MCP/OpenAPI lets an external agent/service call approved backend capabilities without requiring the webpage.

## Existing Website Upgrade Workflow
When a user asks VLA to make an existing website AI-agent ready:

1. Crawl/audit important pages and conversion actions.
2. Verify XML sitemap, robots, canonicals and indexability.
3. Audit entity/schema coverage and truthfulness.
4. Audit machine-readable assets (`llms`, structured service data, OpenAPI/MCP where relevant).
5. Map user journeys into potential agent tools.
6. Score each tool on value, frequency, reliability, side-effect risk and implementation effort.
7. Implement the top tools using current WebMCP APIs when technically appropriate.
8. Preserve normal human UI and accessibility.
9. Test tool discovery.
10. Test schemas with valid and invalid inputs.
11. Test execution against production-like backend logic.
12. Test auth/permission boundaries.
13. Test cancellation/error paths.
14. Verify that no agent tool can claim or perform more than the human/business system actually permits.
15. Record AI Agent Readiness status in Venture State.

## Readiness scoring
Score 0–100:

- Search discovery: 15
- Entity/schema clarity: 15
- Structured content/data: 15
- Agent documentation/discovery assets: 10
- WebMCP actionable coverage: 20
- Tool reliability/validation: 10
- Security/permission boundaries: 10
- Production verification: 5

Do not give 100 unless all applicable layers are actually tested.

## Minimum launch gate
For a normal informational venture, Layers 1–2 may be enough initially.

For transactional/interactive ventures, identify at least one high-value WebMCP candidate at launch and implement it when current browser support, technical architecture and ROI justify it.

For an existing website explicitly sold as an "AI Agent Readiness" upgrade, WebMCP assessment is mandatory.

## VLA reporting
Report:

### Agent Readiness Score
0–100 and missing layers.

### Agent-capable actions
Which actions can actually be discovered/executed.

### Compatibility
What is production, experimental, or unsupported.

### Safety boundaries
Which actions require confirmation/authentication.

### Top 3 upgrades
Highest economic/user value improvements.

## Rule
The goal is not to add fashionable AI files. The goal is to turn the website into a truthful, structured, machine-readable and increasingly machine-operable business interface for the agentic web.
