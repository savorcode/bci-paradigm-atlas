# 包 A：感知与稳态 · 工作目录

- 范式族：`perception`、`steady_state`
- 任务单：[`curation/packages/pkg_A_感知与稳态.md`](../../packages/pkg_A_感知与稳态.md)
- 候选 46 个：收录 41、并入 4、排除 0、暂缓 1（判定见 [`curation/decisions.md`](../../decisions.md)）
- 本包负责编写的标记物：40 个（`curation/registry/markers.csv` 中 `owner_pkg = A`）

## 写入范围（D-029）

你**只能**新增或修改以下文件：

1. `paradigms/perception/*`、`paradigms/steady_state/*`；
2. `knowledge/markers/` 中 `owner_pkg = A` 的标记物文件（下表），以及你在本包 `marker_requests.csv` 中申请、且登记表中**不存在**同义项的新标记物文件（用清晰的规范 ID，如 `MK.N2pc`，不要用 `MK.new1`）；
3. `curation/work/pkg_A/*`（本目录）。

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
- 本包标记物都已有维护者建的骨架文件（`description` 为"待包 A 编写。"），直接覆盖；4 个种子标记物文件（P3a、P3b、SMR_ERD、SSVEP）已有内容，只做补充。
- 被并入的候选不建文件，写成目标范式的 `variants`（D-030）；混合 BCI、超扫描变体分别以 `Hybrid:`、`Hyperscanning:` 开头（D-022、D-021）。
- 一个 PR 只放一个范式及其首次用到的标记物；本地 `python scripts/validate.py` 0 问题后再提交。
- 查不到的就空着，不要猜；所有出处 `verified: false`，由审核人核实。

## 本包收录范式与必须使用的标记物

| ID | 范式 | 标记物 |
|---|---|---|
| PER-AAD-001 | 听觉选择性注意（鸡尾酒会） | MK.N1_auditory; MK.speech_envelope_tracking |
| PER-CVA-001 | 隐蔽空间注意（α 偏侧化） | MK.alpha_lateralization |
| PER-MMN-001 | 被动 oddball（失匹配负波） | MK.MMN |
| PER-MVEP-001 | 运动起始视觉诱发电位 | MK.mVEP |
| PER-ODD-001 | Oddball 范式 | MK.P3b; MK.P3a |
| PER-AB-001 | 注意瞬脱 | MK.P3b |
| PER-ABR-001 | 听觉脑干反应 | MK.ABR |
| PER-AEP-001 | 听觉诱发电位（纯音/短声） | MK.N1_auditory; MK.P2_auditory |
| PER-BR-001 | 双眼竞争与双稳态知觉 | MK.SSVEP; MK.BOLD_visual_cortex |
| PER-CAT-001 | 视觉物体类别识别 | MK.N170; MK.BOLD_category_selective |
| PER-CUE-001 | Posner 空间线索 | MK.P1_visual; MK.N1_visual |
| PER-FACE-001 | 面孔知觉 | MK.N170; MK.BOLD_category_selective |
| PER-FVEP-001 | 闪光视觉诱发电位 | MK.flash_VEP |
| PER-GATE-001 | 配对短声感觉门控 | MK.P50_gating |
| PER-HBD-001 | 心跳觉察（内感受） | MK.HEP |
| PER-LEP-001 | 激光诱发电位（痛觉） | MK.LEP |
| PER-LG-001 | 局部-全局范式 | MK.MMN; MK.P3b |
| PER-MASK-001 | 掩蔽与阈限知觉 | MK.VAN; MK.P3b |
| PER-MSI-001 | 视听多感觉整合 | MK.AV_interaction_ERP |
| PER-NAT-001 | 自然图像与影片观看 | MK.ISC; MK.BOLD_visual_cortex |
| PER-OLF-001 | 嗅觉诱发电位 | MK.OERP |
| PER-OMIT-001 | 刺激遗漏范式 | MK.omission_response |
| PER-PRVEP-001 | 棋盘格翻转 VEP | MK.P100_PRVEP |
| PER-RET-001 | 视网膜拓扑映射 | MK.BOLD_visual_cortex |
| PER-TACT-001 | 触觉空间注意 | MK.N140_somatosensory; MK.P3b |
| PER-TON-001 | 音调拓扑映射 | MK.BOLD_auditory_cortex |
| PER-VS-001 | 视觉搜索 | MK.N2pc |
| PER-AMASK-001 | 听觉掩蔽 | MK.N1_auditory; MK.MMN |
| PER-BOI-001 | 身体拥有错觉（橡胶手） | MK.BOLD_premotor_parietal |
| PER-CTXC-001 | 情境线索效应 | MK.N2pc; MK.BOLD_hippocampus |
| PER-MOT-001 | 多目标追踪 | MK.CDA; MK.BOLD_frontoparietal |
| PER-NAVON-001 | Navon 全局-局部 | MK.N2_posterior; MK.P3b |
| SSR-ASSR-001 | 听觉稳态响应 | MK.ASSR |
| SSR-CVEP-001 | 编码调制视觉诱发电位 | MK.cVEP |
| SSR-SSMVEP-001 | 稳态运动视觉诱发电位 | MK.SSMVEP |
| SSR-SSSEP-001 | 稳态体感诱发电位 | MK.SSSEP |
| SSR-SSVEP-001 | 稳态视觉诱发电位 | MK.SSVEP |
| SSR-BEAT-001 | 节律与节拍跟随 | MK.SSEP_beat |
| SSR-FFR-001 | 频率跟随响应 | MK.FFR |
| SSR-FPVS-001 | 快速周期视觉刺激（频率标记） | MK.FPVS_oddball |
| SSR-SWEEP-001 | 扫描 VEP（视敏度评估） | MK.SSVEP |

