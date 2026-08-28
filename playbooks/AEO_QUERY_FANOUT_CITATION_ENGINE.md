# AEO Query Fan-Out + Citation Engine

## Purpose
Turn SEO/AEO from single-keyword targeting into topic-wide relevance across the prompts, subquestions, comparisons, entities, and sources that AI answer engines may retrieve when constructing an answer.

This playbook is based on three operating principles:

1. Query fan-out: assistants can decompose one user query into multiple related retrieval needs. Winning one head term is not enough.
2. Citation probability: increase the odds of being reused through consensus, freshness, and authority.
3. Reusable answer assets: structure on-site and off-site information so it is easy to retrieve, quote, compare, and attribute.

---

# 1. Query fan-out map

For every priority audience/topic, do not target only a single keyword.

Create a fan-out graph around the seed topic:

- core question
- definitions
- alternatives
- comparisons
- pricing/cost
- pros/cons
- eligibility/fit
- implementation/how-to
- risks/limitations
- reviews/proof
- local/geographic variants
- role/industry/use-case modifiers
- recency/current-year modifiers
- brand-vs-brand prompts
- "best", "top", "worth it", "should I", "which" decision prompts

The output is a PROMPT/TOPIC GRAPH, not a flat keyword list.

## AI satisfiability filter

For each informational query/prompt, ask:

> Can an AI answer engine plausibly satisfy the user without a click?

If YES:
- optimize for brand mention, citation, inclusion, and recommendation context;
- do not judge success only by click-through rate.

If NO:
- optimize for both citation/relevance and downstream click/conversion.

Classify each prompt:
- CLICK-DEPENDENT
- CITATION-FIRST
- HYBRID

---

# 2. Brand/citation gap analysis

For each priority audience and topic graph, compare the brand against competitors and commonly cited sources.

Identify:
- prompts where competitors are mentioned and the brand is absent;
- topics where the brand has no authoritative page;
- cited third-party publications where competitors have coverage;
- Reddit/Quora/community discussions where the category is discussed but the brand has no legitimate presence;
- YouTube queries where relevant competitors/content dominate;
- stale pages or old evidence that weaken freshness;
- entity inconsistencies across owned and third-party sources.

The objective is not "be everywhere". The objective is to close high-value citation gaps inside the priority audience's decision ecosystem.

---

# 3. Citation probability model

Evaluate content and brand presence through three source-derived levers:

## A. Consensus
Does the same factual entity/positioning appear consistently across multiple credible sources?

Improve with:
- consistent brand/entity naming;
- real editorial mentions;
- reputable directories/associations;
- legitimate community discussions;
- partner/customer references where factual;
- owned content that matches public facts.

Do not manufacture consensus with fake reviews, sockpuppets, spam comments, or synthetic mentions.

## B. Freshness
Is the information current enough for the query?

Improve with:
- visible reviewed/updated dates when meaningful;
- periodic content refreshes based on material changes;
- current prices/data/year references only when verified;
- updated comparison tables;
- current screenshots/data/examples;
- refreshed structured data and machine-readable assets.

Do not change dates without substantive review/update.

## C. Authority
Does the domain/page/entity have evidence of expertise and trust?

Build through:
- traditional SEO authority;
- useful backlinks/editorial references;
- expert authorship where relevant;
- original research/data;
- case studies with evidence;
- strong internal topic architecture;
- reputable third-party mentions.

These three levers are prioritization heuristics, not guarantees of AI citation.

---

# 4. AI-reusable content format

Use content structures that are easy for humans to scan and machines to extract.

## BLUF
Put the Bottom Line Up Front when the user expects a direct answer.

Pattern:
1. direct answer
2. qualifiers/conditions
3. evidence/explanation
4. next action or deeper detail

## Atomic sections
Each section should answer one coherent sub-question and remain understandable when retrieved independently.

Prefer:
- descriptive headings;
- short declarative sentences;
- explicit subject/entity names instead of ambiguous pronouns;
- lists for enumerations;
- tables for consistent comparisons;
- definitions before nuanced exceptions;
- numbers with units, geography, source, and timeframe.

Avoid:
- fluffy introductions;
- hidden answer buried below many paragraphs;
- vague claims;
- unsupported superlatives;
- giant mixed-topic sections.

## Entity-rich writing
State relationships explicitly:

