<!-- PR 描述草稿 · SOC-PAIN-001 · curator_e · sprint 2 · 2026-10-03 -->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`SOC-PAIN-001` 疼痛共情 / Empathy for pain
- 范式类 / Class：`SOC-PAIN`（新范式类 / new class：否；范式类修改见 `sprint2/class_updates.yaml`）
- 给号依据 / Numbering criterion（D-057）：—（-001 标准配置）；与兄弟协议 `同类其他具体范式见 split_log.csv` 的区别：Standard configuration (earliest published or canonical; D-057 -001): cue-based self/other pain paradigm with a present partner (lead R0920). Differs from SOC-PAIN-002 (pictures of body parts in painful situations).
- 工作包 / Package：E
- 类型 / Kind：修正（sprint 2：新增 protocol）
- 新增或修改的标记物 / Markers touched：无新标记物 / none（使用 MK.LPP, MK.BOLD_anterior_insula）
- 写入的变体（含被并入候选，D-030）/ Variants：无 / none

## 出处核对表 / Source verification table

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | R0920: Empathy for pain involves the affective but not sensory components of pain. | 待核对原文 | 待核对原文 |
| protocol | R0920；策展人依据线索与检索页面撰写 / written from leads and fetched pages | 待核对原文 | 待核对原文 |
| description (en/zh) | 策展人撰写 / curator-written from leads R0919;R0920;R0982;R0984 | 待核对原文 | 待核对原文 |
| markers: MK.LPP | curation/registry/paradigm_markers.csv / 范式类登记 | 待核对原文 | 待核对原文 |
| markers: MK.BOLD_anterior_insula | curation/registry/paradigm_markers.csv / 范式类登记 | 待核对原文 | 待核对原文 |
| datasets | — | — | — |

## 线索核对 / Lead check

- 使用的线索 / Leads used：R0919;R0920;R0982;R0984；sprint 2 检索编号见 `sprint2/search_log.md`
- 线索有误之处 / Errors found in leads：见 notes（作者缺失的线索未补作者）

## 自查 / Checklist

- [x] 本地 `python scripts/validate.py` 0 problem(s)
- [x] `class` 等于 ID 去掉序号；新序号已在上方和 `protocol.distinguishing` 中写明依据的给号准则（1–4，D-057），只改参数的写进了 `variants` 而没有新开序号
- [x] 只修改了本包写入范围内的文件（D-029）
- [x] `markers` 只使用登记表中的 ID
- [x] 所有出处 `verified: false`
- [x] 查不到的字段已删除或留空，没有根据记忆或推测填写任何文献、DOI、数字
- [ ] 没有转引：每条出处都对照原文核对过（未对照原文，页码与原文待核对）
- [ ] 混合 BCI / 超扫描变体使用 `Hybrid:` / `Hyperscanning:` 前缀（D-022、D-021）
- [x] 已更新本包 `sprint2/split_log.csv`、`sprint2/worklog.md`
- [ ] 提交已签署（`git commit -s`，DCO）

## 审核人 / Reviewer

- 交叉审核包 / Cross-review package：D 审 E
- [ ] 审核人已对照原文核实源头文献与描述
