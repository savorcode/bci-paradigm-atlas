# 具体范式拆分 QA（交叉审核模拟）· sprint 2

> 维护者（maintainer），2026-10-03。范围：合并 5 个包 sprint 2 分支后的 `integration`（405 个具体范式、267 个范式类）。所有出处仍为 `verified: false`，下文"一致"只表示条目、线索表与登记表内部一致，未对照原文。

## 1. 方法

- **抽样**：每包 10 个、共 50 个（占 405 的 12%）。为了侧重本冲刺新建的文件，每包从 sprint 2 新建的具体范式中抽 7 个、从 `-001`（原有文件，本冲刺补写 `protocol`）中抽 3 个（`random.seed(20261003)`，按 ID 排序后抽样）。合计新建 35 个、`-001` 15 个。
- **检查项**（脚本 + 人工）：
  1. **protocol 完整性**：`n_classes`、`classes`、`cue`、`paradigm_timing`、`feedback`、`distinguishing` 是否填写；`n_classes` 与 `classes` 个数一致（`validate.py` 已查）。`stimulus_coding` 只在有编码方案时要求。
  2. **distinguishing 引用准则是否正确**：`-001` 应写"标准配置"；其他具体范式应写准则编号。脚本取 distinguishing 中第一个提到的兄弟 ID（未提到则取 `-001`），比较两者的结构化字段（准则 1 = `n_classes`+`classes`；2 = `cue`+`stimulus_coding`；3 = `paradigm_timing`；4 = `feedback`），列出"引用的准则"与"结构化字段确有差异的准则"；引用了但字段上看不出的标为"仅见于文字"，再人工判断。
  3. **兄弟差异**：`scripts/check_siblings.py` 对**全部** 87 个有多个具体范式的范式类、268 对兄弟做比较（见第 3 节）。
  4. **first_source ↔ 线索**：first_source 的 DOI / PMID / 题名能否在 `literature.csv` 找到，且 `paradigm_literature.csv` 中有该范式的 `first_source_candidate` 关联；TBD 是否写了线索。
  5. **PR 草稿**：`curation/work/pkg_<X>/sprint2/pr/<ID>.md` 是否存在（全量检查）。

## 2. 结果汇总

| 检查项 | 抽样 50 个 | 全量 405 个 |
|---|---|---|
| 有 `protocol` | 50 / 50 | 405 / 405（`validate.py` 0 条"无 protocol"警告） |
| protocol 必填要素齐全 | 43 / 50（QA 中平凡补写 2 个后；原为 41）。缺 `n_classes` 5 个（均为目标数是参数的同质目标集，见 D-058）、缺 `classes` 1 个（IMG-MA-002）、缺 4 项 1 个（CTL-RAVEN-001） | 缺 `n_classes` 33、缺 `classes` 9、缺 `feedback` 12、缺 `paradigm_timing` 3、缺 `cue` 1（覆盖度报告 §8.5） |
| `-001` 写"标准配置" | 15 / 15 | 267 / 267；QA 前有 12 个包 A 的 `-001` 仍写"本类暂无其他具体范式"而实际已有兄弟，**已更正**（PER-ODD-001 另把兄弟列表误写在 `stimulus_coding`，已移回 distinguishing） |
| 新具体范式写明准则编号 | 35 / 35 | 138 / 138 |
| 引用的准则在结构化字段上可见 | 29 / 35；6 个"仅见于文字"：1 个为脚本误报（MOT-MI-006），3 个是准则 3 用于多日/多轮/延迟期结构（MOT-SACC-002、EMO-FC-003、SOC-TRUST-002，`paradigm_timing` 只有 4 个取值，见 D-059），2 个是准则 1 的论据在 classes 中看不出（ERR-GAM-002 待核原文、LAN-SWITCH-002 任务由产出变为理解） | — |
| 兄弟完全相同（4 条准则全同） | 0 | **0 对**（268 对中） |
| 兄弟只在自由文本上不同（需人工确认） | — | 35 对，逐对人工复核后均有实质差异；其中 4 对的依据需例会口径（D-058、D-059），见第 3 节 |
| first_source 与线索一致 | 非 TBD 40 个全部能在 `literature.csv` / `paradigm_literature.csv` 对上（本次补了 97 条 first_source 关联与 220 条 notes 中 R 编号的关联）；其中占位题名/转引 2 个、`qa_flag` 3 个 | — |
| first_source 为 TBD | 10 / 50（9 个写了线索，PER-SPN-001 无线索） | 64 / 405（15.8%）；范式类 36 / 267 |
| 源头存疑 / 书目不完整 | 6 个（PER-MMN-002 无作者；IMG-MA-002、LAN-LOC-002 题名占位；ERR-OBS-003 转引；EMO-THREAT-001 协议文；SOC-NAME-002 所见最早） | 见 D-066 清单 |
| PR 草稿存在 | 50 / 50 | 405 / 405 |
| `verified: true` | 0 | 0 |

