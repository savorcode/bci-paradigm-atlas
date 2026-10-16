# Worklog - sprint 7, group Q2 (2026-10-17)

Assignment: PER-MUSAT, PER-FBA, PER-SURR, PER-TONIC, PER-SMMN, SSR-BINB, STM-TACEP, STA-RESP (from curation/work/sprint7/gap/gap_candidates.csv).
Contributor tags: curator_a (perception), curator_b (steady_state, stimulation), curator_e (state).

## Outcome

| Class | Family | Class first source | Concrete paradigms |
|---|---|---|---|
| PER-MUSAT | perception | Treder et al. 2014 | -001 multi-streamed musical oddball (Treder 2014); -002 continuous music, envelope decoding (Cantisani 2019, MAD-EEG) |
| PER-FBA | perception | Müller et al. 2006 | -001 overlapping red/blue dot fields, offline (Müller 2006); -002 online BCI, counter-rotating surfaces (Zhang 2010) |
| PER-SURR | perception | Chubb et al. 1989 (behavioural) | -001 centre-surround SSVEP (Vanegas 2015; HBN-EEG dataset) |
| PER-TONIC | perception | Hines & Brown 1936 | -001 cold pressor (Hines & Brown 1936); -002 10 min tonic heat with continuous rating (Schulz 2015) |
| PER-SMMN | perception | Kekoni et al. 1997 | -001 vibrotactile oddball |
| SSR-BINB | steady_state | Oster 1973 | -001 binaural beats |
| STM-TACEP | stimulation | Larsson & Prevec 1970 | -001 mechanical taps; -002 air-jet (Schieppati & Ducati 1984) |
| STA-RESP | state | Davis 1942 | -001 hyperventilation EEG; -002 breath-hold fMRI (Kastrup 1998) |

8 classes, 13 concrete paradigm files. Class entries: classes_new.yaml. Provisional IDs kept (all short codes unused; prefixes match the family directories).

Validation: `python3 scripts/validate.py` reports only the 13 expected "class not registered" errors. A trial merge of classes_new.yaml into a copy of the registry validates with 0 problems (292 classes).

## Duplicate checks

Searched paradigm ids, names and aliases in paradigms/ and paradigms/_classes.yaml for: polyphon, instrument, music attention, feature-based, superimposed / overlapping / dot field, selection negativity, surround suppress, cold pressor, capsaicin, tonic / sustained pain, somatosensory / tactile mismatch, sMMN, binaural, air-puff / air-jet, mechanical, tactile evoked, hyperventilation, breath-hold, respiratory, cerebrovascular; also curation/candidates.csv and curation/registry/*.csv.

- PER-MUSAT: no match. Neighbours: PER-AAD (speech streams, envelope decoding), PER-STREAM (segregation), PER-ODD (single stream), LAN-MUS (music syntax), SSR-ASSR-002 (two modulated tone streams), SSR-BEAT. Attention to an instrument in music is not covered.
- PER-FBA: no match. PER-CVA / PER-CUE are spatial; no SSVEP file uses overlapping feature-defined populations.
- PER-SURR: no match. SSR-SSVEP files have no surround manipulation; PER-CROWD is identification under crowding.
- PER-TONIC: no match. PER-LEP (phasic), SSR-NSSEP (periodic nociceptive), SOC-PAIN (empathy), EMO-STRESS (TSST/MIST, no pain stimulus).
- PER-SMMN: no file. PER-MMN-001..003 are auditory; PER-VMMN is a separate class with its own marker (D-041). PER-TACT is attention to tactile sites (N140/P3b), not a passive mismatch design.
- SSR-BINB: no match. SSR-ASSR uses physically modulated sounds; "binaural" appears only in STM-GVS (binaural mastoid GVS, unrelated).
- STM-TACEP: no match. STM-SEP is electrical; SSR-SSSEP periodic vibration; STM-VIB tendon vibration illusion; IMG-SAO uses vibrotactile stimulation for selective sensation.
- STA-RESP: no match. PER-RREP (inspiratory occlusion evoked potential) is a respiratory stimulus, not a breathing manoeuvre; SSR-SSVEP-003 notes mention hyperventilation only in a lead title (clinical audit).

## Decisions and uncertainties

1. PER-SMMN placement (D-041 vs draft D-060). Kept as a separate class by the PER-VMMN precedent (different sensory channel -> different marker and generator -> different class, D-041). D-060 (draft) says modality change is criterion 2 within a class and never creates a class; if confirmed, PER-SMMN-001 should become PER-MMN-004 (proposals.csv), and PER-VMMN would need the same review. MK.MMN is a placeholder; MK.sMMN requested.
2. STM-TACEP placement: same question with respect to STM-SEP; alternative STM-SEP-002/-003 in proposals.csv.
3. PER-FBA origin: Saenz et al. 2002 (fMRI, overlapping dot fields) predates Müller et al. 2006; the class source was set to the earliest frequency-tagged configuration because the gap entry scopes the class to overlapping frequency-tagged stimuli. Maintainer to decide whether Saenz 2002 should be the class first source (D-062 allows -001 to be the canonical configuration).
4. PER-SURR: class source behavioural (Chubb 1989, D-031); -001 source is the first EEG configuration found (Vanegas 2015). The class set (no / parallel / orthogonal surround) is inferred from the HBN factor structure and needs the Vanegas full text.
5. PER-TONIC: origin is a cardiovascular test (D-031). First neural recording not established (EEG lead Chen et al. 1989 could not be retrieved because of rate limiting). Capsaicin configuration not sourced (proposals.csv).
6. SSR-BINB: Oster 1973 is a Scientific American article used as the standard reference; flag weak_origin. MK.ASSR chosen over MK.oscillatory_entrainment because the systematic review reports inconsistent entrainment.
7. STA-RESP: Davis 1942 is the earliest standardised EEG hyperventilation record found (one author in the Crossref record; one-page entry). stimulus_modality motor_execution is the closest term for a voluntary breathing manoeuvre. Both markers are placeholders (MK.slow_wave, MK.HbO_prefrontal); requests MK.HV_slowing and MK.BOLD_CVR.
8. PER-MUSAT-002: protocol details beyond "attend to a target instrument in a mixture; 8 participants; 20-channel EEG" were not read; cue and excerpt durations left open. MK.speech_envelope_tracking is a placeholder (request MK.music_envelope_tracking).
9. PER-FBA-002 feedback recorded as discrete because classification was online; the feedback display is not described in the abstract.
10. Several phase durations are approximate typical ranges (marked in each phase note) because the first-source full texts were not read; only PER-MUSAT-001 timings come from the source.

## Datasets

- PER-MUSAT-002: MAD-EEG (Zenodo record 4537751), verified.
- PER-SURR-001: HBN-EEG Release 1 (OpenNeuro ds005505), identified through its NEMAR page and the HBN-EEG preprint; OpenNeuro page not rendered, so the task list per release is unchecked.
- No public dataset was found for Treder et al. 2014 or for the other classes.

## Bibliographic checks

Every cited DOI was retrieved from Crossref or OpenAlex (search_log.md). Crossref HTTP 429 for Müller 2006 (DOI then taken from a Crossref title search: 10.1073/pnas.0606668103, which differs from the DOI noted before the check), Hines & Brown 1936 and Langer 2017 (OpenAlex used); Crossref error for the HBN-EEG preprint (OpenAlex used). Records not retrieved and therefore not cited: Hashimoto 1987 (air-puff stimulator), Chen et al. 1989 (cold pressor EEG), Dove 1839, Hines & Brown 1932, pre-EEG hyperventilation work. All first_source.verified = false.
