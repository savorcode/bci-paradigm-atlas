<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## CTL-CPT-002 AX continuous performance task (AX-CPT) — 书目核实 / bibliographic check

- 文件 / File：`paradigms/control/CTL-CPT-002.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete CTL-CPT-002 | confirmed | Crossref | 10.1001/archpsyc.1996.01830120037008 | — | Crossref record lists only the first author and only the first page (JAMA legacy record); title, first author, year, venue, 53(12):1105 agree; citation text kept. |

- 新 citation / New citation：Servan-Schreiber D, Cohen JD, Steingard S. Schizophrenic deficits in the processing of context: a test of a theoretical model. Archives of General Psychiatry 53(12): 1105-1112. 1996.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
