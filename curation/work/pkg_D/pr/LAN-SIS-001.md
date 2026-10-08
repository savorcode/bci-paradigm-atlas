<!-- PR draft · curator_d · 2026-10-03 -->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`LAN-SIS-001` 言语诱发抑制与听觉反馈 / Speaking-induced suppression / altered auditory feedback
- 工作包 / Package：D
- 类型 / Kind：第一遍骨架（新候选，curator_d 提议）
- 新增或修改的标记物 / Markers touched：无（仅引用）
- 写入的变体（含被并入候选，D-030）/ Variants added：无

## 出处核对表 / Source verification table

所有原文页码与原句均未核对（第一遍骨架）。

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | DN39 Speaking modifies voice-evoked activity in the human auditory cortex. | 待核对原文 | 待核对原文 |
| description | 策展人撰写（教科书层面）；待对照：DN39, DN40 | 待核对原文 | 待核对原文 |
| aliases | 策展人拟定 | 待核对原文 | 待核对原文 |
| recording_modality | 策展人拟定；待对照：DN39, DN40 | 待核对原文 | 待核对原文 |
| stimulus_modality | 策展人拟定；待对照：DN39, DN40 | 待核对原文 | 待核对原文 |
| bci_category | 策展人拟定；待对照：DN39, DN40 | 待核对原文 | 待核对原文 |
| interop.bids_task | 策展人拟定（BIDS task label） | 待核对原文 | 待核对原文 |
| markers: MK.N1_auditory | curation/registry/paradigm_markers.csv（新候选：策展人选定，见 new_candidates.csv / marker_requests.csv）；支持文献待第二遍：DN39, DN40 | 待核对原文 | 待核对原文 |
| markers: MK.high_gamma | curation/registry/paradigm_markers.csv（新候选：策展人选定，见 new_candidates.csv / marker_requests.csv）；支持文献待第二遍：DN39, DN40 | 待核对原文 | 待核对原文 |

## 线索核对 / Lead check

- 使用的线索 / Leads used：DN39（可用线索：DN39, DN40）
- 线索有误之处 / Errors found in leads：web_search 线索普遍缺作者/年份字段。

## 自查 / Checklist

- [x] 本地 `python scripts/validate.py` 0 problem(s)
- [x] 只修改了本包写入范围内的文件（`paradigms/memory|language/`、owner 为本包的 `knowledge/markers/`、`curation/work/pkg_D/`；D-029）
- [ ] `markers` 只使用 `curation/registry/paradigm_markers.csv` 中的 ID，或已在 `marker_requests.csv` 中申请（新候选：使用登记表 ID 或已申请的新 ID，未进入 paradigm_markers.csv）
- [x] 所有出处 `verified: false`（由审核人核实后改为 true）
- [x] 查不到的字段已删除或留空，没有根据记忆或推测填写任何文献、DOI、数字
- [ ] 没有转引：每条出处都对照原文核对过（第一遍未核对原文）
- [x] 混合 BCI / 超扫描变体使用 `Hybrid:` / `Hyperscanning:` 前缀（D-022、D-021）（本条目无此类变体）
- [x] 已更新本包 `status.csv`、`worklog.md`
- [x] 提交已签署（`git commit -s`，DCO）

## 审核人 / Reviewer

- 交叉审核包 / Cross-review package：C 审 D
- [ ] 审核人已对照原文核实源头文献与描述
