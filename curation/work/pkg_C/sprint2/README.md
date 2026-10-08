# 包 C：错误监测与认知控制 · sprint 2 工作目录

- 范式族：`error`、`control`
- 依据：[`curation/decisions.md`](../../../decisions.md) **D-057**（两级范式标识符，已确认）；[方法说明 §1、§6](../../../../docs/methodology.zh-CN.md)；schema 0.2
- 本包范式类 52 个，具体范式 52 个（schema 0.2 迁移后一一对应，均无 `protocol`）

## sprint 2 的任务

1. **给每个 `-001` 写 `protocol`**：`-001` 是该范式类最早发表或公认的标准配置。写 `n_classes`、`classes`、`cue`、`stimulus_coding`（适用时）、`paradigm_timing`、`feedback`，`distinguishing` 写"标准配置（最早发表）"及出处。若现有 `-001` 文件混合了多个配置（`trial_structure.conditions`、`datasets`、描述写的是并集），把它收窄到标准配置，其余配置拆出。
2. **复核变体**（下表）：按 D-057 的 4 条准则，判定每个变体是**参数级变体**（留在 `variants`）还是**新的具体范式**（新建 `<范式类>-002` 等文件，从 `variants` 删去该条）。每个判定在 `split_log.csv` 记一行。
3. **发现新配置**：读文献时遇到同一范式类下满足准则的其他配置（不同类别集、编码方案、异步/闭环版本等），同样记入 `split_log.csv`，有出处后建文件。
4. **范式类的修改**（名称、描述、标记物、源头、别名）写入 `class_updates.yaml`，**不要直接改** `paradigms/_classes.yaml`。新建范式类同样写在这里。

### 给号准则（D-057）

同一范式类下，以下任一改变即取新序号：
1. 类别/条件集（数量或身份）；
2. 刺激或提示类型，含编码方案（如 SSVEP 频率编码 vs 联合频率–相位编码；P300 行/列 vs 棋盘格）；
3. 试次结构（同步 vs 异步/自定步调；单试次 vs 组块）；
4. 反馈方式（无 / 离散 / 连续；开环 vs 闭环）。

只改参数（时长、ISI、试次数、同一编码方案内的频率值、人群、电极数）的**不给新号**，写在 `variants` 或参数范围。序号永久有效、不复用；按本包认定顺序取下一个未用序号。被并入候选的作废 ID（如 MOT-GAIT-001）不复活。

## 写入范围（D-029 + D-057）

与 sprint 1 相同，你**只能**新增或修改：

1. `paradigms/error/*`、`paradigms/control/*`（含新建的 `-002`、`-003` …… 文件）；
2. `knowledge/markers/` 中 `owner_pkg = C` 的标记物文件，以及本包新申请且登记表中不存在同义项的标记物文件；
3. `curation/work/pkg_C/*`（含本目录）。

**范式类登记表 `paradigms/_classes.yaml` 是共享文件**：本包族下范式类的修改与新增写入本目录 `class_updates.yaml`，由维护者统一合入，避免 5 个包的 PR 冲突。新的具体范式文件的 `class` 必须是已登记或已在 `class_updates.yaml` 中提出的范式类（维护者合入前，新范式类的 PR 校验会报"class not registered"，这是预期的，在 PR 中注明即可）。

不得修改：`paradigms/_classes.yaml`、`curation/candidates.csv`、`curation/registry/*`、`curation/decisions.md`、`knowledge/regions.yaml`、`knowledge/constructs.yaml`、`taxonomy/*`、`schema/*`、`scripts/*`，以及其他包的文件。

## 本目录文件

| 文件 | 用途 |
|---|---|
| `split_log.csv` | 每个拆分/保留判定一行（见下） |
| `class_updates.yaml` | 本包范式类的修改与新增，维护者合入 `paradigms/_classes.yaml` |
| `worklog.md` | 工作日志，每次工作追加一节 |
| `search_log.md` | 检索记录（格式同 sprint 1） |
| `pr/` | PR 描述草稿 `<具体范式ID>.md`（PR 模板中须写明给号依据） |

### `split_log.csv` 列

`class_id,new_id,criterion,distinguishing,source_ref,lead_url,status,note`

- `class_id`：范式类，如 `MOT-MI`；
- `new_id`：新具体范式 ID（如 `MOT-MI-002`）；判定为参数级变体的写原文件 ID 并在 `status` 写"保留为变体"；
- `criterion`：`1`、`2`、`3`、`4`，多个用 `;` 分隔（如 `1;4`）；保留为变体的留空；
- `distinguishing`：与兄弟协议的区别（与文件中 `protocol.distinguishing` 一致）；
- `source_ref`：出处的 R 编号或 DOI/PMID；`lead_url`：本次检索看到的 URL（无则空）；
- `status`：`提议` / `已建文件` / `保留为变体` / `待例会`；
- `note`：相关决议（如 D-014）、被拆出的变体名等。

### `class_updates.yaml` 格式

```yaml
updates:
  - id: MOT-MI            # 范式类 ID
    action: modify        # modify | add | deprecate
    fields:               # 只写要改的字段（字段同 schema/paradigm_class.schema.json）
      description: {en: "...", zh: "..."}
    reason: "..."         # 理由与出处
```

## 待复核的变体

| 具体范式 | 变体 | 相关决议 | 可能涉及的准则（维护者初判，仅供参考） |
|---|---|---|---|
| `ERR-AWARE-001` | Antisaccade error-awareness task (error signalling of saccade errors) | D-015 | 2 |