**结论**：sprint 2 的拆分在形式上合规：所有具体范式都有 `protocol` 与 `distinguishing`，兄弟之间没有完全相同的配置，PR 草稿齐全，新线索全部登记（R1266 – R1343）。主要问题有三类：(1) **准则 1 的粒度**——同质目标的个数（SSVEP 键盘 12 vs 40、矩阵大小、振动器个数）有时被当作准则 1，有时被当作参数（D-058）；(2) **准则 3 的范围**——多日、多轮、插入延迟期这类结构改变无法用 `paradigm_timing` 表达（D-059）；(3) **源头质量**——新具体范式多以数据集文献或所见最早文献为 first_source，仍有 64 个 TBD（D-066）。都不阻塞里程碑 M2。

## 3. 兄弟差异检查（全部范式类）

`python3 scripts/check_siblings.py`：267 个范式类中 87 个有多个具体范式，共 268 对兄弟。

- **DUPLICATE（4 条准则全同）：0 对。**
- **REVIEW（`n_classes`、`stimulus_coding`、`paradigm_timing`、`feedback` 全同，只在 `classes` / `cue` 的自由文本上不同）：35 对**。逐对阅读后，31 对的差异是实质性的类别集或刺激改变（如 CTL-FLK 字母 vs 箭头、CTL-SIM 听觉 vs 视觉、LAN-CPS 语音 vs 书面、MEM-DS 顺背 vs 倒背、MOT-MI 各类别集）。需例会口径的 4 对：
  - **SOC-TRUST-001 / -003**：类别集、提示、时序、反馈结构化字段全同，区别只是"与同一伙伴多轮互动、结果依赖历史"（distinguishing 引准则 3）。依 D-059 草案保留；若例会认为"轮数"只是参数，-003 降为 -001 的变体。
  - **EMO-FC-001 / -003**：区别是第二天的消退回忆测试（准则 3，多日结构），依 D-059 保留。
  - **ERR-GAM-001 / -002**：-002 的准则 1 论据（-001 中金额是否为因素）待核对原文（D-069）。
  - **STA-SCP-001 / -002**：两者都是负/正二分类 SCP，区别是 -002 把两类映射为字母组的选择/拒绝（拼写装置）。依 D-058"有独立发表的协议且改变输出（逐字符选择）"保留。
- 另外，D-058 草案若确认，**SSR-SSVEP-006**（12 目标 JFPM）与 SSR-SSVEP-005（40 目标 JFPM）只在同质目标个数上不同，应降为 -005 的参数级变体（序号作废不复用）；脚本没有把它列入 REVIEW，因为 -006 的数据集页面未写反馈（`feedback: none`），两者在准则 4 上"不同"只是因为信息缺失。

完整的 35 对见附录 A。

## 4. 已做的平凡修正

- 12 个包 A `-001` 的 distinguishing 去掉过时的"本类暂无其他具体范式（no sibling protocol yet）"，改为列出兄弟 ID：PER-BR、PER-CUE、PER-CVA、PER-HBD、PER-MMN、PER-MSI、PER-MVEP、PER-ODD、PER-OMIT、SSR-ASSR、SSR-FFR、SSR-SSSEP。
- PER-ODD-001：`stimulus_coding` 中误写的兄弟列表移回 distinguishing，删去该字段（两刺激 oddball 无编码方案）。
- SOC-DICT-002 补 `n_classes: 3`、EMO-MID-002 补 `n_classes: 2`（`classes` 已列出）。
- 范式类 MOT-GRASP 补 MK.low_freq_kinematics（MOT-GRASP-003 使用，class_updates 的并集漏了）。
- `paradigm_literature.csv`：97 条 first_source 关联、220 条 notes 中 R 编号的关联（多为新具体范式沿用 `-001` 的线索）；notes 中的临时线索编号替换为 R 编号（25 处）或在检索编号后注明 `[=R….]`（52 处），另 18 个文件在 notes 末尾注明登记的 R 编号。

