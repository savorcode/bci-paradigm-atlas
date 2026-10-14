# Sprint 5 vocabulary work log

Vocabulary curator, 2026-10-14. Rules as in `curation/work/sprint4/README.md`; requests from D-076.

## 1. Cognitive Atlas mappings (constructs)

Looked up each of the 9 new constructs with the Cognitive Atlas API (`concept?name=`), trying synonyms when the name was not found. Details in `mapping.csv`.

- Found (7): perceptual_learning, perceptual_discrimination (broader concept "discrimination"), auditory_selective_attention ("auditory attention", defined as selective), emotion_regulation, reward_anticipation, empathy, voice_perception.
- Not found (2): approach_motivation, social_decision. Several synonyms returned no concept; `cognitive_atlas` left out.

## 2. Regions BR.OFA and BR.SEF

- Added `atlas_refs` (Brodmann, AAL3, HCP-MMP1.0), kept `coordinate_space: MNI152`, added the AAL3 (Rolls 2020) and Glasser 2016 source objects plus one localisation paper each, and `notes`.
- BR.OFA: BA19 / Occipital_Inf_L,R / PIT (low confidence). Localisation source Pitcher, Walsh & Duchaine 2011; the Crossref API was rate-limited at the time, so the record was retrieved from the OpenAlex API.
- BR.SEF: BA6 / Supp_Motor_Area_L,R (AAL3 has no separate label) / SCEF. Localisation source Amiez & Petrides 2009, record retrieved from the Crossref API.
- Moved BR.OFA to sit after BR.FFA, and BR.SEF after BR.FEF.

## 3. Re-mapped sprint-4 links

13 changes in 12 markers, listed in `remap.csv`:

- 10 links moved from the closest id to the new id (sources unchanged).
- 2 old links kept because they have their own support, with the new link added alongside: MK.LPP (CN.emotional_state for arousal covariation, plus CN.emotion_regulation for reappraisal) and MK.BOLD_anterior_insula (CN.somatosensation for experienced pain, plus CN.empathy). In both cases the relation text was split between the two links.
- MK.BOLD_oculomotor: added a BR.SEF generator (evidence A, same sources as BR.FEF). The OpenAlex API records for Grosbras 2005 and Jamadar 2013 both name the supplementary eye fields in their abstracts. Took out the FEF note saying SEF had no id.
- MK.frontal_alpha_asymmetry: relation reworded to approach/withdrawal; grade B kept.

## 4. Validation

`python3 scripts/validate.py`: 0 problems, 0 warnings.

## Open points

- Neither approach_motivation nor social_decision has a Cognitive Atlas mapping.
- The HCP-MMP label for BR.OFA (PIT) has low confidence. PIT is also listed for BR.LOC.
- No sources in this work have been checked against the full text yet (`verified: false`).
