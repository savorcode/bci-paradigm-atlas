"""Build knowledge/regions.yaml (sprint 4, vocabulary curator: regions). Run from repo root."""
import csv, json
import yaml

IDS = json.load(open("curation/work/sprint4/vocab_ids.json"))["regions"]

AAL3 = {"citation": "Rolls ET, Huang CC, Lin CP, Feng J, Joliot M. Automated anatomical labelling atlas 3. "
                    "NeuroImage. 2020;206:116189.",
        "doi": "10.1016/j.neuroimage.2019.116189", "year": 2020, "verified": False}
HCP = {"citation": "Glasser MF, Coalson TS, Robinson EC, et al. A multi-modal parcellation of human cerebral cortex. "
                   "Nature. 2016;536(7615):171-178.",
       "doi": "10.1038/nature18933", "year": 2016, "verified": False}


def LR(*names):
    return [f"{n}_{h}" for n in names for h in ("L", "R")]


THAL = ["Thal_AV", "Thal_LP", "Thal_VA", "Thal_VL", "Thal_VPL", "Thal_IL", "Thal_Re", "Thal_MDm", "Thal_MDl",
        "Thal_LGN", "Thal_MGN", "Thal_PuI", "Thal_PuM", "Thal_PuA", "Thal_PuL"]
CEREB = ["Cerebellum_Crus1", "Cerebellum_Crus2", "Cerebellum_3", "Cerebellum_4_5", "Cerebellum_6", "Cerebellum_7b",
         "Cerebellum_8", "Cerebellum_9", "Cerebellum_10"]
VERMIS = ["Vermis_1_2", "Vermis_3", "Vermis_4_5", "Vermis_6", "Vermis_7", "Vermis_8", "Vermis_9", "Vermis_10"]

