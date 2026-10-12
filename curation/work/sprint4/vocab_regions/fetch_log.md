# fetch_log — vocab_regions (sprint 4)

| # | Tool | Target | Outcome |
|---|---|---|---|
| 1 | Bash curl | api.crossref.org/works/10.1016/j.neuroimage.2019.116189 and 10.1038/nature18933 | failed: proxy 403 (CONNECT rejected); retried via WebFetch |
| 2 | WebFetch | https://api.crossref.org/works/10.1016/j.neuroimage.2019.116189 | OK: "Automated anatomical labelling atlas 3", NeuroImage 2020;206:116189; Rolls, Huang, Lin, Feng, Joliot. DOI confirmed |
| 3 | WebFetch | https://api.crossref.org/works/10.1038/nature18933 | OK: "A multi-modal parcellation of human cerebral cortex", Nature 2016;536:171-178; Glasser, Coalson, Robinson, Hacker, Harwell... DOI confirmed |
| 4 | WebFetch | https://www.gin.cnrs.fr/en/tools/aal/ | OK but no label list; confirms AAL3 adds new ACC, thalamus, N_Acc, SN, VTA, Red_N, LC, raphe |
| 5 | WebSearch | "AAL3v1_1mm.nii.txt labels ACC_sub_L ACC_pre_L ACC_sup_L N_Acc_L Thal_AV_L" | OK: found cedalion docs page and AAL3 paper PDF at oxcns.org |
| 6 | WebFetch | https://doc.ibs.tu-berlin.de/cedalion/doc/dev/examples/head_models/52_mni_atlas_labels_aal3_brodmann.html | partial: 33 labels with _L/_R spelling (Frontal_Sup_2_L, Frontal_Mid_2_L, Thal_PuM_R, Red_N_R, Insula_R, ...) |
| 7 | WebFetch | https://www.oxcns.org/papers/607%20Rolls%20Huang%20Lin%20Feng%20Joliot%202020%20AAL3.pdf | OK: AAL3 Table 3 labels (ACC_sub/pre/sup, 15 Thal_* nuclei, OFCmed/ant/post/lat, N_Acc, VTA, SN_pc/pr, Red_N, LC, Raphe_D/M, Cerebellum_*, Vermis_*); Cingulate_Ant removed in AAL3; no STN label. Thal_Re spelled Thal_RE in Table 1 |
