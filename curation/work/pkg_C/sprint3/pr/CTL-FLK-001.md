<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## CTL-FLK-001 Eriksen flanker task (letter version) — 书目核实 / bibliographic check

- 文件 / File：`paradigms/control/CTL-FLK-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete CTL-FLK-001 | corrected | OpenAlex | 10.3758/bf03203267 | issue 2->1; pages added | — |

- 新 citation / New citation：Eriksen BA, Eriksen CW. Effects of noise letters upon the identification of a target letter in a nonsearch task. Perception & Psychophysics. 1974;16(1):143-149.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
