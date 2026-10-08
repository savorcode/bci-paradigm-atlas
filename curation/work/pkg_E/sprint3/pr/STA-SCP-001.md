<!-- PR 描述草稿 · STA-SCP-001 · curator_d (reviewer, sprint 3) · 2026-10-05 -->

## 内容 / Summary

- 文件 / File：`paradigms/state/STA-SCP-001.yaml`
- 类型 / Kind：第三冲刺书目核实（D-072，仅书目级；`verified` 仍为 false）
- 更正的字段 / Fields corrected：
  - STA-SCP-001 — first_source: first_source written (was TBD)
- 依据 / Source of record：见 `curation/work/pkg_E/sprint3/sources_check.csv` 与 `fetch_log.md`（Crossref / OpenAlex 记录）

- 备注 / Note：原为 TBD。Elbert, Rockstroh, Lutzenberger & Birbaumer 1980（EEG Clin Neurophysiol 48(3):293-301）为 SCP 操作性反馈的原始研究（notes 中原称"memory-only lead"），早于 1992 年记录 R1333/R1334；内容未核。状态 `tbd_resolved`。按 D-062，类源头 STA-SCP 本次未改（仍为 Birbaumer 1999，书目已确认），是否改为 1980 年研究由维护者决定。

## 检查清单 / Checklist

- [x] 只改了 `first_source` / 变体 `source` 的书目字段与 `notes`；其他字段未动
- [x] 没有根据记忆填写字段：所有新字段来自取回的 Crossref / OpenAlex 记录
- [x] `verified: false` 保持不变
- [x] 本地 `python3 scripts/validate.py` 0 errors / 0 warnings
