# 检索记录（Search protocol）

> 本文件记录候选范式清单与文献线索的来源，供论文方法部分（PRISMA-ScR 流程图）引用。每次新增检索请在末尾追加一条。

## S-001 · 2026-10-02 · 初始收集（管理者批量收集）

**执行方式**：由 Claude 作为管理者统一收集，分 4 路并行检索；之后用 HED 任务目录和 Wikipedia 参考文献补充；最后汇总去重。

**计划使用但不可访问的来源**（本次环境的网络策略拦截或限流）：
- Google Scholar（拦截）
- OpenAlex、Crossref、Semantic Scholar、PubMed E-utilities API（拦截或返回 429）
- Cognitive Atlas API、OpenNeuro GraphQL（拦截）
- PubMed / PMC 网页（多数返回 429 或验证码）

> 以上来源需在正式检索（S-002 起）中由策展人用浏览器补检。

**实际使用的来源**

| 渠道 | 方式 | 规模 | 贡献 |
|---|---|---|---|
| 网页检索（web_search） | 每个范式 1–3 次检索，检索式形如 `<英文名> review EEG`、`<英文名> paradigm original`、`<英文名> BCI dataset`；命中结果以 PubMed、PMC、出版社页面和 arXiv 为主 | 约 200 次检索（会话配额上限） | 398 条范式-文献关联 |
| HED 任务目录（hed_catalog） | 逐页读取 https://www.hedtags.org/hed-task/tasks/ 全部 105 个任务页的参考文献（含作者、年份、期刊、DOI、PMID） | 105 页 | 656 条关联；新增候选范式约 40 个 |
| Wikipedia 参考文献（wikipedia） | 针对仍缺文献的 37 个范式，读取对应词条的参考文献列表 | 37 页（31 页成功） | 137 条关联 |
| 管理者整理 | 依据 12 个范式族逐族列举候选，并对照 HED 目录补漏 | — | 156 个初始候选 |

**结果**
- 候选范式：209 个（12 个范式族，5 个工作包）
- 文献线索：1,073 条（去重后），其中有 DOI 757 条、有 PMID 779 条
- 范式-文献关联：1,100 条
- 没有任何文献线索的范式：12 个
- 判定建议：并入其他范式 7 个，排除 2 个，其余待例会确认

**去重规则**：先按 DOI 合并；没有 DOI 的按 PMID、PMCID 合并；再按规范化后的标题（前 90 个字母数字字符）合并。

**已知局限**
1. 所有文献均未核实（`verified=false`）。HED 页面和 Wikipedia 属于二手来源，已发现个别 DOI 与文献不符（例如 HED n-back 页中 Jonides 1997 的 DOI 指向 1998 年的文章）。
2. 网页检索结果常常不显示作者和年份，这些字段留空，需要策展人补齐。
3. 「检索线索（模型记忆）」字段由检索代理根据记忆写出，**没有经过检索确认**，只能作为下一步检索的关键词，不能作为出处。
4. 基于 HED 目录的范式偏向行为与认知任务；BCI 专用范式主要来自网页检索，覆盖度较低，需在 S-002 中重点补检。

## S-002 · 2026-10-03 · 第一遍骨架冲刺（sprint 1）策展人检索

- **执行人**：curator_a – curator_e（各自在本包分支上检索），维护者汇总（2026-10-03，合并后）。
- **原始记录**：`curation/work/pkg_<X>/search_log.md`（逐次检索/抓取）、`curation/work/pkg_D/new_leads.csv`（DN01–DN46）、包 E worklog 中的 S01–S28 书目表。
- **工具**：会话内 WebSearch（每包配额 30 次，结果只含标题与 URL）与 WebFetch（打开结果页核对书目）。没有使用 Google Scholar、IEEE Xplore、Scopus 等需要登录或交互的数据库。
- **目的**：(1) 为缺源头的已收录候选补 first_source；(2) 为读综述时发现的遗漏范式找线索（新候选）；(3) 为并入候选的变体找出处。

**按包统计**

