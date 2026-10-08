<!-- PR draft · curator_d · 2026-10-03 -->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`MEM-NAV-001` 虚拟空间导航记忆 / Virtual spatial navigation
- 工作包 / Package：D
- 类型 / Kind：第一遍骨架
- 新增或修改的标记物 / Markers touched：`MK.hippocampal_theta`
- 写入的变体（含被并入候选，D-030）/ Variants added：Virtual radial arm maze

## 出处核对表 / Source verification table

所有原文页码与原句均未核对（第一遍骨架）。

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | R0164 Maguire EA et al. Knowing where and getting there: A human navigation network. Science 280(5365). 1998. | 待核对原文 | 待核对原文 |
| description | 策展人撰写（教科书层面）；待对照：R0037, R0065, R0164, R0265 | 待核对原文 | 待核对原文 |
| aliases | curation/candidates.csv aliases 列 | 待核对原文 | 待核对原文 |
| recording_modality | curation/candidates.csv；待对照：R0037, R0065, R0164, R0265 | 待核对原文 | 待核对原文 |
| stimulus_modality | curation/candidates.csv；待对照：R0037, R0065, R0164, R0265 | 待核对原文 | 待核对原文 |
| bci_category | curation/candidates.csv；待对照：R0037, R0065, R0164, R0265 | 待核对原文 | 待核对原文 |
| interop.bids_task | 策展人拟定（BIDS task label） | 待核对原文 | 待核对原文 |
| markers: MK.hippocampal_theta | curation/registry/paradigm_markers.csv；支持文献待第二遍：R0037, R0065, R0164, R0265 | 待核对原文 | 待核对原文 |
| markers: MK.BOLD_hippocampus | curation/registry/paradigm_markers.csv；支持文献待第二遍：R0037, R0065, R0164, R0265 | 待核对原文 | 待核对原文 |
| variants[0] (Virtual radial arm maze) | R0289 Astur, R. S., Tropp, J., Sava, S., Constable, R. T., & Markus, E. J. Sex differences and correlations in a virtual Morris water task, a virtual radial arm maze, and mental rotation. Behavioural Brain Research. 2004. | 待核对原文 | 待核对原文 |

## 线索核对 / Lead check

- 使用的线索 / Leads used：R0164, R0289（可用线索：R0037, R0065, R0164, R0265, R0289, R0315, R0366, R0393, R0580, R0654, R0698, R0704, R0722, R0748）
- 线索有误之处 / Errors found in leads：未发现。

## 自查 / Checklist

- [x] 本地 `python scripts/validate.py` 0 problem(s)
- [x] 只修改了本包写入范围内的文件（`paradigms/memory|language/`、owner 为本包的 `knowledge/markers/`、`curation/work/pkg_D/`；D-029）
- [x] `markers` 只使用 `curation/registry/paradigm_markers.csv` 中的 ID，或已在 `marker_requests.csv` 中申请
- [x] 所有出处 `verified: false`（由审核人核实后改为 true）
- [x] 查不到的字段已删除或留空，没有根据记忆或推测填写任何文献、DOI、数字
- [ ] 没有转引：每条出处都对照原文核对过（第一遍未核对原文）
- [x] 混合 BCI / 超扫描变体使用 `Hybrid:` / `Hyperscanning:` 前缀（D-022、D-021）（本条目无此类变体）
- [x] 已更新本包 `status.csv`、`worklog.md`
- [x] 提交已签署（`git commit -s`，DCO）

## 审核人 / Reviewer

- 交叉审核包 / Cross-review package：C 审 D
- [ ] 审核人已对照原文核实源头文献与描述
