# 包 D：记忆与语言 · 工作目录

- 范式族：`memory`、`language`
- 任务单：[`curation/packages/pkg_D_记忆与语言.md`](../../packages/pkg_D_记忆与语言.md)
- 候选 42 个：收录 38、并入 2、排除 1、暂缓 1（判定见 [`curation/decisions.md`](../../decisions.md)）
- 本包负责编写的标记物：17 个（`curation/registry/markers.csv` 中 `owner_pkg = D`）

## 写入范围（D-029）

你**只能**新增或修改以下文件：

1. `paradigms/memory/*`、`paradigms/language/*`；
2. `knowledge/markers/` 中 `owner_pkg = D` 的标记物文件（下表），以及你在本包 `marker_requests.csv` 中申请、且登记表中**不存在**同义项的新标记物文件（用清晰的规范 ID，如 `MK.N2pc`，不要用 `MK.new1`）；
3. `curation/work/pkg_D/*`（本目录）。

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
- 本包标记物都已有维护者建的骨架文件（`description` 为"待包 D 编写。"），直接覆盖；4 个种子标记物文件（P3a、P3b、SMR_ERD、SSVEP）已有内容，只做补充。
- 被并入的候选不建文件，写成目标范式的 `variants`（D-030）；混合 BCI、超扫描变体分别以 `Hybrid:`、`Hyperscanning:` 开头（D-022、D-021）。
- 一个 PR 只放一个范式及其首次用到的标记物；本地 `python scripts/validate.py` 0 问题后再提交。
- 查不到的就空着，不要猜；所有出处 `verified: false`，由审核人核实。

## 本包收录范式与必须使用的标记物

| ID | 范式 | 标记物 |
|---|---|---|
| MEM-NBK-001 | n-back | MK.frontal_midline_theta; MK.P3b; MK.alpha_posterior; MK.HbO_prefrontal; MK.BOLD_frontoparietal |
| MEM-CD-001 | 变化检测 | MK.CDA |
| MEM-DF-001 | 定向遗忘 | MK.alpha_posterior; MK.BOLD_dlPFC |
| MEM-DMS-001 | 延迟匹配 | MK.alpha_posterior; MK.gamma_power |
| MEM-DRM-001 | 错误记忆（DRM） | MK.FN400; MK.parietal_old_new |
| MEM-FR-001 | 自由回忆与词表学习 | MK.Dm; MK.high_gamma |
| MEM-NAV-001 | 虚拟空间导航记忆 | MK.hippocampal_theta; MK.BOLD_hippocampus |
| MEM-ON-001 | 新旧再认 | MK.FN400; MK.parietal_old_new |
| MEM-PA-001 | 配对联想学习 | MK.hippocampal_theta; MK.BOLD_hippocampus |
| MEM-RC-001 | 回溯线索 | MK.alpha_lateralization |
| MEM-SB-001 | Sternberg 工作记忆 | MK.frontal_midline_theta; MK.alpha_posterior |
| MEM-SME-001 | 后续记忆效应 | MK.Dm; MK.BOLD_hippocampus |
| MEM-SWM-001 | 空间工作记忆 | MK.CDA; MK.BOLD_frontoparietal |
| MEM-TMR-001 | 睡眠中目标记忆再激活 | MK.sleep_spindle; MK.slow_wave |
| MEM-TNT-001 | 想/不想 | MK.N2_frontocentral; MK.BOLD_hippocampus |
| MEM-CFMT-001 | 剑桥面孔记忆 | MK.N170; MK.BOLD_category_selective |
| MEM-DS-001 | 数字广度 | MK.frontal_midline_theta |
| MEM-META-001 | 元记忆（知晓感、学习判断） | MK.BOLD_frontopolar |
| MEM-MST-001 | 记忆相似性（模式分离） | MK.BOLD_hippocampus |
| MEM-PM-001 | 前瞻记忆 | MK.N300_prospective; MK.BOLD_frontopolar |
| MEM-SRC-001 | 来源记忆 | MK.right_frontal_old_new |
| MEM-SRE-001 | 自我参照编码 | MK.BOLD_mPFC |
| LAN-OVS-001 | 出声或尝试言语产生 | MK.high_gamma; MK.motor_cortical_spiking |
| LAN-HIER-001 | 语言层级结构频率标记 | MK.linguistic_structure_tracking |
| LAN-LDT-001 | 词汇判断 | MK.N400 |
| LAN-LOC-001 | 语言定位任务 | MK.BOLD_language_network |
| LAN-MUS-001 | 音乐句法违例 | MK.ERAN |
| LAN-N400-001 | 语义违例 | MK.N400 |
| LAN-NAT-001 | 自然语音聆听 | MK.speech_envelope_tracking |
| LAN-P600-001 | 句法违例 | MK.P600; MK.left_anterior_negativity |
| LAN-PN-001 | 图片命名 | MK.high_gamma; MK.BOLD_language_network |
| LAN-PRIME-001 | 语义启动 | MK.N400 |
| LAN-READ-001 | 自然阅读（眼动同步） | MK.FRP |
| LAN-SC-001 | 句子理解 | MK.N400; MK.P600; MK.BOLD_language_network |
| LAN-VF-001 | 言语流畅性 | MK.HbO_prefrontal |
| LAN-VG-001 | 动词生成 | MK.BOLD_language_network |
| LAN-AGL-001 | 人工语法学习 | MK.P600; MK.ERAN |
| LAN-PHA-001 | 语音意识 | MK.MMN; MK.BOLD_language_network |

