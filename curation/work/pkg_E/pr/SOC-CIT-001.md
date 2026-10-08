> **已作废（维护者，2026-10-03）**：D-035：与 MEM-CIT-001 重复，已合并到 MEM-CIT-001；本条目文件已删除，ID 不复用。本草稿仅作记录保留。

<!-- PR 描述草稿 · SOC-CIT-001 · curator_e · 2026-10-03 -->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`SOC-CIT-001` 隐匿信息测验（基于 P300） / Concealed information test (P300-based)
- 工作包 / Package：E
- 类型 / Kind：第一遍骨架
- 新增或修改的标记物 / Markers touched：无 / none
- 写入的变体（含被并入候选，D-030）/ Variants added：无 / none
- 新候选 / New candidate：由 curator_e 新增（见 `curation/work/pkg_E/new_candidates.csv`），待维护者分配确认 ID

## 出处核对表 / Source verification table

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | S13 (curator_e search, see search_log.md): Farwell LA, Donchin E. The Truth Will Out: Interrogative Polygraphy ("Lie Detection") with Event-Related Brain Potentials. Psychophysiology 28(5):531-547. 1991. (doi:10.1111/j.1469-8986.1991.tb01990.x) | 待核对原文 | 待核对原文 |
| description (en/zh) | 策展人依据线索标题与摘要撰写，待对照原文 / written from leads: S13 | 待核对原文 | 待核对原文 |
| markers: MK.P3b | curator_e 提议 / proposed from S13 | 待核对原文 | 待核对原文 |
| interop.bids_task | `cit` 策展人拟定 / curator-chosen label | 待核对原文 | 待核对原文 |

## 线索核对 / Lead check

- 使用的线索 / Leads used：S13
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
