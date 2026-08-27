# Lean Operations Playbook

## Objective
Deliver reliably while keeping fixed cost low until demand proves what deserves automation or infrastructure.

## Default operating principle
Partner or perform manually before owning expensive infrastructure.

## Minimum workflow
Map the business from customer request to completed outcome:

`lead → qualification → quote → booking/order → fulfillment → completion → payment → follow-up → repeat/referral`

For each stage define:

- owner
- input
- output
- system of record
- SLA/expected timing
- failure mode
- notification
- metric

## System of record
Use one central database/CRM for business-critical status. Do not rely on browser local storage, inbox memory, or disconnected spreadsheets for core customer state.

Minimum fields:

- customer/contact
- source/UTM
- requested service/product
- geography
- value
- stage/status
- assigned owner/partner
- timestamps
- notes
- outcome

## Exception-first design
Before automating everything, record exceptions:

- unavailable geography
- unusual service request
- pricing uncertainty
- fulfillment delay
- failed payment
- refund/claim
- partner failure

Automate common paths only after enough repetitions reveal the stable process.

## Fixed-cost gate
Do not add stores, vehicles, staff, equipment, or custom software merely because they may improve the experience.

Add fixed infrastructure when evidence shows:

- recurring demand
- positive contribution margin
- capacity constraint
- forecastable utilization
- acceptable payback period

## Automation priority
Automate repeated, low-judgment work first:

1. lead acknowledgement
2. routing/assignment
3. reminders/follow-ups
4. status notifications
5. CRM sync
6. reporting
7. invoicing/payment events

Keep high-judgment exceptions human until patterns stabilize.

## Weekly operating review
Track:

- leads received
- conversion by stage
- cycle time
- fulfillment cost
- gross contribution
- cancellations/refunds
- partner/vendor failures
- repeat rate
- capacity utilization

Identify the single bottleneck limiting revenue or quality and fix that before adding features.
