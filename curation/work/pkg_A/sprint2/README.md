# 包 A：感知与稳态 · sprint 2 工作目录

- 范式族：`perception`、`steady_state`
- 依据：[`curation/decisions.md`](../../../decisions.md) **D-057**（两级范式标识符，已确认）；[方法说明 §1、§6](../../../../docs/methodology.zh-CN.md)；schema 0.2
- 本包范式类 59 个，具体范式 59 个（schema 0.2 迁移后一一对应，均无 `protocol`）

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

1. `paradigms/perception/*`、`paradigms/steady_state/*`（含新建的 `-002`、`-003` …… 文件）；
2. `knowledge/markers/` 中 `owner_pkg = A` 的标记物文件，以及本包新申请且登记表中不存在同义项的标记物文件；
3. `curation/work/pkg_A/*`（含本目录）。

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
| `PER-MMN-001` | Speech-sound / phoneme-contrast MMN (native and non-native phoneme contrasts) | D-017 | 2 |
| `PER-MVEP-001` | Motion-onset VEP BCI | — | 1;4 |
| `PER-ODD-001` | P300 speller (row/column matrix) | 种子 | 1;2;4 |
| `PER-ODD-001` | Rapid serial visual presentation (RSVP) target detection (incl. RSVP typing and image-triage BCIs) | D-011 | 2;3 |
| `SSR-SSSEP-001` | Steady-state tactile spatial attention (attend-left vs attend-right vibration) | D-012 | 2 |
| `SSR-SSVEP-001` | SSVEP-based BCI | 种子 | 1;2;4 |
| `SSR-SSVEP-001` | Photic driving (clinical intermittent photic stimulation) | D-002 | 1;3 |
| `SSR-SSVEP-001` | Frequency-tagged attention to multiple concurrent stimuli | D-003 | 1;2 |
| `SSR-SSVEP-001` | High-frequency / imperceptible-flicker SSVEP | D-004 | （多为参数） |

- D-041：PER-ACC-001 倾向并入 PER-AEP-001——若例会判定并入，按 D-057 在 PER-AEP 下取新序号（准则 2），不写成变体。
- "SSVEP 频率编码 vs 联合频率–相位编码"、"P300 行/列 vs 棋盘格"是 D-057 的典型例子，请优先处理 SSR-SSVEP 与 PER-ODD。

## 本包范式类与具体范式（schema 0.2 迁移后）

