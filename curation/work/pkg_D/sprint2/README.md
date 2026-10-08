# 包 D：记忆与语言 · sprint 2 工作目录

- 范式族：`memory`、`language`
- 依据：[`curation/decisions.md`](../../../decisions.md) **D-057**（两级范式标识符，已确认）；[方法说明 §1、§6](../../../../docs/methodology.zh-CN.md)；schema 0.2
- 本包范式类 53 个，具体范式 53 个（schema 0.2 迁移后一一对应，均无 `protocol`）

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

1. `paradigms/memory/*`、`paradigms/language/*`（含新建的 `-002`、`-003` …… 文件）；
2. `knowledge/markers/` 中 `owner_pkg = D` 的标记物文件，以及本包新申请且登记表中不存在同义项的标记物文件；
3. `curation/work/pkg_D/*`（含本目录）。

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
| `MEM-CD-001` | Delayed estimation (continuous report of a remembered feature) | D-044 | 1;3 |
| `MEM-FR-001` | Rey Auditory Verbal Learning Test (RAVLT) | — | 待判定 |
| `MEM-META-001` | Judgment of learning (JOL) | — | 待判定 |
| `MEM-NAV-001` | Virtual radial arm maze | — | 待判定 |
| `MEM-ON-001` | Remember/know judgements | D-024 | 1 |
| `LAN-P600-001` | Garden-path sentences | — | 待判定 |
| `LAN-PN-001` | Picture-word interference | — | 待判定 |
| `LAN-SC-001` | Sign language sentence comprehension | D-044 | 2 |
| `LAN-VF-001` | fNIRS / EEG-fNIRS mental-task BCI: covert word generation (letter, category or associate cue) | D-036 | 3;4 |

- D-042：若 ERR-AAF-001 并入 LAN-SIS-001，由本包在 LAN-SIS 下取新序号（准则 2）。

## 本包范式类与具体范式（schema 0.2 迁移后）

| 范式类 | 具体范式 | 名称 | 变体数 |
|---|---|---|---|
| `MEM-CD` | `MEM-CD-001` | 变化检测 | 1 |
| `MEM-CFMT` | `MEM-CFMT-001` | 剑桥面孔记忆 | 0 |
| `MEM-CIT` | `MEM-CIT-001` | 隐匿信息测试（P300） | 0 |
| `MEM-DF` | `MEM-DF-001` | 定向遗忘 | 0 |
| `MEM-DMS` | `MEM-DMS-001` | 延迟匹配 | 0 |
| `MEM-DRM` | `MEM-DRM-001` | 错误记忆（DRM） | 0 |
| `MEM-DS` | `MEM-DS-001` | 数字广度 | 0 |
| `MEM-EFT` | `MEM-EFT-001` | 情景未来思维 | 0 |
| `MEM-FR` | `MEM-FR-001` | 自由回忆与词表学习 | 1 |
| `MEM-META` | `MEM-META-001` | 元记忆（知晓感、学习判断） | 1 |
| `MEM-MST` | `MEM-MST-001` | 记忆相似性（模式分离） | 0 |
| `MEM-NAV` | `MEM-NAV-001` | 虚拟空间导航记忆 | 1 |
| `MEM-NBK` | `MEM-NBK-001` | n-back | 0 |
| `MEM-ON` | `MEM-ON-001` | 新旧再认 | 1 |
| `MEM-PA` | `MEM-PA-001` | 配对联想学习 | 0 |
| `MEM-PM` | `MEM-PM-001` | 前瞻记忆 | 0 |
| `MEM-RC` | `MEM-RC-001` | 回溯线索 | 0 |
| `MEM-RIF` | `MEM-RIF-001` | 提取诱发遗忘 | 0 |
| `MEM-RMEM` | `MEM-RMEM-001` | 奖赏驱动的记忆编码 | 0 |
| `MEM-RPRIM` | `MEM-RPRIM-001` | 重复启动（内隐记忆） | 0 |
| `MEM-RPT` | `MEM-RPT-001` | 近期探测任务（前摄干扰） | 0 |
| `MEM-SB` | `MEM-SB-001` | Sternberg 工作记忆 | 0 |
| `MEM-SME` | `MEM-SME-001` | 后续记忆效应 | 0 |
| `MEM-SRC` | `MEM-SRC-001` | 来源记忆 | 0 |
| `MEM-SRE` | `MEM-SRE-001` | 自我参照编码 | 0 |
| `MEM-SWM` | `MEM-SWM-001` | 空间工作记忆 | 0 |
| `MEM-TMR` | `MEM-TMR-001` | 睡眠中目标记忆再激活 | 0 |
| `MEM-TNT` | `MEM-TNT-001` | 想/不想 | 0 |
| `LAN-AGL` | `LAN-AGL-001` | 人工语法学习 | 0 |
| `LAN-CPS` | `LAN-CPS-001` | 韵律边界加工 | 0 |
| `LAN-GEST` | `LAN-GEST-001` | 言语—手势整合 | 0 |
| `LAN-HIER` | `LAN-HIER-001` | 语言层级结构频率标记 | 0 |
| `LAN-LDT` | `LAN-LDT-001` | 词汇判断 | 0 |
| `LAN-LOC` | `LAN-LOC-001` | 语言定位任务 | 0 |
| `LAN-MUS` | `LAN-MUS-001` | 音乐句法违例 | 0 |
| `LAN-N400` | `LAN-N400-001` | 语义违例 | 0 |
| `LAN-NAT` | `LAN-NAT-001` | 自然语音聆听 | 0 |
| `LAN-NWL` | `LAN-NWL-001` | 新词学习 | 0 |
| `LAN-OVS` | `LAN-OVS-001` | 出声或尝试言语产生 | 0 |
| `LAN-P600` | `LAN-P600-001` | 句法违例 | 1 |
| `LAN-PCAT` | `LAN-PCAT-001` | 音位范畴化 | 0 |
| `LAN-PHA` | `LAN-PHA-001` | 语音意识 | 0 |
| `LAN-PN` | `LAN-PN-001` | 图片命名 | 1 |
| `LAN-PRIME` | `LAN-PRIME-001` | 语义启动 | 0 |
| `LAN-READ` | `LAN-READ-001` | 自然阅读（眼动同步） | 0 |
| `LAN-SC` | `LAN-SC-001` | 句子理解 | 1 |
| `LAN-SEMD` | `LAN-SEMD-001` | 语义判断任务（语言定位） | 0 |
| `LAN-SIS` | `LAN-SIS-001` | 言语诱发抑制与听觉反馈 | 0 |
| `LAN-SL` | `LAN-SL-001` | 统计学习（言语切分） | 0 |
| `LAN-SWITCH` | `LAN-SWITCH-001` | 双语语言切换 | 0 |
| `LAN-VF` | `LAN-VF-001` | 言语流畅性 | 1 |
| `LAN-VG` | `LAN-VG-001` | 动词生成 | 0 |
| `LAN-VWFA` | `LAN-VWFA-001` | 视觉词形加工（字词定位） | 0 |