# id: (definition, parent, brodmann, aal3, hcp, confidence, note, extra)
R = {
 "BR.V1": ("Primary visual cortex in the calcarine sulcus of the occipital lobe, the first cortical stage of visual processing.",
           "BR.visual_cortex", ["BA17"], LR("Calcarine"), ["V1"], "high", "AAL3 Calcarine also contains some V2 at the sulcal banks"),
 "BR.extrastriate": ("Occipital visual areas V2 to V4 surrounding V1 that carry early and intermediate visual processing.",
           "BR.visual_cortex", ["BA18", "BA19"], LR("Cuneus", "Lingual", "Occipital_Sup", "Occipital_Mid", "Occipital_Inf"),
           ["V2", "V3", "V4"], "medium", "AAL3 gyral labels only approximate retinotopic V2-V4 boundaries"),
 "BR.LOC": ("Lateral occipital and posterior ventral occipitotemporal cortex that responds preferentially to object shape.",
           "BR.visual_cortex", ["BA19", "BA37"], LR("Occipital_Mid", "Occipital_Inf", "Temporal_Inf"), ["LO1", "LO2", "LO3", "PIT"],
           "medium", "functionally defined region; atlas labels are approximate; Temporal_Inf only its posterior part"),
 "BR.FFA": ("Face-selective region of the mid-lateral fusiform gyrus, typically larger in the right hemisphere.",
           "BR.visual_cortex", ["BA37"], LR("Fusiform"), ["FFC"], "medium",
           "functionally defined; HCP-MMP FFC is the 'fusiform face complex'; right-lateralised"),
 "BR.pSTS": ("Posterior part of the superior temporal sulcus, involved in biological motion, gaze and audiovisual integration.",
           None, ["BA21", "BA22", "BA39"], LR("Temporal_Sup", "Temporal_Mid"), ["STSdp", "STSvp", "TPOJ1"], "medium",
           "AAL3 has no sulcal label; posterior parts of Temporal_Sup/Temporal_Mid"),
 "BR.A1": ("Primary auditory cortex on Heschl's gyrus in the superior temporal plane.",
           None, ["BA41", "BA42"], LR("Heschl"), ["A1", "LBelt", "MBelt", "PBelt"], "high",
           "A1 core = HCP A1/BA41; belt areas (BA42) included for Heschl gyrus as a whole"),
 "BR.STG": ("Superior temporal gyrus of the lateral temporal lobe, including auditory association cortex for speech and sound processing.",
           None, ["BA22", "BA41", "BA42"], LR("Temporal_Sup"), ["A4", "A5", "STGa", "TA2", "STV"], "medium",
           "Heschl gyrus listed separately under BR.A1"),
 "BR.MTG": ("Posterior part of the left middle temporal gyrus, implicated in lexical-semantic access.",
           None, ["BA21", "BA37"], ["Temporal_Mid_L"], ["PHT", "TE1p", "TE1m"], "medium",
           "left hemisphere only per term definition; posterior portion of AAL3 Temporal_Mid_L"),
 "BR.ATL": ("Anterior temporal lobe including the temporal pole, implicated in semantic memory and social knowledge.",
           None, ["BA38", "BA20", "BA21"], LR("Temporal_Pole_Sup", "Temporal_Pole_Mid"),
           ["TGd", "TGv", "TE1a", "TE2a", "STGa", "STSda", "STSva"], "medium",
           "anterior Temporal_Inf / Temporal_Mid also part of ATL in many studies"),
 "BR.IFG": ("Inferior frontal gyrus (pars opercularis, triangularis and orbitalis) of the lateral frontal lobe, involved in language and inhibitory control.",
           "BR.frontal_cortex", ["BA44", "BA45", "BA47"], LR("Frontal_Inf_Oper", "Frontal_Inf_Tri", "Frontal_Inf_Orb_2"),
           ["44", "45", "47l"], "high", ""),
 "BR.IPS": ("Intraparietal sulcus separating the superior and inferior parietal lobules, involved in spatial attention and numerical processing.",
           "BR.parietal_cortex", ["BA7", "BA39", "BA40"], LR("Parietal_Sup", "Parietal_Inf"),
           ["IP0", "IP1", "IP2", "IPS1", "AIP", "MIP", "LIPv", "LIPd", "VIP"], "medium",
           "sulcal region on boundary of two AAL3 gyral labels"),
 "BR.TPJ": ("Cortex where the posterior superior temporal and inferior parietal lobes meet, involved in attentional reorienting and mentalizing.",
           "BR.parietal_cortex", ["BA39", "BA40", "BA22"], LR("SupraMarginal", "Angular", "Temporal_Sup"),
           ["PGi", "PGs", "PFm", "TPOJ1", "TPOJ2", "TPOJ3", "STV", "PSL"], "medium",
           "same region as the atlas id BR.temporoparietal_junction; Temporal_Sup only its posterior part"),
 "BR.dACC": ("Dorsal (supracallosal) anterior cingulate cortex on the medial frontal wall, involved in performance monitoring.",
           None, ["BA24", "BA32"], LR("ACC_sup"), ["a24pr", "p24pr", "a32pr", "p32pr", "33pr"], "medium",
           "AAL3 replaces Cingulate_Ant with ACC_sub/ACC_pre/ACC_sup; anterior Cingulate_Mid often included in dACC/aMCC"),
 "BR.preSMA": ("Medial frontal area rostral to the SMA (anterior to the vertical line through the anterior commissure), involved in action selection and inhibition.",
           "BR.frontal_cortex", ["BA6"], LR("Supp_Motor_Area"), ["6ma"], "medium",
           "AAL3 Supp_Motor_Area covers both SMA and pre-SMA (anterior part)"),
 "BR.SMA": ("Supplementary motor area on the medial surface of BA6, involved in self-initiated movement and movement sequencing.",
           "BR.frontal_cortex", ["BA6"], LR("Supp_Motor_Area"), ["6mp"], "high",
           "AAL3 Supp_Motor_Area posterior part"),
 "BR.M1": ("Primary motor cortex in the precentral gyrus, the main cortical origin of descending motor commands.",
           "BR.sensorimotor_cortex", ["BA4"], LR("Precentral"), ["4"], "medium",
           "AAL3 Precentral also contains lateral premotor cortex (BA6)"),
 "BR.S1": ("Primary somatosensory cortex in the postcentral gyrus, receiving tactile and proprioceptive input.",
           "BR.sensorimotor_cortex", ["BA3", "BA1", "BA2"], LR("Postcentral"), ["3a", "3b", "1", "2"], "high", ""),
 "BR.DLPFC": ("Dorsolateral prefrontal cortex on the middle and superior frontal gyri, involved in working memory and cognitive control.",
           "BR.frontal_cortex", ["BA9", "BA46"], LR("Frontal_Mid_2", "Frontal_Sup_2"),
           ["46", "9-46d", "a9-46v", "p9-46v"], "medium", "functionally broad; AAL3 gyral labels extend beyond DLPFC"),
 "BR.vmPFC": ("Ventromedial prefrontal and medial orbitofrontal cortex, involved in value representation and emotion regulation.",
           "BR.frontal_cortex", ["BA10", "BA11", "BA25", "BA32"], LR("Frontal_Med_Orb", "Rectus", "OFCmed", "ACC_sub"),
           ["10r", "10v", "25", "s32", "p32", "a24", "OFC", "pOFC"], "medium",
           "definitions of vmPFC vary; ventral parts of pregenual ACC (ACC_pre) sometimes included"),
 "BR.striatum": ("Ventral striatum centred on the nucleus accumbens, involved in reward processing and reward prediction error.",
           None, [], LR("N_Acc"), [], "high", "subcortical; no Brodmann or HCP-MMP cortical area; ventral caudate/putamen sometimes included"),
 "BR.amygdala": ("Medial temporal nuclear complex anterior to the hippocampus, involved in threat detection and emotional salience.",
           None, [], LR("Amygdala"), [], "high", "subcortical; no Brodmann or HCP-MMP cortical area"),
 "BR.thalamus": ("Paired diencephalic nuclear complex relaying and gating sensory, motor and cortico-cortical signals.",
           None, [], LR(*THAL), [], "high",
           "AAL3 splits the thalamus into 15 nuclei per hemisphere; Thal_Re spelled Thal_RE in one table of the AAL3 paper (medium on that label)"),
 "BR.hippocampus": ("Medial temporal lobe structure (hippocampal formation) involved in episodic memory and spatial navigation.",
           None, [], LR("Hippocampus"), ["H"], "high",
           "HCP-MMP1.0 includes hippocampus as area H; no Brodmann area assigned"),
 "BR.frontal_cortex": ("Frontal lobe cortex anterior to the central sulcus, including motor, premotor and prefrontal areas.",
           None, ["BA4", "BA6", "BA8", "BA9", "BA10", "BA11", "BA44", "BA45", "BA46", "BA47"],
           LR("Precentral", "Frontal_Sup_2", "Frontal_Mid_2", "Frontal_Inf_Oper", "Frontal_Inf_Tri", "Frontal_Inf_Orb_2",
              "Supp_Motor_Area", "Frontal_Sup_Medial", "Frontal_Med_Orb", "Rectus", "OFCmed", "OFCant", "OFCpost", "OFClat"),
           [], "medium", "macro region; HCP-MMP areas not enumerated (see child terms); cingulate excluded"),
 "BR.parietal_cortex": ("Parietal lobe cortex between the central and parieto-occipital sulci, including somatosensory and posterior parietal areas.",
           None, ["BA1", "BA2", "BA3", "BA5", "BA7", "BA39", "BA40"],
           LR("Postcentral", "Parietal_Sup", "Parietal_Inf", "SupraMarginal", "Angular", "Precuneus"),
           [], "medium", "macro region; HCP-MMP areas not enumerated (see child terms)"),
 "BR.temporoparietal_junction": ("Cortex where the posterior superior temporal and inferior parietal lobes meet (supramarginal/angular gyri and posterior STG).",
           "BR.parietal_cortex", ["BA39", "BA40", "BA22"], LR("SupraMarginal", "Angular", "Temporal_Sup"),
           ["PGi", "PGs", "PFm", "TPOJ1", "TPOJ2", "TPOJ3", "STV", "PSL"], "medium",
           "same region as the factory id BR.TPJ; both ids kept"),
 "BR.sensorimotor_cortex": ("Pericentral cortex comprising primary motor and primary somatosensory cortex, the main generator of mu and beta rhythms.",
           None, ["BA4", "BA3", "BA1", "BA2"], LR("Precentral", "Postcentral", "Paracentral_Lobule"),
           ["4", "3a", "3b", "1", "2"], "high", ""),
 "BR.visual_cortex": ("Occipital and adjacent occipitotemporal cortex devoted to visual processing, including V1 and extrastriate areas.",
           None, ["BA17", "BA18", "BA19"], LR("Calcarine", "Cuneus", "Lingual", "Occipital_Sup", "Occipital_Mid", "Occipital_Inf"),
           ["V1", "V2", "V3", "V4", "V3A", "V3B", "V3CD", "V6", "V6A", "V7", "V8", "LO1", "LO2", "LO3", "PIT",
            "FFC", "VVC", "VMV1", "VMV2", "VMV3", "MT", "MST", "V4t", "FST"], "medium",
           "macro region; HCP-MMP early, dorsal, ventral and MT+ visual areas listed"),
 "BR.premotor": ("Lateral premotor cortex (dorsal and ventral) anterior to M1 in BA6, involved in movement planning and sensorimotor transformation.",
           "BR.frontal_cortex", ["BA6"], LR("Precentral", "Frontal_Sup_2", "Frontal_Mid_2"),
           ["6d", "6a", "6v", "6r", "55b", "PEF"], "medium",
           "AAL3 has no premotor label; anterior Precentral and posterior Frontal_Sup_2/Frontal_Mid_2 (low for AAL3)"),
 "BR.FEF": ("Frontal eye field near the junction of the superior frontal and precentral sulci, controlling saccades and spatial attention.",
           "BR.frontal_cortex", ["BA8", "BA6"], LR("Precentral", "Frontal_Mid_2"), ["FEF"], "medium",
           "human FEF lies in BA6 at the precentral sulcus rather than classical BA8; AAL3 labels low confidence"),
 "BR.precuneus": ("Medial posterior parietal cortex, part of the default mode network, involved in self-referential processing and mental imagery.",
           "BR.parietal_cortex", ["BA7", "BA31"], LR("Precuneus"), ["7m", "7Pm", "7Am", "PCV"], "high", ""),
 "BR.PCC": ("Posterior cingulate cortex on the medial parietal wall, a core default mode network hub.",
           None, ["BA23", "BA31"], LR("Cingulate_Post"), ["d23ab", "v23ab", "23d", "31pd", "31pv", "31a"], "medium",
           "AAL3 Cingulate_Post is smaller than most functional PCC definitions; posterior Cingulate_Mid often included"),
 "BR.dmPFC": ("Dorsomedial prefrontal cortex on the medial superior frontal gyrus, involved in mentalizing and self-referential judgment.",
           "BR.frontal_cortex", ["BA8", "BA9", "BA32"], LR("Frontal_Sup_Medial"), ["8BM", "9m", "d32"], "medium", ""),
 "BR.frontopolar": ("Most anterior prefrontal cortex (BA10), involved in prospective memory, metacognition and exploration.",
           "BR.frontal_cortex", ["BA10"], LR("Frontal_Sup_2", "Frontal_Mid_2", "Frontal_Sup_Medial"),
           ["10pp", "a10p", "p10p", "10d"], "medium",
           "AAL3 has no frontopolar label; anterior parts of the listed labels (low for AAL3)"),
 "BR.anterior_insula": ("Anterior part of the insular cortex, involved in interoceptive awareness, salience detection and emotion.",
           None, [], LR("Insula"), ["AAIC", "AVI"], "medium",
           "AAL3 Insula not split; Brodmann insular areas (13-16) not defined in human Brodmann map, omitted"),
 "BR.posterior_insula": ("Posterior part of the insular cortex, receiving primary interoceptive, thermal and pain input.",
           None, [], LR("Insula"), ["PoI1", "PoI2", "Ig"], "medium",
           "AAL3 Insula not split; Brodmann omitted as for anterior insula"),
 "BR.parahippocampal": ("Parahippocampal gyrus of the medial temporal lobe, including the parahippocampal place area responsive to scenes.",
           None, ["BA35", "BA36"], LR("ParaHippocampal"), ["PHA1", "PHA2", "PHA3"], "medium",
           "PPA mapped to HCP PHA1-3; perirhinal/entorhinal (PeEc, EC) not included"),
 "BR.cerebellum": ("Hindbrain structure posterior to the brainstem involved in motor coordination, timing and some cognitive functions.",
           None, [], LR(*CEREB) + VERMIS, [], "high", "no Brodmann or HCP-MMP cortical areas; Vermis labels are midline"),
 "BR.STN": ("Small lens-shaped nucleus of the basal ganglia below the thalamus, involved in stopping and conflict-related braking.",
           None, [], [], [], "low", "no AAL3 label (AAL3 adds N_Acc, VTA, SN, Red_N, LC, raphe but not STN); use a dedicated subcortical atlas"),
 "BR.dorsal_striatum": ("Dorsal part of the striatum comprising caudate nucleus and putamen, involved in action selection and habit learning.",
           None, [], LR("Caudate", "Putamen"), [], "high", "subcortical; no Brodmann or HCP-MMP cortical area"),
 "BR.MT": ("Motion-sensitive visual area complex (hMT+/V5) at the occipitotemporal junction.",
           "BR.visual_cortex", ["BA19", "BA37"], LR("Occipital_Mid", "Temporal_Mid", "Occipital_Inf"), ["MT", "MST", "FST", "V4t"],
           "medium", "HCP-MMP MT/MST/FST/V4t form the hMT+ complex (high); AAL3 labels approximate (low)"),
 "BR.SII": ("Secondary somatosensory cortex in the parietal operculum, involved in tactile and pain processing.",
           "BR.parietal_cortex", ["BA40", "BA43"], LR("Rolandic_Oper", "SupraMarginal"), ["OP1", "OP4", "OP2-3"], "medium",
           "SII mainly OP1/OP4; Rolandic_Oper also contains non-SII cortex"),
 "BR.OFC_lateral": ("Lateral orbitofrontal cortex on the orbital surface of the frontal lobe, involved in reward valuation and reversal learning.",
           "BR.frontal_cortex", ["BA47", "BA11"], LR("OFClat", "Frontal_Inf_Orb_2"), ["47m", "11l", "13l", "47s"], "medium",
           "BA47/12 lateral orbital; Frontal_Inf_Orb_2 also contains part of ventral IFG"),
}

