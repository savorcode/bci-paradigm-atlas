# 检索记录 · 包 A 感知与稳态

> 每次检索追加一行，维护者每周汇总进 `curation/search_protocol.md`（S-002 起）。不使用的检索也要记（命中 0 也记）。

| 编号 | 日期 | 数据库 | 检索式 / URL | 命中数 | 新增文献数 | 相关范式 | 执行人 | 用途 |
|---|---|---|---|---|---|---|---|---|
| SA01 | 2026-10-03 | WebSearch | visual mismatch negativity vMMN review | 9 链接 | 3 | PER-VMMN-001 | curator_a | 新候选 vMMN 线索（PMC11867396 系统综述、jyx 元分析） |
| SA02 | 2026-10-03 | WebFetch | https://pubmed.ncbi.nlm.nih.gov/?term=visual+mismatch+negativity+review | 代理拒绝（403） | 0 | — | curator_a | 未用；未重试 |
| SA03 | 2026-10-03 | WebFetch | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8888690/ | 302 跳转 | 0 | — | curator_a | 跳转至 pmc.ncbi.nlm.nih.gov |
| SA04 | 2026-10-03 | WebFetch | https://pmc.ncbi.nlm.nih.gov/articles/PMC8888690 | 1 | 1 | PER-VMMN-001 | curator_a | Czigler & Kojouharova 2022 题录（未标明 vMMN 首报） |
| SA05 | 2026-10-03 | WebFetch | PubMed 组合检索页（ABR/ASSR/P50/c-VEP 源头） | 0（页面只显示热门文章） | 0 | — | curator_a | 未用 |
| SA06 | 2026-10-03 | WebFetch | eutils.ncbi.nlm.nih.gov esearch | robots.txt 禁止 | 0 | — | curator_a | 未用 |
| SA07 | 2026-10-03 | WebFetch | www.ebi.ac.uk/europepmc REST 检索 | 429 限流 | 0 | — | curator_a | 未用；按要求不重试 |
| SA08 | 2026-10-03 | WebFetch | https://en.wikipedia.org/wiki/Auditory_brainstem_response（R0856） | 1 | 0 | PER-ABR-001 | curator_a | 正文提及 Sohmer & Feinmesser 1967、Jewett & Williston 1971，但无完整参考文献 |
| SA09 | 2026-10-03 | WebSearch | auditory middle latency response Pa Na generators human scalp | 9 | 3 | PER-MLR-001 | curator_a | 新候选 MLR 线索 |
| SA10 | 2026-10-03 | WebSearch | acoustic change complex N1-P2 cortical response to change within ongoing sound | 10 | 1 | PER-ACC-001 | curator_a | 新候选 ACC 线索（多数结果无标题，未用） |
| SA11 | 2026-10-03 | WebSearch | object-related negativity mistuned harmonic concurrent sound segregation Alain | 10 | 2 | PER-ORN-001 | curator_a | 新候选 ORN 线索与源头候选 |
| SA12 | 2026-10-03 | WebSearch | auditory stream segregation mismatch negativity Sussman | 10 | 1 | PER-STREAM-001 | curator_a | 新候选听觉流分离线索与源头候选 |
| SA13 | 2026-10-03 | WebSearch | gustatory evoked potentials human taste stimulation EEG | 10 | 3 | PER-GEP-001 | curator_a | 新候选味觉诱发电位线索 |
| SA14 | 2026-10-03 | WebSearch | sustained posterior negativity symmetry perception ERP Makin Bertamini | 10 | 1 | PER-SPN-001 | curator_a | 新候选对称知觉线索 |
| SA15 | 2026-10-03 | WebSearch | illusory contour Kanizsa ERP "IC effect" visual evoked potential | 9 | 1 | PER-IC-001 | curator_a | 新候选错觉轮廓线索 |
| SA16 | 2026-10-03 | WebSearch | distractor positivity Pd additional singleton paradigm ERP suppression | 9 | 1 | PER-ADDS-001 | curator_a | 新候选附加单例/Pd 线索（标题截断） |
| SA17 | 2026-10-03 | WebSearch | inattentional blindness ERP visual awareness negativity Pitts | 9 | 2 | PER-IB-001 | curator_a | 新候选非注意盲线索 |
| SA18 | 2026-10-03 | WebSearch | change blindness event-related potentials awareness of change Koivisto Revonsuo | 10 | 1 | PER-CB-001 | curator_a | 新候选变化盲线索 |
| SA19 | 2026-10-03 | WebSearch | respiratory-related evoked potential inspiratory occlusion EEG | 10 | 2 | PER-RREP-001 | curator_a | 新候选 RREP 线索 |
| SA20 | 2026-10-03 | WebSearch | Belin voice-selective areas in human auditory cortex temporal voice areas localizer | 10 | 2 | PER-VOICE-001 | curator_a | 新候选嗓音区线索；Edinburgh 数据库页 |
| SA21 | 2026-10-03 | WebSearch | extrastriate body area Downing 2001 cortical area selective for visual processing of the human body | 10 | 2 | PER-BODY-001 | curator_a | 源头候选（DOI 10.1126/science.1063414 可见） |
| SA22 | 2026-10-03 | WebSearch | intermodulation frequency tagging EEG holistic integration Boremanse Norcia Rossion | 10 | 0 | SSR-IM-001 | curator_a | 结果无标题，由 SA27 补全 |
| SA23 | 2026-10-03 | WebSearch | nociceptive steady-state evoked potentials rapid periodic thermal stimulation Mouraux | 10 | 2 | SSR-NSSEP-001 | curator_a | 源头候选及相关线索 |
| SA24 | 2026-10-03 | WebSearch | fast periodic auditory stimulation oddball EEG frequency tagging voice discrimination | 10 | 2 | SSR-FPAS-001 | curator_a | 源头候选及 eNeuro 线索 |
| SA25 | 2026-10-03 | WebSearch | rhythmic visual stimulation entrainment alpha oscillations perception Spaak 2014 Mathewson 2012 | 9 | 1 | SSR-RVS-001 | curator_a | 新候选 α 夹带线索（标题截断） |
| SA26 | 2026-10-03 | WebFetch | https://pmc.ncbi.nlm.nih.gov/articles/PMC5934372 | reCAPTCHA | 0 | SSR-IM-001 | curator_a | 未用 |
| SA27 | 2026-10-03 | WebFetch | https://research.dial.uclouvain.be/entities/publication/293fb0cc-3d48-4391-9cc9-128854424ded | 1 | 1 | SSR-IM-001 | curator_a | Boremanse, Norcia & Rossion 2014 题录（first_source） |
| SA28 | 2026-10-03 | WebFetch | https://research.dial.uclouvain.be/handle/2078.5/160267 | 1 | 1 | SSR-NSSEP-001 | curator_a | Mouraux et al. 2011 题录（first_source） |
| SA29 | 2026-10-03 | WebFetch | https://research.dial.uclouvain.be/handle/2078.5/238396 | 1 | 1 | SSR-FPAS-001 | curator_a | Barbero et al. 2019 会议报告题录（first_source） |
| SA30 | 2026-10-03 | WebSearch | Nozaradan 2011 tagging the neuronal entrainment to beat and meter Journal of Neuroscience | 10 | 1 | SSR-BEAT-001 | curator_a | 源头候选 |
| SA31 | 2026-10-03 | WebSearch | tactile spatial attention somatosensory ERP N140 attended hand Michie Eimer | 9 | 0 | PER-TACT-001 | curator_a | 结果无标题，由 SA35 补全一条 |
| SA32 | 2026-10-03 | WebSearch | high-frequency SSVEP BCI imperceptible flicker above critical flicker fusion | 10 | 1 | SSR-SSVEP-001 | curator_a | 高频 SSVEP 变体出处（Ladouce 2024，标题来自 PDF 文件名） |
| SA33 | 2026-10-03 | WebSearch | Jewett Williston 1971 auditory-evoked far fields averaged from the scalp of humans Brain | 9 | 0 | PER-ABR-001 | curator_a | 未检到源头文献 |
| SA34 | 2026-10-03 | WebFetch | https://research.dial.uclouvain.be/handle/2078.5/97863 | 1 | 1 | SSR-BEAT-001 | curator_a | Nozaradan et al. 2011 题录（first_source） |
| SA35 | 2026-10-03 | WebFetch | https://repository.essex.ac.uk/1230/ | 1 | 1 | PER-TACT-001 | curator_a | Sambo et al. 2009 题录（非源头） |
| SA36 | 2026-10-03 | WebFetch | https://en.wikipedia.org/wiki/Frequency_following_response | 1 | 1 | SSR-FFR-001 | curator_a | Worden & Marsh 1968 参考文献（first_source，人/动物待核） |
| SA37 | 2026-10-03 | WebFetch | https://en.wikipedia.org/wiki/P50_(neuroscience)（R1023） | 1 | 0 | PER-GATE-001 | curator_a | 未说明配对短声范式的提出者 |
| SA38 | 2026-10-03 | WebFetch | https://en.wikipedia.org/wiki/Retinotopy | 1 | 2 | PER-RET-001 | curator_a | DeYoe et al. 1996（first_source）、Engel et al. 1997 |
| SA39 | 2026-10-03 | WebSearch | Adler 1982 neurophysiological evidence for a defect in neuronal mechanisms involved in sensory gating in schizophrenia | 9 | 0 | PER-GATE-001 | curator_a | 未检到源头文献 |
| SA40 | 2026-10-03 | WebSearch | Halliday McDonald Mushin 1972 delayed visual evoked response in optic neuritis Lancet pattern reversal | 10 | 0 | PER-PRVEP-001 | curator_a | 结果无标题，未用 |
| SA41 | 2026-10-03 | WebSearch | Rossion 2014 fast periodic visual stimulation face categorization EEG oddball Liu-Shuang | 10 | 0 | SSR-FPVS-001 | curator_a | 结果无标题，由 SA43 补全一条 |
| SA42 | 2026-10-03 | WebSearch | Sutter 1992 brain response interface real-time communication system m-sequence VEP | 10 | 0 | SSR-CVEP-001 | curator_a | 未检到源头文献 |
| SA43 | 2026-10-03 | WebFetch | https://research.dial.uclouvain.be/handle/2078.5/107553 | 1 | 1 | SSR-FPVS-001 | curator_a | Rossion et al. 2020 综述题录（非源头） |
| SA44 | 2026-10-03 | WebFetch | https://portaldelaciencia.uva.es/documentos/61be2d03baa1ae41a49c5f5a（R0866） | 1 | 0 | SSR-CVEP-001 | curator_a | 补全 R0866 题录；页面未说明 c-VEP 源头 |
| SA45 | 2026-10-03 | WebSearch | Guo Hong Gao 2008 brain-computer interface using motion-onset visual evoked potential J Neural Eng | 9 | 1 | PER-MVEP-001 | curator_a | mVEP-BCI 变体出处 |
| SA46 | 2026-10-03 | WebSearch | Hasson 2004 intersubject synchronization of cortical activity during natural vision Science | 9 | 1 | PER-NAT-001 | curator_a | first_source（PubMed 15016991） |
| SA47 | 2026-10-03 | WebFetch | https://arch.neicon.ru/xmlui/handle/123456789/2112616?show=full | 1 | 1 | PER-MVEP-001 | curator_a | Guo et al. 2008 题录 |
| SA48 | 2026-10-03 | WebFetch | https://www.jneurosci.org/content/26/37/9494 | 1 | 1 | PER-CVA-001 | curator_a | 补全 R0343 题录（DOI 一致） |

合计：WebSearch 28 次（上限 30），WebFetch 20 次（其中 1 次 429、1 次代理 403、1 次 robots 禁止、1 次 reCAPTCHA，均未重试）。WebSearch 结果只返回标题与 URL；DOI/PMID 仅在 URL 或页面中可见时记录。
