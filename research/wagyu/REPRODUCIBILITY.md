# reproduction and coverage

## reproduce without contacting any service

run from the extracted directory with python 3.10 or newer:

```sh
python verify.py
```

the verifier checks raw-response sha256 values, the identity and selected-file manifest of the public baseline evidence package, the 36-account quantity and cost, matched issuer transfers, all raw fill proceeds windows, current multisig configurations, sampled evm inclusion, local links and svg syntax. it does not send network requests or certify external claims. `SHA256SUMS.json` covers the files delivered in this checkpoint; the manifest and its text twin exclude themselves to avoid circular hashes.

raw responses are the authoritative preserved observations. derived calculations can be regenerated with this sequence:

```sh
python analyze.py
python finalize_financial.py
python normalize_financial.py
python verify.py
```

`analyze.py` retains an initial aggregated-fill calculation; `finalize_financial.py` adds the authoritative raw-fill result; `normalize_financial.py` places the old calculation under an explicit superseded heading. the initial aggregate calculation's token residual omitted the small prior buy and token fee; it is not an alternative current balance conclusion. scripts write derived files, so regeneration can change manifest verification until the regenerated content is compared with the saved original. do not overwrite raw evidence to make digests agree.

optional visual rendering uses cairosvg and pillow: `python render.py`. all ten editable svg originals and png previews are included. final svg and markdown files preserve the reviewed editorial edition; internal document generators are excluded.

## optional fresh public requests

`collect.py`, `sources.py`, `evm.py` and `page_seller.py` are read-only collectors, but rerunning them in this folder replaces evidence with newer observations. copy them to a new checkpoint first. exact urls and json payloads for every saved request are in [source register json](evidence/source_register.json). none requires a wallet signature, private key or transaction.

## endpoint limits and actual responses

- official info documentation says time-range queries generally return 500 elements or distinct blocks. actual records returned here can exceed 500; that is not proof of exhaustive coverage. preserve the actual response shape and use overlap pagination rather than enforcing an invented universal count limit.
- userFillsByTime documents at most 2,000 fills per response and availability of only the latest 10,000 fills. the seller queries returned 2,000, 2,000 and 715 rows, with duplicate timestamp overlaps retained in raw pages. 4,594 unique records are identified by hash and trade id, sorted by time and trade id. a final short page is evidence of termination of this query, not a protocol-wide historical archive guarantee.
- advancing from the last timestamp assumes fewer than a whole response cap of distinct fills share that timestamp. no such unresolved full-cap same-timestamp group was encountered. preserve ties when paginating.
- aggregated fills can round weighted prices and combine records. they corroborate quantity; raw fill price × size determines final usdc amounts.
- date-bounded queries in the inherited package sometimes returned empty while no-endTime queries returned real activity. no absence claim is based on those empty results. request failures and contradictory replies remain preserved.
- non-funding ledger responses are event arrays with time/hash/delta. issuer and seller short results agree on three transfer entries. recipient distribution responses of 192 and 694 records are not represented as a complete compensation register; the larger result requires further pagination/coverage checks before an exhaustive claim.
- spotClearinghouseState provides an observation of current token balances, not historical reserves or all off-platform payments. signer configuration is queried separately through userToMultiSigSigners; userRole alone is not a multisig test.
- candleSnapshot documents only the most recent 5,000 candles. the preserved minute window covers the collapse, not all subsequent market history. a minute low is not a timestamped individual execution. no-trade gaps must not be interpolated as observed trades.
- ethereum/arbitrum native balances use explicit block numbers. successive chain snapshots are not simultaneous. successful sampled receipts establish those transactions, not complete bridge settlement or exclusive proceeds attribution.

## preservation boundaries

the historical frogman evidence is unchanged. the original package identity and selected public evidence digests are documented in [publication notes](PUBLICATION_NOTES.md). old raw files and classifications are unchanged. this checkpoint's new observations extend through the latest timestamp recorded in its per-request metadata; its frogman account observations retain their earlier cutoff and were not recollected.

## technical checks and publication adaptation

the unmodified editorial source passes 884 technical checks. publication removes private prose and internal status/generation files, replaces the nested private zip with a selected evidence zip and updates its verification path and expected digest. the count therefore changes; it must not be represented as the same 884-check payload. original raw evidence hashes and all ten finalized svg hashes remain unchanged. the original digest maps and an exact exclusion list are published.
