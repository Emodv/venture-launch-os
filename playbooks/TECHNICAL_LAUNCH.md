# Technical Launch Playbook

## Objective
Move from approved venture specification to a verified production system.

## Default stack
Use a better connected stack when justified; otherwise default to:

- GitHub — source control
- Vercel — deployment
- Supabase — database/backend/auth
- Stripe — payments when applicable
- HubSpot or equivalent — CRM
- GA4 or equivalent — analytics
- Google Search Console — indexing/search diagnostics

## Execution sequence

`repo → scaffold → environment → database → local/build test → commit → deploy → domain → DNS → SSL → canonicalization → production QA → analytics → indexing`

## 1. Repository
If absent and tools permit, create a repository with:

- README
- `.gitignore`
- environment example file with no secrets
- app source
- deployment configuration
- documentation for required external accounts

Never commit credentials, tokens, customer data, private keys, or production secrets.

## 2. Application scaffold
Ship the leanest architecture capable of:

- mobile-first pages
- lead/order persistence
- analytics events
- SEO metadata
- structured data
- API endpoints required by the venture
- production deployment

Avoid native apps, microservices, queues, or custom infrastructure before demand requires them.

## 3. Environment management
Maintain separate values for development/preview/production where relevant.

Required behavior:

- `.env.example` contains names only
- real secrets live in platform secret stores
- public keys are distinguished from privileged keys
- rotate compromised credentials immediately

## 4. Database/backend
Before launch verify:

- schema exists
- server-side validation
- authorization/RLS where applicable
- no privileged key exposed client-side
- spam/rate-limit strategy
- logging/error handling
- backups/recovery appropriate to business risk
- idempotency for payment/order mutations

## 5. Deployment
Production deploy is not complete until:

- build passes
- primary routes return successfully
- server/API routes work
- environment variables are present
- no obvious console/runtime failures

## 6. Domain + DNS
Connect production domain and verify:

- root domain
- `www` behavior
- one canonical host
- HTTPS certificate
- redirect consistency
- no staging hostname used as canonical

## 7. Production smoke test
Test from a clean session/mobile viewport:

- homepage
- navigation
- CTA
- progressive form/quote
- validation errors
- successful submission
- database persistence
- notification/CRM sync if configured
- payment test path if applicable
- API endpoints
- sitemap
- robots
- structured data
- machine-readable discovery files

## 8. Production reliability baseline
Where appropriate add:

- error monitoring
- uptime monitoring
- logs
- rollback path
- backup policy
- email authentication (SPF/DKIM/DMARC)
- transactional email domain

## 9. Indexing
After production verification:

- connect Search Console when access exists
- submit sitemap
- inspect critical URLs
- verify indexability
- do not claim indexing until the search engine confirms it or the URL is observed indexed

## Completion definition
A technical launch is complete only when the production domain is live, core conversion path works end-to-end, persistence is verified, and critical production assets resolve successfully.
