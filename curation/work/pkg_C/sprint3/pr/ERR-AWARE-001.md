<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## ERR-AWARE-001 Error awareness (choice task with accuracy judgements) — 书目核实 / bibliographic check

- 文件 / File：`paradigms/error/ERR-AWARE-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete ERR-AWARE-001 | corrected | Crossref | 10.1037/0096-1523.26.1.141 | pages 141-51->141-151 | — |

- 新 citation / New citation：Scheffers MK, Coles MGH. Performance monitoring in a confusing world: Error-related brain activity, judgments of response accuracy, and types of errors. Journal of Experimental Psychology: Human Perception and Performance. 2000;26(1):141-151.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
