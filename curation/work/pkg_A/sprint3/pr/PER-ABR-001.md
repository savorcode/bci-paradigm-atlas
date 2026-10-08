<!-- 草稿：curator_e（审核人），2026-10-05。sprint 3 书目核实（D-072，仅书目级；verified 保持 false）。 -->

## 内容 / Summary

- 文件 / File: `paradigms/perception/PER-ABR-001.yaml`
- 工作包 / Package: A
- 类型 / Kind: sprint 3 出处书目核实 / bibliographic verification

## 更正 / Corrections

| 条目 / Entity | 状态 / Status | 更正字段 / Fields | 匹配 DOI | 来源 / Source API | 说明 / Note |
|---|---|---|---|---|---|
| PER-ABR-001 | tbd_resolved | citation,doi,year | 10.1093/brain/94.4.681 | OpenAlex (works/doi; DOI candidate from curator memory, record title matched) | queries: Sohmer & Feinmesser 1967 (10.1177/000348946707600211) -> 429 not retried; Jewett & Williston 1971 -> record matched. Sohmer & Feinmesser 1967 (Ann Otol Rhinol Laryngol 76:427-435) is the earlier surface-electrode report named in R0856 and should be checked for priority |

## 自查 / Checklist

- [x] 只改了 first_source / variant source 的 citation、doi、year 与 notes 标签；其他字段未动
- [x] `verified: false` 保持不变
- [x] `python3 scripts/validate.py` 0 problem(s), 0 warning(s)
- [ ] 内容核实（对照原文）待维护者 / content verification pending
