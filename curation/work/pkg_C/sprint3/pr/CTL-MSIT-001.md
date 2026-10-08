<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## CTL-MSIT-001 Multi-source interference task (MSIT) — 书目核实 / bibliographic check

- 文件 / File：`paradigms/control/CTL-MSIT-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete CTL-MSIT-001 | corrected | Crossref | 10.1038/sj.mp.4001217 | authors added (Bush G, Shin LM, Holmes J, Rosen BR, Vogt BA) | — |

- 新 citation / New citation：Bush G, Shin LM, Holmes J, Rosen BR, Vogt BA. The Multi-Source Interference Task: validation study with fMRI in individual subjects. Molecular Psychiatry. 2003;8(1):60-70.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
