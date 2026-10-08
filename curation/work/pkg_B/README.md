# 包 B：运动、想象与刺激 · 工作目录

- 范式族：`motor`、`imagery`、`stimulation`
- 任务单：[`curation/packages/pkg_B_运动、想象与刺激.md`](../../packages/pkg_B_运动、想象与刺激.md)
- 候选 41 个：收录 34、并入 5、排除 2、暂缓 0（判定见 [`curation/decisions.md`](../../decisions.md)）
- 本包负责编写的标记物：23 个（`curation/registry/markers.csv` 中 `owner_pkg = B`）

## 写入范围（D-029）

你**只能**新增或修改以下文件：

1. `paradigms/motor/*`、`paradigms/imagery/*`、`paradigms/stimulation/*`；
2. `knowledge/markers/` 中 `owner_pkg = B` 的标记物文件（下表），以及你在本包 `marker_requests.csv` 中申请、且登记表中**不存在**同义项的新标记物文件（用清晰的规范 ID，如 `MK.N2pc`，不要用 `MK.new1`）；
3. `curation/work/pkg_B/*`（本目录）。

你**不能**修改：`curation/candidates.csv`、`curation/registry/*`、`knowledge/regions.yaml`、`knowledge/constructs.yaml`、`taxonomy/*`、`schema/*`、`scripts/*`，以及其他包的范式、标记物和工作目录。需要改这些文件时，写进 `worklog.md` 并在周五例会提出，由维护者修改。

## 本目录文件

| 文件 | 用途 |
|---|---|
| `worklog.md` | 工作日志：每次工作追加一节；跨包交接、待例会事项写在这里 |
| `search_log.md` | 检索记录（日期、数据库、检索式、命中数、新增文献数），维护者汇总进 `search_protocol.md` |
| `status.csv` | 本包范式进度：`proposed_id,status,first_source_ref,n_leads_used,blockers`。status 取值：待认领 / 编写中 / 待审核 / 已合并（骨架）/ 已审核（完整）/ 提请暂缓 |
| `new_candidates.csv` | 读综述时发现的遗漏范式（不要直接改 candidates.csv），维护者每周审查并分配 ID |
| `marker_requests.csv` | 登记表中没有的标记物申请（D-028 第 7 条） |
| `pr/` | 每个 PR 的出处核对表草稿，文件名 `<范式ID>.md`，内容即 PR 描述 |

## 规则速查

- `markers` 字段只用 `curation/registry/paradigm_markers.csv` 给出的 ID；要改，先在 `marker_requests.csv` 或 worklog 中提出。
- 本包标记物都已有维护者建的骨架文件（`description` 为"待包 B 编写。"），直接覆盖；4 个种子标记物文件（P3a、P3b、SMR_ERD、SSVEP）已有内容，只做补充。
- 被并入的候选不建文件，写成目标范式的 `variants`（D-030）；混合 BCI、超扫描变体分别以 `Hybrid:`、`Hyperscanning:` 开头（D-022、D-021）。
- 一个 PR 只放一个范式及其首次用到的标记物；本地 `python scripts/validate.py` 0 问题后再提交。
- 查不到的就空着，不要猜；所有出处 `verified: false`，由审核人核实。

## 本包收录范式与必须使用的标记物

