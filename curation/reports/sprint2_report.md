# 具体范式拆分冲刺（sprint 2）总结

> 写给：项目负责人。起草：维护者（maintainer），2026-10-03。
> 对应里程碑：M2（`integration` 分支）。
> 详细材料：决议草案 `curation/decisions.md` D-058 – D-071；QA `curation/reports/qa_sprint2.md`；覆盖度 `curation/reports/coverage_M2.md`；具体范式总表 `curation/registry/concrete_paradigms.csv`；检索记录 `curation/search_protocol.md` S-003。

## 一、一句话结论

5 个包按 D-057 把 267 个范式类拆成了 **405 个具体范式**（新增 138 个），每个都有 `protocol` 块和写明给号准则的 `distinguishing`；`validate.py` **0 错误、0 条"无 protocol"警告**，兄弟之间**没有完全相同的配置**。主要问题不是形式，而是**口径**：准则 1 的粒度（同质目标的个数算不算新协议）、准则 3 的范围、刺激模态改变是否算准则 2、行为学最早配置的标记物怎么写。为此起草了 14 条决议（D-058 – D-071），其中 **D-058（准则 1 粒度）、D-061（标记物继承）、D-062（类源头与 -001）、D-063（ID 冻结点）** 需要在 v0.1.0 发布前确认。D-057 的 MI 示例与实际文件不符（MOT-MI-003 实为 Ofner 2017 的 7 类），已勘误，规则未改。

## 二、全局数字

| 项目 | 冲刺前（M2 开始前） | 冲刺后（M2） |
|---|---|---|
| 范式类 | 267 | 267（无新增、无作废；74 条修改） |
| 具体范式 | 267（与类一一对应） | **405**（新增 138；平均每类 1.52 个） |
| 有多个具体范式的范式类 | 0 | **87**（最多：MOT-MI 11、PER-ODD 9、SSR-SSVEP 8、MOT-ME 5） |
| 有 `protocol` 的具体范式 | 0（267 条警告） | **405 / 405** |
| 变体（参数级） | 35（多为配置级） | 10（配置级变体全部复核：拆分或保留） |
| 标记物 | 129 | 129（无新申请；替代标记物 2 处，D-061） |
| 范式–标记物关联 | 417 | 587 |
| 文献线索 | 1,244 | **1,322**（新增 78 条 R1266 – R1343） |
| 范式–文献关联 | 1,271 | 1,626 |
| first_source 为 TBD | 37（具体范式） | **64 / 405**（15.8%）；范式类 36 / 267 |
| 已核实（verified: true）出处 | 0 | 0 |
| 检索 | S-002 | S-003：WebSearch 44 次、WebFetch 92 次，被拒 16 次 |
| 图谱（build_graph） | 674 节点 / 1,111 边 | 812 节点 / 1,437 边 |

`protocol` 分布（覆盖度报告 §8）：试次结构同步 285、组块 69、连续 38、异步 10；反馈无 311、离散 64、连续 18；类别数为 2 的 229 个（57%）。BCI 用途的具体范式集中在 MOT-MI（反馈含连续）、PER-ODD 与 SSR-SSVEP（离散选择反馈）、ERR-ERRP（离散 + 连续）。

## 三、每包拆分结果

| 包 | 范式类 | 具体范式（前 → 后） | 新建 | ≥2 个具体范式的类 | class_updates | 新登记文献 | TBD | WebSearch / WebFetch |
|---|---|---|---|---|---|---|---|---|
| A 感知与稳态 | 59 | 59 → 89 | 30 | 15 | 15 | 21 | 32 | 11 / 27 |
| B 运动、想象与刺激 | 49 | 49 → 84 | 35 | 16 | 10 | 21 | 5 | 7 / 23 |
| C 错误监测与认知控制 | 52 | 52 → 73 | 21 | 14 | 12 | 14 | 7 | 7 / 26 |
| D 记忆与语言 | 53 | 53 → 83 | 30 | 24 | 24 | 7 | 16 | 7 / 8 |
| E 情绪、社会与脑状态 | 54 | 54 → 76 | 22 | 18 | 13 | 15 | 4 | 12 / 8 |
| **合计** | **267** | **267 → 405** | **138** | **87** | **74** | **78** | **64** | **44 / 92** |

各包要点：
- **A**：PER-ODD 拆为 9 个（两刺激、三刺激、行/列拼写器、RSVP 检测、RSVP 拼写、棋盘格、单项闪烁、听觉空间 AMUSE、触觉 P300——后者解决了 sprint 1 的 D-012 阻塞项）；SSR-SSVEP 8 个；c-VEP 按编码方案 3 个。高频/不可见 SSVEP 留作参数级变体（D-004）。TBD 最多（32），主要是 sprint 1 遗留。
- **B**：MOT-MI 拆为 11 个，是全图谱最大的类；MOT-ME 5 个、MOT-GRASP 4 个。不硬拆：33 个类只有 -001。指出 D-057 示例错误（已勘误，D-067）。
- **C**：ERR-ERRP 4 个（离散指令、监视、P300 拼写器反馈、连续反馈）、ERR-OBS 3 个；10 个 -001 收窄并改名（如 CTL-CPT 由"AX-CPT"改为 X-CPT，AX-CPT 成为 -002）。
- **D**：拆分最细（24 个类有兄弟）；MEM-NBK 4 个、LAN-OVS 3 个；9 个待复核变体全部判为配置级。提出标记物继承与刺激模态两个口径问题。
- **E**：EMO-FILM 4 个（离散影片、DEAP、SEED、SEED-IV）；STA-SCP 重排（-001 改为二分类训练，拼写装置移到 -002）；按 D-031 改了 SOC-CYB、EMO-THREAT 的源头。

