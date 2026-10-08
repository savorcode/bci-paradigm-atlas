<!-- PR draft · curator_d · sprint 2 · 2026-10-03 -->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`MEM-NBK-003` 双通道 n-back / Dual n-back
- 范式类 / Class：`MEM-NBK`（新范式类 / new class：否）
- 给号依据 / Numbering criterion（D-057）：1;2；与兄弟协议 `MEM-NBK-001`, `MEM-NBK-002`, `MEM-NBK-004` 的区别：准则 1;2：刺激由单一流（MEM-NBK-001）变为同时呈现的视觉空间流与听觉字母流，靶类别由一类变为视觉/听觉/双重/无四类。
- 工作包 / Package：D
- 类型 / Kind：第二冲刺：新具体范式（D-057 拆分）
- 新增或修改的标记物 / Markers touched：无（仅引用）
- 写入的变体（含被并入候选，D-030）/ Variants added：无

## 出处核对表 / Source verification table

本轮未核对原文页码与原句（所有出处 `verified: false`）。

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | Jaeggi SM, Seewer R, Nirkko AC, Eckstein D, Schroth G, Groner R, Gutbrod K. Does excessive memory load attenuate activation in the prefrontal cortex? Load-dependent processing in single and dual tasks: functional magnetic resonance imaging study. 2003. | 待核对原文 | 待核对原文 |
| protocol.distinguishing | 策展人依据 D-057 撰写 | 待核对原文 | 待核对原文 |
| protocol.classes / n_classes | 策展人依据 description 与线索标题撰写，待对照原文 | 待核对原文 | 待核对原文 |
| protocol.paradigm_timing / feedback | synchronous / none；待对照原文 | 待核对原文 | 待核对原文 |
| description | 策展人撰写，待对照原文 | 待核对原文 | 待核对原文 |
| trial_structure.conditions | 策展人撰写，待对照原文 | 待核对原文 | 待核对原文 |
| markers: MK.BOLD_frontoparietal | knowledge/markers/；支持文献待第二遍 | 待核对原文 | 待核对原文 |

## 线索核对 / Lead check

- 使用的线索 / Leads used：DN48, DN49
- 线索有误之处 / Errors found in leads：见 `sprint2/worklog.md`（如 R0979 从 BCI 变体改配到 LAN-VF-003；web_search 线索普遍缺作者/年份）。

## 自查 / Checklist

- [x] 本地 `python scripts/validate.py` 0 problem(s)
- [x] `class` 等于 ID 去掉序号；新序号已在上方和 `protocol.distinguishing` 中写明依据的给号准则（1–4，D-057），只改参数的写进了 `variants` 而没有新开序号
- [x] 只修改了本包写入范围内的文件（`paradigms/memory|language/`、`curation/work/pkg_D/`；D-029）
- [x] `markers` 只使用登记表中已有的 ID
- [x] 所有出处 `verified: false`（由审核人核实后改为 true）
- [x] 查不到的字段已删除或留空，没有根据记忆或推测填写任何文献、DOI、数字
- [ ] 没有转引：每条出处都对照原文核对过（本轮未核对原文）
- [x] 混合 BCI / 超扫描变体使用 `Hybrid:` / `Hyperscanning:` 前缀（D-022、D-021）（本条目无此类变体）
- [x] 已更新本包 `sprint2/split_log.csv`、`sprint2/worklog.md`
- [x] 提交已签署（`git commit -s`，DCO）

## 审核人 / Reviewer

- 交叉审核包 / Cross-review package：C 审 D
- [ ] 审核人已对照原文核实源头文献与描述
