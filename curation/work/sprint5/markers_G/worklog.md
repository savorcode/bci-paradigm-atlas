# Sprint 5 markers_G worklog (curator G)

Date: 2026-10-14. Scope: MK.theta_drowsiness, MK.parietal_old_new, MK.hippocampal_theta, MK.NoGo_P3, MK.FN400, MK.Dm, MK.switch_positivity, MK.N450, MK.CPP, MK.presaccadic_potential. Only `generators`, `indexes` and an appended `notes` sentence were changed in each file. All sources `verified: false`.

## Decisions

- **Grading.** A only where a meta-analysis/systematic review exists (Tran 2020 for fatigue theta) or cross-laboratory, cross-modality replication (hippocampal theta: depth electrodes plus MEG). Generators supported only by scalp topography are capped at C. fMRI localisation of a region linked to an ERP effect is treated as indirect for the ERP (C) even when the fMRI evidence is meta-analytic (Kim 2011 for Dm/IFG).
- **MK.theta_drowsiness.** Generator BR.frontal_cortex (C, scalp topography only): sleepiness theta has a frontal/fronto-central emphasis, but Tran 2020 shows large effects at frontal, central and posterior sites. No source-imaging study located. Indexes CN.vigilance (A) and CN.sleep (B, homeostatic sleep pressure; Cajochen 1995 and Finelli 2000 from separate laboratories).
- **MK.parietal_old_new.** Generator BR.parietal_cortex (C, fMRI localisation via Vilberg & Rugg 2008; inference only). Index CN.recognition_memory (recollection) B.
- **MK.FN400.** Generator BR.frontal_cortex (C, scalp topography only, explicitly noted that a frontal maximum does not identify the source). Index CN.recognition_memory (familiarity) B, with the conceptual-priming alternative (Paller 2007) recorded in the note rather than as a second index, because no README construct fits conceptual priming.
- **MK.hippocampal_theta.** Generator BR.hippocampus A. Index CN.spatial_navigation kept at B because the earliest study (Kahana 1999) recorded cortical, not hippocampal, theta. CN.episodic_encoding B with the frequency-dependent direction (Lega 2012) noted.
- **MK.NoGo_P3.** Midcingulate cortex is the main source in distributed source estimates (Hong 2017; Huster 2013 review) -> mapped to BR.dACC; vocabulary request BR.MCC filed. BR.IFG B from two independent source studies (Enriquez-Geppert 2010; Hong 2017). Index CN.response_inhibition B; the review notes debate on inhibition versus outcome evaluation.
- **MK.Dm.** BR.hippocampus B (intracranial Fernández 1999 plus fMRI meta-analysis); note records that the scalp contribution of medial temporal closed-field sources is uncertain. BR.IFG C. Index CN.episodic_encoding B.
- **MK.switch_positivity.** Only one combined ERP-fMRI study (Jamadar 2010) -> BR.parietal_cortex C. Index CN.task_switching B; Nicholson 2005 and Jamadar 2010 are from the same group, but the Karayanidis 2010 review documents replications from other laboratories (Lavric, Miniussi, Poulsen and others). An independent primary study (Lavric 2008) could not be traced to a DOI within the search budget.
- **MK.N450.** BR.dACC B (dipole and distributed source models from two laboratories). Index CN.conflict_monitoring B.
- **MK.CPP.** BR.parietal_cortex C (topography). BR.preSMA C from Pisauro 2017 (posterior medial frontal cortex, value-based task); vocabulary request BR.pMFC filed. CN.evidence_accumulation B (O'Connell/Kelly group plus Pisauro 2017 from a different laboratory; review O'Connell 2018). CN.metacognition C (single study, Herding 2019).
- **MK.presaccadic_potential.** BR.FEF C: Richards 2003 dipoles in BA 8/10/11; BA 8 taken as the FEF region. An MEG high-gamma study (Hinkley 2010) also locates saccade preparation in FEF but concerns a different signal, so it is not cited. Index CN.motor_preparation B.

## Uncertainties

- Year conventions: Kim (NeuroImage 54(3)) and Hanslmayr (J Cogn Neurosci 20(2)) carry an earlier online year in OpenAlex; cited with the issue year (2011, 2008). Lega 2012 likewise issued online 2011, cited 2012 (Crossref print year).
- Karayanidis 2010: the Crossref record lists only the first author; the full author list was taken from the OpenAlex record.
- Everling 1997 and Herding 2019 abstracts were not available in the record; Herding was checked against an abstract on the neuinfo record. Everling 1997 is cited for the general pro-/antisaccade presaccadic negativity finding and should be prioritised in the full-text check.
- Liotti 2000 ACC dipole is cited from prior knowledge of the paper; the OpenAlex record confirms bibliographic details only. Flag for full-text check.
- Crossref failures: 11 look-ups failed with a 429 or fetch error and were confirmed through the OpenAlex API instead; one candidate DOI resolved to an unrelated paper and was discarded.

## Validation

`python3 scripts/validate.py` -> 0 problems, 0 warnings.
