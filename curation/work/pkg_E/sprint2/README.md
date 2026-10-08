# 包 E：情绪、社会与脑状态 · sprint 2 工作目录

- 范式族：`emotion`、`social`、`state`
- 依据：[`curation/decisions.md`](../../../decisions.md) **D-057**（两级范式标识符，已确认）；[方法说明 §1、§6](../../../../docs/methodology.zh-CN.md)；schema 0.2
- 本包范式类 54 个，具体范式 54 个（schema 0.2 迁移后一一对应，均无 `protocol`）

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

1. `paradigms/emotion/*`、`paradigms/social/*`、`paradigms/state/*`（含新建的 `-002`、`-003` …… 文件）；
2. `knowledge/markers/` 中 `owner_pkg = E` 的标记物文件，以及本包新申请且登记表中不存在同义项的标记物文件；
3. `curation/work/pkg_E/*`（含本目录）。

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
| `EMO-FC-001` | Fear generalization (parametric CS similarity gradient) | — | 待判定 |
| `EMO-FILM-001` | Music and music-video emotion elicitation (e.g. DEAP, AMIGOS datasets) | D-018 | 2 |
| `EMO-MID-001` | Social incentive delay (social reward cues) | D-025 | 2 |
| `SOC-JA-001` | Hyperscanning: cooperative interaction tasks recorded simultaneously from two brains | D-021 | （记录配置；看任务） |
| `SOC-TOM-001` | fMRI false-belief localizer (false belief vs false photograph) | — | 待判定 |
| `SOC-TRUST-001` | Hyperscanning: multi-round trust game with both players scanned | D-021 | （记录配置；看任务） |
| `STA-NF-001` | Real-time fMRI neurofeedback of regional BOLD | D-020 | 4 |
| `STA-NF-001` | fNIRS haemodynamic neurofeedback | D-020 | 4 |

- D-022 混合 BCI 与 D-021 超扫描：记录配置或组合方式本身不是给号准则；其中的任务配置满足准则 1–4 时才给号。

## 本包范式类与具体范式（schema 0.2 迁移后）

| 范式类 | 具体范式 | 名称 | 变体数 |
|---|---|---|---|
| `EMO-APRIME` | `EMO-APRIME-001` | 情感（评价）启动 | 0 |
| `EMO-AUTO` | `EMO-AUTO-001` | 自传体回忆情绪诱发 | 0 |
| `EMO-DOT` | `EMO-DOT-001` | 点探测注意偏向任务 | 0 |
| `EMO-EST` | `EMO-EST-001` | 情绪 Stroop | 0 |
| `EMO-FACE` | `EMO-FACE-001` | 情绪面孔加工 | 0 |
| `EMO-FC` | `EMO-FC-001` | 巴甫洛夫恐惧条件化 | 1 |
| `EMO-FILM` | `EMO-FILM-001` | 自然刺激情绪诱发（影片、音乐、音乐视频） | 1 |
| `EMO-HUMOR` | `EMO-HUMOR-001` | 幽默欣赏 | 0 |
| `EMO-IAPS` | `EMO-IAPS-001` | 情绪图片观看 | 0 |
| `EMO-MID` | `EMO-MID-001` | 金钱激励延迟任务 | 1 |
| `EMO-REG` | `EMO-REG-001` | 情绪调节（认知重评） | 0 |
| `EMO-SOUND` | `EMO-SOUND-001` | 情绪声音与语音韵律 | 0 |
| `EMO-STRESS` | `EMO-STRESS-001` | 社会心理应激诱发（TSST／MIST） | 0 |
| `EMO-THREAT` | `EMO-THREAT-001` | 电击威胁预期 | 0 |
| `EMO-TOUCH` | `EMO-TOUCH-001` | 情感触觉（C 触觉纤维最适触摸） | 0 |
| `EMO-WORD` | `EMO-WORD-001` | 情绪词阅读 | 0 |
| `SOC-ANIM` | `SOC-ANIM-001` | 几何图形动画心智化（Frith-Happé 动画） | 0 |
| `SOC-BIO` | `SOC-BIO-001` | 生物运动知觉 | 0 |
| `SOC-CONF` | `SOC-CONF-001` | 社会从众 | 0 |
| `SOC-CYB` | `SOC-CYB-001` | 网络传球社会排斥（Cyberball） | 0 |
| `SOC-DICT` | `SOC-DICT-001` | 独裁者博弈 | 0 |
| `SOC-EYE` | `SOC-EYE-001` | 真人双向目光接触 | 0 |
| `SOC-GAZE` | `SOC-GAZE-001` | 目光线索与共同注意 | 0 |
| `SOC-IAT` | `SOC-IAT-001` | 内隐联想测验 | 0 |
| `SOC-IMIT` | `SOC-IMIT-001` | 模仿抑制（自动模仿） | 0 |
| `SOC-JA` | `SOC-JA-001` | 联合动作与人际协调 | 1 |
| `SOC-MORAL` | `SOC-MORAL-001` | 道德两难判断 | 0 |
| `SOC-NAME` | `SOC-NAME-001` | 自我名字范式 | 0 |
| `SOC-PAIN` | `SOC-PAIN-001` | 疼痛共情 | 0 |
| `SOC-RACE` | `SOC-RACE-001` | 种族与群体身份面孔分类 | 0 |
| `SOC-RME` | `SOC-RME-001` | 眼中读心测验 | 0 |
| `SOC-SELF` | `SOC-SELF-001` | 自我面孔识别 | 0 |
| `SOC-SFB` | `SOC-SFB-001` | 社会评价反馈（社会判断范式） | 0 |
| `SOC-TOM` | `SOC-TOM-001` | 心理理论（错误信念） | 1 |
| `SOC-TPP` | `SOC-TPP-001` | 第三方惩罚 | 0 |
| `SOC-TRUST` | `SOC-TRUST-001` | 信任博弈与囚徒困境 | 1 |
| `SOC-UG` | `SOC-UG-001` | 最后通牒博弈 | 0 |
| `SOC-VPT` | `SOC-VPT-001` | 视觉观点采择 | 0 |
| `SOC-WIT` | `SOC-WIT-001` | 武器识别任务 | 0 |
| `STA-ANES` | `STA-ANES-001` | 麻醉与意识水平 | 0 |
| `STA-CLAS` | `STA-CLAS-001` | 睡眠慢振荡闭环听觉刺激 | 0 |
| `STA-DREAM` | `STA-DREAM-001` | 系列唤醒梦境报告范式 | 0 |
| `STA-DRV` | `STA-DRV-001` | 模拟驾驶与持续警觉 | 0 |
| `STA-ENG` | `STA-ENG-001` | 自然视频与学习中的投入度 | 0 |
| `STA-HYPN` | `STA-HYPN-001` | 催眠诱导 | 0 |
| `STA-MATB` | `STA-MATB-001` | 多属性任务组（MATB） | 0 |
| `STA-MED` | `STA-MED-001` | 冥想 | 0 |
| `STA-MW` | `STA-MW-001` | 走神（思维探测） | 0 |
| `STA-NF` | `STA-NF-001` | 神经反馈训练 | 2 |
| `STA-PSY` | `STA-PSY-001` | 致幻剂药物状态 | 0 |
| `STA-PVT` | `STA-PVT-001` | 精神运动警觉任务（PVT） | 0 |
| `STA-REST` | `STA-REST-001` | 静息态（睁眼／闭眼） | 0 |
| `STA-SCP` | `STA-SCP-001` | 慢皮层电位自我调节 | 0 |
| `STA-SLP` | `STA-SLP-001` | 睡眠分期（多导睡眠图） | 0 |
