# Sprint 7 vocabulary work log

Vocabulary curator, 2026-10-17. Requests from the sprint 6 marker groups (`curation/work/sprint6/markers_{I,J,K}/vocab_requests.csv`), handled as approved in D-079. Details in `mapping.csv` and `remap.csv`.

## 1. New terms

Regions (`knowledge/regions.yaml`, 47 → 51), all MNI152, atlas notes start "Atlas correspondence approximate.":

- `BR.retrosplenial` (压后皮层), after BR.PCC. BA29/BA30, HCP-MMP RSC. AAL3 has no retrosplenial label, so aal3 and the AAL3 source are left out. No parent (no limbic or cingulate macro region). Localisation: Vann et al. 2009 (Crossref API).
- `BR.piriform_cortex` (梨状皮层（初级嗅皮层）), after BR.OFC_lateral. HCP-MMP Pir only: no human Brodmann number, and AAL3 Olfactory does not match piriform cortex. No parent (spans frontal and temporal lobes). Localisation: Seubert et al. 2013 (Crossref API).
- `BR.PIVC` (顶-岛前庭皮层（顶盖 OP2）), after BR.SII. AAL3 Rolandic_Oper (low confidence), HCP-MMP OP2-3 (shared with BR.SII). Parent is **BR.parietal_cortex, not BR.insula**: OP2 sits in the parietal operculum, and HCP-MMP groups OP2-3 with the posterior opercular areas. Localisation: zu Eulenburg et al. 2012 (Crossref API).
- `BR.auditory_brainstem` (听神经与下位听觉脑干（耳蜗核、上橄榄复合体）), after BR.inferior_colliculus. No atlas labels exist, so atlas_refs are omitted, and there is no parent (same treatment as BR.inferior_colliculus). Localisation: Sitek et al. 2019 (Crossref API; abstract via OpenAlex API).

Constructs (`knowledge/constructs.yaml`, 92 → 95):

- `CN.scene_perception` (场景知觉, parent CN.perception), after CN.face_perception.
- `CN.vestibular_perception` (前庭知觉, parent CN.perception), after CN.somatosensation.
- `CN.olfactory_imagery` (嗅觉意象, parent CN.mental_imagery), after CN.auditory_imagery.

The Cognitive Atlas API had no concept for any of the three, including the name variants listed in `mapping.csv`. `cognitive_atlas` is left out, and each term's notes say so.

## 2. Re-mapped links (4 markers)

- MK.BOLD_parahippocampal: generator BR.precuneus → BR.retrosplenial; index CN.object_recognition → CN.scene_perception.
- MK.BOLD_olfactory_cortex: generator BR.amygdala → BR.piriform_cortex; index CN.mental_imagery → CN.olfactory_imagery.
- MK.BOLD_vestibular_cortex: generator BR.posterior_insula → BR.PIVC; index CN.multisensory_integration → CN.vestibular_perception.
- MK.ABR: new generator BR.auditory_brainstem for waves I-III, with evidence B and the same intracranial sources as wave V. The BR.inferior_colliculus generator stays for wave V.

Evidence, relations and sources are unchanged. Placeholder notes that pointed to the vocabulary requests were removed.

## 3. Validation

`python3 scripts/validate.py`: 0 problems, 0 warnings (129 markers, 51 regions, 95 constructs).

## Open points

- BR.PIVC parent: D-079 suggested BR.insula. I chose BR.parietal_cortex (reason above). The lead may prefer BR.insula for roll-up from the old posterior-insula mapping.
- MK.BOLD_vestibular_cortex: the Bense 2001 relation also describes cross-modal decreases. The lead may want to keep a second index on CN.multisensory_integration.
- Not edited, but possible candidates for the new ids: MK.BOLD_category_selective (PPA scene selectivity on BR.parahippocampal, index may suit CN.scene_perception); MK.CPS (posterior cingulate / retrosplenial source mapped to BR.PCC); MK.FFR (note says cochlear nucleus has no region id; BR.auditory_brainstem now exists).
- The remaining D-079 requests (BR.MCC, BR.frontal_operculum, CN.interference_resolution, CN.effective_connectivity, CN.basal_ganglia_stimulation_response) were not added, as D-079 proposes.
- New sources are not checked against the full text (`verified: false`). For Seubert 2013 and zu Eulenburg 2012, the OpenAlex records have no abstract.
