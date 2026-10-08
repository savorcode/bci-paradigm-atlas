# 工作日志 · 维护者（maintainer）

> 每次工作追加一节（最新在下）。

## 2026-10-02 · 第 0 周 · maintainer

**目标**：明天 5 位策展人并行开工前，把判定、标记物登记表、工作目录和仓库基础设施准备好。本次没有做外部检索（检索配额留给策展人 S-002）。

### 1. 例会决议草案（`curation/decisions.md`）
- 起草 D-001 – D-030，覆盖 `decisions_pending.md` 全部事项，另有 2 项维护者补充的并入（D-024 记得/知道 → 新旧再认，D-025 社会激励延迟 → 金钱激励延迟）和 4 条流程决议（D-026 其余候选收录、D-028 标记物登记表、D-029 写入范围、D-030 并入的处理方式）。
- 判定基准统一按方法说明 §1："标记物与构念都不变"才算变体。
- 主要结果：7 项建议并入全部同意；2 项建议排除全部排除；11 项独立性问题中 5 项并入（RSVP → Oddball、下肢想象 → MI、音位辨别 → MMN、音乐情绪 → 影片情绪、超扫描 → 联合动作），其余独立；不新增 hybrid 族，STA-HYB-001 暂缓，混合系统写成组成范式中以 `Hybrid:` 开头的变体；心算留在 imagery；行为为主任务按统一口径暂缓 4 项（UFOV、DSST、TMT、OSPAN），排除自定步速阅读，收录瑞文推理和数字广度。
- `candidates.csv`：`decision` 改为 收录 / 并入 <ID> / 排除 / 暂缓，新增 `decision_ref` 列；非收录候选的 `status` 改为"不建条目（作为变体）""不建条目（排除）""暂缓"，防止被认领。结果：收录 187、并入 14、排除 3、暂缓 5。
- `decisions_pending.md` 顶部加了指向 decisions.md 的说明，原文保留。

### 2. 标记物登记表（`curation/registry/`）
- 从 187 个收录候选的 `likely_markers` 归并出 **111 个规范标记物**（保留原有 4 个 ID），`markers.csv` 列出类型、记录模态、owner 包、使用范式和归并说明；`paradigm_markers.csv` 给出每个收录范式必须使用的标记物。
- 归并原则见 D-028：同义词归一（P300 → P3b，mu 抑制 → SMR_ERD，RewP/MFN → FRN 等）；血流动力学标记物按脑区或网络分组；分析方法和含义不明的描述（"节律调制""被训练节律""编码模型"）不登记。
- 有几处在 `likely_markers` 之外按记录模态补了标记物（如 MEM-NBK-001 加了 HbO_prefrontal 和 BOLD_frontoparietal，MOT-ME-001 加了 BOLD_motor_network），策展人核对文献后可通过 `marker_requests.csv` / worklog 提出删改。
- owner 分布：A 40、B 23、C 17、D 17、E 14。包 A 负担较重（很多共用的 ERP 和 BOLD 标记物在行序上最先出现在包 A），第一次例会上可以讨论是否把部分标记物（如 MK.BOLD_hippocampus、MK.BOLD_frontoparietal）改给使用最多的包。

### 3. 标记物骨架文件
- 为 107 个新标记物在 `knowledge/markers/` 建了最小合法骨架（`status: draft`，`contributors: [maintainer]`，description 为"待包 X 编写。"）。4 个种子标记物文件没有改动。

### 4. 工作目录（`curation/work/pkg_A` – `pkg_E`）
- 每个包一个 README（写入范围、文件说明、规则速查、本包收录范式与标记物、需要写成变体的被并入候选、本包负责的标记物）和空模板：`worklog.md`、`search_log.md`、`new_candidates.csv`、`status.csv`、`marker_requests.csv`、`pr/.gitkeep`。

### 5. 仓库基础设施
- `.github/ISSUE_TEMPLATE/paradigm.yml`：范式 Issue 表单（ID、包、类型、标记物、线索、纳入理由、写入范围确认）。
- `.github/pull_request_template.md`：出处核对表 + 自查清单 + 交叉审核。
- `.github/workflows/validate.yml`：checkout → Python 3.11 → 安装依赖 → `validate.py` → `build_graph.py`。
- `.gitignore`：忽略 `dist/`、`__pycache__/`。

