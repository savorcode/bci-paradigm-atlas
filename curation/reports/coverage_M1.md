# 覆盖度报告 里程碑 M1

> 由 `scripts/coverage_report.py` 生成（2026-10-03），数据来自 `paradigms/`、`knowledge/markers/`、`taxonomy/` 与 `curation/candidates.csv`（包归属）。请勿手工修改本文件，重新运行脚本即可。

## 1. 总数

| 项目 | 数量 |
|---|---|
| 范式文件 | 267 |
| 标记物文件 | 129 |
| 范式–标记物关联（elicits） | 417 |
| 每个范式的平均标记物数 | 1.56 |
| 变体 | 35 |
| first_source 为 TBD 的范式 | 37（13.9%） |
| 出处已核实（verified: true）的 first_source | 0 |
| status: reviewed 的范式 | 0 |
| 未被任何范式使用的标记物 | 0 |

## 2. 分布

### 2.1 范式族

| 取值 | 范式数 | 占比 |
|---|---|---|
| perception（感知与注意） | 46 | 17.2% |
| motor（运动执行与想象） | 24 | 9.0% |
| steady_state（稳态响应） | 13 | 4.9% |
| error（错误监测与反馈） | 19 | 7.1% |
| language（语言） | 25 | 9.4% |
| memory（记忆） | 28 | 10.5% |
| emotion（情绪与情感） | 16 | 6.0% |
| control（认知控制） | 33 | 12.4% |
| imagery（非运动想象） | 9 | 3.4% |
| social（社会认知） | 23 | 8.6% |
| state（脑状态（静息、睡眠、警觉）） | 15 | 5.6% |
| stimulation（刺激诱发） | 16 | 6.0% |

### 2.2 工作包

| 取值 | 范式数 | 占比 |
|---|---|---|
| A（包 A） | 59 | 22.1% |
| B（包 B） | 49 | 18.4% |
| C（包 C） | 52 | 19.5% |
| D（包 D） | 53 | 19.9% |
| E（包 E） | 54 | 20.2% |

### 2.3 记录模态

一个范式可有多个记录模态，占比按范式数计算，合计可超过 100%。

| 取值 | 范式数 | 占比 |
|---|---|---|
| EEG（脑电图） | 226 | 84.6% |
| MEG（脑磁图） | 52 | 19.5% |
| fNIRS（功能近红外光谱） | 19 | 7.1% |
| fMRI（功能磁共振成像） | 139 | 52.1% |
| ECoG（皮层脑电） | 19 | 7.1% |
| sEEG（立体定向脑电） | 5 | 1.9% |
| intracortical（皮层内微电极记录） | 9 | 3.4% |
| fUS（功能超声） | 0 | 0.0% |
| PET（正电子发射断层成像） | 4 | 1.5% |
| other（其他） | 2 | 0.7% |

### 2.4 刺激模态

一个范式可有多个刺激模态。

| 取值 | 范式数 | 占比 |
|---|---|---|
| visual（视觉） | 196 | 73.4% |
| auditory（听觉） | 80 | 30.0% |
| somatosensory（体感 / 触觉） | 16 | 6.0% |
| olfactory（嗅觉） | 3 | 1.1% |
| gustatory（味觉） | 2 | 0.7% |
| electrical_stimulation（电刺激） | 13 | 4.9% |
| magnetic_stimulation（磁刺激） | 4 | 1.5% |
| ultrasound_stimulation（超声刺激） | 1 | 0.4% |
| motor_execution（运动执行） | 34 | 12.7% |
| mental_imagery（心理想象（运动、视觉、听觉、言语）） | 10 | 3.7% |
| cognitive_task（无外部刺激的认知任务） | 12 | 4.5% |
| resting_state（静息态） | 4 | 1.5% |
| naturalistic（自然场景（影片、叙事、游戏）） | 6 | 2.2% |
| optical_stimulation（组织光刺激（经颅光生物调节；不含视觉光刺激）） | 1 | 0.4% |
| pharmacological（药物给予（麻醉药、精神活性药物）） | 2 | 0.7% |

### 2.5 BCI 类别

| 取值 | 范式数 | 占比 |
|---|---|---|
| active（主动） | 23 | 8.6% |
| reactive（反应式） | 12 | 4.5% |
| passive（被动） | 22 | 8.2% |
| none（非 BCI） | 235 | 88.0% |

### 2.6 标记物类型

| 类型 | 标记物数 | 范式–标记物关联数 |
|---|---|---|
| erp_component（事件相关电位 / 磁场成分） | 64 | 175 |
| oscillatory（节律调制（ERD/ERS、功率、相位）） | 18 | 78 |
| steady_state（稳态诱发响应） | 12 | 15 |
| hemodynamic（血流动力学响应（BOLD、HbO/HbR）） | 26 | 120 |
| single_unit（单 / 多神经元放电） | 1 | 6 |
| field_potential（局部场电位或高 gamma 活动） | 2 | 12 |
| connectivity（功能连接模式） | 6 | 11 |

### 2.7 包 × 族

| 包 | 族 | 范式数 | TBD |
|---|---|---|---|
| A | perception | 46 | 22 |
| A | steady_state | 13 | 5 |
| B | imagery | 9 | 0 |
| B | motor | 24 | 0 |
| B | stimulation | 16 | 0 |
| C | control | 33 | 0 |
| C | error | 19 | 1 |
| D | language | 25 | 3 |
| D | memory | 28 | 4 |
| E | emotion | 16 | 1 |
| E | social | 23 | 0 |
| E | state | 15 | 1 |