## 需要写成变体的被并入候选

| 被并入候选 | 来源包 | 目标范式 | 决议 |
|---|---|---|---|
| PER-RSVP-001 快速序列视觉呈现 | A | PER-ODD-001 | D-011 |
| SSR-FT-001 多目标频率标记注意 | A | SSR-SSVEP-001 | D-003 |
| SSR-PD-001 闪光光驱动 | A | SSR-SSVEP-001 | D-002 |
| SSR-SSVEPHF-001 高频/不可见 SSVEP | A | SSR-SSVEP-001 | D-004 |
| LAN-PHON-001 音位辨别 | D | PER-MMN-001 | D-017 |

## 本包不建条目的候选

| 候选 | 判定 | 决议 |
|---|---|---|
| PER-RSVP-001 快速序列视觉呈现 | 并入 PER-ODD-001 | D-011 |
| PER-UFOV-001 有效视野 | 暂缓 | D-023 |
| SSR-FT-001 多目标频率标记注意 | 并入 SSR-SSVEP-001 | D-003 |
| SSR-PD-001 闪光光驱动 | 并入 SSR-SSVEP-001 | D-002 |
| SSR-SSVEPHF-001 高频/不可见 SSVEP | 并入 SSR-SSVEP-001 | D-004 |

## 本包负责编写的标记物