### 6. 校验
- `python3 scripts/validate.py`：3 paradigms, 111 markers, 5 regions, 6 constructs checked; 0 problem(s)。`build_graph.py` 运行正常。

### 待办 / 待例会
- [ ] 负责人确认 D-001 – D-030（尤其是维护者补充的 D-024、D-025，以及 D-011 RSVP 并入 Oddball、D-013 SSMVEP 独立）。
- [ ] 讨论 decisions.md 末尾"下次例会候议"的 5 对候选。
- [ ] 标记物 owner 负担再平衡（见第 2 节）。
- [ ] 下一版词表讨论与 schema 0.3 提议：`tags` 字段（hybrid、hyperscanning、closed_loop）、DBS-LFP 记录模态（D-022、D-027）。
- [ ] 按 candidates.csv 中 187 个收录范式批量开 Issue（使用新 Issue 表单）；建看板与 Zotero 群组库。
- [ ] 脑区（regions.yaml 只有 5 个）和构念（constructs.yaml 只有 6 个）词表需要在第二遍前扩充，避免各包自行新增同义词条。

## 2026-10-03 · 第 1 周 · maintainer（sprint 1 合并与对账）

**目标**：合并 5 个包的第一遍骨架，跨包对账，更新登记表与总表，做 QA 抽样，完成里程碑 M1。本次没有做外部检索。

### 1. 合并（`integration`）
- 依次 `git merge --no-ff curation/pkg-A … pkg-E`（"Merge pkg X sprint 1 (first pass)"），**无冲突**：各包只写了本包范围（D-029），没有两个包创建同名标记物。合并后 269 个范式、129 个标记物，校验 0 问题。
- 核对种子条目（PER-ODD-001、SSR-SSVEP-001、MOT-MI-001）：A、B 用 safe_dump 改成块状 YAML，逐字段比较 main 版本，原有内容全部保留（D-054）。

### 2. 跨包对账与决议草案
- 用脚本比较全部条目的英文名、中文名、别名（规范化后）和标记物集合，找出 3 组确定重复并合并：STM-CLAS-001 → STA-CLAS-001（D-034）、SOC-CIT-001 → MEM-CIT-001（D-035）、IMG-WORD-001 → LAN-VF-001 变体（D-036）。作废 ID 不复用，PR 草稿顶部注明作废。
- 起草 D-031 – D-056（26 条），覆盖 5 个包 worklog 中的全部问题：源头规则（D-031，`notes` 中 `First neural recording:` 约定，schema 0.3 提议 `first_neural_source`，不改 schema）、TBD（D-032）、状态取值（D-033）、11 组边界（D-037 – D-042）、MEM-DS 复核（D-043）、D 的 2 个变体（D-044）、词表（D-045 – D-049）、标记物（D-050 – D-052）、新候选（D-053）、种子格式（D-054）、线索 QA（D-055）、CTL-STR 别名（D-056）。
- 已执行的：`taxonomy/stimulus_modality.yaml` 加草案词条 `pharmacological`、`optical_stimulation`；STA-ANES-001、STA-PSY-001 改用 `pharmacological`；按 B 的线索代建 STM-PBM-001（含 PR 草稿）；6 个血流标记物加 PET；D-031 涉及的 19 个条目 `notes` 加说明。

### 3. 登记表与总表
- `markers.csv`：从文件重新生成 `used_by`、类型、模态；登记 18 个新标记物（owner = 申请包）；owner 无变化；无未被使用的标记物。`paradigm_markers.csv`：从 267 个文件重新生成。
- `candidates.csv`：追加 C210 – C294（85 个新候选，收录 81、并入 4）；全部 294 行按各包 `status.csv` 更新状态（第一遍完成 223、阻塞 44、并入 19、暂缓 5、排除 3）；n_refs / n_reviews 按 paradigm_literature 重算；删除 CTL-STR-001 的情绪 Stroop 别名。
- `literature.csv`：新增 171 条（R1095 – R1265，`found_via=curator_search`），来自检索所得 first_source（102 个条目）、各包 new_candidates 的线索列、包 D new_leads.csv；新增 `qa_flag` 列，标记 34 条。`paradigm_literature.csv`：新增 172 条关联；8 条错配线索改配（MEM-RC → MEM-CD，LAN-HIER → PER-MMN / LAN-PCAT）。
- 引文拆分（作者 / 题名 / 期刊 / 年份）用启发式规则，约 43% 的新线索没有作者字段（检索页本身不显示）；DOI 与题名对不上的单列为"DOI only"行，不猜。

