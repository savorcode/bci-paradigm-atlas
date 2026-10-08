# 工作包 C：错误监测与认知控制

> 范式族：错误监测与反馈（error）、认知控制（control）　|　范式 37 个（P1 核心 2、P2 标准 24、P3 长尾 11）　|　文献线索 225 条

> 所有文献均为**自动收集、未核实**的线索：使用前须找到原文核对。标为「检索线索（模型记忆）」的内容没有经过检索确认，只能作为下一步检索的关键词。

## 进度总表

| # | ID | 范式 | 优先级 | 收录判定 | 文献 | 源头候选 | 综述 | 待办 |
|---|---|---|---|---|---|---|---|---|
| 88 | ERR-ERRP-001 | 交互式错误电位 | P1 核心 | 收录 | 3 | 2 | 1 | — |
| 89 | ERR-OBS-001 | 观察性错误 | P1 核心 | 收录 | 2 | 1 | 1 | — |
| 90 | ERR-ADAPT-001 | 运动适应（视觉旋转） | P2 标准 | 收录 | 3 | 1 | 0 | 缺综述 |
| 91 | ERR-AWARE-001 | 错误觉知 | P2 标准 | 收录 | 6 | 1 | 1 | — |
| 92 | ERR-BANDIT-001 | 多臂老虎机（探索-利用） | P2 标准 | 收录 | 5 | 1 | 1 | — |
| 93 | ERR-GAM-001 | 赌博与奖赏反馈 | P2 标准 | 收录 | 3 | 1 | 2 | — |
| 94 | ERR-PRL-001 | 概率反转学习 | P2 标准 | 收录 | 7 | 2 | 1 | — |
| 95 | ERR-PSEL-001 | 概率选择任务 | P2 标准 | 收录（新增，待确认） | 7 | 3 | 0 | 缺综述 |
| 96 | ERR-TE-001 | 时间估计任务 | P2 标准 | 收录 | 2 | 1 | 1 | — |
| 97 | ERR-CAUS-001 | 因果学习 | P3 长尾 | 收录（新增，待确认） | 7 | 3 | 1 | — |
| 98 | ERR-INST-001 | 工具性条件化 | P3 长尾 | 收录（新增，待确认） | 6 | 2 | 0 | 缺综述 |
| 99 | ERR-PCL-001 | 概率分类学习（天气预报任务） | P3 长尾 | 收录（新增，待确认） | 7 | 3 | 0 | 缺综述 |
| 100 | ERR-TS-001 | 两阶段决策（基于模型/无模型） | P3 长尾 | 收录（新增，待确认） | 7 | 3 | 1 | — |
| 101 | CTL-ANT-001 | 注意网络测试 | P2 标准 | 收录 | 6 | 3 | 2 | — |
| 102 | CTL-AS-001 | 反向眼跳 | P2 标准 | 收录 | 7 | 2 | 3 | — |
| 103 | CTL-CNV-001 | S1-S2 预期任务 | P2 标准 | 收录 | 2 | 1 | 1 | — |
| 104 | CTL-CPT-001 | 持续操作任务（AX-CPT） | P2 标准 | 收录 | 7 | 3 | 2 | — |
| 105 | CTL-DD-001 | 延迟折扣 | P2 标准 | 收录 | 5 | 2 | 2 | — |
| 106 | CTL-DT-001 | 双任务 | P2 标准 | 收录 | 6 | 2 | 1 | — |
| 107 | CTL-FLK-001 | Flanker 任务 | P2 标准 | 收录 | 9 | 3 | 2 | — |
| 108 | CTL-GNG-001 | Go/NoGo | P2 标准 | 收录 | 9 | 2 | 4 | — |
| 109 | CTL-IGT-001 | 爱荷华赌博任务 | P2 标准 | 收录 | 8 | 3 | 2 | — |
| 110 | CTL-PDM-001 | 知觉决策（随机点运动） | P2 标准 | 收录 | 7 | 3 | 2 | — |
| 111 | CTL-SART-001 | 持续注意反应任务（SART） | P2 标准 | 收录（新增，待确认） | 10 | 4 | 1 | — |
| 112 | CTL-SIM-001 | Simon 任务 | P2 标准 | 收录 | 7 | 3 | 2 | — |
| 113 | CTL-SST-001 | 停止信号任务 | P2 标准 | 收录 | 10 | 3 | 2 | — |
| 114 | CTL-STR-001 | Stroop 任务 | P2 标准 | 收录 | 7 | 2 | 3 | — |
| 115 | CTL-SW-001 | 任务切换 | P2 标准 | 收录 | 7 | 3 | 2 | — |
| 116 | CTL-TOL-001 | 伦敦塔（计划） | P2 标准 | 收录 | 7 | 3 | 1 | — |
| 117 | CTL-WCST-001 | 威斯康星卡片分类 | P2 标准 | 收录 | 5 | 1 | 2 | — |
| 118 | CTL-BART-001 | 气球模拟风险任务 | P3 长尾 | 收录（新增，待确认） | 6 | 3 | 0 | 缺综述 |
| 119 | CTL-DSST-001 | 数字符号替换 | P3 长尾 | 收录（新增，待确认） | 4 | 0 | 1 | 缺源头候选；需确认神经标记物 |
| 120 | CTL-EFF-001 | 努力决策 | P3 长尾 | 收录（新增，待确认） | 7 | 3 | 1 | — |
| 121 | CTL-RAT-001 | 远距离联想（创造力） | P3 长尾 | 收录（新增，待确认） | 7 | 3 | 0 | 缺综述 |
| 122 | CTL-RAVEN-001 | 瑞文推理 | P3 长尾 | 收录（新增，待确认） | 6 | 2 | 0 | 缺综述；需确认神经标记物 |
| 123 | CTL-TMT-001 | 连线测验 | P3 长尾 | 收录（新增，待确认） | 5 | 2 | 0 | 缺综述；需确认神经标记物 |
| 124 | CTL-WASON-001 | Wason 选择任务 | P3 长尾 | 收录（新增，待确认） | 6 | 3 | 0 | 缺综述 |

## 错误监测与反馈（error）

### ERR-ERRP-001　交互式错误电位　/ Interaction error-related potentials

