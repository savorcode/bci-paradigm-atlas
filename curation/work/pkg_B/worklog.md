# 工作日志 · 包 B 运动、想象与刺激

> 每次工作追加一节（最新在下）。写：做了什么、核对了哪些线索（R 编号）、遇到的问题、需要例会讨论或需要其他包处理的事项（含 D-030 跨包交接的线索）。

<!-- 模板
## YYYY-MM-DD · <策展人>
- 完成：
- 核对线索：
- 问题 / 待例会：
- 交接给其他包：
-->

## 2026-10-03 · curator_b（第一遍骨架 + 候选扩充）

**时间线**
- 09:00 读取 methodology、CONTRIBUTING、schema、taxonomy、模板与种子条目、decisions.md（D-001–D-030）、本目录 README、任务单、candidates.csv、registry、literature.csv / paradigm_literature.csv。
- 09:30 整理本包 41 个候选的线索（166 条，R 编号）；确定需要检索源头的范式：MOT-CURSOR、MOT-BIMAN、MOT-RT、IMG-SPI、IMG-SAO、STM-CCEP、STM-DBSEP、STM-PAS、STM-SEP、STM-TACS、STM-TEP、STM-TUS，以及并入变体 IMG-FACE（无线索）。
- 10:00–12:30 检索（WebSearch 30 次，见 search_log.md）。PubMed 检索页与 Crossref 检索接口返回 429，eutils 被 robots 禁止，PMC 页面为验证码页；均未重试，改用机构库/DOAJ/neurosynth 等页面核对书目。
- 13:00 编写 49 个骨架条目（33 个收录候选 + 16 个新候选）的数据，补充种子 MOT-MI-001；改写 22 个本包标记物骨架，新建 5 个申请标记物。
- 15:00 `python3 scripts/validate.py` → 0 problem(s)；生成 status.csv、pr/*.md（50 份）、new_candidates.csv（17 行）、marker_requests.csv（5 行）。

**决定**
- first_source 一律 `verified: false`；只写线索或检索页上实际显示的字段。只有标题的线索（多数 web_search 线索）引文只写标题，附 PMID（若有）。
- 检索补到的源头：MOT-CURSOR（Wolpaw 1991）、MOT-BIMAN（Kelso 1984，DOI 由 Crossref 记录页确认）、MOT-RT（Gratton 1988）、IMG-SPI（DaSalla 2009）、IMG-SAO（Yao 2013）、STM-CCEP（Matsumoto 2004）、STM-DBSEP（Sinclair 2018）、STM-PAS（Stefan 2000）、STM-SEP（Dawson 1947）、STM-TACS（Zaehle 2010）、STM-TEP（Ilmoniemi 1997）、STM-TUS（Legon 2014）。status.csv 中 first_source_ref 记为 `search`。
- MOT-HW-001 选 bioRxiv 预印本（R0948，最早且有 DOI）为 first_source，正式版 R0947 写入 notes。
- MOT-OBS-001 选最早的 R0995（TMS-MEP），R0845（MEG）在 notes 中作为最早神经记录线索——请审核人决定。
- MOT-SACC-001 按规则选 R0001（Javal 1878，唯一源头候选），但它不是眼跳任务论文；标为阻塞。antisaccade 从别名移除（CTL-AS-001 已收录，包 C）。
- STM-TACS-001 不采用 R0596（颅电疗治疗抑郁的 Cochrane 综述，与记录无关）。
- 变体（D-030）：MOT-ME-001 ← MOT-FING-001（R0871）、步行（D-014，R0955）、定速手指敲击（R0189）；MOT-MI-001 ← MOT-GAIT-001（R0883）；IMG-AUD-001 ← IMG-MUS-001（R0186，取自本范式线索）；IMG-VIS-001 ← IMG-FACE-001（检索 S15，题名未确认）；IMG-CMD-001 ← IMG-NAV-001（R0893）及床旁 EEG（R0858）。共 8 个变体。
- 种子 MOT-MI-001 只追加别名、变体、数据集与备注，原有内容未改动；MK.SMR_ERD 种子文件未改动。
- 新候选 STM-PBM-001（经颅光生物调节）只登记在 new_candidates.csv，未建文件：stimulus_modality 词表无光刺激词条。

**问题 / 待例会**
1. 新标记物申请 5 个（marker_requests.csv）：MK.corticokinematic_coherence、MK.perturbation_N1、MK.BOLD_olfactory_cortex、MK.BOLD_vestibular_cortex、MK.subthalamic_beta——需维护者补进登记表（文件已按 D-028 第 7 条建好）。
2. 词表：stimulus_modality 需要 `optical_stimulation`（STM-PBM-001）；recording_modality 的 `DBS-LFP` 提议（D-027）也适用于 STM-ADBS-001 与 MK.subthalamic_beta。
3. 族归属待定：STM-CLAS-001（stimulation vs state，与 MEM-TMR-001 的关系）、STM-VIB-001（stimulation vs motor）。
4. 边界：IMG-WORD-001 与 LAN-VF-001 / LAN-VG-001（包 D）高度重叠；MOT-LIBET-001 与 MOT-MRCP-001 / MOT-IB-001；MOT-PURS-001 是否为 MOT-SACC-001 的变体；MOT-SMS-001 与 SSR-BEAT-001（A）、SOC-JA-001（E）。
5. 线索可疑之处：R0874（PMID 42538749）、R0972（PMID 42435827）、R0956/R1045/R1051 的 PMID 偏大，需核对；R0820 卷/文章号与 DOI 尾号不一致（105131 vs 105187）；R0176（心理测量函数拟合）与镜像描摹无关；R0024（心理旋转）被挂在 IMG-VIS-001 下；R0062 为猴研究。
6. 源头只有行为学研究或 MEP 研究：MOT-BIMAN、MOT-SRT、MOT-MIRR、IMG-ROT（行为）；STM-PAS、STM-TDCS、STM-PHTMS（MEP）。是否需要另记“首个神经记录研究”请例会定口径。
7. 新候选 IMG-OLF-001 的源头（Djordjevic 2005）只见于 N07 的参考文献表，属转引，必须核原文。

**交接给其他包**
- 包 C：CTL-AS-001 与 MOT-SACC-001 共用 MK.presaccadic_potential、MK.BOLD_oculomotor（已写好标记物）；CTL-SIM-001 使用 MK.LRP（已写好）。
- 包 D：IMG-WORD-001 与 LAN-VF-001 / LAN-VG-001 边界；STM-CLAS-001 引用 MK.slow_wave、MK.sleep_spindle（owner D），请在 indexes 中考虑 CLAS 证据。
- 包 A：STM-TAVNS-001 引用 MK.P3b。
- 包 E：MK.SMR_ERD 的社会认知 indexes 仍由使用包向 owner（B）提出；MK.alpha_posterior、MK.frontal_midline_theta 描述已写，供 STA-* 条目引用。
