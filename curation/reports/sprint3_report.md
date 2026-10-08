# 出处书目核实冲刺（sprint 3）总结

> 写给：项目负责人。起草：维护者（maintainer），2026-10-07。
> 对应里程碑：M3（`integration` 分支，已合并到 `main`）。
> 详细材料：核实报告 `curation/reports/verification_sprint3.md`；决议 `curation/decisions.md` D-072 – D-074；结果表 `curation/verification/sources_check.csv`；覆盖度 `curation/reports/coverage_M3.md`；检索记录 `curation/search_protocol.md` S-004。

## 一、一句话结论

五位审核人交叉审核（A ← e、B ← a、C ← b、D ← c、E ← d），把图谱里**全部 682 条出处**（404 个具体范式、267 个范式类的 first_source，11 个变体源）逐条与 Crossref / OpenAlex 的权威记录比对：**一致 168、更正 379、TBD 找到候选 88、TBD 仍开放 12、查不到 35、指向另一篇 0**。更正绝大多数是把"只有题名"或缺卷期页的引文**补全**（补 DOI 184 条），实质性错误约 10 处（卷号、期号、页码、第一作者、作者顺序、重印本当原文各 1–2 处）。首次把 **first_source 为 TBD** 从 64 个具体范式 / 36 个范式类降到 **9 / 3**。

必须说清楚的一点：这是**书目核实**，不是**内容核实**。审核人确认了"这篇文献存在、书目字段正确"，没有读原文确认"它确实描述了该范式、而且是最早的"。所以 `verified: true` 仍然是 **0**。为此把两级核实写成了决议 D-072（已按授权裁定确认），`verified` 的含义不变。

## 二、全局数字

| 项目 | M2 | M3 |
|---|---|---|
| 范式类 / 具体范式 / 标记物 | 267 / 404（+1 作废）/ 129 | 不变 |
| 核实过书目的出处 | 0 | **635 / 682**（93.1%；一致 168 + 更正 379 + TBD 候选 88） |
| first_source 为 TBD（具体范式 / 范式类） | 64 / 36 | **9 / 3** |
| first_source 带 DOI 的有效具体范式 | 208 / 404（51%） | **370 / 404（92%）** |
| `verified: true`（内容核实） | 0 | **0** |
| 改动的 YAML 文件 | — | 382（381 个具体范式 + `_classes.yaml`，其中 184 个类的 first_source） |
| 接口请求 | — | 504 次（被拒 106 次；无 WebSearch） |
| `validate.py` | 0 / 0 | **0 问题、0 警告** |
| 图谱 | 811 节点 / 1,435 边 | 不变 |

按包：

| 包 | 审核人 | 行 | confirmed | corrected | tbd_resolved | tbd_open | not_found |
|---|---|---|---|---|---|---|---|
| A 感知与稳态 | curator_e | 150 | 56 | 30 | 57 | 2 | 5 |
| B 运动、想象与刺激 | curator_a | 133 | 39 | 83 | 5 | 0 | 6 |
| C 错误监测与认知控制 | curator_b | 127 | 10 | 94 | 0 | 8 | 15 |
| D 记忆与语言 | curator_c | 137 | 17 | 94 | 21 | 2 | 3 |
| E 情绪、社会与脑状态 | curator_d | 135 | 46 | 78 | 5 | 0 | 6 |

## 三、有代表性的更正（更多见核实报告第 7 节）

