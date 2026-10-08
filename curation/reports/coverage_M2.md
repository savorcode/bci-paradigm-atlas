# 覆盖度报告 里程碑 M2

> 由 `scripts/coverage_report.py` 生成（2026-10-05），数据来自 `paradigms/`、`knowledge/markers/`、`taxonomy/` 与 `curation/candidates.csv`（包归属）。请勿手工修改本文件，重新运行脚本即可。

## 1. 总数

| 项目 | 数量 |
|---|---|
| 范式文件（具体范式，不含 deprecated） | 404 |
| status: deprecated 的范式文件（并入其他具体范式，序号不复用） | 1（SSR-SSVEP-006） |
| 范式类（paradigms/_classes.yaml） | 267 |
| 有 `protocol` 的具体范式 | 404 |
| 标记物文件 | 129 |
| 范式–标记物关联（elicits） | 586 |
| 每个范式的平均标记物数 | 1.45 |
| 变体 | 11 |
| first_source 为 TBD 的范式 | 64（15.8%） |
| 出处已核实（verified: true）的 first_source | 0 |
| status: reviewed 的范式 | 0 |
| 未被任何范式使用的标记物 | 0 |

## 2. 分布

### 2.1 范式族

| 取值 | 范式数 | 占比 |
|---|---|---|
| perception（感知与注意） | 64 | 15.8% |
| motor（运动执行与想象） | 51 | 12.6% |
| steady_state（稳态响应） | 24 | 5.9% |
| error（错误监测与反馈） | 31 | 7.7% |
| language（语言） | 38 | 9.4% |
| memory（记忆） | 45 | 11.1% |
| emotion（情绪与情感） | 25 | 6.2% |
| control（认知控制） | 42 | 10.4% |
| imagery（非运动想象） | 17 | 4.2% |
| social（社会认知） | 30 | 7.4% |
| state（脑状态（静息、睡眠、警觉）） | 21 | 5.2% |
| stimulation（刺激诱发） | 16 | 4.0% |

### 2.2 工作包

| 取值 | 范式数 | 占比 |
|---|---|---|
| A（包 A） | 88 | 21.8% |
| B（包 B） | 84 | 20.8% |
| C（包 C） | 73 | 18.1% |
| D（包 D） | 83 | 20.5% |
| E（包 E） | 76 | 18.8% |

### 2.3 记录模态

一个范式可有多个记录模态，占比按范式数计算，合计可超过 100%。

| 取值 | 范式数 | 占比 |
|---|---|---|
| EEG（脑电图） | 334 | 82.7% |
| MEG（脑磁图） | 64 | 15.8% |
| fNIRS（功能近红外光谱） | 24 | 5.9% |
| fMRI（功能磁共振成像） | 182 | 45.0% |
| ECoG（皮层脑电） | 24 | 5.9% |
| sEEG（立体定向脑电） | 6 | 1.5% |
| intracortical（皮层内微电极记录） | 11 | 2.7% |
| fUS（功能超声） | 0 | 0.0% |
| PET（正电子发射断层成像） | 5 | 1.2% |
| other（其他） | 2 | 0.5% |

### 2.4 刺激模态

一个范式可有多个刺激模态。

| 取值 | 范式数 | 占比 |
|---|---|---|
| visual（视觉） | 308 | 76.2% |
| auditory（听觉） | 108 | 26.7% |
| somatosensory（体感 / 触觉） | 18 | 4.5% |
| olfactory（嗅觉） | 3 | 0.7% |
| gustatory（味觉） | 2 | 0.5% |
| electrical_stimulation（电刺激） | 17 | 4.2% |
| magnetic_stimulation（磁刺激） | 4 | 1.0% |
| ultrasound_stimulation（超声刺激） | 1 | 0.2% |
| motor_execution（运动执行） | 57 | 14.1% |
| mental_imagery（心理想象（运动、视觉、听觉、言语）） | 31 | 7.7% |
| cognitive_task（无外部刺激的认知任务） | 20 | 5.0% |
| resting_state（静息态） | 6 | 1.5% |
| naturalistic（自然场景（影片、叙事、游戏）） | 9 | 2.2% |
| optical_stimulation（组织光刺激（经颅光生物调节；不含视觉光刺激）） | 1 | 0.2% |
| pharmacological（药物给予（麻醉药、精神活性药物）） | 2 | 0.5% |

### 2.5 BCI 类别

| 取值 | 范式数 | 占比 |
|---|---|---|
| active（主动） | 59 | 14.6% |
| reactive（反应式） | 26 | 6.4% |
| passive（被动） | 37 | 9.2% |
| none（非 BCI） | 320 | 79.2% |

### 2.6 标记物类型

| 类型 | 标记物数 | 范式–标记物关联数 |
|---|---|---|
| erp_component（事件相关电位 / 磁场成分） | 64 | 236 |
| oscillatory（节律调制（ERD/ERS、功率、相位）） | 18 | 127 |
| steady_state（稳态诱发响应） | 12 | 26 |
| hemodynamic（血流动力学响应（BOLD、HbO/HbR）） | 26 | 160 |
| single_unit（单 / 多神经元放电） | 1 | 7 |
| field_potential（局部场电位或高 gamma 活动） | 2 | 18 |
| connectivity（功能连接模式） | 6 | 12 |

### 2.7 包 × 族

| 包 | 族 | 范式数 | TBD |
|---|---|---|---|
| A | perception | 64 | 25 |
| A | steady_state | 24 | 7 |
| B | imagery | 17 | 0 |
| B | motor | 51 | 5 |
| B | stimulation | 16 | 0 |
| C | control | 42 | 4 |
| C | error | 31 | 3 |
| D | language | 38 | 6 |
| D | memory | 45 | 10 |
| E | emotion | 25 | 2 |
| E | social | 30 | 0 |
| E | state | 21 | 2 |

## 3. first_source 为 TBD 的范式

共 64 个。

| 包 | ID | 名称 | 族 |
|---|---|---|---|
| A | PER-ABR-001 | 听觉脑干反应 | perception |
| A | PER-ACC-001 | 声学变化复合波 | perception |
| A | PER-ADDS-001 | 附加单例与干扰抑制 | perception |
| A | PER-AEP-001 | 听觉诱发电位（纯音/短声） | perception |
| A | PER-AMASK-001 | 听觉掩蔽 | perception |
| A | PER-BR-001 | 双眼竞争与双稳态知觉 | perception |
| A | PER-BR-002 | 频率标记双眼竞争 | perception |
| A | PER-CB-001 | 变化盲 | perception |
| A | PER-CVA-002 | 隐蔽注意 α 偏侧化脑机接口 | perception |
| A | PER-FVEP-001 | 闪光视觉诱发电位 | perception |
| A | PER-GATE-001 | 配对短声感觉门控 | perception |
| A | PER-GEP-001 | 味觉诱发电位 | perception |
| A | PER-IB-001 | 非注意盲 | perception |
| A | PER-IC-001 | 错觉轮廓知觉 | perception |
| A | PER-MLR-001 | 听觉中潜伏期反应 | perception |
| A | PER-MSI-002 | 简单刺激的视听交互（加性模型） | perception |
| A | PER-MVEP-001 | 运动起始视觉诱发电位 | perception |
| A | PER-OLF-001 | 嗅觉诱发电位 | perception |
| A | PER-OMIT-001 | 刺激遗漏范式 | perception |
| A | PER-PRVEP-001 | 棋盘格翻转 VEP | perception |
| A | PER-RREP-001 | 呼吸相关诱发电位 | perception |
| A | PER-SPN-001 | 视觉对称知觉 | perception |
| A | PER-TACT-001 | 触觉空间注意 | perception |
| A | PER-VMMN-001 | 视觉失匹配负波 | perception |
| A | PER-VOICE-001 | 嗓音知觉（颞叶嗓音区定位） | perception |
| A | SSR-CVEP-001 | 编码调制视觉诱发电位 | steady_state |
| A | SSR-FFR-002 | 语音诱发 FFR（复杂声听觉脑干反应） | steady_state |
| A | SSR-FPVS-001 | 快速周期视觉刺激（频率标记） | steady_state |
| A | SSR-RVS-001 | 节律性视觉刺激（α 夹带） | steady_state |
| A | SSR-SSSEP-001 | 稳态体感诱发电位 | steady_state |
| A | SSR-SSVEP-008 | 异步（自定步调）SSVEP 脑机接口 | steady_state |
| A | SSR-SWEEP-001 | 扫描 VEP（视敏度评估） | steady_state |
| B | MOT-ME-003 | 地面/跑步机行走 | motor |
| B | MOT-MI-005 | 带连续视觉反馈的左/右手运动想象 | motor |
| B | MOT-MI-006 | 右手对双脚运动想象（提示驱动，无反馈） | motor |
| B | MOT-MI-009 | 异步（自定步调）运动想象（含空闲态） | motor |
| B | MOT-REACH-002 | 四方向腕部中心外伸运动（脑磁） | motor |
| C | CTL-FLK-002 | Flanker 任务（箭头版） | control |
| C | CTL-SIM-002 | Simon 任务（视觉版） | control |
| C | CTL-STR-002 | Stroop 任务（单试次计算机化颜色词） | control |
| C | CTL-SW-003 | 自主任务切换 | control |
| C | ERR-AAF-001 | 音高偏移听觉反馈（言语运动误差） | error |
| C | ERR-ERRP-003 | P300 拼写器反馈错误电位 | error |
| C | ERR-GAM-002 | 门选择猜测任务（doors task） | error |
| D | LAN-GEST-001 | 言语—手势整合 | language |
| D | LAN-NWL-001 | 新词学习 | language |
| D | LAN-PN-002 | 图词干扰 | language |
| D | LAN-PRIME-002 | 掩蔽语义启动 | language |
| D | LAN-SWITCH-001 | 双语语言切换 | language |
| D | LAN-VF-003 | 言语流畅性 fNIRS 组块设计 | language |
| D | MEM-DF-002 | 列表法定向遗忘 | memory |
| D | MEM-DS-002 | 倒背数字广度 | memory |
| D | MEM-NAV-003 | 虚拟 Morris 水迷宫 | memory |
| D | MEM-NBK-002 | 含 0-back 控制的多负荷 n-back（组块设计） | memory |
| D | MEM-PA-001 | 配对联想学习 | memory |
| D | MEM-PA-002 | 视空间配对联想学习 | memory |
| D | MEM-PM-002 | 时间型前瞻记忆 | memory |
| D | MEM-RMEM-001 | 奖赏驱动的记忆编码 | memory |
| D | MEM-RPRIM-001 | 重复启动（内隐记忆） | memory |
| D | MEM-RPT-001 | 近期探测任务（前摄干扰） | memory |
| E | EMO-EST-001 | 情绪 Stroop | emotion |
| E | EMO-FILM-004 | 影片片段四分类情绪诱发（SEED-IV） | emotion |
| E | STA-DRV-002 | 连续模拟驾驶（眼动警觉标注） | state |
| E | STA-SCP-001 | 慢皮层电位自我调节训练（二分类） | state |