### 4. QA 与报告
- `curation/reports/qa_sprint1.md`：每包随机 8 个、共 40 个。形式检查全部通过；源头存疑 11 个、TBD 6 个；修了 18 处过时 notes、1 处引文标点。
- `scripts/coverage_report.py`（通用，经 `scripts/atlas.py` 读取）→ `curation/reports/coverage_M1.md`。
- `search_protocol.md` 写入 S-002（WebSearch 143、WebFetch 140、被拒 21、新候选 85）与 S-003 计划；`CHANGELOG.md` 增加 M1 条目（已并入 [0.1.0]）；`curation/reports/sprint1_report.md` 给负责人。
- `validate.py`：267 paradigms, 129 markers; 0 problem(s)。`build_graph.py`：407 nodes, 427 edges。

### 待办 / 待例会
- [ ] 负责人确认 D-001 – D-056（高优先级：D-031、D-033 – D-036、D-045、D-046）；确认后完成里程碑 M1 并合并 `main`。
- [ ] 解决数据库访问，集中补 37 个 TBD（D-032）；核对 34 条 `qa_flag` 线索。
- [ ] 改写各包 README 的 status 取值表（D-033）。
- [ ] 标记物 owner 再平衡（A 负责 50 个）。
- [ ] 把 `coverage_report.py` 加入 CI；扩充 regions / constructs 词表。

## 2026-10-03 · 第 1 周 · maintainer（D-057 两级标识符与 schema 0.2）

**目标**：落实负责人确认的两级范式标识符规则（D-057），完成 schema 0.2 迁移，为 sprint 2 的协议定义与拆分准备工作目录。本次没有做外部检索，未打标签。

### 1. 决议与文档
- `decisions.md` 新增 D-057（已确认（负责人，2026-10-03））：范式类 / 具体范式定义、4 条给号准则、MI 示例（MOT-MI-001 二分类、-002 四分类、-003 11 类上肢）；列出需在 sprint 2 复核的旧决议（判定基准、D-002 – D-008、D-011、D-012、D-014、D-015、D-017、D-018、D-020 – D-022、D-024、D-025、D-030、D-036、D-044，待议 D-041、D-042）与全部 35 个现有变体；文件开头的判定基准处加修订注。
- 方法说明中英文 §1（范式类、具体范式、变体 = 参数级）与 §6（标识符表、给号准则、永久性）重写；README 的 schema 版本改为 0.2。

### 2. schema 0.2 与迁移
- `paradigm.schema.json`：`schema_version` 只接受 "0.2"；必填 `class`（`^[A-Z]{3}-[A-Z0-9]{2,8}$`）；可选 `protocol`（additionalProperties false；`distinguishing` 必填）。新增 `paradigm_class.schema.json`。
- 标记物与词表：选择**一并迁移到 "0.2"**（只接受 "0.2"），内容不变，避免仓库中两个版本号并存。
- 迁移脚本（一次性，不入库）：267 个范式文件只改第 1 行版本号并在 `id` 后插入 `class`，其余字节不变；`paradigms/_classes.yaml` 由各 `-001` 文件生成 267 个范式类（名称、描述、标记物、源头、别名、状态照抄，`contributors: [maintainer]`，`notes: migrated from schema-0.1 file <ID>`）。别名也照抄了：迁移后范式类与具体范式一一对应，sprint 2 拆分时由策展人在 `class_updates.yaml` 中整理。

### 3. 脚本
- `atlas.py` 加载范式类；`validate.py` 新增范式类检查（schema、唯一、`class` = ID 去序号、已登记、族一致、每类至少一个具体范式、标记物存在、`n_classes` 与 `classes` 数量一致）和不报错的"无 protocol"警告；`build_graph.py` 增加 `paradigm_class` 节点、`instance_of` 与类→标记物 `elicits` 边；`coverage_report.py` 增加第 7 节。在副本中做过反例测试（重复类、错类、族不符、未知标记物、缺 distinguishing、n_classes 不符）均被报出。

### 4. sprint 2 工作目录
- `curation/work/pkg_A … pkg_E/sprint2/`：README（任务、给号准则、写入范围——范式类修改写 `class_updates.yaml`，由维护者合入 `_classes.yaml`；本包待复核变体表与维护者初判准则）、`split_log.csv`（表头）、`class_updates.yaml`（空）、`worklog.md`、`search_log.md`、`pr/.gitkeep`。

