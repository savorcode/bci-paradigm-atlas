<!-- PR draft · curator_d · sprint 2 · 2026-10-03 -->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`MEM-NAV-002` 虚拟放射臂迷宫 / Virtual radial arm maze
- 范式类 / Class：`MEM-NAV`（新范式类 / new class：否）
- 给号依据 / Numbering criterion（D-057）：1;2;4；与兄弟协议 `MEM-NAV-001`, `MEM-NAV-003` 的区别：准则 1;2：环境与任务由城镇寻路（MEM-NAV-001）变为多臂迷宫中的赢—移（win-shift）觅食，类别为已访问/未访问、有/无奖励的臂；每次进入给出是否获得奖励的离散反馈（准则 4）。
- 工作包 / Package：D
- 类型 / Kind：第二冲刺：新具体范式（D-057 拆分）
- 新增或修改的标记物 / Markers touched：无（仅引用）
- 写入的变体（含被并入候选，D-030）/ Variants added：（由 `MEM-NAV-001` 的变体“Virtual radial arm maze”拆出）

## 出处核对表 / Source verification table

本轮未核对原文页码与原句（所有出处 `verified: false`）。

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | Astur, R. S., Tropp, J., Sava, S., Constable, R. T., & Markus, E. J. Sex differences and correlations in a virtual Morris water task, a virtual radial arm maze, and mental rotation. Behavioural Brain Research. 2004. | 待核对原文 | 待核对原文 |
| protocol.distinguishing | 策展人依据 D-057 撰写 | 待核对原文 | 待核对原文 |
| protocol.classes / n_classes | 策展人依据 description 与线索标题撰写，待对照原文 | 待核对原文 | 待核对原文 |
| protocol.paradigm_timing / feedback | synchronous / discrete；待对照原文 | 待核对原文 | 待核对原文 |
| description | 策展人撰写，待对照原文 | 待核对原文 | 待核对原文 |
| trial_structure.conditions | 策展人撰写，待对照原文 | 待核对原文 | 待核对原文 |
| markers: MK.BOLD_hippocampus | knowledge/markers/；支持文献待第二遍 | 待核对原文 | 待核对原文 |

## 线索核对 / Lead check

- 使用的线索 / Leads used：R0037, R0289, R0315, R0366, R0698
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