## 4. 被 ≥3 个范式使用的标记物

共 64 个。

| 标记物 | 类型 | 范式数 | 涉及族数 | 范式 |
|---|---|---|---|---|
| MK.SMR_ERD | oscillatory | 39 | 5 | IMG-CMD-001, IMG-CMD-002, IMG-SAO-001, IMG-SAO-002, IMG-TACT-001, MOT-ATT-001, MOT-ATT-002, MOT-ATT-003, MOT-BIMAN-001, MOT-CURSOR-001, MOT-CURSOR-002, MOT-FORCE-001, MOT-GRASP-003, MOT-GRASP-004, MOT-ME-001, MOT-ME-002, MOT-ME-003, MOT-ME-005, MOT-MI-001, MOT-MI-002, MOT-MI-003, MOT-MI-004, MOT-MI-005, MOT-MI-006, MOT-MI-007, MOT-MI-008, MOT-MI-009, MOT-MI-010, MOT-MI-011, MOT-MSL-001, MOT-MVF-001, MOT-OBS-001, MOT-PASS-001, MOT-SMS-001, MOT-SRT-001, SOC-IMIT-001, SOC-JA-001, STA-NF-001, STM-PHTMS-001 |
| MK.P3b | erp_component | 35 | 7 | CTL-ANT-001, CTL-ANT-002, CTL-CPT-001, CTL-CPT-002, CTL-DT-001, CTL-WCST-001, ERR-ADAPT-002, ERR-CHGPT-001, ERR-CHGPT-002, MEM-CIT-001, MEM-CIT-002, MEM-NBK-001, MEM-NBK-002, PER-AB-001, PER-IB-001, PER-LG-001, PER-MASK-001, PER-NAVON-001, PER-ODD-001, PER-ODD-002, PER-ODD-003, PER-ODD-004, PER-ODD-005, PER-ODD-006, PER-ODD-007, PER-ODD-008, PER-ODD-009, PER-TACT-001, SOC-CYB-001, SOC-NAME-001, SOC-NAME-002, SOC-SELF-001, STA-MW-001, STA-MW-002, STM-TAVNS-001 |
| MK.alpha_posterior | oscillatory | 25 | 6 | CTL-AUT-001, CTL-RAT-001, CTL-SART-001, IMG-ROT-001, IMG-VIS-001, MEM-DF-001, MEM-DF-002, MEM-DMS-001, MEM-NBK-001, MEM-NBK-002, MEM-SB-001, SOC-VPT-001, STA-DRV-001, STA-DRV-002, STA-ENG-001, STA-MATB-001, STA-MED-001, STA-MW-001, STA-MW-002, STA-NF-001, STA-PSY-001, STA-PVT-001, STA-REST-001, STA-REST-002, STM-PBM-001 |
| MK.BOLD_striatum_reward | hemodynamic | 18 | 5 | CTL-AMBIG-001, CTL-DD-001, CTL-MIXG-001, EMO-HUMOR-001, EMO-MID-001, EMO-MID-002, ERR-APC-001, ERR-INST-001, ERR-PCL-001, ERR-PRL-001, ERR-TS-001, ERR-TS-002, MEM-RMEM-001, SOC-CONF-001, SOC-GAZE-002, SOC-TRUST-001, SOC-TRUST-002, SOC-TRUST-003 |
| MK.FRN | erp_component | 18 | 4 | CTL-BART-001, CTL-IGT-001, EMO-MID-001, ERR-ADAPT-001, ERR-ADAPT-002, ERR-BANDIT-001, ERR-GAM-001, ERR-GAM-002, ERR-GAM-003, ERR-INST-001, ERR-PRL-001, ERR-PRT-001, ERR-PSEL-001, ERR-TE-001, ERR-TS-001, SOC-TRUST-001, SOC-TRUST-002, SOC-UG-001 |
| MK.high_gamma | field_potential | 17 | 4 | IMG-AUD-001, IMG-SPI-001, IMG-SPI-002, IMG-SPI-003, LAN-OVS-001, LAN-OVS-002, LAN-OVS-003, LAN-PCAT-001, LAN-PN-001, LAN-SIS-001, MEM-FR-001, MOT-GRASP-001, MOT-GRASP-002, MOT-ME-001, MOT-ME-002, MOT-REACH-001, MOT-TRACK-001 |
| MK.frontal_midline_theta | oscillatory | 16 | 6 | CTL-DT-001, CTL-SW-001, CTL-SW-002, CTL-SW-003, EMO-FC-003, ERR-OGNG-001, ERR-PSEL-001, IMG-MA-001, IMG-MA-002, MEM-DS-001, MEM-DS-002, MEM-NBK-001, MEM-NBK-002, MEM-SB-001, STA-MATB-001, STA-MED-001 |
| MK.BOLD_hippocampus | hemodynamic | 13 | 2 | MEM-EFT-001, MEM-MST-001, MEM-MST-002, MEM-NAV-001, MEM-NAV-002, MEM-NAV-003, MEM-PA-001, MEM-PA-002, MEM-RMEM-001, MEM-SME-001, MEM-TMR-002, MEM-TNT-001, PER-CTXC-001 |
| MK.BOLD_amygdala | hemodynamic | 11 | 3 | CTL-AMBIG-001, EMO-AUTO-001, EMO-FACE-001, EMO-FACE-002, EMO-FC-001, EMO-FC-002, EMO-FC-003, EMO-IAPS-001, EMO-REG-002, EMO-THREAT-001, STA-NF-002 |
| MK.BOLD_frontoparietal | hemodynamic | 11 | 6 | CTL-RAVEN-001, CTL-SYLL-001, ERR-AWARE-003, IMG-ROT-001, MEM-NBK-001, MEM-NBK-002, MEM-NBK-003, MEM-NBK-004, MEM-SWM-001, MOT-SACC-002, PER-MOT-001 |
| MK.HbO_prefrontal | hemodynamic | 11 | 6 | CTL-TOL-001, CTL-WCST-001, EMO-STRESS-001, EMO-STRESS-002, IMG-MA-001, LAN-VF-001, LAN-VF-002, LAN-VF-003, MEM-NBK-001, MEM-NBK-002, STA-MATB-001 |
| MK.N400 | erp_component | 11 | 4 | EMO-APRIME-001, LAN-GEST-001, LAN-LDT-001, LAN-N400-001, LAN-N400-002, LAN-NWL-001, LAN-PRIME-001, LAN-PRIME-002, LAN-SC-001, MEM-RPRIM-001, SOC-IAT-001 |
| MK.LPP | erp_component | 10 | 2 | EMO-APRIME-001, EMO-EST-001, EMO-IAPS-001, EMO-REG-001, EMO-REG-002, EMO-SOUND-001, EMO-WORD-001, SOC-IAT-001, SOC-PAIN-001, SOC-PAIN-002 |
| MK.N2_frontocentral | erp_component | 10 | 5 | CTL-FLK-001, CTL-FLK-002, CTL-GNG-001, CTL-SIM-001, CTL-SIM-002, EMO-EST-001, LAN-SWITCH-001, LAN-SWITCH-002, MEM-TNT-001, SOC-WIT-001 |
| MK.BOLD_category_selective | hemodynamic | 9 | 4 | IMG-VIS-001, IMG-VIS-002, LAN-VWFA-001, MEM-CFMT-001, MEM-RIF-001, MEM-RPRIM-001, PER-BODY-001, PER-CAT-001, PER-FACE-001 |
| MK.BOLD_language_network | hemodynamic | 9 | 1 | LAN-LOC-001, LAN-LOC-002, LAN-PHA-001, LAN-PN-001, LAN-PN-002, LAN-SC-001, LAN-SC-002, LAN-SEMD-001, LAN-VG-001 |
| MK.N170 | erp_component | 9 | 5 | EMO-FACE-001, LAN-VWFA-001, MEM-CFMT-001, PER-BODY-001, PER-CAT-001, PER-FACE-001, SOC-BIO-001, SOC-GAZE-001, SOC-SELF-001 |
| MK.SSVEP | steady_state | 9 | 2 | PER-BR-002, SSR-SSVEP-001, SSR-SSVEP-002, SSR-SSVEP-003, SSR-SSVEP-004, SSR-SSVEP-005, SSR-SSVEP-007, SSR-SSVEP-008, SSR-SWEEP-001 |
| MK.BOLD_dlPFC | hemodynamic | 8 | 4 | CTL-BART-001, CTL-RNG-001, CTL-TOL-001, CTL-WASON-001, CTL-WCST-001, ERR-CAUS-001, MEM-DF-001, SOC-TPP-001 |
| MK.BOLD_motor_network | hemodynamic | 8 | 3 | IMG-CMD-001, IMG-CMD-003, MOT-ME-001, MOT-ME-004, MOT-MIRR-001, MOT-MSL-001, MOT-SMS-001, STM-VIB-001 |
| MK.N1_auditory | erp_component | 8 | 4 | ERR-AAF-001, LAN-SIS-001, LAN-SIS-002, MOT-IB-001, PER-AAD-001, PER-ACC-001, PER-AEP-001, PER-AMASK-001 |
| MK.low_freq_kinematics | oscillatory | 8 | 1 | MOT-ATT-003, MOT-GRASP-003, MOT-HW-002, MOT-ME-005, MOT-MI-003, MOT-REACH-002, MOT-TRACK-001, MOT-TRACK-002 |
| MK.BOLD_dACC | hemodynamic | 7 | 3 | CTL-EFF-001, CTL-FORAGE-001, CTL-MSIT-001, SOC-CONF-001, SOC-CYB-001, SOC-SFB-001, STA-HYPN-001 |
| MK.ErrP | erp_component | 7 | 1 | ERR-ADAPT-001, ERR-ERRP-001, ERR-ERRP-002, ERR-ERRP-003, ERR-ERRP-004, ERR-OBS-001, ERR-VRPE-001 |
| MK.MMN | erp_component | 7 | 2 | LAN-PHA-001, PER-AMASK-001, PER-LG-001, PER-MMN-001, PER-MMN-002, PER-MMN-003, PER-STREAM-001 |
| MK.motor_cortical_spiking | single_unit | 7 | 2 | LAN-OVS-003, MOT-ATT-001, MOT-CURSOR-001, MOT-CURSOR-003, MOT-GRASP-001, MOT-HW-001, MOT-REACH-001 |
| MK.BOLD_TPJ | hemodynamic | 6 | 1 | SOC-ANIM-001, SOC-IMIT-001, SOC-RME-001, SOC-TOM-001, SOC-TOM-002, SOC-VPT-001 |
| MK.BOLD_frontopolar | hemodynamic | 6 | 3 | CTL-ANAL-001, ERR-BANDIT-001, MEM-META-001, MEM-META-002, MEM-PM-001, MEM-PM-002 |
| MK.BOLD_vmPFC_value | hemodynamic | 6 | 2 | CTL-DD-001, CTL-IGT-001, CTL-MIXG-001, CTL-VBC-001, SOC-DICT-001, SOC-DICT-002 |
| MK.LRP | erp_component | 6 | 2 | CTL-FLK-002, CTL-MRP-001, CTL-SIM-001, CTL-SIM-002, MOT-RT-001, MOT-SRT-001 |
| MK.slow_wave | oscillatory | 6 | 2 | MEM-TMR-001, STA-ANES-001, STA-CLAS-001, STA-DREAM-001, STA-SLP-001, STA-SLP-002 |
| MK.BOLD_mPFC | hemodynamic | 5 | 2 | MEM-EFT-001, MEM-SRE-001, SOC-ANIM-001, SOC-MORAL-001, SOC-RME-001 |
| MK.BOLD_visual_cortex | hemodynamic | 5 | 2 | IMG-VIS-001, PER-BR-001, PER-NAT-001, PER-RET-001, PER-RET-002 |
| MK.DMN_connectivity | connectivity | 5 | 2 | CTL-CPT-003, STA-HYPN-001, STA-MW-001, STA-PSY-001, STA-REST-001 |
| MK.MRCP | erp_component | 5 | 1 | MOT-IB-001, MOT-LIBET-001, MOT-MRCP-001, MOT-MRCP-002, MOT-MRCP-003 |
| MK.N1_visual | erp_component | 5 | 2 | CTL-ANT-001, CTL-ANT-002, PER-CUE-001, PER-CUE-002, PER-IC-001 |
| MK.Pe | erp_component | 5 | 2 | CTL-CONF-001, CTL-FLK-001, CTL-FLK-002, ERR-AWARE-001, ERR-AWARE-002 |
| MK.affective_band_power | oscillatory | 5 | 1 | EMO-AUTO-001, EMO-FILM-001, EMO-FILM-002, EMO-FILM-003, EMO-FILM-004 |
| MK.frontal_alpha_asymmetry | oscillatory | 5 | 1 | EMO-FILM-001, EMO-FILM-002, EMO-FILM-003, EMO-FILM-004, EMO-STRESS-001 |
| MK.BOLD_anterior_insula | hemodynamic | 4 | 2 | EMO-THREAT-001, SOC-PAIN-001, SOC-PAIN-002, SOC-UG-001 |
| MK.BOLD_auditory_cortex | hemodynamic | 4 | 2 | IMG-AUD-001, IMG-AUD-002, PER-TON-001, PER-VOICE-001 |
| MK.BOLD_oculomotor | hemodynamic | 4 | 2 | CTL-AS-001, MOT-PURS-001, MOT-SACC-001, MOT-SACC-002 |
| MK.BOLD_stimulated_region | hemodynamic | 4 | 1 | STM-TDCS-001, STM-TI-001, STM-TMSFMRI-001, STM-TUS-001 |
| MK.CDA | erp_component | 4 | 2 | MEM-CD-001, MEM-CD-002, MEM-CD-003, PER-MOT-001 |
| MK.CNV | erp_component | 4 | 1 | CTL-ANT-001, CTL-ANT-002, CTL-CNV-001, CTL-CPT-002 |
| MK.P1_visual | erp_component | 4 | 3 | EMO-DOT-001, PER-CUE-001, PER-CUE-002, SOC-GAZE-001 |
| MK.P2_auditory | erp_component | 4 | 3 | EMO-SOUND-001, ERR-AAF-001, PER-ACC-001, PER-AEP-001 |
| MK.P600 | erp_component | 4 | 1 | LAN-AGL-001, LAN-P600-001, LAN-P600-002, LAN-SC-001 |
| MK.sleep_spindle | oscillatory | 4 | 2 | MEM-TMR-001, STA-CLAS-001, STA-SLP-001, STA-SLP-002 |
| MK.BOLD_pSTS | hemodynamic | 3 | 1 | SOC-BIO-001, SOC-GAZE-001, SOC-GAZE-002 |
| MK.Dm | erp_component | 3 | 1 | MEM-FR-001, MEM-FR-002, MEM-SME-001 |
| MK.EPN | erp_component | 3 | 1 | EMO-FACE-001, EMO-IAPS-001, EMO-WORD-001 |
| MK.ERN | erp_component | 3 | 2 | CTL-FLK-001, CTL-FLK-002, ERR-AWARE-002 |
| MK.FN400 | erp_component | 3 | 1 | MEM-DRM-001, MEM-ON-001, MEM-ON-002 |
| MK.N2pc | erp_component | 3 | 2 | EMO-DOT-001, PER-CTXC-001, PER-VS-001 |
| MK.NoGo_P3 | erp_component | 3 | 1 | CTL-GNG-001, CTL-SART-001, CTL-SST-001 |
| MK.SEP_N20 | erp_component | 3 | 1 | STM-PAS-001, STM-SEP-001, STM-TUS-001 |
| MK.VAN | erp_component | 3 | 1 | PER-CB-001, PER-IB-001, PER-MASK-001 |
| MK.alpha_lateralization | oscillatory | 3 | 2 | MEM-RC-001, PER-CVA-001, PER-CVA-002 |
| MK.cVEP | steady_state | 3 | 1 | SSR-CVEP-001, SSR-CVEP-002, SSR-CVEP-003 |
| MK.hippocampal_theta | oscillatory | 3 | 1 | MEM-NAV-001, MEM-NAV-003, MEM-PA-001 |
| MK.oERN | erp_component | 3 | 1 | ERR-OBS-001, ERR-OBS-002, ERR-OBS-003 |
| MK.parietal_old_new | erp_component | 3 | 1 | MEM-DRM-001, MEM-ON-001, MEM-ON-002 |
| MK.theta_drowsiness | oscillatory | 3 | 1 | STA-DRV-001, STA-DRV-002, STA-PVT-001 |

