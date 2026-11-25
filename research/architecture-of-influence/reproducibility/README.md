# reproducibility

The comparison uses the official original and corrected report ZIPs linked in [source notes](../SOURCES.md). They are not bundled because redistribution rights were not established. Download both files and run:

```sh
python compare_notices.py original.zip corrected.zip --out comparison.json
```

Python 3.10 or newer; standard library only. The script checks archive integrity, finds the report CSVs, preserves physical and unique column counts, rejects conflicting duplicate headers, confirms stable category keys, records changed/missing values, and calculates parent/child arithmetic without assuming categories are additive.

The checked outputs in `notices_comparison.json` and `transparency_report_diff.json` were produced from the preserved copies in the private archive. These outputs do not establish the underlying number of moderation events, external file provenance, cause, intent or effectiveness of platform controls.
