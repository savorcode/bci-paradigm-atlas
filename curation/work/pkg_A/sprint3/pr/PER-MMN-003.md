<!-- 草稿：curator_e（审核人），2026-10-05。sprint 3 书目核实（D-072，仅书目级；verified 保持 false）。 -->

## 内容 / Summary

- 文件 / File: `paradigms/perception/PER-MMN-003.yaml`
- 工作包 / Package: A
- 类型 / Kind: sprint 3 出处书目核实 / bibliographic verification

## 更正 / Corrections

| 条目 / Entity | 状态 / Status | 更正字段 / Fields | 匹配 DOI | 来源 / Source API | 说明 / Note |
|---|---|---|---|---|---|
| PER-MMN-003 | corrected | citation,doi | 10.1016/j.clinph.2003.04.001 | OpenAlex (works/pmid, fallback; PubMed reCAPTCHA) | authors, 115(1):140-144 and DOI added (via PMID 14706481). Year kept 2004 = print issue 115(1) Jan 2004; OpenAlex lists online date 2003-12-04 |

## 自查 / Checklist

- [x] 只改了 first_source / variant source 的 citation、doi、year 与 notes 标签；其他字段未动
- [x] `verified: false` 保持不变
- [x] `python3 scripts/validate.py` 0 problem(s), 0 warning(s)
- [ ] 内容核实（对照原文）待维护者 / content verification pending
