# 包 C：错误监测与认知控制 · 工作目录

- 范式族：`error`、`control`
- 任务单：[`curation/packages/pkg_C_错误监测与认知控制.md`](../../packages/pkg_C_错误监测与认知控制.md)
- 候选 37 个：收录 35、并入 0、排除 0、暂缓 2（判定见 [`curation/decisions.md`](../../decisions.md)）
- 本包负责编写的标记物：17 个（`curation/registry/markers.csv` 中 `owner_pkg = C`）

## 写入范围（D-029）

你**只能**新增或修改以下文件：

1. `paradigms/error/*`、`paradigms/control/*`；
2. `knowledge/markers/` 中 `owner_pkg = C` 的标记物文件（下表），以及你在本包 `marker_requests.csv` 中申请、且登记表中**不存在**同义项的新标记物文件（用清晰的规范 ID，如 `MK.N2pc`，不要用 `MK.new1`）；
3. `curation/work/pkg_C/*`（本目录）。

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
- 本包标记物都已有维护者建的骨架文件（`description` 为"待包 C 编写。"），直接覆盖；4 个种子标记物文件（P3a、P3b、SMR_ERD、SSVEP）已有内容，只做补充。
- 被并入的候选不建文件，写成目标范式的 `variants`（D-030）；混合 BCI、超扫描变体分别以 `Hybrid:`、`Hyperscanning:` 开头（D-022、D-021）。
- 一个 PR 只放一个范式及其首次用到的标记物；本地 `python scripts/validate.py` 0 问题后再提交。
- 查不到的就空着，不要猜；所有出处 `verified: false`，由审核人核实。

## 本包收录范式与必须使用的标记物

| ID | 范式 | 标记物 |
|---|---|---|
| ERR-ERRP-001 | 交互式错误电位 | MK.ErrP |
| ERR-OBS-001 | 观察性错误 | MK.oERN; MK.ErrP |
| ERR-ADAPT-001 | 运动适应（视觉旋转） | MK.FRN; MK.ErrP |
| ERR-AWARE-001 | 错误觉知 | MK.Pe |
| ERR-BANDIT-001 | 多臂老虎机（探索-利用） | MK.FRN; MK.BOLD_frontopolar |
| ERR-GAM-001 | 赌博与奖赏反馈 | MK.FRN |
| ERR-PRL-001 | 概率反转学习 | MK.FRN; MK.BOLD_striatum_reward |
| ERR-PSEL-001 | 概率选择任务 | MK.FRN; MK.frontal_midline_theta |
| ERR-TE-001 | 时间估计任务 | MK.FRN |
| ERR-CAUS-001 | 因果学习 | MK.BOLD_dlPFC |
| ERR-INST-001 | 工具性条件化 | MK.FRN; MK.BOLD_striatum_reward |
| ERR-PCL-001 | 概率分类学习（天气预报任务） | MK.BOLD_striatum_reward |
| ERR-TS-001 | 两阶段决策（基于模型/无模型） | MK.BOLD_striatum_reward; MK.FRN |
| CTL-ANT-001 | 注意网络测试 | MK.N1_visual; MK.P3b; MK.CNV |
| CTL-AS-001 | 反向眼跳 | MK.presaccadic_potential; MK.BOLD_oculomotor |
| CTL-CNV-001 | S1-S2 预期任务 | MK.CNV |
| CTL-CPT-001 | 持续操作任务（AX-CPT） | MK.CNV; MK.P3b |
| CTL-DD-001 | 延迟折扣 | MK.BOLD_striatum_reward; MK.BOLD_vmPFC_value |
| CTL-DT-001 | 双任务 | MK.P3b; MK.frontal_midline_theta |
| CTL-FLK-001 | Flanker 任务 | MK.ERN; MK.Pe; MK.N2_frontocentral |
| CTL-GNG-001 | Go/NoGo | MK.N2_frontocentral; MK.NoGo_P3 |
| CTL-IGT-001 | 爱荷华赌博任务 | MK.FRN; MK.BOLD_vmPFC_value |
| CTL-PDM-001 | 知觉决策（随机点运动） | MK.CPP |
| CTL-SART-001 | 持续注意反应任务（SART） | MK.NoGo_P3; MK.alpha_posterior |
| CTL-SIM-001 | Simon 任务 | MK.N2_frontocentral; MK.LRP |
| CTL-SST-001 | 停止信号任务 | MK.NoGo_P3; MK.rIFG_beta |
| CTL-STR-001 | Stroop 任务 | MK.N450 |
| CTL-SW-001 | 任务切换 | MK.frontal_midline_theta; MK.switch_positivity |
| CTL-TOL-001 | 伦敦塔（计划） | MK.BOLD_dlPFC; MK.HbO_prefrontal |
| CTL-WCST-001 | 威斯康星卡片分类 | MK.BOLD_dlPFC; MK.P3b; MK.HbO_prefrontal |
| CTL-BART-001 | 气球模拟风险任务 | MK.FRN; MK.BOLD_dlPFC |
| CTL-EFF-001 | 努力决策 | MK.BOLD_dACC |
| CTL-RAT-001 | 远距离联想（创造力） | MK.alpha_posterior |
| CTL-RAVEN-001 | 瑞文推理 | MK.BOLD_frontoparietal |
| CTL-WASON-001 | Wason 选择任务 | MK.BOLD_dlPFC |

