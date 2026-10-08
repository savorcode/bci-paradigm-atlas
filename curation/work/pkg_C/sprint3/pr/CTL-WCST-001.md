<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## CTL-WCST-001 Wisconsin Card Sorting Test — 书目核实 / bibliographic check

- 文件 / File：`paradigms/control/CTL-WCST-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete CTL-WCST-001 | corrected | Crossref-search | 10.1037/h0059831 | volume ->38; doi added | — |

- 新 citation / New citation：Grant DA, Berg E. A behavioral analysis of degree of reinforcement and ease of shifting to new responses in a Weigl-type card-sorting problem. Journal of Experimental Psychology. 1948;38(4):404-411.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
