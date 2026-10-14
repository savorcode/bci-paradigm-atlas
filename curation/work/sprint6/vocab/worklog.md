# Sprint 6 vocabulary work log

Vocabulary curator, 2026-10-14. Requests from the sprint 5 marker groups (`curation/work/sprint5/markers_{F,G,H}/vocab_requests.csv`), handled as approved in D-077. Details in `mapping.csv` and `remap.csv`.

## 1. New terms

Regions (`knowledge/regions.yaml`, 45 → 47):

- `BR.inferior_colliculus` (下丘（听觉中脑）), placed after BR.thalamus. No parent: the file has no brainstem or midbrain macro region. `atlas_refs` left out because there is no Brodmann or HCP-MMP1.0 area, and AAL3 has no inferior colliculus label. MNI152. Localisation source: Sitek et al. 2019 (eLife), an MNI-space atlas of the subcortical auditory system. Record retrieved from the Crossref API.
- `BR.insula` (脑岛（未区分亚区）), placed before BR.anterior_insula. No parent, because the insula subregions had none. Atlas refs: BA13 (the Talairach-atlas convention; Brodmann did not number the human insula, and BA14 is not used), AAL3 Insula_L/R, and HCP-MMP1.0 AAIC, AVI, MI, Ig, PoI1 and PoI2. Opercular, para-insular and piriform parcels are not included. The AAL3 and Glasser source objects are reused.
- `BR.anterior_insula` and `BR.posterior_insula` now have `parent: BR.insula`. Nothing else in them changed.

Constructs (`knowledge/constructs.yaml`, 90 → 92):

- `CN.statistical_learning` (统计学习, parent CN.memory), placed after CN.perceptual_learning. Cognitive Atlas has no concept under "statistical learning", "statistical-learning" or "probabilistic learning". "Sequence learning" and "implicit learning" (which has no definition) do exist but do not fit, so `cognitive_atlas` is left out.
- `CN.music_syntax` (音乐句法加工, parent CN.perception), placed after CN.syntactic_processing. Maps to Cognitive Atlas trm_hsrxov4azQ6nM (music syntax), an exact name match. Its Cognitive Atlas definition is broader than ours, and the term's notes say so.

## 2. Not added: BR.MCC and BR.pMFC

- BR.dACC notes: studies naming the anterior midcingulate cortex are mapped here.
- BR.preSMA notes: "posterior medial frontal cortex" reports that span pre-SMA and dACC are mapped here, or to BR.dACC when the peak is cingulate.
- The links in MK.NoGo_P3 and MK.CPP stay as they are.

## 3. Re-mapped links (4 markers)

- MK.FFR: added a BR.inferior_colliculus generator with evidence B (MEG/EEG source). Sources are Coffey et al. 2016, whose abstract names the cochlear nucleus, inferior colliculus and medial geniculate; Bidelman 2018, which finds that subcortical sources dominate; and Coffey et al. 2019, a review. All three records were retrieved from the OpenAlex API. The BR.A1 and BR.thalamus generators are kept, and the thalamus note no longer says the midbrain source lacks an id. The cochlear nucleus still has no id. This is noted but not requested.
- MK.linguistic_structure_tracking: index CN.perceptual_learning → CN.statistical_learning (Batterink & Paller 2017). Evidence C and the relation are unchanged.
- MK.ERAN: index CN.syntactic_processing → CN.music_syntax. Evidence B and the relation are unchanged, and the note keeps the single-group caveat.
- MK.HEP: generator BR.posterior_insula → BR.insula. Neither source gives an insular subdivision. Evidence B is unchanged.

In all four, the placeholder notes that pointed to `vocab_requests.csv` were removed.

## 4. Validation

`python3 scripts/validate.py`: 0 problems, 0 warnings (129 markers, 47 regions, 92 constructs).

## Open points

- BR.insula lists BA13, but BR.anterior_insula and BR.posterior_insula still leave Brodmann out (their notes say insular areas are not defined in the human map). The lead may want to align these.
- CN.statistical_learning has no Cognitive Atlas mapping.
- The Cognitive Atlas concept for CN.music_syntax is defined more broadly than our term.
- No new sources have been checked against the full text yet (`verified: false`).