## 5. 每个标记物的范式数

### 5.1 分布

| 使用该标记物的范式数 | 标记物数 |
|---|---|
| 1 | 40 |
| 2 | 25 |
| 3 | 15 |
| 4 | 10 |
| 5 | 8 |
| 6 | 5 |
| 7 | 4 |
| 8 | 4 |
| 9 | 4 |
| 10 | 2 |
| 11 | 4 |
| 13 | 1 |
| 16 | 1 |
| 17 | 1 |
| 18 | 2 |
| 25 | 1 |
| 35 | 1 |
| 39 | 1 |

### 5.2 全表

| 标记物 | 类型 | 范式数 | 范式 |
|---|---|---|---|
| MK.ABR | erp_component | 1 | PER-ABR-001 |
| MK.ASSR | steady_state | 2 | SSR-ASSR-001, SSR-ASSR-002 |
| MK.AV_interaction_ERP | erp_component | 2 | PER-MSI-001, PER-MSI-002 |
| MK.BOLD_TPJ | hemodynamic | 6 | SOC-ANIM-001, SOC-IMIT-001, SOC-RME-001, SOC-TOM-001, SOC-TOM-002, SOC-VPT-001 |
| MK.BOLD_amygdala | hemodynamic | 11 | CTL-AMBIG-001, EMO-AUTO-001, EMO-FACE-001, EMO-FACE-002, EMO-FC-001, EMO-FC-002, EMO-FC-003, EMO-IAPS-001, EMO-REG-002, EMO-THREAT-001, STA-NF-002 |
| MK.BOLD_anterior_insula | hemodynamic | 4 | EMO-THREAT-001, SOC-PAIN-001, SOC-PAIN-002, SOC-UG-001 |
| MK.BOLD_auditory_cortex | hemodynamic | 4 | IMG-AUD-001, IMG-AUD-002, PER-TON-001, PER-VOICE-001 |
| MK.BOLD_category_selective | hemodynamic | 9 | IMG-VIS-001, IMG-VIS-002, LAN-VWFA-001, MEM-CFMT-001, MEM-RIF-001, MEM-RPRIM-001, PER-BODY-001, PER-CAT-001, PER-FACE-001 |
| MK.BOLD_dACC | hemodynamic | 7 | CTL-EFF-001, CTL-FORAGE-001, CTL-MSIT-001, SOC-CONF-001, SOC-CYB-001, SOC-SFB-001, STA-HYPN-001 |
| MK.BOLD_dlPFC | hemodynamic | 8 | CTL-BART-001, CTL-RNG-001, CTL-TOL-001, CTL-WASON-001, CTL-WCST-001, ERR-CAUS-001, MEM-DF-001, SOC-TPP-001 |
| MK.BOLD_frontoparietal | hemodynamic | 11 | CTL-RAVEN-001, CTL-SYLL-001, ERR-AWARE-003, IMG-ROT-001, MEM-NBK-001, MEM-NBK-002, MEM-NBK-003, MEM-NBK-004, MEM-SWM-001, MOT-SACC-002, PER-MOT-001 |
| MK.BOLD_frontopolar | hemodynamic | 6 | CTL-ANAL-001, ERR-BANDIT-001, MEM-META-001, MEM-META-002, MEM-PM-001, MEM-PM-002 |
| MK.BOLD_hippocampus | hemodynamic | 13 | MEM-EFT-001, MEM-MST-001, MEM-MST-002, MEM-NAV-001, MEM-NAV-002, MEM-NAV-003, MEM-PA-001, MEM-PA-002, MEM-RMEM-001, MEM-SME-001, MEM-TMR-002, MEM-TNT-001, PER-CTXC-001 |
| MK.BOLD_language_network | hemodynamic | 9 | LAN-LOC-001, LAN-LOC-002, LAN-PHA-001, LAN-PN-001, LAN-PN-002, LAN-SC-001, LAN-SC-002, LAN-SEMD-001, LAN-VG-001 |
| MK.BOLD_left_IFG | hemodynamic | 1 | MEM-RPT-001 |
| MK.BOLD_mPFC | hemodynamic | 5 | MEM-EFT-001, MEM-SRE-001, SOC-ANIM-001, SOC-MORAL-001, SOC-RME-001 |
| MK.BOLD_motor_network | hemodynamic | 8 | IMG-CMD-001, IMG-CMD-003, MOT-ME-001, MOT-ME-004, MOT-MIRR-001, MOT-MSL-001, MOT-SMS-001, STM-VIB-001 |
| MK.BOLD_oculomotor | hemodynamic | 4 | CTL-AS-001, MOT-PURS-001, MOT-SACC-001, MOT-SACC-002 |
| MK.BOLD_olfactory_cortex | hemodynamic | 1 | IMG-OLF-001 |
| MK.BOLD_pSTS | hemodynamic | 3 | SOC-BIO-001, SOC-GAZE-001, SOC-GAZE-002 |
| MK.BOLD_parahippocampal | hemodynamic | 2 | IMG-CMD-001, IMG-CMD-003 |
| MK.BOLD_posterior_insula | hemodynamic | 1 | EMO-TOUCH-001 |
| MK.BOLD_premotor_parietal | hemodynamic | 2 | MOT-OBS-001, PER-BOI-001 |
| MK.BOLD_stimulated_region | hemodynamic | 4 | STM-TDCS-001, STM-TI-001, STM-TMSFMRI-001, STM-TUS-001 |
| MK.BOLD_striatum_reward | hemodynamic | 18 | CTL-AMBIG-001, CTL-DD-001, CTL-MIXG-001, EMO-HUMOR-001, EMO-MID-001, EMO-MID-002, ERR-APC-001, ERR-INST-001, ERR-PCL-001, ERR-PRL-001, ERR-TS-001, ERR-TS-002, MEM-RMEM-001, SOC-CONF-001, SOC-GAZE-002, SOC-TRUST-001, SOC-TRUST-002, SOC-TRUST-003 |
| MK.BOLD_vestibular_cortex | hemodynamic | 1 | STM-GVS-001 |
| MK.BOLD_visual_cortex | hemodynamic | 5 | IMG-VIS-001, PER-BR-001, PER-NAT-001, PER-RET-001, PER-RET-002 |
| MK.BOLD_vmPFC_value | hemodynamic | 6 | CTL-DD-001, CTL-IGT-001, CTL-MIXG-001, CTL-VBC-001, SOC-DICT-001, SOC-DICT-002 |
| MK.CCEP | erp_component | 1 | STM-CCEP-001 |
| MK.CDA | erp_component | 4 | MEM-CD-001, MEM-CD-002, MEM-CD-003, PER-MOT-001 |
| MK.CNV | erp_component | 4 | CTL-ANT-001, CTL-ANT-002, CTL-CNV-001, CTL-CPT-002 |
| MK.CPP | erp_component | 2 | CTL-PDM-001, CTL-PDM-002 |
| MK.CPS | erp_component | 2 | LAN-CPS-001, LAN-CPS-002 |
| MK.DBS_cortical_EP | erp_component | 1 | STM-DBSEP-001 |
| MK.DMN_connectivity | connectivity | 5 | CTL-CPT-003, STA-HYPN-001, STA-MW-001, STA-PSY-001, STA-REST-001 |
| MK.Dm | erp_component | 3 | MEM-FR-001, MEM-FR-002, MEM-SME-001 |
| MK.EPN | erp_component | 3 | EMO-FACE-001, EMO-IAPS-001, EMO-WORD-001 |
| MK.ERAN | erp_component | 2 | LAN-AGL-001, LAN-MUS-001 |
| MK.ERN | erp_component | 3 | CTL-FLK-001, CTL-FLK-002, ERR-AWARE-002 |
| MK.ERNA | field_potential | 1 | STM-DBSEP-001 |
| MK.ErrP | erp_component | 7 | ERR-ADAPT-001, ERR-ERRP-001, ERR-ERRP-002, ERR-ERRP-003, ERR-ERRP-004, ERR-OBS-001, ERR-VRPE-001 |
| MK.FFR | steady_state | 2 | SSR-FFR-001, SSR-FFR-002 |
| MK.FN400 | erp_component | 3 | MEM-DRM-001, MEM-ON-001, MEM-ON-002 |
| MK.FPAS_oddball | steady_state | 1 | SSR-FPAS-001 |
| MK.FPVS_oddball | steady_state | 1 | SSR-FPVS-001 |
| MK.FRN | erp_component | 18 | CTL-BART-001, CTL-IGT-001, EMO-MID-001, ERR-ADAPT-001, ERR-ADAPT-002, ERR-BANDIT-001, ERR-GAM-001, ERR-GAM-002, ERR-GAM-003, ERR-INST-001, ERR-PRL-001, ERR-PRT-001, ERR-PSEL-001, ERR-TE-001, ERR-TS-001, SOC-TRUST-001, SOC-TRUST-002, SOC-UG-001 |
| MK.FRP | erp_component | 1 | LAN-READ-001 |
| MK.GEP | erp_component | 1 | PER-GEP-001 |
| MK.HEP | erp_component | 2 | PER-HBD-001, PER-HBD-002 |
| MK.HbO_prefrontal | hemodynamic | 11 | CTL-TOL-001, CTL-WCST-001, EMO-STRESS-001, EMO-STRESS-002, IMG-MA-001, LAN-VF-001, LAN-VF-002, LAN-VF-003, MEM-NBK-001, MEM-NBK-002, STA-MATB-001 |
| MK.ISC | connectivity | 2 | PER-NAT-001, STA-ENG-001 |
| MK.LEP | erp_component | 1 | PER-LEP-001 |
| MK.LPP | erp_component | 10 | EMO-APRIME-001, EMO-EST-001, EMO-IAPS-001, EMO-REG-001, EMO-REG-002, EMO-SOUND-001, EMO-WORD-001, SOC-IAT-001, SOC-PAIN-001, SOC-PAIN-002 |
| MK.LRP | erp_component | 6 | CTL-FLK-002, CTL-MRP-001, CTL-SIM-001, CTL-SIM-002, MOT-RT-001, MOT-SRT-001 |
| MK.MLR | erp_component | 1 | PER-MLR-001 |
| MK.MMN | erp_component | 7 | LAN-PHA-001, PER-AMASK-001, PER-LG-001, PER-MMN-001, PER-MMN-002, PER-MMN-003, PER-STREAM-001 |
| MK.MRCP | erp_component | 5 | MOT-IB-001, MOT-LIBET-001, MOT-MRCP-001, MOT-MRCP-002, MOT-MRCP-003 |
| MK.N140_somatosensory | erp_component | 1 | PER-TACT-001 |
| MK.N170 | erp_component | 9 | EMO-FACE-001, LAN-VWFA-001, MEM-CFMT-001, PER-BODY-001, PER-CAT-001, PER-FACE-001, SOC-BIO-001, SOC-GAZE-001, SOC-SELF-001 |
| MK.N1_auditory | erp_component | 8 | ERR-AAF-001, LAN-SIS-001, LAN-SIS-002, MOT-IB-001, PER-AAD-001, PER-ACC-001, PER-AEP-001, PER-AMASK-001 |
| MK.N1_visual | erp_component | 5 | CTL-ANT-001, CTL-ANT-002, PER-CUE-001, PER-CUE-002, PER-IC-001 |
| MK.N2_frontocentral | erp_component | 10 | CTL-FLK-001, CTL-FLK-002, CTL-GNG-001, CTL-SIM-001, CTL-SIM-002, EMO-EST-001, LAN-SWITCH-001, LAN-SWITCH-002, MEM-TNT-001, SOC-WIT-001 |
| MK.N2_posterior | erp_component | 2 | PER-NAVON-001, SOC-BIO-001 |
| MK.N2pc | erp_component | 3 | EMO-DOT-001, PER-CTXC-001, PER-VS-001 |
| MK.N300_prospective | erp_component | 1 | MEM-PM-001 |
| MK.N400 | erp_component | 11 | EMO-APRIME-001, LAN-GEST-001, LAN-LDT-001, LAN-N400-001, LAN-N400-002, LAN-NWL-001, LAN-PRIME-001, LAN-PRIME-002, LAN-SC-001, MEM-RPRIM-001, SOC-IAT-001 |
| MK.N450 | erp_component | 2 | CTL-STR-001, CTL-STR-002 |
| MK.NoGo_P3 | erp_component | 3 | CTL-GNG-001, CTL-SART-001, CTL-SST-001 |
| MK.OERP | erp_component | 1 | PER-OLF-001 |
| MK.ORN | erp_component | 1 | PER-ORN-001 |
| MK.P100_PRVEP | erp_component | 1 | PER-PRVEP-001 |
| MK.P1_visual | erp_component | 4 | EMO-DOT-001, PER-CUE-001, PER-CUE-002, SOC-GAZE-001 |
| MK.P2_auditory | erp_component | 4 | EMO-SOUND-001, ERR-AAF-001, PER-ACC-001, PER-AEP-001 |
| MK.P2_visual | erp_component | 2 | SOC-RACE-001, SOC-WIT-001 |
| MK.P3a | erp_component | 1 | PER-ODD-002 |
| MK.P3b | erp_component | 35 | CTL-ANT-001, CTL-ANT-002, CTL-CPT-001, CTL-CPT-002, CTL-DT-001, CTL-WCST-001, ERR-ADAPT-002, ERR-CHGPT-001, ERR-CHGPT-002, MEM-CIT-001, MEM-CIT-002, MEM-NBK-001, MEM-NBK-002, PER-AB-001, PER-IB-001, PER-LG-001, PER-MASK-001, PER-NAVON-001, PER-ODD-001, PER-ODD-002, PER-ODD-003, PER-ODD-004, PER-ODD-005, PER-ODD-006, PER-ODD-007, PER-ODD-008, PER-ODD-009, PER-TACT-001, SOC-CYB-001, SOC-NAME-001, SOC-NAME-002, SOC-SELF-001, STA-MW-001, STA-MW-002, STM-TAVNS-001 |
| MK.P50_gating | erp_component | 1 | PER-GATE-001 |
| MK.P600 | erp_component | 4 | LAN-AGL-001, LAN-P600-001, LAN-P600-002, LAN-SC-001 |
| MK.Pd | erp_component | 1 | PER-ADDS-001 |
| MK.Pe | erp_component | 5 | CTL-CONF-001, CTL-FLK-001, CTL-FLK-002, ERR-AWARE-001, ERR-AWARE-002 |
| MK.RREP | erp_component | 1 | PER-RREP-001 |
| MK.SCP | erp_component | 2 | STA-SCP-001, STA-SCP-002 |
| MK.SEP_N20 | erp_component | 3 | STM-PAS-001, STM-SEP-001, STM-TUS-001 |
| MK.SMR_ERD | oscillatory | 39 | IMG-CMD-001, IMG-CMD-002, IMG-SAO-001, IMG-SAO-002, IMG-TACT-001, MOT-ATT-001, MOT-ATT-002, MOT-ATT-003, MOT-BIMAN-001, MOT-CURSOR-001, MOT-CURSOR-002, MOT-FORCE-001, MOT-GRASP-003, MOT-GRASP-004, MOT-ME-001, MOT-ME-002, MOT-ME-003, MOT-ME-005, MOT-MI-001, MOT-MI-002, MOT-MI-003, MOT-MI-004, MOT-MI-005, MOT-MI-006, MOT-MI-007, MOT-MI-008, MOT-MI-009, MOT-MI-010, MOT-MI-011, MOT-MSL-001, MOT-MVF-001, MOT-OBS-001, MOT-PASS-001, MOT-SMS-001, MOT-SRT-001, SOC-IMIT-001, SOC-JA-001, STA-NF-001, STM-PHTMS-001 |
| MK.SPN | erp_component | 1 | PER-SPN-001 |
| MK.SSEP_beat | steady_state | 1 | SSR-BEAT-001 |
| MK.SSEP_nociceptive | steady_state | 1 | SSR-NSSEP-001 |
| MK.SSMVEP | steady_state | 1 | SSR-SSMVEP-001 |
| MK.SSSEP | steady_state | 2 | SSR-SSSEP-001, SSR-SSSEP-002 |
| MK.SSVEP | steady_state | 9 | PER-BR-002, SSR-SSVEP-001, SSR-SSVEP-002, SSR-SSVEP-003, SSR-SSVEP-004, SSR-SSVEP-005, SSR-SSVEP-007, SSR-SSVEP-008, SSR-SWEEP-001 |
| MK.TEP | erp_component | 2 | STM-PAS-001, STM-TEP-001 |
| MK.VAN | erp_component | 3 | PER-CB-001, PER-IB-001, PER-MASK-001 |
| MK.affective_band_power | oscillatory | 5 | EMO-AUTO-001, EMO-FILM-001, EMO-FILM-002, EMO-FILM-003, EMO-FILM-004 |
| MK.alpha_lateralization | oscillatory | 3 | MEM-RC-001, PER-CVA-001, PER-CVA-002 |
| MK.alpha_posterior | oscillatory | 25 | CTL-AUT-001, CTL-RAT-001, CTL-SART-001, IMG-ROT-001, IMG-VIS-001, MEM-DF-001, MEM-DF-002, MEM-DMS-001, MEM-NBK-001, MEM-NBK-002, MEM-SB-001, SOC-VPT-001, STA-DRV-001, STA-DRV-002, STA-ENG-001, STA-MATB-001, STA-MED-001, STA-MW-001, STA-MW-002, STA-NF-001, STA-PSY-001, STA-PVT-001, STA-REST-001, STA-REST-002, STM-PBM-001 |
| MK.cVEP | steady_state | 3 | SSR-CVEP-001, SSR-CVEP-002, SSR-CVEP-003 |
| MK.corticokinematic_coherence | connectivity | 1 | MOT-PASS-001 |
| MK.corticomuscular_coherence | connectivity | 1 | MOT-FORCE-001 |
| MK.flash_VEP | erp_component | 1 | PER-FVEP-001 |
| MK.frontal_alpha_anesthesia | oscillatory | 1 | STA-ANES-001 |
| MK.frontal_alpha_asymmetry | oscillatory | 5 | EMO-FILM-001, EMO-FILM-002, EMO-FILM-003, EMO-FILM-004, EMO-STRESS-001 |
| MK.frontal_midline_theta | oscillatory | 16 | CTL-DT-001, CTL-SW-001, CTL-SW-002, CTL-SW-003, EMO-FC-003, ERR-OGNG-001, ERR-PSEL-001, IMG-MA-001, IMG-MA-002, MEM-DS-001, MEM-DS-002, MEM-NBK-001, MEM-NBK-002, MEM-SB-001, STA-MATB-001, STA-MED-001 |
| MK.gamma_power | oscillatory | 1 | MEM-DMS-001 |
| MK.high_gamma | field_potential | 17 | IMG-AUD-001, IMG-SPI-001, IMG-SPI-002, IMG-SPI-003, LAN-OVS-001, LAN-OVS-002, LAN-OVS-003, LAN-PCAT-001, LAN-PN-001, LAN-SIS-001, MEM-FR-001, MOT-GRASP-001, MOT-GRASP-002, MOT-ME-001, MOT-ME-002, MOT-REACH-001, MOT-TRACK-001 |
| MK.hippocampal_theta | oscillatory | 3 | MEM-NAV-001, MEM-NAV-003, MEM-PA-001 |
| MK.interbrain_synchrony | connectivity | 2 | SOC-EYE-001, SOC-JA-001 |
| MK.interhemispheric_coherence | connectivity | 1 | MOT-BIMAN-001 |
| MK.intermodulation | steady_state | 1 | SSR-IM-001 |
| MK.left_anterior_negativity | erp_component | 1 | LAN-P600-001 |
| MK.linguistic_structure_tracking | steady_state | 2 | LAN-HIER-001, LAN-SL-001 |
| MK.low_freq_kinematics | oscillatory | 8 | MOT-ATT-003, MOT-GRASP-003, MOT-HW-002, MOT-ME-005, MOT-MI-003, MOT-REACH-002, MOT-TRACK-001, MOT-TRACK-002 |
| MK.mVEP | erp_component | 2 | PER-MVEP-001, PER-MVEP-002 |
| MK.motor_cortical_spiking | single_unit | 7 | LAN-OVS-003, MOT-ATT-001, MOT-CURSOR-001, MOT-CURSOR-003, MOT-GRASP-001, MOT-HW-001, MOT-REACH-001 |
| MK.oERN | erp_component | 3 | ERR-OBS-001, ERR-OBS-002, ERR-OBS-003 |
| MK.omission_response | erp_component | 2 | PER-OMIT-001, PER-OMIT-002 |
| MK.oscillatory_entrainment | oscillatory | 2 | SSR-RVS-001, STM-TACS-001 |
| MK.parietal_old_new | erp_component | 3 | MEM-DRM-001, MEM-ON-001, MEM-ON-002 |
| MK.perturbation_N1 | erp_component | 1 | MOT-PERT-001 |
| MK.presaccadic_potential | erp_component | 2 | CTL-AS-001, MOT-SACC-001 |
| MK.rIFG_beta | oscillatory | 1 | CTL-SST-001 |
| MK.right_frontal_old_new | erp_component | 1 | MEM-SRC-001 |
| MK.sleep_spindle | oscillatory | 4 | MEM-TMR-001, STA-CLAS-001, STA-SLP-001, STA-SLP-002 |
| MK.slow_wave | oscillatory | 6 | MEM-TMR-001, STA-ANES-001, STA-CLAS-001, STA-DREAM-001, STA-SLP-001, STA-SLP-002 |
| MK.speech_envelope_tracking | oscillatory | 2 | LAN-NAT-001, PER-AAD-001 |
| MK.subthalamic_beta | oscillatory | 1 | STM-ADBS-001 |
| MK.switch_positivity | erp_component | 2 | CTL-SW-001, CTL-SW-002 |
| MK.tES_power_aftereffect | oscillatory | 2 | STM-TACS-001, STM-TDCS-001 |
| MK.theta_drowsiness | oscillatory | 3 | STA-DRV-001, STA-DRV-002, STA-PVT-001 |
| MK.vMMN | erp_component | 1 | PER-VMMN-001 |

