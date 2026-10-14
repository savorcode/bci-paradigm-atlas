# Worklog — curator_b, sprint 4 (2026-10-12)

## Scope
MK.SMR_ERD, MK.high_gamma, MK.low_freq_kinematics, MK.motor_cortical_spiking, MK.LRP, MK.MRCP, MK.CNV, MK.sleep_spindle, MK.slow_wave, MK.DMN_connectivity. Edited with yaml.safe_load/safe_dump (this re-serialised flow-style mappings to block style and removed YAML anchors in MK.SMR_ERD; content of other fields unchanged). A `notes` sentence was appended to each marker.

## Record retrieval
- Direct curl to Crossref/OpenAlex/PubMed is blocked by the egress proxy; HTTP request to Crossref mostly returned 429, so OpenAlex records were the primary check (Crossref used for Crone 1998 I/II and Boveroux 2010). Citation fields were copied from the record. Year = issue year where OpenAlex reported the online-first year (Ritter 2009, Fox 2016, Collinger 2013, Greicius 2003, Spreng 2009, Vanhaudenhuyse 2010, Fernandez 2020, Bareš 2007).
- Five DOIs recalled from memory resolved to the WRONG paper (Mukamel 2005, Ray & Maunsell 2011, Brunia & van Boxtel 2001, Nagai 2004 first guess, Rohrbaugh 1976) and three did not resolve (Churchland 2006, Kopp 1996, Praamstra 1999). None of these are cited. This is exactly why every DOI needs a retrieved record.
- Crone et al. 1998 (Brain 121:2271 and 121:2301): both Crossref and OpenAlex list only the first author, so citations read "Crone NE, et al."; maintainer should complete the author list from the PDF.
- Bradberry 2010: OpenAlex lists 4 authorships (I recall 3); cited as "et al." per record — check.
- Cunnington 2003 and Leuthold & Jentzsch 2002 subtitles: OpenAlex title truncated/lacks subtitle; subtitle from publisher/repository page.
- Nagai 2004 and Nir 2011 and Kumral 2023 records have no abstract; region claims for Nagai rely on indexed keywords plus prior knowledge (thalamus, ACC, SMA) — check against full text. Kumral 2023 direction of effect ("positive association") is inferred from the title and must be checked.

## Grading decisions
- SMR_ERD: kept BR.sensorimotor_cortex at A but now backed by ECoG + MEG + EEG-fMRI (cross-lab, cross-modality) rather than the Pfurtscheller review alone. Added BR.M1 (beta) and BR.S1 (mu) at B. CN.motor_imagery upgraded B→A (EEG Graz + ECoG Miller 2010). New CN.social_perception (A, Fox 2016 meta-analysis on action-observation mu suppression) and CN.cortical_idling (B, reviews from one group).
- high_gamma: generators are task-dependent; recorded the two best-documented sites (sensorimotor, STG). No meta-analysis → B max.
- low_freq_kinematics: source localisation evidence is thin (C). Kinematics index B; artefact confounds debated (Antelis 2013 not retrievable, not cited).
- motor_cortical_spiking: BR.M1 and CN.movement_kinematics at A (intracortical, cross-lab, monkey + human). CN.intent_selection added (B) because the marker is the HMI intent signal in iBCI.
- LRP: only one source-localisation study retrieved (C). Coles/Gratton share a lab; Leuthold adds independent support → B for motor_preparation.
- MRCP: SMA and M1 at B (intracranial Ikeda 1992 + fMRI + review). Kept motor_preparation at B (could be argued A by cross-modal replication). CN.intent_selection with Libet/Schurger caveat.
- CNV: SMA and dACC B (SEEG + EEG-fMRI), thalamus C.
- sleep_spindle: thalamus A (animal intracellular + human EEG-fMRI + major review); memory_consolidation A (meta-analysis).
- slow_wave: frontal B (HD-EEG + source modelling), PCC B (source + EEG-fMRI). Consciousness_level C (single propofol study).
- DMN_connectivity: hemodynamic marker → generator = measured region; PCC, vmPFC, precuneus A via Laird 2009 coordinate meta-analysis. Angular gyrus/lateral parietal not added (no README id short of BR.parietal_cortex/BR.TPJ); no vocab request filed.

## Vocabulary
All needed IDs were in the README list; vocab_requests.csv contains only the header.

## Validation
`python3 scripts/validate.py`: 0 problems, 0 warnings.