## 5. 留给 sprint 3 的事项

1. 补 `protocol` 缺项：CTL 族 11 个行为测验的 `feedback`（CTL-RAVEN、CTL-TOL、CTL-WASON 另缺 `paradigm_timing`），MOT-FORCE-001 的 `feedback`，MOT-GRASP-004 的 `cue`，IMG-MA-002 / IMG-SPI-002 / MOT-MI-011 的 `classes`。
2. 依 D-058 统一同质目标集的写法：`n_classes` 写标准配置的目标数，`distinguishing` 不再以目标数作准则 1（PER-ODD-006、SSR-SSVEP-005 的"准则 1：目标数"一句删去）。
3. 依 D-059 在 distinguishing 中写明准则 3 指哪种结构（多日、多轮依赖、插入延迟期、单试次 vs 组块）。
4. D-066 清单中的源头核对；64 个 TBD 集中处理（D-032）。
5. 把 `check_siblings.py` 加入 CI（DUPLICATE 报错，REVIEW 只列出）。

## 6. 逐条结果（抽样 50 个）

| 包 | ID | 新/原有 | protocol 缺项 | distinguishing 引用的准则（脚本比较） | first_source ↔ 线索 | PR 草稿 | 人工发现 | 处理 |
|---|---|---|---|---|---|---|---|---|
| A | PER-AMASK-001 | -001/原有 | — | 标准配置 | TBD（有线索） | 有 | first_source TBD（有线索） | D-032 |
| A | PER-BR-002 | 新 | — | 引 2 vs PER-BR-001；结构化差异 1,2 | TBD（有线索） | 有 | first_source TBD（线索 R0346） | D-032 |
| A | PER-MMN-002 | 新 | — | 引 2 vs PER-MMN-001；结构化差异 1,2 | 对应 R0988 (first_source_candidate) | 有 | first_source 只有题名、无作者/年份 | D-066 |
| A | PER-ODD-003 | 新 | n_classes | 引 1,2,4 vs PER-ODD-001；结构化差异 1,2,4 | 对应 R1052 (first_source_candidate) | 有 | 未写 n_classes（矩阵大小为参数） | D-058：同质目标数为参数，可不写或写标准 6×6=36 |
| A | PER-ODD-004 | 新 | — | 引 2,3 vs PER-ODD-001；结构化差异 1,2,3 | 对应 R0038 (first_source_candidate) | 有 | — | — |
| A | PER-ODD-009 | 新 | n_classes | 引 1,2 vs PER-ODD-001；结构化差异 1,2,4 | 对应 R1284 (first_source_candidate) | 有 | 未写 n_classes（振动器 2/4/6 个为参数） | D-058 |
| A | PER-OLF-001 | -001/原有 | — | 标准配置 | TBD（有线索） | 有 | first_source TBD | D-032 |
| A | PER-SPN-001 | -001/原有 | — | 标准配置 | TBD（无线索） | 有 | first_source TBD，无线索 | D-032 |
| A | SSR-CVEP-002 | 新 | n_classes | 引 2 vs SSR-CVEP-001；结构化差异 1,2 | 对应 R1279 (first_source_candidate) | 有 | 未写 n_classes（目标数为参数） | D-058 |
| A | SSR-SSVEP-008 | 新 | n_classes | 引 3 vs SSR-SSVEP-002；结构化差异 1,2,3 | TBD（有线索） | 有 | 未写 n_classes；first_source TBD（线索 R1280） | D-058、D-032 |
| B | IMG-AUD-002 | 新 | — | 引 1,2 vs IMG-AUD-001；结构化差异 1,2 | 对应 R0186 (first_source_candidate) | 有 | — | — |
| B | IMG-MA-002 | 新 | classes | 引 1 vs IMG-MA-001；结构化差异 1,2 | 对应 R1301 (first_source_candidate) qa:title_placeholder | 有 | 未写 classes：BNCI2015_004 两页类别列表矛盾；源头题名为占位 | D-068 |
| B | IMG-TACT-001 | -001/原有 | — | 标准配置 | 对应 R1124 (first_source_candidate) | 有 | — | — |
| B | MOT-HW-002 | 新 | — | 引 1,4 vs MOT-HW-001；结构化差异 1,2,4 | 对应 R1297 (first_source_candidate) | 有 | —（类改名，D-068 第 4 款） | — |
| B | MOT-ME-005 | 新 | — | 引 1 vs MOT-ME-001；结构化差异 1,2 | 对应 R1288 (first_source_candidate) | 有 | 与 MOT-MI-003 同源（同一研究的执行/想象条件），合理 | — |
| B | MOT-MI-003 | 新 | — | 引 1 vs MOT-MI-001；结构化差异 1,2 | 对应 R1288 (first_source_candidate) | 有 | 与 D-057 示例不符（示例写 11 类），已勘误 | D-067 |
| B | MOT-MI-006 | 新 | — | 引 1,4 vs MOT-MI-001；结构化差异 1,2；4 仅见于文字 | TBD（无线索） | 有 | 脚本误报："准则 4"是相对 MOT-MI-007 而言，正确；first_source TBD | D-032 |
| B | MOT-PASS-001 | -001/原有 | — | 标准配置 | 对应 R1119 (first_source_candidate) | 有 | — | — |
| B | MOT-SACC-002 | 新 | — | 引 2,3 vs MOT-SACC-001；结构化差异 1,2,4；3 仅见于文字 | 对应 R1299 (first_source_candidate) | 有 | 反馈也不同（目标重现 = 离散反馈）但未引准则 4；准则 3 指插入延迟期，paradigm_timing 不反映 | 建议补"准则 4"；D-059 |
| B | STM-SEP-001 | -001/原有 | — | 标准配置 | 对应 R1114 (first_source_candidate) | 有 | — | — |
| C | CTL-CPT-002 | 新 | — | 引 1 vs CTL-CPT-001；结构化差异 1,2 | 对应 R1316 (first_source_candidate) | 有 | — | — |
| C | CTL-CPT-003 | 新 | — | 引 2,3 vs CTL-CPT-001；结构化差异 1,2,3 | 对应 R0575 (first_source_candidate) | 有 | 标记物 MK.DMN_connectivity 为替代项（gradCPT 报告的是 DMN 活动而非连接） | D-061 |
| C | CTL-GNG-001 | -001/原有 | — | 标准配置 | 对应 R0019 (first_source_candidate;key_reference) | 有 | — | — |
| C | CTL-PDM-001 | -001/原有 | — | 标准配置 | 对应 R0102 (first_source_candidate;key_reference) | 有 | — | — |
| C | CTL-PDM-002 | 新 | — | 引 3 vs CTL-PDM-001；结构化差异 1,2,3,4 | 对应 R0578 (first_source_candidate) | 有 | S_KELLY2013 = 已有 R0578，已替换 | — |
| C | CTL-RAVEN-001 | -001/原有 | n_classes,classes,paradigm_timing,feedback | 标准配置 | 对应 R1137 (first_source_candidate) qa:secondhand | 有 | protocol 缺 n_classes、classes、paradigm_timing、feedback（行为测验） | sprint 3 补写 |
| C | CTL-SW-002 | 新 | — | 引 2 vs CTL-SW-001；结构化差异 2 | 对应 R1314 (first_source_candidate) | 有 | — | — |
| C | ERR-ERRP-004 | 新 | — | 引 1,3,4 vs ERR-ERRP-001；结构化差异 1,2,3,4 | 对应 R1308 (first_source_candidate) | 有 | — | — |
| C | ERR-GAM-002 | 新 | — | 引 1,2 vs ERR-GAM-001；结构化差异 2；1 仅见于文字 | TBD（有线索） | 有 | 准则 1 的论据（-001 金额是否为因素）待核对原文；first_source TBD | D-069、D-032 |
| C | ERR-OBS-003 | 新 | — | 引 2 vs ERR-OBS-001；结构化差异 1,2 | 对应 R1320 (占位/转引书目) qa:secondhand | 有 | first_source 为 R0714 中的转引（secondhand）；与 ERR-ERRP 的边界 | D-064、D-066 |
| D | LAN-GEST-001 | -001/原有 | — | 标准配置 | TBD（有线索） | 有 | first_source TBD | D-032 |
| D | LAN-LOC-002 | 新 | — | 引 2 vs LAN-LOC-001；结构化差异 1,2 | 对应 R1328 (占位/转引书目) qa:title_placeholder | 有 | first_source 题名未见（占位） | D-066；准则 2 依 D-060 |
| D | LAN-P600-002 | 新 | — | 引 1 vs LAN-P600-001；结构化差异 1 | 对应 R0864 (first_source_candidate) | 有 | — | — |
| D | LAN-SC-002 | 新 | — | 引 2 vs LAN-SC-001；结构化差异 1,2,3 | 对应 R1223 (first_source_candidate) | 有 | —（模态改变，D-060） | — |
| D | LAN-SL-001 | -001/原有 | — | 标准配置 | 对应 R1166 (first_source_candidate) | 有 | — | — |
| D | LAN-SWITCH-002 | 新 | — | 引 1,2 vs LAN-SWITCH-001；结构化差异 2；1 仅见于文字 | 对应 R1212 (first_source_candidate) | 有 | 准则 1（产出→理解）在 classes 中看不出（两者类别名相同） | 建议 classes 写明任务；可接受 |
| D | MEM-DF-002 | 新 | — | 引 3 vs MEM-DF-001；结构化差异 1,2,3 | TBD（有线索） | 有 | first_source TBD | D-032 |
| D | MEM-MST-002 | 新 | — | 引 1 vs MEM-MST-001；结构化差异 1,2 | 对应 R0416 (first_source_candidate) | 有 | — | — |
| D | MEM-NAV-003 | 新 | — | 引 1,2,4 vs MEM-NAV-001；结构化差异 1,2,4 | TBD（有线索） | 有 | first_source TBD（Astur 1998 未检到） | D-032 |
| D | MEM-SME-001 | -001/原有 | — | 标准配置 | 对应 R1157 (first_source_candidate) | 有 | — | — |
| E | EMO-FC-002 | 新 | n_classes | 引 1 vs EMO-FC-001；结构化差异 1,2 | 对应 R1010 (first_source_candidate) | 有 | 未写 n_classes（梯度刺激个数为参数） | D-058 |
| E | EMO-FC-003 | 新 | — | 引 3 vs EMO-FC-001；结构化差异 1,2；3 仅见于文字 | 对应 R0276 (first_source_candidate) | 有 | 准则 3 指多日（习得—消退—回忆）结构，paradigm_timing 不反映 | D-059 |
| E | EMO-MID-002 | 新 | — | 引 2 vs EMO-MID-001；结构化差异 1,2 | 对应 R0426 (first_source_candidate) | 有 | 未写 n_classes（classes 已列 2 项） | 已补 n_classes: 2（平凡） |
| E | EMO-THREAT-001 | -001/原有 | — | 标准配置 | 对应 R1332 (first_source_candidate) qa:weak_origin | 有 | 源头为 2012 协议文（weak_origin），D-031 处理 | D-066 |
| E | SOC-CYB-001 | -001/原有 | — | 标准配置 | 对应 R1343 (first_source_candidate) qa:behaviour_only | 有 | 源头改为行为学原始研究（behaviour_only），神经研究移入 notes | D-031（已按惯例） |
| E | SOC-DICT-002 | 新 | — | 引 1 vs SOC-DICT-001；结构化差异 1,2 | 对应 R0341 (first_source_candidate) | 有 | 未写 n_classes（classes 已列 3 项） | 已补 n_classes: 3（平凡） |
| E | SOC-GAZE-002 | 新 | — | 引 1,4 vs SOC-GAZE-001；结构化差异 1,2,4 | 对应 R0986 (first_source_candidate) | 有 | — | — |
| E | SOC-NAME-002 | 新 | — | 引 1 vs SOC-NAME-001；结构化差异 1,2,3 | 对应 R1341 (first_source_candidate) | 有 | 源头为所见最早（2009），2008 组研究未确认 | D-066 |
| E | SOC-RACE-001 | -001/原有 | — | 标准配置 | 对应 R1190 (first_source_candidate) | 有 | — | — |
| E | SOC-TRUST-002 | 新 | — | 引 1,3 vs SOC-TRUST-001；结构化差异 1,2；3 仅见于文字 | 对应 R0217 (first_source_candidate) | 有 | 准则 3 指多轮重复，paradigm_timing 不反映 | D-059 |