## 6. 零覆盖空白

下表中的 · 表示该组合目前没有任何范式。并非每个空格都是缺口（例如 PET × 稳态响应在方法上不适用），但它们是第二遍和新候选检索的检查清单。

### 6.1 记录模态 × 族

|  | perception | motor | steady_state | error | language | memory | emotion | control | imagery | social | state | stimulation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EEG | 60 | 47 | 24 | 27 | 27 | 33 | 21 | 31 | 14 | 19 | 19 | 12 |
| MEG | 29 | 12 | 6 | · | 7 | 3 | 1 | 1 | · | · | 3 | 2 |
| fNIRS | · | 3 | · | · | 4 | 2 | 1 | 2 | 3 | 3 | 5 | 1 |
| fMRI | 14 | 13 | · | 11 | 15 | 32 | 19 | 33 | 8 | 24 | 6 | 7 |
| ECoG | 3 | 9 | · | · | 9 | · | · | · | 2 | · | · | 1 |
| sEEG | · | · | · | · | · | 4 | · | · | 1 | · | · | 1 |
| intracortical | · | 8 | · | · | 1 | · | · | 1 | 1 | · | · | · |
| fUS | · | · | · | · | · | · | · | · | · | · | · | · |
| PET | · | · | · | · | · | · | · | 1 | 3 | 1 | · | · |
| other | · | · | · | · | · | · | · | · | · | · | · | 2 |

