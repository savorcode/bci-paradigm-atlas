<!--
一个 PR 只放一个范式，以及它首次用到的、归本包编写的标记物。
One PR = one paradigm (plus the markers it first uses that your package owns).
草稿可先写在 curation/work/pkg_<X>/pr/<范式ID>.md。
-->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`<ID>` <中文名> / <English name>
- 范式类 / Class：`<范式族>-<简称>`（新范式类 / new class：是 / 否；新类写入 `sprint2/class_updates.yaml`）
- 给号依据 / Numbering criterion（D-057；新序号必填）：<1 类别/条件集 | 2 刺激或提示类型（含编码）| 3 试次结构 | 4 反馈方式>；与兄弟协议 `<ID>` 的区别：
- 工作包 / Package：<A–E>
- 类型 / Kind：<第一遍骨架 | 第二遍补完整 | 修正>
- 新增或修改的标记物 / Markers touched：`MK.…`
- 写入的变体（含被并入候选，D-030）/ Variants added：

## 出处核对表 / Source verification table

每个填写的字段都要有一行：出自哪篇文献、第几页、原文原句。Zotero 标签用范式 ID。
One row per filled field: which publication, page, verbatim quote.

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | | | |
| description | | | |
| markers: MK.… | | | |
| trial_structure | | | |
| variants[0] | | | |

## 线索核对 / Lead check

- 使用的线索 / Leads used：R0…, R0…
- 线索有误之处 / Errors found in leads（DOI 不符、年份错误等）：

## 自查 / Checklist

- [ ] 本地 `python scripts/validate.py` 0 problem(s)
- [ ] `class` 等于 ID 去掉序号；新序号已在上方和 `protocol.distinguishing` 中写明依据的给号准则（1–4，D-057），只改参数的写进了 `variants` 而没有新开序号
- [ ] 只修改了本包写入范围内的文件（`paradigms/<本包族>/`、owner 为本包的 `knowledge/markers/`、`curation/work/pkg_<X>/`；D-029）
- [ ] `markers` 只使用 `curation/registry/paradigm_markers.csv` 中的 ID，或已在 `marker_requests.csv` 中申请
- [ ] 所有出处 `verified: false`（由审核人核实后改为 true）
- [ ] 查不到的字段已删除或留空，没有根据记忆或推测填写任何文献、DOI、数字
- [ ] 没有转引：每条出处都对照原文核对过
- [ ] 混合 BCI / 超扫描变体使用 `Hybrid:` / `Hyperscanning:` 前缀（D-022、D-021）
- [ ] 已更新本包 `status.csv`、`worklog.md`
- [ ] 提交已签署（`git commit -s`，DCO）

## 审核人 / Reviewer

- 交叉审核包 / Cross-review package：<A 审 B，B 审 C，C 审 D，D 审 E，E 审 A>
- [ ] 审核人已对照原文核实源头文献与描述