| ID | 范式 | 标记物 |
|---|---|---|
| MOT-ATT-001 | 尝试运动（瘫痪患者） | MK.SMR_ERD; MK.motor_cortical_spiking |
| MOT-CURSOR-001 | 闭环光标控制 | MK.SMR_ERD; MK.motor_cortical_spiking |
| MOT-GRASP-001 | 抓握与手势 | MK.high_gamma; MK.motor_cortical_spiking |
| MOT-HW-001 | 尝试手写 | MK.motor_cortical_spiking |
| MOT-ME-001 | 运动执行 | MK.SMR_ERD; MK.high_gamma; MK.BOLD_motor_network |
| MOT-MI-001 | 运动想象 | MK.SMR_ERD |
| MOT-MRCP-001 | 自主运动准备（准备电位） | MK.MRCP |
| MOT-REACH-001 | 中心外伸伸够任务 | MK.motor_cortical_spiking; MK.high_gamma |
| MOT-BIMAN-001 | 双手协调 | MK.SMR_ERD; MK.interhemispheric_coherence |
| MOT-FORCE-001 | 等长力控制 | MK.SMR_ERD; MK.corticomuscular_coherence |
| MOT-MSL-001 | 运动序列学习（手指序列） | MK.SMR_ERD; MK.BOLD_motor_network |
| MOT-OBS-001 | 动作观察 | MK.SMR_ERD; MK.BOLD_premotor_parietal |
| MOT-RT-001 | 简单/选择反应时 | MK.LRP |
| MOT-SACC-001 | 眼跳任务 | MK.presaccadic_potential; MK.BOLD_oculomotor |
| MOT-SRT-001 | 序列反应时（运动序列学习） | MK.LRP; MK.SMR_ERD |
| MOT-TRACK-001 | 连续轨迹追踪 | MK.low_freq_kinematics; MK.high_gamma |
| MOT-IB-001 | 意向绑定（主体感） | MK.MRCP; MK.N1_auditory |
| MOT-MIRR-001 | 镜像描摹 | MK.BOLD_motor_network |
| IMG-CMD-001 | 指令跟随想象（意识评估） | MK.BOLD_motor_network; MK.BOLD_parahippocampal; MK.SMR_ERD |
| IMG-MA-001 | 心算 | MK.HbO_prefrontal; MK.frontal_midline_theta |
| IMG-SPI-001 | 想象语音（内部言语） | MK.high_gamma |
| IMG-AUD-001 | 听觉想象 | MK.BOLD_auditory_cortex; MK.high_gamma |
| IMG-ROT-001 | 心理旋转 | MK.alpha_posterior; MK.BOLD_frontoparietal |
| IMG-SAO-001 | 体感注意定向 | MK.SMR_ERD |
| IMG-VIS-001 | 视觉想象 | MK.alpha_posterior; MK.BOLD_visual_cortex; MK.BOLD_category_selective |
| IMG-WORD-001 | 词语联想与生成 | MK.HbO_prefrontal |
| STM-CCEP-001 | 皮层-皮层诱发电位 | MK.CCEP |
| STM-DBSEP-001 | 深部脑刺激诱发电位 | MK.ERNA; MK.DBS_cortical_EP |
| STM-PAS-001 | 成对联合刺激 | MK.TEP; MK.SEP_N20 |
| STM-SEP-001 | 正中神经体感诱发电位 | MK.SEP_N20 |
| STM-TACS-001 | 经颅交流电刺激同步脑电 | MK.oscillatory_entrainment; MK.tES_power_aftereffect |
| STM-TDCS-001 | 经颅直流电刺激同步记录 | MK.tES_power_aftereffect; MK.BOLD_stimulated_region |
| STM-TEP-001 | TMS 诱发脑电 | MK.TEP |
| STM-TUS-001 | 经颅超声刺激 | MK.BOLD_stimulated_region; MK.SEP_N20 |

## 需要写成变体的被并入候选

| 被并入候选 | 来源包 | 目标范式 | 决议 |
|---|---|---|---|
| MOT-FING-001 单指运动解码 | B | MOT-ME-001 | D-005 |
| MOT-GAIT-001 下肢运动想象与步态 | B | MOT-MI-001 | D-014 |
| IMG-FACE-001 面孔与场景想象 | B | IMG-VIS-001 | D-007 |
| IMG-MUS-001 音乐想象 | B | IMG-AUD-001 | D-006 |
| IMG-NAV-001 空间导航想象 | B | IMG-CMD-001 | D-008 |

## 本包不建条目的候选

| 候选 | 判定 | 决议 |
|---|---|---|
| MOT-FING-001 单指运动解码 | 并入 MOT-ME-001 | D-005 |
| MOT-GAIT-001 下肢运动想象与步态 | 并入 MOT-MI-001 | D-014 |
| IMG-FACE-001 面孔与场景想象 | 并入 IMG-VIS-001 | D-007 |
| IMG-MUS-001 音乐想象 | 并入 IMG-AUD-001 | D-006 |
| IMG-NAV-001 空间导航想象 | 并入 IMG-CMD-001 | D-008 |
| STM-ECS-001 皮层电刺激功能定位 | 排除 | D-010 |
| STM-ICMS-001 皮层内微刺激感觉反馈 | 排除 | D-009 |

## 本包负责编写的标记物

