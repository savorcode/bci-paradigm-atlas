# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres to [Semantic Versioning](https://semver.org).

本文件记录项目的重要变更，格式参考 Keep a Changelog，版本号遵循语义化版本。

## [Unreleased]

## [0.1.0] - 2026-10-08

First feature release after v0.0.1. The three seed paradigms grow into an atlas covering all 12 paradigm families, with two-level paradigm identifiers (schema 0.2) and a reproducible `protocol` for every concrete paradigm. Counts: 267 paradigm classes, 405 concrete paradigm files (404 active, 1 deprecated; all active ones with `protocol`), 129 markers, 294 candidates, 1,322 literature leads, 1,626 paradigm–literature links. All 682 first sources (404 concrete paradigms, 267 classes, 11 variants) were checked against Crossref/OpenAlex: 168 confirmed, 379 corrected, 88 TBD resolved, 12 TBD open, 35 not found, 0 mismatches; first sources TBD: 9 concrete paradigms, 3 classes. Content verification against the full text has not been done yet, so `verified: true` is 0 and every entry is `draft`. Identifier meanings are frozen from this release (D-063). The work was organised internally in three milestones: M1 first-pass skeletons (2026-10-03), M2 two-level identifiers and protocols (2026-10-05), M3 bibliographic verification (2026-10-07). Release notes: `curation/reports/release_v0.1.0.md`.
v0.0.1 之后的第一个功能版本。3 个种子范式扩展为覆盖全部 12 个范式族的图谱，采用两级范式标识符（schema 0.2），每个具体范式都有可复现的 `protocol`。数量：范式类 267、具体范式文件 405（有效 404、作废 1；有效者全部有 `protocol`）、标记物 129、候选 294、文献线索 1,322、范式–文献关联 1,626。全部 682 条源头（404 个具体范式、267 个范式类、11 个变体）已与 Crossref / OpenAlex 比对：一致 168、更正 379、TBD 找到候选 88、TBD 仍开放 12、查不到 35、指向另一篇 0；first_source 为 TBD：具体范式 9、范式类 3。尚未对照原文做内容核实，`verified: true` 为 0，所有条目为 `draft`。自本版起标识符含义冻结（D-063）。工作在内部按三个里程碑组织：M1 第一遍骨架（2026-10-03）、M2 两级标识符与协议（2026-10-05）、M3 出处书目核实（2026-10-07）。发布说明见 `curation/reports/release_v0.1.0.md`。

### Added / 新增
- Paradigms: 264 first-pass entries from five curation packages plus STM-PBM-001 (267 classes across 12 families), then split into 405 concrete paradigms (138 new, e.g. MOT-MI-001…-011, PER-ODD-001…-009, SSR-SSVEP-001…-008), each with a `protocol` block (`n_classes`, `classes`, `cue`, `stimulus_coding`, `paradigm_timing`, `feedback`, `distinguishing`).
  范式：5 个工作包第一遍建成 264 个条目，另有维护者代建的 STM-PBM-001（12 个族共 267 个范式类）；随后拆分为 405 个具体范式（新增 138 个，如 MOT-MI-001…-011、PER-ODD-001…-009、SSR-SSVEP-001…-008），每个都有 `protocol` 块。
- Schema 0.2: `schema/paradigm_class.schema.json` and the class registry `paradigms/_classes.yaml` (267 classes); required `class` and optional `protocol` in `paradigm.schema.json`.
  schema 0.2：新增范式类 schema 与登记表 `paradigms/_classes.yaml`（267 个范式类）；范式 schema 新增必填 `class` 与可选 `protocol`。
- Markers: descriptions for 107 marker skeletons and 18 newly requested markers (e.g. MK.vMMN, MK.MLR, MK.Pd, MK.intermodulation, MK.subthalamic_beta, MK.BOLD_left_IFG); 129 markers in total.
  标记物：为 107 个骨架编写描述，新增 18 个申请的标记物（如 MK.vMMN、MK.MLR、MK.Pd、MK.intermodulation、MK.subthalamic_beta、MK.BOLD_left_IFG）；共 129 个。
- Curation records: 85 curator-proposed candidates (C210–C294); 249 curator-search literature leads (R1095–R1343) with a `qa_flag` column (D-055); `curation/registry/concrete_paradigms.csv`; class-level columns in `candidates.csv`, `markers.csv` and `paradigm_markers.csv`.
  策展记录：策展人提出的候选 85 个（C210–C294）；策展人检索线索 249 条（R1095–R1343），新增 `qa_flag` 列（D-055）；具体范式登记表 `concrete_paradigms.csv`；`candidates.csv`、`markers.csv`、`paradigm_markers.csv` 增加范式类层级的列。
