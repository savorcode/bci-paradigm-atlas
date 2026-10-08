<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## CTL-TOL-001 Tower of London — 书目核实 / bibliographic check

- 文件 / File：`paradigms/control/CTL-TOL-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete CTL-TOL-001 | corrected | Crossref | 10.1098/rstb.1982.0082 | venue (full journal title); pages added | — |

- 新 citation / New citation：Shallice T. Specific impairments of planning. Philosophical Transactions of the Royal Society of London. B, Biological Sciences. 1982;298(1089):199-209.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