| ID | 之前 | 之后 |
|---|---|---|
| CTL-WCST-001（Grant & Berg 1948） | J Exp Psychol **34**:404-411 | J Exp Psychol 1948;**38**(4):404-411，补 DOI |
| CTL-AS-001（Hallett 1978） | Vision Research 18(**11**) | 1978;18(**10**):1279-1296 |
| MEM-META-002（Nelson & Dunlosky 1991） | 页 267-**270** | 267-**271** |
| STA-HYPN-001（催眠 fMRI） | **Spiegel DR et al.** 2017 | **Jiang H, White MP, Greicius MD, Waelde LC, Spiegel D.** 2017，补 DOI |
| SOC-JA-001（phi 复合波） | **Kelso JAS, Tognoli E, …** PNAS 104 | **Tognoli E, Lagarde J, DeGuzman GC, Kelso JAS.** 2007;104(19)，补 DOI |
| STA-MED-001（坐禅 EEG） | Hirai & Kasamatsu **1973** 重印本 | **Kasamatsu & Hirai 1966** 原文，Folia Psychiatr Neurol Jpn |
| MEM-SME-001（Paller 1987） | 题名漏 "learning"，无期页 | 补题名、67(4):360-371、DOI |
| PER-AAD-001 / MOT-ATT-001 / LAN-CPS-001 / PER-FACE-001 / STM-ADBS-001 | 只有题名 | 完整作者、期刊、年、卷期页、DOI |
| PER-ABR-001（TBD） | 无源头 | Jewett & Williston 1971 Brain（候选；1967 年 Sohmer & Feinmesser 待查优先权） |
| STA-SCP-001（TBD） | 无源头（最早见 1992 年记录） | Elbert, Rockstroh, Lutzenberger & Birbaumer 1980（候选，早 12 年） |

## 四、需要负责人知道的三件事

1. **工具环境远比预期差。** Crossref / OpenAlex 的**书目检索**接口经代理几乎全程 429，只有"按 DOI / PMID 取记录"可用；PubMed 页面是验证码或空页，**PMID 一律没有核验**。包 C 在约 85 次请求后遭全局限流，15 条（9 个具体范式 + 6 个类）**根本没有检查**，在结果表里记为 not_found（note 写明 "not checked"）。
2. **"凭记忆的候选 DOI"。** 检索不可用时，四个包（A 69 行、E 26 行、D 8 行、B 5 行）用审核人回忆的 DOI 作查询键取记录，记录题名 / 作者 / 年份与条目一致才写入；不一致者一律未写（如 IMG-MA 的 Keirn & Aunon 1990）。这与方法说明"不推测标识符"字面上有张力，但写入的是接口返回的权威记录而非推测。已按授权裁定为 D-073：**允许**，但 108 条都加了固定短语 `origin candidate recalled, record confirmed via <API>`，内容核实时优先复查。局限：只有包 A 逐行标注，E / D / B 由维护者按日志整体标注，可能有少数漏标或多标。
3. **88 条 "TBD 已解决"只是候选。** 它们满足 D-031 "任务程序最早描述"的书目条件，但没有读原文；其中几条审核人已指出更早的候选（PER-ABR、MEM-DF、MOT-MI-005 / -009、STM-ADBS）。覆盖度报告的 TBD 计数（9 / 3）因此偏乐观，真实的"源头待定"应理解为 9 / 3 开放 + 88 候选待核。

## 五、决议

| 编号 | 内容 | 状态 |
|---|---|---|
| D-072 | 两级核实：书目核实（`sources_check.csv` + notes 短语）vs 内容核实（`verified: true`）；schema 0.3 提议 `source_check` 字段 | 已确认（专家裁定，负责人授权，2026-10-07） |
| D-073 | 凭记忆候选 DOI、接口记录确认：允许，固定短语，内容核实前不得 verified | 已确认（同上） |
| D-074 | 47 行遗留（C 15 行未检查；20 行手册 / 指南 / 学位论文 / 书章无记录；12 行 TBD 开放）→ 第四冲刺，需机构数据库 | **草案，请确认** |

另：D-059、D-060、D-064 – D-070 仍待例会确认（M2 遗留）。

## 六、下一步（第四冲刺建议）

1. **先解决访问**：机构数据库（Web of Science / Scopus / PsycINFO）、Crossref polite pool（mailto 参数）或 OpenAlex API key、PubMed 机构访问。没有这些，第四冲刺做不了内容核实，也补不了 C 包的 15 行。
2. **顺序**：C 包 15 行未检查（纯书目，半天）→ 20 行手册 / 指南（WorldCat / 出版社记录，接受无 DOI）→ 12 行 TBD 开放 → 88 条 tbd_resolved 与 108 条 D-073 条目的**内容核实**（优先 P1 核心类，D-066）。
3. **维护者事项**：`literature.csv` 的 R 编号书目与 `sources_check.csv` 同步（本版未做）；schema 0.3 提议清单（`marker_basis`、`structure`、`source_check`）合并讨论。