- D-042：ERR-AAF-001 倾向并入 LAN-SIS-001（包 D）——若例会判定并入，由包 D 在 LAN-SIS 下取新序号；本包在 worklog 中交接线索。
- 包 C 现有变体少，重点是给全部 52 个 `-001` 写 `protocol`，并检查 `trial_structure.conditions` 是否混入了不同配置（如 Flanker 的箭头 vs 字母、Go/NoGo 的比例只是参数）。

## 本包范式类与具体范式（schema 0.2 迁移后）

| 范式类 | 具体范式 | 名称 | 变体数 |
|---|---|---|---|
| `ERR-AAF` | `ERR-AAF-001` | 音高偏移听觉反馈（言语运动误差） | 0 |
| `ERR-ADAPT` | `ERR-ADAPT-001` | 运动适应（视觉旋转） | 0 |
| `ERR-APC` | `ERR-APC-001` | 食欲性巴甫洛夫条件化（时间差分预测误差） | 0 |
| `ERR-AWARE` | `ERR-AWARE-001` | 错误觉知 | 1 |
| `ERR-BANDIT` | `ERR-BANDIT-001` | 多臂老虎机（探索-利用） | 0 |
| `ERR-CAUS` | `ERR-CAUS-001` | 因果学习 | 0 |
| `ERR-CHGPT` | `ERR-CHGPT-001` | 预测推断（变点）任务 | 0 |
| `ERR-ERRP` | `ERR-ERRP-001` | 交互式错误电位 | 0 |
| `ERR-GAM` | `ERR-GAM-001` | 赌博与奖赏反馈 | 0 |
| `ERR-INST` | `ERR-INST-001` | 工具性条件化 | 0 |
| `ERR-OBS` | `ERR-OBS-001` | 观察性错误 | 0 |
| `ERR-OGNG` | `ERR-OGNG-001` | 正交化 Go/NoGo 学习任务 | 0 |
| `ERR-PCL` | `ERR-PCL-001` | 概率分类学习（天气预报任务） | 0 |
| `ERR-PRL` | `ERR-PRL-001` | 概率反转学习 | 0 |
| `ERR-PRT` | `ERR-PRT-001` | 概率奖赏任务（信号检测） | 0 |
| `ERR-PSEL` | `ERR-PSEL-001` | 概率选择任务 | 0 |
| `ERR-TE` | `ERR-TE-001` | 时间估计任务 | 0 |
| `ERR-TS` | `ERR-TS-001` | 两阶段决策（基于模型/无模型） | 0 |
| `ERR-VRPE` | `ERR-VRPE-001` | 虚拟现实视觉–触觉失配（预测误差负波） | 0 |
| `CTL-AMBIG` | `CTL-AMBIG-001` | 风险与模糊决策 | 0 |
| `CTL-ANAL` | `CTL-ANAL-001` | 类比推理 | 0 |
| `CTL-ANT` | `CTL-ANT-001` | 注意网络测试 | 0 |
| `CTL-AS` | `CTL-AS-001` | 反向眼跳 | 0 |
| `CTL-AUT` | `CTL-AUT-001` | 替代用途任务（发散思维） | 0 |
| `CTL-BART` | `CTL-BART-001` | 气球模拟风险任务 | 0 |
| `CTL-CNV` | `CTL-CNV-001` | S1-S2 预期任务 | 0 |
| `CTL-CONF` | `CTL-CONF-001` | 决策信心判断（知觉元认知） | 0 |
| `CTL-CPT` | `CTL-CPT-001` | 持续操作任务（AX-CPT） | 0 |
| `CTL-DD` | `CTL-DD-001` | 延迟折扣 | 0 |
| `CTL-DT` | `CTL-DT-001` | 双任务 | 0 |
| `CTL-EFF` | `CTL-EFF-001` | 努力决策 | 0 |
| `CTL-FLK` | `CTL-FLK-001` | Flanker 任务 | 0 |
| `CTL-FORAGE` | `CTL-FORAGE-001` | 觅食决策（留守/探索） | 0 |
| `CTL-GNG` | `CTL-GNG-001` | Go/NoGo | 0 |
| `CTL-IGT` | `CTL-IGT-001` | 爱荷华赌博任务 | 0 |
| `CTL-MIXG` | `CTL-MIXG-001` | 混合赌局（损失厌恶） | 0 |
| `CTL-MRP` | `CTL-MRP-001` | 掩蔽反应启动 | 0 |
| `CTL-MSIT` | `CTL-MSIT-001` | 多源干扰任务 | 0 |
| `CTL-PDM` | `CTL-PDM-001` | 知觉决策（随机点运动） | 0 |
| `CTL-RAT` | `CTL-RAT-001` | 远距离联想（创造力） | 0 |
| `CTL-RAVEN` | `CTL-RAVEN-001` | 瑞文推理 | 0 |
| `CTL-RNG` | `CTL-RNG-001` | 随机数生成 | 0 |
| `CTL-SART` | `CTL-SART-001` | 持续注意反应任务（SART） | 0 |
| `CTL-SIM` | `CTL-SIM-001` | Simon 任务 | 0 |
| `CTL-SST` | `CTL-SST-001` | 停止信号任务 | 0 |
| `CTL-STR` | `CTL-STR-001` | Stroop 任务 | 0 |
| `CTL-SW` | `CTL-SW-001` | 任务切换 | 0 |
| `CTL-SYLL` | `CTL-SYLL-001` | 三段论推理 | 0 |
| `CTL-TOL` | `CTL-TOL-001` | 伦敦塔（计划） | 0 |
| `CTL-VBC` | `CTL-VBC-001` | 基于价值的选择（支付意愿） | 0 |
| `CTL-WASON` | `CTL-WASON-001` | Wason 选择任务 | 0 |
| `CTL-WCST` | `CTL-WCST-001` | 威斯康星卡片分类 | 0 |
