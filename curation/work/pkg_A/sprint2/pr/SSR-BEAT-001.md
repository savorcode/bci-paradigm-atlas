<!-- 草稿：curator_a，2026-10-03，sprint 2。PR 描述按 .github/pull_request_template.md 填写。 -->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`SSR-BEAT-001` 节律与节拍跟随 / Beat / rhythm entrainment
- 范式类 / Class：`SSR-BEAT`（新范式类 / new class：否）
- 给号依据 / Numbering criterion（D-057）：`-001` 标准配置（最早发表或公认），不取新号；标准配置（最早发表，即 first_source）：聆听节律声音，有/无想象节拍（二拍/三拍）。本类暂无其他具体范式（no sibling protocol yet）。
- 工作包 / Package：A
- 类型 / Kind：第二遍补完整（D-057 protocol）
- 新增或修改的标记物 / Markers touched：无（仅引用 `MK.SSEP_beat`）
- 写入的变体（含被并入候选，D-030）/ Variants added：无

## 出处核对表 / Source verification table

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | Nozaradan S, Peretz I, Missal M, Mouraux A. Tagging the neuronal entrainment to beat and meter. The Journal of Neuroscience. 2011. (doi 10.1523/JNEUROSCI.0411-11.2011) | 待核对原文 | 待核对原文 |
| description | 沿用 sprint 1（未改） | 待核对原文 | 待核对原文 |
| protocol | 依据 first_source 与 notes 所列检索记录（数据集页面/摘要） | 待核对原文 | 见 search_log 对应条目的摘录 |
| markers: MK.SSEP_beat | curation/registry/markers.csv（仅引用） | — | — |

## 线索核对 / Lead check

- 使用的线索 / Leads used：R0377, R0548, R0623, R0688；检索 SA30, SA34
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