old = {t["id"]: t for t in yaml.safe_load(open("knowledge/regions.yaml"))["terms"]}
terms, rows = [], []
for rid, en, zh in IDS:
    d, parent, ba, aal, hcp, conf, note, *_ = R[rid]
    t = {"id": rid, "en": en, "zh": zh, "definition": d}
    if rid in old and "includes" in old[rid]:
        t["includes"] = old[rid]["includes"]
    if parent:
        t["parent"] = parent
    refs = {}
    if ba: refs["brodmann"] = ba
    if aal: refs["aal3"] = aal
    if hcp: refs["hcp_mmp1"] = hcp
    if refs: t["atlas_refs"] = refs
    t["coordinate_space"] = "MNI152"
    src = ([AAL3] if aal else []) + ([HCP] if hcp else [])
    if src: t["sources"] = [dict(s) for s in src]
    if note: t["notes"] = "Atlas correspondence approximate. " + note[0].upper() + note[1:] + "."
    else: t["notes"] = "Atlas correspondence approximate."
    terms.append(t)
    rows.append([rid, ";".join(ba), ";".join(aal), ";".join(hcp), parent or "", conf, note])

assert len(terms) == 43 and set(R) == {i[0] for i in IDS}
for t in terms:
    assert t.get("parent") is None or t["parent"] in R
header = ("# Brain regions / 脑区 (knowledge layer, sprint 4). atlas_refs give approximate correspondences to Brodmann,\n"
          "# AAL3 (Rolls et al. 2020) and HCP-MMP1.0 (Glasser et al. 2016) labels in MNI152 space.\n"
          "# 图谱对应关系为近似，粒度与置信度见 curation/work/sprint4/vocab_regions/mapping.csv。\n")
body = yaml.safe_dump({"schema_version": "0.2", "prefix": "BR", "terms": terms}, allow_unicode=True, sort_keys=False, width=120)
open("knowledge/regions.yaml", "w").write(header + body)
with open("curation/work/sprint4/vocab_regions/mapping.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["id", "brodmann", "aal3", "hcp_mmp1", "parent", "confidence", "note"]); w.writerows(rows)
print(len(terms), "terms")
