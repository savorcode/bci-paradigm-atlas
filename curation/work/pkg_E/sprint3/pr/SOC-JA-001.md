<!-- PR 描述草稿 · SOC-JA-001 · curator_d (reviewer, sprint 3) · 2026-10-05 -->

## 内容 / Summary

- 文件 / File：`paradigms/social/SOC-JA-001.yaml`
- 类型 / Kind：第三冲刺书目核实（D-072，仅书目级；`verified` 仍为 false）
- 更正的字段 / Fields corrected：
  - SOC-JA-001 — first_source: author order (Tognoli first, Kelso last), doi, year, issue added
  - variant 'Hyperscanning: cooperative interaction tasks recorded simultaneously from two brains' — source: doi, author, issue added
- 依据 / Source of record：见 `curation/work/pkg_E/sprint3/sources_check.csv` 与 `fetch_log.md`（Crossref / OpenAlex 记录）

- 备注 / Note：记录的作者顺序为 Tognoli, Lagarde, DeGuzman, Kelso（2007），原引文把 Kelso 列为第一作者且无年份，已按记录改正。超扫描变体的 Montague 2002 记录在 Crossref 与 OpenAlex 中都只列一位作者（Montague P），引文照记录写。

## 检查清单 / Checklist

- [x] 只改了 `first_source` / 变体 `source` 的书目字段与 `notes`；其他字段未动
- [x] 没有根据记忆填写字段：所有新字段来自取回的 Crossref / OpenAlex 记录
- [x] `verified: false` 保持不变
- [x] 本地 `python3 scripts/validate.py` 0 errors / 0 warnings