## 3. first_source 为 TBD 的范式

共 37 个。

| 包 | ID | 名称 | 族 |
|---|---|---|---|
| A | PER-ABR-001 | 听觉脑干反应 | perception |
| A | PER-ACC-001 | 声学变化复合波 | perception |
| A | PER-ADDS-001 | 附加单例与干扰抑制 | perception |
| A | PER-AEP-001 | 听觉诱发电位（纯音/短声） | perception |
| A | PER-AMASK-001 | 听觉掩蔽 | perception |
| A | PER-BR-001 | 双眼竞争与双稳态知觉 | perception |
| A | PER-CB-001 | 变化盲 | perception |
| A | PER-FVEP-001 | 闪光视觉诱发电位 | perception |
| A | PER-GATE-001 | 配对短声感觉门控 | perception |
| A | PER-GEP-001 | 味觉诱发电位 | perception |
| A | PER-IB-001 | 非注意盲 | perception |
| A | PER-IC-001 | 错觉轮廓知觉 | perception |
| A | PER-MLR-001 | 听觉中潜伏期反应 | perception |
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
| A | SSR-FPVS-001 | 快速周期视觉刺激（频率标记） | steady_state |
| A | SSR-RVS-001 | 节律性视觉刺激（α 夹带） | steady_state |
| A | SSR-SSSEP-001 | 稳态体感诱发电位 | steady_state |
| A | SSR-SWEEP-001 | 扫描 VEP（视敏度评估） | steady_state |
| C | ERR-AAF-001 | 音高偏移听觉反馈（言语运动误差） | error |
| D | LAN-GEST-001 | 言语—手势整合 | language |
| D | LAN-NWL-001 | 新词学习 | language |
| D | LAN-SWITCH-001 | 双语语言切换 | language |
| D | MEM-PA-001 | 配对联想学习 | memory |
| D | MEM-RMEM-001 | 奖赏驱动的记忆编码 | memory |
| D | MEM-RPRIM-001 | 重复启动（内隐记忆） | memory |
| D | MEM-RPT-001 | 近期探测任务（前摄干扰） | memory |
| E | EMO-EST-001 | 情绪 Stroop | emotion |
| E | STA-NF-001 | 神经反馈训练 | state |

## 4. 被 ≥3 个范式使用的标记物

共 51 个。

