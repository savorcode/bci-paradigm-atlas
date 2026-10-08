# 工作日志 · 包 E 情绪、社会与脑状态

> 每次工作追加一节（最新在下）。写：做了什么、核对了哪些线索（R 编号）、遇到的问题、需要例会讨论或需要其他包处理的事项（含 D-030 跨包交接的线索）。

<!-- 模板
## YYYY-MM-DD · <策展人>
- 完成：
- 核对线索：
- 问题 / 待例会：
- 交接给其他包：
-->

## 2026-10-03 · curator_e（第一遍骨架）

### 时间线（按顺序；记录写于 2026-10-03 16:31 UTC）
- ① 通读方法说明、CONTRIBUTING、三份 schema、taxonomy、模板与种子条目、decisions.md（D-001–D-030）、本包 README、任务单、candidates.csv（E 包 43 行）、标记物登记表与 paradigm_markers.csv、literature.csv / paradigm_literature.csv（E 包线索 244 条）。
- ② 汇总每个候选的线索、HED 任务页与数据集线索；确认 39 个收录候选、3 个并入（EMO-MUS-001 → EMO-FILM-001，SOC-HYP-001 → SOC-JA-001，SOC-SID-001 → EMO-MID-001）、1 个暂缓（STA-HYB-001，不建条目）。
- ③ 检索（30 次 WebSearch 用满配额 + 29 次 WebFetch（含 2 次失败），见 search_log.md）：为缺源头的既有候选补源头，为新候选找线索。PubMed 检索页 WebFetch 返回 429，未重试；E-utilities 被 robots 拒绝。
- ④ 用脚本（yaml.safe_dump，allow_unicode，sort_keys=False）生成 55 个范式文件（39 既有 + 16 新候选）与 15 个标记物文件；描述均为逐条手写。
- ⑤ `python3 scripts/validate.py`：58 paradigms, 112 markers；0 problem(s)。分批提交。

### 决定
1. **first_source 选择**：优先「源头候选 / 关键文献(HED)」中年份最早的线索；线索无作者/年份（PubMed 自动线索 R08xx–R10xx）时只写标题、期刊、PMID。
   - SOC-TOM-001 取行为学源头 R0060（Wimmer & Perner 1983），fMRI 定位任务 R0260 写成变体；SOC-UG-001 同理取 R0054，R0264 在 notes。
   - EMO-AUTO-001 取 R0073（线索词自传体记忆测验，临床背景），notes 说明不是情绪诱发的源头。
   - STA-SCP-001 既有线索（R0012 等）是准备电位文献，改用检索到的 S03（Birbaumer et al. 1999）。
   - 线索中无合理源头、检索后仍找不到：**EMO-EST-001**（R0137 为 1996 综述）、**STA-NF-001**（全部为综述/方法文献）→ citation 写 TBD，status.csv 记为阻塞。
2. **变体**（共 8 条）：EMO-FILM-001 音乐/音乐视频（并入 EMO-MUS-001，D-018，来源 R0862 为综述）；SOC-JA-001 `Hyperscanning:`（并入 SOC-HYP-001，D-021，R0227）；EMO-MID-001 社会激励延迟（并入 SOC-SID-001，D-025，R0426）；SOC-TRUST-001 `Hyperscanning:` 多轮信任博弈（R0312）；SOC-TOM-001 fMRI 错误信念定位（R0260）；EMO-FC-001 恐惧泛化（R1010）；STA-NF-001 rtfMRI 与 fNIRS 神经反馈（R0940、R0936，按 D-020）。被并入候选的英文名与别名并入目标 `aliases`，线索与 HED 页写入目标 `notes`（D-030）。
3. **名称**：EMO-FILM-001、SOC-JA-001 按 D-018、D-021 使用扩展名称。
4. **数据集**只取 candidates.csv `datasets` 列中的名称（无 URL）：SEED、DEAP、AMIGOS、sustained-attention driving（figshare）、COG-BCI、MPI LEMON、睡眠剥夺静息 EEG、Sleep-EDF Expanded。
5. **标记物**：14 个本包标记物骨架全部覆盖（名称、别名、类型、模态、中英描述）；signature 只写教科书级特征，notes 注明待核对；不写 generators/indexes。新申请 **MK.BOLD_posterior_insula**（EMO-TOUCH-001 用，登记表无同义项），已建文件并登记 marker_requests.csv。
6. **新候选 16 个**（new_candidates.csv，均建议收录、已建骨架）：EMO-WORD、EMO-THREAT、EMO-TOUCH、EMO-HUMOR、SOC-NAME、SOC-CIT、SOC-MORAL、SOC-CONF、SOC-SFB、SOC-ANIM、SOC-RACE、SOC-EYE、STA-CLAS、STA-DREAM、STA-PSY、STA-HYPN（均 -001）。查重：已核对全部 209 个候选的名称与别名，无重复。

