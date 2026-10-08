# 包 E · sprint 3 · 取数日志 / fetch log（curator_d，2026-10-05）

工具：WebFetch（经代理）。WebSearch 配额已尽，未用；PubMed 文章页被代理拒绝（429），未再试；Crossref 书目检索对长查询串返回与查询无关的默认列表（见 #68、#95–#97），改用短查询串后正常。按 DOI 取记录时 Crossref 多次 429，改用 OpenAlex `works/doi:` 与 `works/pmid:`（README 允许的回退源）。共 100 次取数；被拒的 URL 一律不重试。

| # | 来源 | URL | 结果 |
|---|---|---|---|
| 1 | Crossref | https://api.crossref.org/works/10.1037/0022-3514.50.2.229 | 记录取回（EMO-APRIME-001） |
| 2 | Crossref | https://api.crossref.org/works/10.1037/0021-843x.95.2.144 | 429 |
| 3 | Crossref | https://api.crossref.org/works/10.1037/0021-843x.95.1.15 | 记录取回（EMO-DOT-001） |
| 4 | Crossref | https://api.crossref.org/works/10.1016/j.neuron.2004.08.042 | 记录取回（EMO-FC-003） |
| 5 | Crossref | https://api.crossref.org/works/10.1080/02699939508408966 | 记录取回（EMO-FILM-001） |
| 6 | Crossref | https://api.crossref.org/works/10.1109/T-AFFC.2011.15 | 记录取回（EMO-FILM-002） |
| 7 | OpenAlex | https://api.openalex.org/works/doi:10.1037/0021-843x.95.2.144 | 记录取回（EMO-AUTO-001） |
| 8 | Crossref | https://api.crossref.org/works/10.1006/nimg.2000.0593 | 429 |
| 9 | Crossref | https://api.crossref.org/works/10.1093/scan/nsn051 | 429（代理拒绝） |
| 10 | Crossref | https://api.crossref.org/works/10.1162/089892902760807212 | 记录取回（EMO-REG-001） |
| 11 | OpenAlex | https://api.openalex.org/works/doi:10.1006/nimg.2000.0593 | 记录取回（EMO-MID-001） |
| 12 | OpenAlex | https://api.openalex.org/works/doi:10.1093/scan/nsn051 | 记录取回（EMO-MID-002） |
| 13 | Crossref | https://api.crossref.org/works/10.1097/wnr.0b013e3282f454db | 429（代理拒绝） |
| 14 | OpenAlex | https://api.openalex.org/works/doi:10.1097/wnr.0b013e3282f454db | 记录取回（EMO-SOUND-001） |
| 15 | OpenAlex | https://api.openalex.org/works/doi:10.1038/nn896 | 记录取回（EMO-TOUCH-001） |
| 16 | OpenAlex | https://api.openalex.org/works/doi:10.1111/j.1467-9280.2007.01924.x | 记录取回（EMO-WORD-001；题名字段只有 "Buzzwords"） |
| 17 | OpenAlex | https://api.openalex.org/works/doi:10.3758/bf03212378 | 记录取回（SOC-BIO-001） |
| 18 | OpenAlex | https://api.openalex.org/works/doi:10.1016/j.neuron.2008.11.027 | 记录取回（SOC-CONF-001） |
| 19 | OpenAlex | https://api.openalex.org/works/doi:10.1006/game.1994.1021 | 记录取回（SOC-DICT-001） |
| 20 | OpenAlex | https://api.openalex.org/works/doi:10.1073/pnas.0604475103 | 记录取回（SOC-DICT-002） |
| 21 | OpenAlex | https://api.openalex.org/works/doi:10.1016/j.neuroimage.2017.06.018 | 记录取回（SOC-EYE-001） |
| 22 | OpenAlex | https://api.openalex.org/works/doi:10.1037/0022-3514.74.6.1464 | 记录取回（SOC-IAT-001） |
| 23 | OpenAlex | https://api.openalex.org/works/doi:10.1006/brcg.2000.1225 | 记录取回（SOC-IMIT-001） |
| 24 | OpenAlex | https://api.openalex.org/works/doi:10.1126/science.1062872 | 记录取回（SOC-MORAL-001） |
| 25 | OpenAlex | https://api.openalex.org/works/doi:10.1016/0168-5597(95)00116-a | 记录取回（SOC-NAME-001） |
| 26 | OpenAlex | https://api.openalex.org/works/doi:10.1080/13554790902724904 | 记录取回（SOC-NAME-002） |
| 27 | OpenAlex | https://api.openalex.org/works/doi:10.1111/1469-7610.00715 | 记录取回（SOC-RME-001） |
| 28 | OpenAlex | https://api.openalex.org/works/doi:10.1038/35053167 | 记录取回（SOC-SELF-001） |
| 29 | OpenAlex | https://api.openalex.org/works/doi:10.1038/nn1728 | 记录取回（SOC-SFB-001） |
| 30 | OpenAlex | https://api.openalex.org/works/doi:10.1016/0010-0277(83)90004-5 | 记录取回（SOC-TOM-001；作者只列 Wimmer） |
| 31 | OpenAlex | https://api.openalex.org/works/doi:10.1016/0010-0277(85)90022-8 | 记录取回（SOC-TOM-001 变体） |
| 32 | OpenAlex | https://api.openalex.org/works/doi:10.1016/s1053-8119(03)00230-1 | 记录取回（SOC-TOM-002） |
| 33 | OpenAlex | https://api.openalex.org/works/doi:10.1006/game.1995.1027 | 记录取回（SOC-TRUST-001） |
| 34 | OpenAlex | https://api.openalex.org/works/doi:10.1016/s0896-6273(02)00755-9 | 记录取回（SOC-TRUST-002） |
| 35 | OpenAlex | https://api.openalex.org/works/doi:10.1126/science.1108062 | 记录取回（SOC-TRUST-003 及其变体） |
| 36 | OpenAlex | https://api.openalex.org/works/doi:10.1016/0167-2681(82)90011-7 | 记录取回（SOC-UG-001） |
| 37 | OpenAlex | https://api.openalex.org/works/doi:10.1162/jocn.2006.18.6.898 | 记录取回（SOC-VPT-001） |
| 38 | OpenAlex | https://api.openalex.org/works/doi:10.1037/0022-3514.81.2.181 | 记录取回（SOC-WIT-001） |
| 39 | OpenAlex | https://api.openalex.org/works/doi:10.1007/bf01618421 | 记录取回（STA-ANES-001） |
| 40 | OpenAlex | https://api.openalex.org/works/doi:10.1016/j.neuron.2013.03.006 | 记录取回（STA-CLAS-001） |
| 41 | OpenAlex | https://api.openalex.org/works/doi:10.1038/nn.4545 | 记录取回（STA-DREAM-001） |
| 42 | OpenAlex | https://api.openalex.org/works/doi:10.1109/TCSI.2005.857555 | 记录取回（STA-DRV-001） |
| 43 | OpenAlex | https://api.openalex.org/works/doi:10.3389/fnhum.2012.00112 | 记录取回（STA-ENG-001） |
| 44 | OpenAlex | https://api.openalex.org/works/doi:10.1111/j.2164-0947.1970.tb02056.x | 记录取回（STA-MW-001） |
| 45 | OpenAlex | https://api.openalex.org/works/doi:10.1016/S1053-8119(03)00145-9 | 记录取回（STA-NF-002） |
| 46 | OpenAlex | https://api.openalex.org/works/doi:10.1073/pnas.1518377113 | 记录取回（STA-PSY-001） |
| 47 | OpenAlex | https://api.openalex.org/works/doi:10.3758/bf03200977 | 记录取回（STA-PVT-001） |
| 48 | OpenAlex | https://api.openalex.org/works/doi:10.1002/mrm.1910340409 | 记录损坏（题名/作者属于另一篇），弃用 |
| 49 | Crossref | https://api.crossref.org/works/10.1002/mrm.1910340409 | 记录取回（STA-REST-001） |
| 50 | Crossref | https://api.crossref.org/works/10.1016/j.clinph.2007.07.028 | 记录取回（STA-REST-002） |
| 51 | Crossref | https://api.crossref.org/works/10.1038/18581 | 记录取回（STA-SCP-002；类 STA-SCP） |
| 52 | PubMed | https://pubmed.ncbi.nlm.nih.gov/11930154/ | 429（代理拒绝）；此后不再访问 PubMed |
| 53 | Crossref 检索 | https://api.crossref.org/works?query.bibliographic=An+ERP+study+on+the+time+course+of+emotional+face+processing&rows=3&select=... | 首条命中题名完全一致（EMO-FACE-001，Eimer & Holmes 2002） |
| 54 | Crossref 检索 | https://api.crossref.org/works?query.bibliographic=Hariri+The+amygdala+response+...&rows=3&select=... | 429（代理拒绝） |
| 55 | OpenAlex | https://api.openalex.org/works/pmid:12482086 | 记录取回（EMO-FACE-002） |
| 56 | OpenAlex | https://api.openalex.org/works/pmid:9620698 | 记录取回（EMO-FC-001） |
| 57 | OpenAlex | https://api.openalex.org/works/pmid:23748500 | 记录取回（EMO-FC-002） |
| 58 | OpenAlex | https://api.openalex.org/works/pmid:24552785 | 记录取回（EMO-FILM-002 变体；类型 Review） |
| 59 | OpenAlex | https://api.openalex.org/works/pmid:14659102 | 记录取回（EMO-HUMOR-001） |
| 60 | OpenAlex | https://api.openalex.org/works/pmid:10699350 | 记录取回（EMO-IAPS-001） |
| 61 | OpenAlex | https://api.openalex.org/works/pmid:17888411 | 记录取回（EMO-REG-002） |
| 62 | OpenAlex | https://api.openalex.org/works/pmid:10944414 | 记录取回（SOC-ANIM-001） |
| 63 | OpenAlex | https://api.openalex.org/works/pmid:19929761 | 记录取回（SOC-GAZE-002） |
| 64 | OpenAlex | https://api.openalex.org/works/pmid:14976305 | 记录取回（SOC-PAIN-001） |
| 65 | OpenAlex | https://api.openalex.org/works/pmid:14561116 | 记录取回（SOC-RACE-001） |
| 66 | OpenAlex | https://api.openalex.org/works/pmid:39428887 | 记录取回（STA-NF-002 变体；perspective） |
| 67 | OpenAlex 检索 | https://api.openalex.org/works?search=Zheng%20Lu%20Investigating%20critical%20frequency%20bands...&per-page=3 | 429 |
| 68 | Crossref 检索 | https://api.crossref.org/works?query.bibliographic=Zheng+Lu+Investigating+critical+frequency+bands+...+2015&rows=3&select=... | 返回与查询无关的三条记录（长查询串未生效） |
| 69 | OpenAlex 检索 | https://api.openalex.org/works?filter=title.search:critical%20frequency%20bands...&per-page=3 | 429 |
| 70 | Crossref | https://api.crossref.org/works/10.1109/TAMD.2015.2431497 | 429（代理拒绝） |
| 71 | OpenAlex | https://api.openalex.org/works/doi:10.1109/TAMD.2015.2431497 | 记录取回（EMO-FILM-003；题名/作者/年份与引文一致） |
| 72 | OpenAlex | https://api.openalex.org/works/doi:10.1109/TCYB.2018.2797176 | 记录取回（EMO-FILM-004 TBD 候选：EmotionMeter） |
| 73 | OpenAlex | https://api.openalex.org/works/doi:10.1088/1741-2552/aa5a98 | 记录取回（STA-DRV-002 TBD 候选：Zheng & Lu 2017） |
| 74 | OpenAlex | https://api.openalex.org/works/doi:10.1016/0013-4694(80)90265-5 | 记录取回（STA-SCP-001 TBD 候选：Elbert et al. 1980） |
| 75 | OpenAlex | https://api.openalex.org/works/doi:10.1037/0022-3514.47.2.427 | 记录取回（EMO-EST-001 TBD 候选：Gotlib & McCann 1984） |
| 76 | OpenAlex | https://api.openalex.org/works/doi:10.1159/000119004 | 记录取回（EMO-STRESS-001；OpenAlex 年份字段 2008 为 Karger 上网年，卷 28 为 1993） |
| 77 | OpenAlex | https://api.openalex.org/works/doi:10.1038/nprot.2012.001 | 429（代理拒绝） |
| 78 | Crossref | https://api.crossref.org/works/10.1038/nprot.2012.001 | 记录取回（EMO-THREAT-001） |
| 79 | Crossref | https://api.crossref.org/works/10.1037/0022-3514.79.5.748 | 记录取回（SOC-CYB-001） |
| 80 | Crossref | https://api.crossref.org/works/10.3758/BF03208827 | 记录取回（SOC-GAZE-001；题名完全一致） |
| 81 | Crossref | https://api.crossref.org/works/10.1073/pnas.0611453104 | 429（代理拒绝） |
| 82 | OpenAlex | https://api.openalex.org/works/doi:10.1073/pnas.0611453104 | 记录取回（SOC-JA-001；作者顺序 Tognoli…Kelso） |
| 83 | OpenAlex | https://api.openalex.org/works/doi:10.1006/nimg.2002.1150 | 记录取回（SOC-JA-001 变体；仅一位作者） |
| 84 | OpenAlex | https://api.openalex.org/works/doi:10.1016/j.neuroimage.2004.09.006 | 记录取回（SOC-PAIN-002；题名完全一致） |
| 85 | OpenAlex | https://api.openalex.org/works/doi:10.1016/S1090-5138(04)00005-4 | 记录取回（SOC-TPP-001） |
| 86 | OpenAlex | https://api.openalex.org/works/doi:10.1093/cercor/bhw220 | 记录取回（STA-HYPN-001；第一作者 Jiang） |
| 87 | OpenAlex | https://api.openalex.org/works/doi:10.1016/0013-4694(72)90028-4 | 记录取回（STA-NF-001） |
| 88 | OpenAlex | https://api.openalex.org/works/doi:10.1111/j.1440-1819.1966.tb02646.x | 记录取回（STA-MED-001：1966 年原文） |
| 89 | Crossref 检索 | https://api.crossref.org/works?query.bibliographic=Dedovic+Montreal+Imaging+Stress+Task+2005+...&rows=3&select=... | 429（代理拒绝） |
| 90 | OpenAlex | https://api.openalex.org/works/pmid:16151536 | 记录取回（EMO-STRESS-002；OpenAlex 给出的 DOI 10.1139/jpn.0541 未经 Crossref 确认，未写入） |
| 91 | OpenAlex 检索 | https://api.openalex.org/works?filter=title.search:multi-attribute%20task%20battery...&per-page=3&sort=publication_year:asc | 429 |
| 92 | Crossref 检索 | https://api.crossref.org/works?query.bibliographic=Comstock+Arnegard+1992+The+multi-attribute+task+battery+...&rows=3&select=... | 429 |
| 93 | Crossref | https://api.crossref.org/works/10.1006/nimg.2002.1150 | 记录取回（SOC-JA-001 变体；同样只列 Montague P） |
| 94 | Crossref 检索 | https://api.crossref.org/works?query.bibliographic=multi-attribute+task+battery+for+human+operator+workload+and+strategic+behavior+research+Comstock&rows=3&select=... | 只有引用 MATB 的后续研究，无 NASA TM 记录（STA-MATB-001 not_found） |
| 95 | Crossref 检索 | https://api.crossref.org/works?query.bibliographic=Schooler+Reichle+Halpern+Zoning+out+while+reading+...&rows=3&select=... | 返回与查询无关的记录（长查询串未生效） |
| 96 | Crossref 检索 | https://api.crossref.org/works?query.bibliographic=Rechtschaffen+Kales+1968+A+manual+of+standardized+terminology+...&rows=3&select=... | 返回与查询无关的记录（长查询串未生效） |
| 97 | Crossref 检索 | 同上，%20 编码 | 同上 |
| 98 | Crossref 检索 | https://api.crossref.org/works?query.bibliographic=AASM+Manual+Scoring+Sleep+Associated+Events+2007+Iber&rows=3&select=... | 只有评论文章（Schulz 2007、Collop 2012），无手册记录（STA-SLP-002 not_found） |
| 99 | Crossref 检索 | https://api.crossref.org/works?query.bibliographic=Rechtschaffen+Kales+1968+manual+scoring+sleep+stages&rows=3&select=... | 只有引用该手册的论文，无手册记录（STA-SLP-001 not_found） |
| 100 | Crossref 检索 | https://api.crossref.org/works?query.bibliographic=Schooler+Zoning+out+while+reading+metaconsciousness&rows=3&select=... | 首条为 2001 年 PsycEXTRA 会议记录（Schooler, Reichle, Halpern；题名 "meta-awareness"），非 2004 年书章；STA-MW-002 not_found，作者线索记入 note |

说明：#71–#88 中有 13 个 DOI 是审核人凭记忆写出、再用取回的记录核对题名/作者/年份后才写入 YAML 的（EMO-FILM-003、EMO-STRESS-001、EMO-THREAT-001、SOC-CYB-001、SOC-GAZE-001、SOC-JA-001 及变体、SOC-PAIN-002、SOC-TPP-001、STA-HYPN-001、STA-MED-001、STA-NF-001，以及四个 TBD 候选）。凡记录与引文的题名或第一作者不一致者一律未写入。
