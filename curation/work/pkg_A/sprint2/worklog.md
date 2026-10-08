# 工作日志 · 包 A 感知与稳态 · sprint 2

> 每次工作追加一节（最新在下）。写：写了哪些 `protocol`、拆出了哪些具体范式（对应 `split_log.csv` 行）、保留了哪些变体及理由、`class_updates.yaml` 的改动、遇到的问题、待例会事项、跨包交接。

<!-- 模板
## YYYY-MM-DD · <策展人>
- protocol：
- 拆分 / 保留：
- class_updates：
- 核对线索：
- 问题 / 待例会：
- 交接给其他包：
-->

## 2026-10-03 · curator_a

- protocol：59 个 `-001` 全部写入 `protocol`（n_classes/classes/cue/stimulus_coding（适用时）/paradigm_timing/feedback/distinguishing）。44 个范式类只有一个真实配置，保留 `-001`，distinguishing 写"标准配置……本类暂无其他具体范式"。
- 拆分 / 保留（`split_log.csv` 共 97 行）：具体范式 59 → 89（+30）。
  - 9 个待复核变体：8 个按准则改为新具体范式（PER-MMN-002、PER-MVEP-002、PER-ODD-003、PER-ODD-004、SSR-SSSEP-002、SSR-SSVEP-002/-003/-004）；高频/不可见闪烁（D-004）保留为参数级变体，并从 SSR-SSVEP-001 移到 SSR-SSVEP-004（其出处是空间注意频率标记研究）。
  - `-001` 混合多配置而收窄的：PER-HBD（辨别 vs 计数）、PER-CUE（内源 vs 外源）、PER-OMIT（外部定时 vs 自发按键）、PER-RET（相位编码 vs pRF）、PER-MSI（McGurk vs 加性模型）、PER-BR（报告 vs 频率标记）、PER-CVA/SSR-ASSR/SSR-SSSEP/PER-MVEP（开环研究 vs BCI）、SSR-SSVEP-001（收窄为 Regan 1966 单刺激被动记录）、PER-ODD-001（收窄为两刺激 oddball，删去 RSVP 别名与 P3a 标记物，后者移到 -002）。
  - 新增（文献/公开数据集）：PER-ODD-002 三刺激、-005 RSVP 拼写（BNCI2015_010）、-006 棋盘格（Townsend 2010）、-007 单项闪烁（EPFLP300）、-008 AMUSE（BNCI2015_009）、-009 触觉 P300（Brouwer & van Erp 2010，解决 sprint 1 的 D-012 阻塞项）；PER-MMN-003 多特征；SSR-SSVEP-005 JFPM 40 目标、-006 JFPM 12 目标、-007 含静息类、-008 异步；SSR-CVEP-002 Gold 码、-003 burst 码；SSR-ASSR-002 ASSR BCI；SSR-FFR-002 语音 FFR；PER-CVA-002、PER-OMIT-002、PER-RET-002、PER-HBD-002、PER-CUE-002、PER-MSI-002、PER-BR-002。
  - 只记提议、未建文件（split_log 状态"提议/待例会"）：PER-MVEP 视网膜位置编码 mVEP（R0836）、PER-BR 歧义图形、PER-MASK 元对比、PER-NAT 静态自然图像、SSR-FPVS 面孔身份 vs 类别、SSR-SWEEP 对比度扫描、PER-AEP（D-041）。
- class_updates：15 个范式类（别名并集；PER-ODD、SSR-SSVEP、SSR-CVEP 改写为类级描述）。无新范式类、无新标记物。
- 核对线索：见各文件 notes 与 `search_log.md`（S2A01–S2A39；WebSearch 11 次）。
- TBD first_source（新文件）：SSR-SSVEP-008、SSR-FFR-002、PER-CVA-002、PER-MSI-002、PER-BR-002；另有 sprint 1 遗留 TBD 的 `-001` 未改。
- 问题 / 待例会：
  1. SSR-SSVEP 的类源头：临床光驱动（-003）早于 Regan 1966，`-001`/类源头是否改由光驱动承担（D-031）。
  2. 准则 1 的粒度：SSR-SSVEP-005（40 目标）与 -006（12 目标）同为 JFPM，只因目标集不同而分号；-007 仅多一个静息类。若例会认为目标数属于参数，可把 -006/-007 降为变体（序号不复用）。
  3. 若干新文件的 first_source 是数据集文献而非最早文献（PER-ODD-008 AMUSE、SSR-SSVEP-006、SSR-SSSEP-002 为综述）；PER-ODD-002 对 Squires et al. 1975 的归属仅依据 Wikipedia；PER-CUE-002 与 -001 共用 Posner 1980；PER-MMN-003、SSR-SSVEP-005 作者未在所读页面出现。
  4. PER-FACE-001 的 fMRI 组块定位器与 ERP 事件相关设计是否应按准则 3 分号，第二遍再定。
- 交接给其他包：无（MK.oscillatory_entrainment 的说明见 sprint 1）。
