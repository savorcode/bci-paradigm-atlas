# Sprint 4 markers_D worklog (curator_d, 2026-10-12)

Scope: MK.affective_band_power, MK.frontal_alpha_asymmetry, MK.HbO_prefrontal, MK.BOLD_amygdala, MK.BOLD_anterior_insula, MK.BOLD_striatum_reward, MK.BOLD_vmPFC_value, MK.BOLD_dACC, MK.BOLD_mPFC, MK.BOLD_TPJ.
None had generators/indexes before this sprint. Edited with Python (yaml.safe_load / safe_dump); only generators, indexes and notes changed (stale "to be added in the second pass" phrases removed, Sprint 4 line appended). MK.HbO_prefrontal was flow-style YAML and is now block-style (same content). `python3 scripts/validate.py` -> 0 problems, 0 warnings.

## Retrieval
- 51 distinct sources, all records retrieved (Crossref 39, OpenAlex 12 as fallback after 3 Crossref 429s and 7 fetch errors). No source cited without a retrieved record.
- Year convention as curator_a: print (volume) year where online and print differ (Feng 2015, Clithero 2014, Van Overwalle 2009, Rotgé 2015, Krall 2015, Cui 2011, Harmon-Jones 2010, Alarcão 2019, Zheng 2019, Fullana 2016, Herff 2014 [vol 7 = 2013 volume, published Jan 2014]).
- Frontiers article numbers (3, 76, 935) taken from OpenAlex first_page; Crossref record had none.

## Decisions
- Hemodynamic markers: generator = measured region, graded A where a coordinate-based meta-analysis localises the effect (amygdala, anterior insula, ventral striatum, vmPFC, dACC, dmPFC/vmPFC, TPJ). Dorsal striatum B (one primary study + meta-analysis that pools striatum).
- MK.BOLD_mPFC: two generators (BR.dmPFC for mentalizing, BR.vmPFC for self) following the Denny 2012 gradient.
- MK.BOLD_TPJ: factory id BR.TPJ (not BR.temporoparietal_junction).
- MK.HbO_prefrontal: DLPFC B from NIRS-fMRI co-registration (Cui 2011) + probabilistic optode projection (Okamoto 2004); frontopolar C (anatomical projection only). No fNIRS working-memory meta-analysis found -> CN.working_memory B.
- MK.frontal_alpha_asymmetry: CN.emotional_state B (not A) because the two meta-analyses diverge (Thibodeau 2006 positive; van der Vinne 2017 null for MDD). DLPFC C from a single LORETA study; frontal_cortex C (scalp topography cap).
- MK.affective_band_power: only scalp-channel evidence -> BR.frontal_cortex C. CN.emotional_state B: two independent datasets (DEAP, SEED) + survey; no meta-analysis; generalisation across subjects/datasets is weak.
- MK.BOLD_amygdala: CN.threat_fear B, not A — Costafreda 2008 supports fear stimuli, Fullana 2016 shows amygdala is not consistently activated in fear conditioning. CN.emotional_salience A.
- MK.BOLD_dACC: social exclusion graded B because Rotgé 2015 finds effects in ventral ACC and midcingulate rather than specifically dACC.

## Vocabulary mappings (see vocab_requests.csv)
- approach motivation -> CN.emotional_state; empathy for pain -> CN.somatosensation; fairness / charitable giving / social exclusion -> CN.social_interaction; reward anticipation -> CN.anticipation.

## Uncertainties for review
- CN.social_interaction ("人际协调与互动") is a loose fit for unfairness, prosocial value and exclusion; a CN.social_decision construct would be cleaner.
- Lateral temporal scalp sites in affective_band_power are not represented as a generator (no scalp-level temporal region id).
