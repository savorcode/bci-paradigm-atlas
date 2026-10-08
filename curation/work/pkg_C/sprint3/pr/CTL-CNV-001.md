<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## CTL-CNV-001 S1-S2 paradigm — 书目核实 / bibliographic check

- 文件 / File：`paradigms/control/CTL-CNV-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete CTL-CNV-001 | corrected | Crossref | 10.1038/203380a0 | authors (et al. expanded); pages added | — |

- 新 citation / New citation：Walter WG, Cooper R, Aldridge VJ, McCallum WC, Winter AL. Contingent Negative Variation: An Electric Sign of Sensori-Motor Association and Expectancy in the Human Brain. Nature. 1964;203(4943):380-384.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