| 范式类 | 具体范式 | 名称 | 变体数 |
|---|---|---|---|
| `PER-AAD` | `PER-AAD-001` | 听觉选择性注意（鸡尾酒会） | 0 |
| `PER-AB` | `PER-AB-001` | 注意瞬脱 | 0 |
| `PER-ABR` | `PER-ABR-001` | 听觉脑干反应 | 0 |
| `PER-ACC` | `PER-ACC-001` | 声学变化复合波 | 0 |
| `PER-ADDS` | `PER-ADDS-001` | 附加单例与干扰抑制 | 0 |
| `PER-AEP` | `PER-AEP-001` | 听觉诱发电位（纯音/短声） | 0 |
| `PER-AMASK` | `PER-AMASK-001` | 听觉掩蔽 | 0 |
| `PER-BODY` | `PER-BODY-001` | 身体知觉 | 0 |
| `PER-BOI` | `PER-BOI-001` | 身体拥有错觉（橡胶手） | 0 |
| `PER-BR` | `PER-BR-001` | 双眼竞争与双稳态知觉 | 0 |
| `PER-CAT` | `PER-CAT-001` | 视觉物体类别识别 | 0 |
| `PER-CB` | `PER-CB-001` | 变化盲 | 0 |
| `PER-CTXC` | `PER-CTXC-001` | 情境线索效应 | 0 |
| `PER-CUE` | `PER-CUE-001` | Posner 空间线索 | 0 |
| `PER-CVA` | `PER-CVA-001` | 隐蔽空间注意（α 偏侧化） | 0 |
| `PER-FACE` | `PER-FACE-001` | 面孔知觉 | 0 |
| `PER-FVEP` | `PER-FVEP-001` | 闪光视觉诱发电位 | 0 |
| `PER-GATE` | `PER-GATE-001` | 配对短声感觉门控 | 0 |
| `PER-GEP` | `PER-GEP-001` | 味觉诱发电位 | 0 |
| `PER-HBD` | `PER-HBD-001` | 心跳觉察（内感受） | 0 |
| `PER-IB` | `PER-IB-001` | 非注意盲 | 0 |
| `PER-IC` | `PER-IC-001` | 错觉轮廓知觉 | 0 |
| `PER-LEP` | `PER-LEP-001` | 激光诱发电位（痛觉） | 0 |
| `PER-LG` | `PER-LG-001` | 局部-全局范式 | 0 |
| `PER-MASK` | `PER-MASK-001` | 掩蔽与阈限知觉 | 0 |
| `PER-MLR` | `PER-MLR-001` | 听觉中潜伏期反应 | 0 |
| `PER-MMN` | `PER-MMN-001` | 被动 oddball（失匹配负波） | 1 |
| `PER-MOT` | `PER-MOT-001` | 多目标追踪 | 0 |
| `PER-MSI` | `PER-MSI-001` | 视听多感觉整合 | 0 |
| `PER-MVEP` | `PER-MVEP-001` | 运动起始视觉诱发电位 | 1 |
| `PER-NAT` | `PER-NAT-001` | 自然图像与影片观看 | 0 |
| `PER-NAVON` | `PER-NAVON-001` | Navon 全局-局部 | 0 |
| `PER-ODD` | `PER-ODD-001` | Oddball 范式（怪球范式） | 2 |
| `PER-OLF` | `PER-OLF-001` | 嗅觉诱发电位 | 0 |
| `PER-OMIT` | `PER-OMIT-001` | 刺激遗漏范式 | 0 |
| `PER-ORN` | `PER-ORN-001` | 失谐谐波与同时声音分离 | 0 |
| `PER-PRVEP` | `PER-PRVEP-001` | 棋盘格翻转 VEP | 0 |
| `PER-RET` | `PER-RET-001` | 视网膜拓扑映射 | 0 |
| `PER-RREP` | `PER-RREP-001` | 呼吸相关诱发电位 | 0 |
| `PER-SPN` | `PER-SPN-001` | 视觉对称知觉 | 0 |
| `PER-STREAM` | `PER-STREAM-001` | 听觉流分离 | 0 |
| `PER-TACT` | `PER-TACT-001` | 触觉空间注意 | 0 |
| `PER-TON` | `PER-TON-001` | 音调拓扑映射 | 0 |
| `PER-VMMN` | `PER-VMMN-001` | 视觉失匹配负波 | 0 |
| `PER-VOICE` | `PER-VOICE-001` | 嗓音知觉（颞叶嗓音区定位） | 0 |
| `PER-VS` | `PER-VS-001` | 视觉搜索 | 0 |
| `SSR-ASSR` | `SSR-ASSR-001` | 听觉稳态响应 | 0 |
| `SSR-BEAT` | `SSR-BEAT-001` | 节律与节拍跟随 | 0 |
| `SSR-CVEP` | `SSR-CVEP-001` | 编码调制视觉诱发电位 | 0 |
| `SSR-FFR` | `SSR-FFR-001` | 频率跟随响应 | 0 |
| `SSR-FPAS` | `SSR-FPAS-001` | 快速周期听觉刺激 | 0 |
| `SSR-FPVS` | `SSR-FPVS-001` | 快速周期视觉刺激（频率标记） | 0 |
| `SSR-IM` | `SSR-IM-001` | 互调频率标记 | 0 |
| `SSR-NSSEP` | `SSR-NSSEP-001` | 伤害性稳态诱发电位 | 0 |
| `SSR-RVS` | `SSR-RVS-001` | 节律性视觉刺激（α 夹带） | 0 |
| `SSR-SSMVEP` | `SSR-SSMVEP-001` | 稳态运动视觉诱发电位 | 0 |
| `SSR-SSSEP` | `SSR-SSSEP-001` | 稳态体感诱发电位 | 1 |
| `SSR-SSVEP` | `SSR-SSVEP-001` | 稳态视觉诱发电位范式 | 4 |
| `SSR-SWEEP` | `SSR-SWEEP-001` | 扫描 VEP（视敏度评估） | 0 |
