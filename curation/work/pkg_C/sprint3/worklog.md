# 包 C sprint 3 审核人工作日志 / reviewer worklog（curator_b，2026-10-05）

任务：对包 C「错误监测与认知控制」（ERR、CTL 两族）的 127 条 first_source（73 条具体范式、2 条变体、52 条范式类）做**书目核实**（D-072 第一级）。内容核实未做，所有 `verified` 保持 false。

## 方法

- 有 DOI 的行：Crossref `works/<DOI>`；Crossref 429 时改用 OpenAlex `works/doi:<DOI>`（Eriksen 1974、Tom 2007、Dickinson 1984、Nieuwenhuis 2001 四条）。PubMed 文章页经 WebFetch 只返回空壳（JS 页面），不可用；PMID 一律沿用原条目，未新增。
- 无 DOI 的行：Crossref `query.bibliographic`（作者 + 题名关键词 + 年份），取前 3 条；仅当首条命中题名、第一作者、年份均吻合才写入 DOI 并改写 citation。
- citation 统一改写为 house style `Author AB, Author CD. Title. Journal. Year;Vol(Issue):Pages.`，字段**只取** Crossref/OpenAlex 记录；题名大小写按记录原样。记录只列第一作者的（Servan-Schreiber 1996、Bunge 2005，JAMA/OUP 旧记录），**保留原 citation 文本**，只补 DOI。
- 范式类条目不直接改 `paradigms/_classes.yaml`，写入 `class_updates.yaml`（fields.first_source 为整体替换；fields.notes.append 为追加句）。
- `check_status=corrected` 包含两类：真正的字段更正（见下）与"补全"（et al. 展开、补卷期页、补 DOI）；具体差异见 `sources_check.csv` 的 corrected_fields。
- Crossref `issued` 为在线日期而印刷卷年份不同的三条（Esterman 2012/2013、Bunge 2004/2005、Fink 2008/2009），`year` 取印刷卷年份并在 note 说明。

## 结果

| check_status | 条数 |
|---|---|
| confirmed | 10 |
| corrected | 94 |
| mismatch | 0 |
| not_found | 15 |
| tbd_resolved | 0 |
| tbd_open | 8 |
| 合计 | 127 |

按实体类型：class confirmed 4；class corrected 41；class not_found 6；class tbd_open 1；concrete confirmed 6；concrete corrected 51；concrete not_found 9；concrete tbd_open 7；variant corrected 2。

- 改动的 YAML 文件：57 个（具体范式与变体；含 10 条仅追加 notes 的 confirmed）。范式类更正 41 条写入 `class_updates.yaml`。
- **实质性更正**（非仅补全）：
  - CTL-AS-001: issue 11->10; pages added
  - CTL-DT-001: title; pages 1-35->1-36; doi added
  - CTL-FLK-001: issue 2->1; pages added
  - CTL-SW-001: title; pages added
  - CTL-TOL-001: venue (full journal title); pages added
  - CTL-WCST-001: volume ->38; doi added
  - ERR-ADAPT-002: authors added (Palidis DJ, Cashaback JGA, Gribble PL); year 2018 added; venue bioRxiv (preprint, posted 2018-02-09)
  - ERR-ERRP-002: title added (Learning From EEG Error-Related Potentials in Noninvasive Brain-Computer Interfaces); volume/issue/pages added
  - ERR-VRPE-001: venue (proceedings title); pages 427-437->1-11 (Crossref; 427 is the paper number); author initials Chen H-T->HT
- 值得注意：
  - CTL-WCST-001 卷号 34 → 38（1948 年 J Exp Psychol 第 38 卷）。
  - CTL-DT-001 题名 "response" → "responses"，页码 1-35 → 1-36。
  - CTL-FLK-001 期号 (2) → (1)（OpenAlex）。CTL-AS-001 期号 (11) → (10)。
  - CTL-SW-001 Crossref/APA 记录题名拼作 "predictible"，按记录照录。
  - ERR-VRPE-001 原引"pp. 427-437"实为 CHI 论文号 427；Crossref 页码 1-11。
  - ERR-ERRP-002、ERR-APC-001、ERR-ADAPT-002、CTL-MSIT-001 原缺题名或作者，已从记录补全（ERR-ADAPT-002 为 bioRxiv 预印本，Palidis, Cashaback & Gribble 2018）。
  - 无 mismatch：所有已核 DOI 均指向引文所述论文。
- **未能核实**（not_found，9 条具体范式 + 对应类）：CTL-MRP-001, CTL-WASON-001, ERR-ERRP-001, ERR-GAM-001, ERR-GAM-003, ERR-OBS-002, ERR-OBS-003, ERR-OGNG-001, ERR-PRT-001。原因：WebFetch 代理在约 85 次请求后持续返回 429（全局限流，等待 10 分钟以上仍被拒），书目检索未能执行；**不是** Crossref 无记录。YAML 未改，notes 未加句。计划的检索词见 CSV note，交维护者或下一轮执行。其中 ERR-GAM-003 / ERR-OBS-002 / ERR-OBS-003 只有"作者 年份，转引自 R0714"，须先对照 R0714 的参考文献表确定篇目。
- **TBD**（tbd_open，7 条 + 类 ERR-AAF）：CTL-FLK-002, CTL-SIM-002, CTL-STR-002, CTL-SW-003, ERR-AAF-001, ERR-ERRP-003, ERR-GAM-002。同样因限流未检索；每条在 CSV note 中列出 3 条候选检索（按 D-031 口径：任务程序最早描述，不取综述/指南）。无 tbd_resolved。

## 取数统计

见 `fetch_log.md`：共 83 次请求（Crossref DOI 43 次成功 / 4 次 429；Crossref 书目检索 12 次成功 / 11 次 429 / 2 次 403（URL 过长）/ 3 次查询被截断返回无关结果；OpenAlex 4 次成功 / 2 次 429；PubMed 页面 1 次空页；Europe PMC 1 次 429）。限流经验：Crossref 并发 >6 即 429；代理对 WebFetch 总量另有限额，约 75 次后每次请求需间隔 ≥8 分钟；`query.bibliographic` 查询串超过约 90 字符会被截断而返回无关结果（见日志中 3 次"irrelevant hits"）。

## 过程文件

- `sources_check.csv`、`class_updates.yaml`、`fetch_log.md`、`pr/<ID>.md`（57 个改动文件各一份）。
- 校验：`python3 scripts/validate.py` → 0 problem(s), 0 warning(s)。
