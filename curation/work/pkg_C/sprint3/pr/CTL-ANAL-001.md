<!-- PR draft, sprint 3 bibliographic verification, curator_b, 2026-10-05 -->

## CTL-ANAL-001 Analogical reasoning — 书目核实 / bibliographic check

- 文件 / File：`paradigms/control/CTL-ANAL-001.yaml`
- 级别 / Level：书目核实（D-072）；`verified` 保持 false，内容核实未做。

| 条目 / Entry | 状态 / Status | 来源 / API | DOI | 更正字段 / Fields corrected | 备注 / Note |
|---|---|---|---|---|---|
| concrete CTL-ANAL-001 | corrected | Crossref-search | 10.1093/cercor/bhh126 | pages added; doi added | Crossref record lists only the first author; citation text kept, DOI added. Crossref issued 2004 (online); print 15(3) 2005. Crossref issued 2004 = online; print vol 15(3) 2005 |

- 新 citation / New citation：Bunge SA, Wendelken C, Badre D, Wagner AD. Analogical reasoning and prefrontal cortex: evidence for separable retrieval and integration mechanisms. Cerebral Cortex. 2005.
- 自查 / Checklist：`python3 scripts/validate.py` 0 problem(s)；只改 `first_source`/变体 `source` 与 `notes`；未改 `verified`。