## 附录 A：REVIEW 兄弟对（check_siblings.py --markdown 输出）

| class | pair | differs in criterion |
|---|---|---|
| CTL-ANT | CTL-ANT-001 / CTL-ANT-002 | 1,2 |
| CTL-FLK | CTL-FLK-001 / CTL-FLK-002 | 1,2 |
| CTL-SIM | CTL-SIM-001 / CTL-SIM-002 | 1,2 |
| CTL-SW | CTL-SW-001 / CTL-SW-002 | 2 |
| CTL-SW | CTL-SW-001 / CTL-SW-003 | 1,2 |
| CTL-SW | CTL-SW-002 / CTL-SW-003 | 1,2 |
| EMO-FC | EMO-FC-001 / EMO-FC-003 | 1,2 |
| EMO-FILM | EMO-FILM-001 / EMO-FILM-002 | 1,2 |
| ERR-AWARE | ERR-AWARE-001 / ERR-AWARE-002 | 1,2 |
| ERR-ERRP | ERR-ERRP-001 / ERR-ERRP-002 | 1,2 |
| ERR-ERRP | ERR-ERRP-001 / ERR-ERRP-003 | 1,2 |
| ERR-ERRP | ERR-ERRP-002 / ERR-ERRP-003 | 1,2 |
| ERR-GAM | ERR-GAM-001 / ERR-GAM-002 | 2 |
| ERR-GAM | ERR-GAM-001 / ERR-GAM-003 | 1,2 |
| ERR-GAM | ERR-GAM-002 / ERR-GAM-003 | 1,2 |
| ERR-OBS | ERR-OBS-001 / ERR-OBS-003 | 1,2 |
| IMG-AUD | IMG-AUD-001 / IMG-AUD-002 | 1,2 |
| IMG-VIS | IMG-VIS-001 / IMG-VIS-002 | 1,2 |
| LAN-CPS | LAN-CPS-001 / LAN-CPS-002 | 1,2 |
| LAN-LOC | LAN-LOC-001 / LAN-LOC-002 | 1,2 |
| LAN-P600 | LAN-P600-001 / LAN-P600-002 | 1 |
| LAN-SWITCH | LAN-SWITCH-001 / LAN-SWITCH-002 | 2 |
| MEM-DS | MEM-DS-001 / MEM-DS-002 | 1,2 |
| MEM-MST | MEM-MST-001 / MEM-MST-002 | 1,2 |
| MEM-PA | MEM-PA-001 / MEM-PA-002 | 1,2 |
| MOT-GRASP | MOT-GRASP-001 / MOT-GRASP-004 | 1,2 |
| MOT-MI | MOT-MI-001 / MOT-MI-004 | 1,2 |
| MOT-MI | MOT-MI-001 / MOT-MI-006 | 1,2 |
| MOT-MI | MOT-MI-004 / MOT-MI-006 | 1 |
| MOT-MI | MOT-MI-005 / MOT-MI-007 | 1,2 |
| MOT-MI | MOT-MI-008 / MOT-MI-010 | 1,2 |
| SOC-TRUST | SOC-TRUST-001 / SOC-TRUST-002 | 1,2 |
| SOC-TRUST | SOC-TRUST-001 / SOC-TRUST-003 | 2 |
| SOC-TRUST | SOC-TRUST-002 / SOC-TRUST-003 | 1,2 |
| STA-SCP | STA-SCP-001 / STA-SCP-002 | 1,2 |
