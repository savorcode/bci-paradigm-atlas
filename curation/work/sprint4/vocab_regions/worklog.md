# worklog — vocab_regions (sprint 4)

- Read sprint4 README, vocab_ids.json (43 region IDs), vocabulary/common schemas, existing regions.yaml (5 atlas terms).
- Verified the two atlas DOIs via Crossref (WebFetch; curl blocked by proxy). Verified AAL3 label spelling from the AAL3 paper tables and a third-party label listing (fetch_log.md).
- Wrote knowledge/regions.yaml with `build_regions.py` (yaml.safe_dump, allow_unicode, sort_keys=False, width=120): 43 terms in vocab_ids.json order; existing 5 IDs kept with their `includes`; BR.temporoparietal_junction parent BR.parietal_cortex retained.
- Parents: visual_cortex <- V1, extrastriate, LOC, FFA, MT; sensorimotor_cortex <- M1, S1; frontal_cortex <- IFG, preSMA, SMA, DLPFC, vmPFC, premotor, FEF, dmPFC, frontopolar, OFC_lateral; parietal_cortex <- IPS, TPJ, temporoparietal_junction, precuneus, SII. Cingulate, temporal, insular and subcortical terms have no parent (no macro term exists).
- BR.TPJ and BR.temporoparietal_junction cross-referenced in notes; identical atlas_refs.
- sources: AAL3 (Rolls 2020) on 42 terms with aal3 labels; Glasser 2016 on 35 terms with hcp_mmp1 areas; verified: false. No source for Brodmann.
- Decisions: AAL3 has no Cingulate_Ant (uses ACC_sup for dACC, ACC_sub for vmPFC) and no single Thalamus label (15 Thal_* nuclei listed); no STN label (aal3 empty, low). Insula Brodmann omitted (13-16 not defined in human map). Macro frontal/parietal: HCP areas not enumerated.
- `python3 scripts/validate.py`: 0 problems.
