<!-- PR 描述草稿 · SOC-TOM-001 · curator_e · 2026-10-03 -->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`SOC-TOM-001` 心理理论（错误信念） / Theory of mind (false belief)
- 工作包 / Package：E
- 类型 / Kind：第一遍骨架
- 新增或修改的标记物 / Markers touched：`MK.BOLD_TPJ`
- 写入的变体（含被并入候选，D-030）/ Variants added：fMRI false-belief localizer (false belief vs false photograph)

## 出处核对表 / Source verification table

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | R0060: Wimmer, H., & Perner, J. Beliefs about beliefs: Representation and constraining function of wrong beliefs in young children's understanding of deception. Cognition, 13(1), 103–128. 1983. (doi:10.1016/0010-0277(83)90004-5) | 待核对原文 | 待核对原文 |
| description (en/zh) | 策展人依据线索标题与摘要撰写，待对照原文 / written from leads: R0060, R0068, R0207, R0260, R0308, R0435, R0561, R0604, R0741, R0875, R0967, R1074 | 待核对原文 | 待核对原文 |
| markers: MK.BOLD_TPJ | curation/registry/paradigm_markers.csv | 待核对原文 | 待核对原文 |
| variants[0] fMRI false-belief localizer (false belief vs false photograph) | R0260: Saxe, R., & Kanwisher, N. People thinking about thinking people: The role of the temporo-parietal junction in "theory of mind.". NeuroImage, 19(4), 1835-1842. 2003. (doi:10.1016/s1053-8119(03)00230-1) | 待核对原文 | 待核对原文 |
| interop.bids_task | `tom` 策展人拟定 / curator-chosen label | 待核对原文 | 待核对原文 |

## 线索核对 / Lead check

- 使用的线索 / Leads used：R0060, R0068, R0207, R0260, R0308, R0435, R0561, R0604, R0741, R0875, R0967, R1074
- 线索有误之处 / Errors found in leads：第一遍未发现（未对照原文）

## 自查 / Checklist

- [x] 本地 `python scripts/validate.py` 0 problem(s)
- [x] 只修改了本包写入范围内的文件（`paradigms/<本包族>/`、owner 为本包的 `knowledge/markers/`、`curation/work/pkg_E/`；D-029）
- [x] `markers` 只使用 `curation/registry/paradigm_markers.csv` 中的 ID，或已在 `marker_requests.csv` 中申请
- [x] 所有出处 `verified: false`（由审核人核实后改为 true）
- [x] 查不到的字段已删除或留空，没有根据记忆或推测填写任何文献、DOI、数字
- [ ] 没有转引：每条出处都对照原文核对过（第一遍未对照原文，页码与原文待核对）
- [ ] 混合 BCI / 超扫描变体使用 `Hybrid:` / `Hyperscanning:` 前缀（D-022、D-021）（不适用）
- [x] 已更新本包 `status.csv`、`worklog.md`
- [ ] 提交已签署（`git commit -s`，DCO）

## 审核人 / Reviewer

- 交叉审核包 / Cross-review package：D 审 E
- [ ] 审核人已对照原文核实源头文献与描述
