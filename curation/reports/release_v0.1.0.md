# v0.1.0 发布说明

> 写给：项目负责人、全体策展人与外部读者。起草：维护者（maintainer），2026-10-08。
> v0.1.0 是继 v0.0.1（2026-10-01，初始发布）之后的第一个功能版本。
> 配套材料：`CHANGELOG.md` [0.1.0]；覆盖度 `curation/reports/coverage_v0.1.0.md`；Excel 总览 `curation/reports/BCI范式图谱_v0.1.0_总览.xlsx`；核实报告 `curation/reports/verification_sprint3.md`；决议 `curation/decisions.md`（D-031 – D-074）。

## 一、一句话

v0.1.0 把 v0.0.1 的 3 个种子范式扩展为覆盖 12 个范式族的完整图谱：**267 个范式类、405 个具体范式（404 有效 + 1 作废）、129 个神经标记物**，采用**两级范式标识符**（范式类 / 具体范式），每个具体范式都有 **`protocol` 块**（类别集、提示/编码、试次结构、反馈方式与给号依据）；全部 **682 条出处已完成书目核实**（Crossref / OpenAlex），但**内容核实（读原文）尚未做**，所有条目仍为 `draft`、`verified: false`。

## 二、本版内容

| 项目 | 数量 |
|---|---|
| 范式类（`paradigms/_classes.yaml`） | **267**（12 个族） |
| 具体范式文件 | **405**（**404 有效** + 1 作废：SSR-SSVEP-006，D-058） |
| 有 `protocol` 的具体范式 | 404 / 404 |
| 有多个具体范式的范式类 | 87（最多：MOT-MI 11 个、PER-ODD 9 个、SSR-SSVEP 7 个有效） |
| 参数级变体 | 11 |
| 神经标记物 | **129**（全部有描述） |
| 范式–标记物关联（具体范式层） | 586 |
| 图谱（`dist/graph.json`） | 811 节点 / 1,435 边 |
| 候选（`curation/candidates.csv`） | 294 |
| 文献线索（`curation/literature.csv`） | **1,322**（58 行带 `qa_flag`） |
| 范式–文献关联 | 1,626 |
| 出处书目核实（`curation/verification/sources_check.csv`） | **682 条**：一致 168、更正 379、TBD 找到候选 88、TBD 仍开放 12、查不到 35、指向另一篇 0 |
| first_source 为 TBD | 具体范式 **9**、范式类 **3** |
| 出处已做内容核实（`verified: true`） | **0** |
| 校验（`validate.py`） | 0 错误、0 警告 |
| 兄弟检查（`check_siblings.py`） | 261 对；0 对完全相同，35 对待人工复核 |

## 三、本版口径（已确认的决议要点）

- **D-057 两级标识符**（负责人确认）：范式类 `<族>-<简称>` 记录共同机制（标记物、构念、源头）；具体范式 `<族>-<简称>-<序号>` 是一个可复现协议。给号准则 4 条：(1) 类别/条件集；(2) 刺激或提示类型，含编码方案；(3) 试次结构；(4) 反馈方式。参数变化记 `variants`，不给号。序号永久、不复用。
- **D-058 准则 1 的粒度**（专家裁定，负责人授权）：同质、可互换目标集的**目标个数是参数**；异质类别集的身份或数量改变、**加入或去掉静息/空闲类**属准则 1；布局或编码方案改变属准则 2；有独立数据集本身不构成给号理由。SSR-SSVEP-006 据此作废并入 SSR-SSVEP-005 的变体。
- **D-061 具体范式的标记物**：写该配置**有文献记载**的标记物；行为学配置保留类标记物并在 notes 写 `marker inherited from class`（7 个文件），替代标记物写 `stand-in marker`（2 个文件）。不变式：**范式类的标记物 = 具体范式标记物的并集**，`validate.py` 以错误级检查。
- **D-062 范式类源头 vs -001**：范式类 `first_source` = 该类中任一配置最早的、书目可识别的**原始研究**；`-001` = **标准配置（公认）**，不因发现更早配置而改号；指南、综述、只有题名的记录不替换原始研究。
- **D-063 含义冻结**：标识符含义自 **v0.1.0 发布**起冻结，此后只能作废 + 新号。IMG-MA-001/-002 不对调；STA-SCP-001 由"拼写装置"改为"二分类 SCP 训练"的改义被接受（schema 0.1 时的骨架条目从未有过 protocol）。
- **D-072 两级核实**：*书目核实*（引文字段与 Crossref / OpenAlex / PubMed 记录一致）记在 `sources_check.csv` 与 notes 固定短语 `bibliography confirmed|corrected (<API>, <date>)`；只有*内容核实*（读原文确认描述该范式且为最早）才设 `verified: true`。
- **D-073 凭记忆的候选 DOI**：检索接口不可用时允许以审核人回忆的候选 DOI 作查询键，取回记录与条目一致才写入；notes 含 `origin candidate recalled, record confirmed via <API>`（108 条），内容核实前不得标 `verified: true`。
- 仍为草案、待例会：D-001 – D-056（标"已执行"者已落实到文件）、D-059、D-060、D-064 – D-070、D-074。各包已按草案倾向给号，确认与否可能影响少数条目的写法，但不改变已冻结 ID 的含义。

