# Evidence provenance and documented corrections

## 2016 injury figures

**Original primary PDF reopened:** [Europol, *European Union Terrorism Situation and Trend Report 2017*](https://www.europol.europa.eu/sites/default/files/documents/tesat2017.pdf). This is a **same-edition, directly verified internal numerical incompatibility**, not an inference from later national casualty revisions.

| Source location (printed page) | Original statement / number | Audit result |
|---|---|---|
| p. 10, general overview | **379** injured; **142** victims killed; **142** attacks reported | Confirmed as original headline |
| p. 49, Annex 1 | **374 out of 379** casualties in religiously inspired category; **135 out of 142** deaths | Confirmed original annex wording |
| p. 24, Brussels narrative | **340** injured across Zaventem and Maelbeek, combined | Confirmed; **do not duplicate across both sites** |
| p. 23, Nice narrative | **201** injured | Confirmed |
| p. 23, Berlin narrative | **56** injured | Confirmed |

**Arithmetic:** 340 + 201 + 56 = **597**, exceeding the report's 379 by **218**. Even the two-event sum Brussels + Nice = **541**, exceeding 379 by **162**. All three events are described by the report as 2016 attacks in the EU. **Therefore the narrative figures and the headline cannot be treated as one consistent, additive injury population.** The underlying cause (definition, correction, temporal cutoff, editorial error or another issue) is **not established** by the checked pages. Do not assign one.

Europol's [web edition §1.1](https://www.europol.europa.eu/tesat/2017/1.1.TERRORIST_ATTACKS_AND_SUSPECTS_ARRESTED.html) and Annex 1 retain the divergent source observations. No corrigendum was found in the sources examined. The aggregate, annex and narrative figures have no verified common measurement definition. See the [statistical discrepancy register](../audit/DISCREPANCIES.md).

## Italian source and event corrections

Two original Italian government sources were added to [2016 source register](../2016/sources.csv):
- `IT16-INTEL`: 2016 intelligence report, Senate Doc. XXXIII no. 4, printed pp. 69–70; source URL in register.
- `IT16-INTERIOR`: Ministry of Interior parliamentary report, Doc. XXXVIII no. 5 vol. I, printed pp. 11–12; source URL in register.

The following **only** fields were amended in [2016 case register](../2016/incidents.csv): `IT16-CIV.event_date=2016-01-12` and source IDs `EU16;IT16-INTEL;IT16-INTERIOR`; `IT16-PAR.event_date=2016-06-07` and `EU16;IT16-INTEL`; `IT16-BIO.event_date=2016-06-09`, `locality=Milan`, and `EU16;IT16-INTEL`. Original Europol source ID, confidence, category, outcome, death and injury cells, event IDs and row counts were retained.

The initial 2016 intelligence report descriptions of the Parma and Milan cases as unclaimed remain distinct from the intelligence assessment of a probable common campaign and Europol’s FAI/FRI-cell attribution. The Civitavecchia claim does not establish who carried out the other cases. [Judgment and incident crosswalk](JUDGMENT_INCIDENT_CROSSWALK.md) · [FAI/FRI profile](organisations/FAI_FRI.md).

## Attribution boundaries

The [organisation index](ORGANISATIONS.md) separates ideological affinity, a public claim, an intelligence assessment, a court finding and an executive designation. The [source register](SOURCES.md) supplies the national and institutional locators. The annual and case datasets remain the source of the recorded evidence classifications.
