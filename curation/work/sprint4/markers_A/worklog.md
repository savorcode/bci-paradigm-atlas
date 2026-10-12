# Sprint 4 markers_A worklog (curator_a, 2026-10-12)

Scope: MK.P3b, MK.N1_auditory, MK.P2_auditory, MK.P1_visual, MK.N1_visual, MK.N170, MK.MMN, MK.SSVEP, MK.CDA, MK.alpha_posterior.
Edited with Python (yaml.safe_load / safe_dump); `python3 scripts/validate.py` -> 0 problems, 0 warnings.

## Retrieval
- Bash curl to api.crossref.org / api.openalex.org / eutils is blocked (403) in this sandbox; all record checks were done with WebFetch.
- Every cited DOI's record was retrieved from Crossref or OpenAlex (record_api column in links.csv). Title, authors, journal, volume(issue):pages copied from the record.
- Four DOIs I recalled turned out to belong to other papers (10.1002/hbm.22339, 10.1002/hbm.20947, 10.1002/hbm.20265, 10.1016/j.heares.2008.12.006); none were cited. The correct Kim 2014 DOI (10.1002/hbm.22326) was found via a Crossref query.
- Dropped because record not retrievable (429 / fetch errors): Halgren 1980 Science (P3b hippocampus), Bledowski 2004 J Neurosci (P3b EEG-fMRI), Heinze 1994 Nature (P1 PET-ERP), Di Russo 2007 HBM (SSVEP sources), Sadeh 2010 (N170 EEG-fMRI), Doeller 2003 (MMN IFG), Robitaille 2010 (CDA sources), Ross & Tremblay 2009 (P2).

## Year conventions
- Where online-first and print years differ, the print (volume) year is used: Kim 2014 (Crossref issued 2013), Jacques 2019 (issued 2018), Di Russo 2002 (OpenAlex 2001), Klimesch 2007 (OpenAlex 2006).
- OpenAlex lists only the first author for Allison 1999 and Jensen 2002; cited as "Allison T, et al." / "Jensen O, et al." rather than adding unretrieved co-authors. A maintainer should complete these from the full text.

## Decisions
- MK.P3b: existing BR.temporoparietal_junction replaced by the factory id BR.TPJ (same region per README). Added BR.IPS. Kept context_updating and attention_allocation (B) and upgraded their sources. Evidence accumulation graded C because O'Connell 2012 and Twomey 2015 come from the same group.
- MK.SSVEP: the existing generator BR.visual_cortex was cited only to Regan 1966, which does not localize the response. Replaced by BR.V1 + BR.extrastriate (Norcia 2015 review). Regan 1966 moved to CN.neural_entrainment. Kept the existing CN.sustained_visual_attention index (Morgan 1996) and added Norcia 2015.
- MK.N170: CN.face_perception graded A on cross-lab, cross-modality replication (scalp, MEG, intracranial). CN.emotional_salience graded A on a meta-analysis (Hinojosa 2015). IOG source mapped to BR.LOC (BR.OFA requested).
- MK.MMN: STG and IFG kept at B (narrative reviews plus primary work). An upgrade to A on cross-modality replication is defensible but left for review.
- MK.P2_auditory: the generator rests mainly on the Crowley & Colrain 2004 review (B). The training effect is mapped to CN.phonological_processing (C); CN.perceptual_learning requested.
- MK.CDA: no CDA meta-analysis found (WebSearch), so working memory is graded B. The only retrievable localization is the MEG study by Mitchell & Cusack 2011, giving IPS at C.
- MK.alpha_posterior: visual cortex B (intracranial Halgren 2019 + EEG-fMRI Goldman 2002); thalamus C (Goldman only, and thalamic role contested by Halgren 2019).
- Stale "No generators/indexes yet" phrases removed from notes; a Sprint 4 note was appended. No other fields changed.

## Uncertainties for review
- Twomey 2015 pages 1636-1643 with issue 1 as given by Crossref.
- No auditory selective-attention construct exists; N1 attention is mapped to CN.spatial_attention (vocab request filed).
