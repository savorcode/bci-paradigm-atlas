<!-- PR 描述草稿 · SOC-JA-001 · curator_e · 2026-10-03 -->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`SOC-JA-001` 联合动作与人际协调 / Joint action and interpersonal coordination
- 工作包 / Package：E
- 类型 / Kind：第一遍骨架
- 新增或修改的标记物 / Markers touched：`MK.interbrain_synchrony`
- 写入的变体（含被并入候选，D-030）/ Variants added：Hyperscanning: cooperative interaction tasks recorded simultaneously from two brains

## 出处核对表 / Source verification table

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | S06 (curator_e search, see search_log.md): Kelso JAS, Tognoli E, Lagarde J, Deguzman GC. The phi complex as a neuromarker of human social coordination. Proceedings Of The National Academy Of Sciences 104:8190-8195. (https://ordb.biotech.ttu.edu/ORDB/Data/139136) | 待核对原文 | 待核对原文 |
| description (en/zh) | 策展人依据线索标题与摘要撰写，待对照原文 / written from leads: R0227, R0841, R0953, R0963, R0964, R1042, R1061, S06 | 待核对原文 | 待核对原文 |
| markers: MK.SMR_ERD | curation/registry/paradigm_markers.csv | 待核对原文 | 待核对原文 |
| markers: MK.interbrain_synchrony | curation/registry/paradigm_markers.csv | 待核对原文 | 待核对原文 |
| variants[0] Hyperscanning: cooperative interaction tasks recorded simultaneously from two brains | R0227: Hyperscanning: Simultaneous fMRI during linked social interactions. NeuroImage 16, 1159-1164. 2002. (https://fbri.vtc.vt.edu/content/dam/fbri_vtc_vt_edu/publications/montague-publications/MontagueEtAlHyperscanning2002.pdf) | 待核对原文 | 待核对原文 |
| interop.bids_task | `jointaction` 策展人拟定 / curator-chosen label | 待核对原文 | 待核对原文 |

## 线索核对 / Lead check

- 使用的线索 / Leads used：R0227, R0841, R0953, R0963, R0964, R1042, R1061, S06
- 线索有误之处 / Errors found in leads：S06 记录年份 2006 与 PNAS 104 卷（2007）可能不符，year 已留空

## 自查 / Checklist

- [x] 本地 `python scripts/validate.py` 0 problem(s)
- [x] 只修改了本包写入范围内的文件（`paradigms/<本包族>/`、owner 为本包的 `knowledge/markers/`、`curation/work/pkg_E/`；D-029）
- [x] `markers` 只使用 `curation/registry/paradigm_markers.csv` 中的 ID，或已在 `marker_requests.csv` 中申请
- [x] 所有出处 `verified: false`（由审核人核实后改为 true）
- [x] 查不到的字段已删除或留空，没有根据记忆或推测填写任何文献、DOI、数字
- [ ] 没有转引：每条出处都对照原文核对过（第一遍未对照原文，页码与原文待核对）
- [x] 混合 BCI / 超扫描变体使用 `Hybrid:` / `Hyperscanning:` 前缀（D-022、D-021）
- [x] 已更新本包 `status.csv`、`worklog.md`
- [ ] 提交已签署（`git commit -s`，DCO）

## 审核人 / Reviewer

- 交叉审核包 / Cross-review package：D 审 E
- [ ] 审核人已对照原文核实源头文献与描述
