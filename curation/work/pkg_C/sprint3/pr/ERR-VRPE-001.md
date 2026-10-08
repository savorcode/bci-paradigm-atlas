<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## ERR-VRPE-001 Visuo-haptic mismatch in virtual reality — 书目核实 / bibliographic check

- 文件 / File：`paradigms/error/ERR-VRPE-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete ERR-VRPE-001 | corrected | Crossref | 10.1145/3290605.3300657 | venue (proceedings title); pages 427-437->1-11 (Crossref; 427 is the paper number); author initials Chen H-T->HT | — |
| variant:ERR-VRPE-001 EMS force-feedback condition (visual + vibrotactil | corrected | Crossref | 10.3389/fnrgo.2024.1411305 | pages added | — |

- 新 citation / New citation：Gehrke L, Akman S, Lopes P, Chen A, Singh AK, Chen HT, Lin CT, Gramann K. Detecting Visuo-Haptic Mismatches in Virtual Reality using the Prediction Error Negativity of Event-Related Brain Potentials. Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems. 2019:1-11.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
