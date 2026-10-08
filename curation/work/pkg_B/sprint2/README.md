# 包 B：运动、想象与刺激 · sprint 2 工作目录

- 范式族：`motor`、`imagery`、`stimulation`
- 依据：[`curation/decisions.md`](../../../decisions.md) **D-057**（两级范式标识符，已确认）；[方法说明 §1、§6](../../../../docs/methodology.zh-CN.md)；schema 0.2
- 本包范式类 49 个，具体范式 49 个（schema 0.2 迁移后一一对应，均无 `protocol`）

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

1. `paradigms/motor/*`、`paradigms/imagery/*`、`paradigms/stimulation/*`（含新建的 `-002`、`-003` …… 文件）；
2. `knowledge/markers/` 中 `owner_pkg = B` 的标记物文件，以及本包新申请且登记表中不存在同义项的标记物文件；
3. `curation/work/pkg_B/*`（含本目录）。

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
| `MOT-ME-001` | Individual finger movements (ECoG/intracortical finger decoding) | D-005 | 1 |
| `MOT-ME-001` | Overground / treadmill walking | D-014 | 1;3 |
| `MOT-ME-001` | Paced finger tapping (visual or auditory pacing) | — | 2 |
| `MOT-MI-001` | Lower-limb / foot motor imagery | D-014 | 1 |
| `IMG-AUD-001` | Musical imagery | D-006 | 1;2 |
| `IMG-CMD-001` | Spatial navigation imagery (house navigation) | D-008 | 1 |
| `IMG-CMD-001` | Bedside EEG motor-imagery command following | — | 1;2 |
| `IMG-VIS-001` | Category-specific imagery (faces / places) | D-007 | 1 |

- MOT-MI 是 D-057 的示例：MOT-MI-001 = 左/右手二分类（Pfurtscheller & Neuper 1997），MOT-MI-002 = 四分类（左手/右手/双脚/舌头，BCI Competition IV 2a），MOT-MI-003 = 单侧上肢 11 类动作想象。请按此建文件（每个具体范式须有本包核对过的出处，查不到的先在 split_log 中记为"提议"）、写 `protocol`，并把 MOT-MI-001 的 `trial_structure.conditions`、`datasets`、描述收窄到二分类配置（四分类数据集移到 MOT-MI-002）。
- D-022 混合 BCI（`Hybrid:` 变体）：组合本身不是给号准则；若组合后的类别集或反馈方式构成独立配置，在 split_log 中提出，待例会。

## 本包范式类与具体范式（schema 0.2 迁移后）

| 范式类 | 具体范式 | 名称 | 变体数 |
|---|---|---|---|
| `MOT-ATT` | `MOT-ATT-001` | 尝试运动（瘫痪患者） | 0 |
| `MOT-BIMAN` | `MOT-BIMAN-001` | 双手协调 | 0 |
| `MOT-CURSOR` | `MOT-CURSOR-001` | 闭环光标控制 | 0 |
| `MOT-FORCE` | `MOT-FORCE-001` | 等长力控制 | 0 |
| `MOT-GRASP` | `MOT-GRASP-001` | 抓握与手势 | 0 |
| `MOT-HW` | `MOT-HW-001` | 尝试手写 | 0 |
| `MOT-IB` | `MOT-IB-001` | 意向绑定（主体感） | 0 |
| `MOT-LIBET` | `MOT-LIBET-001` | Libet 意图时刻判断任务 | 0 |
| `MOT-ME` | `MOT-ME-001` | 运动执行 | 3 |
| `MOT-MI` | `MOT-MI-001` | 提示性运动想象 | 1 |
| `MOT-MIRR` | `MOT-MIRR-001` | 镜像描摹 | 0 |
| `MOT-MRCP` | `MOT-MRCP-001` | 自主运动准备（准备电位） | 0 |
| `MOT-MSL` | `MOT-MSL-001` | 运动序列学习（手指序列） | 0 |
| `MOT-MVF` | `MOT-MVF-001` | 镜像视觉反馈 | 0 |
| `MOT-OBS` | `MOT-OBS-001` | 动作观察 | 0 |
| `MOT-PASS` | `MOT-PASS-001` | 被动运动（本体感觉刺激） | 0 |
| `MOT-PERT` | `MOT-PERT-001` | 姿势平衡扰动 | 0 |
| `MOT-PURS` | `MOT-PURS-001` | 平滑追踪眼动 | 0 |
| `MOT-REACH` | `MOT-REACH-001` | 中心外伸伸够任务 | 0 |
| `MOT-RT` | `MOT-RT-001` | 简单/选择反应时 | 0 |
| `MOT-SACC` | `MOT-SACC-001` | 眼跳任务 | 0 |
| `MOT-SMS` | `MOT-SMS-001` | 感觉运动同步（节拍器敲击） | 0 |
| `MOT-SRT` | `MOT-SRT-001` | 序列反应时（运动序列学习） | 0 |
| `MOT-TRACK` | `MOT-TRACK-001` | 连续轨迹追踪 | 0 |
| `IMG-AUD` | `IMG-AUD-001` | 听觉想象 | 1 |
| `IMG-CMD` | `IMG-CMD-001` | 指令跟随想象（意识评估） | 2 |
| `IMG-MA` | `IMG-MA-001` | 心算 | 0 |
| `IMG-OLF` | `IMG-OLF-001` | 嗅觉想象 | 0 |
| `IMG-ROT` | `IMG-ROT-001` | 心理旋转 | 0 |
| `IMG-SAO` | `IMG-SAO-001` | 体感注意定向 | 0 |
| `IMG-SPI` | `IMG-SPI-001` | 想象语音（内部言语） | 0 |
| `IMG-TACT` | `IMG-TACT-001` | 触觉想象 | 0 |
| `IMG-VIS` | `IMG-VIS-001` | 视觉想象 | 1 |
| `STM-ADBS` | `STM-ADBS-001` | 自适应（闭环）深部脑刺激 | 0 |
| `STM-CCEP` | `STM-CCEP-001` | 皮层-皮层诱发电位 | 0 |
| `STM-DBSEP` | `STM-DBSEP-001` | 深部脑刺激诱发电位 | 0 |
| `STM-GVS` | `STM-GVS-001` | 直流电前庭刺激 | 0 |
| `STM-PAS` | `STM-PAS-001` | 成对联合刺激 | 0 |
| `STM-PBM` | `STM-PBM-001` | 经颅光生物调节同步脑电 | 0 |
| `STM-PHTMS` | `STM-PHTMS-001` | 脑电相位触发 TMS | 0 |
| `STM-SEP` | `STM-SEP-001` | 正中神经体感诱发电位 | 0 |
| `STM-TACS` | `STM-TACS-001` | 经颅交流电刺激同步脑电 | 0 |
| `STM-TAVNS` | `STM-TAVNS-001` | 经皮耳迷走神经刺激 | 0 |
| `STM-TDCS` | `STM-TDCS-001` | 经颅直流电刺激同步记录 | 0 |
| `STM-TEP` | `STM-TEP-001` | TMS 诱发脑电 | 0 |
| `STM-TI` | `STM-TI-001` | 时间干涉电刺激 | 0 |
| `STM-TMSFMRI` | `STM-TMSFMRI-001` | TMS 与功能磁共振同步 | 0 |
| `STM-TUS` | `STM-TUS-001` | 经颅超声刺激 | 0 |
| `STM-VIB` | `STM-VIB-001` | 肌腱振动运动错觉 | 0 |
