# 工作日志 · 包 B 运动、想象与刺激 · sprint 2

> 每次工作追加一节（最新在下）。写：写了哪些 `protocol`、拆出了哪些具体范式（对应 `split_log.csv` 行）、保留了哪些变体及理由、`class_updates.yaml` 的改动、遇到的问题、待例会事项、跨包交接。

<!-- 模板
## YYYY-MM-DD · <策展人>
- protocol：
- 拆分 / 保留：
- class_updates：
- 核对线索：
- 问题 / 待例会：
- 交接给其他包：
-->

## 2026-10-03 · curator_b
- **protocol**：49 个 `-001` 全部加了 `protocol`（n_classes/classes/cue/stimulus_coding/paradigm_timing/feedback/distinguishing），`distinguishing` 以“Standard configuration (earliest published) / 标准配置（最早发表）”开头并列出兄弟协议。收窄到标准配置（描述、`trial_structure`、`datasets`、别名）的：MOT-MI-001、MOT-ME-001、MOT-ATT-001、MOT-CURSOR-001、MOT-GRASP-001、MOT-MRCP-001、MOT-SACC-001、MOT-TRACK-001、IMG-AUD-001、IMG-CMD-001、IMG-SAO-001、IMG-SPI-001、IMG-VIS-001。
- **拆分**：具体范式 49 → 84（新建 35 个文件，见 `split_log.csv`）。MOT-MI 001–011；MOT-ME 001–005；MOT-ATT、MOT-CURSOR、MOT-MRCP、IMG-CMD、IMG-SPI 各 001–003；MOT-GRASP 001–004；MOT-HW、MOT-REACH、MOT-SACC、MOT-TRACK、IMG-AUD、IMG-MA、IMG-SAO、IMG-VIS 各 001–002；其余 33 个范式类只有 `-001`（没有第二个有出处的配置，不硬拆）。
- **变体复核**（README 表中 8 条）：7 条拆为新具体范式——MOT-ME 单指 → -002（准则 1），行走 → -003（1;3），节律敲击 → -004（2;3）；MOT-MI 下肢/足部 → -004（1）；IMG-AUD 音乐想象 → -002（1;2）；IMG-CMD 床旁脑电 → -002（1;2;3）；IMG-VIS 类别特异 → -002（1）。IMG-CMD“空间导航想象”是 Owen 2006 标准配置类别集的一部分，已从 `variants` 删去并写入 -001 的 `protocol.classes`；“只用导航想象”的配置记为“提议”。本包现无保留的参数级变体（无 `Hybrid:` 变体）。
- **MOT-MI 与 D-057 示例的差异**：示例中 MOT-MI-003 写“单侧上肢 11 类（肘屈伸、前臂旋前/旋后、手抓握/张开）”，但这组动作是 Ofner et al. 2017（6 动作 + 休息 = 7 类，MOABB Ofner2017），11 类是 Jeong et al. 2020（GigaScience，任务未在所见页面列出）。按所见出处：MOT-MI-003 = Ofner 2017，MOT-MI-011 = Jeong 2020（classes 待补）。请维护者确认。
- **class_updates**：10 条 modify（MOT-MI、MOT-ME、MOT-ATT、MOT-HW 改名为“书写（尝试或实际执行）”、MOT-MRCP 改名与泛化、MOT-GRASP、MOT-REACH、MOT-SACC、MOT-CURSOR、IMG-CMD）：描述泛化、标记物并集、别名。无新范式类。
- **核对线索**：沿用 R 编号线索；sprint 2 检索 7 次 WebSearch（上限 12）、23 次 WebFetch（见 `search_log.md`，新线索 S2B-L01…L17 待分配 R 编号）。PMC 页面返回 reCAPTCHA，未重试。
- **TBD first_source**（5 个，D-032 写法）：MOT-MI-005（Graz 连续反馈，已知数据集文献 doi 10.1109/TNSRE.2007.906956）、MOT-MI-006（BNCI2003_004）、MOT-MI-009（BCI Competition IV ds1）、MOT-ME-003（行走）、MOT-REACH-002（BCI Competition IV ds3）。另有多个新文件以“所见最早文献”作 first_source、notes 注明“origin not established”。
- **问题 / 待例会**：
  1. IMG-MA：MOABB 两页对 BNCI2015_004 的类别列表不一致；若 Keirn & Aunon 1990（R0842）原始配置是五任务，-001/-002 的角色需对调（序号不变，改内容）。
  2. 若干 protocol 字段来自现有文件描述或文献标题，未对照原文（notes 中标“to be checked”）：MOT-ATT-001/-002、MOT-GRASP-001/-002（手势名为占位）/-004、MOT-HW-001、IMG-SPI-001/-002、IMG-CMD-002、MOT-FORCE-001（反馈方式未填）。
  3. MOT-TRACK-001 的 first_source（R0889）可能是 3-D 中心外伸运动而非追踪，若是应移入 MOT-REACH。
  4. MOT-HW-002（健康被试实际书写）是否留在 MOT-HW（需按 class_updates 改名）还是归 MOT-ME。
  5. MOT-MI-004 的外骨骼行走 MI 数据库类别集未核对，可能需单独给号。
- **交接给其他包**：MOT-SACC-002 用到 A 包标记物 MK.BOLD_frontoparietal；MOT-ATT-002 与 IMG-CMD-002 交叉（DoC 指令跟随，均为 B 包）。
- **校验**：`python3 scripts/validate.py` 0 problem(s)；本包三个族 0 条“no protocol”警告。