（· = 0）

### 6.2 刺激模态 × 族

|  | perception | motor | steady_state | error | language | memory | emotion | control | imagery | social | state | stimulation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| visual | 38 | 44 | 15 | 30 | 27 | 42 | 22 | 40 | 10 | 29 | 10 | 1 |
| auditory | 22 | 9 | 6 | 2 | 20 | 17 | 9 | 6 | 8 | 4 | 5 | · |
| somatosensory | 5 | 3 | 3 | 1 | · | · | 1 | · | 2 | · | · | 3 |
| olfactory | 1 | · | · | · | · | 1 | · | · | 1 | · | · | · |
| gustatory | 1 | · | · | 1 | · | · | · | · | · | · | · | · |
| electrical_stimulation | · | 2 | · | · | · | · | 4 | · | · | · | · | 11 |
| magnetic_stimulation | · | · | · | · | · | · | · | · | · | · | · | 4 |
| ultrasound_stimulation | · | · | · | · | · | · | · | · | · | · | · | 1 |
| motor_execution | · | 37 | · | 5 | 8 | · | · | 1 | · | 2 | 4 | · |
| mental_imagery | · | 15 | · | · | · | · | 1 | · | 15 | · | · | · |
| cognitive_task | 2 | · | · | · | 3 | 1 | 3 | 2 | 2 | · | 7 | · |
| resting_state | · | · | · | · | · | · | · | · | · | · | 6 | · |
| naturalistic | 1 | · | · | · | 2 | 1 | 4 | · | · | · | 1 | · |
| optical_stimulation | · | · | · | · | · | · | · | · | · | · | · | 1 |
| pharmacological | · | · | · | · | · | · | · | · | · | · | 2 | · |