- Source verification: `curation/verification/sources_check.csv` (682 rows) and per-package process files (`curation/work/pkg_<X>/sprint3/`); notes phrases `bibliography confirmed|corrected (<API>, <date>)` (635 entries) and `origin candidate recalled, record confirmed via <API>` (108 entries).
  出处核实：结果表 `sources_check.csv`（682 行）与各包过程文件；notes 固定短语 `bibliography confirmed|corrected (<API>, <date>)`（635 条）与 `origin candidate recalled, record confirmed via <API>`（108 条）。
- Draft stimulus-modality terms `pharmacological` and `optical_stimulation` (D-045, D-046), pending confirmation.
  刺激模态草案词条 `pharmacological`（药物给予）与 `optical_stimulation`（组织光刺激），待例会确认。
- Scripts: `coverage_report.py` (Markdown coverage report), `check_siblings.py` (compares the concrete paradigms of each class on numbering criteria 1–4; 0 duplicates, 35 pairs to review), `verification_report.py` (bibliographic verification summary), `build_overview.py` (Excel overview; needs the optional `openpyxl`).
  脚本：覆盖度报告、兄弟差异检查（0 对完全相同，35 对待复核）、出处核实汇总、Excel 总览（需可选依赖 openpyxl）。
- Reports in `curation/reports/`: release notes `release_v0.1.0.md`, coverage `coverage_v0.1.0.md` (with milestone snapshots `coverage_M1.md`, `coverage_M2-start.md`, `coverage_M2.md`, `coverage_M3.md`), QA and sprint reports, `verification_sprint3.md`, and the Excel overview `BCI范式图谱_v0.1.0_总览.xlsx`; search records S-002 – S-004 and the S-005 plan in `curation/search_protocol.md`.
  `curation/reports/` 下的报告：发布说明、本版覆盖度（另附里程碑快照）、QA 与冲刺总结、核实报告、Excel 总览；`search_protocol.md` 新增检索记录 S-002 – S-004 与 S-005 计划。

### Changed / 变更
- Two-level identifiers (D-057): a paradigm class `<FAMILY>-<SHORT>` holds the shared mechanism (markers, constructs, origin); a concrete paradigm `<FAMILY>-<SHORT>-<NNN>` is one reproducible protocol. A new serial number is given when the class/condition set, stimulus or cue type (incl. coding), trial structure or feedback mode changes; `variants` are parameter-level only. All paradigm files migrated (added `class`); `schema_version` "0.2" for paradigms, markers and vocabularies. Methodology §1 and §6 rewritten (en/zh) with an MI numbering example table; template, CONTRIBUTING, PR template and issue form updated.
  两级标识符（D-057）：范式类记录共同机制，具体范式是一个可复现协议；类别/条件集、刺激或提示类型（含编码）、试次结构、反馈方式任一改变即取新序号，`variants` 只记参数级变化。全部范式文件迁移（加 `class`）；`schema_version` 改为 "0.2"。方法说明 §1、§6 中英文重写并加 MI 给号示例表；模板、贡献指南、PR 模板与 Issue 表单同步更新。
- First sources: 379 bibliographic corrections (DOI added 184, pages 178, issue 116, year 106, authors 93, volume 92; e.g. CTL-WCST-001 volume 34→38, STA-HYPN-001 first author Spiegel→Jiang, STA-MED-001 1973 reprint→1966 original) and 88 TBD origins resolved (e.g. PER-ABR-001 Jewett & Williston 1971, STA-SCP-001 Elbert et al. 1980); class origins of MEM-TMR, STA-NF, SOC-CYB and EMO-THREAT changed; 328 class updates from the packages applied to `paradigms/_classes.yaml` (descriptions generalised, marker unions, aliases, four classes renamed). Methodology §3 defines the two verification levels.
  源头：书目更正 379 条（补 DOI 184、页码 178、期号 116、年份 106、作者 93、卷 92；如 CTL-WCST-001 卷 34→38、STA-HYPN-001 第一作者、STA-MED-001 1973 重印本→1966 原文），TBD 找到候选 88 条；MEM-TMR、STA-NF、SOC-CYB、EMO-THREAT 的类源头变更；`_classes.yaml` 合入各包 328 条修改（描述泛化、标记物并集、别名、4 个类改名）。方法说明 §3 加两级核实定义。
- Cross-package duplicates merged (STM-CLAS-001 → STA-CLAS-001, SOC-CIT-001 → MEM-CIT-001, IMG-WORD-001 → LAN-VF-001 variant; D-034 – D-036); SSR-SSVEP-006 deprecated into SSR-SSVEP-005 (D-058); retired IDs are not reused. Seed entries enriched with merged-candidate variants and aliases and rewritten in block YAML (D-054).
  合并跨包重复条目（D-034 – D-036）；SSR-SSVEP-006 作废并入 SSR-SSVEP-005（D-058）；作废 ID 不复用。种子条目补充并入候选的变体与别名，改为块状 YAML（D-054）。
