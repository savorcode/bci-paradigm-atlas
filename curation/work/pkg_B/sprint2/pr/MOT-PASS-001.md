Closes #

## 内容 / Summary

- 范式 / Paradigm：`MOT-PASS-001` 被动运动（本体感觉刺激） / Passive movement / proprioceptive stimulation
- 范式类 / Class：`MOT-PASS`（新范式类 / new class：否；范式类修改见 `sprint2/class_updates.yaml`）
- 给号依据 / Numbering criterion（D-057）：—（-001 标准配置）；与兄弟协议的区别：Standard configuration (earliest published) / 标准配置（最早发表）: rhythmic passive finger movements with kinematics recorded for corticokinematic coherence (Bourguignon et al. 2015). No sibling protocol yet.
- 工作包 / Package：B
- 类型 / Kind：修正（sprint 2：补 protocol，收窄到标准配置）
- 新增或修改的标记物 / Markers touched：—（仅使用登记表中已有的标记物）
- 写入的变体（含被并入候选，D-030）/ Variants added：—；本次移出 `variants` 的条目：—

## 出处核对表 / Source verification table

所有原文页码与原句均为“待核对原文”：出处来自本包线索（R 编号）或 sprint 2 检索页面（`sprint2/search_log.md` 的 WS-B2-/WF-B2- 编号），尚未对照原文。

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | Bourguignon M, Piitulainen H, De Tiege X, Jousmaki V, Hari R. Corticokinematic coherence mainly reflects movement-induced proprioceptive feedback. NeuroImage 106:382-390. 2015. (doi 10.1016/j.neuroimage.2014.11.026) | 待核对原文 | 待核对原文 |
| description | 策展人据出处页面/线索撰写（见 notes 中的线索编号） | 待核对原文 | 待核对原文 |
| markers: MK.corticokinematic_coherence | curation/registry/markers.csv | 待核对原文 | 待核对原文 |
| markers: MK.SMR_ERD | curation/registry/markers.csv | 待核对原文 | 待核对原文 |
| protocol | Standard configuration (earliest published) / 标准配置（最早发表）: rhythmic passive finger movements with kinematics recorded for corticokinematic coherence (Bourguignon et al. 2015). No sibling protocol yet. | 待核对原文 | 待核对原文 |

## 线索核对 / Lead check

- 使用的线索 / Leads used：见文件 `notes`
- 线索有误之处 / Errors found in leads：见文件 `notes`（如 TBD、仅标题线索、二手引用）

## 自查 / Checklist

- [x] 本地 `python scripts/validate.py` 0 problem(s)
- [x] `class` 等于 ID 去掉序号；新序号已在上方和 `protocol.distinguishing` 中写明依据的给号准则（1–4，D-057），只改参数的写进了 `variants` 而没有新开序号
- [x] 只修改了本包写入范围内的文件（`paradigms/motor|imagery|stimulation/`、`curation/work/pkg_B/`；D-029）
- [x] `markers` 只使用 `curation/registry/markers.csv` 中的 ID
- [x] 所有出处 `verified: false`（由审核人核实后改为 true）
- [x] 查不到的字段已删除或留空，没有根据记忆或推测填写任何文献、DOI、数字（无法确认的类别集等已在 notes 标注“to be checked”）
- [ ] 没有转引：每条出处都对照原文核对过（未对照原文，待审核人核实）
- [x] 混合 BCI / 超扫描变体使用 `Hybrid:` / `Hyperscanning:` 前缀（D-022、D-021）（本条无此类变体）
- [x] 已更新本包 `sprint2/split_log.csv`、`sprint2/worklog.md`
- [ ] 提交已签署（`git commit -s`，DCO）

## 审核人 / Reviewer

- 交叉审核包 / Cross-review package：A（A 审 B）
- [ ] 审核人已对照原文核实源头文献与描述
