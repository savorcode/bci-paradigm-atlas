<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## CTL-SW-001 Task switching (alternating runs) — 书目核实 / bibliographic check

- 文件 / File：`paradigms/control/CTL-SW-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete CTL-SW-001 | corrected | Crossref | 10.1037/0096-3445.124.2.207 | title; pages added | Crossref/APA title spelling "predictible" (as in the record) replaces "predictable". |

- 新 citation / New citation：Rogers RD, Monsell S. Costs of a predictible switch between simple cognitive tasks. Journal of Experimental Psychology: General. 1995;124(2):207-231.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
