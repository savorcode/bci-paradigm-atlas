# Sprint 6, markers I: worklog (curator I, 2026-10-16)

Scope: MK.BOLD_stimulated_region, MK.AV_interaction_ERP, MK.BOLD_parahippocampal, MK.BOLD_premotor_parietal, MK.SCP, MK.SSSEP, MK.TEP, MK.oscillatory_entrainment. All links recorded in links.csv; all sources `verified: false`.

## Decisions

- **MK.BOLD_stimulated_region**: generator = stimulated region; BR.M1 chosen because it is the most frequent concurrent TMS-fMRI target and one of only two targets (with visual cortex) with a consistent local BOLD increase (Rafiei & Rahnev 2022). Graded B, not A, because that review attributes the M1 effect largely to movement re-afference. The index (CN.cortical_excitability) is graded C: the same review argues against local BOLD as an excitability readout outside M1/V1. Bestmann et al. 2008 cited as a review of intensity-dependent concurrent TMS-fMRI effects; its OpenAlex record had no abstract, so this attribution rests on the curator's knowledge of the paper and should be checked against the full text.
- **MK.AV_interaction_ERP**: intracranial evidence for auditory cortex (Besle 2008) is a single study -> C. Early posterior interaction effects (Giard & Peronnet 1999; Molholm 2002) rest on scalp topography / current-density mapping -> capped at C.
- **MK.BOLD_parahippocampal**: BR.parahippocampal graded A on the Boccia 2014 fMRI meta-analysis. The retrosplenial component is mapped to BR.precuneus (B) pending BR.retrosplenial. Scene selectivity mapped to CN.object_recognition pending CN.scene_perception. Owen 2006 and Monti 2010 share authors; graded B as two cohorts.
- **MK.BOLD_premotor_parietal**: premotor and parietal generators graded A on two ALE meta-analyses (Caspers 2010; Molenberghs 2012). Body ownership mapped to CN.self_processing (A: Grivaz 2017 meta-analysis plus Ehrsson 2004). CN.motor_imagery (A, Hétu 2013) added because the same network is the consistent motor-imagery network; this extends the marker beyond its description and could be dropped if the maintainers prefer a narrower scope.
- **MK.SCP**: SCPs have no single focal generator; BR.premotor (C) taken from the EEG-fMRI study of SCP self-regulation (Hinterberger 2005), where positivity control co-occurred with premotor deactivation. The basal ganglia activation in that study was not entered as a generator (subcortical modulation, not the scalp source). The journal abstract could not be retrieved; content was read from the matching poster abstract of the same study.
- **MK.SSSEP**: BR.S1 graded B (dipole modelling, Snyder 1992; MEG source, Vakorin 2019). BR.SII C (single MEG study).
- **MK.TEP**: generator = stimulated region; BR.M1 is the most studied target (B). Note: auditory and somatosensory contamination of TEPs is already flagged in the marker notes.
- **MK.oscillatory_entrainment**: generator = stimulated region; BR.parietal_cortex (C) because the cited studies stimulate parietal or parieto-occipital cortex at alpha frequency. Helfrich 2014 used an occipital montage; BR.visual_cortex would also be defensible.

## Uncertainties

- No meta-analysis was found for TEP or SSSEP links; grades stay at B/C.
- Citation for Sci Transl Med 2013 uses the article number 198ra105 from the OpenAlex API (Crossref record has no page field).
