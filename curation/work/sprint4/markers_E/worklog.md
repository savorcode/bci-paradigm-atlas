# Sprint 4 markers_E worklog (curator_e, 2026-10-12)

Markers: MK.BOLD_hippocampus, _frontoparietal, _category_selective, _language_network, _dlPFC, _motor_network, _frontopolar, _visual_cortex, _oculomotor, _auditory_cortex. None had generators/indexes before; added fresh. Edited with yaml.safe_load/safe_dump; only generators, indexes and a notes sentence changed (safe_dump reformatted the flow-style YAML of motor_network and oculomotor; content unchanged).

## Decisions
- Hemodynamic markers: generator = the measured region; method `fMRI localization`; graded A when an ALE/coordinate meta-analysis (or broad cross-lab replication, e.g. retinotopic mapping; FFA with fMRI + intracranial stimulation) supports it.
- Frontoparietal: two generators (DLPFC, IPS); FEF component left to MK.BOLD_oculomotor.
- Category-selective: FFA (A), parahippocampal/PPA (B), LOC (B). EBA has no region id; mentioned under LOC note.
- Language network: IFG, MTG (A), ATL (B, susceptibility dropout makes it less consistent).
- Motor network: M1, SMA, cerebellum (premotor omitted to stay at 3; covered by Hetu 2013 for imagery). Command-following in DoC indexed as CN.consciousness_level B (Owen 2006/Monti 2010 overlap in authors; Kondziella 2016 meta-analysis pools across modalities).
- Visual cortex: imagery graded B because Winlove 2018 meta-analysis found early visual activation inconsistent.
- Oculomotor: antisaccade > prosaccade mapped to CN.response_inhibition (B, interpretive).
- Auditory cortex: generators graded B (independent tonotopy studies, no meta-analysis cited). Voice selectivity mapped to CN.social_perception (C) with vocab request CN.voice_perception.

## Uncertainties / citation notes
- Year convention: print-issue year used where Crossref/OpenAlex issued year is the online year: Hardwick 2013 (record 2012), Kondziella 2016 (record 2015), Molholm 2005 (record 2004).
- Halpern 1999 Cereb Cortex 9(7):697-704: both Crossref and OpenAlex list only "Halpern AR"; the published article is by Halpern AR and Zatorre RJ, cited with both authors. Maintainer should confirm against the full text.
- Wager & Smith 2003: Crossref title truncated at the colon; subtitle "a meta-analysis" added.
- Binder 2009: Crossref container-title empty; journal (Cereb Cortex) taken from DOI prefix and print record.
- Not cited (record not retrieved or DOI mismatch): Brefczynski & DeYoe 1999, Polonsky et al. 2000.
- curl to Crossref/OpenAlex blocked by proxy (403); HTTP request rate limits (429) handled by waiting.
