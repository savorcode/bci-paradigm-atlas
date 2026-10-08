<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## CTL-CPT-001 Continuous performance test (X-CPT) — 书目核实 / bibliographic check

- 文件 / File：`paradigms/control/CTL-CPT-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete CTL-CPT-001 | corrected | Crossref | 10.1037/h0043220 | authors (et al. expanded); pages added | — |

- 新 citation / New citation：Rosvold HE, Mirsky AF, Sarason I, Bransome ED, Beck LH. A continuous performance test of brain damage. Journal of Consulting Psychology. 1956;20(5):343-350.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