### 5. 结果
- `validate.py`：267 paradigms, 267 classes, 129 markers; **0 problem(s)，267 warning(s)**（全部为"无 protocol"）。
- `build_graph.py`：674 nodes（paradigm_class 267、paradigm 267、marker 129、construct 6、region 5），1111 edges（elicits 834、instance_of 267、indexes 6、generates 4）。
- `coverage_report.py` → `curation/reports/coverage_M2-start.md`（M1 报告保留不动）。

### 待办 / 待例会
- [ ] sprint 2：各包给 `-001` 写 `protocol`，按 split_log 复核 35 个变体；维护者每周合入 `class_updates.yaml`，并在 `candidates.csv` 中登记新具体范式 ID。
- [ ] 例会决定 D-041、D-042 时按 D-057 处理（并入 → 目标类下新序号）。
- [ ] `markers.csv` / `paradigm_markers.csv` 是否增加范式类层级（目前仍按具体范式生成）。
- [ ] CI 中是否在 sprint 2 结束后把"无 protocol"警告升级为错误。


## 2026-10-03 · 第 2 周 · maintainer（sprint 2 合并、登记与 QA，里程碑 M2 候选）

**目标**：合并 5 个包的 sprint 2（具体范式拆分），合入范式类修改，登记新线索与具体范式，起草决议，QA，出里程碑 M2 的候选状态。本次没有做外部检索（未使用 WebSearch）。

### 1. 合并（`integration`）
- 依次 `git merge --no-ff sprint2/pkg-A … pkg-E`（"Merge pkg X sprint 2 (split into concrete paradigms)"），**无冲突**：各包只改本包族的文件与 `curation/work/pkg_<X>/`（D 另改了 `new_leads.csv`）。具体范式 267 → 405（新建 138）。
- 合并后 `validate.py` 即为 0 问题、0 警告（405 个文件全部有 `protocol`）。

### 2. 范式类、标记物、文献、登记表
- `class_updates.yaml` 74 条（全部 `modify`）合入 `paradigms/_classes.yaml`：逐条检查 ID 已登记、字段在 schema 内、标记物已登记、在本包范围内；别名取并集——EMO-FILM 的更新删了 6 个原有别名（仍被 EMO-FILM-001 使用），保留。每条在类 notes 记来源、`contributors` 加策展人。脚本检查"类标记物 ⊇ 具体范式标记物"：MOT-GRASP 漏了 MK.low_freq_kinematics（已补）；MEM-SWM 的 MK.CDA 无具体范式使用（D-061，暂留）。
- 标记物：sprint 2 无新申请。`markers.csv` 重新生成，加 `used_by_class`、`n_classes`、`n_concrete`；`paradigm_markers.csv` 加 `class`、`class_marker_ids`。
- 文献：从 5 个包的 search_log、B 的线索表、C 的 S_ 编号、D 的 DN47 – DN53、以及文件 first_source / notes 中未登记的出处整理出 79 条线索，去重（DOI → PMID → 题名）后新建 78 条 R1266 – R1343（`found_via=curator_search_s2`，23 条带 `qa_flag`），S_KELLY2013 = R0578。R1093 补书目。notes 中的临时线索编号换成 R 编号（25 处）、检索编号后注 `[=R….]`（52 处）、18 个文件末尾注明登记的 R 编号。`paradigm_literature.csv` 新增 355 条（新线索 88；sprint 2 文件的 first_source 关联 97 条与 notes 中 R 编号 220 条，`found_via=sprint2_split`）。
- `candidates.csv` 加 `class`、`n_concrete`（27 行作废 ID 留空）；新建 `curation/registry/concrete_paradigms.csv`（405 行，first_source_status：待核实 341、TBD 64）。

### 3. 决议
- D-058 – D-071（14 条）：准则 1 粒度（提议同质目标数为参数，SSR-SSVEP-006 降为变体、-007 保留）、准则 3 范围、刺激模态 = 准则 2、标记物继承与替代标记物、类源头 vs -001、ID 冻结点（v0.1.0 发布）、ERR-OBS/ERR-ERRP 边界、EMO-ECONF 新类、first_source 质量、D-057 示例勘误（已执行）、包 B/C/E 待核对项、合并记录。
- D-057：示例 MOT-MI-003 改为 Ofner 2017 的 7 类、加 MOT-MI-011 = Jeong 2020 的 11 类；标题与状态行注明勘误、规则未改；方法说明中英文 §6 加与文件一致的 MI 示例表。

