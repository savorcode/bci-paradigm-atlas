<!-- PR 描述草稿 · STA-HYPN-001 · curator_d (reviewer, sprint 3) · 2026-10-05 -->

## 内容 / Summary

- 文件 / File：`paradigms/state/STA-HYPN-001.yaml`
- 类型 / Kind：第三冲刺书目核实（D-072，仅书目级；`verified` 仍为 false）
- 更正的字段 / Fields corrected：
  - STA-HYPN-001 — first_source: first author (Jiang H, not Spiegel), author list expanded, doi added
- 依据 / Source of record：见 `curation/work/pkg_E/sprint3/sources_check.csv` 与 `fetch_log.md`（Crossref / OpenAlex 记录）

- 备注 / Note：记录的第一作者为 Jiang H（Spiegel D 为末位作者），原引文写 "Spiegel DR et al."，已改正。

## 检查清单 / Checklist

- [x] 只改了 `first_source` / 变体 `source` 的书目字段与 `notes`；其他字段未动
- [x] 没有根据记忆填写字段：所有新字段来自取回的 Crossref / OpenAlex 记录
- [x] `verified: false` 保持不变
- [x] 本地 `python3 scripts/validate.py` 0 errors / 0 warnings
