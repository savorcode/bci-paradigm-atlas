# 检索记录 · 包 B 运动、想象与刺激 · sprint 2

> 每次检索追加一行，维护者汇总进 `curation/search_protocol.md`（S-003 起）。不使用的检索也要记（命中 0 也记）。

| 编号 | 日期 | 数据库 | 检索式 / URL | 命中数 | 新增文献数 | 相关范式 | 执行人 | 用途 |
|---|---|---|---|---|---|---|---|---|
| WF-B2-01 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/dataset_summary.html | 1 页（MI 表截断至 Dreyer2023C） | — | — | curator_b | MOT-MI-006/-007/-008, MOT-TRACK-001; dataset list (BNCI2003_004, BNCI2014_002, Beetl2021_B, Cho2017, BNCI2020_002) |
| WF-B2-02 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/dataset_summary.html (second prompt: rest of MI table) | 1 页（后半部分不可见） | — | — | curator_b | class names of BNCI2014_001, BNCI2015_004, Beetl2021_A/B, Chang2025 |
| WF-B2-03 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.Ofner2017.html | 1 页 | 1 | MOT-MI-003, MOT-ME-005 | curator_b | Ofner et al. 2017 PLoS ONE doi 10.1371/journal.pone.0182578 => MOT-MI-003, MOT-ME-005 |
| WF-B2-04 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.PhysionetMI.html | 1 页 | 1 | MOT-MI-010; MOT-MI-001, MOT-ME-001 datasets | curator_b | Schalk et al. 2004 BCI2000 doi 10.1109/TBME.2004.827072 => MOT-MI-010; MOT-MI-001, MOT-ME-001 datasets |
| WF-B2-05 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.BNCI2014_004.html | 1 页 | 1 | MOT-MI-005, MOT-MI-001 datasets | curator_b | Leeb et al. 2007 doi 10.1109/TNSRE.2007.906956 (title not shown) => MOT-MI-005, MOT-MI-001 datasets |
| WF-B2-06 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.BNCI2014_001.html | 1 页 | 0 | MOT-MI-002 dataset timing | curator_b | Tangermann et al. 2012 (competition review) => MOT-MI-002 dataset timing |
| WF-B2-07 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.BNCI2015_001.html | 1 页 | 1 | MOT-MI-007 | curator_b | Faller et al. 2012 IEEE TNSRE doi 10.1109/tnsre.2012.2189584 => MOT-MI-007 |
| WF-B2-08 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.Zhou2016.html | 1 页 | 1 | MOT-MI-008 | curator_b | Zhou et al. 2016 PLoS ONE doi 10.1371/journal.pone.0162657 => MOT-MI-008 |
| WF-B2-09 | 2026-10-03 | WebFetch | https://www.bbci.de/competition/iv/ | 1 页 | 0 | MOT-MI-009, MOT-ME-002, MOT-REACH-002 | curator_b | BCI Competition IV datasets 1, 2a, 2b, 3, 4 => MOT-MI-009, MOT-ME-002, MOT-REACH-002 |
| WF-B2-10 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.BNCI2019_001.html | 1 页 | 1 | MOT-ATT-003 | curator_b | Ofner et al. 2019 Sci Rep doi 10.1038/s41598-019-43594-9 => MOT-ATT-003 |
| WF-B2-11 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.BNCI2024_001.html | 1 页 | 1 | MOT-HW-002 | curator_b | Crell & Müller-Putz 2024 Comput Biol Med doi 10.1016/j.compbiomed.2024.109132 => MOT-HW-002 |
| WF-B2-12 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.BNCI2015_004.html | 1 页 | 1 | IMG-MA-002; class list conflicts with WF-B2-02 | curator_b | Scherer et al. 2015 PLoS ONE doi 10.1371/journal.pone.0123727 (title not shown) => IMG-MA-002; class list conflicts with WF-B2-02 |
| WF-B2-13 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.BNCI2020_001.html | 1 页 | 1 | MOT-GRASP-003 | curator_b | Schwarz et al. 2020 Front Neurosci doi 10.3389/fnins.2020.00849 => MOT-GRASP-003 |
| WF-B2-14 | 2026-10-03 | WebFetch | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4735988/ | 302 重定向 | 0 | — | curator_b | R0835 (MRCP review) — redirected to pmc.ncbi.nlm.nih.gov |
| WF-B2-15 | 2026-10-03 | WebFetch | https://pmc.ncbi.nlm.nih.gov/articles/PMC4735988 | reCAPTCHA 页面（拒绝） | 0 | — | curator_b | not retried (rule: never retry a refused page) |
| WS-B2-01 | 2026-10-03 | WebSearch | q="Pfurtscheller 2006 NeuroImage mu rhythm (de)synchronization single-trial classification different motor imagery tasks hand foot tongue" | 9 条结果 | 1 | MOT-MI-002 | curator_b | doi 10.1016/J.NEUROIMAGE.2005.12.003; author PDF pub.ista.ac.at => MOT-MI-002 |
| WS-B2-02 | 2026-10-03 | WebSearch | q="Wolpaw McFarland 2004 PNAS control of a two-dimensional movement signal by a noninvasive brain-computer interface" | 10 条结果 | 1 | MOT-CURSOR-002 | curator_b | neurotechcenter.org/node/3139 => MOT-CURSOR-002 |
| WS-B2-03 | 2026-10-03 | WebSearch | q="multimodal signal dataset 11 intuitive movement tasks single upper extremity EEG GigaScience" | 9 条结果 | 1 | MOT-MI-011 | curator_b | PMC7539536, pure.korea.ac.kr => MOT-MI-011 |
| WS-B2-04 | 2026-10-03 | WebSearch | q="cue-based versus self-paced movement-related cortical potential detection ankle dorsiflexion brain-computer interface Niazi" | 9 条结果 | 1 | MOT-MRCP-002/-003 | curator_b | vbn.aau.dk brainsci_09_00127.pdf => MOT-MRCP-002/-003 |
| WF-B2-16 | 2026-10-03 | WebFetch | https://pub.ista.ac.at/~schloegl/publications/pfurtscheller2006.pdf | 1 页 | — | MOT-MI-002 | curator_b | Pfurtscheller, Brunner, Schlögl, Lopes da Silva 2006 NeuroImage 31:153-159: 4 classes, arrow at s 3 for 1.25 s, no feedback => MOT-MI-002 |
| WF-B2-17 | 2026-10-03 | WebFetch | https://www.neurotechcenter.org/node/3139 | 1 页 | — | MOT-CURSOR-002 | curator_b | Wolpaw & McFarland 2004 PNAS 101:17849-17854, doi 10.1073/pnas.0403504101, PMID 15585584 => MOT-CURSOR-002 |
| WF-B2-18 | 2026-10-03 | WebFetch | https://pure.korea.ac.kr/en/publications/multimodal-signal-dataset-for-11-intuitive-movement-tasks-from-si/ | 1 页 | — | MOT-MI-011 | curator_b | Jeong et al. 2020 GigaScience 9(10), doi 10.1093/GIGASCIENCE/GIAA098; 11 tasks not enumerated => MOT-MI-011 |
| WF-B2-19 | 2026-10-03 | WebFetch | https://vbn.aau.dk/ws/files/305102099/brainsci_09_00127.pdf | 1 页 | — | MOT-MRCP-002/-003 | curator_b | Jochumsen et al. 2019 Brain Sci 9(6):127 doi 10.3390/brainsci9060127 => MOT-MRCP-002/-003 |
| WS-B2-05 | 2026-10-03 | WebSearch | q="Monti 2010 New England Journal of Medicine willful modulation of brain activity in disorders of consciousness yes/no questions tennis imagery" | 9 条结果 | 1 | IMG-CMD-003 | curator_b | montilab.psych.ucla.edu PDF => IMG-CMD-003 |
| WS-B2-06 | 2026-10-03 | WebSearch | q="memory-guided saccade task fMRI human frontal eye field delay period remembered target location" | 9 条结果 | 1 | MOT-SACC-002 | curator_b | cns.nyu.edu Schluppeck-JNeurosci2006.pdf => MOT-SACC-002 |
| WS-B2-07 | 2026-10-03 | WebSearch | q=""Thinking out loud" inner speech EEG dataset Nieto 2022 Scientific Data words arriba abajo derecha izquierda pronounced visualized" | 9 条结果 | 2 | IMG-SPI-002/-003 | curator_b | sinc.unl.edu.ar NPRKS22; frontiersin frsip.2022.760643 => IMG-SPI-002/-003 |
| WF-B2-20 | 2026-10-03 | WebFetch | https://montilab.psych.ucla.edu/wp-content/uploads/sites/49/2015/11/Monti_etal_2010_NEJM.pdf | 1 页 | — | IMG-CMD-003 | curator_b | Monti et al. 2010 NEJM 362(7):579-589: yes/no mapping, 30 s imagery/30 s rest => IMG-CMD-003 |
| WF-B2-21 | 2026-10-03 | WebFetch | https://www.sinc.unl.edu.ar/sinc-publications/2022/NPRKS22/ | 1 页（仅书目信息） | — | IMG-SPI-002 | curator_b | Nieto et al. 2022 Sci Data 9(1):52 => IMG-SPI-002 |
| WF-B2-22 | 2026-10-03 | WebFetch | https://www.cns.nyu.edu/heegerlab/content/publications/Schluppeck-JNeurosci2006.pdf | 1 页 | — | MOT-SACC-002 | curator_b | Schluppeck et al. 2006 J Neurosci 26(19):5098-5108; cites Gnadt & Andersen 1988 => MOT-SACC-002 |
| WF-B2-23 | 2026-10-03 | WebFetch | https://www.frontiersin.org/journals/signal-processing/articles/10.3389/frsip.2022.760643/full | 1 页 | 1 | IMG-SPI-002/-003 | curator_b | Varshney & Khan 2022 Front Signal Process; secondary citations Zhao & Rudzicz 2015, Coretto et al. 2017, Nieto et al. 2021 => IMG-SPI-002/-003 |

