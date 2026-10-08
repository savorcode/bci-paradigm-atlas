<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## ERR-PSEL-001 Probabilistic selection task — 书目核实 / bibliographic check

- 文件 / File：`paradigms/error/ERR-PSEL-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete ERR-PSEL-001 | corrected | Crossref | 10.1126/science.1102941 | pages added | — |

- 新 citation / New citation：Frank MJ, Seeberger LC, O'Reilly RC. By Carrot or by Stick: Cognitive Reinforcement Learning in Parkinsonism. Science. 2004;306(5703):1940-1943.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
