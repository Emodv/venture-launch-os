# Privacy-First Knowledge Distillation Protocol

## Non-negotiable rule
Historical client material is used only to learn generalized operating patterns. Client identity, personal information, company-identifying information, account identifiers, confidential metrics, source links, credentials, and NDA-protected details must never enter the reusable/public VLA knowledge layer.

## Purpose
VLA may inspect authorized private historical evidence to extract transferable marketing judgment. The output of that process is doctrine, patterns, benchmark ranges, failure modes, and decision rules — not client records.

## Data boundary

### Private evidence zone
May contain authorized source material such as:
- Gmail threads
- Drive files
- GA4/GSC/Google Ads exports
- CRM reports
- proposals and audits
- campaign notes
- client feedback

This material remains private and source-scoped. It must not be copied into public repositories or reusable prompts.

### Distilled knowledge zone
Only the following may cross the boundary:
- anonymized business archetype
- generalized audience pattern
- generalized channel pattern
- normalized/aggregated metric ranges when safe
- diagnosis
- decision rule
- action pattern
- outcome class
- confidence level
- era/relevance classification

## Forbidden fields in reusable knowledge
Never persist or expose:
- person names
- company names
- domains or URLs that identify the client
- email addresses
- phone numbers
- physical addresses
- Google Ads customer IDs
- GA/GSC property identifiers
- CRM/contact IDs
- invoice/account IDs
- credentials, tokens, API keys, passwords
- exact confidential revenue/spend figures when they can identify a client
- exact quotations from NDA-protected correspondence
- source message IDs or private file IDs
- unique combinations of facts that make re-identification likely

## Anonymization standard
Replace client identity with a broad archetype such as:
- Canadian local-service business
- B2B SaaS company
- professional-services firm
- ecommerce retailer
- financial-services business

Generalize geography where necessary. Bucket sensitive values instead of copying exact figures when exactness is not required for the learning.

Examples:

Bad:
`Company X spent $10,165.27 and received 14,687 clicks.`

Good:
`A local-service account with five-figure annual paid-search spend showed that channel efficiency should be evaluated against lead quality, not click volume alone.`

Bad:
`Client Y's /specific-page ranked #6 and produced 23 leads.`

Good:
`A high-intent service landing page ranking on page one materially outperformed broader informational traffic in qualified lead production.`

## Knowledge object
A reusable historical learning should look like:

```text
Archetype: professional-services / local lead generation
Era: legacy | transitional | current
Evidence quality: strong
Pattern confidence: repeated
Situation: acquisition traffic stable, lead volume falls
Diagnosis: verify conversion infrastructure before raising spend
Decision rule: inspect phone/forms/tracking/landing-page behavior first
Outcome class: avoided unnecessary acquisition spend
Current relevance: high
```

No identity is required.

## Re-identification guard
Do not combine enough quasi-identifiers to reconstruct a client identity. If a record is unusually distinctive, generalize further or exclude it from reusable memory.

## NDA rule
NDA-protected evidence can inform internal reasoning only within the authorized source context. The reusable doctrine must be abstracted so that it cannot disclose the protected party, confidential facts, strategy specifics, or proprietary results.

## Public repository rule
The public Venture Launch OS repository may contain:
- frameworks
- schemas
- anonymization code
- generalized doctrine
- synthetic examples

It must not contain:
- private client datasets
- private source IDs
- identifying examples copied from source systems
- confidential performance records

## Retention principle
Prefer extracting the minimum durable knowledge necessary. Raw evidence is not the moat; the distilled decision system is the moat.

## Output review checklist
Before a historical learning is reusable, verify:
1. No person or company identity.
2. No contact information.
3. No account/property/source identifiers.
4. No credentials/secrets.
5. No confidential exact metric unnecessarily preserved.
6. No unique details enabling re-identification.
7. The learning is expressed as a transferable decision principle.
8. Era/current-relevance is labeled.
9. Confidence is labeled.
10. The original private evidence remains outside the public knowledge layer.