（· = 0）

### 6.3 BCI 类别 × 族

|  | perception | motor | steady_state | error | language | memory | emotion | control | imagery | social | state | stimulation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| active | 1 | 36 | · | · | 4 | · | · | · | 14 | · | 4 | · |
| reactive | 13 | · | 10 | 1 | · | · | · | · | · | 2 | · | · |
| passive | 5 | · | · | 7 | · | 3 | 7 | · | · | · | 13 | 2 |
| none | 54 | 23 | 14 | 24 | 34 | 43 | 25 | 42 | 6 | 30 | 11 | 14 |

（· = 0）

### 6.4 标记物类型 × 族（按范式–标记物关联）

|  | perception | motor | steady_state | error | language | memory | emotion | control | imagery | social | state | stimulation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| erp_component | 65 | 10 | · | 30 | 24 | 21 | 17 | 38 | · | 19 | 4 | 8 |
| oscillatory | 3 | 38 | 1 | 2 | 1 | 18 | 11 | 8 | 9 | 3 | 27 | 6 |
| steady_state | 1 | · | 23 | · | 2 | · | · | · | · | · | · | · |
| hemodynamic | 12 | 10 | · | 9 | 13 | 31 | 16 | 22 | 12 | 26 | 3 | 6 |
| single_unit | · | 6 | · | · | 1 | · | · | · | · | · | · | · |
| field_potential | · | 6 | · | · | 6 | 1 | · | · | 4 | · | · | 1 |
| connectivity | 1 | 3 | · | · | · | · | · | 1 | · | 2 | 5 | · |

