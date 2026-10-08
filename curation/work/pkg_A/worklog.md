# 工作日志 · 包 A 感知与稳态

> 每次工作追加一节（最新在下）。写：做了什么、核对了哪些线索（R 编号）、遇到的问题、需要例会讨论或需要其他包处理的事项（含 D-030 跨包交接的线索）。

<!-- 模板
## YYYY-MM-DD · <策展人>
- 完成：
- 核对线索：
- 问题 / 待例会：
- 交接给其他包：
-->

## 2026-10-03 · curator_a（第一遍骨架冲刺）

### 时间线
- 09:00 读入 methodology、CONTRIBUTING、schema、taxonomy、种子条目、decisions.md（D-001–D-030）、本目录 README、任务单、candidates.csv、登记表与文献线索表。
- 09:40 规划：41 个收录候选（含 2 个种子 PER-ODD-001、SSR-SSVEP-001）＋ 5 个并入变体（D-002/003/004/011/017）＋ D-012 两个变体；本包 40 个标记物（37 个骨架 + P3a/P3b/SSVEP 种子）。
- 10:00–11:30 检索（WebSearch 28 次，WebFetch 20 次，见 search_log.md SA01–SA48）：先为新候选找线索，再为缺源头的核心范式补检。PubMed 检索页、E-utilities、Europe PMC 不可用（403/robots/429），之后改用机构库与 Wikipedia 页面补全题录。
- 11:30–13:00 编写 57 个新范式文件（39 个原有候选 + 18 个新候选）的描述（中英文均为本人撰写），用脚本生成 YAML（yaml.safe_dump，allow_unicode）。
- 13:00 补充两个种子条目（只增不删）；覆盖 37 个标记物骨架；新建 10 个申请的标记物文件；MK.SSVEP 种子只补别名（登记表 notes 中的同义项）。
- 13:30 生成 status.csv、new_candidates.csv、marker_requests.csv、pr/*.md（59 份）；`python3 scripts/validate.py` → 0 problem(s)。

### 决定
- **first_source 规则**：只用线索表字段拼引文；线索不含源头时用检索补（8 个已有范式 + 7 个新候选的源头来自检索，notes 中注明 SA 编号）；仍找不到的写 `TBD`（27 个，列入 status.csv 阻塞）。所有出处 `verified: false`。
- PER-CVA-001：R0343 线索只有 DOI 无标题，用期刊页面（SA48）补全题录，DOI 与线索一致，first_source_ref 仍记 R0343。
- PER-MVEP-001：Guo et al. 2008（SA45/47）只代表 mVEP-BCI，写作变体，不作源头。
- PER-OLF-001：R0046（Freeman 1978）疑为动物嗅球研究，不作源头。
- PER-CAT-001：R0059（Ungerleider & Mishkin 1982）是唯一"源头候选"但属理论章节，暂用并在 notes/status 中标记待议。
- SSR-FFR-001：Wikipedia（SA36）给出 Worden & Marsh 1968；该文是否为人类记录待核对。
- 不填 trial_structure（第一遍避免未核实的数字）；描述中的潜伏期/频率为教科书级近似。
- 数据集只写线索中出现的名称：PER-FACE-001（ds000117、SPM faces）、PER-ODD-001（NITRC RSVP ESS）、SSR-SSVEP-001（BETA、清华 benchmark）、PER-VOICE-001（Edinburgh Human Voice Areas）。HED 任务页与"关键词页"不作为数据集。

### 变体（D-030）
- PER-ODD-001：RSVP 目标检测（PER-RSVP-001，出处 R0038）；别名加入 RSVP、RSVP-BCI 等（注意瞬脱类别名留给 PER-AB-001）。
- SSR-SSVEP-001：光驱动（R1090）、多目标频率标记注意（R0802）、高频/不可见闪烁 SSVEP（检索 SA32，Ladouce 2024）。
- PER-MMN-001：音位对比 MMN（LAN-PHON-001，R0988）。
- SSR-SSSEP-001：稳态触觉空间注意（D-012，R1048）。
- PER-MVEP-001：mVEP-BCI（Guo et al. 2008）。
- **未写**：PER-ODD-001 的触觉 P300 BCI 变体（D-012）——无任何线索，列为阻塞。

### 新候选（new_candidates.csv，18 个，建议收录，均已建骨架）
PER-VMMN-001、PER-MLR-001、PER-ACC-001、PER-ORN-001、PER-STREAM-001、PER-GEP-001、PER-SPN-001、PER-IC-001、PER-ADDS-001、PER-IB-001、PER-CB-001、PER-RREP-001、PER-VOICE-001、PER-BODY-001、SSR-IM-001、SSR-NSSEP-001、SSR-FPAS-001、SSR-RVS-001。
已核对与全部 209 个候选的名称/别名不重复。其中 10 个申请新标记物（marker_requests.csv），其余复用登记表标记物。

### 问题 / 待例会
1. 27 个条目 first_source = TBD（含 ABR、AEP、PRVEP、FVEP、GATE、c-VEP、SSSEP、FPVS、SWEEP、TACT 等核心/临床范式）。WebSearch 只返回标题+URL，PubMed/Europe PMC 无法抓取，建议维护者在有数据库访问时集中补源头。
2. 需维护者写入登记表：10 个新标记物（MK.vMMN、MK.MLR、MK.ORN、MK.GEP、MK.SPN、MK.Pd、MK.RREP、MK.intermodulation、MK.SSEP_nociceptive、MK.FPAS_oddball）；以及 paradigm_markers.csv 中 18 个新候选的标记物行、markers.csv 的 used_by 更新（MK.MMN + PER-STREAM-001；MK.N1_auditory/MK.P2_auditory + PER-ACC-001；MK.N1_visual + PER-IC-001；MK.VAN + PER-IB-001/PER-CB-001；MK.P3b + PER-IB-001；MK.BOLD_auditory_cortex + PER-VOICE-001；MK.BOLD_category_selective/MK.N170 + PER-BODY-001；MK.oscillatory_entrainment + SSR-RVS-001）。
3. 独立性待议：SSR-FPAS-001（是否作为 SSR-FPVS-001 的听觉变体，届时 MK.FPAS_oddball 并入 MK.FPVS_oddball）；PER-ACC-001（是否为 PER-AEP-001 变体）；SSR-SWEEP-001（维护者候议）。
4. 新候选 PER-RREP-001 的刺激模态暂记 `somatosensory`（呼吸机械感受），词表无"内感受"项；PER-HBD-001 记 `cognitive_task`。是否在下一版词表中增加 `interoceptive`？
5. 种子条目用 yaml.safe_dump 重写后格式变化（flow → block 样式），内容未删减；如维护者希望保留原格式，可在合并时用 diff 只取新增部分。

### 交接给其他包
- 包 B：SSR-RVS-001 引用 MK.oscillatory_entrainment（owner B），请在 description 中考虑"节律性感觉刺激引起的夹带"，不只 tACS。
- 包 D：LAN-PHON-001 的线索（R0968、R0975、R0988、R1068）已从 paradigm_literature.csv 直接取用并写入 PER-MMN-001 变体；无需再交接。
- 包 E（交叉审核 A）：pr/*.md 的出处核对表页码与原文栏全部为"待核对原文"。
