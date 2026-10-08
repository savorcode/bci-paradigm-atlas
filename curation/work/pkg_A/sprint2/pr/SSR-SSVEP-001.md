<!-- 草稿：curator_a，2026-10-03，sprint 2。PR 描述按 .github/pull_request_template.md 填写。 -->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`SSR-SSVEP-001` 稳态视觉诱发电位范式 / Steady-state visual evoked potential paradigm
- 范式类 / Class：`SSR-SSVEP`（新范式类 / new class：否；类级修改见 sprint2/class_updates.yaml）
- 给号依据 / Numbering criterion（D-057）：`-001` 标准配置（最早发表或公认），不取新号；标准配置（最早发表，即 first_source）：单一调制光源，按运行改变频率，被动观察，开环（Regan 1966）。多目标频率编码 BCI -002（准则 1;4）、临床光驱动 -003（准则 1;3）、多刺激频率标记注意 -004（准则 1;2）、JFPM 40 目标拼写 -005、JFPM 12 目标 -006、含静息类 -007、异步 -008。
- 工作包 / Package：A
- 类型 / Kind：第二遍补完整（D-057 protocol）；收窄配置并拆出兄弟协议
- 新增或修改的标记物 / Markers touched：无（仅引用 `MK.SSVEP`）
- 写入的变体（含被并入候选，D-030）/ Variants added：无

## 出处核对表 / Source verification table

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | Regan D. Some characteristics of average steady-state and transient responses evoked by modulated light. Electroencephalogr Clin Neurophysiol. 1966;20(3):238-248. (doi 10.1016/0013-4694(66)90088-5) | 待核对原文 | 待核对原文 |
| description | 本次策展人撰写，依据 notes 所列线索 | 待核对原文 | 待核对原文 |
| protocol | 依据 first_source 与 notes 所列检索记录（数据集页面/摘要） | 待核对原文 | 见 search_log 对应条目的摘录 |
| markers: MK.SSVEP | curation/registry/markers.csv（仅引用） | — | — |
| trial_structure | 见 notes（数据集页面给出的时序；其余仅列条件） | 待核对原文 | 待核对原文 |

## 线索核对 / Lead check

- 使用的线索 / Leads used：R0085, R0206, R0398, R0483, R0667, R0802, R0867, R0954, R1047, R1090
- 线索有误之处 / Errors found in leads（DOI 不符、年份错误等）：未发现（未对照原文）

## 自查 / Checklist

- [x] 本地 `python scripts/validate.py` 0 problem(s)
- [x] `class` 等于 ID 去掉序号；给号依据已在上方和 `protocol.distinguishing` 中写明（D-057），只改参数的写进了 `variants`
- [x] 只修改了本包写入范围内的文件（D-029）
- [x] `markers` 只使用登记表中的 ID
- [x] 所有出处 `verified: false`
- [x] 查不到的字段已删除或留空，没有根据记忆或推测填写任何文献、DOI、数字
- [ ] 没有转引：每条出处都对照原文核对过（本轮出处来自线索表、检索结果页或数据集页面，未读原文）
- [x] 混合 BCI / 超扫描变体使用 `Hybrid:` / `Hyperscanning:` 前缀（本条目无此类变体）
- [x] 已更新本包 sprint2 `split_log.csv`、`worklog.md`
- [x] 提交已签署（`git commit -s`，DCO）

## 审核人 / Reviewer

- 交叉审核包 / Cross-review package：E 审 A
- [ ] 审核人已对照原文核实源头文献与描述
