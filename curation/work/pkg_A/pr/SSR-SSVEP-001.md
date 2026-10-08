<!-- 草稿：curator_a，2026-10-03。PR 描述按 .github/pull_request_template.md 填写。 -->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`SSR-SSVEP-001` 稳态视觉诱发电位 / SSVEP
- 工作包 / Package：A
- 类型 / Kind：修正（种子条目补充：别名、3 个并入变体、数据集）
- 新增或修改的标记物 / Markers touched：`MK.SSVEP`
- 写入的变体（含被并入候选，D-030）/ Variants added：Photic driving (clinical intermittent photic stimulation); Frequency-tagged attention to multiple concurrent stimuli; High-frequency / imperceptible-flicker SSVEP

## 出处核对表 / Source verification table

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | Regan 1966（种子条目原有，未改） | 待核对原文 | 待核对原文 |
| description | 种子条目原有（未改） | 待核对原文 | 待核对原文 |
| markers: MK.SSVEP | curation/registry/paradigm_markers.csv；文献：种子条目原有（未改） | 待核对原文 | 待核对原文 |
| variants[0] | R1090: guidelines for visual sensitive eeg testing. Canadian Journal of Neurological Sciences. | 待核对原文 | 待核对原文 |
| variants[1] | R0802: Davidson, M. J. The SSVEP tracks attention, not consciousness, during visual masking. eLife. 2020. | 待核对原文 | 待核对原文 |
| variants[2] | search (SA32): Ladouce et al. Frequency tagging of spatial attention using periliminal flickers. Imaging Neuroscience. 2024. | 待核对原文 | 待核对原文 |
| trial_structure | 未填写（第一遍不填） | — | — |

## 线索核对 / Lead check

- 使用的线索 / Leads used：R0667, R0867, R1047; R0954, R1090; R0085, R0206, R0398, R0483, R0802; search SA32
- 线索有误之处 / Errors found in leads（DOI 不符、年份错误等）：未发现（未对照原文）
- 备注：MK.SSVEP 种子文件仅补充别名（光驱动响应、频率标记视觉响应，见登记表 notes）。

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
