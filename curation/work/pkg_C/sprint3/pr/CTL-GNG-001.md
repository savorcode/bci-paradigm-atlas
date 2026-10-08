<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## CTL-GNG-001 Go/NoGo task — 书目核实 / bibliographic check

- 文件 / File：`paradigms/control/CTL-GNG-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete CTL-GNG-001 | corrected | Crossref | 10.1016/0001-6918(69)90065-1 | pages added | Crossref record is the 1969 Acta Psychologica translation; the "(orig. 1868)" remark remains in the entry notes (Donders 1868/1969). |

- 新 citation / New citation：Donders FC. On the speed of mental processes. Acta Psychologica. 1969;30:412-431.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