| 包 | WebSearch | WebFetch | 被拒绝/不可用的抓取 | 被拒绝的来源 | 新候选 | 由检索补得的 first_source |
|---|---|---|---|---|---|---|
| A 感知与稳态 | 28 | 20 | 4 | PubMed 检索页（403）、NCBI E-utilities（robots.txt）、Europe PMC REST（429）；PubMed 组合检索页无结果 | 18 | 11 |
| B 运动、想象与刺激 | 30 | 42 | 7 | PubMed（429）、E-utilities（robots）、Crossref 检索接口（429）、journals.physiology.org（403）、PMC（验证码） | 17 | 27 |
| C 错误监测与认知控制 | 25 | 30 | 4 | PMC（reCAPTCHA）、PubMed、E-utilities | 17 | 21 |
| D 记忆与语言 | 30 | 19 | 4 | PMC 与 PubMed 文章页（reCAPTCHA） | 17 | 17 |
| E 情绪、社会与脑状态 | 30 | 29（含 2 次失败） | 2 | PubMed 检索页（429）、E-utilities（robots） | 16 | 26 |
| **合计** | **143** | **140** | **21** | — | **85** | **102** |

> 说明："由检索补得的 first_source"按各包 `status.csv` 中 `first_source_ref` 不是 R 编号（`search`）且不是 TBD 的条目计数，含新候选。被拒绝的抓取均按规则**未重试**。

**结果**
- 新增文献线索 **171 条**（R1095 – R1265，`found_via=curator_search`），来源：检索所得 first_source 102 个条目（去重后）、5 个包 `new_candidates.csv` 的线索列、包 D `new_leads.csv` 46 条。去重规则同 S-001（DOI → PMID → 规范化题名前 70 字符）。
- 新增范式–文献关联 172 条；改配错配线索 8 条（D-055）。合并后 `literature.csv` 共 1,244 条，`paradigm_literature.csv` 共 1,271 条。
- 新候选 85 个（C210 – C294）：收录 81、并入 4（D-034、D-035、D-044）。
- 仍为 TBD 的 first_source：37 个（A 27、C 1、D 7、E 2）。

**已知局限**
1. WebSearch 只返回标题与 URL，作者、年份常常只能从 URL 片段、机构库或第三方页面得到；约 43% 的新增线索没有作者字段，部分只有题名。题名中的截断（"…"）原样保留。
2. 二手来源（Wikipedia 参考文献表、他文参考文献、任务网站）得到的书目已在 `qa_flag` 中标为 `secondhand`（CTL-DT-001、CTL-RAVEN-001、IMG-OLF-001 的源头等），必须核原文。
3. PubMed / PMC / Europe PMC 普遍不可用，是 TBD 无法消除的主要原因（D-032）。
4. 由于配额按包均分，A 包（59 个条目、27 个 TBD）的检索强度明显不足。

## S-003 · 2026-10-03 · 第二冲刺（sprint 2）策展人检索：具体范式拆分

- **执行人**：curator_a – curator_e（各自在 `sprint2/pkg-<X>` 分支上检索），维护者汇总（2026-10-03，合并后）。
- **原始记录**：`curation/work/pkg_<X>/sprint2/search_log.md`（逐次检索/抓取；B 另附线索表 S2B-L01 – L17）、`curation/work/pkg_D/new_leads.csv`（DN47 – DN53）、各文件 `notes`。
- **工具**：会话内 WebSearch（每包上限 12 次）与 WebFetch；A、E 各有 1 次 `curl` 尝试（代理 403，未重试）。没有使用需要登录的数据库。
- **目的**：与 S-002 不同，本轮主要不是补源头，而是**为拆分出的具体范式找协议出处**：公开数据集页面（MOABB、BNCI Horizon 2020、BCI Competition、OpenNeuro/OpenfMRI、SEED、DEAP、ERP CORE）、HED 任务目录的变体表、任务网站（Millisecond、PsyToolkit、Cognitive Atlas），以及给新具体范式找 first_source。TBD 源头按 D-032 不在本轮集中处理。

**按包统计**