| 标记物 | 类型 | 范式数 | 涉及族数 | 范式 |
|---|---|---|---|---|
| MK.alpha_posterior | oscillatory | 20 | 6 | CTL-AUT-001, CTL-RAT-001, CTL-SART-001, IMG-ROT-001, IMG-VIS-001, MEM-DF-001, MEM-DMS-001, MEM-NBK-001, MEM-SB-001, SOC-VPT-001, STA-DRV-001, STA-ENG-001, STA-MATB-001, STA-MED-001, STA-MW-001, STA-NF-001, STA-PSY-001, STA-PVT-001, STA-REST-001, STM-PBM-001 |
| MK.P3b | erp_component | 19 | 7 | CTL-ANT-001, CTL-CPT-001, CTL-DT-001, CTL-WCST-001, ERR-CHGPT-001, MEM-CIT-001, MEM-NBK-001, PER-AB-001, PER-IB-001, PER-LG-001, PER-MASK-001, PER-NAVON-001, PER-ODD-001, PER-TACT-001, SOC-CYB-001, SOC-NAME-001, SOC-SELF-001, STA-MW-001, STM-TAVNS-001 |
| MK.SMR_ERD | oscillatory | 19 | 5 | IMG-CMD-001, IMG-SAO-001, IMG-TACT-001, MOT-ATT-001, MOT-BIMAN-001, MOT-CURSOR-001, MOT-FORCE-001, MOT-ME-001, MOT-MI-001, MOT-MSL-001, MOT-MVF-001, MOT-OBS-001, MOT-PASS-001, MOT-SMS-001, MOT-SRT-001, SOC-IMIT-001, SOC-JA-001, STA-NF-001, STM-PHTMS-001 |
| MK.FRN | erp_component | 14 | 4 | CTL-BART-001, CTL-IGT-001, EMO-MID-001, ERR-ADAPT-001, ERR-BANDIT-001, ERR-GAM-001, ERR-INST-001, ERR-PRL-001, ERR-PRT-001, ERR-PSEL-001, ERR-TE-001, ERR-TS-001, SOC-TRUST-001, SOC-UG-001 |
| MK.BOLD_striatum_reward | hemodynamic | 13 | 5 | CTL-AMBIG-001, CTL-DD-001, CTL-MIXG-001, EMO-HUMOR-001, EMO-MID-001, ERR-APC-001, ERR-INST-001, ERR-PCL-001, ERR-PRL-001, ERR-TS-001, MEM-RMEM-001, SOC-CONF-001, SOC-TRUST-001 |
| MK.high_gamma | field_potential | 11 | 4 | IMG-AUD-001, IMG-SPI-001, LAN-OVS-001, LAN-PCAT-001, LAN-PN-001, LAN-SIS-001, MEM-FR-001, MOT-GRASP-001, MOT-ME-001, MOT-REACH-001, MOT-TRACK-001 |
| MK.frontal_midline_theta | oscillatory | 10 | 5 | CTL-DT-001, CTL-SW-001, ERR-OGNG-001, ERR-PSEL-001, IMG-MA-001, MEM-DS-001, MEM-NBK-001, MEM-SB-001, STA-MATB-001, STA-MED-001 |
| MK.N170 | erp_component | 9 | 5 | EMO-FACE-001, LAN-VWFA-001, MEM-CFMT-001, PER-BODY-001, PER-CAT-001, PER-FACE-001, SOC-BIO-001, SOC-GAZE-001, SOC-SELF-001 |
| MK.N400 | erp_component | 9 | 4 | EMO-APRIME-001, LAN-GEST-001, LAN-LDT-001, LAN-N400-001, LAN-NWL-001, LAN-PRIME-001, LAN-SC-001, MEM-RPRIM-001, SOC-IAT-001 |
| MK.BOLD_category_selective | hemodynamic | 8 | 4 | IMG-VIS-001, LAN-VWFA-001, MEM-CFMT-001, MEM-RIF-001, MEM-RPRIM-001, PER-BODY-001, PER-CAT-001, PER-FACE-001 |
| MK.BOLD_dlPFC | hemodynamic | 8 | 4 | CTL-BART-001, CTL-RNG-001, CTL-TOL-001, CTL-WASON-001, CTL-WCST-001, ERR-CAUS-001, MEM-DF-001, SOC-TPP-001 |
| MK.BOLD_hippocampus | hemodynamic | 8 | 2 | MEM-EFT-001, MEM-MST-001, MEM-NAV-001, MEM-PA-001, MEM-RMEM-001, MEM-SME-001, MEM-TNT-001, PER-CTXC-001 |
| MK.LPP | erp_component | 8 | 2 | EMO-APRIME-001, EMO-EST-001, EMO-IAPS-001, EMO-REG-001, EMO-SOUND-001, EMO-WORD-001, SOC-IAT-001, SOC-PAIN-001 |
| MK.BOLD_dACC | hemodynamic | 7 | 3 | CTL-EFF-001, CTL-FORAGE-001, CTL-MSIT-001, SOC-CONF-001, SOC-CYB-001, SOC-SFB-001, STA-HYPN-001 |
| MK.HbO_prefrontal | hemodynamic | 7 | 6 | CTL-TOL-001, CTL-WCST-001, EMO-STRESS-001, IMG-MA-001, LAN-VF-001, MEM-NBK-001, STA-MATB-001 |
| MK.N1_auditory | erp_component | 7 | 4 | ERR-AAF-001, LAN-SIS-001, MOT-IB-001, PER-AAD-001, PER-ACC-001, PER-AEP-001, PER-AMASK-001 |
| MK.N2_frontocentral | erp_component | 7 | 5 | CTL-FLK-001, CTL-GNG-001, CTL-SIM-001, EMO-EST-001, LAN-SWITCH-001, MEM-TNT-001, SOC-WIT-001 |
| MK.BOLD_amygdala | hemodynamic | 6 | 2 | CTL-AMBIG-001, EMO-AUTO-001, EMO-FACE-001, EMO-FC-001, EMO-IAPS-001, EMO-THREAT-001 |
| MK.BOLD_frontoparietal | hemodynamic | 6 | 4 | CTL-RAVEN-001, CTL-SYLL-001, IMG-ROT-001, MEM-NBK-001, MEM-SWM-001, PER-MOT-001 |
| MK.BOLD_language_network | hemodynamic | 6 | 1 | LAN-LOC-001, LAN-PHA-001, LAN-PN-001, LAN-SC-001, LAN-SEMD-001, LAN-VG-001 |
| MK.BOLD_motor_network | hemodynamic | 6 | 3 | IMG-CMD-001, MOT-ME-001, MOT-MIRR-001, MOT-MSL-001, MOT-SMS-001, STM-VIB-001 |
| MK.motor_cortical_spiking | single_unit | 6 | 2 | LAN-OVS-001, MOT-ATT-001, MOT-CURSOR-001, MOT-GRASP-001, MOT-HW-001, MOT-REACH-001 |
| MK.BOLD_TPJ | hemodynamic | 5 | 1 | SOC-ANIM-001, SOC-IMIT-001, SOC-RME-001, SOC-TOM-001, SOC-VPT-001 |
| MK.BOLD_mPFC | hemodynamic | 5 | 2 | MEM-EFT-001, MEM-SRE-001, SOC-ANIM-001, SOC-MORAL-001, SOC-RME-001 |
| MK.BOLD_vmPFC_value | hemodynamic | 5 | 2 | CTL-DD-001, CTL-IGT-001, CTL-MIXG-001, CTL-VBC-001, SOC-DICT-001 |
| MK.MMN | erp_component | 5 | 2 | LAN-PHA-001, PER-AMASK-001, PER-LG-001, PER-MMN-001, PER-STREAM-001 |
| MK.slow_wave | oscillatory | 5 | 2 | MEM-TMR-001, STA-ANES-001, STA-CLAS-001, STA-DREAM-001, STA-SLP-001 |
| MK.BOLD_frontopolar | hemodynamic | 4 | 3 | CTL-ANAL-001, ERR-BANDIT-001, MEM-META-001, MEM-PM-001 |
| MK.BOLD_stimulated_region | hemodynamic | 4 | 1 | STM-TDCS-001, STM-TI-001, STM-TMSFMRI-001, STM-TUS-001 |
| MK.BOLD_visual_cortex | hemodynamic | 4 | 2 | IMG-VIS-001, PER-BR-001, PER-NAT-001, PER-RET-001 |
| MK.DMN_connectivity | connectivity | 4 | 1 | STA-HYPN-001, STA-MW-001, STA-PSY-001, STA-REST-001 |
| MK.ErrP | erp_component | 4 | 1 | ERR-ADAPT-001, ERR-ERRP-001, ERR-OBS-001, ERR-VRPE-001 |
| MK.LRP | erp_component | 4 | 2 | CTL-MRP-001, CTL-SIM-001, MOT-RT-001, MOT-SRT-001 |
| MK.P2_auditory | erp_component | 4 | 3 | EMO-SOUND-001, ERR-AAF-001, PER-ACC-001, PER-AEP-001 |
| MK.BOLD_anterior_insula | hemodynamic | 3 | 2 | EMO-THREAT-001, SOC-PAIN-001, SOC-UG-001 |
| MK.BOLD_auditory_cortex | hemodynamic | 3 | 2 | IMG-AUD-001, PER-TON-001, PER-VOICE-001 |
| MK.BOLD_oculomotor | hemodynamic | 3 | 2 | CTL-AS-001, MOT-PURS-001, MOT-SACC-001 |
| MK.CDA | erp_component | 3 | 2 | MEM-CD-001, MEM-SWM-001, PER-MOT-001 |
| MK.CNV | erp_component | 3 | 1 | CTL-ANT-001, CTL-CNV-001, CTL-CPT-001 |
| MK.EPN | erp_component | 3 | 1 | EMO-FACE-001, EMO-IAPS-001, EMO-WORD-001 |
| MK.MRCP | erp_component | 3 | 1 | MOT-IB-001, MOT-LIBET-001, MOT-MRCP-001 |
| MK.N1_visual | erp_component | 3 | 2 | CTL-ANT-001, PER-CUE-001, PER-IC-001 |
| MK.N2pc | erp_component | 3 | 2 | EMO-DOT-001, PER-CTXC-001, PER-VS-001 |
| MK.NoGo_P3 | erp_component | 3 | 1 | CTL-GNG-001, CTL-SART-001, CTL-SST-001 |
| MK.P1_visual | erp_component | 3 | 3 | EMO-DOT-001, PER-CUE-001, SOC-GAZE-001 |
| MK.P600 | erp_component | 3 | 1 | LAN-AGL-001, LAN-P600-001, LAN-SC-001 |
| MK.Pe | erp_component | 3 | 2 | CTL-CONF-001, CTL-FLK-001, ERR-AWARE-001 |
| MK.SEP_N20 | erp_component | 3 | 1 | STM-PAS-001, STM-SEP-001, STM-TUS-001 |
| MK.SSVEP | steady_state | 3 | 2 | PER-BR-001, SSR-SSVEP-001, SSR-SWEEP-001 |
| MK.VAN | erp_component | 3 | 1 | PER-CB-001, PER-IB-001, PER-MASK-001 |
| MK.sleep_spindle | oscillatory | 3 | 2 | MEM-TMR-001, STA-CLAS-001, STA-SLP-001 |