### 本次检索采用的文献（S 编号，范式 notes 中引用）

| 编号 | 书目（仅含可见字段） | DOI | PMID | URL | 获取方式 |
|---|---|---|---|---|---|
| S01 | Eisenberger et al. Does rejection hurt? An fMRI study of social exclusion. 2003. |  | 14551436 | https://pubmed.ncbi.nlm.nih.gov/14551436/ | WebSearch #2 (titles + URLs; author/year from stafforini.com URL slug 'eisenberger-2003-does-rejection-hurt') |
| S01b | Kip Williams's List of Cyberball Publications. |  |  | https://www3.psych.purdue.edu/~willia55/Announce/Cyberball_Articles.htm | WebSearch #1 |
| S02 | Dmochowski JP, Sajda P, Dias J, Parra LC. Correlated Components of Ongoing EEG Point to Emotionally Laden Attention – A Possible Marker of Engagement? Frontiers in Human Neuroscience 6. 2012. | 10.3389/fnhum.2012.00112 | 22623915 | https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2012.00112/full | WebSearch #3 + WebFetch (frontiersin.org) |
| S03 | Birbaumer N, Ghanayim N, Hinterberger T, Iversen I, Kotchoubey B, Kübler A, Perelmouter J, Taub E, Flor H. A spelling device for the paralysed. Nature 398(6725):297-298. 1999. | 10.1038/18581 |  | https://ideas.repec.org/a/nat/nature/v398y1999i6725d10.1038_18581.html | WebSearch #4 + WebFetch (ideas.repec.org) |
| S04 | Sensorimotor EEG operant conditioning: Experimental and clinical effects. |  |  | https://scholarhub.vn/publication/:slug/f95af23a-e8b0-42d2-b17e-973ef65dc03a | WebSearch #5 |
| S05 | Hirai T, Kasamatsu A. An Electroencephalographic Study on the Zen Meditation Zazen. Journal of the American Institute of Hypnosis 14(3):107-114. 1973. |  |  | https://dlbs.liberal.ntu.edu.tw/search/search_detail.jsp?seq=282367 | WebSearch #6 + WebFetch (NTU Digital Library of Buddhist Studies record) |
| S06 | Kelso JAS, Tognoli E, Lagarde J, Deguzman GC. The phi complex as a neuromarker of human social coordination. Proceedings Of The National Academy Of Sciences 104:8190-8195. |  |  | https://ordb.biotech.ttu.edu/ORDB/Data/139136 | WebSearch #7 + WebFetch (ORDB record) |
| S07 | Rechtschaffen A, Kales A (eds). A manual of standardized terminology, techniques and scoring system for sleep stages of human subjects. U.S. Dept. of Health, Education, and Welfare, Bethesda, Md. 1968. |  |  | https://search.worldcat.org/oclc/2518321 | WebSearch #8 + WebFetch (WorldCat OCLC 2518321) |
| S08 | Kissler J, Herbert C, Peyk P, Junghofer M. Buzzwords: early cortical responses to emotional words during reading. Psychological Science 18(6). 2007. | 10.1111/j.1467-9280.2007.01924.x |  | https://www.psychologicalscience.org/journals/psychological-science/j.1467-9280.2007.01924.x/ | WebSearch #9 + WebFetch (psychologicalscience.org) |
| S09 | Alvarez RP, Chen G, Bodurka J, Kaplan R, Grillon C. Phasic and sustained fear in humans elicits distinct patterns of brain activity. NeuroImage. 2011. |  | 21111828 | https://neurosynth.org/studies/21111828 | WebSearch #11 + WebFetch (neurosynth.org) |
| S10 | Olausson H et al. Unmyelinated tactile afferents signal touch and project to insular cortex. Nature Neuroscience. 2002. | 10.1038/nn896 |  | https://link.springer.com/article/10.1038/news020722-12 | WebSearch #12 + WebFetch (Nature news 'Caress touches a nerve', 2002-07-22, which cites the paper) |
| S11 | Mobbs D, Greicius MD, Abdel-Azim E, Menon V, Reiss AL. Humor modulates the mesolimbic reward centers. Neuron. 2003. |  | 14659102 | https://neurosynth.org/studies/14659102 | WebSearch #13 + WebFetch (neurosynth.org) |
| S12 | Berlad I, Pratt H. P300 in response to subject's own name. Electroencephalogr Clin Neurophysiol 96:472-474. 1995. | 10.1016/0168-5597(95)00116-a |  | https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00194/full | WebSearch #14 + WebFetch (reference list of Tacikowski et al. 2014) |
| S12b | Tacikowski P, Cygan HB, Nowicka A. Neural correlates of own and close-other's name recognition: ERP evidence. Frontiers in Human Neuroscience. 2014. | 10.3389/fnhum.2014.00194 |  | https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00194/full | WebSearch #14 + WebFetch |
| S13 | Farwell LA, Donchin E. The Truth Will Out: Interrogative Polygraphy ("Lie Detection") with Event-Related Brain Potentials. Psychophysiology 28(5):531-547. 1991. | 10.1111/j.1469-8986.1991.tb01990.x |  | https://digitalcommons.usf.edu/psy_facpub/311 | WebSearch #15 + WebFetch (USF Digital Commons) |
| S14 | Greene J, Sommerville B, Nystrom L, Darley J, Cohen J. An fMRI Investigation of Emotional Engagement in Moral Judgment. Science 293(5537):2105-2108. 2001. | 10.1126/science.1062872 | 11557895 | https://nystrom.scholar.princeton.edu/bibcite/export/bibtex/bibcite_reference/91 | WebSearch #16 + WebFetch (Princeton BibTeX export); PMID from pubmed result URL |
| S15 | Klucharev V, Hytönen K, Rijpkema M, Smidts A, Fernandez G. Reinforcement Learning Signal Predicts Social Conformity. Neuron 61(1):140-151. 2009. | 10.1016/j.neuron.2008.11.027 | 19146819 | https://repub.eur.nl/pub/15056 | WebSearch #17 + WebFetch (repub.eur.nl); PMID from pubmed result URL |
| S16 | Somerville LH, Heatherton TF, Kelley WM. Anterior cingulate cortex responds differentially to expectancy violation and social rejection. Nature Neuroscience 9:1007-1008. 2006. | 10.1038/nn1728 |  | https://www.nature.com/articles/nn1728 | WebSearch #18 + WebFetch (nature.com) |
| S17 | Castelli F, Happé F, Frith U, Frith C. Movement and Mind: A Functional Imaging Study of Perception and Interpretation of Complex Intentional Movement Patterns. 2000. |  | 10944414 | https://iris.unipv.it/handle/11571/1511996 | WebSearch #19 + WebFetch (IRIS Univ. Pavia record) |
| S17b | Gaze patterns and brain activations in humans and marmosets in the Frith-Happé theory-of-mind animation task. |  |  | https://elifesciences.org/articles/86327v1/figures | WebSearch #19 |
| S18 | Ito TA, Urland GR. Race and gender on the brain: Electrocortical measures of attention to the race and gender of multiply categorizable individuals. Journal of Personality and Social Psychology 85(4):616-626. 2003. |  | 14561116 | https://experts.colorado.edu/display/pubid_52678 | WebSearch #20 + WebFetch (CU Experts record); PMID from top pubmed result URL (title not displayed in result) - verify |
| S19 | Ngo HVV, Martinetz T, Born J, Mölle M. Auditory closed-loop stimulation of the sleep slow oscillation enhances memory. Neuron 78(3):545-553. 2013. | 10.1016/j.neuron.2013.03.006 |  | https://research.uni-luebeck.de/en/publications/auditory-closed-loop-stimulation-of-the-sleep-slow-oscillation-en/ | WebSearch #21 + WebFetch (Univ. Lübeck research portal) |
| S20 | Siclari F, Baird B, Perogamvros L, Bernardi G, LaRocque JJ, Riedner B, Boly M, Postle BR, Tononi G. The neural correlates of dreaming. Nature Neuroscience 20(6):872-878. 2017. | 10.1038/nn.4545 | 28394322 | https://archive-ouverte.unige.ch/unige:96505 | WebSearch #22 + WebFetch (Archive ouverte UNIGE) |
| S21 | Carhart-Harris RL, Muthukumaraswamy S, Roseman L, Kaelen M, Droog W, et al. Neural correlates of the LSD experience revealed by multimodal neuroimaging. Proceedings of the National Academy of Sciences 113(17):4853-4858. 2016. | 10.1073/pnas.1518377113 |  | https://orca.cardiff.ac.uk/id/eprint/95413/ | WebSearch #23 + WebFetch (ORCA Cardiff) |
| S22 | Spiegel DR et al. Brain Activity and Functional Connectivity Associated with Hypnosis. Cerebral Cortex 27(8):4083-4093. 2017. |  |  | https://researchers.evms.edu/display/pub27469596 | WebSearch #24 + WebFetch (EVMS researcher record; only Spiegel listed) |
| S23 | Lin CT, Wu RC, Liang SF, Chao WH, Chen YJ, Jung TP. EEG-based drowsiness estimation for safety driving using independent component analysis. IEEE Transactions on Circuits and Systems I: Regular Papers 52(12):2726-2738. 2005. | 10.1109/TCSI.2005.857555 |  | https://opus.lib.uts.edu.au/handle/10453/123837 | WebSearch #25 + WebFetch (UTS OPUS) |
| S24 | Third party punishment and social norms. Evolution and Human Behavior 25:63-87. 2004. |  |  | https://www.merlin.uzh.ch/publication/show/5664 | WebSearch #26 + WebFetch (UZH MERLIN record; authors not displayed) |
| S25 | Paulmann S, Kotz SA. Early emotional prosody perception based on different speaker voices. NeuroReport 19(2):209-213. 2008. | 10.1097/wnr.0b013e3282f454db |  | https://repository.essex.ac.uk/3391/ | WebSearch #27 + WebFetch (Essex repository) |
| S26 | Hirsch J, Zhang X, Noah JA, Ono Y. Frontal temporal and parietal systems synchronize within and across brains during live eye-to-eye contact. NeuroImage 157:314-330. 2017. | 10.1016/j.neuroimage.2017.06.018 |  | https://discovery-pp.ucl.ac.uk/id/eprint/10064566 | WebSearch #28 + WebFetch (UCL Discovery) |
| S27 | Keenan JP, Nelson A, O'Connor M, Pascual-Leone A. Self-recognition and the right hemisphere. Nature 409(6818):305. 2001. | 10.1038/35053167 |  | https://ideas.repec.org/a/nat/nature/v409y2001i6818d10.1038_35053167.html | WebSearch #29 + WebFetch (ideas.repec.org) |
| S28 | David N, Bewernick BH, Cohen MX, Newen A, Lux S, Fink GR, Shah NJ, Vogeley K. Neural representations of self versus other: visual-spatial perspective taking and agency in a virtual ball-tossing game. J Cognitive Neurosci 18(6):898-910. 2006. | 10.1162/jocn.2006.18.6.898 | 16839298 | https://fis.uke.de/portal/en/publications/neural-representations-of-self-versus-other-visualspatial-perspective-taking-and-agency-in-a-virtual-balltossing-game(7b363190-1007-4395-8ea7-53a5f7ecb39c)/export.html | WebSearch #30 + WebFetch (UKE research portal export) |

