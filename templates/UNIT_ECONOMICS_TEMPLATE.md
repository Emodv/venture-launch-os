# Unit Economics Template

Use before scaling paid acquisition or adding fixed operating cost.

## Core inputs

| Metric | Value | Status |
|---|---:|---|
| Average order value / contract value | [PLACEHOLDER] | Assumption / Known |
| Direct fulfillment cost | [PLACEHOLDER] | Assumption / Known |
| Payment fees | [PLACEHOLDER] | Assumption / Known |
| Delivery/logistics | [PLACEHOLDER] | Assumption / Known |
| Support/refund allowance | [PLACEHOLDER] | Assumption / Known |
| Gross contribution per order | [PLACEHOLDER] | Calculated |
| Repeat orders / retention | [PLACEHOLDER] | Assumption / Known |
| Estimated LTV | [PLACEHOLDER] | Calculated |
| CAC | [PLACEHOLDER] | Known after acquisition tests |
| CAC ceiling | [PLACEHOLDER] | Calculated |
| Payback period | [PLACEHOLDER] | Calculated |

## Formulas

`Contribution margin = Revenue - variable fulfillment - payment fees - delivery - refund/support allowance`

`Contribution margin % = Contribution margin / Revenue`

`CAC = Acquisition spend / New won customers`

`Simple LTV = Contribution per order × expected lifetime orders`

`LTV:CAC = LTV / CAC`

## Default decision rules

- Do not scale a channel with negative contribution margin.
- Do not use clicks or leads as the final success metric when won-customer data is available.
- Set kill criteria before paid testing begins.
- Prefer partner/variable-cost fulfillment until recurring demand justifies fixed infrastructure.
- Treat CAC ceiling as a constraint, not a target to spend up to automatically.

## Scenario table

Model at least three cases:

1. Bear: lower AOV, higher fulfillment/CAC.
2. Base: realistic current assumptions.
3. Bull: improved conversion/repeat rate without heroic assumptions.

## Output

Return:

- contribution margin dollars and percentage
- CAC ceiling
- expected payback
- estimated LTV:CAC
- largest economic risk
- one change with the highest expected profit impact
