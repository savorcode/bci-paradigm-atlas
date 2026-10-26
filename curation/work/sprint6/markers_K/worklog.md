# Sprint 6 markers_K worklog (curator K)

Date: 2026-10-16. Markers: MK.ERNA, MK.FPAS_oddball, MK.FPVS_oddball, MK.FRP, MK.GEP, MK.LEP, MK.MLR, MK.N140_somatosensory. Only `generators`, `indexes` and a `notes` line were added; other fields untouched.

## Summary

| marker | generators | indexes |
|---|---|---|
| MK.ERNA | 1 (STN B) | 2 (B, C) |
| MK.FPAS_oddball | 1 (STG C) | 2 (C, C) |
| MK.FPVS_oddball | 2 (FFA B, OFA B) | 3 (B, B, C) |
| MK.FRP | 1 (visual_cortex C) | 4 (B, B, B, C) |
| MK.GEP | 1 (insula B) | 1 (B) |
| MK.LEP | 3 (SII A, posterior_insula B, dACC B) | 2 (A, B) |
| MK.MLR | 2 (A1 A, thalamus C) | 3 (B, B, C) |
| MK.N140_somatosensory | 2 (SII B, frontal_cortex C) | 2 (B, B) |

Totals: 13 generators, 19 indexes; grades A 3, B 19, C 10 (per link). 39 distinct sources, all DOIs retrieved from the Crossref API or the OpenAlex API (see search_log.md, links.csv).

## Decisions

- A grades: LEP→BR.SII (intracranial Frot 2003/2008 plus multi-laboratory dipole/MEG work reviewed by García-Larrea 2003); MLR→BR.A1 (intracranial, MEG/EEG source and lesion evidence from independent laboratories); LEP→CN.somatosensation (EFNS guideline built on a systematic, evidence-graded review). All other links B or C.
- ERNA: generator is the recording site (STN contacts of the DBS lead); evidence from two independent groups (Melbourne, Oxford) → B. Construct mapping is imperfect: ERNA reflects basal ganglia responsiveness to stimulation, mapped to CN.cortical_excitability with a vocab request. The motor link (largest ERNA at clinically effective contacts) is graded C because it rests on one group and a perspective article.
- FPAS oddball: only voice-categorisation studies (one group, adults and infants) were found; graded C throughout. Source localisation is a beamformer without individual MRI.
- FPVS oddball: generators FFA and OFA from intracerebral recordings (Jonas 2016) and fMRI FPS (Gao 2018); same group, cross-modal → B. Peykarjou 2022 (systematic review of infant visual oddball frequency tagging) supports the discrimination index.
- FRP: no intracranial or source-imaging evidence retrieved for the lambda response; generator graded C from scalp topography and P100 comparison (Kazai and Yagi 2003). Target-fixation P3-like FRP from two independent labs (Brouwer 2013, Kaunitz 2013) → B.
- GEP: generator BR.insula from MEG dipoles (two Japanese studies, partly overlapping authors) plus the taste ALE meta-analysis as indirect support → B.
- LEP P2/N2 vertex: midcingulate cortex mapped to BR.dACC (vocab request BR.MCC). Saliency index (CN.orienting) uses two papers from the same group → B because of consistent multi-experiment findings.
- MLR thalamus link is indirect (lesion sparing and sleep dissociation) → C.
- N140: intracranial evidence implicates SII (Allison 1992, Frot 1999); frontal contribution from Allison 1992 only → C.

## Uncertainties and record issues

- Crossref/OpenAlex records for Frot 2003 (Brain), Frot 1999 (Cereb Cortex), Yvert 2001 (Cereb Cortex) and Mizoguchi 2002 (Chem Senses) list only the first author; citations copy the record. Full author lists to be completed at full-text check.
- Jonas 2016 PNAS: Crossref record has no page range; citation gives volume and issue only.
- Record years follow the API record where they differ from print year: Liu-Shuang 2013 (Neuropsychologia vol. 52), Calce 2023 (Curr Biol vol. 34), Hummel 2009 (JNNP vol. 81).
- García-Larrea 1995 title spelled "trasition" in the record; kept as recorded.
- Dropped because the record could not be retrieved (429 or fetch error): Kobayakawa 1999 Chem Senses; Kamienkowski 2012 J Vis; Iannetti 2005 Neuroscience. A guessed DOI for Sinclair 2018 resolved to a different paper and was discarded; the correct DOI came from a Crossref API search.
- Barbero 2021 metadata confirmed from the OpenAlex API search record (Crossref look-ups for this DOI were rate limited).

## Validation

`python3 scripts/validate.py`: no problems in the eight marker files; the remaining reported problems concern paradigm classes curated by other groups.
