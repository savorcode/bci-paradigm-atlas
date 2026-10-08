# 工作日志 · 包 C 错误监测与认知控制 · sprint 2

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

## 2026-10-03 · curator_c

- **protocol**：本包 52 个 `-001` 全部补写 `protocol`（`distinguishing` 均写"标准配置"及出处线索编号），并补 `trial_structure.conditions`（只写条件名，不写时长/试次数，原文未读）。校验 0 错误、本包 0 条"no protocol"警告。
- **拆分 / 新建**：具体范式 52 → 73（新建 21 个文件），见 `split_log.csv`：
  - ERR-ERRP（P1 核心）：-002 监视型（BNCI 013-2015）、-003 P300 拼写器反馈错误（BCI Challenge @ NER 2015，源头 TBD）、-004 连续反馈（Spüler & Niethammer 2015）；-001 收窄为离散指令交互。
  - ERR-OBS（P1 核心）：-002 观察 Go/NoGo、-003 VR 化身动作错误（均据 R0714 引文，完整书目未见）；-001 收窄为观察他人选择任务。
  - ERR-AWARE：-002 反向眼跳（原 variants 唯一一条，D-015 复核，准则 2）、-003 EAT（Hester et al. 2005）。
  - ERR-GAM：-002 doors task（源头 TBD）、-003 被动老虎机；ERR-ADAPT-002 奖赏型伸手学习（准则 4）；ERR-CHGPT-002 oddball 条件（准则 1）；ERR-TS-002 Kool 2016 确定性转移。
  - CTL-FLK-002 箭头版（ERP CORE 数据集移入，刺激类型待核对）；CTL-SIM-002 视觉版；CTL-STR-002 单试次计算机化；CTL-SW-002 线索切换、-003 自主切换；CTL-CPT-002 AX-CPT、-003 gradCPT；CTL-ANT-002 ANT-I；CTL-PDM-002 连续监视随机点。
  - -001 被收窄并改名：ERR-AWARE、ERR-CHGPT、ERR-ERRP、ERR-OBS、CTL-CPT（原名"AX-CPT"→ X-CPT）、CTL-FLK、CTL-PDM、CTL-SIM、CTL-STR、CTL-SW；别名随配置迁移（如 "Cued task switching" → CTL-SW-002，"ANT-I" → CTL-ANT-002，"EAT" → ERR-AWARE-003）。
- **保留为变体 / 新增变体**：ERR-VRPE-001 新增 EMS 力反馈条件（R1258，待例会）；CTL-AS-001 新增国际标准化协议（R0566，参数级）。
- **只记提议、未建文件**（证据不足或缺标记物线索）：ERR-TS Gläscher 2010、CTL-STR 计数 Stroop、CTL-ANT ANT-R、CTL-CPT Conners not-X、CTL-GNG 线索 Go/NoGo。未拆分但讨论过：CTL-BART Rao 2008 主动/被动（仅 1 篇）、CTL-EFF 认知努力折扣、CTL-TOL 计算机化/SoC、CTL-WASON 内容条件、CTL-SST 选择性停止（无线索）。
- **class_updates**：12 条 modify（ERR-ERRP、ERR-OBS、ERR-AWARE、ERR-GAM、ERR-ADAPT、ERR-CHGPT、ERR-TS、CTL-CPT、CTL-FLK、CTL-SW、CTL-PDM、CTL-STR）：描述泛化到类、标记物并集（ERR-AWARE +MK.ERN +MK.BOLD_frontoparietal；ERR-ADAPT +MK.P3b；CTL-CPT +MK.DMN_connectivity；CTL-FLK +MK.LRP）、别名；CTL-CPT 类名去掉"AX-CPT"，ERR-ADAPT 类名扩为"运动适应与基于奖赏的运动学习"。无新范式类，无新标记物申请。
- **检索**：WebSearch 7 次（上限 12），WebFetch 26 次，见 `search_log.md`。PubMed 1 次 reCAPTCHA，未重试。
- **请维护者补入 literature.csv 的检索线索**：S_SPULER2015、S_TUEBINGEN_CONTERRP、S_HESTER2005、S_CALLEJAS2004、S_CALLEJAS2005、S_MEIRAN1996、S_SERVANSCHREIBER1996、S_KELLY2013、BNCI 013-2015 的 TNSRE 2010 文献；并更新 R1093 书目（Proudfit 2015, Psychophysiology, 10.1111/psyp.12370）。
- **TBD first_source（新增 6 个）**：ERR-ERRP-003、ERR-GAM-002、CTL-FLK-002、CTL-SIM-002、CTL-STR-002、CTL-SW-003；另有 4 个只见转引/无作者：ERR-ERRP-002（标题未见）、ERR-OBS-002、ERR-OBS-003、ERR-GAM-003（作者年份转引自 R0714），ERR-ADAPT-002（R1001 无作者/年份）。原有 TBD：ERR-AAF-001。
- **问题 / 待例会**：
  1. ERR-OBS 与 ERR-ERRP 的边界：观察机器/光标的错误（R0714 中 Ullsperger 2007、Gentsch 2009）现归 ERR-ERRP-002。
  2. CTL-STR-001（卡片版）沿用类标记物 MK.N450，但 N450 只在单试次版本记录；是否在 -001 去掉标记物需决定（schema 要求 ≥1）。同类问题：ERR-TS-002、CTL-ANT-002 的标记物继承自类，源头为行为学研究。
  3. CTL-CPT-003 用 MK.DMN_connectivity（E 包）近似默认模式网络活动，可能需新标记物。
  4. ERR-VRPE 的 EMS 反馈条件、ERR-ADAPT 终点 vs 连续光标反馈是否构成准则 2/4 的新序号。
  5. CTL-FLK-002：ERP CORE 页面未写刺激类型，"箭头版"依记忆归入。
- **交接**：D-042 若 ERR-AAF 并入 LAN-SIS（包 D），线索 R1259 交包 D 在 LAN-SIS 下给号。ERR-ERRP-003 依附于 P300 拼写器（PER-ODD，包 A），供包 A 在 P300 拼写器具体范式中互相引用。