## 5. 每个标记物的范式数

### 5.1 分布

| 使用该标记物的范式数 | 标记物数 |
|---|---|
| 1 | 57 |
| 2 | 21 |
| 3 | 17 |
| 4 | 7 |
| 5 | 5 |
| 6 | 5 |
| 7 | 4 |
| 8 | 4 |
| 9 | 2 |
| 10 | 1 |
| 11 | 1 |
| 13 | 1 |
| 14 | 1 |
| 19 | 2 |
| 20 | 1 |

### 5.2 全表

| 标记物 | 类型 | 范式数 | 范式 |
|---|---|---|---|
| MK.ABR | erp_component | 1 | PER-ABR-001 |
| MK.ASSR | steady_state | 1 | SSR-ASSR-001 |
| MK.AV_interaction_ERP | erp_component | 1 | PER-MSI-001 |
| MK.BOLD_TPJ | hemodynamic | 5 | SOC-ANIM-001, SOC-IMIT-001, SOC-RME-001, SOC-TOM-001, SOC-VPT-001 |
| MK.BOLD_amygdala | hemodynamic | 6 | CTL-AMBIG-001, EMO-AUTO-001, EMO-FACE-001, EMO-FC-001, EMO-IAPS-001, EMO-THREAT-001 |
| MK.BOLD_anterior_insula | hemodynamic | 3 | EMO-THREAT-001, SOC-PAIN-001, SOC-UG-001 |
| MK.BOLD_auditory_cortex | hemodynamic | 3 | IMG-AUD-001, PER-TON-001, PER-VOICE-001 |
| MK.BOLD_category_selective | hemodynamic | 8 | IMG-VIS-001, LAN-VWFA-001, MEM-CFMT-001, MEM-RIF-001, MEM-RPRIM-001, PER-BODY-001, PER-CAT-001, PER-FACE-001 |
| MK.BOLD_dACC | hemodynamic | 7 | CTL-EFF-001, CTL-FORAGE-001, CTL-MSIT-001, SOC-CONF-001, SOC-CYB-001, SOC-SFB-001, STA-HYPN-001 |
| MK.BOLD_dlPFC | hemodynamic | 8 | CTL-BART-001, CTL-RNG-001, CTL-TOL-001, CTL-WASON-001, CTL-WCST-001, ERR-CAUS-001, MEM-DF-001, SOC-TPP-001 |
| MK.BOLD_frontoparietal | hemodynamic | 6 | CTL-RAVEN-001, CTL-SYLL-001, IMG-ROT-001, MEM-NBK-001, MEM-SWM-001, PER-MOT-001 |
| MK.BOLD_frontopolar | hemodynamic | 4 | CTL-ANAL-001, ERR-BANDIT-001, MEM-META-001, MEM-PM-001 |
| MK.BOLD_hippocampus | hemodynamic | 8 | MEM-EFT-001, MEM-MST-001, MEM-NAV-001, MEM-PA-001, MEM-RMEM-001, MEM-SME-001, MEM-TNT-001, PER-CTXC-001 |
| MK.BOLD_language_network | hemodynamic | 6 | LAN-LOC-001, LAN-PHA-001, LAN-PN-001, LAN-SC-001, LAN-SEMD-001, LAN-VG-001 |
| MK.BOLD_left_IFG | hemodynamic | 1 | MEM-RPT-001 |
| MK.BOLD_mPFC | hemodynamic | 5 | MEM-EFT-001, MEM-SRE-001, SOC-ANIM-001, SOC-MORAL-001, SOC-RME-001 |
| MK.BOLD_motor_network | hemodynamic | 6 | IMG-CMD-001, MOT-ME-001, MOT-MIRR-001, MOT-MSL-001, MOT-SMS-001, STM-VIB-001 |
| MK.BOLD_oculomotor | hemodynamic | 3 | CTL-AS-001, MOT-PURS-001, MOT-SACC-001 |
| MK.BOLD_olfactory_cortex | hemodynamic | 1 | IMG-OLF-001 |
| MK.BOLD_pSTS | hemodynamic | 2 | SOC-BIO-001, SOC-GAZE-001 |
| MK.BOLD_parahippocampal | hemodynamic | 1 | IMG-CMD-001 |
| MK.BOLD_posterior_insula | hemodynamic | 1 | EMO-TOUCH-001 |
| MK.BOLD_premotor_parietal | hemodynamic | 2 | MOT-OBS-001, PER-BOI-001 |
| MK.BOLD_stimulated_region | hemodynamic | 4 | STM-TDCS-001, STM-TI-001, STM-TMSFMRI-001, STM-TUS-001 |
| MK.BOLD_striatum_reward | hemodynamic | 13 | CTL-AMBIG-001, CTL-DD-001, CTL-MIXG-001, EMO-HUMOR-001, EMO-MID-001, ERR-APC-001, ERR-INST-001, ERR-PCL-001, ERR-PRL-001, ERR-TS-001, MEM-RMEM-001, SOC-CONF-001, SOC-TRUST-001 |
| MK.BOLD_vestibular_cortex | hemodynamic | 1 | STM-GVS-001 |
| MK.BOLD_visual_cortex | hemodynamic | 4 | IMG-VIS-001, PER-BR-001, PER-NAT-001, PER-RET-001 |
| MK.BOLD_vmPFC_value | hemodynamic | 5 | CTL-DD-001, CTL-IGT-001, CTL-MIXG-001, CTL-VBC-001, SOC-DICT-001 |
| MK.CCEP | erp_component | 1 | STM-CCEP-001 |
| MK.CDA | erp_component | 3 | MEM-CD-001, MEM-SWM-001, PER-MOT-001 |
| MK.CNV | erp_component | 3 | CTL-ANT-001, CTL-CNV-001, CTL-CPT-001 |
| MK.CPP | erp_component | 1 | CTL-PDM-001 |
| MK.CPS | erp_component | 1 | LAN-CPS-001 |
| MK.DBS_cortical_EP | erp_component | 1 | STM-DBSEP-001 |
| MK.DMN_connectivity | connectivity | 4 | STA-HYPN-001, STA-MW-001, STA-PSY-001, STA-REST-001 |
| MK.Dm | erp_component | 2 | MEM-FR-001, MEM-SME-001 |
| MK.EPN | erp_component | 3 | EMO-FACE-001, EMO-IAPS-001, EMO-WORD-001 |
| MK.ERAN | erp_component | 2 | LAN-AGL-001, LAN-MUS-001 |
| MK.ERN | erp_component | 1 | CTL-FLK-001 |
| MK.ERNA | field_potential | 1 | STM-DBSEP-001 |
| MK.ErrP | erp_component | 4 | ERR-ADAPT-001, ERR-ERRP-001, ERR-OBS-001, ERR-VRPE-001 |
| MK.FFR | steady_state | 1 | SSR-FFR-001 |
| MK.FN400 | erp_component | 2 | MEM-DRM-001, MEM-ON-001 |
| MK.FPAS_oddball | steady_state | 1 | SSR-FPAS-001 |
| MK.FPVS_oddball | steady_state | 1 | SSR-FPVS-001 |
| MK.FRN | erp_component | 14 | CTL-BART-001, CTL-IGT-001, EMO-MID-001, ERR-ADAPT-001, ERR-BANDIT-001, ERR-GAM-001, ERR-INST-001, ERR-PRL-001, ERR-PRT-001, ERR-PSEL-001, ERR-TE-001, ERR-TS-001, SOC-TRUST-001, SOC-UG-001 |
| MK.FRP | erp_component | 1 | LAN-READ-001 |
| MK.GEP | erp_component | 1 | PER-GEP-001 |
| MK.HEP | erp_component | 1 | PER-HBD-001 |
| MK.HbO_prefrontal | hemodynamic | 7 | CTL-TOL-001, CTL-WCST-001, EMO-STRESS-001, IMG-MA-001, LAN-VF-001, MEM-NBK-001, STA-MATB-001 |
| MK.ISC | connectivity | 2 | PER-NAT-001, STA-ENG-001 |
| MK.LEP | erp_component | 1 | PER-LEP-001 |
| MK.LPP | erp_component | 8 | EMO-APRIME-001, EMO-EST-001, EMO-IAPS-001, EMO-REG-001, EMO-SOUND-001, EMO-WORD-001, SOC-IAT-001, SOC-PAIN-001 |
| MK.LRP | erp_component | 4 | CTL-MRP-001, CTL-SIM-001, MOT-RT-001, MOT-SRT-001 |
| MK.MLR | erp_component | 1 | PER-MLR-001 |
| MK.MMN | erp_component | 5 | LAN-PHA-001, PER-AMASK-001, PER-LG-001, PER-MMN-001, PER-STREAM-001 |
| MK.MRCP | erp_component | 3 | MOT-IB-001, MOT-LIBET-001, MOT-MRCP-001 |
| MK.N140_somatosensory | erp_component | 1 | PER-TACT-001 |
| MK.N170 | erp_component | 9 | EMO-FACE-001, LAN-VWFA-001, MEM-CFMT-001, PER-BODY-001, PER-CAT-001, PER-FACE-001, SOC-BIO-001, SOC-GAZE-001, SOC-SELF-001 |
| MK.N1_auditory | erp_component | 7 | ERR-AAF-001, LAN-SIS-001, MOT-IB-001, PER-AAD-001, PER-ACC-001, PER-AEP-001, PER-AMASK-001 |
| MK.N1_visual | erp_component | 3 | CTL-ANT-001, PER-CUE-001, PER-IC-001 |
| MK.N2_frontocentral | erp_component | 7 | CTL-FLK-001, CTL-GNG-001, CTL-SIM-001, EMO-EST-001, LAN-SWITCH-001, MEM-TNT-001, SOC-WIT-001 |
| MK.N2_posterior | erp_component | 2 | PER-NAVON-001, SOC-BIO-001 |
| MK.N2pc | erp_component | 3 | EMO-DOT-001, PER-CTXC-001, PER-VS-001 |
| MK.N300_prospective | erp_component | 1 | MEM-PM-001 |
| MK.N400 | erp_component | 9 | EMO-APRIME-001, LAN-GEST-001, LAN-LDT-001, LAN-N400-001, LAN-NWL-001, LAN-PRIME-001, LAN-SC-001, MEM-RPRIM-001, SOC-IAT-001 |
| MK.N450 | erp_component | 1 | CTL-STR-001 |
| MK.NoGo_P3 | erp_component | 3 | CTL-GNG-001, CTL-SART-001, CTL-SST-001 |
| MK.OERP | erp_component | 1 | PER-OLF-001 |
| MK.ORN | erp_component | 1 | PER-ORN-001 |
| MK.P100_PRVEP | erp_component | 1 | PER-PRVEP-001 |
| MK.P1_visual | erp_component | 3 | EMO-DOT-001, PER-CUE-001, SOC-GAZE-001 |
| MK.P2_auditory | erp_component | 4 | EMO-SOUND-001, ERR-AAF-001, PER-ACC-001, PER-AEP-001 |
| MK.P2_visual | erp_component | 2 | SOC-RACE-001, SOC-WIT-001 |
| MK.P3a | erp_component | 1 | PER-ODD-001 |
| MK.P3b | erp_component | 19 | CTL-ANT-001, CTL-CPT-001, CTL-DT-001, CTL-WCST-001, ERR-CHGPT-001, MEM-CIT-001, MEM-NBK-001, PER-AB-001, PER-IB-001, PER-LG-001, PER-MASK-001, PER-NAVON-001, PER-ODD-001, PER-TACT-001, SOC-CYB-001, SOC-NAME-001, SOC-SELF-001, STA-MW-001, STM-TAVNS-001 |
| MK.P50_gating | erp_component | 1 | PER-GATE-001 |
| MK.P600 | erp_component | 3 | LAN-AGL-001, LAN-P600-001, LAN-SC-001 |
| MK.Pd | erp_component | 1 | PER-ADDS-001 |
| MK.Pe | erp_component | 3 | CTL-CONF-001, CTL-FLK-001, ERR-AWARE-001 |
| MK.RREP | erp_component | 1 | PER-RREP-001 |
| MK.SCP | erp_component | 1 | STA-SCP-001 |
| MK.SEP_N20 | erp_component | 3 | STM-PAS-001, STM-SEP-001, STM-TUS-001 |
| MK.SMR_ERD | oscillatory | 19 | IMG-CMD-001, IMG-SAO-001, IMG-TACT-001, MOT-ATT-001, MOT-BIMAN-001, MOT-CURSOR-001, MOT-FORCE-001, MOT-ME-001, MOT-MI-001, MOT-MSL-001, MOT-MVF-001, MOT-OBS-001, MOT-PASS-001, MOT-SMS-001, MOT-SRT-001, SOC-IMIT-001, SOC-JA-001, STA-NF-001, STM-PHTMS-001 |
| MK.SPN | erp_component | 1 | PER-SPN-001 |
| MK.SSEP_beat | steady_state | 1 | SSR-BEAT-001 |
| MK.SSEP_nociceptive | steady_state | 1 | SSR-NSSEP-001 |
| MK.SSMVEP | steady_state | 1 | SSR-SSMVEP-001 |
| MK.SSSEP | steady_state | 1 | SSR-SSSEP-001 |
| MK.SSVEP | steady_state | 3 | PER-BR-001, SSR-SSVEP-001, SSR-SWEEP-001 |
| MK.TEP | erp_component | 2 | STM-PAS-001, STM-TEP-001 |
| MK.VAN | erp_component | 3 | PER-CB-001, PER-IB-001, PER-MASK-001 |
| MK.affective_band_power | oscillatory | 2 | EMO-AUTO-001, EMO-FILM-001 |
| MK.alpha_lateralization | oscillatory | 2 | MEM-RC-001, PER-CVA-001 |
| MK.alpha_posterior | oscillatory | 20 | CTL-AUT-001, CTL-RAT-001, CTL-SART-001, IMG-ROT-001, IMG-VIS-001, MEM-DF-001, MEM-DMS-001, MEM-NBK-001, MEM-SB-001, SOC-VPT-001, STA-DRV-001, STA-ENG-001, STA-MATB-001, STA-MED-001, STA-MW-001, STA-NF-001, STA-PSY-001, STA-PVT-001, STA-REST-001, STM-PBM-001 |
| MK.cVEP | steady_state | 1 | SSR-CVEP-001 |
| MK.corticokinematic_coherence | connectivity | 1 | MOT-PASS-001 |
| MK.corticomuscular_coherence | connectivity | 1 | MOT-FORCE-001 |
| MK.flash_VEP | erp_component | 1 | PER-FVEP-001 |
| MK.frontal_alpha_anesthesia | oscillatory | 1 | STA-ANES-001 |
| MK.frontal_alpha_asymmetry | oscillatory | 2 | EMO-FILM-001, EMO-STRESS-001 |
| MK.frontal_midline_theta | oscillatory | 10 | CTL-DT-001, CTL-SW-001, ERR-OGNG-001, ERR-PSEL-001, IMG-MA-001, MEM-DS-001, MEM-NBK-001, MEM-SB-001, STA-MATB-001, STA-MED-001 |
| MK.gamma_power | oscillatory | 1 | MEM-DMS-001 |
| MK.high_gamma | field_potential | 11 | IMG-AUD-001, IMG-SPI-001, LAN-OVS-001, LAN-PCAT-001, LAN-PN-001, LAN-SIS-001, MEM-FR-001, MOT-GRASP-001, MOT-ME-001, MOT-REACH-001, MOT-TRACK-001 |
| MK.hippocampal_theta | oscillatory | 2 | MEM-NAV-001, MEM-PA-001 |
| MK.interbrain_synchrony | connectivity | 2 | SOC-EYE-001, SOC-JA-001 |
| MK.interhemispheric_coherence | connectivity | 1 | MOT-BIMAN-001 |
| MK.intermodulation | steady_state | 1 | SSR-IM-001 |
| MK.left_anterior_negativity | erp_component | 1 | LAN-P600-001 |
| MK.linguistic_structure_tracking | steady_state | 2 | LAN-HIER-001, LAN-SL-001 |
| MK.low_freq_kinematics | oscillatory | 1 | MOT-TRACK-001 |
| MK.mVEP | erp_component | 1 | PER-MVEP-001 |
| MK.motor_cortical_spiking | single_unit | 6 | LAN-OVS-001, MOT-ATT-001, MOT-CURSOR-001, MOT-GRASP-001, MOT-HW-001, MOT-REACH-001 |
| MK.oERN | erp_component | 1 | ERR-OBS-001 |
| MK.omission_response | erp_component | 1 | PER-OMIT-001 |
| MK.oscillatory_entrainment | oscillatory | 2 | SSR-RVS-001, STM-TACS-001 |
| MK.parietal_old_new | erp_component | 2 | MEM-DRM-001, MEM-ON-001 |
| MK.perturbation_N1 | erp_component | 1 | MOT-PERT-001 |
| MK.presaccadic_potential | erp_component | 2 | CTL-AS-001, MOT-SACC-001 |
| MK.rIFG_beta | oscillatory | 1 | CTL-SST-001 |
| MK.right_frontal_old_new | erp_component | 1 | MEM-SRC-001 |
| MK.sleep_spindle | oscillatory | 3 | MEM-TMR-001, STA-CLAS-001, STA-SLP-001 |
| MK.slow_wave | oscillatory | 5 | MEM-TMR-001, STA-ANES-001, STA-CLAS-001, STA-DREAM-001, STA-SLP-001 |
| MK.speech_envelope_tracking | oscillatory | 2 | LAN-NAT-001, PER-AAD-001 |
| MK.subthalamic_beta | oscillatory | 1 | STM-ADBS-001 |
| MK.switch_positivity | erp_component | 1 | CTL-SW-001 |
| MK.tES_power_aftereffect | oscillatory | 2 | STM-TACS-001, STM-TDCS-001 |
| MK.theta_drowsiness | oscillatory | 2 | STA-DRV-001, STA-PVT-001 |
| MK.vMMN | erp_component | 1 | PER-VMMN-001 |

