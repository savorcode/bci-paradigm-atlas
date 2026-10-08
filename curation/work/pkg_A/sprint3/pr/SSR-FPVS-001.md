<!-- 草稿：curator_e（审核人），2026-10-05。sprint 3 书目核实（D-072，仅书目级；verified 保持 false）。 -->

## 内容 / Summary

- 文件 / File: `paradigms/steady_state/SSR-FPVS-001.yaml`
- 工作包 / Package: A
- 类型 / Kind: sprint 3 出处书目核实 / bibliographic verification

## 更正 / Corrections

| 条目 / Entity | 状态 / Status | 更正字段 / Fields | 匹配 DOI | 来源 / Source API | 说明 / Note |
|---|---|---|---|---|---|
| SSR-FPVS-001 | tbd_resolved | citation,doi,year | 10.1016/j.neuropsychologia.2013.10.022 | OpenAlex (works/doi; DOI candidate from curator memory, record title matched) | query: Liu-Shuang, Norcia & Rossion -> record matched (fast periodic oddball design). Year written 2014 = print volume 52; OpenAlex lists online 2013. Heinrich, Mell & Bach 2009 (Int J Psychophysiol) may be an earlier frequency-domain oddball - not fetched |

## 自查 / Checklist

- [x] 只改了 first_source / variant source 的 citation、doi、year 与 notes 标签；其他字段未动
- [x] `verified: false` 保持不变
- [x] `python3 scripts/validate.py` 0 problem(s), 0 warning(s)
- [ ] 内容核实（对照原文）待维护者 / content verification pending
