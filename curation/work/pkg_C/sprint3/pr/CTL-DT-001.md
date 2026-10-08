<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## CTL-DT-001 Dual-task / PRP — 书目核实 / bibliographic check

- 文件 / File：`paradigms/control/CTL-DT-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete CTL-DT-001 | corrected | Crossref-search | 10.1037/h0073262 | title; pages 1-35->1-36; doi added | — |

- 新 citation / New citation：Telford CW. The refractory phase of voluntary and associative responses. Journal of Experimental Psychology. 1931;14(1):1-36.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