### 4. QA 与脚本
- 新脚本 `scripts/check_siblings.py`：全部 87 个有兄弟的类、268 对兄弟——0 对完全相同，35 对只在自由文本上不同（逐对人工复核，4 对需例会口径）。
- 抽样 50 个（每包新建 7 + `-001` 3）→ `curation/reports/qa_sprint2.md`。平凡修正：12 个包 A `-001` 过时的"本类暂无其他具体范式"、PER-ODD-001 的 `stimulus_coding` 误用、SOC-DICT-002 / EMO-MID-002 的 `n_classes`。
- `coverage_report.py`：新具体范式按类取工作包；新增第 8 节（protocol 字段分布、前 15 个类、各包 TBD）→ `coverage_M2.md`。

### 5. 结果
- `validate.py`：405 paradigms, 267 classes, 129 markers; **0 problem(s), 0 warning(s)**。
- `build_graph.py`：812 nodes（paradigm 405、paradigm_class 267、marker 129、construct 6、region 5），1437 edges（elicits 1022、instance_of 405、indexes 6、generates 4）。
- `search_protocol.md` S-003（WebSearch 44、WebFetch 92、被拒 16、新线索 78）与 S-004 计划；`CHANGELOG.md` M2 条目（2026-10-03，已并入 [0.1.0]）；`curation/reports/sprint2_report.md`。

### 待办 / 待例会
- [ ] 负责人确认 D-058、D-061 – D-063（v0.1.0 发布前），执行 SSR-SSVEP-006 降级、标记物固定短语、MEM-TMR / STA-SCP 的类 notes 与 distinguishing。
- [ ] IMG-MA-001/-002 是否对调（D-063，需核 R0842、R1301）。
- [ ] CI 加 `check_siblings.py` 与类标记物并集检查；"无 protocol"警告升级为错误。
- [ ] S-004 集中补源（64 个 TBD，优先 P1 核心类）；23 条 sprint 2 `qa_flag` 线索核原文。


## 2026-10-05 · 第 2 周 · maintainer（D-058 / D-061 – D-063 裁定执行，完成里程碑 M2）

**目标**：负责人授权专家裁定四条发布前必须决定的决议，按裁定改文件，完成里程碑 M2 并合并到 `main`。没有外部检索。

### 1. 决议登记
- `decisions.md`：D-058、D-061、D-062、D-063 状态行改为"已确认（专家裁定，负责人授权，2026-10-05）"，各加"裁定说明"（D-063 修订一处：IMG-MA 不对调）；第二冲刺草案的总状态行加 2026-10-05 更新；新增"schema 0.3 提议清单"（`marker_basis`、`structure`、`interoceptive`/`sleep`）。

### 2. 文件修改
- **D-058**：SSR-SSVEP-006 → `status: deprecated`，notes "merged into SSR-SSVEP-005 per D-058"（文件保留）；SSR-SSVEP-005 加变体 "12-target JFPM layout (Nakanishi et al. 2015)"、Nakanishi2015 数据集、别名，distinguishing 改写；PER-ODD-006/-008/-009 的 distinguishing 不再以目标数为准则 1；SSR-SSVEP-001/-002 中对 -006 的引用改写；`literature.csv` R1267 的 paradigms 与 `paradigm_literature.csv` 关联改到 -005（角色 dataset）；`candidates.csv` SSR-SSVEP 的 n_concrete 8 → 7；方法说明中英文 §6 准则 1 加同质目标规则。
- **D-061**：7 个文件 notes 加 `marker inherited from class` + 兄弟（CTL-STR-001→-002、ERR-TS-002→-001、CTL-ANT-002→-001、MEM-CD-001→-003、MEM-FR-002→-001、MEM-NBK-004→-001/-003、LAN-VF-001→-002/-003）；CTL-CPT-003、STA-NF-002 加 `stand-in marker`；MEM-SWM 类 notes 注明 MK.CDA 暂留。
- **D-062**：MEM-TMR-001 distinguishing → "标准配置（公认）/ canonical configuration"，指向更早的 -002；MEM-TMR、SSR-SSVEP、STA-SCP 类 notes 写入源头说明；方法说明中英文 §1 加类源头定义、§6 永久性一段改写。
- **D-063**：IMG-MA-001 distinguishing → "Canonical configuration / 标准配置（公认）"，R0842 仅为类源头候选；IMG-MA-002 注明内容待 sprint 3 核实；IMG-MA、STA-SCP 类 notes 与 STA-SCP-001 notes 记录裁定；方法说明 §6 加冻结点。