| 包 | WebSearch | WebFetch | 其他 | 被拒绝/不可用 | 主要来源 | 新登记文献 |
|---|---|---|---|---|---|---|
| A 感知与稳态 | 11 | 27 | curl 1 | 4（代理 403、PMC reCAPTCHA、跨站 302、robots） | MOABB 数据集页（SSVEP、c-VEP、P300）、Wikipedia P3a | 21 |
| B 运动、想象与刺激 | 7 | 23 | — | 2（PMC 302 → reCAPTCHA） | MOABB / BNCI（MI、ME、抓握、书写）、BCI Competition IV、作者 PDF | 21 |
| C 错误监测与认知控制 | 7 | 26 | — | 2（PubMed reCAPTCHA、OpenNeuro 空页面） | BNCI 013-2015、BCI Challenge @ NER 2015、HED 变体表、ERP CORE、机构库 | 14 |
| D 记忆与语言 | 7 | 8 | — | 1（PMC reCAPTCHA） | TU Berlin BibTeX（Shin 2018 数据集）、Wikipedia n-back、机构库、EvLab | 7 |
| E 情绪、社会与脑状态 | 12 | 8（含多 URL 行） | curl 1 | 7（二进制 PDF 2、验证码 3、重定向 1、代理 403 1） | DEAP、SEED 主页、机构库、Cognitive Atlas、Wikipedia | 15 |
| **合计** | **44** | **92** | **2** | **16** | — | **78** |

> 被拒绝的抓取均按规则**未重试**。"新登记文献"按 `literature.csv` 中 `found_via=curator_search_s2` 的行计数（R1266 – R1343）。

**结果**
- 支撑 138 个新具体范式（267 → 405）与 74 条范式类修改（D-071）。
- 新增文献线索 **78 条**（R1266 – R1343），来源：B 的 S2B-L01 – L17、C 的 S_SPULER2015 等 8 个临时编号（S_KELLY2013 与已有 R0578 重复，未新建）、D 的 DN47 – DN53、A / E 检索记录中"新增文献数 ≥1"的检索、以及文件 first_source / notes 中尚未登记的出处（含 sprint 1 线索 S06 与 WAY-EEG-GAL）。其中有 DOI 43 条、无作者 9 条；`qa_flag`：`title_placeholder` 10、`secondhand` 9、`weak_origin` 3、`behaviour_only` 1。R1093 补全书目（Proudfit 2015）。
- `paradigm_literature.csv` 新增 355 条关联（新线索 88、first_source 关联与 notes 中 R 编号的关联 267），共 1,626 条；`literature.csv` 共 1,322 条。
- first_source 为 TBD：具体范式 64 个（A 32、B 5、C 7、D 16、E 4），范式类 36 个。

**已知局限**
1. 数据集页面给出的是**数据集文献**，常常不是该配置的最早描述（D-066：`weak_origin`）；MOABB 摘要页被截断，BNCI2015_004 的类别列表两页矛盾（D-068）。
2. 多条书目只见题名或只有转引（R0714 中的 Bates 2005、Pavone 2016、Yeung 2004），作者由检索式或 URL 推断的已在 notes 注明。
3. PubMed / PMC 仍普遍返回验证码，Europe PMC 与 Crossref 接口经代理 403。

## S-004 · 2026-10-05 · 第三冲刺（sprint 3）出处书目核实（Crossref / OpenAlex 接口）

- **执行人**：交叉审核——A ← curator_e、B ← curator_a、C ← curator_b、D ← curator_c、E ← curator_d（各自在 `sprint3/pkg-<X>` 分支上）；维护者汇总（2026-10-07）。
- **原始记录**：`curation/work/pkg_<X>/sprint3/fetch_log.md`（逐次请求：接口、URL、结果）、`sources_check.csv`（逐条结果）；汇总 `curation/verification/sources_check.csv`（682 行）与 `curation/reports/verification_sprint3.md`。
- **工具**：只用 WebFetch 直接访问接口；**没有使用 WebSearch**。没有使用需要登录的数据库。
- **目的**：与 S-002 / S-003 不同，本轮不找新线索，而是把 `queue_pkg_<X>.csv` 中全部 first_source / 变体源（具体范式 404、变体 11、范式类 267）与权威记录逐条比对（D-072 书目核实），并为 TBD 行找书目可识别的源头候选。
- **端点**：Crossref REST `works/<DOI>`（主）、`works?query.bibliographic=`（检索，大部分 429）；OpenAlex `works/doi:<DOI>`、`works/pmid:<PMID>`（Crossref 429 时的回退，实际为主要来源之一）、`works?search=` / `filter=title.search`（全部 429）；PubMed 文章页（reCAPTCHA / 空页，弃用）；Europe PMC 1 次（429）。