## 6. 零覆盖空白

下表中的 · 表示该组合目前没有任何范式。并非每个空格都是缺口（例如 PET × 稳态响应在方法上不适用），但它们是第二遍和新候选检索的检查清单。

### 6.1 记录模态 × 族

|  | perception | motor | steady_state | error | language | memory | emotion | control | imagery | social | state | stimulation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EEG | 43 | 24 | 13 | 16 | 20 | 24 | 13 | 23 | 8 | 16 | 14 | 12 |
| MEG | 21 | 11 | 5 | · | 6 | 3 | 1 | 1 | · | · | 2 | 2 |
| fNIRS | · | 2 | · | · | 2 | 1 | 1 | 2 | 3 | 3 | 4 | 1 |
| fMRI | 13 | 11 | · | 9 | 12 | 20 | 13 | 26 | 5 | 18 | 5 | 7 |
| ECoG | 3 | 7 | · | · | 6 | · | · | · | 2 | · | · | 1 |
| sEEG | · | · | · | · | · | 3 | · | · | 1 | · | · | 1 |
| intracortical | · | 6 | · | · | 1 | · | · | 1 | 1 | · | · | · |
| fUS | · | · | · | · | · | · | · | · | · | · | · | · |
| PET | · | · | · | · | · | · | · | 1 | 2 | 1 | · | · |
| other | · | · | · | · | · | · | · | · | · | · | · | 2 |