| 标记物 | 名称 | 类型 | 使用范式 |
|---|---|---|---|
| `MK.alpha_posterior` | 后部 α 功率 | oscillatory | IMG-ROT-001; IMG-VIS-001; CTL-SART-001; CTL-RAT-001; MEM-NBK-001; MEM-DF-001; MEM-DMS-001; MEM-SB-001; SOC-VPT-001; STA-DRV-001; STA-MATB-001; STA-REST-001; STA-ENG-001; STA-MED-001; STA-MW-001; STA-NF-001; STA-PVT-001 |
| `MK.BOLD_motor_network` | 运动网络 BOLD（M1、SMA、前运动区、小脑） | hemodynamic | MOT-ME-001; MOT-MSL-001; MOT-MIRR-001; IMG-CMD-001 |
| `MK.BOLD_oculomotor` | 眼动网络 BOLD（额眼区、辅助眼区、顶内沟） | hemodynamic | MOT-SACC-001; CTL-AS-001 |
| `MK.BOLD_parahippocampal` | 海马旁回/导航网络 BOLD | hemodynamic | IMG-CMD-001 |
| `MK.BOLD_stimulated_region` | 受刺激脑区血流动力学响应 | hemodynamic | STM-TDCS-001; STM-TUS-001 |
| `MK.CCEP` | 皮层-皮层诱发电位 | erp_component | STM-CCEP-001 |
| `MK.corticomuscular_coherence` | 皮层-肌肉相干 | connectivity | MOT-FORCE-001 |
| `MK.DBS_cortical_EP` | 深部脑刺激诱发皮层电位 | erp_component | STM-DBSEP-001 |
| `MK.ERNA` | 诱发共振神经活动 | field_potential | STM-DBSEP-001 |
| `MK.frontal_midline_theta` | 额中线 θ | oscillatory | IMG-MA-001; ERR-PSEL-001; CTL-DT-001; CTL-SW-001; MEM-NBK-001; MEM-SB-001; MEM-DS-001; STA-MATB-001; STA-MED-001 |
| `MK.HbO_prefrontal` | 前额叶 HbO 任务响应 | hemodynamic | IMG-MA-001; IMG-WORD-001; CTL-TOL-001; CTL-WCST-001; MEM-NBK-001; LAN-VF-001; EMO-STRESS-001; STA-MATB-001 |
| `MK.high_gamma` | 高 γ 活动（70–150 Hz） | field_potential | MOT-GRASP-001; MOT-ME-001; MOT-REACH-001; MOT-TRACK-001; IMG-SPI-001; IMG-AUD-001; MEM-FR-001; LAN-OVS-001; LAN-PN-001 |
| `MK.interhemispheric_coherence` | 半球间相干 | connectivity | MOT-BIMAN-001 |
| `MK.low_freq_kinematics` | 低频脑电运动学跟踪 | oscillatory | MOT-TRACK-001 |
| `MK.LRP` | 偏侧化准备电位 | erp_component | MOT-RT-001; MOT-SRT-001; CTL-SIM-001 |
| `MK.motor_cortical_spiking` | 运动/前运动皮层神经元放电 | single_unit | MOT-ATT-001; MOT-CURSOR-001; MOT-GRASP-001; MOT-HW-001; MOT-REACH-001; LAN-OVS-001 |
| `MK.MRCP` | 运动相关皮层电位（准备电位） | erp_component | MOT-MRCP-001; MOT-IB-001 |
| `MK.oscillatory_entrainment` | 节律刺激引起的节律夹带 | oscillatory | STM-TACS-001 |
| `MK.presaccadic_potential` | 眼跳前电位 | erp_component | MOT-SACC-001; CTL-AS-001 |
| `MK.SEP_N20` | 正中神经体感诱发电位 N20 | erp_component | STM-PAS-001; STM-SEP-001; STM-TUS-001 |
| `MK.SMR_ERD` | 感觉运动节律 ERD/ERS | oscillatory | MOT-ATT-001; MOT-CURSOR-001; MOT-ME-001; MOT-MI-001; MOT-BIMAN-001; MOT-FORCE-001; MOT-MSL-001; MOT-OBS-001; MOT-SRT-001; IMG-CMD-001; IMG-SAO-001; SOC-JA-001; SOC-IMIT-001; STA-NF-001 |
| `MK.TEP` | TMS 诱发电位 | erp_component | STM-PAS-001; STM-TEP-001 |
| `MK.tES_power_aftereffect` | 经颅电刺激后功率改变 | oscillatory | STM-TACS-001; STM-TDCS-001 |