**按包统计**（请求数按各包 fetch_log）

| 包 | 请求 | 其中被拒 / 失败 | 主要接口 | confirmed | corrected | tbd_resolved | tbd_open | not_found |
|---|---|---|---|---|---|---|---|---|
| A 感知与稳态 | 106 | 20（Crossref 429 含检索 4/4；OpenAlex 偶发 429） | OpenAlex works/doi、Crossref works/DOI | 56 | 30 | 57 | 2 | 5 |
| B 运动、想象与刺激 | 103 | 19（Crossref 429、URL 过长 403；OpenAlex 检索 6/6 429；PubMed reCAPTCHA） | OpenAlex works/doi、works/pmid | 39 | 83 | 5 | 0 | 6 |
| C 错误监测与认知控制 | 83 | 23（Crossref DOI 4、检索 11×429 + 2×403 + 3 次截断无关；OpenAlex 2；PubMed 空页 1；Europe PMC 1）；之后全局限流，15 行未检查 | Crossref works/DOI、Crossref 检索（12 次成功） | 10 | 94 | 0 | 8 | 15 |
| D 记忆与语言 | 112 | 29（Crossref 检索约每 2–4 分钟一次成功；OpenAlex 检索 4/4 429；PubMed reCAPTCHA） | Crossref works/DOI、OpenAlex works/pmid、候选 DOI 探针 | 17 | 94 | 21 | 2 | 3 |
| E 情绪、社会与脑状态 | 100 | 15（Crossref 429；PubMed 429；长查询串返回无关列表 4 次） | OpenAlex works/doi、works/pmid、Crossref works/DOI | 46 | 78 | 5 | 0 | 6 |
| **合计** | **504** | **106** | — | **168** | **379** | **88** | **12** | **35** |

> 被拒绝的 URL 均按规则**未重试**；同一文献改用另一接口。mismatch 0。`source_api` 列：OpenAlex 335、Crossref 322、无（未检查 / 无记录）25。

**结果**
- 682 条源中 93.1% 与权威记录一致或已按记录更正；TBD 源头 64 / 36 → 9 / 3（具体范式 / 范式类）。381 个具体范式文件、184 个类的 first_source 改动；全部 `verified: false`。
- 决议：D-072（两级核实）、D-073（凭记忆候选 DOI）已确认；D-074（遗留 47 行 → 第四冲刺）草案。

**已知局限**
1. 书目检索端点基本不可用，无 DOI 行多用"凭记忆候选 DOI → 取记录 → 题名/作者/年份一致才写入"（D-073，108 条已标注）。
2. PubMed 不可用，PMID 一律未核验。
3. 手册、指南、技术报告、学位论文、书章、会议摘要在 Crossref / OpenAlex 无记录（20 行）。
4. 书目核实不等于内容核实（D-072）；88 条 tbd_resolved 只是候选。

## S-005 · （计划）· 第四冲刺：遗留补源与内容核实
- 对象：D-074 的 47 行（包 C 15 行未检查；20 行无记录；12 行 TBD 开放）；88 条 tbd_resolved 候选与 108 条 D-073 条目的内容核实（优先 P1 核心类，D-066）；`literature.csv` 中有 `qa_flag` 的行；D-068 – D-070 的待核对项。
- 来源：机构数据库（Web of Science / Scopus / PsycINFO）、PubMed / Europe PMC（机构访问）、Crossref polite pool（mailto）或 OpenAlex API key、WorldCat / 出版社记录（手册与书章）、Zotero 群组库。
- 执行：维护者集中补源（D-032），策展人按交叉审核分工核原文；内容核实通过者才写 `verified: true`。
- 记录格式：同 S-004（接口、URL、结果），内容核实另记"读到的原文位置（页 / 节）"。