| 标记物 | 名称 | 类型 | 使用范式 |
|---|---|---|---|
| `MK.ABR` | 听觉脑干反应（I-V 波） | erp_component | PER-ABR-001 |
| `MK.alpha_lateralization` | 后部 α 偏侧化 | oscillatory | PER-CVA-001; MEM-RC-001 |
| `MK.ASSR` | 听觉稳态响应 | steady_state | SSR-ASSR-001 |
| `MK.AV_interaction_ERP` | 早期视听交互 ERP | erp_component | PER-MSI-001 |
| `MK.BOLD_auditory_cortex` | 听皮层 BOLD 响应 | hemodynamic | PER-TON-001; IMG-AUD-001 |
| `MK.BOLD_category_selective` | 腹侧视觉皮层类别选择性 BOLD（FFA、PPA 等） | hemodynamic | PER-CAT-001; PER-FACE-001; IMG-VIS-001; MEM-CFMT-001 |
| `MK.BOLD_frontoparietal` | 额顶网络 BOLD | hemodynamic | PER-MOT-001; IMG-ROT-001; CTL-RAVEN-001; MEM-NBK-001; MEM-SWM-001 |
| `MK.BOLD_hippocampus` | 海马 BOLD 响应 | hemodynamic | PER-CTXC-001; MEM-NAV-001; MEM-PA-001; MEM-SME-001; MEM-TNT-001; MEM-MST-001 |
| `MK.BOLD_premotor_parietal` | 前运动-顶叶 BOLD（动作观察/身体表征） | hemodynamic | PER-BOI-001; MOT-OBS-001 |
| `MK.BOLD_visual_cortex` | 视皮层 BOLD 响应 | hemodynamic | PER-BR-001; PER-NAT-001; PER-RET-001; IMG-VIS-001 |
| `MK.CDA` | 对侧延迟活动 | erp_component | PER-MOT-001; MEM-CD-001; MEM-SWM-001 |
| `MK.cVEP` | 编码调制视觉诱发电位 | steady_state | SSR-CVEP-001 |
| `MK.FFR` | 频率跟随响应 | steady_state | SSR-FFR-001 |
| `MK.flash_VEP` | 闪光视觉诱发电位 | erp_component | PER-FVEP-001 |
| `MK.FPVS_oddball` | 快速周期视觉刺激 oddball 频率响应 | steady_state | SSR-FPVS-001 |
| `MK.HEP` | 心跳诱发电位 | erp_component | PER-HBD-001 |
| `MK.ISC` | 被试间相关 | connectivity | PER-NAT-001; STA-ENG-001 |
| `MK.LEP` | 激光诱发电位（N2-P2） | erp_component | PER-LEP-001 |
| `MK.MMN` | 失匹配负波 | erp_component | PER-MMN-001; PER-LG-001; PER-AMASK-001; LAN-PHA-001 |
| `MK.mVEP` | 运动起始视觉诱发电位（N2） | erp_component | PER-MVEP-001 |
| `MK.N140_somatosensory` | 体感 N140 | erp_component | PER-TACT-001 |
| `MK.N170` | N170（M170） | erp_component | PER-CAT-001; PER-FACE-001; MEM-CFMT-001; EMO-FACE-001; SOC-BIO-001; SOC-GAZE-001; SOC-SELF-001 |
| `MK.N1_auditory` | 听觉 N1（N100） | erp_component | PER-AAD-001; PER-AEP-001; PER-AMASK-001; MOT-IB-001 |
| `MK.N1_visual` | 视觉 N1 | erp_component | PER-CUE-001; CTL-ANT-001 |
| `MK.N2_posterior` | 后部 N2（N2c、枕颞 N2） | erp_component | PER-NAVON-001; SOC-BIO-001 |
| `MK.N2pc` | N2pc | erp_component | PER-VS-001; PER-CTXC-001; EMO-DOT-001 |
| `MK.OERP` | 嗅觉事件相关电位 | erp_component | PER-OLF-001 |
| `MK.omission_response` | 刺激遗漏响应 | erp_component | PER-OMIT-001 |
| `MK.P100_PRVEP` | 图形翻转 VEP P100 | erp_component | PER-PRVEP-001 |
| `MK.P1_visual` | 视觉 P1 | erp_component | PER-CUE-001; EMO-DOT-001; SOC-GAZE-001 |
| `MK.P2_auditory` | 听觉 P2（P200） | erp_component | PER-AEP-001; EMO-SOUND-001 |
| `MK.P3a` | P3a | erp_component | PER-ODD-001 |
| `MK.P3b` | P3b（P300） | erp_component | PER-ODD-001; PER-AB-001; PER-LG-001; PER-MASK-001; PER-TACT-001; PER-NAVON-001; CTL-ANT-001; CTL-CPT-001; CTL-DT-001; CTL-WCST-001; MEM-NBK-001; SOC-CYB-001; SOC-SELF-001; STA-MW-001 |
| `MK.P50_gating` | P50 感觉门控 | erp_component | PER-GATE-001 |
| `MK.speech_envelope_tracking` | 皮层语音包络跟踪 | oscillatory | PER-AAD-001; LAN-NAT-001 |
| `MK.SSEP_beat` | 节拍相关稳态诱发电位 | steady_state | SSR-BEAT-001 |
| `MK.SSMVEP` | 稳态运动视觉诱发电位 | steady_state | SSR-SSMVEP-001 |
| `MK.SSSEP` | 稳态体感诱发电位 | steady_state | SSR-SSSEP-001 |
| `MK.SSVEP` | 稳态视觉诱发电位 | steady_state | PER-BR-001; SSR-SSVEP-001; SSR-SWEEP-001 |
| `MK.VAN` | 视觉觉知负波 | erp_component | PER-MASK-001 |
