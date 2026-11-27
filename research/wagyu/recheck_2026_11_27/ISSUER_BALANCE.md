# issuer balance discrepancy

CONFIRMED: saved 25 november total 13398815.44801162 xmr1; new total 13398820.7090639602; difference **5.2610523402 xmr1**. token index 404 is used, not ticker alone. the preserved independent earlier 27 november check gives the same new total. hold is 0.0; free-versus-reserved reclassification does not explain a change in total. entryNtl is a cost/accounting field, not additional spendable inventory. exact decimal arithmetic is used; the change is far larger than 8-decimal token granularity or the old sub-nanounit balancing residual.

## tests performed

- spotClearinghouseState repeats the observed total. clearinghouseState was queried separately for perpetual state; it is not a substitute spot reserve balance.
- userFills and all-time userFillsByTime return 187 historical rows. recent time-bounded no-endTime requests do not expose a matching xmr1 acquisition. historical rows must not be mislabeled new trades.
- userNonFundingLedgerUpdates from zero returns a full 2,000-row result. overlapping pagination was tested and raw pages retained. those historical pages alone do not guarantee coverage of november; page caps and terminal timestamps are explicitly preserved in pagination_summary.json.
- an independent query starting 20 november returns the known issuer incident transfers and later records. the subset after the 25 november cutoff contains 0 returned records. this demonstrates the endpoint can return known activity while the unexplained increment still lacks a matched post-cutoff ledger entry.
- userFunding, historicalOrders, userFees, userRateLimit and spotDeployState were tested. fee schedule/account state is not an itemized xmr1 deployer-fee revenue statement. spotDeployState returns other deployment state; it does not by itself reconcile xmr1 credits. errors and actual formats are retained.

## alternative explanations

| hypothesis | assessment |
|---|---|
| displayed precision / rounding | insufficient to explain magnitude; not accepted as balancing entry |
| reserved/free balance movement | hold zero and total changed; not supported as explanation |
| ordinary token transfer | no matching returned post-cutoff ledger event; unresolved, not disproven universally |
| purchase / sale correction | no matching new returned fill; unresolved outside api coverage |
| deployer fee accrual, distribution or protocol accounting | technically possible category requiring a specific official rule and matching accrual record; not established here |
| incomplete api coverage / unexposed event class | remains possible; known-event and pagination tests do not establish exhaustive accounting |

conclusion: **UNRESOLVED**. do not call the increment compensation, deposits, reserve replenishment or confirmed fee revenue. a protocol-level balance-delta record or an itemized verified mechanism reconciling the exact amount is needed. this does not affect the separately observed 36-account sum.

## pagination outcome

fifty pages / 100000 rows before deduplication; latest returned historical timestamp 2026-06-13T18:55:29.047000+00:00. the last page is full. the explicit 50-page cap was reached, so the all-time history is not exhausted. november was separately queried and known incident events reproduced. continuing indiscriminately through older dense distributions is not required to label the accounting discrepancy unresolved.
