# 工作日志 · 包 B 运动、想象与刺激 · sprint 3（出处书目核实）

> 审核人 curator_a（交叉审核：包 B 由另一位策展人撰写）。本冲刺只做书目级核实（D-072），`verified` 一律保持 false。

## 2026-10-05 · curator_a

- **队列**：`curation/verification/queue_pkg_B.csv` 133 行（具体范式 84、范式类 49；TBD 5）。去重后 82 篇不同文献（范式类的 first_source 与对应 -001 大多相同）。
- **抓取**：103 次 WebFetch（成功 84），见 `fetch_log.md`。未用 WebSearch；被拒 URL 不重试。
  - Crossref 按 DOI 与书目检索均频繁被代理以 429 拒绝；OpenAlex 的 `works/doi:` 与 `works/pmid:` 可用并成为主要来源；OpenAlex 列表检索（`?search=`）6 次全部 429；PubMed 文章页返回 reCAPTCHA。
  - 因检索接口不可用，无 DOI 的条目改为"按候选 DOI 取单条记录并逐项与引文比对"（题名、第一作者、年份、卷页一致才写入 DOI）；`sources_check.csv` 的 note 对每条都注明了这一点。
- **结果**（`sources_check.csv`，133 行）：
  | check_status | 具体范式 | 范式类 | 合计 |
  |---|---|---|---|
  | confirmed | 24 | 15 | 39 |
  | corrected | 52 | 31 | 83 |
  | tbd_resolved | 5 | — | 5 |
  | not_found | 3 | 3 | 6 |
  | mismatch | 0 | 0 | 0 |
- **YAML 改动**：81 个具体范式文件（52 更正 + 5 TBD 候选改写 first_source；24 仅在 notes 追加 `bibliography confirmed (...)`）。范式类 46 条写入 `class_updates.yaml`（未直接改 `_classes.yaml`）。`python3 scripts/validate.py`：0 problem(s), 0 warning(s)。
- **更正类型**：
  - 19 条"仅题名 + PMID"的记录（IMG-CMD-001/-002、IMG-SAO-002、MOT-ATT-001/-002、MOT-CURSOR-003、MOT-FORCE-001、MOT-GRASP-001/-002、MOT-ME-001/-002、MOT-MI-004、MOT-OBS-001、MOT-PURS-001、MOT-REACH-001、MOT-TRACK-001/-002、STM-GVS-001）补齐作者、期刊、年份、卷期页与 DOI。MOT-ME-001（Szurhaj et al. 2001）的 OpenAlex 记录无期刊名与 DOI，期刊暂缺，待 PubMed 可达时补。
  - 题名缺失的记录补题名：IMG-MA-002（Scherer et al. 2015）、MOT-HW-001（Willett et al. 2020 bioRxiv，Crossref 题名为 "via imagined handwriting"）、IMG-SPI-003（Zhao & Rudzicz 2015 ICASSP）、IMG-VIS-002（O'Craven & Kanwisher 2000）、STM-PBM-001（Wang et al. 2019）、STM-ADBS-001（Little et al. 2014 JoVE）、STM-TI-001（Violante et al. 2023）、MOT-GRASP-004（Luciw et al. 2014）。
  - 其余为补 DOI、补卷期页、展开 "et al."、作者拼写（Jäncke、Kamienkowski、Spies RD）。
- **年份口径**：OpenAlex 的 `publication_year` 常为在线年份；凡 YAML 已有印刷年份且卷期对应（MOT-PASS-001 2015、STM-PHTMS-001 2018、IMG-OLF-001 2005）保留原年份并在 note 说明；YAML 无年份时按印刷卷期写年份（IMG-SAO-002 2017、MOT-ATT-001 2007、MOT-GRASP-001 2012、MOT-GRASP-002 2016、MOT-MI-004 2009），note 注明 OpenAlex 年份。请维护者在 Crossref 可用时复核这 5 条的 `published-print`。
- **TBD（5 条，均 `tbd_resolved`，候选源头，内容未核）**：
  - MOT-MI-005 → Neuper, Schlögl & Pfurtscheller 1999 J Clin Neurophysiol（两类左/右手 MI + 连续反馈）；1993/1996 Graz 反馈研究为未核实的记忆线索。
  - MOT-MI-006 → Dornhege et al. 2004 IEEE TBME（BCI Competition III IVa 数据提供方）。
  - MOT-MI-009 → Blankertz et al. 2007 NeuroImage（BCI Competition IV ds1 数据提供方）；更早的异步 MI（Millán 2003、Scherer 2004、Mason & Birch 2000）为记忆线索。
  - MOT-ME-003 → Gwin et al. 2010 J Neurophysiol（跑步机行走高密度 EEG）。
  - MOT-REACH-002 → Waldert et al. 2008 J Neurosci（BCI Competition IV ds3 数据提供方）。
  - 三条数据提供方文献是否符合 D-031"任务程序最早描述"需内容核实；旧 TBD 原文已保留在 notes。
- **not_found（6 行 / 3 篇）**：
  - IMG-MA-001 / IMG-MA："A new mode of EEG based communication"（R0842，Monash 链接）无法解析；记忆线索 Keirn & Aunon 1990（doi 10.1109/10.64464）题名为 "A new mode of communication between man and his surroundings"，与 R0842 题名不同，**未写入**。依 D-063 R0842 只是范式类源头候选，请维护者裁定是否以 Keirn & Aunon 1990 替换。
  - MOT-SACC-001 / MOT-SACC：Javal 1878 无 Crossref 记录（占位，weak_origin，D-031）。
  - MOT-SMS-001 / MOT-SMS：FAU 博士论文未被索引。
- **需人工注意（非 mismatch 但值得看）**：
  - IMG-CMD-003：Crossref 检索首条是 NEJM 通信（362(20):1936-1938），非原文；已用原文 DOI 10.1056/NEJMoa0905370 的记录核对后写入。
  - MOT-HW-001：Crossref 题名含 "imagined"，原引文漏掉；同行评审版（Nature 2021，R0947）未抓取。
  - STM-ADBS-001：核到的是 JoVE 方法文章（2014），而非 Little et al. 2013 Ann Neurol 原始研究；D-031 源头问题待内容核实。
  - STM-PAS-001、IMG-AUD-002：Crossref/OpenAlex 记录只列第一作者，其余作者保留自原引文。
  - IMG-SPI-003：题名来自 ICASSP 2015 记录，与二手引文（Varshney & Khan 2022）描述的数据集对应关系仍需对照原文。
- **未做**：PubMed 页面不可达，`matched_pmid` 全空，未新增任何 `pmid`；未改 `_classes.yaml`；未改 `literature.csv`（新出现的 DOI/PMID 由维护者分配 R 编号）；contributors 未改。
- **提交**：按族各一提交（imagery、motor、stimulation）+ 过程文件一提交，见 `git log sprint3/pkg-B`。
