# 第三冲刺出处书目核实报告（verification_sprint3）

> 起草：维护者（maintainer），2026-10-07。对应里程碑 M3（`integration`）。
> 级别：**书目核实**（D-072）。`verified` 全部保持 false；内容核实（读原文）待第四冲刺。
> 原始材料：`curation/verification/sources_check.csv`（682 行，由五个包的 `curation/work/pkg_<X>/sprint3/sources_check.csv` 合并，加 `pkg_reviewer`）；各包 `fetch_log.md`、`worklog.md`、`class_updates.yaml`、`pr/`。
> 下列第 1–6 节由 `python3 scripts/verification_report.py` 生成（可随时重跑）；第 7–10 节为维护者说明。

## 0. 一句话结论

682 条源（具体范式 404、变体 11、范式类 267）中 **confirmed 168、corrected 379、tbd_resolved 88、tbd_open 12、not_found 35、mismatch 0**；即 93.1% 的源现在与 Crossref / OpenAlex 的权威记录一致或已按记录更正，原 64 个具体范式 / 36 个范式类的 TBD 源头降到 **9 / 3**。更正以**补全**为主（DOI 184、页码 178、期号 116、年份 106、作者 93、卷 92），真正的数值或归属错误约 10 处（见第 7 节）。381 个具体范式文件与 `_classes.yaml` 有改动。`verified: true` 计 0。

交叉审核分工：A ← curator_e、B ← curator_a、C ← curator_b、D ← curator_c、E ← curator_d。


来源：`curation/verification/sources_check.csv`（682 行）；图谱：405 个具体范式、267 个范式类。

## 1. 各包按 check_status 计数

| 包 | confirmed | corrected | tbd_resolved | tbd_open | not_found | mismatch | 合计 |
|---|---|---|---|---|---|---|---|
| A | 56 | 30 | 57 | 2 | 5 | 0 | 150 |
| B | 39 | 83 | 5 | 0 | 6 | 0 | 133 |
| C | 10 | 94 | 0 | 8 | 15 | 0 | 127 |
| D | 17 | 94 | 21 | 2 | 3 | 0 | 137 |
| E | 46 | 78 | 5 | 0 | 6 | 0 | 135 |
| 合计 | 168 | 379 | 88 | 12 | 35 | 0 | 682 |

## 2. 各包按实体类型与 check_status 计数

| 包 | 实体类型 | confirmed | corrected | tbd_resolved | tbd_open | not_found | mismatch | 合计 |
|---|---|---|---|---|---|---|---|---|
| A | concrete | 36 | 17 | 31 | 1 | 3 | 0 | 88 |
| A | variant | 1 | 2 | 0 | 0 | 0 | 0 | 3 |
| A | class | 19 | 11 | 26 | 1 | 2 | 0 | 59 |
| B | concrete | 24 | 52 | 5 | 0 | 3 | 0 | 84 |
| B | class | 15 | 31 | 0 | 0 | 3 | 0 | 49 |
| C | concrete | 6 | 51 | 0 | 7 | 9 | 0 | 73 |
| C | variant | 0 | 2 | 0 | 0 | 0 | 0 | 2 |
| C | class | 4 | 41 | 0 | 1 | 6 | 0 | 52 |
| D | concrete | 10 | 55 | 15 | 1 | 2 | 0 | 83 |
| D | variant | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| D | class | 7 | 38 | 6 | 1 | 1 | 0 | 53 |
| E | concrete | 25 | 43 | 4 | 0 | 4 | 0 | 76 |
| E | variant | 0 | 5 | 0 | 0 | 0 | 0 | 5 |
| E | class | 21 | 30 | 1 | 0 | 2 | 0 | 54 |
| 合计 | concrete | 101 | 218 | 55 | 9 | 21 | 0 | 404 |
| 合计 | variant | 1 | 10 | 0 | 0 | 0 | 0 | 11 |
| 合计 | class | 66 | 151 | 33 | 3 | 14 | 0 | 267 |

## 3. 图谱中仍为 TBD 的 first_source

具体范式 9 个，范式类 3 个。