（· = 0）

### 6.2 刺激模态 × 族

|  | perception | motor | steady_state | error | language | memory | emotion | control | imagery | social | state | stimulation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| visual | 26 | 20 | 7 | 18 | 18 | 27 | 13 | 32 | 5 | 23 | 6 | 1 |
| auditory | 16 | 5 | 4 | 2 | 21 | 11 | 4 | 5 | 4 | 3 | 5 | · |
| somatosensory | 5 | 2 | 2 | 1 | · | · | 1 | · | 2 | · | · | 3 |
| olfactory | 1 | · | · | · | · | 1 | · | · | 1 | · | · | · |
| gustatory | 1 | · | · | 1 | · | · | · | · | · | · | · | · |
| electrical_stimulation | · | · | · | · | · | · | 2 | · | · | · | · | 11 |
| magnetic_stimulation | · | · | · | · | · | · | · | · | · | · | · | 4 |
| ultrasound_stimulation | · | · | · | · | · | · | · | · | · | · | · | 1 |
| motor_execution | · | 21 | · | 3 | 4 | · | · | 1 | · | 2 | 3 | · |
| mental_imagery | · | 2 | · | · | · | · | 1 | · | 7 | · | · | · |
| cognitive_task | 1 | · | · | · | 1 | 1 | 2 | 2 | 1 | · | 4 | · |
| resting_state | · | · | · | · | · | · | · | · | · | · | 4 | · |
| naturalistic | 1 | · | · | · | 2 | 1 | 1 | · | · | · | 1 | · |
| optical_stimulation | · | · | · | · | · | · | · | · | · | · | · | 1 |
| pharmacological | · | · | · | · | · | · | · | · | · | · | 2 | · |

