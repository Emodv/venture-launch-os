# VLA Intelligence Layer

The intelligence layer turns historical and current operating evidence into reusable decision support for Venture Launch Agent.

## Components

- `HISTORICAL_CLIENT_INTELLIGENCE.md` — methodology, privacy boundary, scoring, experiment reconstruction, and benchmark rules.
- `../templates/HISTORICAL_CLIENT_RECORD_SCHEMA.md` — canonical private case schema.
- `../vla_runtime/intelligence.py` — deterministic data-quality, benchmark-eligibility, and attribution-confidence logic.
- `../vla_runtime/evals/test_intelligence.py` — regression tests for the scoring/eligibility layer.

## Private-data architecture

Raw historical client evidence must remain outside this public repository.

Recommended production architecture:

`Gmail + Drive + GA4 + GSC + Google Ads + CRM -> private ingestion -> normalized client records -> benchmark retrieval -> VLA Venture State`

Public code receives only anonymized benchmark context and opaque case IDs.

## Initial operating workflow

1. Discover candidate historical clients from authorized Gmail/Drive sources.
2. Inventory available evidence by source class.
3. Calculate Data Quality Score.
4. Select benchmark-ready and strategically diverse cases.
5. Reconstruct experiments and outcomes.
6. Store source-level evidence privately.
7. Retrieve only compatible anonymized patterns into VLA.
8. Measure whether benchmark-informed decisions outperform baseline decisions.

## Benchmark principle

The system optimizes for evidence quality, comparability, and economic outcomes—not the volume of archived files.
