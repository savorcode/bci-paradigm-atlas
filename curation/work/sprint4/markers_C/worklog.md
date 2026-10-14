# Sprint 4 markers_C worklog (curator_c, 2026-10-12)

Scope: MK.FRN, MK.ERN, MK.oERN, MK.Pe, MK.ErrP, MK.N2_frontocentral, MK.frontal_midline_theta, MK.N400, MK.P600, MK.LPP.
Edits: added `generators` and `indexes`, appended one Sprint 4 sentence to `notes`; no other field changed (YAML re-serialised with yaml.safe_dump, so MK.frontal_midline_theta lost its flow style; content unchanged).
`python3 scripts/validate.py` -> 0 problems, 0 warnings.

## Retrieval constraints
- curl to Crossref/OpenAlex/EuropePMC is refused by the egress proxy (403); all records fetched with HTTP request.
- The shared HTTP request proxy gave HTTP 429 roughly every 2-3 requests; Crossref was the most throttled, so most records come from OpenAlex single-record lookups (accepted fallback). record_api column in links.csv says which.
- Every J Neurosci DOI (and one Neuron DOI) returned CLIENT_ERROR in both APIs, so no J Neurosci paper is cited. Dropped for that reason: Debener 2005 (ERN EEG-fMRI), Fu 2019 Neuron (single-unit ERN), Becker 2014 (FRN EEG-fMRI; DOI 10.1523/JNEUROSCI.3684-13.2014 found on publisher page but no API record), Steinhauser & Yeung 2010 / Boldt & Yeung 2015 (Pe and confidence), Liu 2012 (LPP generators), McCarthy 1995 (N400 intracranial).
- Rejected wrong remembered DOIs (record showed a different paper): Herrmann 2004 LORETA ERN/Pe, Gehring & Knight 2000. Bonini 2014 (Science) and Stemmer 2004 never retrieved -> not cited.
- OpenAlex lists only the first author for Gevins 1997 and Friederici 1999; remaining authors added from the article byline (flag for the full-text check).
- Year convention: volume (issue) year, not online-first year (Folstein 2008, Kutas & Federmeier 2011, Kuperberg 2007, Kim & Osterhout 2005, Cavanagh 2012, Sabatinelli 2007/2013).

## Grading decisions
- ERN -> BR.dACC A: EEG dipole (Dehaene 1994), MEG (Miltner 2003), fMRI meta-analysis (Ridderinkhof 2004) = cross-lab, cross-modality. No intracranial/lesion source retrieved; a curator may prefer B.
- ERN -> CN.error_monitoring A: independent-lab replications (Falkenstein 1991; Gehring 1993) + MEG. CN.conflict_monitoring C (single computational account, contested).
- FRN -> CN.reward_prediction_error A (Sambrook & Goslin 2015 meta-analysis). FRN -> BR.striatum C: Hajcak lab only, deep source unlikely to be a direct scalp generator.
- Pe -> CN.error_monitoring A: Wessel 2012 treated as a systematic evaluation of the error-awareness literature; if judged narrative, downgrade to B. Error awareness has no own construct id; mapped to CN.error_monitoring (CN.metacognition considered; no retrievable confidence study, so not added).
- oERN vs ErrP overlap: machine-observation effects put under MK.ErrP (B); MK.oERN gets CN.machine_error_perception only at C.
- N2: conflict vs inhibition accounts both kept at B, debate noted.
- FMT -> BR.dACC B (MEG from one group + independent EEG ICA source); BR.dmPFC C. mental_arithmetic C (one group).
- N400 -> CN.semantic_integration A (Šoškić 2022 systematic review + major review). ATL B with intracranial evidence (Nobre 1994) + MEG.
- P600: only generator retrievable is the basal-ganglia lesion effect (Friederici 1999), entered as BR.dorsal_striatum C with the caveat that it is a necessary contributor, not the cortical generator. Gap: cortical P600 generator.
- LPP: BR.visual_cortex B rests on two EEG-fMRI studies from one group plus Hajcak & Foti 2020 review; amygdala not added (could not confirm from retrieved records). Emotion regulation mapped to CN.emotional_state (vocab request CN.emotion_regulation). CN.emotional_salience kept at B (no meta-analysis retrieved).

## Open uncertainties
- Ferrez & Millán 2008 sLORETA-to-ACC and Bokura 2001 lateral-OFC source are from memory of the papers' content; DOI/metadata verified, claims need full-text check (verified: false).
- MK.ERN/FRN/oERN/Pe/ErrP/N2 `notes` still contain the first-pass sentence "Generators and indexes not yet written"; left unchanged per scope rule (only appending allowed). Maintainer may delete it.
