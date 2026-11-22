# accessible text alternatives for figures

Years are source reference years. All values represent reported statistical entries, with conditional scenarios in a separate column. Fixed geography does not harmonize national classification. Unresolved discrepancies are described in the [phase 23 report](../phase23/REPORT.md) and the [English editorial draft](EDITORIAL_REPORT_DRAFT.md).

## lead figure · the 2019 to 2020 geography comparison

| year and scope | reported attack entries |
|---|---:|
| 2019, original EU28 | 119 |
| 2019, fixed EU27 | 55 |
| 2020, original EU27 | 57 |
| 2020, later official revision | 56 |

the 2019 subtraction removes 64 UK entries. the 2020 revision is a separate observation. sources: TE-SAT 2020 p. 84, TE-SAT 2021 pp. 12 and 99, and TE-SAT 2023 p. 9 n. 4.

## 01 and 02 · geography, reported attack entries and arrests

| year | original eu28 attacks | fixed eu27 attacks | fixed eu27 arrests |
|---|---:|---:|---:|
| 2015 | 211 | 108 | 943 |
| 2016 | 142 | 66 | 853 |
| 2017 | 205 | 98 | 807 |
| 2018 | 129 | 69 | 783 |
| 2019 | 119 | 55 | 723 |
| 2020 | — | 57 | 449 |
| 2021 | — | 15 | 388 |
| 2022 | — | 28 | 380 |
| 2023 | — | 120 | 426 |
| 2024 | — | 58 | 449 |
| 2025 | — | 45 | 486 |

The original eu28 column applies through 2019; the later years have no comparable original eu28 entry. The later chart observation of 193 for 2015 is unresolved. The 2023 reporting cohort includes 26 entries from earlier French occurrence years. Attack entries and reported arrests are separate measures. The 2023 arrest total of 426 remains separate from a later annex sum of 431; the 2025 age note uses 344 while the jihadist arrest table gives 347.

## 03 · later official revisions and conditional sensitivity

| year | original fixed eu27 | later official revision | conditional scenario |
|---|---:|---:|---:|
| 2020 | 57 | 56 | 56 |
| 2021 | 15 | 18 | 22 |
| 2022 | 28 | — | 50 |
| 2023 | 120 | — | 94 |

The conditional series uses the two later official revisions and reallocates 26 older french entries from the 2023 reporting cohort to the stated occurrence years 2021 and 2022. Individual matches and potential overlap remain unresolved. A blank official-revision field means no verified later value in this dataset, not zero.

## 04 · identification coverage

| year | original statistical entries | adequately identified | candidate | unidentified |
|---|---:|---:|---:|---:|
| 2015 | 211 | 9 | 3 | 199 |
| 2016 | 142 | 20 | 1 | 121 |
| 2017 | 205 | 27 | 1 | 177 |
| 2018 | 129 | 22 | 0 | 107 |
| 2019 | 119 | 24 | 1 | 94 |
| 2020 | 57 | 15 | 0 | 42 |
| 2021 | 15 | 14 | 1 | 0 |
| 2022 | 28 | 12 | 3 | 13 |
| 2023 | 120 | 9 | 1 | 110 |
| 2024 | 58 | 9 | 7 | 42 |
| 2025 | 45 | 7 | 17 | 21 |

Each year's denominator is its original reporting cohort, including the uk through 2019. In 2025, 18 possible event identities relate to 17 candidate entries. The figures describe the investigation's public-source linkage coverage, not the existence of physical incidents or europol's internal evidence. Each desktop bar is a share of that year’s original cohort. Class order is adequate, candidate and unidentified, from bottom to top. The table gives exact counts.

## 05 and 06 · institutional and judicial observations

[Institutional observations with exact counting units](../phase23/institutional_counts.csv) · [judicial observations with dates and source types](../phase23/judicial_chain.csv).

[Institutional reporting analysis](../phase23/REPORT.md) · [judicial case analysis](../phase23/REPORT.md) · [English source guide](../phase25/SOURCE_GUIDE.md).


### institutional figures for reference year 2025

| country | issuer | count | unit |
|---|---|---:|---|
| germany | north rhine-westphalia | 5 | jihadist motivated attacks nationwide |
| germany | federal government | 4 | locations named in the federal answer |
| germany | europol | 4 | completed jihadist entries |
| france | PNAT | 3 | completed jihadist inspired attacks |
| france | europol | 2 | completed jihadist entries |

the records have no shared event identifier. the totals do not identify any missing event.

### judicial observations and document dates

| case | date | observation and evidence stage |
|---|---|---|
| A100 | 19 august 2020 | initial police and prosecutor assessment |
| A100 | 31 january 2022 | first instance finding and psychiatric placement |
| A100 | 16 february 2023 | federal court review, decision final |
| holbæk | 14 may 2024 | Østre Landsret announced the conviction on appeal and 16 year sentence in case S-25-23; PET reported the result in a separate agency statement |
| solingen | 2025 | TE-SAT publication year for europol's account of contact and encouragement |
| solingen | 12 may 2026 | federal court dismissed the appeal, 3 StR 55/26 |
| solingen | 22 may 2026 | federal court published notice 091/2026 summarizing lower court findings about encouragement and advice |

the A100 statistical link remains a candidate. the solingen case chronology concerns the 2024 incident; the last two dates distinguish the appellate decision and notice. additional holbæk review remains unverified. the examples do not establish shared operational command.

## fixed EU27 identification breakdown

The historical UK subsets in the [2015](../../2015/crosswalk.csv), [2016](../../2016/crosswalk.csv), [2017](../../2017/crosswalk.csv), [2018](../../2018/crosswalk.csv) and [2019](../../2019/crosswalk.csv) crosswalks contain 410 entries (12 adequate, 2 candidate and 396 unidentified). To reproduce, filter `country_iso2` to `GB` in these five files and sum `total`, `adequate`, `candidate` and `unidentified`. Subtract each sum from its corresponding original series total. From 2020 the original EU geography is used.

| scope | total | adequate | candidate | unidentified |
|---|---:|---:|---:|---:|
| original reporting geography | 1129 | 168 | 35 | 926 |
| fixed EU27 | 719 | 156 | 33 | 530 |