### 3. 脚本与登记表
- `validate.py`：新增错误级检查"类标记物 ⊇ 每个非 deprecated 具体范式的标记物"（D-061 第 4 款）及"类至少有一个有效具体范式"；副本反例测试（给 SSR-SSVEP-005 加 MK.P3b）报错正确。现有文件 0 违反。
- `check_siblings.py`、`build_graph.py`、`coverage_report.py` 跳过 `status: deprecated`；覆盖度报告第 1 节单列 deprecated 计数。
- 登记表重新生成（一次性脚本，未入库）：`concrete_paradigms.csv` 加 `status` 列（405 行，同时同步了 sprint 2 QA 的平凡修正）；`paradigm_markers.csv` 404 行；`markers.csv` MK.SSVEP 的 used_by 去掉 -006（n_concrete 10 → 9）。

### 4. 结果
- `validate.py`：405 paradigms, 267 classes, 129 markers; **0 problem(s), 0 warning(s)**。
- `check_siblings.py`：267 classes (87 with siblings), 261 pairs; 0 duplicate, 35 to review。
- `build_graph.py`：811 nodes（paradigm 404、paradigm_class 267、marker 129、construct 6、region 5），1435 edges（elicits 1021、instance_of 404、indexes 6、generates 4）。
- `coverage_report.py` → `coverage_M2.md`（404 有效 + 1 deprecated；TBD 64 / 36）。
- `CHANGELOG.md` M2 条目（2026-10-05，已并入 [0.1.0]，含四条已确认决议，中英双语）；M2 说明（已并入 `curation/reports/release_v0.1.0.md`）。
- 合并：`main` ← `git merge --no-ff integration`（M2）；`main` 校验通过。未推送。已完全合并的 `sprint2/pkg-*`、`curation/pkg-*` 分支删除（`git branch -d`），工作树保留。

### 待办 / 待例会
- [ ] 例会确认 D-059、D-060、D-064 – D-070。
- [ ] S-004 集中补源：64 个具体范式、36 个范式类的 TBD；58 条 `qa_flag` 线索核原文。
- [ ] sprint 3 各包待核对项（D-068 – D-070）；IMG-MA-002 内容核实；CTL-CPT-003 / STA-NF-002 标记物申请。
- [ ] CI 加 `check_siblings.py`；"无 protocol"警告升级为错误；schema 0.3 提议（`marker_basis`、`structure`）。


## 2026-10-07 · 第 3 周 · maintainer（sprint 3 合并：出处书目核实，里程碑 M3）

**目标**：合并五个包的书目核实结果，合入范式类修改，统一 notes 短语，登记 D-072 – D-074，完成里程碑 M3。没有外部检索。

### 1. 合并
- `integration` ← `sprint3/prep`（核实队列 + README）← `sprint3/pkg-A … E`（`--no-ff`，"Merge pkg X sprint 3 (bibliographic verification)"），**无冲突**（各包只改本族文件与 `curation/work/pkg_<X>/sprint3/`）。
- 五个 `sources_check.csv` 合并为 `curation/verification/sources_check.csv`（682 行）：变体行规范为 `entity_type=variant` + `variant_name` 列（审核人原写法为 `variant:<ID>` + 变体名作 entity_id）；加 `pkg_reviewer`。合并前检查：每行 entity 在图谱中存在（0 缺）、变体名在文件中唯一匹配。

