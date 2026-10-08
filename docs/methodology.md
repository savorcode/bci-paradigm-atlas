# Methodology

**English** | [简体中文](methodology.zh-CN.md)

This document defines what the atlas records and the rules every entry follows. It is versioned with the schemas (currently schema 0.2); changes are noted in the changelog.

## 1. Definitions

**Paradigm.** A reproducible specification of stimuli, task instructions and timing, designed to elicit brain activity that is recorded and analysed. A paradigm is defined independently of any single study; studies and datasets instantiate it. Since schema 0.2 the atlas records paradigms at two levels (`curation/decisions.md` D-057):

**Paradigm class.** A group of concrete paradigms that share one mechanism: they elicit the same neural markers, probe the same cognitive constructs and have a common origin publication. A class records the markers, constructs, the class's origin (`first_source`) and a description. Classes are registered in `paradigms/_classes.yaml` with identifiers of the form `<FAMILY>-<SHORT>` (e.g. `MOT-MI`). A change of the elicited marker or of the construct being probed makes a different class. The class's `first_source` is the earliest bibliographically identifiable original study of any configuration in the class; it need not be the source of `-001`, which is the canonical configuration (D-062). A class's `markers` are the union of the markers of its concrete paradigms (D-061).

**Concrete paradigm (protocol).** One reproducible task configuration within a class, with its own class/condition set, cue and stimuli, trial structure, feedback mode and datasets. Its identifier is `<FAMILY>-<SHORT>-<NNN>` (e.g. `MOT-MI-001` left/right-hand two-class, `MOT-MI-002` left hand/right hand/both feet/tongue four-class). Each concrete paradigm is one file under `paradigms/<family>/`; its `class` field points to its class, and its `protocol` block states the configuration and what distinguishes it from its sibling protocols. Numbering rules are given in §6.

**Variant.** A parameter-level change that keeps the configuration: durations, inter-stimulus interval, number of trials, frequency values within the same coding scheme, electrode count or participant population. Variants are recorded in the concrete paradigm's `variants` or parameter ranges and receive no new number. A change of the class/condition set, the stimulus or cue type (including the coding scheme), the trial structure or the feedback mode is not a variant but a new concrete paradigm (§6).

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
- Verification has two levels (D-072): *bibliographic* verification confirms the citation fields against the Crossref, OpenAlex or PubMed record and is recorded in `curation/verification/sources_check.csv` and in the notes phrase `bibliography confirmed|corrected (<API>, <date>)`; *content* verification confirms against the full text that the publication describes the paradigm and is the earliest, and only content verification sets `verified: true`.

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
| Paradigm class | `<FAMILY>-<SHORT>` | `MOT-MI` |
| Concrete paradigm | `<FAMILY>-<SHORT>-<NNN>` | `MOT-MI-001` |
| Neural marker | `MK.<name>` | `MK.SMR_ERD` |
| Brain region | `BR.<name>` | `BR.visual_cortex` |
| Cognitive construct | `CN.<name>` | `CN.sustained_visual_attention` |

`<FAMILY>` is the three-letter prefix from `taxonomy/families.yaml`, `<SHORT>` is 2–8 upper-case letters or digits, and `<NNN>` is a three-digit serial number. The `class` of a concrete paradigm must equal its identifier without the `-<NNN>` suffix and belong to the same family.

**Numbering criteria.** Within a class, a new serial number is assigned when any of the following changes:

1. **Class/condition set**: the number or identity of the classes, targets or conditions decoded or contrasted. For homogeneous, interchangeable target sets (SSVEP/c-VEP keyboards, P300 matrices, loudspeaker or tactor positions) the number of targets is a parameter, not a criterion; adding or removing a rest/idle/non-control class is a criterion-1 change (D-058);
2. **Stimulus or cue type**, including the stimulus coding scheme (e.g. SSVEP frequency coding vs joint frequency–phase coding; P300 row/column vs checkerboard flashing);
3. **Trial structure**: e.g. synchronous (cue-paced) vs asynchronous (self-paced); single-trial vs block;
4. **Feedback mode**: none / discrete / continuous; open vs closed loop.

Parameter changes alone (durations, ISI, number of trials, frequency values within the same scheme) receive no new number and are recorded as variants (§1). The `protocol.distinguishing` field of a new concrete paradigm cites the criterion or criteria it rests on.

**Numbering example (motor imagery, matching the files in `paradigms/motor/`).**

| ID | Concrete paradigm | Basis |
|---|---|---|
| `MOT-MI` | Class: cued motor imagery (MK.SMR_ERD; origin Pfurtscheller & Neuper 1997) | — |
| `MOT-MI-001` | Left vs right hand, visual cue, synchronous trials, no feedback | standard configuration |
| `MOT-MI-002` | Left hand / right hand / feet / tongue, four classes | criterion 1 |
| `MOT-MI-003` | Six movements of one upper limb (elbow flexion/extension, forearm supination/pronation, hand open/close) + rest, seven classes (Ofner et al. 2017) | criterion 1 |
| `MOT-MI-005` | Left vs right hand with continuous visual feedback | criterion 4 |
| `MOT-MI-009` | Asynchronous (self-paced) motor imagery with an idle state | criterion 3 (and 1) |
| `MOT-MI-011` | Eleven upper-extremity tasks (Jeong et al. 2020) | criterion 1 |

(Erratum, 2026-10-03: the first draft of decision D-057 listed the eleven-class protocol as `MOT-MI-003`, which did not match the files; corrected per D-067.)

**Permanence.** Identifiers are permanent. `-001` is the canonical configuration of the class (not necessarily the earliest published one; an earlier sibling is named in its notes and supplies the class origin, D-062) and is never renumbered; later numbers are assigned in the order protocols are recognised. The meaning of every identifier is frozen from release v0.1.0; later corrections deprecate the entry and assign a new number (D-063). A removed entry is marked `deprecated` and its identifier is not reused; nor are the identifiers of merged candidates.

## 7. Status workflow

`draft` → `reviewed` → (optionally) `deprecated`. An entry becomes `reviewed` when all of its sources are verified and at least one maintainer other than the contributor has approved it.

## 8. Versioning

The repository follows Semantic Versioning. Changes to schemas that invalidate existing entries increase the major version after v1.0. Each release is a citable snapshot of the atlas.

## References

Zander TO, Kothe C. Towards passive brain–computer interfaces: applying brain–computer interface technology to human–machine systems in general. *J Neural Eng.* 2011;8(2):025005. doi:10.1088/1741-2560/8/2/025005
