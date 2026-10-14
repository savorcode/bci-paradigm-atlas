# Sprint 5 markers_F worklog (curator F)

Date: 2026-10-14. Scope: MK.cVEP, MK.alpha_lateralization, MK.VAN, MK.SEP_N20, MK.N2pc, MK.P2_visual, MK.N2_posterior, MK.FFR, MK.ASSR, MK.mVEP. Only `generators`, `indexes` and a one-line `notes` addition were changed. Validator: 0 problems, 0 warnings.

## Summary

- 13 generator links, 27 index links; grades A 4, B 17, C 19; 50 distinct sources, all retrieved from Crossref or OpenAlex.
- One DOI candidate rejected (10.1088/1741-2560/6/4/046002 resolves to an SSVEP/CCA paper, not the c-VEP study); replaced by Bin et al. 2011.

## Decisions and uncertainties

- MK.cVEP: no source-localization study of BCI c-VEP found. V1 generator rests on multifocal m-sequence VEP source mapping (Slotnick et al. 1999), which is a related but not identical paradigm; grade C. Intent selection graded B (two independent groups plus Martínez-Cagigal et al. 2021); the review is described by its authors as a literature review, so not A.
- MK.alpha_lateralization: generator in BR.visual_cortex (B) and BR.parietal_cortex (C). Fronto-parietal control regions (IPS/FEF) that modulate alpha were deliberately not entered as generators. Distractor suppression B rests on a framework paper plus one direct test.
- MK.VAN: generator BR.LOC graded C (one MEG study; the Förster review summarises further source work but is narrative). Perceptual awareness B: three narrative reviews, two of them from overlapping authors.
- MK.SEP_N20: S1 (area 3b) graded A — intracranial (Allison et al. 1989) and MEG/EEG (Wood et al. 1985) converge, plus IFCN recommendations. Consciousness-level link is prognostic (systematic review on post-cardiac-arrest outcome); noted as indirect.
- MK.N2pc: both source studies from the Hopf/Luck group, so C for both regions. BR.LOC used for ventral occipito-temporal sources.
- MK.P2_visual: generator uncertain; frontal cortex entered from scalp topography only (C). Emotional salience B (Carretié et al. 2001 plus Olofsson et al. 2008 review).
- MK.N2_posterior: generator from scalp topography only (C). Two N2c links rest on one study (Loughnane et al. 2016), so C.
- MK.FFR: dominant brainstem generator has no region id (vocab request BR.inferior_colliculus). A1 graded B (MEG evidence plus EEG source modelling that limits the cortical share); thalamus C.
- MK.ASSR: A1 graded A (intracranial Heschl gyrus recordings and MEG localization from independent labs). Schizophrenia meta-analysis mapped to CN.cortical_excitability (A) with a note that the construct mapping is indirect. Crossref page field for Thuné et al. 2016 shows only the first page; cited as given.
- MK.mVEP: hMT+/V5 graded B (dipole source analysis plus review of later work). BCI selection C (same group).
- Year conventions: when OpenAlex gave the online year, the print year of the cited volume was used (Koivisto & Revonsuo 2010; Folstein & Van Petten 2008; Kuba et al. 2007).
- MK.SEP_N20 was stored in flow style; rewriting it with the YAML dumper converted it to block style without changing values.
