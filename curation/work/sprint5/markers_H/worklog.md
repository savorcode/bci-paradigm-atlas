# Work log, sprint 5, markers group H (curator H)

Date: 2026-10-14. Scope: MK.EPN, MK.BOLD_pSTS, MK.speech_envelope_tracking, MK.linguistic_structure_tracking, MK.ERAN, MK.CPS, MK.interbrain_synchrony, MK.ISC, MK.HEP, MK.omission_response. Only `generators`, `indexes` and one `notes` sentence were added to each marker file; all other fields untouched. `python3 scripts/validate.py`: 0 problems, 0 warnings.

## Conventions

- Citation year and volume follow the print issue. Where the Crossref "issued" date is the online date of the preceding year (O'Sullivan 2015, Peelle 2013, Ding 2016, Koelsch 2009, Grosbras 2012, Park 2018) the print year is used.
- Grades: A only with a meta-analysis/systematic review or replication across independent laboratories and modalities; B for several studies (some from one lab, noted); C for a single study or same-group pairs; scalp-only evidence not used for generators.
- For hemodynamic and connectivity markers (BOLD pSTS, fNIRS inter-brain synchrony, fMRI ISC) the generator is the measured region; method recorded as "fMRI localization" (for fNIRS, channel localisation of the hemodynamic signal).

## Decisions and uncertainties per marker

- MK.EPN: generator evidence is source estimation from one group (Junghöfer, Schupp) → C. Attention modulation graded B, but the sensitivity of the EPN to task load is debated.
- MK.BOLD_pSTS: pSTS and social perception graded A on the Grosbras 2012 ALE meta-analysis. Multisensory integration (Beauchamp 2004) kept at C; the audiovisual STS cluster is not identical with the biological-motion cluster.
- MK.speech_envelope_tracking: attentional modulation graded A on cross-lab, cross-modality replication (MEG, ECoG, EEG), not on a meta-analysis. The entrainment-versus-evoked debate noted on the CN.neural_entrainment link.
- MK.linguistic_structure_tracking: only STG listed as generator (Ding 2016 ECoG). Frontal ECoG sites in that study were not added because the record did not let me confirm the region (IFG vs. middle frontal). Statistical-learning link filed under CN.perceptual_learning (vocab request CN.statistical_learning).
- MK.ERAN: IFG (Maess 2001 MEG; Koelsch 2002 fMRI) B; STG C from Sammler 2013 subdural EEG; the abstract was not available in the OpenAlex record, the STG attribution rests on the paper's indexed keywords and the curator's reading of the paper; flag for full-text check. Music syntax filed under CN.syntactic_processing (vocab request CN.music_syntax).
- MK.CPS: no localisation study of the speech CPS found; generators (PCC, hippocampus) come from source analysis of the music CPS (Knösche 2005) → C and explicitly indirect. Prosody link B: three Leipzig studies plus an independent replication (Holzgrefe 2013, Potsdam). Holzgrefe full text could not be opened (browser check); its inclusion rests on title and Crossref record.
- MK.interbrain_synchrony: frontal cortex A and TPJ B from the Czeszumski 2022 fNIRS meta-analysis (TPJ supported by fewer studies). IFG C (Jiang 2012). EEG hyperscanning synchrony is not localised.
- MK.ISC: visual cortex C, STG B, precuneus C (fMRI). Attention link B but the two EEG studies share a senior author (Parra).
- MK.HEP: insula subdivision not given in Park 2018 or Pollatos 2005; filed under BR.posterior_insula (interoceptive cortex) with vocab request BR.insula. Interoception A on Coll 2021, which itself warns about heterogeneous methods. Self-processing links share a senior author → C.
- MK.omission_response: STG B from intracranial (Hughes 2001) plus MEG source (Raij 1997). CN.anticipation link (sound-specific pre-activation) C.

## Open items

- All 51 sources `verified: false`; full-text check needed, priority Sammler 2013 (ERAN STG) and Holzgrefe 2013 (CPS replication).
- Three vocabulary requests in vocab_requests.csv.
