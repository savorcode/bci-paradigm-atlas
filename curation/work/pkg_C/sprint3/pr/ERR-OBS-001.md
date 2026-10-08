<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## ERR-OBS-001 Observation of errors (human performer, choice task) — 书目核实 / bibliographic check

- 文件 / File：`paradigms/error/ERR-OBS-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete ERR-OBS-001 | corrected | Crossref | 10.1038/nn1239 | authors (et al. expanded); pages added | — |

- 新 citation / New citation：van Schie HT, Mars RB, Coles MGH, Bekkering H. Modulation of activity in medial frontal and motor cortices during error observation. Nature Neuroscience. 2004;7(5):549-554.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
