# Historical Client Record Schema

Use this schema for private normalized historical client records.

```yaml
client_id: string
status: candidate | inventoried | reconstructed | benchmark_ready

identity:
  real_name_private: string | null
  domain_private: string | null
  industry: string | null
  business_model: B2B | B2C | mixed | unknown
  geography: string | null
  local_vs_national: local | regional | national | international | unknown

business_context:
  primary_offer: string | null
  avg_customer_value: number | null
  sales_cycle_days: number | null
  notes: string | null

audience_map:
  segments:
    - name: string
      business_value_1_10: number | null
      evidence: fact | estimate | inferred | unknown

source_inventory:
  gmail_threads: []
  drive_files: []
  gsc_sources: []
  ga4_sources: []
  google_ads_sources: []
  gbp_sources: []
  merchant_center_sources: []
  crm_sources: []
  proposal_sources: []
  other_sources: []

seo:
  query_data_available: boolean
  page_data_available: boolean
  rankings_available: boolean
  backlinks_available: boolean
  technical_audits_available: boolean
  migration_history_available: boolean

ppc:
  campaign_data_available: boolean
  search_term_data_available: boolean
  spend_available: boolean
  conversion_data_available: boolean
  revenue_or_roas_available: boolean

analytics:
  landing_page_data_available: boolean
  acquisition_data_available: boolean
  conversion_data_available: boolean
  revenue_data_available: boolean

strategy:
  proposals_available: boolean
  implementation_notes_available: boolean
  client_feedback_available: boolean
  timeline_available: boolean

experiments:
  - experiment_id: string
    hypothesis: string
    date_range: string | null
    audience: string | null
    channel: string
    action: string
    baseline: object
    result: object
    confidence: verified | strongly_supported | inferred | unknown
    confounders: []
    learning: string | null

outcomes:
  leads: number | null
  qualified_leads: number | null
  customers: number | null
  revenue: number | null
  retention: number | null
  attribution_confidence: verified | strongly_supported | inferred | unknown

learnings:
  wins: []
  failures: []
  reusable_patterns: []

data_quality:
  business_context: 0
  search_console: 0
  analytics: 0
  paid_search: 0
  landing_page_mapping: 0
  strategy_context: 0
  outcome_evidence: 0
  time_series_depth: 0
  cross_source_joinability: 0
  total: 0
  classification: weak | partial | usable | strong | gold_standard
```

## Score weights

- business_context: 10
- search_console: 15
- analytics: 15
- paid_search: 15
- landing_page_mapping: 10
- strategy_context: 10
- outcome_evidence: 15
- time_series_depth: 5
- cross_source_joinability: 5

The values stored under each field should be weighted points, not 1–10 ratings.