### 问题 / 待例会
1. **源头仍缺**：EMO-EST-001、STA-NF-001（阻塞）。以下条目的 first_source 是较早的神经研究而非范式源头，第二遍需补：SOC-CYB-001（行为源头 Williams et al. 2000 未检出）、SOC-SELF-001（S27 为 Wada 研究，非神经记录）、SOC-VPT-001、SOC-TPP-001（S24 作者未显示）、EMO-SOUND-001、STA-MED-001（1966 原文未核）、STA-HYPN-001、STA-PSY-001、EMO-THREAT-001。
2. **书目疑点**：S06（SOC-JA-001）ORDB 记录年份 2006/作者顺序与 PNAS 104 卷不符，year 留空；S12（SOC-NAME-001）仅见于他文参考文献；S18 PMID 来自未显示标题的结果 URL；R1064（STA-MATB-001）标题为任务单记忆补写；R0683、R0533、R0788 的 DOI 与题名/期刊不符；R0831 DOI 为占位符。请维护者在 literature.csv 中修正。
3. **新候选的边界**（请例会判定收录或并入）：SOC-NAME-001 与 SOC-CIT-001 都用 MK.P3b，可能被视为 PER-ODD-001 变体（包 A）；SOC-CIT-001 也可归 memory 族；STA-CLAS-001 与 MEM-TMR-001（包 D）相邻；SOC-EYE-001 可改为 SOC-GAZE-001 的 `Hyperscanning:` 变体；EMO-TOUCH-001 可归 perception 族；STA-PSY-001 是药物诱导状态，是否算"范式"需确认（与 STA-ANES-001 一致处理）。
4. **词表缺口**：taxonomy 无"药物给予"刺激模态（STA-ANES-001、STA-PSY-001 分别暂用 cognitive_task、resting_state）；睡眠分期暂用 resting_state。建议在下一版词表讨论中处理。
5. **未登记的反馈信号标记物**：STA-NF-001 的 rtfMRI/fNIRS 变体反馈脑区 BOLD/HbO，登记表无对应项；第一遍未申请，待第二遍按 D-020 决定是否申请。
6. **登记表与决议冲突**：candidates.csv 中 CTL-STR-001 的 aliases 含 "Emotional Stroop (variant)"，与 D-019（不加情绪 Stroop 变体）冲突，请维护者删除。
7. SOC-ANIM-001 的源头为 PET 研究，而 MK.BOLD_TPJ / MK.BOLD_mPFC 只登记 fMRI；建议 hemodynamic 标记物的 recording_modality 增加 PET，或在 notes 中统一说明。
8. MK.BOLD_mPFC（包 D）、MK.BOLD_dACC（包 C）被新候选 SOC-MORAL/SOC-ANIM/SOC-CONF/SOC-SFB/STA-HYPN 引用，需维护者把这些范式补入登记表 `used_by`。

### 交接给其他包
- 包 A：SOC-NAME-001 / SOC-CIT-001 与 PER-ODD-001 的关系（见问题 3）；EMO-TOUCH-001 与 PER-TACT-001。
- 包 C：MK.BOLD_dACC 新增使用者 SOC-CONF-001、SOC-SFB-001、STA-HYPN-001。
- 包 D：MK.BOLD_mPFC 新增使用者 SOC-MORAL-001、SOC-ANIM-001；STA-CLAS-001 与 MEM-TMR-001 的边界；SOC-CIT-001 族归属。
