# hosting statements: scope and chronology

classification: CONFIRMED statements; UNRESOLVED causal attribution. original available responses and transcriptions are preserved in evidence, with the primary live status api response in raw/hosting_primary.response.

| source | publication / update | wording and scope |
|---|---|---|
| operator, original x post 2123760480061718801 | 20 november 2026; inherited chronology reports 12:48 utc, exact time not newly authenticated | sweeping assertion about provider compromise; adds a deleted old server retaining the deployer key. the returned oembed truncates the post. a full original post was not recovered here. |
| hosting provider status notice | incident createdDate 2026-11-21 17:20:09; lastUpdatedDate 2026-11-26 19:48:09, as returned without timezone; content heading explicitly 26 november 19:45 utc | distinguishes restoration of disrupted services from exposure of customer-hosted data; excludes seven originally targeted websites from its reassurance. |
| earlier provider wording | indexed 25 november update, 12:35 utc | broader denial of viewing/copying/altering/compromising customer data outside seven sites; not a preserved historical original revision in the live api. do not silently treat a search cache as a forensic version history. |

## exact short passages for editorial verification

operator: “got hacked with everyone's data + internal server files today.”

provider: “customer-hosted data remained safe and was neither accessed nor altered by the attackers.”

operator original url: https://x.com/PerpetualCow/status/2123760480061718801

provider original url: https://status.1984.is/status/public/ ; structured first-party response: https://status.1984.is/api/status-page/public

## adjudication

these are materially conflicting general accounts of the breadth of exposure: the universal reading of the operator's statement is incompatible with the provider's explicit limitation. they are not yet a directly adjudicated contradiction about this specific wagyu server or key. it is unknown whether that server belongs to the seven-site exception, whether deleted storage/internal files fall under the provider's term customer-hosted data, and whether the parties describe the same access period and storage layers. disruption of all services does not mean disclosure of all customer files.

the later provider statement is not an independent forensic certification; the operator's explanation is not independently verified either. neither statement establishes that the other party is lying. native key exfiltration and the october/november causal link remain unresolved. editorial text should place both dated accounts side by side and describe the disagreement over scope, with the server/key link unverified.

## full-post recovery attempts

the original x page returned http 403; the public syndication endpoint returned an empty object. both requests and responses/errors are preserved. no full text is invented beyond the surviving oembed excerpt.