（· = 0）

### 6.3 BCI 类别 × 族

|  | perception | motor | steady_state | error | language | memory | emotion | control | imagery | social | state | stimulation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| active | · | 11 | · | · | 2 | · | · | · | 8 | · | 2 | · |
| reactive | 6 | · | 5 | · | · | · | · | · | · | 1 | · | · |
| passive | 3 | · | · | 3 | · | 2 | 3 | · | · | · | 9 | 2 |
| none | 44 | 18 | 9 | 16 | 24 | 26 | 16 | 33 | 4 | 23 | 8 | 14 |

（· = 0）

### 6.4 标记物类型 × 族（按范式–标记物关联）

|  | perception | motor | steady_state | error | language | memory | emotion | control | imagery | social | state | stimulation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| erp_component | 49 | 8 | · | 18 | 18 | 15 | 16 | 25 | · | 16 | 2 | 8 |
| oscillatory | 2 | 13 | 1 | 2 | 1 | 13 | 4 | 6 | 6 | 3 | 21 | 6 |
| steady_state | 1 | · | 12 | · | 2 | · | · | · | · | · | · | · |
| hemodynamic | 11 | 7 | · | 7 | 8 | 20 | 10 | 22 | 8 | 19 | 2 | 6 |
| single_unit | · | 5 | · | · | 1 | · | · | · | · | · | · | · |
| field_potential | · | 4 | · | · | 4 | 1 | · | · | 2 | · | · | 1 |
| connectivity | 1 | 3 | · | · | · | · | · | · | · | 2 | 5 | · |

（· = 0）

### 6.5 汇总

| 交叉表 | 零格数 | 总格数 |
|---|---|---|
| 记录模态 × 族 | 63 | 120 |
| 刺激模态 × 族 | 117 | 180 |
| BCI 类别 × 族 | 23 | 48 |
| 标记物类型 × 族 | 37 | 84 |

没有任何范式使用的词表取值：recording_modality: fUS

没有任何 BCI 用途（active / reactive / passive）范式的族：control