（· = 0）

### 6.5 汇总

| 交叉表 | 零格数 | 总格数 |
|---|---|---|
| 记录模态 × 族 | 63 | 120 |
| 刺激模态 × 族 | 116 | 180 |
| BCI 类别 × 族 | 21 | 48 |
| 标记物类型 × 族 | 36 | 84 |

没有任何范式使用的词表取值：recording_modality: fUS

没有任何 BCI 用途（active / reactive / passive）范式的族：control

## 7. 范式类与具体范式（D-057）

范式类 `<族>-<简称>` 记录共同机制，具体范式 `<族>-<简称>-<序号>` 是一个可复现的任务配置（类别集、提示/编码、试次结构、反馈任一不同即另取序号）。schema 0.2 迁移时每个 schema 0.1 文件生成一个范式类，因此迁移刚完成时两者一一对应；sprint 2 的拆分会使比值上升。

### 7.1 按族

| 族 | 范式类 | 具体范式 | 具体范式 / 类 | ≥2 个具体范式的类 | 有 protocol |
|---|---|---|---|---|---|
| perception | 46 | 64 | 1.39 | 10 | 64 |
| motor | 24 | 51 | 2.12 | 10 | 51 |
| steady_state | 13 | 24 | 1.85 | 5 | 24 |
| error | 19 | 31 | 1.63 | 7 | 31 |
| language | 25 | 38 | 1.52 | 11 | 38 |
| memory | 28 | 45 | 1.61 | 13 | 45 |
| emotion | 16 | 25 | 1.56 | 6 | 25 |
| control | 33 | 42 | 1.27 | 7 | 42 |
| imagery | 9 | 17 | 1.89 | 6 | 17 |
| social | 23 | 30 | 1.30 | 6 | 30 |
| state | 15 | 21 | 1.40 | 6 | 21 |
| stimulation | 16 | 16 | 1.00 | 0 | 16 |

### 7.2 按工作包

| 包 | 范式类 | 具体范式 | 具体范式 / 类 | ≥2 个具体范式的类 | 有 protocol |
|---|---|---|---|---|---|
| A | 59 | 88 | 1.49 | 15 | 88 |
| B | 49 | 84 | 1.71 | 16 | 84 |
| C | 52 | 73 | 1.40 | 14 | 73 |
| D | 53 | 83 | 1.57 | 24 | 83 |
| E | 54 | 76 | 1.41 | 18 | 76 |

### 7.3 每个范式类的具体范式数

| 具体范式数 | 范式类数 |
|---|---|
| 1 | 180 |
| 2 | 61 |
| 3 | 18 |
| 4 | 4 |
| 5 | 1 |
| 7 | 1 |
| 9 | 1 |
| 11 | 1 |

### 7.4 每个范式类中已写 `protocol` 的具体范式数

| 有 protocol 的具体范式数 | 范式类数 |
|---|---|
| 1 | 180 |
| 2 | 61 |
| 3 | 18 |
| 4 | 4 |
| 5 | 1 |
| 7 | 1 |
| 9 | 1 |
| 11 | 1 |

### 7.5 有多个具体范式的范式类

| 范式类 | 具体范式数 | 具体范式 |
|---|---|---|
| MOT-MI | 11 | MOT-MI-001, MOT-MI-002, MOT-MI-003, MOT-MI-004, MOT-MI-005, MOT-MI-006, MOT-MI-007, MOT-MI-008, MOT-MI-009, MOT-MI-010, MOT-MI-011 |
| PER-ODD | 9 | PER-ODD-001, PER-ODD-002, PER-ODD-003, PER-ODD-004, PER-ODD-005, PER-ODD-006, PER-ODD-007, PER-ODD-008, PER-ODD-009 |
| SSR-SSVEP | 7 | SSR-SSVEP-001, SSR-SSVEP-002, SSR-SSVEP-003, SSR-SSVEP-004, SSR-SSVEP-005, SSR-SSVEP-007, SSR-SSVEP-008 |
| MOT-ME | 5 | MOT-ME-001, MOT-ME-002, MOT-ME-003, MOT-ME-004, MOT-ME-005 |
| EMO-FILM | 4 | EMO-FILM-001, EMO-FILM-002, EMO-FILM-003, EMO-FILM-004 |
| ERR-ERRP | 4 | ERR-ERRP-001, ERR-ERRP-002, ERR-ERRP-003, ERR-ERRP-004 |
| MEM-NBK | 4 | MEM-NBK-001, MEM-NBK-002, MEM-NBK-003, MEM-NBK-004 |
| MOT-GRASP | 4 | MOT-GRASP-001, MOT-GRASP-002, MOT-GRASP-003, MOT-GRASP-004 |
| CTL-CPT | 3 | CTL-CPT-001, CTL-CPT-002, CTL-CPT-003 |
| CTL-SW | 3 | CTL-SW-001, CTL-SW-002, CTL-SW-003 |
| EMO-FC | 3 | EMO-FC-001, EMO-FC-002, EMO-FC-003 |
| ERR-AWARE | 3 | ERR-AWARE-001, ERR-AWARE-002, ERR-AWARE-003 |
| ERR-GAM | 3 | ERR-GAM-001, ERR-GAM-002, ERR-GAM-003 |
| ERR-OBS | 3 | ERR-OBS-001, ERR-OBS-002, ERR-OBS-003 |
| IMG-CMD | 3 | IMG-CMD-001, IMG-CMD-002, IMG-CMD-003 |
| IMG-SPI | 3 | IMG-SPI-001, IMG-SPI-002, IMG-SPI-003 |
| LAN-OVS | 3 | LAN-OVS-001, LAN-OVS-002, LAN-OVS-003 |
| LAN-VF | 3 | LAN-VF-001, LAN-VF-002, LAN-VF-003 |
| MEM-CD | 3 | MEM-CD-001, MEM-CD-002, MEM-CD-003 |
| MEM-NAV | 3 | MEM-NAV-001, MEM-NAV-002, MEM-NAV-003 |
| MOT-ATT | 3 | MOT-ATT-001, MOT-ATT-002, MOT-ATT-003 |
| MOT-CURSOR | 3 | MOT-CURSOR-001, MOT-CURSOR-002, MOT-CURSOR-003 |
| MOT-MRCP | 3 | MOT-MRCP-001, MOT-MRCP-002, MOT-MRCP-003 |
| PER-MMN | 3 | PER-MMN-001, PER-MMN-002, PER-MMN-003 |
| SOC-TRUST | 3 | SOC-TRUST-001, SOC-TRUST-002, SOC-TRUST-003 |
| SSR-CVEP | 3 | SSR-CVEP-001, SSR-CVEP-002, SSR-CVEP-003 |
| CTL-ANT | 2 | CTL-ANT-001, CTL-ANT-002 |
| CTL-FLK | 2 | CTL-FLK-001, CTL-FLK-002 |
| CTL-PDM | 2 | CTL-PDM-001, CTL-PDM-002 |
| CTL-SIM | 2 | CTL-SIM-001, CTL-SIM-002 |
| CTL-STR | 2 | CTL-STR-001, CTL-STR-002 |
| EMO-FACE | 2 | EMO-FACE-001, EMO-FACE-002 |
| EMO-MID | 2 | EMO-MID-001, EMO-MID-002 |
| EMO-REG | 2 | EMO-REG-001, EMO-REG-002 |
| EMO-STRESS | 2 | EMO-STRESS-001, EMO-STRESS-002 |
| ERR-ADAPT | 2 | ERR-ADAPT-001, ERR-ADAPT-002 |
| ERR-CHGPT | 2 | ERR-CHGPT-001, ERR-CHGPT-002 |
| ERR-TS | 2 | ERR-TS-001, ERR-TS-002 |
| IMG-AUD | 2 | IMG-AUD-001, IMG-AUD-002 |
| IMG-MA | 2 | IMG-MA-001, IMG-MA-002 |
| IMG-SAO | 2 | IMG-SAO-001, IMG-SAO-002 |
| IMG-VIS | 2 | IMG-VIS-001, IMG-VIS-002 |
| LAN-CPS | 2 | LAN-CPS-001, LAN-CPS-002 |
| LAN-LOC | 2 | LAN-LOC-001, LAN-LOC-002 |
| LAN-N400 | 2 | LAN-N400-001, LAN-N400-002 |
| LAN-P600 | 2 | LAN-P600-001, LAN-P600-002 |
| LAN-PN | 2 | LAN-PN-001, LAN-PN-002 |
| LAN-PRIME | 2 | LAN-PRIME-001, LAN-PRIME-002 |
| LAN-SC | 2 | LAN-SC-001, LAN-SC-002 |
| LAN-SIS | 2 | LAN-SIS-001, LAN-SIS-002 |
| LAN-SWITCH | 2 | LAN-SWITCH-001, LAN-SWITCH-002 |
| MEM-CIT | 2 | MEM-CIT-001, MEM-CIT-002 |
| MEM-DF | 2 | MEM-DF-001, MEM-DF-002 |
| MEM-DS | 2 | MEM-DS-001, MEM-DS-002 |
| MEM-FR | 2 | MEM-FR-001, MEM-FR-002 |
| MEM-META | 2 | MEM-META-001, MEM-META-002 |
| MEM-MST | 2 | MEM-MST-001, MEM-MST-002 |
| MEM-ON | 2 | MEM-ON-001, MEM-ON-002 |
| MEM-PA | 2 | MEM-PA-001, MEM-PA-002 |
| MEM-PM | 2 | MEM-PM-001, MEM-PM-002 |
| MEM-TMR | 2 | MEM-TMR-001, MEM-TMR-002 |
| MOT-HW | 2 | MOT-HW-001, MOT-HW-002 |
| MOT-REACH | 2 | MOT-REACH-001, MOT-REACH-002 |
| MOT-SACC | 2 | MOT-SACC-001, MOT-SACC-002 |
| MOT-TRACK | 2 | MOT-TRACK-001, MOT-TRACK-002 |
| PER-BR | 2 | PER-BR-001, PER-BR-002 |
| PER-CUE | 2 | PER-CUE-001, PER-CUE-002 |
| PER-CVA | 2 | PER-CVA-001, PER-CVA-002 |
| PER-HBD | 2 | PER-HBD-001, PER-HBD-002 |
| PER-MSI | 2 | PER-MSI-001, PER-MSI-002 |
| PER-MVEP | 2 | PER-MVEP-001, PER-MVEP-002 |
| PER-OMIT | 2 | PER-OMIT-001, PER-OMIT-002 |
| PER-RET | 2 | PER-RET-001, PER-RET-002 |
| SOC-DICT | 2 | SOC-DICT-001, SOC-DICT-002 |
| SOC-GAZE | 2 | SOC-GAZE-001, SOC-GAZE-002 |
| SOC-NAME | 2 | SOC-NAME-001, SOC-NAME-002 |
| SOC-PAIN | 2 | SOC-PAIN-001, SOC-PAIN-002 |
| SOC-TOM | 2 | SOC-TOM-001, SOC-TOM-002 |
| SSR-ASSR | 2 | SSR-ASSR-001, SSR-ASSR-002 |
| SSR-FFR | 2 | SSR-FFR-001, SSR-FFR-002 |
| SSR-SSSEP | 2 | SSR-SSSEP-001, SSR-SSSEP-002 |
| STA-DRV | 2 | STA-DRV-001, STA-DRV-002 |
| STA-MW | 2 | STA-MW-001, STA-MW-002 |
| STA-NF | 2 | STA-NF-001, STA-NF-002 |
| STA-REST | 2 | STA-REST-001, STA-REST-002 |
| STA-SCP | 2 | STA-SCP-001, STA-SCP-002 |
| STA-SLP | 2 | STA-SLP-001, STA-SLP-002 |

