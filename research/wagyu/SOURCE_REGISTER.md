# primary evidence register

observation date: 25 november 2026. exact request start and completion timestamps, methods, payloads, urls, response digests and errors are in [machine register](evidence/source_register.json) and [failed requests](evidence/failed_requests.json). raw response bytes are preserved separately. documentation build dates and event dates are not substituted for observation dates.

| id | evidence domain | local evidence | original/source url |
|---|---|---|---|
| s01 | token identity, supply, inventory and genesis | spotMeta, *_details, *_issuer_spot; token_comparison.json | [https://api.hyperliquid.xyz/info](https://api.hyperliquid.xyz/info) |
| s02 | matched issuer/seller transfers | issuer_incident_ledger_no_end; seller_incident_ledger_no_end; issuer_transfers.json | [https://api.hyperliquid.xyz/info](https://api.hyperliquid.xyz/info) |
| s03 | seller raw paginated fills | seller_raw_page_0 through 2; seller_raw_pagination.json; financial_reconciliation.json | [https://api.hyperliquid.xyz/info](https://api.hyperliquid.xyz/info) |
| s04 | historical original architecture | evidence/historical_docs/; original request/response files retained | [https://docs.wagyu.xyz/native-bridge](https://docs.wagyu.xyz/native-bridge) |
| s05 | current bridge, closure, fees and relaunch | native_bridge_current; changelog_current; current_openapi; wagyu_docs | [https://docs.wagyu.xyz/native-bridge](https://docs.wagyu.xyz/native-bridge) |
| s06 | multisignature configuration | HXMR_deployer_signers; HXMR_treasury_signers; XMR1_issuer_signers; multisig_docs | [https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/multi-sig](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/multi-sig) |
| s07 | operator statements | operator_oct28; original preserved checkpoint raw oembed responses | [https://x.com/Wagyu_xyz/status/2115384084478185875](https://x.com/Wagyu_xyz/status/2115384084478185875) |
| s08 | hosting incident and attempted primary retrieval | hosting_home.error.json; hosting_announcements.error.json; cert_home; baseline media/source evidence | [https://1984.hosting/](https://1984.hosting/) |
| s09 | fixed-block native positions and sampled receipts | ethereum_*; arbitrum_*; bridge_*, onward_*, tornado_*; destination_positions.json | [https://mainnet.gateway.tenderly.co](https://mainnet.gateway.tenderly.co) |
| s10 | original frogman baseline | frogman_baseline_evidence.zip; baseline_validation.json | [https://github.com/npcsignals/npcsignals/tree/main/research/frogman-wallet-drain](https://github.com/npcsignals/npcsignals/tree/main/research/frogman-wallet-drain) |
| s11 | protocol semantics, caps and deployment | info_docs; hip1; hip1_sdk; multisig_docs | [https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint) |
| s12 | candidate distributions | HXMR_treasury_ledger; distribution_a_ledger; distribution_b_ledger; candidate_distributions.json | [https://api.hyperliquid.xyz/info](https://api.hyperliquid.xyz/info) |
| s13 | historical web availability | wayback_index; attempted archived captures (success and failure recorded separately) | [https://web.archive.org/cdx/search/cdx?url=*.wagyu.xyz/](https://web.archive.org/cdx/search/cdx?url=*.wagyu.xyz/) |
| s14 | external analysis used only for comparison | preserved original checkpoint analysis; separately reproduced raw quantities in s02/s03 | [https://bitquery.io/investigations/xmr1-hyperliquid-hack](https://bitquery.io/investigations/xmr1-hyperliquid-hack) |

## provenance and retrieval boundaries

68 successful new response records and 8 failed attempts are indexed. success means retrieval, not confirmation of every assertion in a source. historical docs were copied unchanged from the existing repository; the original frogman raw evidence is repackaged without changing retained file bytes. the baseline manifest has 508 verified entries. operator post text can be verified as a statement without its claims being independently verified. syndicated reporting is not counted as independent corroboration.

archival index results establish listed capture availability, not the contents or ownership of an early domain capture. successful archived bodies, if present, are dated records requiring attribution. failed snapshots do not establish an absence of historical material. provider requests failed with access errors; cert home retrieval is not a complete advisory search. explorer userDetails attempts returned errors; direct info queries succeeded. ethereum history index results and sample receipts do not constitute full multi-chain reconciliation.

retrieved original operator responses, provider/cert media reproduction and original external analysis are retained inside the published baseline evidence package. this new package extends rather than silently rewrites that record. current docs can differ from earlier posts; both are time-specific evidence.

see [publication notes](PUBLICATION_NOTES.md) for exact inclusions, exclusions and original-to-published digest mapping.

fixed-block arbitrum requests use `https://arbitrum.gateway.tenderly.co`; exact endpoint payloads and timestamps are preserved in the raw metadata.
