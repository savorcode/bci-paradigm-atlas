# 工作日志 · 包 D 记忆与语言

> 每次工作追加一节（最新在下）。写：做了什么、核对了哪些线索（R 编号）、遇到的问题、需要例会讨论或需要其他包处理的事项（含 D-030 跨包交接的线索）。

<!-- 模板
## YYYY-MM-DD · <策展人>
- 完成：
- 核对线索：
- 问题 / 待例会：
- 交接给其他包：
-->

## 2026-10-03 · curator_d（第一遍骨架 + 候选扩充）

- 完成：
  - 范式文件 53 个：本包 38 个“收录”候选全部建骨架（`paradigms/memory/` 22 个、`paradigms/language/` 16 个），另为 15 个新候选建骨架（MEM 6、LAN 9）。全部 `status: draft`、`contributors: [curator_d]`、所有出处 `verified: false`。
  - 新候选 17 个写入 `new_candidates.csv`：15 个按“收录”处理并建文件；MEM-DE-001（延迟估计）建议并入 MEM-CD-001、LAN-SIGN-001（手语句子理解）建议并入 LAN-SC-001，均只写成目标范式的变体，不建文件。新线索 DN01–DN46 记入 `new_leads.csv`（仅填写检索结果或抓取页面中可见的字段）。
  - 变体 8 条：MEM-ON-001 Remember/know（D-024 并入的 MEM-RK-001，R0069）；MEM-FR-001 RAVLT（R0550）；MEM-CD-001 延迟估计（DN25）；MEM-NAV-001 虚拟放射臂迷宫（R0289）；MEM-META-001 学习判断（R0098）；LAN-P600-001 花园路径句（R0864）；LAN-PN-001 图词干扰（R1000）；LAN-SC-001 手语句子理解（DN45）。（MEM-RK-001 的别名同时并入 MEM-ON-001 aliases。）
  - 标记物 19 个：覆盖本包 17 个骨架文件（name、aliases、type、modality、description，ERP/节律类给出教科书层面的 signature 并在 notes 注明待核），新建 MK.CPS、MK.BOLD_left_IFG（登记于 `marker_requests.csv`）。
  - `status.csv`、`pr/<ID>.md`（53 份 PR 草稿，含出处核对表与自查清单）、`search_log.md`。
  - `python3 scripts/validate.py`：0 problem(s)。
- 决定：
  - first_source 选取：优先“源头候选/关键文献(HED)”中年代最早者；leads 中无可信源头时动用检索（NBK、FR、RC、SME、DS、HIER、LOC、READ 由检索补得，`first_source_ref = search`）。
  - 无法确定源头者写 TBD 并列为阻塞：MEM-PA-001、MEM-RPT-001、MEM-RMEM-001、MEM-RPRIM-001、LAN-SWITCH-001、LAN-GEST-001、LAN-NWL-001。
  - `status.csv` 的 status 按本次冲刺指令使用“第一遍完成 / 阻塞”（README 中列出的取值不同，请维护者统一）。
  - 数据集：所有线索中均无数据集记录，`datasets` 字段一律省略（未凭记忆填写）。
  - 多篇 S-001 web_search 线索没有作者/年份字段，citation 只写标题，未补写。
- 核对线索（发现的问题）：
  - MEM-RC-001 的 4 条线索（R0031、R0151、R0267、R0402）、LAN-HIER-001 的 4 条线索（R0216、R0321、R0381、R0419）都与范式无关（Wikipedia 页面误配），LAN-READ-001 的 4 条线索均无 EEG。建议维护者在 `paradigm_literature.csv` 中改配。
  - R0154（Jonides 1997）卷期与 DOI 不一致；R0562 标题是占位符；R0229 的 url 指向 TMR 的 Wikipedia 页面。
  - DN04（Paller, Kutas & Mayes 1987）抓取到的标题为 “...in an incidental paradigm”，常见引用为 “incidental learning paradigm”，待对照原文。
  - DMS（R0025）、NAV（R0065、R0037）的源头是动物研究，已在 notes 说明。
- 问题 / 待例会：
  1. **跨包重叠**：IMG-WORD-001（包 B）别名含 verbal fluency、verb generation，与 LAN-VF-001、LAN-VG-001 重叠，需决定归属或划界。LAN-NAT-001 与 PER-AAD-001、LAN-OVS-001 与 IMG-SPI-001 已在 notes 中互相区分。
  2. **MEM-DS-001（D-023）**：检索到 2 条 EEG/ERP 线索（DN06 数字广度 δ/θ 振荡；DN07 ERP 兼容的倒背数字广度），尚未核对原文，请例会判断是否满足“≥2 项独立研究”的口径，否则转为暂缓。状态记为“阻塞”。
  3. **新标记物**：MK.BOLD_left_IFG 可能与 MK.BOLD_language_network（含左 IFG）构成同义，需维护者决定是否并入；MK.CPS 无同义项。MEM-RPRIM-001 暂用 MK.BOLD_category_selective + MK.N400，可考虑专设 MK.repetition_suppression。
  4. 新候选的独立性待判：MEM-CIT-001（是否为 PER-ODD-001 变体）、LAN-PCAT-001（与 PER-MMN-001 音位 MMN 变体的边界，D-017）、LAN-SL-001（与 LAN-AGL-001/LAN-HIER-001）、LAN-SWITCH-001（与 CTL-SW-001）。
  5. 新候选使用的标记物不在 `paradigm_markers.csv` 中，合并时需维护者补登。
  6. PubMed/PMC 页面对 WebFetch 返回 reCAPTCHA，书目信息只能从检索结果标题或第三方页面获得。
- 交接给其他包：
  - 包 A（D-017，LAN-PHON-001 → PER-MMN-001 变体“Speech-sound / phoneme-contrast MMN”）：线索 R0968（Language-specific phoneme representations revealed by electric and magnetic brain responses，源头候选）、R0988（Mismatch negativity in a phonetic discrimination task，源头候选）、R1068 / R0216（Näätänen 2001 综述，同一文献的两条记录）、R0975（SLI 中 MMN 综述）。
  - 包 A：LAN-VWFA-001 使用 MK.N170 与 MK.BOLD_category_selective（owner A），如需在这两个标记物中补充“字词”相关描述，请包 A 处理。
  - 包 B：MK.high_gamma（owner B）被 LAN-SIS-001、LAN-PCAT-001 引用。
  - 包 C：MK.N2_frontocentral 被 LAN-SWITCH-001 引用；MK.BOLD_striatum_reward 被 MEM-RMEM-001 引用。
