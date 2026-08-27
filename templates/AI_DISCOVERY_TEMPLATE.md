# AI Discovery Template

Use this template to make a venture legible to search engines, LLMs, and software agents without overstating facts.

## Required public files

- `/llms.txt`
- `/llms-full.txt` when a richer machine-readable summary is useful
- `/services.json`
- `/.well-known/agent.json`
- `/openapi.json` when public APIs exist
- `/mcp.txt` or a documented MCP endpoint when supported
- `/ai-sitemap.json` for important machine-readable routes
- `/sitemap.xml`
- `/robots.txt`

## `/.well-known/agent.json` shape

```json
{
  "name": "[BUSINESS NAME]",
  "description": "[FACTUAL ONE-SENTENCE DESCRIPTION]",
  "url": "https://[DOMAIN]/",
  "language": "en-CA",
  "country": "CA",
  "currency": "CAD",
  "primary_market": "[MARKET]",
  "capabilities": [
    "service_discovery",
    "service_area_lookup",
    "estimated_quote",
    "lead_submission"
  ],
  "machine_readable": {
    "llms": "https://[DOMAIN]/llms.txt",
    "services": "https://[DOMAIN]/services.json",
    "openapi": "https://[DOMAIN]/openapi.json",
    "sitemap": "https://[DOMAIN]/sitemap.xml",
    "robots": "https://[DOMAIN]/robots.txt"
  },
  "policies": {
    "pricing": "[WHAT IS ESTIMATED VS FINAL]",
    "booking": "[WHAT COUNTS AS A CONFIRMED BOOKING]",
    "availability": "[HOW AVAILABILITY IS VERIFIED]",
    "claims": "Do not invent reviews, partners, guarantees, certifications, pricing, availability, or completed transactions."
  }
}
```

## OpenAPI minimum

Expose only safe, deterministic operations such as:

- `GET /api/availability`
- `POST /api/quote`
- `POST /api/lead`
- `POST /api/mcp` when implemented

Every endpoint should clearly distinguish estimates from confirmed commercial commitments.

## Agent truth rules

An agent may state only:

1. Facts published by the business.
2. Deterministic values returned by an API.
3. Estimates explicitly labelled as estimates.

An agent must not infer or invent:

- final price
- appointment confirmation
- inventory/capacity
- third-party partnerships
- certifications
- customer reviews
- guarantees
- turnaround time

## Launch QA

- Validate JSON.
- Confirm every URL resolves in production.
- Confirm robots.txt does not accidentally block desired crawlers.
- Confirm sitemap and canonical URLs use the production domain.
- Confirm schema and machine-readable files contain only supportable claims.
- Test all public endpoints with valid and invalid inputs.