- `candidates.csv` status vocabulary unified (D-033); 8 misassigned leads moved (D-055); PET added to six hemodynamic markers (D-050); registries (`markers.csv` `used_by`, `paradigm_markers.csv`) regenerated from the files.
  `candidates.csv` 状态取值统一（D-033）；8 条错配线索改配（D-055）；6 个血流动力学标记物加入 PET（D-050）；登记表改为从文件重新生成。
- `validate.py` checks the class registry and fails when a class's markers are not a superset of its concrete paradigms' markers; `build_graph.py` adds `paradigm_class` nodes and `instance_of` edges (811 nodes, 1,435 edges); `check_siblings.py`, `build_graph.py` and `coverage_report.py` skip `status: deprecated` entries.
  校验脚本检查范式类登记表，并以错误级检查"类标记物 ⊇ 具体范式标记物"；图谱导出增加范式类节点与 `instance_of` 边（811 节点、1,435 边）；兄弟检查、图谱导出与覆盖度报告跳过作废条目。

### Fixed / 修正
- Chinese bold text that CommonMark renderers showed as raw `**…**` (17 places): full-width punctuation moved outside the bold span.
  中文加粗在 CommonMark 渲染器中显示为原始 `**…**`（17 处）：全角标点移到加粗外。
- All CSV files start with a UTF-8 BOM so that Excel on Windows shows Chinese correctly; scripts read CSV as `utf-8-sig`.
  全部 CSV 文件加 UTF-8 BOM，Windows 版 Excel 中文不再乱码；脚本以 `utf-8-sig` 读取。
- D-057 numbering example corrected to the actual files (MOT-MI-003 = Ofner et al. 2017, MOT-MI-011 = Jeong et al. 2020; D-067); outdated notes and distinguishing texts found in QA corrected.
  更正 D-057 给号示例（D-067）；QA 中发现的过时 notes 与 distinguishing 已修正。

### Decisions / 决议
- Confirmed: D-057 (two-level identifiers), D-058 (number of homogeneous targets is a parameter; adding/removing a rest class is criterion 1), D-061 (concrete-paradigm markers are those documented; `marker inherited from class`, `stand-in marker`; class markers = union), D-062 (class origin = earliest bibliographically identifiable original study; `-001` = canonical configuration, never renumbered), D-063 (identifier meanings frozen from v0.1.0; IMG-MA-001/-002 not swapped; STA-SCP-001 redefinition accepted), D-072 (two-level source verification: bibliographic vs content; only content verification sets `verified: true`), D-073 (recalled DOI candidates allowed as query keys when the fetched record matches).
  已确认：D-057（两级标识符）、D-058（同质目标个数是参数；增删静息类属准则 1）、D-061（具体范式写有文献记载的标记物；类标记物 = 并集）、D-062（类源头 = 最早的书目可识别原始研究；`-001` 为标准配置，永不改号）、D-063（标识符含义自 v0.1.0 起冻结；IMG-MA-001/-002 不对调；接受 STA-SCP-001 改义）、D-072（两级核实：书目 vs 内容，只有内容核实设 `verified: true`）、D-073（取回记录一致时允许以回忆的候选 DOI 作查询键）。
- Drafts pending the next meeting: D-001 – D-056 (candidate decisions, origin vs first neural recording, status vocabulary, boundaries, taxonomy, markers; those marked "executed" are already applied), D-059, D-060, D-064 – D-070, and D-074 (47 not-found / TBD-open rows deferred until institutional database access).
  待例会确认的草案：D-001 – D-056（标"已执行"者已落实到文件）、D-059、D-060、D-064 – D-070，以及 D-074（47 行查不到 / TBD 开放，待取得机构数据库访问后处理）。

## [0.0.1] - 2026-10-01

### Added
- First public statement of the BCI Paradigm Atlas and Paradigm Factory concepts by 思维刻度 SavorCode.
  思维刻度首次公开提出脑机范式图谱与范式工厂概念。
- Two-layer data model: paradigm catalog and neural knowledge base (markers, regions, constructs).
  双层数据模型：范式目录与神经知识库（标记物、脑区、认知构念）。
- JSON Schemas v0.1 for paradigms, markers and vocabularies.
  范式、标记物与词表的 JSON Schema v0.1。
- Controlled vocabularies: recording modality, stimulus modality, paradigm family, marker type, evidence grade.
  受控词表：记录模态、刺激模态、范式族、标记物类型、证据等级。
- Methodology: definitions, inclusion criteria, source rules, origin attribution and evidence grading.
  方法说明：定义、纳入标准、出处规则、源头认定与证据分级。
- Seed entries (draft): oddball, cued motor imagery and SSVEP paradigms; P3a, P3b, SMR ERD/ERS and SSVEP markers.
  种子条目（草案）：Oddball、提示性运动想象、SSVEP 范式；P3a、P3b、SMR ERD/ERS、SSVEP 标记物。
- Validation with cross-reference checks, knowledge graph export, and continuous integration.
  含交叉引用检查的校验、知识图谱导出与持续集成。