`Entity -> category -> audience -> product/service -> geography -> mechanism -> constraint -> evidence`

Do not keyword-stuff or create unnatural prose merely for machines.

---

# 5. On-site citation program

For each priority topic graph, ensure the website has the minimum authoritative set needed to cover the decision journey.

Possible assets:
- canonical service/product page;
- direct-answer explainer;
- comparison page;
- alternatives page;
- pricing/cost guide;
- eligibility/fit guide;
- process/how-it-works page;
- original benchmark/data page;
- case study;
- glossary/definition only when useful;
- buyer Q&A embedded in relevant pages.

Do not generate one thin page per prompt. Consolidate related prompts into the strongest canonical resource.

---

# 6. Off-site citation program

Use the same Audience Map + Prompt Graph to build brand presence outside the website.

Priority surfaces can include:
- editorial publications;
- industry publications;
- associations;
- partners;
- customer stories;
- Reddit where authentic participation is appropriate;
- Quora where authentic expert answers are appropriate;
- YouTube;
- podcasts/webinars;
- public datasets/directories.

The purpose is credible entity corroboration and useful distribution, not manufactured link volume.

---

# 7. YouTube AEO layer

When video is relevant to the priority audience, treat YouTube as both a discovery and citation surface.

For each priority topic:
- research YouTube search demand/results;
- create videos answering the same high-value prompt clusters;
- use clear titles matching the real user problem;
- state the answer early;
- use chapters;
- include accurate descriptions and relevant links;
- ensure spoken content is explicit and entity-rich;
- create supporting webpage/transcript when useful;
- keep information current.

Do not assume YouTube presence alone causes AI citations. Treat it as an additional authoritative surface to test and measure.

---

# 8. Crawler/agent accessibility audit

Audit `robots.txt`, CDN/WAF rules, and platform defaults for unintended blocking of relevant search/AI crawlers and user agents.

The source specifically calls out checking access for agents/crawlers such as:
- GPTBot
- OAI-SearchBot
- ClaudeBot
- Google-Extended

Important: these user agents can serve different purposes and policies can change. Before changing production crawler policy, verify the current official documentation for each crawler and align access with the business owner's privacy/content-use preferences.

Also check:
- Cloudflare/WAF bot rules;
- rate limiting;
- JavaScript rendering;
- authentication walls;
- accidental geo/IP blocks;
- noindex/X-Robots-Tag;
- canonical conflicts.

Never weaken security just to allow crawlers.

---

# 9. Measurement

Track conventional SEO and AI visibility separately.

## Search
- rankings
- impressions
- clicks
- landing-page conversions
- qualified leads
- revenue/value by audience segment

## AI/AEO
- prompt/topic coverage
- brand mentions in observable AI results
- cited URLs
- competitor citation share
- AI referral traffic
- bot/crawler activity where logs are available
- self-reported attribution ("How did you hear about us?" with AI assistant options)
- assisted conversions from AI referrals

Bot visits are signals of access/retrieval interest, not proof that a citation occurred.

---

# 10. VLA execution sequence

For every meaningful SEO/AEO project:

`Audience Map -> Prompt/Topic Fan-Out -> AI Satisfiability Filter -> Brand/Citation Gap -> Content/Entity Gap -> Consensus/Freshness/Authority Plan -> On-site assets -> Off-site/YouTube distribution -> crawler accessibility audit -> measurement -> refresh loop`

For Mode B existing businesses, insert first-party data and Preservation Map before final prioritization:

`URL -> public audit -> GA4/GSC/CRM access -> Preservation Map -> Audience Map -> Prompt Fan-Out -> citation gaps -> roadmap`

---

# Reporting format

VLA should report:

## Priority topic clusters
Mapped to priority audiences.

## Query fan-out
Top prompts/subqueries, classified as CLICK-DEPENDENT, CITATION-FIRST, or HYBRID.

## Citation gaps
Where competitors/sources appear but the brand does not.

## Citation levers
Consensus / Freshness / Authority weaknesses.

## On-site actions
Highest-value pages/assets to create or refresh.

## Off-site actions
Editorial/community/YouTube opportunities relevant to the audience.

## Access blockers
Crawler/robots/WAF issues requiring review.

## Measurement
Search, AI citations/mentions, referrals, and qualified business outcomes.
