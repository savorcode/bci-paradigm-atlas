<!-- 草稿：curator_a，2026-10-03。PR 描述按 .github/pull_request_template.md 填写。 -->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`PER-CTXC-001` 情境线索效应 / Contextual cueing
- 工作包 / Package：A
- 类型 / Kind：第一遍骨架
- 新增或修改的标记物 / Markers touched：`MK.BOLD_hippocampus`
- 写入的变体（含被并入候选，D-030）/ Variants added：无

## 出处核对表 / Source verification table

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | R0160: Chun, M. M., & Jiang, Y. Contextual cueing: Implicit learning and memory of visual context guides spatial attention. Cognitive Psychology, 36(1), 28–71. 1998. | 待核对原文 | 待核对原文 |
| description | R0160, R0253, R0646, R0707 | 待核对原文 | 待核对原文 |
| markers: MK.N2pc | curation/registry/paradigm_markers.csv；文献：R0160, R0253, R0646, R0707 | 待核对原文 | 待核对原文 |
| markers: MK.BOLD_hippocampus | curation/registry/paradigm_markers.csv；文献：R0160, R0253, R0646, R0707 | 待核对原文 | 待核对原文 |
| trial_structure | 未填写（第一遍不填） | — | — |

## 线索核对 / Lead check

- 使用的线索 / Leads used：R0160, R0253, R0646, R0707, R0746, R0771, R0817
- 线索有误之处 / Errors found in leads（DOI 不符、年份错误等）：未发现（未对照原文）

## 自查 / Checklist

- [x] 本地 `python scripts/validate.py` 0 problem(s)
- [x] 只修改了本包写入范围内的文件（`paradigms/<本包族>/`、owner 为本包的 `knowledge/markers/`、`curation/work/pkg_<X>/`；D-029）
- [x] `markers` 只使用 `curation/registry/paradigm_markers.csv` 中的 ID，或已在 `marker_requests.csv` 中申请
- [x] 所有出处 `verified: false`（由审核人核实后改为 true）
- [x] 查不到的字段已删除或留空，没有根据记忆或推测填写任何文献、DOI、数字
- [ ] 没有转引：每条出处都对照原文核对过（第一遍未对照原文，出处仅来自线索表或检索结果页）
- [x] 混合 BCI / 超扫描变体使用 `Hybrid:` / `Hyperscanning:` 前缀（D-022、D-021）（本条目无此类变体）
- [x] 已更新本包 `status.csv`、`worklog.md`
- [x] 提交已签署（`git commit -s`，DCO）

## 审核人 / Reviewer

- 交叉审核包 / Cross-review package：E 审 A
- [ ] 审核人已对照原文核实源头文献与描述