## 需要写成变体的被并入候选

| 被并入候选 | 来源包 | 目标范式 | 决议 |
|---|---|---|---|
| MEM-RK-001 记得/知道 | D | MEM-ON-001 | D-024 |

## 本包不建条目的候选

| 候选 | 判定 | 决议 |
|---|---|---|
| MEM-OSPAN-001 操作广度 | 暂缓 | D-023 |
| MEM-RK-001 记得/知道 | 并入 MEM-ON-001 | D-024 |
| LAN-PHON-001 音位辨别 | 并入 PER-MMN-001 | D-017 |
| LAN-SPR-001 自定步速阅读 | 排除 | D-023 |

## 本包负责编写的标记物

| 标记物 | 名称 | 类型 | 使用范式 |
|---|---|---|---|
| `MK.BOLD_language_network` | 语言网络 BOLD | hemodynamic | LAN-LOC-001; LAN-PN-001; LAN-SC-001; LAN-VG-001; LAN-PHA-001 |
| `MK.BOLD_mPFC` | 内侧前额叶 BOLD（自我/心智化） | hemodynamic | MEM-SRE-001; SOC-RME-001 |
| `MK.Dm` | 后续记忆效应（Dm） | erp_component | MEM-FR-001; MEM-SME-001 |
| `MK.ERAN` | 早期右前负波 | erp_component | LAN-MUS-001; LAN-AGL-001 |
| `MK.FN400` | FN400（额中部新旧效应） | erp_component | MEM-DRM-001; MEM-ON-001 |
| `MK.FRP` | 注视相关电位 | erp_component | LAN-READ-001 |
| `MK.gamma_power` | 头皮 γ 功率（30–100 Hz） | oscillatory | MEM-DMS-001 |
| `MK.hippocampal_theta` | 海马 θ | oscillatory | MEM-NAV-001; MEM-PA-001 |
| `MK.left_anterior_negativity` | 左前负波 | erp_component | LAN-P600-001 |
| `MK.linguistic_structure_tracking` | 语言层级结构的皮层跟踪 | steady_state | LAN-HIER-001 |
| `MK.N300_prospective` | 前瞻记忆 N300 | erp_component | MEM-PM-001 |
| `MK.N400` | N400 | erp_component | LAN-LDT-001; LAN-N400-001; LAN-PRIME-001; LAN-SC-001; EMO-APRIME-001; SOC-IAT-001 |
| `MK.P600` | P600 | erp_component | LAN-P600-001; LAN-SC-001; LAN-AGL-001 |
| `MK.parietal_old_new` | 左顶叶新旧效应 | erp_component | MEM-DRM-001; MEM-ON-001 |
| `MK.right_frontal_old_new` | 晚期右额新旧效应 | erp_component | MEM-SRC-001 |
| `MK.sleep_spindle` | 睡眠纺锤波 | oscillatory | MEM-TMR-001; STA-SLP-001 |
| `MK.slow_wave` | 慢波 / 慢振荡 | oscillatory | MEM-TMR-001; STA-ANES-001; STA-SLP-001 |
