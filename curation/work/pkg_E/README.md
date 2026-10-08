# 包 E：情绪、社会与脑状态 · 工作目录

- 范式族：`emotion`、`social`、`state`
- 任务单：[`curation/packages/pkg_E_情绪、社会与脑状态.md`](../../packages/pkg_E_情绪、社会与脑状态.md)
- 候选 43 个：收录 39、并入 3、排除 0、暂缓 1（判定见 [`curation/decisions.md`](../../decisions.md)）
- 本包负责编写的标记物：14 个（`curation/registry/markers.csv` 中 `owner_pkg = E`）

## 写入范围（D-029）

你**只能**新增或修改以下文件：

1. `paradigms/emotion/*`、`paradigms/social/*`、`paradigms/state/*`；
2. `knowledge/markers/` 中 `owner_pkg = E` 的标记物文件（下表），以及你在本包 `marker_requests.csv` 中申请、且登记表中**不存在**同义项的新标记物文件（用清晰的规范 ID，如 `MK.N2pc`，不要用 `MK.new1`）；
3. `curation/work/pkg_E/*`（本目录）。

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
- 本包标记物都已有维护者建的骨架文件（`description` 为"待包 E 编写。"），直接覆盖；4 个种子标记物文件（P3a、P3b、SMR_ERD、SSVEP）已有内容，只做补充。
- 被并入的候选不建文件，写成目标范式的 `variants`（D-030）；混合 BCI、超扫描变体分别以 `Hybrid:`、`Hyperscanning:` 开头（D-022、D-021）。
- 一个 PR 只放一个范式及其首次用到的标记物；本地 `python scripts/validate.py` 0 问题后再提交。
- 查不到的就空着，不要猜；所有出处 `verified: false`，由审核人核实。

## 本包收录范式与必须使用的标记物

| ID | 范式 | 标记物 |
|---|---|---|
| EMO-FILM-001 | 情绪影片诱发 | MK.frontal_alpha_asymmetry; MK.affective_band_power |
| EMO-AUTO-001 | 自传体回忆情绪诱发 | MK.affective_band_power; MK.BOLD_amygdala |
| EMO-DOT-001 | 点探测注意偏向 | MK.N2pc; MK.P1_visual |
| EMO-EST-001 | 情绪 Stroop | MK.LPP; MK.N2_frontocentral |
| EMO-FACE-001 | 情绪面孔 | MK.N170; MK.EPN; MK.BOLD_amygdala |
| EMO-FC-001 | 恐惧条件化 | MK.BOLD_amygdala |
| EMO-IAPS-001 | 情绪图片观看 | MK.LPP; MK.EPN; MK.BOLD_amygdala |
| EMO-MID-001 | 金钱激励延迟任务 | MK.BOLD_striatum_reward; MK.FRN |
| EMO-REG-001 | 情绪调节（认知重评） | MK.LPP |
| EMO-SOUND-001 | 情绪声音与语音韵律 | MK.P2_auditory; MK.LPP |
| EMO-STRESS-001 | 社会应激任务 | MK.frontal_alpha_asymmetry; MK.HbO_prefrontal |
| EMO-APRIME-001 | 情感启动 | MK.N400; MK.LPP |
| SOC-BIO-001 | 生物运动知觉 | MK.N170; MK.N2_posterior; MK.BOLD_pSTS |
| SOC-CYB-001 | 社会排斥（Cyberball） | MK.P3b; MK.BOLD_dACC |
| SOC-GAZE-001 | 目光跟随与共同注意 | MK.N170; MK.P1_visual; MK.BOLD_pSTS |
| SOC-JA-001 | 联合动作 | MK.SMR_ERD; MK.interbrain_synchrony |
| SOC-PAIN-001 | 疼痛共情 | MK.LPP; MK.BOLD_anterior_insula |
| SOC-TOM-001 | 心理理论（错误信念） | MK.BOLD_TPJ |
| SOC-TRUST-001 | 信任博弈与囚徒困境 | MK.FRN; MK.BOLD_striatum_reward |
| SOC-UG-001 | 最后通牒博弈 | MK.FRN; MK.BOLD_anterior_insula |
| SOC-DICT-001 | 独裁者博弈 | MK.BOLD_vmPFC_value |
| SOC-IAT-001 | 内隐联想测验 | MK.N400; MK.LPP |
| SOC-IMIT-001 | 模仿抑制 | MK.SMR_ERD; MK.BOLD_TPJ |
| SOC-RME-001 | 眼中读心 | MK.BOLD_TPJ; MK.BOLD_mPFC |
| SOC-SELF-001 | 自我面孔识别 | MK.N170; MK.P3b |
| SOC-TPP-001 | 第三方惩罚 | MK.BOLD_dlPFC |
| SOC-VPT-001 | 视觉观点采择 | MK.BOLD_TPJ; MK.alpha_posterior |
| SOC-WIT-001 | 武器识别 | MK.P2_visual; MK.N2_frontocentral |
| STA-DRV-001 | 模拟驾驶与持续警觉 | MK.alpha_posterior; MK.theta_drowsiness |
| STA-MATB-001 | 多任务认知负荷（MATB） | MK.frontal_midline_theta; MK.alpha_posterior; MK.HbO_prefrontal |
| STA-REST-001 | 静息态（睁眼/闭眼） | MK.alpha_posterior; MK.DMN_connectivity |
| STA-SCP-001 | 慢皮层电位自我调节 | MK.SCP |
| STA-ANES-001 | 麻醉与意识水平 | MK.slow_wave; MK.frontal_alpha_anesthesia |
| STA-ENG-001 | 投入度与视频学习 | MK.ISC; MK.alpha_posterior |
| STA-MED-001 | 冥想 | MK.alpha_posterior; MK.frontal_midline_theta |
| STA-MW-001 | 走神（思维漫游） | MK.alpha_posterior; MK.P3b; MK.DMN_connectivity |
| STA-NF-001 | 神经反馈训练 | MK.SMR_ERD; MK.alpha_posterior |
| STA-PVT-001 | 精神运动警觉任务 | MK.alpha_posterior; MK.theta_drowsiness |
| STA-SLP-001 | 睡眠分期 | MK.sleep_spindle; MK.slow_wave |