### 2. 范式类与短语
- `class_updates.yaml` 254 条（A 56、B 46、C 45、D 53、E 54，全部 `modify`）合入 `_classes.yaml`：first_source 全量替换（184 个类实际改动；`verified` 一律 false），notes 两种写法（A/B/D/E 全文替换、C `append`）统一处理——全文替换前检查新文本包含旧文本（254/254 通过，D-058 / D-061 / D-062 的裁定文字无一丢失）；审核人加入 `contributors`。
- 短语检查（D-072 第 3 款）：confirmed / corrected 的条目审核人都已写 `bibliography confirmed|corrected (<API>, 2026-10-05)`；tbd_resolved 的 83 条（具体范式 50、类 33）审核人写的是 "candidate origin found by bibliographic search"，维护者统一追加 `bibliography confirmed (<API>, 2026-10-05; origin candidate, content unverified)`。not_found / tbd_open 条目 0 条误含短语。
- D-073 短语 `origin candidate recalled, record confirmed via <API>`：108 条（A 69 按 `source_api` 的 "DOI candidate from curator memory" 逐行；E 26 按 fetch_log #71–#88 说明列出的 15 个 ID 及同 DOI 的类 / 变体行；D 8 按 fetch_log 标 "DOI-record probe" 的 5 个 DOI；B 5 = 全部 tbd_resolved，fetch_log #97–#103 直接按候选 DOI 取记录）。`sources_check.csv` 的 note 同步加 "D-073: candidate from memory, record confirmed by API"。局限写入核实报告第 9 节。
- 改写具体范式文件 78 个（只动 notes / 变体 note；脚本逐文件比对其余字段无变化）。

### 3. 决议与方法说明
- D-072（两级核实，已确认）、D-073（凭记忆候选 DOI，已确认）、D-074（47 行遗留 → sprint 4，草案）写入 `decisions.md` 第二十一节；schema 0.3 提议清单加 `source.source_check`。方法说明中英文 §3 各加一句两级定义。`curation/verification/README.md` 标题与列说明更新。

### 4. 脚本与报告
- 新脚本 `scripts/verification_report.py`：按包 × 状态、按包 × 实体类型 × 状态计数，图谱中剩余 TBD，`verified: true` 清单，短语一致性（缺 / 多 / 找不到实体）。结果：682 行；TBD 具体范式 9、类 3；verified:true 0；短语缺 0、多 0。
- `validate.py`：405 paradigms, 267 classes, 129 markers; **0 problem(s), 0 warning(s)**。`check_siblings.py`：0 duplicate、35 to review（不变）。`build_graph.py`：811 节点 / 1,435 边（不变）。`coverage_report.py` → `coverage_M3.md`（TBD 9 / 3）。
- `curation/reports/verification_sprint3.md`（第 1–6 节脚本生成，第 7–10 节：16 条前→后示例、47 行未核实清单分类、工具限制、下一步）；`sprint3_report.md`（负责人可读）；`search_protocol.md` S-004（504 次请求、被拒 106、无 WebSearch）与 S-005 计划；`CHANGELOG.md` M3 条目（2026-10-07，已并入 [0.1.0]）。

### 5. 版本
- 合并：`main` ← `git merge --no-ff integration`（M3：出处书目核实，内容核实待做），`main` 校验通过；回到 `integration`。未推送。已完全合并的 `sprint3/prep` 删除；`sprint3/pkg-A … E` 因工作树（`wt3_A … E`）仍检出而保留。

### 待办 / 待例会
- [ ] 负责人确认 D-074；例会确认 D-059、D-060、D-064 – D-070。
- [ ] 第四冲刺前取得机构数据库 / Crossref polite pool / PubMed 访问。
- [ ] `literature.csv` R 编号书目与 `sources_check.csv` 同步；PMID 核验。
- [ ] 88 条 tbd_resolved、108 条 D-073 条目的内容核实（优先 P1 核心类）。

## 2026-10-08 · 第 3 周 · maintainer（v0.1.0 发布准备）

**目标**：负责人决定公开版本号为 v0.1.0（v0.0.1 之后的第一个功能版本），内部快照不对外出现版本号。没有外部检索，数据无变化。

- 内部快照改称里程碑：M1（第一遍骨架，2026-10-03）、M2（两级标识符与协议，2026-10-05）、M3（出处书目核实，2026-10-07）；ID 冻结点与发布相关的表述改为 v0.1.0；未来提议写"schema 0.3 提议"/"下一版词表讨论"。
- 覆盖度快照改名 `coverage_M1.md`、`coverage_M2-start.md`、`coverage_M2.md`、`coverage_M3.md`；新生成 `coverage_v0.1.0.md` 与 `BCI范式图谱_v0.1.0_总览.xlsx`；发布说明 `release_v0.1.0.md`（替代内部发布说明）。
- `CHANGELOG.md` 合并为 [0.1.0] - 2026-10-08；README 中英文"当前状态"与路线图更新。
- 校验：`validate.py` 0 问题、0 警告；`check_siblings.py` 0 duplicate、35 to review；`build_graph.py`、`verification_report.py` 正常。
