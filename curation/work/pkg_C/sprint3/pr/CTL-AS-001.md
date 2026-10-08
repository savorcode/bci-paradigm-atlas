<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## CTL-AS-001 Antisaccade task — 书目核实 / bibliographic check

- 文件 / File：`paradigms/control/CTL-AS-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete CTL-AS-001 | corrected | Crossref | 10.1016/0042-6989(78)90218-3 | issue 11->10; pages added | — |
| variant:CTL-AS-001 Internationally standardised antisaccade protocol  | corrected | Crossref | 10.1016/j.visres.2013.02.007 | authors (et al. expanded); pages added | — |

- 新 citation / New citation：Hallett PE. Primary and secondary saccades to goals defined by instructions. Vision Research. 1978;18(10):1279-1296.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
