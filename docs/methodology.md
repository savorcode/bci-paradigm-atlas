# Methodology

**English** | [简体中文](methodology.zh-CN.md)

This document defines what the atlas records and the rules every entry follows. It is versioned with the schemas; changes are noted in the changelog.

## 1. Definitions

**Paradigm.** A reproducible specification of stimuli, task instructions and timing, designed to elicit brain activity that is recorded and analysed. A paradigm is defined independently of any single study; studies and datasets instantiate it.

**Variant.** A modification of a paradigm that preserves its core logic (for example, a change of stimulus modality or presentation layout). A modification that changes the elicited marker or the construct being probed is treated as a separate paradigm.

**Neural marker.** A measurable feature of brain activity with a characteristic signature: an ERP component, an oscillatory modulation, a steady-state response, a hemodynamic response, or a single-unit or field-potential pattern.

**Cognitive construct.** A psychological process or state that a marker is held to reflect. Constructs are mapped to Cognitive Atlas concepts where an equivalent exists.

**BCI category.** Following Zander and Kothe (2011): *active* (the user intentionally produces a control signal, e.g. motor imagery), *reactive* (the signal is elicited by external stimulation the user attends to, e.g. SSVEP, P300), *passive* (the signal reflects an implicit state without intentional control, e.g. workload, error perception). Paradigms used only in basic research are recorded as `none`.

## 2. Scope and inclusion criteria

A paradigm is included if all of the following hold:

1. It has been used to record brain activity in humans with at least one recording modality listed in `taxonomy/recording_modality.yaml`.
2. It is described in a peer-reviewed publication or a public preprint with enough detail to be reproduced.
3. It elicits at least one neural marker that can be documented in the knowledge base.

Paradigms used exclusively in non-human studies are out of scope for v1. Clinical protocols are included when they satisfy the criteria above.

## 3. Source rules

- Every claim cites a publication with a persistent identifier (DOI, PMID or arXiv ID) where one exists.
- Sources are checked against the original publication. Secondary citations are not accepted.
- Identifiers are never inferred. An unverifiable field is left empty.
- A source is marked `verified: true` only after a maintainer has checked it.

## 4. Origin attribution

`first_source` records the earliest publication that introduced the paradigm in a recognisable form. Where precursors exist, or where priority is disputed, the entry lists the candidates in `notes` with a short justification. Attribution reflects the published record and can be revised when new evidence is provided.

## 5. Evidence grades

Each *generates* (region → marker) and *indexes* (marker → construct) link carries a grade:

| Grade | Meaning |
|---|---|
| A | Supported by a meta-analysis or systematic review, or replicated across independent laboratories and modalities |
| B | Supported by multiple independent studies |
| C | Supported by a single study or by indirect evidence |
| D | Proposed or theoretical; not yet directly tested |

Grades describe the strength of the published evidence, not the importance of the link.

## 6. Identifiers

| Entity | Format | Example |
|---|---|---|
| Paradigm | `<FAMILY>-<SHORT>-<NNN>` | `MOT-MI-001` |
| Neural marker | `MK.<name>` | `MK.SMR_ERD` |
| Brain region | `BR.<name>` | `BR.visual_cortex` |
| Cognitive construct | `CN.<name>` | `CN.sustained_visual_attention` |

Identifiers are permanent. A removed entry is marked `deprecated` and is not reused.

## 7. Status workflow

`draft` → `reviewed` → (optionally) `deprecated`. An entry becomes `reviewed` when all of its sources are verified and at least one maintainer other than the contributor has approved it.

## 8. Versioning

The repository follows Semantic Versioning. Changes to schemas that invalidate existing entries increase the major version after v1.0. Each release is a citable snapshot of the atlas.

## References

Zander TO, Kothe C. Towards passive brain–computer interfaces: applying brain–computer interface technology to human–machine systems in general. *J Neural Eng.* 2011;8(2):025005. doi:10.1088/1741-2560/8/2/025005
