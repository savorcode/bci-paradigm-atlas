# 检索记录 · 包 C 错误监测与认知控制 · sprint 2

> 每次检索追加一行，维护者汇总进 `curation/search_protocol.md`（S-003 起）。不使用的检索也要记（命中 0 也记）。

| 编号 | 日期 | 数据库 | 检索式 / URL | 命中数 | 新增文献数 | 相关范式 | 执行人 | 用途 |
|---|---|---|---|---|---|---|---|---|
| S2C-F01 | 2026-10-03 | WebFetch | https://bnci-horizon-2020.eu/database/data-sets | 1 | 1（013-2015 Monitoring ErrP，6 名被试，DOI 10.1109/TNSRE.2010.2053387） | ERR-ERRP-002 | curator_c | 数据集 + 出处 DOI |
| S2C-F02 | 2026-10-03 | WebFetch | https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2017.00360/full（R0714 全文） | 1 | 0（列出观察/监督范式及引文：van Schie 2004、Bates 2005、Koban 2010、Padrão 2016、Pavone 2016、Chavarriaga & Millán 2010、Yeung 2004、Donkers 2005 等） | ERR-OBS-001–003、ERR-ERRP-002、ERR-GAM-003 | curator_c | 拆分依据 |
| S2C-S01 | 2026-10-03 | WebSearch | BCI Challenge NER 2015 error-related potentials P300 speller feedback dataset Perrin 2012 Margaux | 10 | 1（BCI Challenge 页面） | ERR-ERRP-003 | curator_c | 公开数据集 |
| S2C-S02 | 2026-10-03 | WebSearch | error-related potentials during continuous feedback Spüler Niethammer 2015 cursor | 9 | 2（S_SPULER2015；Tübingen 同题学位论文/论文标题） | ERR-ERRP-004 | curator_c | 源头 |
| S2C-F03 | 2026-10-03 | WebFetch | https://neuro.embs.org/2015/bci-challenge/ | 1 | 1（在线 P300 拼写器，错误电位检测；页面称 25 名健康被试；无参考文献） | ERR-ERRP-003 | curator_c | 数据集 |
| S2C-F04 | 2026-10-03 | WebFetch | https://public-pages-files-2025.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2015.00155/text | 1 | 1（S_SPULER2015 书目与任务） | ERR-ERRP-004 | curator_c | 源头 |
| S2C-F05 | 2026-10-03 | WebFetch | https://www.hedtags.org/hed-task/tasks/hedtsk_eriksen_flanker.html | 1 | 0（变体表：箭头版标准、字母版 = Eriksen 1974） | CTL-FLK-002 | curator_c | 配置 |
| S2C-F06 | 2026-10-03 | WebFetch | https://www.hedtags.org/hed-task/tasks/hedtsk_task_switching.html | 1 | 0（变体表：线索、交替序列、自主切换等） | CTL-SW-002、-003 | curator_c | 配置 |
| S2C-F07 | 2026-10-03 | WebFetch | https://www.hedtags.org/hed-task/tasks/hedtsk_continuous_performance.html | 1 | 0（变体表：X-CPT、AX-CPT、gradCPT、Conners 等，无出处） | CTL-CPT-001–003 | curator_c | 配置 |
| S2C-F08 | 2026-10-03 | WebFetch | https://www.hedtags.org/hed-task/tasks/hedtsk_attention_network.html | 1 | 0（ANT、ANT-I、ANT-R 等） | CTL-ANT-002 | curator_c | 配置 |
| S2C-S03 | 2026-10-03 | WebSearch | Callejas Lupiáñez Tudela 2004 attentional networks interact alerting orienting executive ANT-I Brain and Cognition | 9 | 2（S_CALLEJAS2004；Millisecond ANT-I 页） | CTL-ANT-002 | curator_c | 源头 |
| S2C-F09 | 2026-10-03 | WebFetch | https://erpinfo.org/erp-core | 1 | 1（ERP CORE：flankers 范式 LRP/ERN；预印本 doi 10.31234/osf.io/4azqm；数据 doi 10.18115/D5JW4R；未写刺激类型） | CTL-FLK-002 | curator_c | 数据集 |
| S2C-F10 | 2026-10-03 | WebFetch | https://produccioncientifica.ugr.es/documentos/61a1f638bd93e62bb6018a4e?lang=en | 1 | 1（S_CALLEJAS2004 书目：Brain Cogn 54(3):225–227，doi 10.1016/j.bandc.2004.02.012） | CTL-ANT-002 | curator_c | 源头 |
| S2C-F11 | 2026-10-03 | WebFetch | https://www.millisecond.com/library/ant_i | 1 | 1（ANT-I：听觉警觉信号 + 线索有效性；引 Callejas et al. 2005 Exp Brain Res） | CTL-ANT-002 | curator_c | 配置 |
| S2C-S04 | 2026-10-03 | WebSearch | Meiran 1996 reconfiguration of processing mode prior to task performance cued task switching Journal of Experimental Psychology Learning Memory Cognition | 9 | 1（S_MEIRAN1996） | CTL-SW-002 | curator_c | 源头 |
| S2C-S05 | 2026-10-03 | WebSearch | Hester Foxe Molholm Shpaner Garavan 2005 Error Awareness Task go/no-go Stroop aware unaware errors NeuroImage | 10 | 2（S_HESTER2005；PMC3703527 标题） | ERR-AWARE-003 | curator_c | 源头 |
| S2C-S06 | 2026-10-03 | WebSearch | Servan-Schreiber Cohen Steingard 1996 schizophrenic deficits in the processing of context AX continuous performance test Archives of General Psychiatry | 9 | 1（S_SERVANSCHREIBER1996） | CTL-CPT-002 | curator_c | 源头 |
| S2C-F12 | 2026-10-03 | WebFetch | https://collaborate.princeton.edu/en/publications/schizophrenic-deficits-in-the-processing-of-context-a-test-of-a-t/ | 1 | 1（书目 + 摘要） | CTL-CPT-002 | curator_c | 源头 |
| S2C-F13 | 2026-10-03 | WebFetch | https://www.tara.tcd.ie/items/92ce6bd2-3b46-47da-951f-5c85fc63aa79 | 1 | 1（S_HESTER2005 书目：NeuroImage 27(3):602–608） | ERR-AWARE-003 | curator_c | 源头 |
| S2C-F14 | 2026-10-03 | WebFetch | https://www.psytoolkit.org/library/taskswitching_cued.html | 1 | 1（线索任务切换说明；引 Meiran 1996 JEP:LMC 22:1423–1442） | CTL-SW-002 | curator_c | 配置 + 源头 |
| S2C-F15 | 2026-10-03 | WebFetch | https://cognitiveatlas.org/task/id/tsk_nzi0bkdoO8a23 | 1 | 0（EAT 任务定义） | ERR-AWARE-003 | curator_c | 配置 |
| S2C-F16 | 2026-10-03 | WebFetch | https://cprlab.psy.fsu.edu/uploads/1/0/8/8/108887279/the_reward_positivity.pdf（R1093） | 1 | 0（R1093 书目补全：Proudfit 2015 Psychophysiology 10.1111/psyp.12370；doors task 描述，无源头引文） | ERR-GAM-002 | curator_c | 配置 |
| S2C-F17 | 2026-10-03 | WebFetch | https://pubmed.ncbi.nlm.nih.gov/39264479/ → reCAPTCHA，未重试 | 0 | 0 | CTL-STR | curator_c | — |
| S2C-F18 | 2026-10-03 | WebFetch | https://www.hedtags.org/hed-task/tasks/hedtsk_stroop_color_word.html | 1 | 0（变体表：经典、按键、口头、计数 Stroop 等） | CTL-STR-002 | curator_c | 配置 |
| S2C-F19 | 2026-10-03 | WebFetch | https://www.hedtags.org/hed-task/tasks/hedtsk_simon.html | 1 | 0（变体表：视觉标准版、听觉版等） | CTL-SIM-002 | curator_c | 配置 |
| S2C-F20 | 2026-10-03 | WebFetch | https://www.hedtags.org/hed-task/tasks/hedtsk_receive_feedback.html | 1 | 0（无变体） | ERR-GAM | curator_c | — |
| S2C-F21 | 2026-10-03 | WebFetch | https://www.hedtags.org/hed-task/tasks/hedtsk_go_no_go.html | 1 | 0（变体均为参数级或无出处） | CTL-GNG | curator_c | 配置 |
| S2C-F22 | 2026-10-03 | WebFetch | https://www.biorxiv.org/content/10.1101/262576v2（R1001） | 1 | 0（二值奖赏反馈 vs 旋转光标；FRN、P300；页面无作者/年份） | ERR-ADAPT-002 | curator_c | 配置 |
| S2C-F23 | 2026-10-03 | WebFetch | https://openneuro.org/datasets/ds000001 → 空页面；改用 https://openfmri.org/dataset/ds000001 | 1 | 1（ds000001 BART，16 名被试，Schonberg et al. 2012） | CTL-BART-001 | curator_c | 数据集 |
| S2C-F24 | 2026-10-03 | WebFetch | https://frontiersin.org/articles/10.3389/fnrgo.2024.1411305/full（R1258） | 1 | 0（Visual / Vibro / EMS 条件；75/25 匹配/失配） | ERR-VRPE-001 | curator_c | 变体 |
| S2C-S07 | 2026-10-03 | WebSearch | O'Connell Dockree Kelly 2012 supramodal accumulation-to-bound signal centroparietal positivity continuous dot motion detection Nature Neuroscience | 9 | 1（S_KELLY2013；O'Connell 2012 未出现） | CTL-PDM-002 | curator_c | 源头 |
| S2C-F25 | 2026-10-03 | WebFetch | https://edepositireland.ie/handle/2262/71242 | 1 | 1（S_KELLY2013 书目与任务） | CTL-PDM-002 | curator_c | 源头 |
| S2C-F26 | 2026-10-03 | WebFetch | https://www.tara.tcd.ie/items/af4ca618-2215-4c05-92be-340aee10838c | 1 | 0（同 S_KELLY2013） | CTL-PDM-002 | curator_c | — |
