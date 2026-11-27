# reproduction and limitations

today's inherited package verified 497 original manifest entries before reuse. selected evidence is preserved byte-for-byte in evidence/inherited_evidence.zip; exclusions are documented. account measurements are inherited, not newly re-collected here. exact original source statements as available are preserved; the operator oembed is truncated and is not a full original post.

run `python verify.py` for all delivered file digests and matched-transfer equality. `collect.py` makes optional new read-only requests but overwrites its raw filenames; run in a new directory to preserve this observation. `follow.py` performs ledger pagination, retaining overlaps, all raw pages and any failures. api records are not consensus replay, a short or empty answer is not guaranteed absence, and balances may include mechanisms outside returned user fills/ledger events. source times are independent per request. historical baseline records reside inside evidence/inherited_evidence.zip.

provider statement: https://status.1984.is/api/status-page/public ; operator original: https://x.com/PerpetualCow/status/2123760480061718801 ; official account data: https://api.hyperliquid.xyz/info . matched hashes and per-account response timestamps are retained. the charts state their observation scope and classifications. no github changes are made by any verification script.

accounts.csv preserves 38 original rows: the 36-account set plus two separately investigated issuer/seller rows. frogman_36_accounts.csv explicitly selects the 36 rows; their decimal sum is 3,586.887420 xmr1. do not include issuer/seller balances in that sum. historical svg copies are preserved from publication commit d692be10b67c2717d3b007a656579ebc07c67948 under visuals/historical_2026_11_25/. see pagination_summary.json for the non-exhaustive 50-page historical cap.

## publication packaging

run `python verify.py` with standard-library python 3.10 or newer. no extraction or network is required. the verifier reads archived ledger pages directly, verifies inherited members, original-to-public raw and svg hashes, account totals, matched transfer, source references and relative links. the original private verifier passed 270 checks; the public count differs because packaging and integrity checks are expanded. raw file names in source_register.json that begin raw/issuer_ledger_page refer to members of evidence/ledger_pages.zip. the omitted concatenation issuer_pagination.json can be reconstructed from the numbered original pages and the initial raw/userNonFundingLedgerUpdates.response. pagination_summary.json discloses the 50-page cap; do not treat the history as exhausted.

source urls, query payloads, failed requests and exact response times remain preserved. the 36-account observations are inherited from the earlier 27 november check; no fresh balances or prices are claimed in this integration. [publication exclusions](PUBLICATION_SELECTION.md).