## 四、拆分示例（P1 核心类）

### 4.1 运动想象 MOT-MI（11 个）

| ID | 具体范式 | 区别（准则） |
|---|---|---|
| MOT-MI-001 | 左/右手二分类，视觉箭头提示，同步，无反馈（Pfurtscheller & Neuper 1997） | 标准配置 |
| MOT-MI-002 | 左手/右手/双脚/舌头四分类（Pfurtscheller et al. 2006；BCI Competition IV 2a） | 1 |
| MOT-MI-003 | 单侧上肢 6 种动作 + 休息共 7 类（Ofner et al. 2017） | 1 |
| MOT-MI-004 | 足部想象脑开关（β 反弹）vs 静息 | 1 |
| MOT-MI-005 | 左/右手 + 连续视觉反馈（Graz，BNCI2014_004；源头 TBD） | 4 |
| MOT-MI-006 | 右手 vs 双脚，无反馈（BNCI2003_004；源头 TBD） | 1 |
| MOT-MI-007 | 右手 vs 双脚 + 连续反馈（Faller et al. 2012） | 1、4 |
| MOT-MI-008 | 左手/右手/双脚三分类（Zhou et al. 2016） | 1 |
| MOT-MI-009 | 异步自定步调 MI，含空闲态（BCI Competition IV ds1；源头 TBD） | 3（及 1） |
| MOT-MI-010 | 双手 vs 双脚 + 休息，屏幕目标提示（BCI2000 / PhysioNet） | 1、2 |
| MOT-MI-011 | 单侧上肢 11 类动作（Jeong et al. 2020；类别名待补） | 1 |

### 4.2 稳态视觉诱发电位 SSR-SSVEP（8 个）

| ID | 具体范式 | 区别（准则） |
|---|---|---|
| SSR-SSVEP-001 | 单一调制光源被动记录（Regan 1966） | 标准配置 |
| SSR-SSVEP-002 | 频率编码多目标 BCI，离散选择反馈（Middendorf et al. 2000） | 1、4 |
| SSR-SSVEP-003 | 临床光驱动（阶梯频率闪光组块） | 1、3 |
| SSR-SSVEP-004 | 并存刺激的频率标记注意（Morgan et al. 1996） | 1、2 |
| SSR-SSVEP-005 | 联合频率–相位调制（JFPM）40 目标拼写器（PNAS 2015） | 2 |
| SSR-SSVEP-006 | JFPM 12 目标（Nakanishi 2015 数据集） | 1 —— **D-058 提议降为 -005 的参数级变体** |
| SSR-SSVEP-007 | 频率编码 + 静息（非控制）类（Kalunga et al. 2016） | 1（D-058 第 3 款：保留） |
| SSR-SSVEP-008 | 异步自定步调 SSVEP，空闲态检测（源头 TBD） | 3 |

### 4.3 P300 / Oddball PER-ODD（9 个）

| ID | 具体范式 | 区别（准则） |
|---|---|---|
| PER-ODD-001 | 两刺激 oddball，计数或按键（Sutton et al. 1965） | 标准配置 |
| PER-ODD-002 | 三刺激 oddball，分离 P3a/P3b（Squires et al. 1975，经 Wikipedia） | 1 |
| PER-ODD-003 | P300 拼写器，行/列矩阵闪烁（Farwell & Donchin 1988） | 1、2、4 |
| PER-ODD-004 | RSVP 靶检测（图像筛查） | 2、3 |
| PER-ODD-005 | RSVP 拼写器，不依赖注视（Acqualagna & Blankertz 2013） | 1、4（vs -004）；2（vs -003） |
| PER-ODD-006 | 棋盘格范式拼写器（Townsend et al. 2010） | 2 |
| PER-ODD-007 | 单项闪烁，六幅图像指令（Hoffmann et al. 2008） | 1、2 |
| PER-ODD-008 | 听觉空间 P300（AMUSE，8 个扬声器；Schreuder et al. 2011） | 2 |
| PER-ODD-009 | 振动触觉 P300（Brouwer & van Erp 2010） | 2 |

## 五、阻塞项

