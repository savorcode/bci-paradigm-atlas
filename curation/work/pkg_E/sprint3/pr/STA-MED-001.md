<!-- PR 描述草稿 · STA-MED-001 · curator_d (reviewer, sprint 3) · 2026-10-05 -->

## 内容 / Summary

- 文件 / File：`paradigms/state/STA-MED-001.yaml`
- 类型 / Kind：第三冲刺书目核实（D-072，仅书目级；`verified` 仍为 false）
- 更正的字段 / Fields corrected：
  - STA-MED-001 — first_source: replaced 1973 reprint record with the 1966 original: authors (order Kasamatsu, Hirai), journal, year, volume, issue, pages, doi
- 依据 / Source of record：见 `curation/work/pkg_E/sprint3/sources_check.csv` 与 `fetch_log.md`（Crossref / OpenAlex 记录）

- 备注 / Note：这不是同一条记录的字段补全，而是用 1966 年原始论文（Kasamatsu & Hirai, Folia Psychiatr Neurol Jpn 20(4):315-336）替换了 1973 年在 J Am Inst Hypnosis 的转载记录（worklog 已标"1966 原文未核"）。作者顺序在原始记录中为 Kasamatsu, Hirai。请维护者确认此替换（D-031 第 1 款）。OpenAlex 记录的刊名字段显示现刊名 Psychiatry and Clinical Neurosciences，引文按 1966 年卷的刊名写。

## 检查清单 / Checklist

- [x] 只改了 `first_source` / 变体 `source` 的书目字段与 `notes`；其他字段未动
- [x] 没有根据记忆填写字段：所有新字段来自取回的 Crossref / OpenAlex 记录
- [x] `verified: false` 保持不变
- [x] 本地 `python3 scripts/validate.py` 0 errors / 0 warnings