## 8. 具体范式的 `protocol` 字段

### 8.1 试次结构（paradigm_timing）

| 取值 | 范式数 | 占比 |
|---|---|---|
| synchronous（同步） | 284 | 70.3% |
| asynchronous（异步） | 10 | 2.5% |
| block（组块） | 69 | 17.1% |
| continuous（连续） | 38 | 9.4% |
| （未填） | 3 | 0.7% |

### 8.2 反馈方式（feedback）

| 取值 | 范式数 | 占比 |
|---|---|---|
| none（无/开环） | 310 | 76.7% |
| discrete（离散） | 64 | 15.8% |
| continuous（连续） | 18 | 4.5% |
| （未填） | 12 | 3.0% |

### 8.3 工作包 × 反馈方式 / 试次结构

| 包 | none | discrete | continuous | （未填） | synchronous | asynchronous | block | continuous | （未填） |
|---|---|---|---|---|---|---|---|---|---|
| A | 71 | 17 | 0 | 0 | 63 | 2 | 10 | 13 | 0 |
| B | 69 | 5 | 9 | 1 | 46 | 7 | 23 | 8 | 0 |
| C | 32 | 27 | 3 | 11 | 64 | 0 | 3 | 3 | 3 |
| D | 77 | 4 | 2 | 0 | 66 | 0 | 12 | 5 | 0 |
| E | 61 | 11 | 4 | 0 | 45 | 1 | 21 | 9 | 0 |

### 8.4 类别/条件数（n_classes）

| 取值 | 范式数 | 占比 |
|---|---|---|
| 1（类/条件） | 54 | 13.4% |
| 2（类/条件） | 229 | 56.7% |
| 3（类/条件） | 53 | 13.1% |
| 4（类/条件） | 19 | 4.7% |
| 5（类/条件） | 5 | 1.2% |
| 6（类/条件） | 3 | 0.7% |
| 7–12（类/条件） | 8 | 2.0% |
| >12（类/条件） | 0 | 0.0% |
| （未填）（未写 n_classes） | 33 | 8.2% |

### 8.5 字段填写率

`stimulus_coding` 只在有编码方案时填写（如 SSVEP、c-VEP、P300 拼写器），未填不算缺项。

| 字段 | 已填 | 未填 | 未填的具体范式（最多 15 个） |
|---|---|---|---|
| n_classes | 371 | 33 | CTL-RAT-001, CTL-RAVEN-001, CTL-TOL-001, CTL-VBC-001, CTL-WASON-001, EMO-FC-002, EMO-FILM-001, EMO-FILM-002, ERR-CAUS-001, IMG-CMD-002, IMG-SPI-001, MOT-ATT-002, MOT-CURSOR-002, MOT-GRASP-001, MOT-GRASP-004 |
| classes | 395 | 9 | CTL-RAT-001, CTL-RAVEN-001, CTL-TOL-001, CTL-VBC-001, CTL-WASON-001, ERR-CAUS-001, IMG-MA-002, IMG-SPI-002, MOT-MI-011 |
| cue | 403 | 1 | MOT-GRASP-004 |
| stimulus_coding | 73 | 331 | — |
| paradigm_timing | 401 | 3 | CTL-RAVEN-001, CTL-TOL-001, CTL-WASON-001 |
| feedback | 392 | 12 | CTL-AMBIG-001, CTL-ANAL-001, CTL-AUT-001, CTL-DD-001, CTL-MIXG-001, CTL-RAT-001, CTL-RAVEN-001, CTL-SYLL-001, CTL-TOL-001, CTL-VBC-001, CTL-WASON-001, MOT-FORCE-001 |
| distinguishing | 404 | 0 |  |

### 8.6 具体范式最多的范式类（前 15）

| 范式类 | 名称 | 包 | 具体范式数 | TBD 源头 | 反馈方式 |
|---|---|---|---|---|---|
| MOT-MI | 提示性运动想象 | B | 11 | 3 | continuous/none |
| PER-ODD | Oddball 范式（怪球范式） | A | 9 | 0 | discrete/none |
| SSR-SSVEP | 稳态视觉诱发电位范式 | A | 7 | 1 | discrete/none |
| MOT-ME | 运动执行 | B | 5 | 1 | none |
| EMO-FILM | 自然刺激情绪诱发（影片、音乐、音乐视频） | E | 4 | 1 | none |
| ERR-ERRP | 交互式错误电位 | C | 4 | 1 | continuous/discrete |
| MEM-NBK | n-back | D | 4 | 1 | discrete/none |
| MOT-GRASP | 抓握与手势 | B | 4 | 0 | none |
| CTL-CPT | 持续操作任务 | C | 3 | 0 | none |
| CTL-SW | 任务切换 | C | 3 | 1 | none |
| EMO-FC | 巴甫洛夫恐惧条件化 | E | 3 | 0 | none |
| ERR-AWARE | 错误觉知 | C | 3 | 0 | none |
| ERR-GAM | 赌博与奖赏反馈 | C | 3 | 1 | discrete |
| ERR-OBS | 观察性错误 | C | 3 | 0 | none |
| IMG-CMD | 指令跟随想象（意识评估） | B | 3 | 0 | none |

### 8.7 TBD 源头

具体范式 first_source 为 TBD：64 个；范式类 first_source 为 TBD：36 个。

| 包 | 具体范式 | TBD | 占比 |
|---|---|---|---|
| A | 88 | 32 | 36.4% |
| B | 84 | 5 | 6.0% |
| C | 73 | 7 | 9.6% |
| D | 83 | 16 | 19.3% |
| E | 76 | 4 | 5.3% |