1. **准则 1 的粒度未定**（D-058）：SSR-SSVEP-006 的去留，以及 PER-ODD、SSR-CVEP 中"目标数"的写法，影响 v0.1.0 发布的 ID 集合。
2. **ID 冻结点**（D-063）：STA-SCP-001 已改义、IMG-MA-001/-002 可能需对调，需在 v0.1.0 发布前完成。
3. **源头**：64 个具体范式 TBD（A 32 个最多），另有 23 条新线索带 `qa_flag`（题名占位 10、转引 9、数据集/协议文 3、行为学 1）。PubMed / PMC 仍不可用（验证码），是 TBD 无法消除的主要原因（D-032）。
4. **待核原文的协议字段**：B 的 "to be checked" 字段（D-068）、IMG-MA-002 类别矛盾、ERP CORE 刺激类型（D-069）、AMIGOS 与 LEMON 的归属（D-070）。
5. **protocol 缺项**（不阻塞校验）：`n_classes` 33 个（多为同质目标集，D-058 后可接受）、`feedback` 12 个（11 个 CTL 行为测验）、`classes` 9 个、`paradigm_timing` 3 个。

## 六、待确认决议清单

| 决议 | 内容 | 优先级 |
|---|---|---|
| D-058 | 准则 1：同质目标的个数是参数，异质类别集的任何改变与增删静息/空闲类才是准则 1；SSR-SSVEP-006 降为 -005 变体，-007 保留 | **v0.1.0 发布前** |
| D-059 | 准则 3 涵盖单试次 vs 组块、试次阶段增删、试次间依赖、多阶段/多日设计；distinguishing 写明子项 | 高 |
| D-060 | 刺激（及作为诱发刺激的反馈）的感觉模态改变属准则 2；记录模态不是准则 | 高 |
| D-061 | 标记物写有文献记载者；行为学配置保留类标记物并注明 `marker inherited from class`；替代标记物注明 `stand-in marker`；类标记物 = 并集；schema 0.3 提议 `marker_basis` 字段 | **v0.1.0 发布前** |
| D-062 | 类源头 = 类中最早、书目可识别的配置；-001 不改号；MEM-TMR 类源头改为 2007 气味研究，SSR-SSVEP、STA-SCP 暂不改 | **v0.1.0 发布前** |
| D-063 | sprint 2 新建 ID 在 v0.1.0 发布前可改义/对调，之后冻结；接受 STA-SCP-001 改义 | **v0.1.0 发布前** |
| D-064 | ERR-OBS = 观察他人/第三人称化身的错误；ERR-ERRP = 被试依赖或监视的装置的错误（含观察机器） | 中 |
| D-065 | Etkin 情绪面孔–词冲突任务另立范式类 EMO-ECONF，不作 EMO-EST-002 | 中 |
| D-066 | 新具体范式允许以数据集/综述/所见最早文献为 first_source，但须带 `qa_flag`、不得进入 reviewed | 中 |
| D-067 | D-057 示例勘误（MI-003 = Ofner 2017 7 类；MI-011 = Jeong 2020 11 类），已执行 | 知悉即可 |
| D-068 – D-070 | 包 B、C、E 的待核对项（IMG-MA、MOT-TRACK 源头、MOT-HW 改名、ERP CORE、ERR-VRPE、AMIGOS、LEMON 等） | sprint 3 |
| D-071 | sprint 2 合并与登记记录（已执行） | 知悉即可 |

D-001 – D-056 仍为草案；sprint 1 报告中标为高优先级的 D-031、D-033 – D-036、D-045、D-046 依然有效，D-031（源头 vs 首个神经记录）已被各包在 sprint 2 中按草案执行。

## 七、下一冲刺（sprint 3）建议

1. **例会先定 D-058、D-061 – D-063**，维护者随即执行（SSR-SSVEP-006 降级、标记物短语、MEM-TMR/STA-SCP 的 distinguishing 与类 notes），然后完成里程碑 M2 并合并 `main`（v0.1.0 发布的 ID 集合以此为准）。
2. **集中补源（S-004）**：64 个 TBD 中先做 P1 核心类（MOT-MI-005/-006/-009、SSR-SSVEP-008、ERR-ERRP-003、MEM-NBK-002 等）；核对 23 条带 `qa_flag` 的新线索。需要解决 PubMed / PMC 的访问（机构代理或 Zotero 群组库）。
3. **补 protocol 缺项**并按 D-059 在 distinguishing 中写明准则 3 的子项；把 `check_siblings.py` 与"类标记物 ⊇ 具体范式标记物"检查加入 CI，"无 protocol"警告升级为错误。
4. **新建档**：EMO-ECONF（D-065）、EMO-FILM-005 AMIGOS（D-070）、MEM-SWM-002 偏侧化空间延迟反应（D-061）、各包 split_log 中标"提议"且已有出处的配置（A 7 条、C 5 条、D 12 条等）。
5. **交叉审核**：首批把 P1 核心类的具体范式推进到 `reviewed`（需全部出处核实），作为下一个公开版本（v0.2.x）的质量样板。
6. **schema 0.3 提议**：`marker_basis`（D-061）、`protocol.structure`（D-059）、`first_neural_source`（D-031）一并讨论。