## 四、构建过程

本版在内部按三个里程碑组织，均由五个工作包（A 感知与稳态、B 运动想象与刺激、C 错误监测与认知控制、D 记忆与语言、E 情绪社会与脑状态）并行完成，维护者合并与 QA：

| 里程碑 | 日期 | 内容 | 材料 |
|---|---|---|---|
| M1 | 2026-10-03 | 第一遍骨架：267 个范式文件、129 个标记物描述、85 个新候选、171 条文献线索；决议草案 D-031 – D-056 | `sprint1_report.md`、`qa_sprint1.md`、`coverage_M1.md` |
| M2 | 2026-10-05 | schema 0.2 两级标识符（D-057）；每个范式类拆分为具体范式（新增 138 个），全部写入 `protocol`；决议 D-058 – D-071 | `sprint2_report.md`、`qa_sprint2.md`、`coverage_M2-start.md`、`coverage_M2.md` |
| M3 | 2026-10-07 | 682 条出处书目核实（交叉审核）；TBD 从 64 / 36 降到 9 / 3；决议 D-072 – D-074 | `sprint3_report.md`、`verification_sprint3.md`、`coverage_M3.md` |

发布前另做了显示修正：中文加粗在 CommonMark 渲染器中的定界问题、CSV 加 UTF-8 BOM（Windows 版 Excel 不乱码），并新增 `scripts/build_overview.py` 生成 Excel 总览。

## 五、已知局限

1. **未做内容核实。** `verified: true` 为 0；书目核实只说明"这篇文献存在、书目正确"，不说明它确实描述了该范式且为最早。所有条目 `status: draft`，引用时请注明 draft 与版本号。
2. **仍有 TBD 源头。** 具体范式 9 个、范式类 3 个（清单见覆盖度报告第 3、8.7 节）。
3. **47 行书目核实遗留**（D-074，草案）：not_found 35 行（其中包 C 15 行因接口限流未检查；20 行为手册、指南、技术报告、学位论文、书章或只有题名的转引，无 Crossref 记录）、tbd_open 12 行。
4. **弱出处与协议细节。** `literature.csv` 58 行带 `qa_flag`；部分具体范式以数据集文献、综述或所见最早文献作为 first_source（D-066）；若干协议细节 notes 标 "to be checked"。
5. **兄弟对待复核。** 35 对具体范式只在自由文本上不同，需人工确认差异是真实的准则 1/2 改变；其中 4 对依赖 D-059/D-060 的确认。

## 六、下一版计划（v0.2.x：内容核实）

1. **内容核实**：对照原文核实 first_source，优先 P1 核心类（MOT-MI、PER-ODD、SSR-SSVEP、ERR-ERRP、MEM-NBK、LAN-OVS）的 `-001`；核实后设 `verified: true` 并按 D-033 流转到 `reviewed`；D-073 短语条目优先复查。
2. **处理 D-074 遗留 47 行**：取得机构数据库访问与接口配额后，先做包 C 的 15 行未检查，再做手册 / 指南，最后做 TBD 开放行。
3. **例会确认** D-059、D-060、D-064 – D-070、D-074，并执行相应的文件修改。
4. **schema 0.3 提议**：`protocol.marker_basis`（D-061）、`protocol.structure`（D-059）、`first_neural_source`（D-031）、`source.source_check`（D-072）、`tags`（D-022），以及下一版词表讨论中的 `DBS-LFP`、`interoceptive`、`sleep` 等词条；CI 加 `check_siblings.py`。
5. 同步 `literature.csv` 的书目与 `sources_check.csv`。