WebSearch 用量：7 次（上限 12）。被拒页面（WF-B2-15，PMC reCAPTCHA）未重试。

### 本轮新线索（待维护者分配 R 编号，写入 `curation/literature.csv`）

| 线索 | 文献 | DOI / PMID | 用于 |
|---|---|---|---|
| S2B-L01 | Pfurtscheller G, Brunner C, Schlögl A, Lopes da Silva FH. Mu rhythm (de)synchronization and EEG single-trial classification of different motor imagery tasks. NeuroImage 31:153-159, 2006 | 10.1016/j.neuroimage.2005.12.003 | MOT-MI-002 |
| S2B-L02 | Ofner P, Schwarz A, Pereira J, Müller-Putz GR. Upper limb movements can be decoded from the time-domain of low-frequency EEG. PLoS ONE 12(8):e0182578, 2017 | 10.1371/journal.pone.0182578 | MOT-MI-003, MOT-ME-005 |
| S2B-L03 | Faller J, Vidaurre C, Solis-Escalante T, Neuper C, Scherer R. Autocalibration and recurrent adaptation: towards a plug and play online ERD-BCI. IEEE TNSRE 20(3):313-319, 2012 | 10.1109/tnsre.2012.2189584 | MOT-MI-007 |
| S2B-L04 | Zhou B, Wu X, Lv Z, Zhang L, Guo X. A fully automated trial selection method for optimization of motor imagery based BCI. PLoS ONE 11(9), 2016 | 10.1371/journal.pone.0162657 | MOT-MI-008 |
| S2B-L05 | Schalk G, McFarland DJ, Hinterberger T, Birbaumer N, Wolpaw JR. BCI2000: a general-purpose BCI system. IEEE TBME 51(6):1034-1043, 2004 | 10.1109/TBME.2004.827072 | MOT-MI-010 |
| S2B-L06 | Jeong JH, Cho JH, Shim KH, et al. Multimodal signal dataset for 11 intuitive movement tasks from single upper extremity during multiple recording sessions. GigaScience 9(10), 2020 | 10.1093/gigascience/giaa098 | MOT-MI-011 |
| S2B-L07 | Leeb R, Brunner C, Müller-Putz GR, Schlögl A, Pfurtscheller G, et al. (title not shown). IEEE TNSRE, 2007 | 10.1109/TNSRE.2007.906956 | MOT-MI-005 (TBD note) |
| S2B-L08 | Ofner P, et al. Attempted arm and hand movements can be decoded from low-frequency EEG from persons with spinal cord injury. Sci Rep 9(1):7134, 2019 | 10.1038/s41598-019-43594-9 | MOT-ATT-003 |
| S2B-L09 | Wolpaw JR, McFarland DJ. Control of a two-dimensional movement signal by a noninvasive brain-computer interface in humans. PNAS 101:17849-17854, 2004 | 10.1073/pnas.0403504101; PMID 15585584 | MOT-CURSOR-002 |
| S2B-L10 | Schwarz A, Escolano C, Montesano L, Müller-Putz GR. Analyzing and decoding natural reach-and-grasp actions using gel, water and dry EEG systems. Front Neurosci 14:849, 2020 | 10.3389/fnins.2020.00849 | MOT-GRASP-003 |
| S2B-L11 | Crell MR, Müller-Putz GR. Handwritten character classification from EEG through continuous kinematic decoding. Comput Biol Med 182:109132, 2024 | 10.1016/j.compbiomed.2024.109132 | MOT-HW-002 |
| S2B-L12 | Jochumsen M, Navid MS, Nedergaard RW, et al. Self-paced online vs. cue-based offline brain-computer interfaces for inducing neural plasticity. Brain Sci 9(6):127, 2019 | 10.3390/brainsci9060127 | MOT-MRCP-002, -003 |
| S2B-L13 | Schluppeck D, Curtis CE, Glimcher PW, Heeger DJ. Sustained activity in topographic areas of human posterior parietal cortex during memory-guided saccades. J Neurosci 26(19):5098-5108, 2006 | — | MOT-SACC-002 |
| S2B-L14 | Monti MM, Vanhaudenhuyse A, Coleman MR, et al. Willful modulation of brain activity in disorders of consciousness. NEJM 362(7):579-589, 2010 | — | IMG-CMD-003 |
| S2B-L15 | Scherer R, Faller J, Friedrich EVC, et al. (title not shown). PLoS ONE, 2015 | 10.1371/journal.pone.0123727 | IMG-MA-002 |
| S2B-L16 | Nieto N, Peterson V, Rufiner HL, Kamienkoski J, Spies R. Thinking out loud, an open-access EEG-based BCI dataset for inner speech recognition. Sci Data 9(1):52, 2022 | — | IMG-SPI-002 |
| S2B-L17 | Varshney YV, Khan A. Imagined speech classification using six phonetically distributed words. Front Signal Process 2:760643, 2022 | 10.3389/frsip.2022.760643 | IMG-SPI-002/-003 (secondary citations), proposal |
