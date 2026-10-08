<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## ERR-TS-002 Two-stage task with deterministic transitions — 书目核实 / bibliographic check

- 文件 / File：`paradigms/error/ERR-TS-002.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete ERR-TS-002 | corrected | Crossref | 10.1371/journal.pcbi.1005090 | pages added | — |

- 新 citation / New citation：Kool W, Cushman FA, Gershman SJ. When Does Model-Based Control Pay Off?. PLOS Computational Biology. 2016;12(8):e1005090.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
