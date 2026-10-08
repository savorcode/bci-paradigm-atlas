<!-- PR 描述草稿 · EMO-REG-002 · curator_d (reviewer, sprint 3) · 2026-10-05 -->

## 内容 / Summary

- 文件 / File：`paradigms/emotion/EMO-REG-002.yaml`
- 类型 / Kind：第三冲刺书目核实（D-072，仅书目级；`verified` 仍为 false）
- 更正的字段 / Fields corrected：
  - EMO-REG-002 — first_source: doi, authors, year, volume, issue, pages added
- 依据 / Source of record：见 `curation/work/pkg_E/sprint3/sources_check.csv` 与 `fetch_log.md`（Crossref / OpenAlex 记录）

- 备注 / Note：OpenAlex 出版年 2007（在线），卷期 63(6) 为 2008 年印刷卷，年份写 2008。

## 检查清单 / Checklist

- [x] 只改了 `first_source` / 变体 `source` 的书目字段与 `notes`；其他字段未动
- [x] 没有根据记忆填写字段：所有新字段来自取回的 Crossref / OpenAlex 记录
- [x] `verified: false` 保持不变
- [x] 本地 `python3 scripts/validate.py` 0 errors / 0 warnings