| 实体类型 | ID | sources_check 状态 |
|---|---|---|
| concrete | CTL-FLK-002 | tbd_open |
| concrete | CTL-SIM-002 | tbd_open |
| concrete | CTL-STR-002 | tbd_open |
| concrete | CTL-SW-003 | tbd_open |
| concrete | ERR-AAF-001 | tbd_open |
| concrete | ERR-ERRP-003 | tbd_open |
| concrete | ERR-GAM-002 | tbd_open |
| concrete | MEM-PA-001 | tbd_open |
| concrete | SSR-SWEEP-001 | tbd_open |
| class | ERR-AAF | tbd_open |
| class | MEM-PA | tbd_open |
| class | SSR-SWEEP | tbd_open |

## 4. 未核实清单（not_found / tbd_open / mismatch）

47 行。

| 包 | 实体类型 | ID | 状态 | 备注（截断） |
|---|---|---|---|---|
| A | concrete | PER-CAT-001 | not_found | book chapter (Ungerleider & Mishkin 1982, in Analysis of Visual Behavior, MIT Press); no DOI; Crossref/OpenAlex bibliogr |
| A | concrete | SSR-FPAS-001 | not_found | conference abstract (B-Audio 2019, Louvain-la-Neuve); not indexed by Crossref; search endpoints 429. A later journal ver |
| A | concrete | SSR-SSVEP-003 | not_found | title-only guideline record ("guidelines for visual sensitive eeg testing", Can J Neurol Sci); no DOI, no authors/year;  |
| A | concrete | SSR-SWEEP-001 | tbd_open | queries planned: Regan 1973 "Rapid objective refraction using evoked brain potentials" Invest Ophthalmol 12(9):669-679;  |
| A | class | PER-CAT | not_found | class first_source identical to PER-CAT-001 (record reused, no extra fetch); book chapter (Ungerleider & Mishkin 1982, i |
| A | class | SSR-FPAS | not_found | class first_source identical to SSR-FPAS-001 (record reused, no extra fetch); conference abstract (B-Audio 2019, Louvain |
| A | class | SSR-SWEEP | tbd_open | class first_source identical to SSR-SWEEP-001 (record reused, no extra fetch); queries planned: Regan 1973 "Rapid object |
| B | concrete | IMG-MA-001 | not_found | title-only citation "A new mode of EEG based communication" (R0842, Monash URL) could not be resolved: Crossref search 4 |
| B | concrete | MOT-SACC-001 | not_found | Crossref bibliographic search returned no record for Javal 1878 (hits: 2010 CUP reprint of Javal's book, unrelated 1878/ |
| B | concrete | MOT-SMS-001 | not_found | Crossref bibliographic search returned no record for the FAU dissertation (Mayville 2000); dissertations are not indexed |
| B | class | MOT-SACC | not_found | Crossref bibliographic search returned no record for Javal 1878 (hits: 2010 CUP reprint of Javal's book, unrelated 1878/ |
| B | class | MOT-SMS | not_found | Crossref bibliographic search returned no record for the FAU dissertation (Mayville 2000); dissertations are not indexed |
| B | class | IMG-MA | not_found | title-only citation "A new mode of EEG based communication" (R0842, Monash URL) could not be resolved: Crossref search 4 |
| C | concrete | CTL-FLK-002 | tbd_open | tbd_open: no bibliographic search performed - WebFetch quota exhausted (429) before the TBD rows were reached; planned q |
| C | concrete | CTL-MRP-001 | not_found | not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP 429) exhausted after ~85 requ |
| C | concrete | CTL-SIM-002 | tbd_open | tbd_open: no bibliographic search performed - WebFetch quota exhausted (429) before the TBD rows were reached; planned q |
| C | concrete | CTL-STR-002 | tbd_open | tbd_open: no bibliographic search performed - WebFetch quota exhausted (429) before the TBD rows were reached; planned q |
| C | concrete | CTL-SW-003 | tbd_open | tbd_open: no bibliographic search performed - WebFetch quota exhausted (429) before the TBD rows were reached; planned q |
| C | concrete | CTL-WASON-001 | not_found | not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP 429) exhausted after ~85 requ |
| C | concrete | ERR-AAF-001 | tbd_open | tbd_open: no bibliographic search performed - WebFetch quota exhausted (429) before the TBD rows were reached; planned q |
| C | concrete | ERR-ERRP-001 | not_found | not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP 429) exhausted after ~85 requ |
| C | concrete | ERR-ERRP-003 | tbd_open | tbd_open: no bibliographic search performed - WebFetch quota exhausted (429) before the TBD rows were reached; planned q |
| C | concrete | ERR-GAM-001 | not_found | not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP 429) exhausted after ~85 requ |
| C | concrete | ERR-GAM-002 | tbd_open | tbd_open: no bibliographic search performed - WebFetch quota exhausted (429) before the TBD rows were reached; planned q |
| C | concrete | ERR-GAM-003 | not_found | not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP 429) exhausted after ~85 requ |
| C | concrete | ERR-OBS-002 | not_found | not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP 429) exhausted after ~85 requ |
| C | concrete | ERR-OBS-003 | not_found | not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP 429) exhausted after ~85 requ |
| C | concrete | ERR-OGNG-001 | not_found | not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP 429) exhausted after ~85 requ |
| C | concrete | ERR-PRT-001 | not_found | not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP 429) exhausted after ~85 requ |
| C | class | ERR-AAF | tbd_open | same TBD as ERR-AAF-001: tbd_open: no bibliographic search performed - WebFetch quota exhausted (429) before the TBD row |
| C | class | ERR-ERRP | not_found | same source as ERR-ERRP-001: not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP  |
| C | class | ERR-GAM | not_found | same source as ERR-GAM-001: not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP 4 |
| C | class | ERR-OGNG | not_found | same source as ERR-OGNG-001: not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP  |
| C | class | ERR-PRT | not_found | same source as ERR-PRT-001: not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP 4 |
| C | class | CTL-MRP | not_found | same source as CTL-MRP-001: not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP 4 |
| C | class | CTL-WASON | not_found | same source as CTL-WASON-001: not checked: Crossref bibliographic search not performed - WebFetch proxy rate limit (HTTP |
| D | concrete | LAN-VF-001 | not_found | test manual (Benton, Hamsher & Sivan, Multilingual Aphasia Examination, AJA Associates) has no Crossref record; search r |
| D | concrete | MEM-FR-002 | not_found | handbook (Lezak et al. 2012, Neuropsychological Assessment, OUP); two Crossref bibliographic searches were refused (HTTP |
| D | concrete | MEM-PA-001 | tbd_open | queries: (1) Crossref query.author=Calkins bibliographic "Association Psychological Review 1894" -> Calkins 1894 Experim |
| D | class | LAN-VF | not_found | test manual (Benton, Hamsher & Sivan, Multilingual Aphasia Examination, AJA Associates) has no Crossref record; search r |
| D | class | MEM-PA | tbd_open | see MEM-PA-001 |
| E | concrete | STA-MATB-001 | not_found | Crossref bibliographic search (query: multi-attribute task battery ... Comstock) returns only later studies using the MA |
| E | concrete | STA-MW-002 | not_found | Crossref search top hit is a 2001 PsycEXTRA conference record "Zoning out during reading: evidence for dissociations bet |
| E | concrete | STA-SLP-001 | not_found | Crossref search (Rechtschaffen Kales 1968 manual) returns only papers citing the manual; the manual itself has no Crossr |
| E | concrete | STA-SLP-002 | not_found | Crossref search (AASM Manual Scoring Sleep 2007 Iber) returns only commentaries (Schulz 2007, Collop 2012); the manual h |
| E | class | STA-MATB | not_found | Crossref bibliographic search (query: multi-attribute task battery ... Comstock) returns only later studies using the MA |
| E | class | STA-SLP | not_found | Crossref search (Rechtschaffen Kales 1968 manual) returns only papers citing the manual; the manual itself has no Crossr |

## 5. `verified: true` 的条目（内容核实，方法说明 §3）

0 条（书目核实冲刺后应为 0）。

## 6. notes 短语一致性（D-072 / D-073）

- confirmed/corrected/tbd_resolved 但 notes 缺 `bibliography confirmed|corrected`：0
- not_found/tbd_open/mismatch 但 notes 含该短语：0
- 含 D-073 短语 `origin candidate recalled, record confirmed via <API>` 的条目：108
- sources_check 行在图谱中找不到对应实体：0

# 682 rows; TBD concrete 9, class 3; verified:true 0; phrase missing 0, forbidden 0

## 7. 字段更正示例（前 → 后，来自里程碑 M2 → M3 的 diff）

| # | ID（包） | 更正字段 | 之前 | 之后 | 接口 |
|---|---|---|---|---|---|
| 1 | CTL-WCST-001（C） | **卷号错误**、题名连字符、DOI | Journal of Experimental Psychology **34**:404-411. 1948 | Journal of Experimental Psychology. 1948;**38**(4):404-411；doi 10.1037/h0059831 | Crossref 检索 |
| 2 | CTL-AS-001（C） | **期号错误**、页码 | Vision Research 18(**11**). 1978 | Vision Research. 1978;18(**10**):1279-1296 | Crossref |
| 3 | MEM-META-002（D） | **页码错误** | Psychological Science, 2(4), 267-**270** | Psychological Science. 1991;2(4):267-**271** | Crossref |
| 4 | MEM-SME-001（D） | **题名漏词**、期/页、DOI | Neural correlates of encoding in an incidental paradigm. … 67. 1987 | … in an incidental **learning** paradigm. 1987;67(4):360-371；doi 10.1016/0013-4694(87)90124-6 | OpenAlex（候选 DOI 探针，D-073） |
| 5 | STA-HYPN-001（E） | **第一作者错误**、作者表、DOI | **Spiegel DR et al.** Brain Activity and Functional Connectivity Associated with Hypnosis. Cerebral Cortex 27(8). 2017 | **Jiang H, White MP, Greicius MD, Waelde LC, Spiegel D.** … 2017;27(8):4083-4093；doi 10.1093/cercor/bhw220 | OpenAlex（D-073） |
| 6 | SOC-JA-001（E） | **作者顺序错误**、年份、期号、DOI | **Kelso JAS, Tognoli E, Lagarde J, Deguzman GC.** The phi complex … PNAS 104:8190-8195 | **Tognoli E, Lagarde J, DeGuzman GC, Kelso JAS.** … 2007;104(19):8190-8195；doi 10.1073/pnas.0611453104 | OpenAlex（D-073） |
| 7 | STA-MED-001（E） | **1973 年重印本 → 1966 年原文**（作者顺序、期刊、年、卷期页、DOI） | Hirai T, Kasamatsu A. … Journal of the American Institute of Hypnosis 14(3):107-114. **1973** | Kasamatsu A, Hirai T. … Folia Psychiatrica et Neurologica Japonica. **1966**;20(4):315-336；doi 10.1111/j.1440-1819.1966.tb02646.x | OpenAlex（D-073） |
| 8 | PER-AAD-001（A） | 题名-only → 完整书目（作者 9 人、年、卷期页） | Attentional Selection in a Cocktail Party Environment … Cerebral Cortex. | O'Sullivan JA, Power AJ, … Lalor EC. … Cereb Cortex. 2015;25(7):1697-1706；year 2015 | Crossref |
| 9 | MOT-ATT-001（B） | 题名-only → 完整书目 + DOI | Event-related beta EEG-changes during passive and attempted foot movements in paraplegic patients. | Müller-Putz GR, Zimmermann D, Graimann B, Nestinger K, Korisek G, Pfurtscheller G. … Brain Research. 2007;1137(1):84-91；doi 10.1016/j.brainres.2006.12.052 | OpenAlex |
| 10 | LAN-CPS-001（D） | 题名-only（PMID 线索）→ 完整书目 + DOI | Brain potentials indicate immediate use of prosodic cues in natural speech processing. | Steinhauer K, Alter K, Friederici AD. … Nature Neuroscience. 1999;2(2):191-196；doi 10.1038/5757；year 1999 | Crossref |
| 11 | ERR-APC-001（C） | 作者、卷期页、DOI | Temporal difference models and reward-related learning in the human brain. Neuron. 2003. | O'Doherty JP, Dayan P, Friston K, Critchley H, Dolan RJ. … Neuron. 2003;38(2):329-337；doi 10.1016/s0896-6273(03)00169-7 | Crossref 检索 |
| 12 | SOC-TPP-001（E） | 作者（缺）、题名连字符、期号、DOI | Third party punishment and social norms. Evolution and Human Behavior 25:63-87. 2004. | Fehr E, Fischbacher U. Third-party punishment and social norms. … 2004;25(2):63-87；doi 10.1016/S1090-5138(04)00005-4 | OpenAlex（D-073） |
| 13 | STM-ADBS-001（B） | 题名-only → 完整书目 + DOI（JoVE 方法文章，非 aDBS 原始研究，D-031 待核） | Controlling Parkinson's Disease With Adaptive Deep Brain Stimulation. | Little S, Pogosyan A, … Brown P. … Journal of Visualized Experiments. 2014;(89):51403；doi 10.3791/51403 | OpenAlex |
| 14 | MOT-CURSOR-001（B） | 作者缩写、期号 | Wolpaw **J**, McFarland DJ, … 78:252-259. 1991 | Wolpaw **JR**, … 1991;78(**3**):252-259 | Crossref |
| 15 | PER-FACE-001（A） | 题名-only → 完整书目 + DOI | Electrophysiological Studies of Face Perception in Humans. | Bentin S, Allison T, Puce A, Perez E, McCarthy G. … J Cogn Neurosci. 1996;8(6):551-565；doi 10.1162/jocn.1996.8.6.551 | OpenAlex（D-073） |
| 16 | IMG-AUD-001（B） | DOI 补入、引文改为统一格式 | Zatorre, R. J., Halpern, A. R., … 8(1), 29-46. 1996. | Zatorre RJ, Halpern AR, Perry DW, Meyer E, Evans AC. … 1996;8(1):29-46；doi 10.1162/jocn.1996.8.1.29 | Crossref 检索 |

TBD 解决示例（tbd_resolved，候选源头，内容未核）：PER-ABR-001 → Jewett & Williston 1971 Brain（更早的 Sohmer & Feinmesser 1967 待查优先权）；PER-ACC-001 → Ostroff, Martin & Boothroyd 1998 Ear Hear；MOT-MI-005 → Neuper, Schlögl & Pfurtscheller 1999 J Clin Neurophysiol；LAN-GEST-001 → Kelly, Kravitz & Hopkins 2003 Brain Lang；EMO-EST-001 → Gotlib & McCann 1984 JPSP；STA-SCP-001 → Elbert, Rockstroh, Lutzenberger & Birbaumer 1980 EEG Clin Neurophysiol（早于原 1992 年记录 12 年）。

对应的范式类：184 个类的 `first_source` 按 `class_updates.yaml` 同步更正（类源头与 -001 相同者直接复用记录，D-062），254 个类的 notes 加核实短语。

## 8. 未核实清单（not_found 35 + tbd_open 12 = 47 行）

完整列表见上文第 4 节；归类：

| 类别 | 行数 | 条目 |
|---|---|---|
| 因代理限流**未检查**（包 C，记为 not_found） | 15 | CTL-MRP-001, CTL-WASON-001, ERR-ERRP-001, ERR-GAM-001, ERR-GAM-003, ERR-OBS-002, ERR-OBS-003, ERR-OGNG-001, ERR-PRT-001 + 类 CTL-MRP, CTL-WASON, ERR-ERRP, ERR-GAM, ERR-OGNG, ERR-PRT |
| Crossref / OpenAlex **无记录**：手册、指南、技术报告、学位论文、书章、会议摘要 | 20 | LAN-VF-001 / LAN-VF（Benton MAE）、MEM-FR-002（Lezak 手册）、STA-SLP-001（R&K 1968）、STA-SLP-002 / STA-SLP（AASM 2007）、STA-MATB-001 / STA-MATB（NASA TM 104174）、SSR-SSVEP-003（临床光驱动指南）、MOT-SMS-001 / MOT-SMS（FAU 学位论文）、PER-CAT-001 / PER-CAT（Ungerleider & Mishkin 1982 书章）、SSR-FPAS-001 / SSR-FPAS（2019 会议摘要）、MOT-SACC-001 / MOT-SACC（Javal 1878）、STA-MW-002（2004 书章）、IMG-MA-001 / IMG-MA（R0842 题名-only；Keirn & Aunon 1990 题名不同，未写入） |
| **TBD 仍开放** | 12 | SSR-SWEEP-001 / SSR-SWEEP、CTL-FLK-002、CTL-SIM-002、CTL-STR-002、CTL-SW-003、ERR-AAF-001 / ERR-AAF、ERR-ERRP-003、ERR-GAM-002、MEM-PA-001 / MEM-PA（Calkins 1894） |

这些行的 YAML 未改、notes 无核实短语（第 6 节检查 0 多）。处理计划见 D-074（草案）。

## 9. 工具限制与方法说明

1. **检索接口不可用**。Crossref `works?query.bibliographic=` 与 OpenAlex `works?search=` / `filter=title.search` 经代理大面积 429（A：4/4 失败；B：6/6 失败；D：约每 2–4 分钟成功一次；E：长查询串返回无关默认列表）。只有"按 DOI / PMID 取记录"稳定可用。包 C 在约 85 次请求后遭全局限流（等待 10 分钟以上仍被拒），15 行未检查。
2. **PubMed 不可用**。文章页返回 reCAPTCHA 或空壳（JS 页面），E-utilities 被 robots.txt 禁止。因此 **PMID 一律未核验**：原条目的 PMID 保留；接口记录给出的 PMID 只有在 OpenAlex `ids.pmid` 给出时才写入（B、E 若干），`matched_pmid` 列仅为记录值。
3. **凭记忆的候选 DOI（D-073）**。检索不可用时，A（69 行，逐行标注）、E（13 个 DOI + 4 个 TBD 候选，日志整体说明）、D（5 个 "DOI-record probe"）、B（5 个 TBD 候选）用审核人回忆的 DOI 作查询键取记录，记录与条目一致才写入。维护者按 D-073 给 108 条加短语 `origin candidate recalled, record confirmed via <API>`。**局限**：E、D、B 的审核人没有逐行标注，维护者按工作日志 / 抓取日志能确定的范围整体标注（E 按日志列出的 15 个 ID 及其同 DOI 的类 / 变体行；D 按抓取日志中标 "probe" 的 5 个 DOI；B 按 5 条 tbd_resolved），可能有少数漏标或多标，内容核实时以 fetch_log 为准。
4. **年份口径**。接口 `issued` / `publication_year` 常为在线年；与卷期对应的印刷年优先（如 MOT-ATT-001 2007、LAN-HIER-001 2016），原条目无年份时按接口年份写并在 note 说明。
5. **记录本身的缺陷**。Crossref 对部分旧文献只列第一作者（IMG-AUD-002、CTL-ANAL-001、SOC-JA-001 变体），引文作者表保留原文；OpenAlex 给出的 DOI 若未经 Crossref 确认不写入（EMO-STRESS-002）。
6. **书目核实 ≠ 内容核实**。记录一致只说明"这篇文献存在且书目正确"；它是否描述该范式、是否最早（D-031、D-062），须读原文。tbd_resolved 的 88 条尤其只是候选。

## 10. 下一步

- **第四冲刺（D-074）**：取得机构数据库 / Crossref polite pool 后，先补包 C 的 15 行未检查，再处理手册 / 指南 / 技术报告（接受无 DOI 的完整书目），最后做 12 行 TBD 开放行与 88 条 tbd_resolved 候选的**内容核实**（优先 P1 核心类，D-066）。
- 内容核实时优先复查带 D-073 短语的 108 条，以及审核人在 sources_check note 中指出的优先权问题：PER-ABR（Sohmer & Feinmesser 1967）、MEM-DF（Bjork 1968 早于类源头 Bjork 1970）、MOT-MI-005 / -009（更早的 Graz / 异步 MI 研究）、STM-ADBS（Little 2013 原始研究 vs JoVE 方法文章）、PER-IC（Kanizsa 1955 意大利文原文）。
- 维护者：`literature.csv` 中对应 R 编号的书目按 `sources_check.csv` 同步（本版未做，避免与 Zotero 导出冲突；列入 sprint 4）。
- schema 0.3 提议：`source.source_check: {bibliographic, content}`（D-072 第 5 款），`verified: true` ⇔ `content` 非空。
