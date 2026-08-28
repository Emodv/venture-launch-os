# Venture Launch OS — AI Agent Readiness Standard

AI Agent Readiness is a core launch dimension for every applicable website built or upgraded by Venture Launch OS / VLA.

## Default requirement

Every website should be evaluated across four layers:

1. Search discovery — XML sitemap, robots, canonicals, internal linking and indexability.
2. Semantic understanding — truthful structured data/schema, explicit entity identity, products/services, How It Works, Q&A and structured catalogs.
3. Agent discovery — machine-readable compatibility assets such as llms files, service data, agent manifests, OpenAPI/server MCP when genuinely implemented.
4. Agent actuation — safe browser-native WebMCP tools for valuable user actions when technically appropriate.

Use:

- `playbooks/AI_AGENT_READINESS_WEBMCP.md`
- `templates/AI_AGENT_READINESS_CHECKLIST.md`

## VLA behavior

For a new venture, VLA should design agent readiness into the website architecture from the start.

For an existing website, VLA should offer/perform an AI Agent Readiness audit and modernization covering discovery, semantic clarity and agent-operable actions.

For transactional sites, identify the highest-value actions that agents may need to perform, such as checking service area, finding products, obtaining estimates, requesting quotes, scheduling, or other safe workflows.

WebMCP actions must reuse the site's real validated business logic and respect existing authentication, authorization and user confirmation requirements.

## Source of truth

Track the current WebMCP proposal from the Web Machine Learning Community Group rather than coding against historical community implementations:

- https://github.com/webmachinelearning/webmcp
- https://webmachinelearning.github.io/webmcp/

WebMCP is evolving. Feature-detect browser APIs, verify current syntax before implementation, and clearly distinguish experimental compatibility from broad production support.

## Completion rule

Do not call a website "AI-agent ready" because it has an `llms.txt` file.

Agent readiness requires truthful machine-readable content and, where applicable, verified machine-operable actions with safe permission boundaries.