## 需要写成变体的被并入候选

| 被并入候选 | 来源包 | 目标范式 | 决议 |
|---|---|---|---|
| EMO-MUS-001 音乐/音乐视频情绪诱发 | E | EMO-FILM-001 | D-018 |
| SOC-HYP-001 超扫描协作 | E | SOC-JA-001 | D-021 |
| SOC-SID-001 社会激励延迟 | E | EMO-MID-001 | D-025 |

## 本包不建条目的候选

| 候选 | 判定 | 决议 |
|---|---|---|
| EMO-MUS-001 音乐/音乐视频情绪诱发 | 并入 EMO-FILM-001 | D-018 |
| SOC-HYP-001 超扫描协作 | 并入 SOC-JA-001 | D-021 |
| SOC-SID-001 社会激励延迟 | 并入 EMO-MID-001 | D-025 |
| STA-HYB-001 混合 BCI（多范式组合） | 暂缓 | D-022 |

## 本包负责编写的标记物

| 标记物 | 名称 | 类型 | 使用范式 |
|---|---|---|---|
| `MK.affective_band_power` | 情绪相关频段功率模式 | oscillatory | EMO-FILM-001; EMO-AUTO-001 |
| `MK.BOLD_amygdala` | 杏仁核 BOLD 响应 | hemodynamic | EMO-AUTO-001; EMO-FACE-001; EMO-FC-001; EMO-IAPS-001 |
| `MK.BOLD_anterior_insula` | 前岛叶 BOLD | hemodynamic | SOC-PAIN-001; SOC-UG-001 |
| `MK.BOLD_pSTS` | 后颞上沟 BOLD | hemodynamic | SOC-BIO-001; SOC-GAZE-001 |
| `MK.BOLD_TPJ` | 颞顶联合区 BOLD | hemodynamic | SOC-TOM-001; SOC-IMIT-001; SOC-RME-001; SOC-VPT-001 |
| `MK.DMN_connectivity` | 默认模式网络连接 | connectivity | STA-REST-001; STA-MW-001 |
| `MK.EPN` | 早期后部负波 | erp_component | EMO-FACE-001; EMO-IAPS-001 |
| `MK.frontal_alpha_anesthesia` | 麻醉相关额区 α | oscillatory | STA-ANES-001 |
| `MK.frontal_alpha_asymmetry` | 额叶 α 不对称 | oscillatory | EMO-FILM-001; EMO-STRESS-001 |
| `MK.interbrain_synchrony` | 脑间同步 | connectivity | SOC-JA-001 |
| `MK.LPP` | 晚期正电位 | erp_component | EMO-EST-001; EMO-IAPS-001; EMO-REG-001; EMO-SOUND-001; EMO-APRIME-001; SOC-PAIN-001; SOC-IAT-001 |
| `MK.P2_visual` | 视觉 P2 | erp_component | SOC-WIT-001 |
| `MK.SCP` | 慢皮层电位 | erp_component | STA-SCP-001 |
| `MK.theta_drowsiness` | 困倦相关 θ 功率升高 | oscillatory | STA-DRV-001; STA-PVT-001 |