- **优先级**：P1 核心（BCI 相关度：核心）　**收录判定**：收录（Core BCI paradigm: EEG potentials elicited when an interface/machine misinterprets the user's command.）
- **可能的神经标记物**：ErrP　**记录模态**：EEG
- **别名**：Interaction ErrP; error-related potentials in BCI; iErrP
- **文献线索**（3 条）：
  - [源头候选] Ferrez PW & Millán JdR 2008. Error-Related EEG Potentials Generated during Simulated Brain-Computer Interaction. *IEEE Transactions on Biomedical Engineering 55(3)*.  [R0403](https://publications.idiap.ch/publications/show/46)
  - [源头候选] You are wrong! Automatic detection of interaction errors from brain waves.  [R1085](https://www.academia.edu/125884475/You_are_wrong_automatic_detection_of_interaction_errors_from_brain_waves)
  - [综述] Chavarriaga R et al. 2014. Errare machinale est: the use of error-related potentials in brain-machine interfaces. *Frontiers in Neuroscience*. doi:10.3389/fnins.2014.00208 [R0603](https://www.frontiersin.org/articles/10.3389/fnins.2014.00208/text)
- **检索线索（模型记忆，未核实）**：BNCI Horizon 2020 dataset 'Monitoring error-related potentials' (013-2015, Chavarriaga & Millán) likely exists; not confirmed via search. 'You are wrong!' is Ferrez & Millán IJCAI 2005 (unconfirmed).

### ERR-OBS-001　观察性错误　/ Observation of errors

- **优先级**：P1 核心（BCI 相关度：核心）　**收录判定**：收录（Distinct paradigm: observing another agent's (human or machine) errors elicits observer ERN (oERN)/ErrP; basis for passive-BCI error monitoring. Closely related to ERR-ERRP-001 but the subject is not the actor.）
- **可能的神经标记物**：oERN; ErrP　**记录模态**：EEG
- **别名**：Observed error paradigm; oERN; observation ErrP; observer ERN
- **文献线索**（2 条）：
  - [源头候选] van Schie HT & x 2004. Modulation of activity in medial frontal and motor cortices during error observation. *Nature Neuroscience*. doi:10.1038/nn1239 [R0279](https://link.springer.com/article/10.1038/nn1239)
  - [综述] Somon B & x 2017. Performance Monitoring Applied to System Supervision. *Frontiers in Human Neuroscience*. doi:10.3389/fnhum.2017.00360 [R0714](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2017.00360/full)
- **检索线索（模型记忆，未核实）**：Miltner, Brauer, Hecht, Trippe & Coles 2004 (J Cogn Neurosci) 'Parallel brain activity for self-generated and observed errors' is another origin candidate; not confirmed via search.

### ERR-ADAPT-001　运动适应（视觉旋转）　/ Visuomotor adaptation

- **优先级**：P2 标准（BCI 相关度：相关）　**收录判定**：收录（Visuomotor rotation/adaptation is a distinct sensorimotor-error paradigm (sensory vs reward prediction errors; FRN, P300, beta rebound) used in EEG and motor BCI research.）
- **可能的神经标记物**：FRN; ErrP　**记录模态**：EEG
- **别名**：Cursor rotation adaptation; Visuomotor adaptation task; Visuomotor rotation
- **文献线索**（3 条）：
  - [源头候选] Krakauer JW & x 2000. Learning of visuomotor transformations for vectorial planning of reaching trajectories. *Journal of Neuroscience 20(23)*.  [R0194](https://www.jneurosci.org/content/jneuro/20/23/8916.full.pdf)
  - [方法/基准] Neural Signatures of Reward and Sensory Prediction Error in Motor Learning. *bioRxiv*. doi:10.1101/262576 [R1001](https://www.biorxiv.org/content/10.1101/262576v2)
  - [方法/基准] Neural signatures of reward and sensory error feedback processing in motor learning.  [R1009](https://ir.lib.uwo.ca/brainpub/488)
- **检索线索（模型记忆，未核实）**：Review candidate: Krakauer JW, Hadjiosif AM, Xu J, Wong AL, Haith AM (2019) 'Motor learning', Comprehensive Physiology - not confirmed via search. EEG/FRN-in-adaptation paper above is Palidis DJ et al. (J Neurophysiol 2019) per memory. Early rotation adaptation: Cunningham 1989.
- **检索备注**：No review confirmed for this row.

### ERR-AWARE-001　错误觉知　/ Error awareness

- **优先级**：P2 标准（BCI 相关度：相关）　**收录判定**：收录（Error-awareness paradigms (e.g., error-signalling/antisaccade or Go/NoGo with awareness reports) dissociate aware vs unaware errors, with the Pe tracking awareness; distinct question, though implemented on top of flanker/GNG/antisaccade tasks.）
- **可能的神经标记物**：Pe　**记录模态**：EEG
- **别名**：Aware vs unaware errors; Error Awareness Task (EAT); Error awareness paradigm; Error signaling task
- **文献线索**（6 条）：
  - [源头候选] Gehring WJ et al. 1990. The error-related negativity: an event-related brain potential accompanying errors.  [R0094]
  - [综述] Falkenstein M et al. 2000. ERP components on reaction errors and their functional significance: a tutorial. *Biological Psychology 51 (2–3): 87–107*. doi:10.1016/s0301-0511(99)00031-9 [R0190](https://doi.org/10.1016/s0301-0511(99)00031-9)
  - [其他] Nieuwenhuis S et al. 2001. Error-related brain potentials are differentially related to awareness of response errors: evidence from an antisaccade task. *Psychophysiology 38 (5): 752–60*. doi:10.1111/1469-8986.3850752 [R0205](https://doi.org/10.1111/1469-8986.3850752)
  - [其他] Scheffers MK & Coles MG 2000. Performance monitoring in a confusing world: error-related brain activity, judgments of response accuracy, and types of errors. *Journal of Experimental Psychology. Human Perception and Performance 26 (1): 141–51*. doi:10.1037/0096-1523.26.1.141 [R0195](https://doi.org/10.1037/0096-1523.26.1.141)
  - [其他] Olvet DM & Hajcak G 2008. The error-related negativity (ERN) and psychopathology: toward an endophenotype. *Clinical Psychology Review 28 (8): 1343–54*. doi:10.1016/j.cpr.2008.07.003 [R0421](https://doi.org/10.1016/j.cpr.2008.07.003)
  - [其他] Holroyd CB & Coles MG 2002. The neural basis of human error processing: reinforcement learning, dopamine, and the error-related negativity. *Psychological Review 109 (4): 679–709*. doi:10.1037/0033-295x.109.4.679 [R0236](https://doi.org/10.1037/0033-295x.109.4.679)
- **检索线索（模型记忆，未核实）**：Not confirmed (search budget exhausted): Nieuwenhuis, Ridderinkhof, Blom, Band & Kok 2001 (Psychophysiology) 'Error-related brain potentials are differentially related to awareness of response errors: evidence from an antisaccade task'; Hester et al. 2005 Error Awareness Task (NeuroImage); review Wessel 2012 (Front Hum Neurosci) 'Error awareness and the error-related negativity: evaluating the first decade of evidence'; Overbeek, Nieuwenhuis & Ridderinkhof 2005 Pe review (J Psychophysiol).
- **检索备注**：No reference could be verified for this row; needs follow-up. Consider tagging as variant overlay on CTL-FLK-001 / CTL-AS-001.

### ERR-BANDIT-001　多臂老虎机（探索-利用）　/ Multi-armed bandit

- **优先级**：P2 标准（BCI 相关度：基础）　**收录判定**：收录（Multi-armed (restless/volatile) bandit is the standard explore-exploit paradigm (frontopolar BOLD for exploration; FRN/RewP to outcomes); distinct from reversal learning by continuous drifting payoffs and explicit exploration.）
- **可能的神经标记物**：FRN; 前额 BOLD　**记录模态**：EEG; fMRI
- **别名**：Bandit Task; Explore-exploit task; K-Armed Bandit; MAB; Multi-Armed Bandit; Multi-armed bandit; Restless bandit; Volatile bandit
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_multi_armed_bandit.html
- **文献线索**（5 条）：
  - [源头候选、关键文献(HED)] Daw ND & x 2006. Cortical substrates for exploratory decisions in humans. *Nature 441*. doi:10.1038/nature04766 [R0338](https://pubmed.ncbi.nlm.nih.gov/16778890/)
  - [延伸文献(HED)、综述] Schulz E & Gershman SJ 2019. The algorithmic architecture of exploration in the human brain. *Current Opinion in Neurobiology 55*. doi:10.1016/j.conb.2018.11.003 [R0781](https://pubmed.ncbi.nlm.nih.gov/30529148/)
  - [延伸文献(HED)、方法/基准] Gershman SJ 2018. Deconstructing the human algorithms for exploration. *Cognition 173*. doi:10.1016/j.cognition.2017.12.014 [R0737](https://pubmed.ncbi.nlm.nih.gov/29289795/)
  - [延伸文献(HED)] Cogliati Dezza et al. 2017. Learning the value of information and reward over time when solving exploration–exploitation problems. *Scientific Reports, 7, 16919*. doi:10.1038/s41598-017-17237-w [R0706](https://doi.org/10.1038/s41598-017-17237-w)
  - [延伸文献(HED)] Chakroun et al. 2020. Dopaminergic modulation of the exploration/exploitation trade-off in human decision-making. *eLife, 9, e51260*. doi:10.7554/elife.51260 [R0794](https://doi.org/10.7554/elife.51260)
- **检索线索（模型记忆，未核实）**：Wilson et al. 2014 'Horizon task' (J Exp Psychol Gen) for directed vs random exploration - not confirmed. Family 'error' fits loosely; could also be 'decision'.
- **检索备注**：From HED multi-armed bandit page https://www.hedtags.org/hed-task/tasks/hedtsk_multi_armed_bandit.html (fetched).

### ERR-GAM-001　赌博与奖赏反馈　/ Gambling / reward feedback

- **优先级**：P2 标准（BCI 相关度：相关）　**收录判定**：收录（Classic simple-gambling / doors / reward-feedback paradigm eliciting the FRN / reward positivity (RewP); distinct from response-locked error paradigms.）
- **可能的神经标记物**：FRN (RewP)　**记录模态**：EEG
- **别名**：Doors task; FRN paradigm; Feedback Block; Performance Feedback; RewP paradigm; Reward feedback paradigm; Score Screen; Simple gambling task
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_receive_feedback.html
- **文献线索**（3 条）：
  - [源头候选] Gehring WJ & Willoughby AR 2002. The medial frontal cortex and the rapid processing of monetary gains and losses. *Science*. PMID 11910116 [R0235](https://pubmed.ncbi.nlm.nih.gov/11910116/)
  - [综述] Sambrook TD & Goslin J. A neural reward prediction error revealed by a meta-analysis of ERPs using great grand averages. *Psychological Bulletin 141(1)*.  [R0840](https://research-portal.uea.ac.uk/en/publications/a-neural-reward-prediction-error-revealed-by-a-meta-analysis-of-e/)
  - [综述] the reward positivity (PDF, FSU CPR lab).  [R1093](https://cprlab.psy.fsu.edu/uploads/1/0/8/8/108887279/the_reward_positivity.pdf)
- **检索线索（模型记忆，未核实）**：The FSU PDF is probably Proudfit GH (2015) 'The reward positivity: from basic research on reward to a biomarker for depression', Psychophysiology 52:449-459 - not confirmed. Origin also: Miltner, Braun & Coles 1997 (J Cogn Neurosci) feedback ERN in time estimation. Sambrook & Goslin year 2015 from memory. Doors task: Foti & Hajcak.
- **检索备注**：Venue for Sambrook & Goslin inferred from PDF filename 'bul_141_1_213'.

### ERR-PRL-001　概率反转学习　/ Probabilistic reversal learning

- **优先级**：P2 标准（BCI 相关度：基础）　**收录判定**：收录（Standard reinforcement-learning/cognitive-flexibility paradigm with probabilistic feedback and contingency reversals; FRN in EEG, striatal/OFC BOLD in fMRI.）
- **可能的神经标记物**：FRN; 纹状体 BOLD　**记录模态**：EEG; fMRI
- **别名**：PRL; Probabilistic Reversal Learning; Probabilistic reversal learning task; Reversal learning task
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_reversal_learning.html
- **文献线索**（7 条）：
  - [源头候选、关键文献(HED)] Cools et al. 2002. Defining the neural mechanisms of probabilistic reversal learning using event-related functional magnetic resonance imaging. *Journal of Neuroscience*. doi:10.1523/jneurosci.22-11-04563.2002 [R0223](https://doi.org/10.1523/jneurosci.22-11-04563.2002)
  - [关键文献(HED)] Dias et al. 1996. Dissociation in prefrontal cortex of affective and attentional shifts. *Nature*. doi:10.1038/380069a0 [R0130](https://doi.org/10.1038/380069a0)
  - [延伸文献(HED)、综述] Izquierdo et al. 2017. The neural basis of reversal learning: An updated perspective. *Neuroscience*. doi:10.1016/j.neuroscience.2016.03.021 [R0725](https://doi.org/10.1016/j.neuroscience.2016.03.021)
  - [方法/基准] Cognitive Atlas task page (surfaced for probabilistic reversal learning query; task name not verified). *Cognitive Atlas*.  [R0873](https://cognitiveatlas.org/task/id/trm_4da6318f7381b)
  - [延伸文献(HED)] den Ouden et al. 2013. Dissociable effects of dopamine and serotonin on reversal learning. *Neuron*. doi:10.1016/j.neuron.2013.08.030 [R0570](https://doi.org/10.1016/j.neuron.2013.08.030)
  - [延伸文献(HED)] Schlagenhauf et al. 2014. Striatal dysfunction during reversal learning in unmedicated schizophrenia patients. *NeuroImage*. doi:10.1016/j.neuroimage.2013.11.034 [R0616](https://doi.org/10.1016/j.neuroimage.2013.11.034)
  - [延伸文献(HED)] Costa et al. 2015. Reversal learning and dopamine: A Bayesian perspective. *Journal of Neuroscience*. doi:10.1523/jneurosci.1989-14.2015 [R0657](https://doi.org/10.1523/jneurosci.1989-14.2015)
- **检索线索（模型记忆，未核实）**：Izquierdo et al. review is Neuroscience 2017 (memory). Neurosynth lists Cools 2002 under study id 12040063 (likely PMID).
- **检索备注**：Neurosynth URL for Cools 2002: https://neurosynth.org/studies/12040063

### ERR-PSEL-001　概率选择任务　/ Probabilistic selection task

- **优先级**：P2 标准（BCI 相关度：基础）　**收录判定**：收录（新增，待确认）
- **可能的神经标记物**：FRN; 额中线 θ　**记录模态**：EEG; fMRI
- **别名**：Frank Task; PSS; PST; Probabilistic Selection; Probabilistic Stimulus Selection Task
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_probabilistic_selection.html
- **文献线索**（7 条）：
  - [源头候选、关键文献(HED)] Frank MJ et al. 2004. By carrot or by stick: Cognitive reinforcement learning in parkinsonism. *Science 306(5703)*. doi:10.1126/science.1102941 [R0272](https://pubmed.ncbi.nlm.nih.gov/15528409/)
  - [关键文献(HED)] Frank et al. 2007. Genetic triple dissociation reveals multiple roles for dopamine in reinforcement learning. *Proceedings of the National Academy of Sciences*. doi:10.1073/pnas.0706111104 [R0365](https://doi.org/10.1073/pnas.0706111104)
  - [关键文献(HED)] Frank 2005. Dynamic dopamine modulation in the basal ganglia: A neurocomputational account of cognitive deficits in medicated and nonmedicated parkinsonism. *Journal of Cognitive Neuroscience*. doi:10.1162/0898929052880093 [R0310](https://doi.org/10.1162/0898929052880093)
  - [延伸文献(HED)、方法/基准] Cavanagh JF & x 2010. Frontal theta links prediction errors to behavioral adaptation in reinforcement learning. *NeuroImage 49(4)*. doi:10.1016/j.neuroimage.2009.11.080 [R0463](https://pubmed.ncbi.nlm.nih.gov/19969093/)
  - [延伸文献(HED)] Waltz et al. 2007. Selective reinforcement learning deficits in schizophrenia support predictions from computational models of striatal-cortical dysfunction. *Biological Psychiatry*. doi:10.1016/j.biopsych.2006.09.042 [R0378](https://doi.org/10.1016/j.biopsych.2006.09.042)
  - [延伸文献(HED)] Doll et al. 2009. Instructional control of reinforcement learning: A behavioral and neurocomputational investigation. *Brain Research*. doi:10.1016/j.brainres.2009.07.007 [R0439](https://doi.org/10.1016/j.brainres.2009.07.007)
  - [延伸文献(HED)] Bodi et al. 2009. Reward-learning and the novelty-seeking personality: A between- and within-subjects study of the effects of dopamine agonists on young Parkinson's patients. *Brain*. doi:10.1093/brain/awp094 [R0440](https://doi.org/10.1093/brain/awp094)

### ERR-TE-001　时间估计任务　/ Time estimation task

- **优先级**：P2 标准（BCI 相关度：基础）　**收录判定**：收录（Time-estimation task with correct/incorrect feedback is the original paradigm in which the feedback ERN/FRN was described; distinct from gambling feedback (performance-contingent feedback).）
- **可能的神经标记物**：FRN　**记录模态**：EEG
- **别名**：Interval estimation with feedback; Miltner time-estimation task; Time estimation task
- **文献线索**（2 条）：
  - [源头候选] Miltner WHR et al. 1997. Event-related brain potentials following incorrect feedback in a time-estimation task: evidence for a generic neural system for error detection. *Journal of Cognitive Neuroscience*. doi:10.1162/jocn.1997.9.6.788 [R0146](https://www.citedrive.com/en/discovery/event-related-brain-potentials-following-incorrect-feedback-in-a-time-estimation-task-evidence-for-a-generic-neural-system-for-error-detection)
  - [综述] Learning from experience: event-related potential correlates of reward processing, neural adaptation, and behavioral choice.  [R0969](https://pmc.ncbi.nlm.nih.gov/articles/PMC3432149)
- **检索线索（模型记忆，未核实）**：Review is likely Walsh MM & Anderson JR (2012) Neurosci Biobehav Rev; authors/year not confirmed (PMC page blocked).
- **检索备注**：Review URL matched via exact-title search only; PMC page could not be fetched.

### ERR-CAUS-001　因果学习　/ Causal learning

- **优先级**：P3 长尾（BCI 相关度：基础）　**收录判定**：收录（新增，待确认）
- **可能的神经标记物**：预测误差 BOLD　**记录模态**：fMRI
- **别名**：Allergy Prediction Task; Causal Induction Task; Causal Judgment Task; Contingency Judgment Task; Contingency Learning Task; Delta-P Task
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_causal_learning.html
- **文献线索**（7 条）：
  - [关键文献(HED)] Shanks & Dickinson 1987. Associative accounts of causality judgment. *Psychology of Learning and Motivation, 21, 229-261*. doi:10.1016/s0079-7421(08)60030-4 [R0077](https://doi.org/10.1016/s0079-7421(08)60030-4)
  - [关键文献(HED)] Cheng 1997. From covariation to causation: A causal power theory. *Psychological Review, 104(2), 367-405*. doi:10.1037/0033-295x.104.2.367 [R0147](https://doi.org/10.1037/0033-295x.104.2.367)
  - [关键文献(HED)] Dickinson et al. 1984. Judgement of act-outcome contingency: The role of selective attribution. *Quarterly Journal of Experimental Psychology Section A, 36(1), 29-50*. doi:10.1080/14640748408401502 [R0066](https://doi.org/10.1080/14640748408401502)
  - [综述] De Houwer & Beckers 2002. A review of recent developments in research and theories on human contingency learning. *Quarterly Journal of Experimental Psychology Section B, 55(4), 289-310*. doi:10.1080/02724990244000034 [R0218](https://doi.org/10.1080/02724990244000034)
  - [延伸文献(HED)] Griffiths & Tenenbaum 2005. Structure and strength in causal induction. *Cognitive Psychology, 51(4), 334-384*. doi:10.1016/j.cogpsych.2005.05.004 [R0327](https://doi.org/10.1016/j.cogpsych.2005.05.004)
  - [延伸文献(HED)] Perales et al. 2005. Dissociation between judgments and outcome-expectancy measures in covariation learning: A signal detection theory approach. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 31(5), 1105-1120*. doi:10.1037/0278-7393.31.5.1105 [R0307](https://doi.org/10.1037/0278-7393.31.5.1105)
  - [延伸文献(HED)] Lu et al. 2008. Bayesian generic priors for causal learning. *Psychological Review, 115(4), 955-984*. doi:10.1037/a0013256 [R0396](https://doi.org/10.1037/a0013256)

### ERR-INST-001　工具性条件化　/ Instrumental conditioning

- **优先级**：P3 长尾（BCI 相关度：基础）　**收录判定**：收录（新增，待确认）
- **可能的神经标记物**：FRN; 纹状体 BOLD　**记录模态**：EEG; fMRI
- **别名**：Instrumental Learning; Operant Conditioning; PIT; Pavlovian-Instrumental Transfer
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_instrumental_conditioning.html
- **文献线索**（6 条）：
  - [关键文献(HED)] Schultz et al. 1997. A neural substrate of prediction and reward. *Science, 275(5306), 1593-1599*. doi:10.1126/science.275.5306.1593 [R0140](https://doi.org/10.1126/science.275.5306.1593)
  - [关键文献(HED)] Haber & Knutson 2010. The reward circuit: Linking primate anatomy and human imaging. *Neuropsychopharmacology, 35(1), 4-26*. doi:10.1038/npp.2010.129 [R0489](https://doi.org/10.1038/npp.2010.129)
  - [延伸文献(HED)] Balleine & O'Doherty 2010. Human and rodent homologies in action control: Corticostriatal determinants of goal-directed and habitual action. *Neuropsychopharmacology, 35(1), 48–69*. doi:10.1038/npp.2009.131 [R0466](https://doi.org/10.1038/npp.2009.131)
  - [延伸文献(HED)] Dolan RJ & Dayan P 2013. Goals and habits in the brain. *Neuron 80(2)*. doi:10.1016/j.neuron.2013.09.007 [R0572](https://pubmed.ncbi.nlm.nih.gov/24139036/)
  - [延伸文献(HED)] Lee et al. 2014. Neural computations underlying arbitration between model-based and model-free learning. *Neuron, 81(3), 687–699*. doi:10.1016/j.neuron.2013.11.028 [R0609](https://doi.org/10.1016/j.neuron.2013.11.028)
  - [延伸文献(HED)] Gillan et al. 2016. Characterizing a psychiatric symptom dimension related to deficits in goal-directed control. *eLife, 5, e11305*. doi:10.7554/elife.11305 [R0673](https://doi.org/10.7554/elife.11305)

### ERR-PCL-001　概率分类学习（天气预报任务）　/ Probabilistic classification learning

- **优先级**：P3 长尾（BCI 相关度：基础）　**收录判定**：收录（新增，待确认）
- **可能的神经标记物**：纹状体 BOLD　**记录模态**：fMRI
- **别名**：Probabilistic Classification Learning; WPT; Weather Prediction; Weather Prediction Task
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_probabilistic_classification_learning.html
- **文献线索**（7 条）：
  - [关键文献(HED)] Knowlton et al. 1994. Probabilistic classification learning in amnesia. *Learning & Memory*. doi:10.1101/lm.1.2.106 [R0118](https://doi.org/10.1101/lm.1.2.106)
  - [关键文献(HED)] Poldrack et al. 1999. Striatal activation during acquisition of a cognitive skill. *Neuropsychology*. doi:10.1037/0894-4105.13.4.564 [R0182](https://doi.org/10.1037/0894-4105.13.4.564)
  - [关键文献(HED)] Seger 2008. How do the basal ganglia contribute to categorization? Their roles in generalization, response selection, and learning via feedback.. *Neuroscience & Biobehavioral Reviews*. doi:10.1016/j.neubiorev.2007.07.010 [R0406](https://doi.org/10.1016/j.neubiorev.2007.07.010)
  - [延伸文献(HED)] Knowlton & Patterson 2018. Habit formation and the striatum. *Current Topics in Behavioral Neurosciences*. doi:10.1007/7854_2016_451 [R0740](https://doi.org/10.1007/7854_2016_451)
  - [延伸文献(HED)] Meeter et al. 2006. Strategies in probabilistic categorization: Results from a new way of analyzing performance. *Learning & Memory*. doi:10.1101/lm.43006 [R0352](https://doi.org/10.1101/lm.43006)
  - [延伸文献(HED)] Price 2009. Distinguishing the contributions of implicit and explicit processes to performance of the weather prediction task. *Memory & Cognition*. doi:10.3758/mc.37.2.210 [R0434](https://doi.org/10.3758/mc.37.2.210)
  - [延伸文献(HED)] Foerde et al. 2006. Modulation of competing memory systems by distraction. *Proceedings of the National Academy of Sciences*. doi:10.1073/pnas.0602659103 [R0344](https://doi.org/10.1073/pnas.0602659103)

### ERR-TS-001　两阶段决策（基于模型/无模型）　/ Two-stage decision task

- **优先级**：P3 长尾（BCI 相关度：基础）　**收录判定**：收录（新增，待确认）
- **可能的神经标记物**：纹状体 BOLD; FRN　**记录模态**：fMRI; EEG
- **别名**：Daw Task; MB/MF Task; Two-Step Task
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_two_stage_decision.html
- **文献线索**（7 条）：
  - [源头候选、关键文献(HED)] Daw ND & x 2011. Model-based influences on humans' choices and striatal prediction errors. *Neuron 69(6)*. doi:10.1016/j.neuron.2011.02.027 [R0510](https://pubmed.ncbi.nlm.nih.gov/21435563/)
  - [关键文献(HED)、综述] Dolan RJ & Dayan P 2013. Goals and habits in the brain. *Neuron 80(2)*. doi:10.1016/j.neuron.2013.09.007 [R0572](https://pubmed.ncbi.nlm.nih.gov/24139036/)
  - [关键文献(HED)] Glascher et al. 2010. States versus rewards: Dissociable neural prediction error signals underlying model-based and model-free reinforcement learning. *Neuron*. doi:10.1016/j.neuron.2010.04.016 [R0482](https://doi.org/10.1016/j.neuron.2010.04.016)
  - [延伸文献(HED)] Kool et al. 2016. When does model-based control pay off?. *PLoS Computational Biology*. doi:10.1371/journal.pcbi.1005090 [R0692](https://doi.org/10.1371/journal.pcbi.1005090)
  - [延伸文献(HED)] Gillan et al. 2016. Characterizing a psychiatric symptom dimension related to deficits in goal-directed control. *eLife, 5, e11305*. doi:10.7554/elife.11305 [R0673](https://doi.org/10.7554/elife.11305)
  - [延伸文献(HED)] da Silva & Hare 2020. Humans primarily use model-based inference in the two-stage task. *Nature Human Behaviour*. doi:10.1038/s41562-020-0905-y [R0796](https://doi.org/10.1038/s41562-020-0905-y)
  - [延伸文献(HED)] Feher da Silva & Hare 2018. A note on the analysis of two-stage task results: How changes in task structure affect what model-free and model-based strategies predict about the effects of reward and transition on the stay probability. *PLoS ONE*. doi:10.1371/journal.pone.0195328 [R0730](https://doi.org/10.1371/journal.pone.0195328)


## 认知控制（control）

### CTL-ANT-001　注意网络测试　/ Attention Network Test (ANT)

- **优先级**：P2 标准（BCI 相关度：基础）　**收录判定**：收录（Attention Network Test combines cueing and flanker to index alerting, orienting and executive networks; a standardized composite paradigm (cue N1/P1, CNV, P3).）
- **可能的神经标记物**：N1; P3; CNV　**记录模态**：EEG; fMRI
- **别名**：ANT; ANT-I (interaction variant); Attention Network Test; Clinical Screening ANT
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_attention_network.html
- **文献线索**（6 条）：
  - [源头候选、关键文献(HED)] Fan J & x 2002. Testing the efficiency and independence of attentional networks. *Journal of Cognitive Neuroscience 14(3)*. doi:10.1162/089892902317361886 [R0234](https://pubmed.ncbi.nlm.nih.gov/11970796/)
  - [关键文献(HED)、方法/基准] Fan J & x 2005. The activation of attentional networks. *NeuroImage 26(2)*. doi:10.1016/j.neuroimage.2005.02.004 [R0329](https://pubmed.ncbi.nlm.nih.gov/15907304/)
  - [关键文献(HED)、综述] Petersen SE & Posner MI 2012. The attention system of the human brain: 20 years after. *Annual Review of Neuroscience 35*. doi:10.1146/annurev-neuro-062111-150525 [R0557](https://pubmed.ncbi.nlm.nih.gov/22524787/)
  - [延伸文献(HED)、综述] MacLeod JW & x 2010. Appraising the ANT: Psychometric and theoretical considerations of the Attention Network Test. *Neuropsychology 24(5)*. doi:10.1037/a0019803 [R0456](https://pubmed.ncbi.nlm.nih.gov/20804252/)
  - [延伸文献(HED)] Arora et al. 2020. The Attention Network Test database: ADHD and cross-cultural applications. *Frontiers in Psychology, 11, 388*. doi:10.3389/fpsyg.2020.00388 [R0801](https://doi.org/10.3389/fpsyg.2020.00388)
  - [延伸文献(HED)] Ishigami & Klein 2010. Repeated measurement of the components of attention using two versions of the Attention Network Test (ANT): Stability, isolability, robustness, and reliability. *Journal of Neuroscience Methods, 190(1), 117–128*. doi:10.1016/j.jneumeth.2010.04.019 [R0476](https://doi.org/10.1016/j.jneumeth.2010.04.019)
- **检索备注**：From HED ANT page https://www.hedtags.org/hed-task/tasks/hedtsk_attention_network.html (fetched). Arora, Lawrence & Klein 2020 'The Attention Network Test database' (Front Psychol, PMID 32292363) is a behavioral-data compilation, not neural.

### CTL-AS-001　反向眼跳　/ Antisaccade task

- **优先级**：P2 标准（BCI 相关度：基础）　**收录判定**：收录（Canonical oculomotor inhibition paradigm (look away from a sudden target); presaccadic negativity/EEG and FEF/DLPFC fMRI.）
- **可能的神经标记物**：眼跳前电位　**记录模态**：EEG; fMRI
- **别名**：AST; Anti-Saccade; Anti-saccade; Antisaccade; Antisaccade task; Pro/antisaccade task
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_anti_saccade.html
- **文献线索**（7 条）：
  - [源头候选、关键文献(HED)] Hallett PE 1978. Primary and secondary saccades to goals defined by instructions. *Vision Research 18(11)*. doi:10.1016/0042-6989(78)90218-3 [R0045](https://www.hedtags.org/hed-task/tasks/hedtsk_anti_saccade.html)
  - [关键文献(HED)、综述] Munoz DP & Everling S 2004. Look away: The anti-saccade task and the voluntary control of eye movement. *Nature Reviews Neuroscience 5(3)*. doi:10.1038/nrn1345 [R0278](https://www.hedtags.org/hed-task/tasks/hedtsk_anti_saccade.html)
  - [综述] Hutton SB & Ettinger U 2006. The antisaccade task as a research tool in psychopathology: A critical review. *Psychophysiology 43(3)*. doi:10.1111/j.1469-8986.2006.00403.x [R0355](https://www.hedtags.org/hed-task/tasks/hedtsk_anti_saccade.html)
  - [综述] Everling & Fischer 1998. The antisaccade: A review of basic research and clinical findings. *Neuropsychologia*. doi:10.1016/s0028-3932(98)00020-7 [R0171](https://doi.org/10.1016/s0028-3932(98)00020-7)
  - [延伸文献(HED)、方法/基准] Antoniades CA & x 2013. An internationally standardised antisaccade protocol. *Vision Research 84*. doi:10.1016/j.visres.2013.02.007 [R0566](https://www.hedtags.org/hed-task/tasks/hedtsk_anti_saccade.html)
  - [延伸文献(HED)] Crawford et al. 2005. Inhibitory control of saccadic eye movements and cognitive impairment in Alzheimer's disease. *Biological Psychiatry*. doi:10.1016/j.biopsych.2005.01.017 [R0313](https://doi.org/10.1016/j.biopsych.2005.01.017)
  - [延伸文献(HED)] Munoz et al. 2003. Altered control of visual fixation and saccadic eye movements in attention-deficit hyperactivity disorder. *Journal of Neurophysiology*. doi:10.1152/jn.00192.2003 [R0246](https://doi.org/10.1152/jn.00192.2003)
- **检索备注**：Citations taken from HED task catalog page (fetched).

### CTL-CNV-001　S1-S2 预期任务　/ S1-S2 paradigm

- **优先级**：P2 标准（BCI 相关度：相关）　**收录判定**：收录（S1-S2 (warned reaction time) paradigm is the classic elicitor of the CNV, an anticipatory slow potential; foundational for anticipation/preparation markers.）
- **可能的神经标记物**：CNV　**记录模态**：EEG
- **别名**：CNV paradigm; Contingent negative variation paradigm; S1-S2 paradigm; Warned reaction-time paradigm
- **文献线索**（2 条）：
  - [源头候选] Walter WG & x 1964. Contingent Negative Variation: an electric sign of sensorimotor association and expectancy in the human brain. *Nature 203(4943)*. doi:10.1038/203380a0 [R0010](https://pubmed.ncbi.nlm.nih.gov/14197376/)
  - [综述] Tecce JJ 1972. Contingent negative variation (CNV) and psychological processes in man. *Psychological Bulletin 77(2)*. doi:10.1037/h0032177 [R0026](https://pubmed.ncbi.nlm.nih.gov/4621420/)
- **检索线索（模型记忆，未核实）**：Loveless & Sanford 1975 (early O-wave / late E-wave CNV distinction) cited on Wikipedia; a more recent review would be desirable (e.g., Kononowicz & Penney 2016 'The contingent negative variation (CNV): timing isn't everything', not confirmed).
- **检索备注**：Citations and PMIDs from Wikipedia 'Contingent negative variation' reference list (https://en.wikipedia.org/wiki/Contingent_negative_variation, fetched); PubMed URLs constructed from those PMIDs.

### CTL-CPT-001　持续操作任务（AX-CPT）　/ Continuous performance task (AX-CPT)

- **优先级**：P2 标准（BCI 相关度：相关）　**收录判定**：收录（Continuous performance tests (incl. the AX-CPT context-maintenance variant) are canonical sustained-attention/proactive-control paradigms (CNV, P3; DLPFC/ACC fMRI).）
- **可能的神经标记物**：CNV; P3　**记录模态**：EEG; fMRI
- **别名**：AX continuous performance task; AX-CPT; AX-CPT variant; CPT; CPT-II; CPT-X; Continuous Performance
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_continuous_performance.html
- **文献线索**（7 条）：
  - [源头候选、关键文献(HED)] Rosvold HE & x 1956. A continuous performance test of brain damage. *Journal of Consulting Psychology 20(5)*. doi:10.1037/h0043220 [R0003](https://www.hedtags.org/hed-task/tasks/hedtsk_continuous_performance.html)
  - [关键文献(HED)、方法/基准] Carter CS & x 1998. Anterior cingulate cortex, error detection, and the online monitoring of performance. *Science 280(5364)*. doi:10.1126/science.280.5364.747 [R0158](https://www.hedtags.org/hed-task/tasks/hedtsk_continuous_performance.html)
  - [关键文献(HED)] Nuechterlein et al. 1983. Visual sustained attention: Image degradation produces rapid sensitivity decrement over time. *Science, 220(4594), 327-329*. doi:10.1126/science.6836276 [R0063](https://doi.org/10.1126/science.6836276)
  - [延伸文献(HED)、综述] Fortenbaugh FC & x 2017. Recent theoretical, neural, and clinical advances in sustained attention research. *Annals of the New York Academy of Sciences 1396(1)*. doi:10.1111/nyas.13318 [R0715](https://www.hedtags.org/hed-task/tasks/hedtsk_continuous_performance.html)
  - [综述] Huang-Pollock CL & x 2012. Evaluating vigilance deficits in ADHD: A meta-analysis of CPT performance. *Journal of Abnormal Psychology 121(2)*. doi:10.1037/a0027205 [R0538](https://www.hedtags.org/hed-task/tasks/hedtsk_continuous_performance.html)
  - [延伸文献(HED)] Esterman et al. 2013. In the zone or zoning out? Tracking behavioral and neural fluctuations during sustained attention. *Cerebral Cortex, 23(11), 2712–2723*. doi:10.1093/cercor/bhs261 [R0575](https://doi.org/10.1093/cercor/bhs261)
  - [延伸文献(HED)] Weigard & Huang-Pollock 2017. The role of speed in ADHD-related working memory deficits: A time-based resource-sharing and diffusion model account.  [R0726]
- **检索线索（模型记忆，未核实）**：AX-CPT-specific origin not confirmed: Servan-Schreiber, Cohen & Steingard 1996 (Arch Gen Psychiatry); Cohen, Barch, Carter & Servan-Schreiber 1999; Braver 2012 'The variable nature of cognitive control: a dual mechanisms framework' (TICS) as review.
- **检索备注**：Citations from HED task catalog page (fetched). Web search budget ran out before AX-CPT-specific searches.

### CTL-DD-001　延迟折扣　/ Delay discounting

- **优先级**：P2 标准（BCI 相关度：基础）　**收录判定**：收录（Intertemporal choice / delay discounting paradigm; ventral striatum/vmPFC vs lateral PFC BOLD; EEG less common.）
- **可能的神经标记物**：纹状体/前额 BOLD　**记录模态**：fMRI; EEG
- **别名**：Delay discounting; Delay of Gratification; Intertemporal choice task; Temporal Discounting; Temporal discounting
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_delay_discounting.html
- **文献线索**（5 条）：
  - [源头候选、关键文献(HED)] McClure SM & x 2004. Separate neural systems value immediate and delayed monetary rewards. *Science 306(5695)*. doi:10.1126/science.1100907 [R0288](https://pubmed.ncbi.nlm.nih.gov/15486304/)
  - [源头候选、关键文献(HED)] Kable JW & Glimcher PW 2007. The neural correlates of subjective value during intertemporal choice. *Nature Neuroscience 10(12)*. doi:10.1038/nn2007 [R0385](https://pubmed.ncbi.nlm.nih.gov/17982449/)
  - [延伸文献(HED)、综述] Peters J & Büchel C 2011. The neural mechanisms of inter-temporal decision-making: Understanding variability. *Trends in Cognitive Sciences 15(5)*. doi:10.1016/j.tics.2011.03.002 [R0518](https://pubmed.ncbi.nlm.nih.gov/21497544/)
  - [延伸文献(HED)、综述] Bickel WK & x 2014. The behavioral- and neuro-economic process of temporal discounting: A candidate behavioral marker of addiction. *Neuropharmacology 76*. doi:10.1016/j.neuropharm.2013.06.013 [R0621](https://pubmed.ncbi.nlm.nih.gov/23806805/)
  - [延伸文献(HED)] Kable 2014. Valuation, intertemporal choice, and self-control. *Neuroeconomics (2nd ed., pp. 173–192). Academic Press*. doi:10.1016/b978-0-12-416008-8.00010-3 [R0629](https://doi.org/10.1016/b978-0-12-416008-8.00010-3)
- **检索线索（模型记忆，未核实）**：Behavioral origin: Ainslie 1975; Mazur 1987 hyperbolic discounting; Kirby & Marakovic 1996 MCQ - not confirmed. Family 'control' is debatable (decision/valuation).
- **检索备注**：From HED delay discounting page https://www.hedtags.org/hed-task/tasks/hedtsk_delay_discounting.html (fetched).

### CTL-DT-001　双任务　/ Dual-task / PRP

- **优先级**：P2 标准（BCI 相关度：相关）　**收录判定**：收录（Dual-task / psychological refractory period (PRP) paradigm for central bottleneck; P3 latency and frontal theta markers; also basis of workload assessment.）
- **可能的神经标记物**：P3; 额中线 θ　**记录模态**：EEG; fMRI
- **别名**：Dual-task paradigm; PRP; PRP paradigm; Psychological Refractory Period; Psychological refractory period
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_psychological_refractory_period.html
- **文献线索**（6 条）：
  - [关键文献(HED)、综述] Pashler H 1994. Dual-task interference in simple tasks: Data and theory. *Psychological Bulletin 116(2)*. doi:10.1037/0033-2909.116.2.220 [R0113](https://pubmed.ncbi.nlm.nih.gov/7972591/)
  - [关键文献(HED)] Pashler & Johnston 1998. Attentional limitations in dual-task performance.  [R0159]
  - [延伸文献(HED)、方法/基准] Sigman M & Dehaene S 2008. Brain mechanisms of serial and parallel processing during dual-task performance. *Journal of Neuroscience 28(30)*. doi:10.1523/jneurosci.0948-08.2008 [R0397](https://pubmed.ncbi.nlm.nih.gov/18650336/)
  - [延伸文献(HED)、方法/基准] Tombu M & Jolicoeur P 2003. A central capacity sharing model of dual-task performance. *Journal of Experimental Psychology: Human Perception and Performance 29(1)*. doi:10.1037/0096-1523.29.1.3 [R0243](https://pubmed.ncbi.nlm.nih.gov/12669744/)
  - [延伸文献(HED)] Strobach et al. 2014. The specificity of stimulus-response and response-response compatibility effects in dual tasks.  [R0627]
  - [延伸文献(HED)] Zickerick et al. 2021. Differential effects of the psychological refractory period on early perceptual processing.  [R0805]
- **检索线索（模型记忆，未核实）**：Origin: Telford 1931 (refractory phase of voluntary responses); Welford 1952 single-channel theory - not confirmed.
- **检索备注**：From HED PRP page https://www.hedtags.org/hed-task/tasks/hedtsk_psychological_refractory_period.html (fetched).

### CTL-FLK-001　Flanker 任务　/ Eriksen flanker task

- **优先级**：P2 标准（BCI 相关度：相关）　**收录判定**：收录（Canonical interference/conflict task; primary paradigm for eliciting ERN/Pe (response errors) and conflict N2.）
- **可能的神经标记物**：ERN; Pe; N2　**记录模态**：EEG; MEG; fMRI
- **别名**：Arrow flanker task; Eriksen flanker; Flanker; Flanker Task; Flanker task; Letter flanker task
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_eriksen_flanker.html
- **公开数据集线索**：ERP CORE (flanker task: ERN and LRP); ERP CORE OSF repository; ERP CORE: An Open Resource for Human Event-Related Potential Research
- **文献线索**（9 条）：
  - [源头候选、关键文献(HED)] Eriksen BA & Eriksen CW 1974. Effects of noise letters upon the identification of a target letter in a nonsearch task. *Perception & Psychophysics 16(2)*. doi:10.3758/bf03203267 [R0030](https://wikidp.org/Q29540789)
  - [关键文献(HED)、综述] Botvinick MM & x 2001. Conflict monitoring and cognitive control. *Psychological Review 108(3)*. doi:10.1037/0033-295x.108.3.624 [R0204](https://pubmed.ncbi.nlm.nih.gov/11488380/)
  - [关键文献(HED)] Egner & Hirsch 2005. Cognitive control mechanisms resolve conflict through cortical amplification of task-relevant information. *Nature Neuroscience, 8(12), 1784-1790*. doi:10.1038/nn1594 [R0302](https://doi.org/10.1038/nn1594)
  - [综述] what weve learned (PDF, FSU CPR lab; ERN review).  [R1094](https://cprlab.psy.fsu.edu/uploads/1/0/8/8/108887279/what_weve_learned.pdf)
  - [方法/基准] Gehring WJ & x 1993. A Neural System for Error Detection and Compensation. *Psychological Science*. doi:10.1111/j.1467-9280.1993.tb00586.x [R0103](https://www.citedrive.com/en/discovery/a-neural-system-for-error-detection-and-compensation)
  - [延伸文献(HED)] White et al. 2018. Testing the validity of conflict drift-diffusion models for use in estimating cognitive processes: A parameter-recovery study. *Psychonomic Bulletin & Review, 25(1), 323–330*. doi:10.3758/s13423-017-1271-2 [R0749](https://doi.org/10.3758/s13423-017-1271-2)
  - [延伸文献(HED)] Ulrich et al. 2015. Automatic and controlled stimulus processing in conflict tasks: Superimposed diffusion processes and delta functions. *Cognitive Psychology, 78, 148–174*. doi:10.1016/j.cogpsych.2015.02.005 [R0638](https://doi.org/10.1016/j.cogpsych.2015.02.005)
  - [延伸文献(HED)] Servant & Logan 2019. Dynamics of attentional focusing in the Eriksen flanker task. *Attention, Perception, & Psychophysics, 81, 2710–2721*. doi:10.3758/s13414-019-01796-3 [R0763](https://doi.org/10.3758/s13414-019-01796-3)
  - [延伸文献(HED)] Donner et al. 2009. Buildup of choice-predictive activity in human motor cortex during perceptual decision making. *Current Biology, 19(18), 1581–1585*. doi:10.1016/j.cub.2009.07.066 [R0427](https://doi.org/10.1016/j.cub.2009.07.066)
- **检索线索（模型记忆，未核实）**：Falkenstein et al. 1991 (Electroencephalogr Clin Neurophysiol) independent ERN/Ne origin - not confirmed. The FSU PDF likely Gehring/Hajcak ERN review - title not verified.
- **检索备注**：ERP CORE year/venue from DOAJ listing 'NeuroImage (Jan 2021)'. Eriksen DOI and Botvinick 2001 from HED flanker page (fetched).

### CTL-GNG-001　Go/NoGo　/ Go/NoGo task

- **优先级**：P2 标准（BCI 相关度：相关）　**收录判定**：收录（Canonical response-inhibition paradigm (NoGo-N2 / NoGo-P3); distinct from stop-signal (action restraint vs action cancellation).）
- **可能的神经标记物**：N2; P3　**记录模态**：EEG; fMRI
- **别名**：GNG; Go No-Go; Go/No-Go; Go/Nogo task
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_go_no_go.html
- **文献线索**（9 条）：
  - [源头候选、关键文献(HED)] Donders FC 1969 (orig. 1868). On the speed of mental processes. *Acta Psychologica 30*. doi:10.1016/0001-6918(69)90065-1 [R0019](https://pubmed.ncbi.nlm.nih.gov/5811531/)
  - [关键文献(HED)、方法/基准] Garavan H et al. 1999. Right hemispheric dominance of inhibitory control: An event-related functional MRI study. *PNAS 96(14)*. doi:10.1073/pnas.96.14.8301 [R0180](https://pubmed.ncbi.nlm.nih.gov/10393989/)
  - [综述] Huster RJ & x. Electroencephalography of response inhibition tasks: Functional networks and cognitive contributions. *International Journal of Psychophysiology*. doi:10.1016/j.ijpsycho.2012.08.001 [R0915](https://www.doi.org/10.1016/j.ijpsycho.2012.08.001)
  - [综述] Simmonds DJ et al. 2008. Meta-analysis of Go/No-go tasks demonstrating that fMRI activation associated with response inhibition is task-dependent. *Neuropsychologia 46(1)*. doi:10.1016/j.neuropsychologia.2007.07.015 [R0408](https://pubmed.ncbi.nlm.nih.gov/17850833/)
  - [延伸文献(HED)、综述] Wessel JR 2018. Prepotent motor activity and inhibitory control demands in different variants of the go/no-go paradigm. *Psychophysiology 55(3)*. doi:10.1111/psyp.12871 [R0747](https://www.hedtags.org/hed-task/tasks/hedtsk_go_no_go.html)
  - [综述] Swick et al. 2011. Are the neural correlates of stopping and not going identical? Quantitative meta-analysis of two response inhibition tasks. *NeuroImage, 56(3), 1655–1665*. doi:10.1016/j.neuroimage.2011.02.070 [R0494](https://doi.org/10.1016/j.neuroimage.2011.02.070)
  - [方法/基准] Differences in unity: the go/no-go and stop signal tasks rely on different inhibitory mechanisms. *bioRxiv*. doi:10.1101/705079 [R0898](https://www.biorxiv.org/content/10.1101/705079.full.pdf)
  - [延伸文献(HED)] Criaud & Boulinguez 2013. Have we been asking the right questions when assessing response inhibition in go/no-go tasks with fMRI?. *Neuroscience & Biobehavioral Reviews, 37(1), 11–23*. doi:10.1016/j.neubiorev.2012.11.003 [R0573](https://doi.org/10.1016/j.neubiorev.2012.11.003)
  - [延伸文献(HED)] Littman & Takács 2017. Do all inhibitions act alike? A study of Go/No-Go and stop-signal paradigms using drift-diffusion modeling. *PLOS ONE, 12(10), e0186774*. doi:10.1371/journal.pone.0186774 [R0700](https://doi.org/10.1371/journal.pone.0186774)
- **检索线索（模型记忆，未核实）**：Origin candidates not confirmed: Donders (1868/1969) reaction-time 'c-reaction'; Pfefferbaum et al. 1985 (EEG Clin Neurophysiol) NoGo ERPs; Falkenstein, Hoormann & Hohnsbein 1999 (Acta Psychologica) 'ERP components in Go/Nogo tasks and their relation to inhibition'. fMRI meta-analysis: Simmonds, Pekar & Mostofsky 2008 (Neuropsychologia).
- **检索备注**：Huster review venue inferred from DOI prefix ijpsycho; year likely 2013. Additional refs from HED Go/No-Go page (fetched).

### CTL-IGT-001　爱荷华赌博任务　/ Iowa gambling task

- **优先级**：P2 标准（BCI 相关度：基础）　**收录判定**：收录（Iowa Gambling Task: decision-making under ambiguity with reward/punishment feedback (vmPFC; FRN/P3 in ERP studies).）
- **可能的神经标记物**：FRN; 前额 BOLD　**记录模态**：EEG; fMRI
- **别名**：Bechara gambling task; IGT; Iowa Gambling; Iowa Gambling Task
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_iowa_gambling.html
- **文献线索**（8 条）：
  - [源头候选、关键文献(HED)] Bechara A & x 1994. Insensitivity to future consequences following damage to human prefrontal cortex. *Cognition 50(1-3)*. doi:10.1016/0010-0277(94)90018-3 [R0116](https://pubmed.ncbi.nlm.nih.gov/8039375/)
  - [关键文献(HED)、方法/基准] Bechara A & x 1997. Deciding advantageously before knowing the advantageous strategy. *Science 275(5304)*. doi:10.1126/science.275.5304.1293 [R0144](https://pubmed.ncbi.nlm.nih.gov/9036851/)
  - [关键文献(HED)、方法/基准] Li X & x 2010. The Iowa Gambling Task in fMRI images. *Human Brain Mapping 31(3)*. doi:10.1002/hbm.20875 [R0485](https://www.hedtags.org/hed-task/tasks/hedtsk_iowa_gambling.html)
  - [延伸文献(HED)、综述] Buelow MT & Suhr JA 2009. Construct validity of the Iowa Gambling Task. *Neuropsychology Review 19(1)*. doi:10.1007/s11065-009-9083-4 [R0430](https://pubmed.ncbi.nlm.nih.gov/19194801/)
  - [延伸文献(HED)、综述] 2025. Decision-making and performance in the Iowa Gambling Task: recent ERP findings and clinical implications. *Frontiers in Psychology 16*. doi:10.3389/fpsyg.2025.1492471 [R0825](https://pubmed.ncbi.nlm.nih.gov/40177039/)
  - [延伸文献(HED)] Steingroever et al. 2013. Performance of healthy participants on the Iowa Gambling Task. *Psychological Assessment, 25(1), 180–193*. doi:10.1037/a0029929 [R0583](https://doi.org/10.1037/a0029929)
  - [延伸文献(HED)] Haines et al. 2018. The Outcome-Representation Learning Model: A novel reinforcement learning model of the Iowa Gambling Task. *Cognitive Science, 42(Suppl 3), 1098–1122*. doi:10.1111/cogs.12688 [R0750](https://doi.org/10.1111/cogs.12688)
  - [延伸文献(HED)] Ahn et al. 2008. Comparison of decision learning models using the generalization criterion method. *Cognitive Science, 32(8), 1376–1402*. doi:10.1080/03640210802352992 [R0399](https://doi.org/10.1080/03640210802352992)
- **检索线索（模型记忆，未核实）**：Steingroever et al. 2015 'Data from 617 healthy participants performing the Iowa gambling task: A many labs collaboration' (J Open Psychol Data) is a behavioral dataset - not confirmed.
- **检索备注**：From HED IGT page https://www.hedtags.org/hed-task/tasks/hedtsk_iowa_gambling.html (fetched).

### CTL-PDM-001　知觉决策（随机点运动）　/ Perceptual decision making (random-dot motion)

- **优先级**：P2 标准（BCI 相关度：相关）　**收录判定**：收录（Random-dot motion (RDK) perceptual decision paradigm; evidence-accumulation markers (LIP in monkeys, centroparietal positivity CPP in human EEG).）
- **可能的神经标记物**：CPP　**记录模态**：EEG; intracortical
- **别名**：Dot Motion; Dot Motion Task; Motion coherence discrimination; Perceptual decision making; RDK; Random Dot Kinematogram; Random dot kinematogram; Random dot motion task
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_random_dot_kinematogram.html
- **文献线索**（7 条）：
  - [源头候选、关键文献(HED)] Britten KH & x 1992. The analysis of visual motion: A comparison of neuronal and psychophysical performance. *Journal of Neuroscience 12(12)*. doi:10.1523/jneurosci.12-12-04745.1992 [R0102](https://pubmed.ncbi.nlm.nih.gov/1464765/)
  - [关键文献(HED)、综述] Gold JI & Shadlen MN 2007. The neural basis of decision making. *Annual Review of Neuroscience 30*. doi:10.1146/annurev.neuro.29.051605.113038 [R0384](https://pubmed.ncbi.nlm.nih.gov/17600525/)
  - [关键文献(HED)] Shadlen & Newsome 2001. Neural basis of a perceptual decision in the parietal cortex (area LIP) of the rhesus monkey. *Journal of Neurophysiology*. doi:10.1152/jn.2001.86.4.1916 [R0208](https://doi.org/10.1152/jn.2001.86.4.1916)
  - [延伸文献(HED)、综述] Ratcliff R & x 2016. Diffusion decision model: Current issues and history. *Trends in Cognitive Sciences 20(4)*. doi:10.1016/j.tics.2016.01.007 [R0675](https://pubmed.ncbi.nlm.nih.gov/26952739/)
  - [延伸文献(HED)、方法/基准] Steinemann NA et al. 2018. Decisions are expedited through multiple neural adjustments spanning the sensorimotor hierarchy. *Nature Communications 9*. doi:10.1038/s41467-018-06117-0 [R0736](https://pubmed.ncbi.nlm.nih.gov/30194305/)
  - [延伸文献(HED)] Shooshtari et al. 2019. Confidence representation of perceptual decision by EEG and eye data in a random dot motion task. *Neuroscience*. doi:10.1016/j.neuroscience.2019.03.031 [R0761](https://doi.org/10.1016/j.neuroscience.2019.03.031)
  - [延伸文献(HED)] Turner et al. 2018. Approaches to analysis in model-based cognitive neuroscience. *Journal of Mathematical Psychology*. doi:10.1016/j.neubiorev.2018.04.011 [R0732](https://doi.org/10.1016/j.neubiorev.2018.04.011)
- **检索线索（模型记忆，未核实）**：CPP origin: O'Connell, Dockree & Kelly 2012 (Nat Neurosci) 'A supramodal accumulation-to-bound signal that determines perceptual decisions in humans'; Kelly & O'Connell 2013 (J Neurosci) RDK CPP - not confirmed. Newsome & Pare 1988 monkey RDK origin.
- **检索备注**：From HED RDK page https://www.hedtags.org/hed-task/tasks/hedtsk_random_dot_kinematogram.html (fetched).

### CTL-SART-001　持续注意反应任务（SART）　/ Sustained attention to response task

- **优先级**：P2 标准（BCI 相关度：相关）　**收录判定**：收录（新增，待确认）
- **可能的神经标记物**：P3; α　**记录模态**：EEG
- **别名**：SART; Sustained Attention to Response
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_sustained_attention_to_response.html
- **文献线索**（10 条）：
  - [源头候选、关键文献(HED)] Robertson IH & x 1997. 'Oops!': Performance correlates of everyday attentional failures in traumatic brain injured and normal subjects. *Neuropsychologia 35(6)*. doi:10.1016/s0028-3932(97)00015-8 [R0139](https://pubmed.ncbi.nlm.nih.gov/9204482/)
  - [关键文献(HED)] Smallwood et al. 2004. Subjective experience and the attentional lapse: Task engagement and disengagement during sustained attention. *Consciousness and Cognition*. doi:10.1016/j.concog.2004.06.003 [R0290](https://doi.org/10.1016/j.concog.2004.06.003)
  - [关键文献(HED)] Manly et al. 1999. The absent mind: Further investigations of sustained attention to response. *Neuropsychologia*. doi:10.1016/s0028-3932(98)00127-4 [R0184](https://doi.org/10.1016/s0028-3932(98)00127-4)
  - [关键文献(HED)] Smallwood & Schooler 2006. The restless mind. *Psychological Bulletin*. doi:10.1037/0033-2909.132.6.946 [R0356](https://doi.org/10.1037/0033-2909.132.6.946)
  - [延伸文献(HED)、综述] Fortenbaugh FC & x 2017. Recent theoretical, neural, and clinical advances in sustained attention research. *Annals of the New York Academy of Sciences 1396(1)*. doi:10.1111/nyas.13318 [R0715](https://www.hedtags.org/hed-task/tasks/hedtsk_continuous_performance.html)
  - [延伸文献(HED)、方法/基准] Dockree PM & x 2007. Optimal sustained attention is linked to the spectral content of background EEG activity: Greater ongoing tonic alpha (~10 Hz) power supports successful phasic goal activation. *European Journal of Neuroscience 25(3)*. doi:10.1111/j.1460-9568.2007.05324.x [R0372](https://pubmed.ncbi.nlm.nih.gov/17328783/)
  - [延伸文献(HED)] Seli et al. 2013. Wandering minds and wavering rhythms: Linking mind wandering and behavioral variability. *Journal of Experimental Psychology: Human Perception and Performance*. doi:10.1037/a0030954 [R0592](https://doi.org/10.1037/a0030954)
  - [延伸文献(HED)] Head & Helton 2014. Sustained attention failures are primarily due to sustained cognitive load not task monotony. *Acta Psychologica*. doi:10.1016/j.actpsy.2014.09.007 [R0617](https://doi.org/10.1016/j.actpsy.2014.09.007)
  - [延伸文献(HED)] McVay & Kane 2009. Conducting the train of thought: Working memory capacity, goal neglect, and mind wandering in an executive-control task. *Journal of Experimental Psychology: Learning, Memory, and Cognition*. doi:10.1037/a0014104 [R0429](https://doi.org/10.1037/a0014104)
  - [延伸文献(HED)] Seli et al. 2016. Mind-wandering with and without intention. *Trends in Cognitive Sciences*. doi:10.1016/j.tics.2016.05.010 [R0681](https://doi.org/10.1016/j.tics.2016.05.010)

### CTL-SIM-001　Simon 任务　/ Simon task

- **优先级**：P2 标准（BCI 相关度：基础）　**收录判定**：收录（Classic spatial stimulus-response correspondence conflict task; N2 and LRP (incorrect-hand activation) markers.）
- **可能的神经标记物**：N2; LRP　**记录模态**：EEG
- **别名**：Simon Effect Task; Simon effect; Simon task; Spatial Compatibility; Spatial S-R compatibility task
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_simon.html
- **文献线索**（7 条）：
  - [源头候选、关键文献(HED)] Simon JR & Rudell AP 1967. Auditory S-R compatibility: The effect of an irrelevant cue on information processing. *Journal of Applied Psychology 51(3)*. doi:10.1037/h0020586 [R0016](https://www.hedtags.org/hed-task/tasks/hedtsk_simon.html)
  - [关键文献(HED)、方法/基准] Kornblum S et al. 1990. Dimensional overlap: Cognitive basis for stimulus-response compatibility - A model and taxonomy. *Psychological Review 97(2)*. doi:10.1037/0033-295x.97.2.253 [R0091](https://www.hedtags.org/hed-task/tasks/hedtsk_simon.html)
  - [关键文献(HED)] De Jong et al. 1994. Conditional and unconditional automaticity: A dual-process model of effects of spatial stimulus-response correspondence. *Journal of Experimental Psychology: Human Perception and Performance, 20(4), 731–750*. doi:10.1037/0096-1523.20.4.731 [R0112](https://doi.org/10.1037/0096-1523.20.4.731)
  - [延伸文献(HED)、综述] Hommel B 2011. The Simon effect as tool and heuristic. *Acta Psychologica 136(2)*. doi:10.1016/j.actpsy.2010.04.011 [R0516](https://www.hedtags.org/hed-task/tasks/hedtsk_simon.html)
  - [延伸文献(HED)、综述] Salzer Y et al. 2017. Sensory neural pathways revisited to unravel the temporal dynamics of the Simon effect: A model-based cognitive neuroscience approach. *Neuroscience & Biobehavioral Reviews 77*. doi:10.1016/j.neubiorev.2017.02.023 [R0717](https://www.hedtags.org/hed-task/tasks/hedtsk_simon.html)
  - [延伸文献(HED)] Wiegand & Wascher 2005. Dynamic aspects of stimulus-response correspondence: Evidence for two mechanisms involved in the Simon effect. *Journal of Experimental Psychology: Human Perception and Performance, 31(3), 453–464*. doi:10.1037/0096-1523.31.3.453 [R0309](https://doi.org/10.1037/0096-1523.31.3.453)
  - [延伸文献(HED)] Proctor et al. 2011. Reaction time distribution analysis of spatial correspondence effects. *Psychonomic Bulletin & Review, 18(2), 242–266*. doi:10.3758/s13423-011-0053-5 [R0514](https://doi.org/10.3758/s13423-011-0053-5)
- **检索备注**：Citations taken from HED task page reference list (fetched); URL points to that page.

### CTL-SST-001　停止信号任务　/ Stop-signal task

- **优先级**：P2 标准（BCI 相关度：基础）　**收录判定**：收录（Canonical action-cancellation paradigm (SSRT, stop-P3, right IFG beta); distinct from Go/NoGo.）
- **可能的神经标记物**：抑制 P3; 右额下回 β　**记录模态**：EEG; fMRI
- **别名**：Countermanding task; SST; Stop Signal; Stop Task; Stop-Signal; Stop-signal paradigm
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_stop_signal.html
- **文献线索**（10 条）：
  - [关键文献(HED)] Logan & Cowan 1984. On the ability to inhibit thought and action: A theory of an act of control. *Psychological Review*. doi:10.1037/0033-295x.91.3.295 [R0067](https://doi.org/10.1037/0033-295x.91.3.295)
  - [关键文献(HED)] Aron & Poldrack 2006. Cortical and subcortical contributions to Stop signal response inhibition: Role of the subthalamic nucleus. *Journal of Neuroscience*. doi:10.1523/jneurosci.4682-05.2006 [R0337](https://doi.org/10.1523/jneurosci.4682-05.2006)
  - [关键文献(HED)] Verbruggen & Logan 2008. Response inhibition in the stop-signal paradigm. *Trends in Cognitive Sciences*. doi:10.1016/j.tics.2008.07.005 [R0418](https://doi.org/10.1016/j.tics.2008.07.005)
  - [延伸文献(HED)、综述] Verbruggen et al. 2019. A consensus guide to capturing the ability to inhibit actions and impulsive behaviors in the stop-signal task. *eLife*. doi:10.7554/elife.46323 [R0756](https://doi.org/10.7554/elife.46323)
  - [综述] Huster RJ & x. Electroencephalography of response inhibition tasks: Functional networks and cognitive contributions. *International Journal of Psychophysiology*. doi:10.1016/j.ijpsycho.2012.08.001 [R0915](https://www.doi.org/10.1016/j.ijpsycho.2012.08.001)
  - [方法/基准] Logan GD. On the ability to inhibit thought and action: A users' guide to the stop signal paradigm.  [R1018](https://dare.uva.nl/id/d72ffa14-a640-4cd8-9910-51634bf7ab36)
  - [方法/基准] Logan GD & x. On the ability to inhibit thought and action: General and special theories of an act of control.  [R1019](https://dare.uva.nl/id/6c66136e-3deb-4049-93d3-fb35ba5f1b4b)
  - [延伸文献(HED)] Matzke et al. 2019. Bayesian modeling of stop-signal reaction time distributions.  [R0759]
  - [延伸文献(HED)] Skippen et al. 2019. Reliability of triggering inhibitory process is a better predictor of impulsivity than SSRT. *Acta Psychologica*. doi:10.1016/j.actpsy.2018.10.016 [R0779](https://doi.org/10.1016/j.actpsy.2018.10.016)
  - [延伸文献(HED)] Bissett et al. 2021. Design issues and solutions for stop-signal data from the Adolescent Brain Cognitive Development (ABCD) study. *eLife*. doi:10.7554/elife.60185 [R0804](https://doi.org/10.7554/elife.60185)
- **检索线索（模型记忆，未核实）**：Origin: Logan & Cowan (1984) Psychological Review 91:295 'On the ability to inhibit thought and action: A theory of an act of control' - not directly surfaced. Lappin & Eriksen 1966 earlier stop-signal. Users' guide likely Logan 1994; general/special theories likely Logan, Van Zandt, Verbruggen & Wagenmakers 2014. Aron, Robbins & Poldrack 2004/2014 TICS rIFG reviews.
- **检索备注**：eLife PMC id PMC6533084 appeared in same result set (association inferred).

### CTL-STR-001　Stroop 任务　/ Stroop task

- **优先级**：P2 标准（BCI 相关度：基础）　**收录判定**：收录（Classic interference paradigm (color-word Stroop); N450 / conflict SP in EEG, ACC/DLPFC in fMRI.）
- **可能的神经标记物**：N450　**记录模态**：EEG; fMRI
- **别名**：CWIT; Color-Word Interference Test; Color-word interference task; Emotional Stroop (variant); Stroop; Stroop color-word task
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_stroop_color_word.html
- **文献线索**（7 条）：
  - [源头候选、关键文献(HED)] Stroop JR 1935. Studies of interference in serial verbal reactions. *Journal of Experimental Psychology 18(6)*. doi:10.1037/h0054651 [R0002](https://psychclassics.yorku.ca/Stroop/)
  - [关键文献(HED)、方法/基准] Wager TD & x 2005. Common and unique components of response inhibition revealed by fMRI. *NeuroImage 27(3)*. doi:10.1016/j.neuroimage.2005.01.054 [R0303](https://pubmed.ncbi.nlm.nih.gov/16019232/)
  - [综述] MacLeod CM 1991. Half a century of research on the Stroop effect: an integrative review. *Psychological Bulletin 109(2)*. doi:10.1037/0033-2909.109.2.163 [R0096](https://pubmed.ncbi.nlm.nih.gov/2034749/)
  - [综述] Egetemeyer J & x 2024. Not all Stroop-type tasks are alike: Assessing the impact of stimulus material, task design, and cognitive demand via meta-analyses across neuroimaging studies. *Neuropsychology Review 34*. doi:10.1007/s11065-024-09647-1 [R0821](https://pubmed.ncbi.nlm.nih.gov/39264479/)
  - [综述] Neumann et al. 2005. Meta-analysis of functional imaging data using replicator dynamics. *Human Brain Mapping*. doi:10.1002/hbm.20133 [R0317](https://doi.org/10.1002/hbm.20133)
  - [延伸文献(HED)] Servant et al. 2014. Conflict tasks and the diffusion framework: Insight in model constraints based on psychological laws. *Cognitive Psychology*. doi:10.1016/j.cogpsych.2014.03.002 [R0601](https://doi.org/10.1016/j.cogpsych.2014.03.002)
  - [延伸文献(HED)] Algom & Chajut 2019. Reclaiming the Stroop effect back from control to input-driven attention and perception. *Frontiers in Psychology*. doi:10.3389/fpsyg.2019.01683 [R0777](https://doi.org/10.3389/fpsyg.2019.01683)
- **检索线索（模型记忆，未核实）**：N450 origin candidates: Liotti, Woldorff, Perez & Mayberg 2000 (Neuropsychologia) 'An ERP study of the temporal course of the Stroop color-word interference effect'; West & Alain 2000. Not confirmed via search.
- **检索备注**：DOIs/volumes and extra refs from HED Stroop page (fetched).

### CTL-SW-001　任务切换　/ Task switching

- **优先级**：P2 标准（BCI 相关度：基础）　**收录判定**：收录（Canonical cognitive-flexibility paradigm (switch cost; frontal-midline theta, switch-related P3/posterior positivity).）
- **可能的神经标记物**：额中线 θ; 切换 P3　**记录模态**：EEG; fMRI
- **别名**：Alternating Runs; Alternating runs paradigm; Cued task switching; Set Shifting; Task switching; Task-switching paradigm
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_task_switching.html
- **文献线索**（7 条）：
  - [源头候选、关键文献(HED)] Rogers RD & Monsell S 1995. Costs of a predictable switch between simple cognitive tasks. *Journal of Experimental Psychology: General 124(2)*. doi:10.1037/0096-3445.124.2.207 [R0121](https://www.hedtags.org/hed-task/tasks/hedtsk_task_switching.html)
  - [关键文献(HED)、综述] Monsell S 2003. Task switching. *Trends in Cognitive Sciences 7(3)*. doi:10.1016/s1364-6613(03)00028-7 [R0261](https://pubmed.ncbi.nlm.nih.gov/12639695/)
  - [关键文献(HED)、方法/基准] Braver TS et al. 2003. Neural mechanisms of transient and sustained cognitive control during task switching. *Neuron 39(4)*. doi:10.1016/s0896-6273(03)00466-5 [R0258](https://pubmed.ncbi.nlm.nih.gov/12925284/)
  - [综述] Kiesel A & x 2010. Control and interference in task switching - A review. *Psychological Bulletin 136(5)*. doi:10.1037/a0019842 [R0459](https://pubmed.ncbi.nlm.nih.gov/20804238/)
  - [延伸文献(HED)] Vandierendonck et al. 2010. Task switching: Interplay of reconfiguration and interference control. *Psychological Bulletin*. doi:10.1037/a0019791 [R0484](https://doi.org/10.1037/a0019791)
  - [延伸文献(HED)] Grange & Houghton 2014. Models of cognitive control in task switching. *Task Switching and Cognitive Control*. doi:10.1093/acprof:osobl/9780199921959.003.0008 [R0608](https://doi.org/10.1093/acprof:osobl/9780199921959.003.0008)
  - [延伸文献(HED)] Braem & Egner 2018. Getting a grip on cognitive flexibility. *Current Directions in Psychological Science*. doi:10.1177/0963721418787475 [R0739](https://doi.org/10.1177/0963721418787475)
- **检索线索（模型记忆，未核实）**：Jersild 1927 'Mental set and shift' is the historical origin (not confirmed).
- **检索备注**：Citations and PMIDs taken from HED task catalog page https://www.hedtags.org/hed-task/tasks/hedtsk_task_switching.html (fetched); PubMed URLs constructed from PMIDs listed there.

### CTL-TOL-001　伦敦塔（计划）　/ Tower of London

- **优先级**：P2 标准（BCI 相关度：基础）　**收录判定**：收录（Tower of London is the canonical planning/problem-solving paradigm (DLPFC BOLD; fNIRS HbO).）
- **可能的神经标记物**：前额 BOLD; HbO　**记录模态**：fMRI; fNIRS
- **别名**：Shallice Tower Task; Stockings of Cambridge (CANTAB variant); TOL; TOL-F; Tower of London
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_tower_of_london.html
- **文献线索**（7 条）：
  - [源头候选、关键文献(HED)] Shallice T 1982. Specific impairments of planning. *Philosophical Transactions of the Royal Society of London B 298(1089)*. doi:10.1098/rstb.1982.0082 [R0057](https://pubmed.ncbi.nlm.nih.gov/6125971/)
  - [关键文献(HED)、综述] Unterrainer JM & Owen AM 2006. Planning and problem solving: From neuropsychology to functional neuroimaging. *Journal of Physiology-Paris 99(4-6)*. doi:10.1016/j.jphysparis.2006.03.014 [R0348](https://pubmed.ncbi.nlm.nih.gov/16750617/)
  - [关键文献(HED)、方法/基准] Owen AM & x 1996. Planning and spatial working memory: A positron emission tomography study in humans. *European Journal of Neuroscience 8(2)*. doi:10.1111/j.1460-9568.1996.tb01219.x [R0136](https://pubmed.ncbi.nlm.nih.gov/8714706/)
  - [延伸文献(HED)、方法/基准] Kaller CP & x 2011. Dissociable contributions of left and right dorsolateral prefrontal cortex in planning. *Cerebral Cortex 21(2)*. doi:10.1093/cercor/bhq096 [R0498](https://www.hedtags.org/hed-task/tasks/hedtsk_tower_of_london.html)
  - [延伸文献(HED)] Andrés 2003. Frontal cortex as the central executive of working memory: Time to revise our view. *Cortex*. doi:10.1016/s0010-9452(08)70868-2 [R0251](https://doi.org/10.1016/s0010-9452(08)70868-2)
  - [延伸文献(HED)] Köstering et al. 2015. Assessment of planning performance in clinical samples: Reliability and validity of the Tower of London task (TOL-F). *Neuropsychologia*. doi:10.1016/j.neuropsychologia.2015.07.017 [R0637](https://doi.org/10.1016/j.neuropsychologia.2015.07.017)
  - [延伸文献(HED)] Unterrainer et al. 2004. Planning abilities and the Tower of London: Is this task measuring a discrete cognitive function?. *Journal of Clinical and Experimental Neuropsychology*. doi:10.1080/13803390490509574 [R0287](https://doi.org/10.1080/13803390490509574)
- **检索备注**：From HED Tower of London page (fetched).

### CTL-WCST-001　威斯康星卡片分类　/ Wisconsin Card Sorting Test

- **优先级**：P2 标准（BCI 相关度：基础）　**收录判定**：收录（Classic set-shifting/rule-learning test; EEG/ERP versions (feedback P3, N2) and fMRI/fNIRS PFC activation.）
- **可能的神经标记物**：额叶 BOLD; P3　**记录模态**：EEG; fMRI; fNIRS
- **别名**：Card Sorting Task; Card sorting task; WCST; Wisconsin Card Sorting Test
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_wisconsin_card_sorting.html
- **文献线索**（5 条）：
  - [关键文献(HED)、综述] Nyhus E & Barcelo F 2009. The Wisconsin Card Sorting Test and the cognitive assessment of prefrontal executive functions: A critical update. *Brain and Cognition 71(3)*. doi:10.1016/j.bandc.2009.03.005 [R0445](https://pubmed.ncbi.nlm.nih.gov/19375839/)
  - [延伸文献(HED)、综述] Lange F et al. 2017. Cognitive flexibility in neurological disorders: Cognitive components and event-related potentials. *Neuroscience & Biobehavioral Reviews 83*. doi:10.1016/j.neubiorev.2017.09.011 [R0699](https://pubmed.ncbi.nlm.nih.gov/28903059/)
  - [延伸文献(HED)、方法/基准] Kopp B et al. 2020. Cognitive flexibility and N2/P3 event-related brain potentials. *Scientific Reports 10*. doi:10.1038/s41598-020-66781-5 [R0789](https://pubmed.ncbi.nlm.nih.gov/32555267/)
  - [延伸文献(HED)] Bishara et al. 2010. Sequential learning models for the Wisconsin Card Sorting Task: Assessing processes in substance dependent individuals. *Journal of Mathematical Psychology*. doi:10.1016/j.jmp.2008.10.002 [R0480](https://doi.org/10.1016/j.jmp.2008.10.002)
  - [延伸文献(HED)] Figueroa-Vargas et al. 2020. Frontoparietal connectivity correlates with cognitive flexibility during the Wisconsin Card Sorting Test.  [R0795]
- **检索线索（模型记忆，未核实）**：Origin: Grant DA & Berg EA (1948) J Exp Psychol 'A behavioral analysis of degree of reinforcement and ease of shifting to new responses in a Weigl-type card-sorting problem'; Berg 1948; Milner 1963 frontal lesions - not confirmed.
- **检索备注**：From HED WCST page https://www.hedtags.org/hed-task/tasks/hedtsk_wisconsin_card_sorting.html (fetched). Overlaps conceptually with CTL-SW-001 and ERR-PRL-001 but retained as standard clinical test.

### CTL-BART-001　气球模拟风险任务　/ Balloon analogue risk task

- **优先级**：P3 长尾（BCI 相关度：基础）　**收录判定**：收录（新增，待确认）
- **可能的神经标记物**：FRN; 前额 BOLD　**记录模态**：EEG; fMRI
- **别名**：BART; Balloon Analog Risk; Balloon Task
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_balloon_analog_risk.html
- **文献线索**（6 条）：
  - [关键文献(HED)] Lejuez et al. 2002. Evaluation of a behavioral measure of risk taking: The Balloon Analogue Risk Task (BART). *Journal of Experimental Psychology: Applied, 8(2), 75-84*. doi:10.1037/1076-898x.8.2.75 [R0224](https://doi.org/10.1037/1076-898x.8.2.75)
  - [关键文献(HED)] Rao et al. 2008. Neural correlates of voluntary and involuntary risk taking in the human brain. *NeuroImage, 42(2), 902-910*. doi:10.1016/j.neuroimage.2008.05.046 [R0411](https://doi.org/10.1016/j.neuroimage.2008.05.046)
  - [关键文献(HED)] Schonberg et al. 2011. Mind the gap: Bridging economic and naturalistic risk-taking with cognitive neuroscience. *Trends in Cognitive Sciences, 15(1), 11-19*. doi:10.1016/j.tics.2010.10.002 [R0509](https://doi.org/10.1016/j.tics.2010.10.002)
  - [延伸文献(HED)] Pleskac 2008. Decision making and learning while taking sequential risks. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 34(1), 167–185*. doi:10.1037/0278-7393.34.1.167 [R0400](https://doi.org/10.1037/0278-7393.34.1.167)
  - [延伸文献(HED)] Wallsten et al. 2005. Modeling behavior in a clinically diagnostic sequential risk-taking task. *Psychological Review, 112(4), 862–880*. doi:10.1037/0033-295x.112.4.862 [R0318](https://doi.org/10.1037/0033-295x.112.4.862)
  - [延伸文献(HED)] Hunt et al. 2005. Construct validity of the Balloon Analog Risk Task (BART). *Assessment, 12(4), 416–428*. doi:10.1177/1073191105278740 [R0305](https://doi.org/10.1177/1073191105278740)

### CTL-DSST-001　数字符号替换　/ Digit symbol substitution

- **优先级**：P3 长尾（BCI 相关度：基础）　**收录判定**：收录（新增，待确认）
- **可能的神经标记物**：待定　**记录模态**：fMRI
- **别名**：Coding Test; DSST; Digit Symbol Substitution; Digit Symbol Substitution Test; SDMT; Symbol Digit Modalities
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_digit_symbol_substitution.html
- **备注**：以行为测量为主，需确认是否满足纳入标准 3
- **文献线索**（4 条）：
  - [综述] Hoyer et al. 2004. Adult age and digit symbol substitution performance: A meta-analysis. *Psychology and Aging, 19(1), 211–214*. doi:10.1037/0882-7974.19.1.211 [R0271](https://doi.org/10.1037/0882-7974.19.1.211)
  - [延伸文献(HED)] Hinton-Bayre & Geffen 2005. Comparability, reliability, and practice effects on alternate forms of the Digit Symbol Substitution and Symbol Digit Modalities Tests. *Psychological Assessment, 17(2), 237–241*. doi:10.1037/1040-3590.17.2.237 [R0304](https://doi.org/10.1037/1040-3590.17.2.237)
  - [延伸文献(HED)] Baudouin et al. 2009. Age-related changes in coding speed: Test-retest reliability and factor structure.  [R0425]
  - [延伸文献(HED)] Patel et al. 2017. Revisiting cognitive reserve and cognition in multiple sclerosis: A closer look at the SDMT. *Multiple Sclerosis Journal, 23(10), 1390–1399*. doi:10.1177/1352458517692887 [R0716](https://doi.org/10.1177/1352458517692887)

### CTL-EFF-001　努力决策　/ Effort-based decision making

- **优先级**：P3 长尾（BCI 相关度：基础）　**收录判定**：收录（新增，待确认）
- **可能的神经标记物**：前扣带 BOLD　**记录模态**：fMRI; EEG
- **别名**：EEfRT; Effort Choice Task; Effort Discounting Task; Effort Expenditure for Rewards Task; Effort-Cost Paradigm
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_effort_based_decision_making.html
- **文献线索**（7 条）：
  - [关键文献(HED)] Treadway et al. 2009. Worth the 'EEfRT'? The Effort Expenditure for Rewards Task as an objective measure of motivation and anhedonia. *PLoS ONE, 4(8), e6598*. doi:10.1371/journal.pone.0006598 [R0451](https://doi.org/10.1371/journal.pone.0006598)
  - [关键文献(HED)] Botvinick et al. 2009. Effort discounting in human nucleus accumbens. *Cognitive, Affective, & Behavioral Neuroscience, 9(1), 16-27*. doi:10.3758/cabn.9.1.16 [R0437](https://doi.org/10.3758/cabn.9.1.16)
  - [关键文献(HED)] Westbrook & Braver 2015. Cognitive effort: A neuroeconomic approach. *Cognitive, Affective, & Behavioral Neuroscience, 15(2), 395-415*. doi:10.3758/s13415-015-0334-y [R0639](https://doi.org/10.3758/s13415-015-0334-y)
  - [综述] Lopez-Gamundi et al. 2021. The neural basis of effort valuation: A meta-analysis of functional magnetic resonance imaging studies. *Neuroscience & Biobehavioral Reviews, 131, 1275-1287*. doi:10.1016/j.neubiorev.2021.10.024 [R0809](https://doi.org/10.1016/j.neubiorev.2021.10.024)
  - [延伸文献(HED)] Chong et al. 2015. Dopamine enhances willingness to exert effort for reward in Parkinson's disease. *Cortex, 69, 40-46*. doi:10.1016/j.cortex.2015.04.003 [R0641](https://doi.org/10.1016/j.cortex.2015.04.003)
  - [延伸文献(HED)] Reddy et al. 2015. Effort-Based Decision-Making Paradigms for Clinical Trials in Schizophrenia: Part 1 — Psychometric Characteristics of 5 Paradigms. *Schizophrenia Bulletin, 41(5), 1045-1054*. doi:10.1093/schbul/sbv089 [R0642](https://doi.org/10.1093/schbul/sbv089)
  - [延伸文献(HED)] Husain & Roiser 2018. Neuroscience of apathy and anhedonia: a transdiagnostic approach. *Nature Reviews Neuroscience, 19(3), 164-178*. doi:10.1038/s41583-018-0029-9 [R0744](https://doi.org/10.1038/s41583-018-0029-9)

### CTL-RAT-001　远距离联想（创造力）　/ Remote associates test

- **优先级**：P3 长尾（BCI 相关度：基础）　**收录判定**：收录（新增，待确认）
- **可能的神经标记物**：α 功率　**记录模态**：EEG; fMRI
- **别名**：RAT; Remote Associates; Remote Associates Test
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_remote_associates.html
- **文献线索**（7 条）：
  - [关键文献(HED)] Mednick 1962. The associative basis of the creative process. *Psychological Review*. doi:10.1037/h0048850 [R0008](https://doi.org/10.1037/h0048850)
  - [关键文献(HED)] Bowden & Jung-Beeman 2003. Aha! Insight experience correlates with solution activation in the right hemisphere. *Psychonomic Bulletin & Review*. doi:10.3758/bf03196539 [R0245](https://doi.org/10.3758/bf03196539)
  - [关键文献(HED)] Jung-Beeman et al. 2004. Neural activity when people solve verbal problems with insight. *PLoS Biology*. doi:10.1371/journal.pbio.0020097 [R0283](https://doi.org/10.1371/journal.pbio.0020097)
  - [延伸文献(HED)] Beaty et al. 2014. The roles of associative and executive processes in creative cognition. *Memory & Cognition*. doi:10.3758/s13421-014-0428-8 [R0626](https://doi.org/10.3758/s13421-014-0428-8)
  - [延伸文献(HED)] Salvi et al. 2016. Insight solutions are correct more often than analytic solutions. *Thinking & Reasoning*. doi:10.1080/13546783.2016.1141798 [R0679](https://doi.org/10.1080/13546783.2016.1141798)
  - [延伸文献(HED)] Kounios & Beeman 2014. The cognitive neuroscience of insight. *Annual Review of Psychology*. doi:10.1146/annurev-psych-010213-115154 [R0622](https://doi.org/10.1146/annurev-psych-010213-115154)
  - [延伸文献(HED)] Olteteanu & Falomir 2015. comRAT-C: A computational compound Remote Associates Test solver based on language data and its comparison to human performance. *Pattern Recognition Letters*. doi:10.1016/j.patrec.2015.05.015 [R0669](https://doi.org/10.1016/j.patrec.2015.05.015)

### CTL-RAVEN-001　瑞文推理　/ Raven's progressive matrices

- **优先级**：P3 长尾（BCI 相关度：基础）　**收录判定**：收录（新增，待确认）
- **可能的神经标记物**：额顶 BOLD　**记录模态**：fMRI; EEG
- **别名**：Progressive Matrices; RPM; Raven's; Raven's Progressive Matrices; Raven's Progressive Matrices Test
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_ravens_progressive_matrices.html
- **备注**：以行为测量为主，需确认是否满足纳入标准 3
- **文献线索**（6 条）：
  - [关键文献(HED)] Carpenter et al. 1990. What one intelligence test measures: A theoretical account of the processing in the Raven Progressive Matrices Test. *Psychological Review, 97(3), 404–431*. doi:10.1037/0033-295x.97.3.404 [R0095](https://doi.org/10.1037/0033-295x.97.3.404)
  - [关键文献(HED)] Gray et al. 2003. Neural mechanisms of general fluid intelligence. *Nature Neuroscience, 6(3), 316–322*. doi:10.1038/nn1014 [R0257](https://doi.org/10.1038/nn1014)
  - [延伸文献(HED)] Prabhakaran et al. 1997. Neural substrates of fluid reasoning: An fMRI study of neocortical activation during performance of the Raven's Progressive Matrices test. *Cognitive Psychology, 33(1), 43–63*. doi:10.1006/cogp.1997.0659 [R0149](https://doi.org/10.1006/cogp.1997.0659)
  - [延伸文献(HED)] Kievit et al. 2016. A watershed model of individual differences in fluid intelligence. *Neuropsychologia, 91, 186–198*. doi:10.1016/j.neuropsychologia.2016.08.008 [R0671](https://doi.org/10.1016/j.neuropsychologia.2016.08.008)
  - [延伸文献(HED)] Matzen et al. 2010. Recreating Raven's: Software for systematically generating large numbers of Raven-like matrix problems with normed properties. *Behavior Research Methods, 42(2), 525–541*. doi:10.3758/brm.42.2.525 [R0475](https://doi.org/10.3758/brm.42.2.525)
  - [延伸文献(HED)] Hayes et al. 2015. Do we really become smarter when our fluid-intelligence test scores improve?. *Intelligence, 48, 1–14*. doi:10.1016/j.intell.2014.10.005 [R0640](https://doi.org/10.1016/j.intell.2014.10.005)

### CTL-TMT-001　连线测验　/ Trail making test

- **优先级**：P3 长尾（BCI 相关度：基础）　**收录判定**：收录（新增，待确认）
- **可能的神经标记物**：前额 HbO　**记录模态**：fNIRS; fMRI
- **别名**：TMT; Trail Making; Trail Making Test; Trails A/B
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_trail_making.html
- **备注**：以行为测量为主，需确认是否满足纳入标准 3
- **文献线索**（5 条）：
  - [关键文献(HED)] Reitan 1958. Validity of the Trail Making Test as an indicator of organic brain damage. *Perceptual and Motor Skills*. doi:10.2466/pms.1958.8.3.271 [R0005](https://doi.org/10.2466/pms.1958.8.3.271)
  - [关键文献(HED)] Bowie & Harvey 2006. Administration and interpretation of the Trail Making Test. *Nature Protocols*. doi:10.1038/nprot.2006.390 [R0336](https://doi.org/10.1038/nprot.2006.390)
  - [延伸文献(HED)] Salthouse 2011. What cognitive abilities are involved in trail-making performance?. *Intelligence*. doi:10.1016/j.intell.2011.03.001 [R0526](https://doi.org/10.1016/j.intell.2011.03.001)
  - [延伸文献(HED)] Sánchez-Cubillo & x 2009. Construct validity of the Trail Making Test: Role of task-switching, working memory, inhibition/interference control, and visuomotor abilities. *Journal of the International Neuropsychological Society*. doi:10.1017/s1355617709090626 [R0431](https://doi.org/10.1017/s1355617709090626)
  - [延伸文献(HED)] Cangoz et al. 2009. Trail Making Test: Normative data for Turkish elderly population by age, sex, and education. *Journal of the Neurological Sciences*. doi:10.1016/j.jns.2009.02.313 [R0450](https://doi.org/10.1016/j.jns.2009.02.313)

### CTL-WASON-001　Wason 选择任务　/ Wason selection task

- **优先级**：P3 长尾（BCI 相关度：基础）　**收录判定**：收录（新增，待确认）
- **可能的神经标记物**：前额 BOLD　**记录模态**：fMRI
- **别名**：Card Selection Task; Wason
- **HED 任务页**：https://www.hedtags.org/hed-task/tasks/hedtsk_wason_selection.html
- **文献线索**（6 条）：
  - [关键文献(HED)] Wason 1966. Reasoning.  [R0015]
  - [关键文献(HED)] Cosmides 1989. The logic of social exchange: Has natural selection shaped how humans reason? Studies with the Wason selection task. *Cognition*. doi:10.1016/0010-0277(89)90023-1 [R0089](https://doi.org/10.1016/0010-0277(89)90023-1)
  - [关键文献(HED)] Griggs & Cox 1982. The elusive thematic-materials effect in Wason's selection task. *British Journal of Psychology*. doi:10.1111/j.2044-8295.1982.tb01823.x [R0058](https://doi.org/10.1111/j.2044-8295.1982.tb01823.x)
  - [延伸文献(HED)] Sperber et al. 1995. Relevance theory explains the selection task. *Cognition*. doi:10.1016/0010-0277(95)00666-m [R0126](https://doi.org/10.1016/0010-0277(95)00666-m)
  - [延伸文献(HED)] Ragni & Johnson-Laird 2020. Reasoning about epistemic possibilities. *Acta Psychologica*. doi:10.1016/j.actpsy.2020.103081 [R0799](https://doi.org/10.1016/j.actpsy.2020.103081)
  - [延伸文献(HED)] Oaksford & Chater 1994. A rational analysis of the selection task as optimal data selection. *Psychological Review*. doi:10.1037/0033-295x.101.4.608 [R0110](https://doi.org/10.1037/0033-295x.101.4.608)