## 本包不建条目的候选

| 候选 | 判定 | 决议 |
|---|---|---|
| CTL-DSST-001 数字符号替换 | 暂缓 | D-023 |
| CTL-TMT-001 连线测验 | 暂缓 | D-023 |

## 本包负责编写的标记物

| 标记物 | 名称 | 类型 | 使用范式 |
|---|---|---|---|
| `MK.BOLD_dACC` | 背侧前扣带 BOLD | hemodynamic | CTL-EFF-001; SOC-CYB-001 |
| `MK.BOLD_dlPFC` | 背外侧前额叶 BOLD | hemodynamic | ERR-CAUS-001; CTL-TOL-001; CTL-WCST-001; CTL-BART-001; CTL-WASON-001; MEM-DF-001; SOC-TPP-001 |
| `MK.BOLD_frontopolar` | 额极皮层 BOLD | hemodynamic | ERR-BANDIT-001; MEM-META-001; MEM-PM-001 |
| `MK.BOLD_striatum_reward` | 纹状体奖赏/预测误差 BOLD | hemodynamic | ERR-PRL-001; ERR-INST-001; ERR-PCL-001; ERR-TS-001; CTL-DD-001; EMO-MID-001; SOC-TRUST-001 |
| `MK.BOLD_vmPFC_value` | 腹内侧前额叶价值 BOLD | hemodynamic | CTL-DD-001; CTL-IGT-001; SOC-DICT-001 |
| `MK.CNV` | 关联性负变 | erp_component | CTL-ANT-001; CTL-CNV-001; CTL-CPT-001 |
| `MK.CPP` | 中央顶正波 | erp_component | CTL-PDM-001 |
| `MK.ERN` | 错误相关负波 | erp_component | CTL-FLK-001 |
| `MK.ErrP` | 交互式错误电位 | erp_component | ERR-ERRP-001; ERR-OBS-001; ERR-ADAPT-001 |
| `MK.FRN` | 反馈相关负波 / 奖赏正波 | erp_component | ERR-ADAPT-001; ERR-BANDIT-001; ERR-GAM-001; ERR-PRL-001; ERR-PSEL-001; ERR-TE-001; ERR-INST-001; ERR-TS-001; CTL-IGT-001; CTL-BART-001; EMO-MID-001; SOC-TRUST-001; SOC-UG-001 |
| `MK.N2_frontocentral` | 额中央 N2（冲突/抑制） | erp_component | CTL-FLK-001; CTL-GNG-001; CTL-SIM-001; MEM-TNT-001; EMO-EST-001; SOC-WIT-001 |
| `MK.N450` | N450（Stroop 干扰） | erp_component | CTL-STR-001 |
| `MK.NoGo_P3` | NoGo/停止 P3（抑制 P3） | erp_component | CTL-GNG-001; CTL-SART-001; CTL-SST-001 |
| `MK.oERN` | 观察性错误相关负波 | erp_component | ERR-OBS-001 |
| `MK.Pe` | 错误正波 | erp_component | ERR-AWARE-001; CTL-FLK-001 |
| `MK.rIFG_beta` | 右额下回 β（停止） | oscillatory | CTL-SST-001 |
| `MK.switch_positivity` | 切换相关正波 | erp_component | CTL-SW-001 |
