# 检索记录 · 包 A 感知与稳态 · sprint 2

> 每次检索追加一行，维护者汇总进 `curation/search_protocol.md`（S-003 起）。不使用的检索也要记（命中 0 也记）。

| 编号 | 日期 | 数据库 | 检索式 / URL | 命中数 | 新增文献数 | 相关范式 | 执行人 | 用途 |
|---|---|---|---|---|---|---|---|---|
| S2A01 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/dataset_summary.html | 摘要被截断（部分表） | 0 | PER-ODD-003; SSR-CVEP-001 | curator_a | 数据集概览：BNCI2014_008 6×6 speller 等 |
| S2A02 | 2026-10-03 | curl (Bash) | https://moabb.neurotechx.com/docs/dataset_summary.html | 代理拒绝（403 CONNECT） | 0 | — | curator_a | 未用；未重试 |
| S2A03 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/dataset_summary.html（第二次提问，缓存页） | 截断 | 0 | — | curator_a | 未得完整表；改用各数据集页 |
| S2A04 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.Wang2016.html | 1 页 | 1 | SSR-SSVEP-005 | curator_a | 40 目标基准数据集；页面未写相位 |
| S2A05 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.Nakanishi2015.html | 1 页 | 1 | SSR-SSVEP-006 | curator_a | 12 目标 JFPM |
| S2A06 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.Kalunga2016.html | 1 页 | 1 | SSR-SSVEP-007 | curator_a | 3 频率 + 静息类 |
| S2A07 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.EPFLP300.html | 1 页 | 1 | PER-ODD-007 | curator_a | 六图像单项闪烁 |
| S2A08 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.BNCI2015_009.html | 1 页 | 1 | PER-ODD-008 | curator_a | AMUSE 听觉空间 |
| S2A09 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.BNCI2015_010.html | 1 页 | 1 | PER-ODD-005 | curator_a | RSVP 拼写 |
| S2A10 | 2026-10-03 | WebFetch | https://en.wikipedia.org/wiki/P3a | 1 页 | 1 | PER-ODD-002 | curator_a | R1022；Squires et al. 1975 完整引文 |
| S2A11 | 2026-10-03 | WebFetch | https://en.wikipedia.org/wiki/Retinotopy | 1 页 | 0 | PER-RET-002 | curator_a | 无方法细节，未用 |
| S2A12 | 2026-10-03 | WebSearch | Townsend 2010 checkerboard paradigm P300 speller Clinical Neurophysiology doi | 9 链接 | 1 | PER-ODD-006 | curator_a | 棋盘格范式 |
| S2A13 | 2026-10-03 | WebFetch | https://pmc.ncbi.nlm.nih.gov/articles/PMC2879474 | 1 页 | 0（同 S2A12） | PER-ODD-006 | curator_a | 引文与摘要 |
| S2A14 | 2026-10-03 | WebSearch | Chen Wang Nakanishi Gao Jung Gao 2015 PNAS high-speed spelling noninvasive brain-computer interface joint frequency phase modulation | 9 链接 | 1 | SSR-SSVEP-005 | curator_a | JFPM 40 目标 |
| S2A15 | 2026-10-03 | WebFetch | https://pmc.ncbi.nlm.nih.gov/articles/PMC4640776 | reCAPTCHA 页 | 0 | — | curator_a | 未用；未重试 |
| S2A16 | 2026-10-03 | WebFetch | https://resource.aminer.org/pub/562901e70cf2bc5294a4d41b | 302 跨站重定向 | 0 | — | curator_a | 未跟随 |
| S2A17 | 2026-10-03 | WebFetch | https://www.kurzweilai.net/fastest-brain-computer-interface-speller-developed | 1 页 | 0（同 S2A14） | SSR-SSVEP-005 | curator_a | 标题、期刊、年份与 JFPM 原句；无作者 |
| S2A18 | 2026-10-03 | WebSearch | Näätänen Pakarinen 2004 "new paradigm" multi-feature mismatch negativity Optimum-1 Clinical Neurophysiology | 9 链接 | 1 | PER-MMN-003 | curator_a | 多特征 MMN |
| S2A19 | 2026-10-03 | WebFetch | https://read.qxmd.com/read/14706481/the-mismatch-negativity-mmn-towards-the-optimal-paradigm | 1 页 | 0（同 S2A18） | PER-MMN-003 | curator_a | 标题、期刊、PMID；无作者 |
| S2A20 | 2026-10-03 | WebSearch | Skoe Kraus 2010 "Auditory brain stem response to complex sounds: a tutorial" Ear and Hearing | 9 链接 | 1 | SSR-FFR-002 | curator_a | 语音 FFR 教程 |
| S2A21 | 2026-10-03 | WebFetch | https://production.wordpress.uconn.edu/skoe/wp-content/uploads/sites/278/2013/11/Skoe_Kraus_EarHear_2010.pdf | 1 PDF | 0（同 S2A20） | SSR-FFR-002 | curator_a | 历史段落；参考文献条目不可靠，未采用 |
| S2A22 | 2026-10-03 | WebSearch | auditory steady-state response brain-computer interface selective attention two amplitude-modulated tones 37 Hz 43 Hz | 10 链接 | 1 | SSR-ASSR-002 | curator_a | ASSR BCI |
| S2A23 | 2026-10-03 | WebFetch | https://scholar.korea.ac.kr/handle/2021.sw.korea/112660?mode=full | 1 页 | 0（同 S2A22） | SSR-ASSR-002 | curator_a | Kim et al. 2011 元数据与摘要 |
| S2A24 | 2026-10-03 | WebFetch | https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2010.00186 | 1 页 | 0（R0937） | PER-CVA-002 | curator_a | R0937 = Jensen & Mazaheri 2010；引用两项在线 α BCI |
| S2A25 | 2026-10-03 | WebSearch | Sutter 1992 "The brain response interface: communication through visually-induced electrical brain responses" Journal of Microcomputer Applications | 9 链接 | 0 | SSR-CVEP-001 | curator_a | 无相关命中，c-VEP 源头仍 TBD |
| S2A26 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.CastillosBurstVEP100.html | 1 页 | 1 | SSR-CVEP-001; SSR-CVEP-003 | curator_a | burst c-VEP |
| S2A27 | 2026-10-03 | WebFetch | https://moabb.neurotechx.com/docs/generated/moabb.datasets.Thielen2015.html | 1 页 | 1 | SSR-CVEP-002 | curator_a | Gold 码 c-VEP |
| S2A28 | 2026-10-03 | WebSearch | asynchronous SSVEP brain-computer interface idle state detection self-paced control state | 10 链接 | 1 | SSR-SSVEP-008 | curator_a | 异步 SSVEP |
| S2A29 | 2026-10-03 | WebFetch | https://robot.sia.cn/article/doi/10.3724/SP.J.1218.2013.00045 | 1 页 | 0（同 S2A28） | SSR-SSVEP-008 | curator_a | Zhang & Deng 2013 |
| S2A30 | 2026-10-03 | WebSearch | Dumoulin Wandell 2008 population receptive field estimates in human visual cortex NeuroImage moving bar | 10 链接 | 1 | PER-RET-002 | curator_a | pRF |
| S2A31 | 2026-10-03 | WebFetch | https://research-portal.uu.nl/en/publications/population-receptive-field-estimates-in-human-visual-cortex/ | 1 页 | 0（同 S2A30） | PER-RET-002 | curator_a | 引文与摘要 |
| S2A32 | 2026-10-03 | WebFetch | https://home.uni-leipzig.de/biocog/archived-20210701/index.php@page=ab | robots 拒绝 | 0 | — | curator_a | 未用；未重试 |
| S2A33 | 2026-10-03 | WebSearch | SanMiguel Widmann Bendixen Trujillo-Barreto Schröger 2013 "Hearing silences" J Neurosci omission self-initiated sounds | 10 链接 | 1 | PER-OMIT-002 | curator_a | 自发遗漏 |
| S2A34 | 2026-10-03 | WebFetch | https://www.doccheck.com/de/detail/articles/6634-baustein-der-gerauschwahrnehmung-entdeckt | 1 页 | 0（R0585） | PER-OMIT-002 | curator_a | 实验描述与 DOI |
| S2A35 | 2026-10-03 | WebFetch | https://doaj.org/article/dd01270b01fb4f17a135a6057f9a8dde | 1 页 | 0（R0792） | PER-OMIT-002 | curator_a | Dercksen et al. 2020 |
| S2A36 | 2026-10-03 | WebSearch | Morgan Hansen Hillyard 1996 PNAS "Selective attention to stimulus location modulates the steady-state visual evoked potential" | 10 链接 | 1 | SSR-SSVEP-004 | curator_a | 频率标记注意源头（D-003） |
| S2A37 | 2026-10-03 | WebFetch | https://buscaintegrada.ufrj.br/Record/pubmed-39354 | 1 页 | 0（同 S2A36） | SSR-SSVEP-004 | curator_a | 引文与截断摘要 |
| S2A38 | 2026-10-03 | WebSearch | Brouwer van Erp 2010 tactile P300 brain-computer interface Frontiers in Neuroscience vibrotactors waist | 10 链接 | 1 | PER-ODD-009 | curator_a | 触觉 P300（D-012） |
| S2A39 | 2026-10-03 | WebFetch | https://doaj.org/article/d7904c0274894787a310c430873f84c4 | 1 页 | 0（同 S2A38） | PER-ODD-009 | curator_a | 引文与摘要 |
