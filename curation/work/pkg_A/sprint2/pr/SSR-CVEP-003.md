<!-- 草稿：curator_a，2026-10-03，sprint 2。PR 描述按 .github/pull_request_template.md 填写。 -->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`SSR-CVEP-003` 突发（burst）编码 c-VEP / Burst c-VEP
- 范式类 / Class：`SSR-CVEP`（新范式类 / new class：否；类级修改见 sprint2/class_updates.yaml）
- 给号依据 / Numbering criterion（D-057）：准则 2；与兄弟协议的区别：准则 2（编码方案）：稀疏突发码取代 -001 的 m 序列循环移位与 -002 的 Gold 码。幅度深度（100%/40%）为参数。
- 工作包 / Package：A
- 类型 / Kind：新具体范式（D-057 拆分/新增）
- 新增或修改的标记物 / Markers touched：无（仅引用 `MK.cVEP`）
- 写入的变体（含被并入候选，D-030）/ Variants added：Reduced amplitude depth (40 %)

## 出处核对表 / Source verification table

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | Cabrera Castillos K, Ladouce S, Darmet L, Dehais F. Burst c-VEP based BCI: optimizing stimulus design for enhanced classification with minimal calibration data and improved user experience. NeuroImage. 2023;284:120446. (doi 10.1016/j.neuroimage.2023.120446) | 待核对原文 | 待核对原文 |
| description | 本次策展人撰写，依据 notes 所列线索 | 待核对原文 | 待核对原文 |
| protocol | 依据 first_source 与 notes 所列检索记录（数据集页面/摘要） | 待核对原文 | 见 search_log 对应条目的摘录 |
| markers: MK.cVEP | curation/registry/markers.csv（仅引用） | — | — |
| trial_structure | 见 notes（数据集页面给出的时序；其余仅列条件） | 待核对原文 | 待核对原文 |
| variants[0] | Cabrera Castillos K, et al. NeuroImage. 2023;284:120446 (dataset CastillosBurstVEP40). | 待核对原文 | 待核对原文 |
| datasets[0] | Castillos burst c-VEP dataset, 100 % amplitude https://moabb.neurotechx.com/docs/generated/moabb.datasets.CastillosBurstVEP100.html | — | 数据集页面 |
| datasets[1] | Castillos burst c-VEP dataset, 40 % amplitude | — | 数据集页面 |

## 线索核对 / Lead check

- 使用的线索 / Leads used：无 R 编号线索；检索 S2A26
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
