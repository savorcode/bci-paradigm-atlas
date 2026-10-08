# curation/verification/ — 第三冲刺：出处核实

## 两级核实（D-072，已确认 2026-10-07；D-073 凭记忆候选 DOI 的处理；D-074 遗留清单）

| 级别 | 含义 | 由谁做 | 写入哪里 |
|---|---|---|---|
| **书目核实**（bibliographic） | 题名、作者、年份、期刊、卷期页、DOI/PMID 与 Crossref 或 PubMed 的权威记录一致，必要时更正 | 审核人（本冲刺），用 Crossref / OpenAlex / PubMed 接口 | `sources_check.csv`；YAML 字段更正；`notes` 加 `bibliography confirmed (Crossref, 2026-10-05)` |
| **内容核实**（content） | 对照原文全文，确认该文献确实描述了该范式/配置，且是最早的 | 维护者或审核人，需要全文访问 | `verified: true`（方法说明 §3 的含义不变） |

本冲刺只做**书目核实**，`verified` 仍为 false。书目核实通过不等于内容核实通过。

## 文件

- `queue_pkg_X.csv`：每个包要核的出处（具体范式、变体、范式类的 first_source）。
- `sources_check.csv`：核实结果（维护者汇总，682 行，2026-10-07）。列：entity_type（concrete / variant / class）, entity_id, variant_name（仅变体行）, pkg, pkg_reviewer, check_status, source_api, matched_doi, matched_pmid, corrected_fields, note, checker, date。凭记忆候选 DOI 的行 note 含 "D-073: candidate from memory, record confirmed by API"。汇总脚本：`scripts/verification_report.py`。
  - check_status 取值：`confirmed`（一致）、`corrected`（有字段更正）、`mismatch`（DOI/PMID 指向另一篇，需人工）、`not_found`（查不到）、`tbd_resolved`（原 TBD 已找到源头候选）、`tbd_open`（仍无源头）。
- 过程文件在 `curation/work/pkg_X/sprint3/`。

## 工具可达性（2026-10-05 测试）

| 来源 | 状态 |
|---|---|
| Crossref REST（按 DOI 取记录、按书目检索） | 可用 |
| OpenAlex（按 DOI 取记录） | 可用，偶尔 429 |
| PubMed 文章页（按 PMID） | 可用 |
| Google Scholar、PubMed E-utilities、Semantic Scholar | robots.txt 禁止 |
| 出版社全文（Elsevier、APA 等） | 多数被拒 |
