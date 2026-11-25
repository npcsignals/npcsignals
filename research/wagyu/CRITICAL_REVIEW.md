# critical review

## findings that survived checks

- original checkpoint bytes and all 508 listed files match saved digests; baseline cost and quantities recalculate.
- token identifiers, genesis allocations and deployment strings come directly from official metadata.
- issuer and recipient ledgers match exact hashes and quantities for all three large xmr1 sends.
- raw fills paginate with overlaps preserved and deduplicated. a terminal 715-row page and aggregate quantity comparison improve the earlier incomplete account reconstruction.
- hxmr deployer and inventory vault both return the same three authorized signers and threshold two. generic userRole must not be misread as ruling out multisig.
- fixed-block native balances reproduce approximately 7,348 eth across three chain/address positions.

## corrections and pressure tests

- endTime-bounded incident queries returned empty despite real records elsewhere. successful no-endTime requests resolve this transport/query discrepancy for this collection; original responses remain retained. empty data alone cannot establish absence.
- 369,623 xmr1 is a rounded number at a source-specific cutoff, not a permanent sale total. later trades and 0.04 xmr1 in early test sells must be separated.
- aggregate prices have rounding differences from raw fill prices. final arithmetic uses raw fills; old aggregate calculations remain explicitly superseded.
- the closing-token calculation has a −0.0000000004 xmr1 residual. it is disclosed rather than hidden in a forced balancing entry.
- no complete primary proof of every conversion and bridge route was obtained. successful sampled receipts and current balances do not close that gap.
- current docs carry newer closure terms than the historical docs. retrieval time and documentation build time are both preserved; current language is not retrospectively assigned to october.
- a configured signer threshold does not prove key independence, operation of all off-chain systems or reserve availability.
- provider notices reproduced by media support a host incident; they do not prove the private-key exposure chain or a connection to october's data exposure.
- transfers to potential distributors lack a complete compensation entitlement map. none is counted as verified paid compensation merely due to the sender.

## remaining limitations

formal establishment date; complete historical snapshot chronology; full bridge/conversion reconciliation and complete buyer inventory; provider/key-exposure mechanism; reserve and liability attestation; recipient-level compensation mapping; legal claim enforceability; independent monero payment proof. these are UNRESOLVED or NOT ASSESSED as specified in the claim matrix. the archive can be complete as a transparent evidence record while the underlying case remains incomplete.
