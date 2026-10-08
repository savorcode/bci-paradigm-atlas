# 例会决议（草案，待负责人确认）

> 起草：维护者（maintainer），2026-10-02（第 0 周）。依据：`decisions_pending.md`、`docs/methodology.zh-CN.md` §1–§2。
> 状态：**草案**。第一次例会逐条确认；确认后在各条标题后注明"（已确认 YYYY-MM-DD）"，被否决或修改的条目保留原文并追加修订说明，编号不复用。
> 同步：每条决议对应的候选已写入 `candidates.csv` 的 `decision` 与 `decision_ref` 列。
>
> **判定基准（方法说明 §1）**：修改若保留范式的核心逻辑，且**所诱发的标记物与所探测的构念都不变**，即为变体；二者任一改变，则为独立范式。仅改变刺激模态、呈现布局、刺激参数、解码粒度、记录方式或使用人群的，均按变体处理。
>
> **D-057 修订（已确认，2026-10-03）**：上述判定基准此后只用于判断是否为独立的**范式类**（`<范式族>-<简称>`）。同一范式类内，类别/条件集、刺激或提示类型（含编码方案）、试次结构、反馈方式任一改变即为新的**具体范式**（新序号），不再写成变体；`variants` 只记参数级变化。下列并入类决议将在 sprint 2 复核，见 D-057。
>
> **decision 取值**：`收录`（建条目）／`并入 <ID>`（不建文件，作为目标范式的 `variants` 条目）／`排除`（不在 v0.1–v1 范围）／`暂缓`（v0.1 不建条目，v1.0 前带新证据可重议）。

## 汇总

| 类别 | 决议 | 结果 |
|---|---|---|
| 分类体系 | D-001、D-022、D-027 | 心算留在 imagery；不新增 hybrid 族，STA-HYB-001 暂缓；DBS 局部场电位记为 `other` |
| 建议并入（7 项） | D-002 – D-008 | 7 项全部同意并入 |
| 建议排除（2 项） | D-009、D-010 | 2 项全部排除 |
| 独立性问题（11 项） | D-011 – D-021 | 并入 5 项（RSVP、下肢想象、音位辨别、音乐情绪、超扫描）；独立 8 个候选（TACT、SSMVEP、AWARE、LDT、PRIME、EST、SCP、NF） |
| 行为为主任务 | D-023 | 暂缓 4 项，排除 1 项，收录 2 项 |
| 维护者补充 | D-024、D-025 | 记得/知道 → 新旧再认；社会激励延迟 → 金钱激励延迟 |
| 其余候选与流程 | D-026、D-028 – D-030 | 其余全部收录；标记物登记表；写入范围；并入的处理方式 |

结果：209 个候选中 **收录 187、并入 14、排除 3、暂缓 5**。

| 包 | 收录 | 并入 | 排除 | 暂缓 |
|---|---|---|---|---|
| A 感知与稳态 | 41 | 4 | 0 | 1 |
| B 运动、想象与刺激 | 34 | 5 | 2 | 0 |
| C 错误监测与认知控制 | 35 | 0 | 0 | 2 |
| D 记忆与语言 | 38 | 2 | 1 | 1 |
| E 情绪、社会与脑状态 | 39 | 3 | 0 | 1 |

---

## 一、分类体系

### D-001 心算归入"非运动想象"族
- **问题**：IMG-MA-001 心算并非严格意义上的"想象"，应归 imagery 还是 control？
- **决定**：暂归 `imagery` 族，ID 保持 IMG-MA-001，在 `notes` 中注明"主动心理任务，非感知性想象"。心理旋转（IMG-ROT-001）、词语联想与生成（IMG-WORD-001）照此处理。v1.0 前再评估是否把 imagery 族改名为"非运动想象与心理任务"，或新增"心理任务"族。
- **理由**：在 BCI 中，心算与运动想象、空间导航想象等一起作为用户主动完成、无外部刺激的"心理任务"使用（fNIRS/EEG 多类心理任务 BCI），标记物（前额 HbO、额中线 θ）与使用场景都与 imagery 族接近。control 族的范式都以外部刺激–反应冲突或规则切换为核心，心算不符合。
- **影响**：IMG-MA-001、IMG-ROT-001、IMG-WORD-001（包 B）。

### D-022 混合 BCI 不新增范式族，STA-HYB-001 暂缓
- **问题**：STA-HYB-001 混合 BCI 在现有 12 个族中没有对应族：新增 `hybrid` 族，还是改为跨族标签？
- **决定**：
  1. v0.1 **不新增** `hybrid` 族，`taxonomy/families.yaml` 不变。
  2. STA-HYB-001 **暂缓**，不建条目，ID 保留不复用。
  3. 混合 BCI 作为**跨族标记**，记录在各组成范式条目的 `variants` 中：变体名以 `Hybrid:` 开头并写出另一组成范式的 ID，例如在 SSR-SSVEP-001 中写 `name: "Hybrid: SSVEP + motor imagery (MOT-MI-001)"`，附该混合系统的文献作为 `source`。每个组成范式各记一次。
  4. 引入非脑信号（EOG、EMG、眼动）的混合系统同样写在变体里，但非脑信号不进 `recording_modality`。
  5. 在 schema 0.3 提议中提出增加可选的 `tags` 字段（如 `hybrid`、`hyperscanning`、`closed_loop`），届时把 `Hybrid:` 变体机器化迁移。
- **理由**：混合 BCI 是若干范式的**组合方式**，本身不诱发新的标记物，也不探测新的构念，不满足"范式"的定义（§1）；作为一个族，它会与所有其他族交叉，破坏"一个范式只属于一个族"的分类原则。把组合写在组成范式的变体里，既保留了信息，又不需要改 schema。
- **影响**：STA-HYB-001（包 E）；所有包在写变体时遵守 `Hybrid:` 命名约定。

### D-027 DBS 电极局部场电位与非脑信号的记录模态
- **问题**：候选表中出现了 `recording_modality.yaml` 之外的模态：STM-DBSEP-001 的 `LFP`（经 DBS 电极记录），STA-HYB-001 的 `EOG`。
- **决定**：经外化 DBS 电极记录的皮层下局部场电位，v0.1 记为 `other`，并在 `notes` 中写明"DBS lead LFP"；在下一版词表讨论中提议新增 `DBS-LFP`（或 `subcortical_LFP`）。EOG、EMG 等非脑信号不作为记录模态（STA-HYB-001 已暂缓）。
- **理由**：词表变更须经例会，第 0 周不改 taxonomy；`other` 可通过校验且不丢信息。
- **影响**：STM-DBSEP-001、MK.ERNA（包 B）。

## 二、建议并入（7 项）

### D-002 闪光光驱动并入 SSVEP
- **问题**：SSR-PD-001 闪光光驱动是否独立成条？
- **决定**：并入 SSR-SSVEP-001，作为变体"Photic driving (clinical intermittent photic stimulation)"；别名"photic driving"加入 SSVEP 条目的 `aliases`。
- **理由**：光驱动是临床脑电对闪烁诱发的稳态视觉响应的叫法，刺激、机制和标记物（MK.SSVEP）相同，探测的仍是视觉通路对周期刺激的跟随。
- **影响**：SSR-PD-001 不建文件；包 A 在 SSR-SSVEP-001 中补变体。

### D-003 多目标频率标记注意并入 SSVEP
- **问题**：SSR-FT-001 多目标频率标记注意是否独立成条（区分认知研究与 BCI 控制）？
- **决定**：并入 SSR-SSVEP-001，作为变体"Frequency-tagged attention to multiple concurrent stimuli"。
- **理由**：标记物相同（MK.SSVEP），构念也相同：MK.SSVEP 已登记的构念就是"对被注意刺激的持续视觉注意"（Morgan et al. 1996 正是频率标记注意研究）。认知研究与 BCI 控制的区别是**用途**，由 `bci_category` 表达，不构成独立范式。
- **影响**：SSR-FT-001 不建文件。注意与 SSR-FPVS-001 区分：FPVS 的 oddball 频率响应标记的是类别辨别，另立 MK.FPVS_oddball，保持独立。

### D-004 高频/不可见 SSVEP 并入 SSVEP
- **问题**：SSR-SSVEPHF-001 是否独立成条？
- **决定**：并入 SSR-SSVEP-001，作为变体"High-frequency / imperceptible-flicker SSVEP"。
- **理由**：只改变了刺激频率（刺激参数），标记物与构念不变。
- **影响**：SSR-SSVEPHF-001 不建文件。

### D-005 单指运动解码并入运动执行
- **问题**：MOT-FING-001 是否独立成条？
- **决定**：并入 MOT-ME-001，作为变体"Individual finger movements (ECoG/intracortical finger decoding)"。
- **理由**：任务仍是运动执行，标记物（MK.high_gamma、MK.SMR_ERD）与构念（运动执行）不变，区别只在解码粒度。
- **影响**：MOT-FING-001 不建文件；其高 γ 文献线索由包 B 用于 MOT-ME-001 的变体与 MK.high_gamma。

### D-006 音乐想象并入听觉想象
- **问题**：IMG-MUS-001 是否独立成条？
- **决定**：并入 IMG-AUD-001，作为变体"Musical imagery"。
- **理由**：音乐想象是听觉想象的子类，标记物（听皮层 BOLD、颞区高 γ）与构念（听觉表象）相同；该候选也没有任何文献线索。
- **影响**：IMG-MUS-001 不建文件；包 B 补检音乐想象文献作为变体出处。

### D-007 面孔与场景想象并入视觉想象
- **问题**：IMG-FACE-001 是否独立成条？
- **决定**：并入 IMG-VIS-001，作为变体"Category-specific imagery (faces / places)"；IMG-VIS-001 的标记物列表加入 MK.BOLD_category_selective。
- **理由**：属于类别特异性的视觉想象，构念不变；FFA/PPA 激活是视觉表象在腹侧视觉皮层的类别特异表现，已作为 MK.BOLD_category_selective 登记（与 PER-CAT-001、PER-FACE-001 共用），不需要独立范式。
- **影响**：IMG-FACE-001 不建文件。

### D-008 空间导航想象并入指令跟随想象
- **问题**：IMG-NAV-001 是否独立成条？
- **决定**：并入 IMG-CMD-001，作为变体"Spatial navigation imagery (house navigation)"；在 BCI 中单独使用导航想象的研究（fMRI/fNIRS 多类心理任务 BCI）也记在该变体下。
- **理由**：导航想象主要作为 Owen et al. 指令跟随范式的第二个任务使用；IMG-CMD-001 的标记物已包含海马旁回/导航网络 BOLD（MK.BOLD_parahippocampal），构念（意图性心理表象）相同。
- **影响**：IMG-NAV-001 不建文件。

## 三、建议排除（2 项）

### D-009 排除皮层内微刺激感觉反馈
- **问题**：STM-ICMS-001 的主要读出是被试的知觉报告，是否满足纳入标准 3？
- **决定**：排除（v0.1–v1）。ID 保留不复用。在 MOT-GRASP-001、MOT-CURSOR-001 的 `notes` 中可提及"双向 BCI 中的 ICMS 感觉反馈"作为背景。
- **理由**：ICMS 是向大脑**写入**信息，其结果以知觉报告与行为表现度量；刺激伪迹也使同步记录的神经响应难以作为成熟标记物。不满足纳入标准 3。若将来 schema 引入"写入/刺激型范式"，再统一讨论。
- **影响**：STM-ICMS-001（包 B）。

### D-010 排除皮层电刺激功能定位
- **问题**：STM-ECS-001 读出的是行为（言语中断、运动），是否满足纳入标准 3？
- **决定**：排除。
- **理由**：电刺激功能定位以行为反应为读出，不记录可分析的诱发神经活动，不满足纳入标准 3。用同类电极做单脉冲刺激并**记录**诱发响应的范式已作为 STM-CCEP-001 收录，覆盖了这一方向的神经记录部分。
- **影响**：STM-ECS-001（包 B）；包 B 可在 STM-CCEP-001 的 `notes` 中注明二者区别。

## 四、独立性问题（11 项）

### D-011 RSVP 并入 Oddball
- **问题**：PER-RSVP-001 标记物与 Oddball 相同（P3b），但时间结构不同，是否独立？
- **决定**：并入 PER-ODD-001，作为变体"Rapid serial visual presentation (RSVP) target detection"（含 RSVP 打字与图像检索 BCI），与已有的 P300 speller 变体并列；`RSVP`、`RSVP-BCI` 加入 Oddball 条目的 `aliases`。
- **理由**：RSVP 目标检测的核心逻辑仍是"低频靶刺激嵌入高频非靶序列"，诱发的标记物（MK.P3b，以及随之出现的 N2）与构念（靶检测/情境更新）不变；时间结构（高速呈现、ERP 重叠）属于呈现参数。P300 speller 已按同样逻辑处理为变体，保持一致。BCI 使用者可通过别名和变体检索到它。
- **影响**：PER-RSVP-001 不建文件；其文献线索由包 A 用于 PER-ODD-001。候选别名中的注意瞬脱类任务（AB Task、Dual-Target RSVP）属于 PER-AB-001，不进 Oddball。

### D-012 触觉空间注意独立成条
- **问题**：PER-TACT-001 与 Oddball 及 SSSEP 的关系？
- **决定**：独立收录，范围限定为"瞬态体感 ERP 的触觉空间注意"（核心标记物 MK.N140_somatosensory 的注意调制，兼有 MK.P3b）。其中：触觉 P300 BCI（对一个触觉部位的低频刺激计数）作为 PER-ODD-001 的变体；稳态振动刺激下的触觉注意作为 SSR-SSSEP-001 的变体。
- **理由**：触觉空间注意探测的是体感通道的空间选择性注意，其特征标记物（N140 注意效应）不同于 Oddball 的 P3b 与 SSSEP 的稳态响应，满足独立条件；而另外两类做法与目标范式标记物、构念一致，按变体处理。
- **影响**：PER-TACT-001 收录（包 A）；PER-ODD-001、SSR-SSSEP-001 各增一个变体。

### D-013 稳态运动 VEP 独立成条
- **问题**：SSR-SSMVEP-001 刺激由闪烁换成运动，是否构成独立范式？
- **决定**：独立收录，标记物另立 MK.SSMVEP（不使用 MK.SSVEP）。
- **理由**：运动翻转刺激主要驱动背侧通路（MT/V5），产生的稳态响应在发生源、频谱特征（谐波结构、低对比度和低视觉疲劳）上与亮度闪烁 SSVEP 不同，属于不同标记物；与 PER-MVEP-001（瞬态运动起始 VEP）的关系类似 SSVEP 之于闪光 VEP。
- **影响**：SSR-SSMVEP-001（包 A）。若策展人在核对中发现文献普遍把 SSMVEP 视为 SSVEP 的一种，可在例会提出重议。

### D-014 下肢运动想象与步态并入运动想象
- **问题**：MOT-GAIT-001 是否作为运动想象的变体？
- **决定**：并入 MOT-MI-001，作为变体"Lower-limb / foot motor imagery"。候选中涉及实际行走的步态脑电研究，作为 MOT-ME-001 的变体"Overground / treadmill walking"。
- **理由**：足部/下肢想象诱发中线（Cz 附近）SMR ERD/ERS，与手部想象是同一标记物（MK.SMR_ERD）的不同躯体定位，构念不变；只是改变了想象的肢体。
- **影响**：MOT-GAIT-001 不建文件；包 B 在 MOT-MI-001、MOT-ME-001 中各补一个变体。

### D-015 错误觉知独立成条
- **问题**：ERR-AWARE-001 是否作为 Flanker 或反向眼跳范式的附加测量？
- **决定**：独立收录，标记物 MK.Pe。
- **理由**：错误觉知探测的构念（对错误的有意识觉察）与 Flanker 的冲突/错误检测（ERN）不同；Pe 在觉知与未觉知错误之间的差异是其特征标记；且有专门设计的范式（如 Error Awareness Task），不只是附加测量。Flanker 与反向眼跳中的觉知报告写入 ERR-AWARE-001 的变体。
- **影响**：ERR-AWARE-001（包 C）；MK.Pe 由包 C 编写，CTL-FLK-001 引用。

### D-016 词汇判断与语义启动分别收录
- **问题**：LAN-LDT-001 与 LAN-PRIME-001 是否合并？
- **决定**：不合并，分别收录，并划定边界：
  - LAN-LDT-001 词汇判断：单词呈现、词/假词判断，操纵词汇性、词频等，探测词汇通达；
  - LAN-PRIME-001 语义启动：启动词–目标词配对、操纵二者关联，探测语义记忆/关联激活；**响应任务不限**（词汇判断、语义判断或被动阅读都算），用词汇判断作响应的启动研究归 PRIME。
  - 两条目 `notes` 中互相引用。
- **理由**：二者共用 N400（MK.N400），但探测的构念不同（词汇通达 vs 语义关联激活），按 §1 应为独立范式；两者也各有独立的 HED 任务页和文献脉络。
- **影响**：LAN-LDT-001、LAN-PRIME-001（包 D）。

### D-017 音位辨别并入被动 oddball（MMN）
- **问题**：LAN-PHON-001 是否作为 MMN 的语言变体？
- **决定**：并入 PER-MMN-001，作为变体"Speech-sound / phoneme-contrast MMN"（含母语与非母语音位对比）。
- **理由**：范式结构（被动 oddball）与标记物（MK.MMN）相同；音位 MMN 反映的仍是听觉变化检测/预测误差，"语言特异的记忆痕迹"是对同一构念在语音刺激上的解释，写在变体说明中即可。
- **影响**：LAN-PHON-001 不建文件。**跨包**：目标范式属包 A，包 D 把 LAN-PHON-001 的文献线索在本包 worklog 中列出交给包 A（D-030）。LAN-PHA-001 语音意识不受影响，仍收录。

### D-018 音乐/音乐视频情绪诱发并入情绪影片诱发
- **问题**：EMO-MUS-001 与 EMO-FILM-001 两种情绪诱发是否合并？
- **决定**：合并，保留 EMO-FILM-001（ID 不变），条目名称扩为"自然刺激情绪诱发（影片、音乐、音乐视频）/ Naturalistic emotion elicitation (film, music, music video)"；音乐与音乐视频诱发作为变体（DEAP、AMIGOS 等数据集记入 `datasets`）。
- **理由**：二者都是用自然刺激诱发持续情绪状态，标记物（额叶 α 不对称、情绪相关频段功率）与构念（情绪效价/唤醒）相同，区别只是刺激模态，按 §1 属于变体。保留 FILM 是因为 SEED 等影片范式文献更早、更成体系。EMO-AUTO-001 自传体回忆情绪诱发无外部刺激，仍独立。
- **影响**：EMO-MUS-001 不建文件；包 E 写 EMO-FILM-001 时使用扩展后的名称。

### D-019 情绪 Stroop 独立成条
- **问题**：EMO-EST-001 是否作为 Stroop 的变体？
- **决定**：独立收录。
- **理由**：情绪 Stroop 不存在颜色–词义的反应冲突，干扰来自情绪词的注意捕获；标记物（LPP、早期 ERP 调制）与构念（情绪注意偏向）都不同于经典 Stroop 的 N450 与冲突控制。
- **影响**：EMO-EST-001（包 E）；CTL-STR-001 不加情绪 Stroop 变体。

### D-020 慢皮层电位自我调节与神经反馈分别收录
- **问题**：STA-SCP-001 是否作为神经反馈（STA-NF-001）的子类？
- **决定**：分别收录。
  - STA-SCP-001：慢皮层电位自我调节（思维翻译装置），标记物 MK.SCP，`bci_category: active`。
  - STA-NF-001：以节律或血流信号为反馈对象的神经反馈训练（伞形条目），标记物先登记 MK.SMR_ERD、MK.alpha_posterior；以其他信号为反馈对象的做法（θ/β、rtfMRI 脑区 BOLD、fNIRS）写成变体，必要时经 `marker_requests.csv` 申请标记物。
- **理由**：SCP 是独立的标记物（慢电位而非节律），且 SCP-BCI 有独立的源头和数据；而"神经反馈"按反馈对象的不同可对应多种标记物，适合作伞形条目。二者标记物不同，按 §1 应分立。
- **影响**：STA-SCP-001、STA-NF-001（包 E）。

### D-021 超扫描协作并入联合动作
- **问题**：SOC-HYP-001 超扫描与 SOC-JA-001 联合动作是否合并？
- **决定**：合并，保留 SOC-JA-001，名称扩为"联合动作与人际协调 / Joint action and interpersonal coordination"；超扫描协作任务作为变体，标记物包括 MK.interbrain_synchrony。
- **理由**：超扫描是**记录配置**（同时记录两人以上），不是任务；按 §1，范式由刺激、任务与时序定义。现有超扫描协作研究的任务多为协同按键、节拍同步等联合动作，标记物（脑间同步）与构念（人际协调）与 SOC-JA-001 一致。在其他社会范式（信任博弈、最后通牒等）中使用超扫描时，写在对应范式的变体中，变体名以 `Hyperscanning:` 开头（与 D-022 的 `Hybrid:` 约定相同）。
- **影响**：SOC-HYP-001 不建文件；其文献线索并入 SOC-JA-001（包 E）。

## 五、以行为测量为主的任务

### D-023 纳入标准 3 的执行口径与 7 个行为为主任务
- **问题**：PER-UFOV-001、CTL-DSST-001、CTL-RAVEN-001、CTL-TMT-001、MEM-OSPAN-001、LAN-SPR-001（候选表中标注"以行为测量为主"的 6 项）以及维护者补查的 MEM-DS-001，是否有成熟的神经标记物？
- **决定**：
  - **口径**："成熟的神经标记物"指：至少 2 项独立的、同行评议的人类神经记录研究，用该任务的标准操纵报告了方向一致的神经效应，且该效应可落到登记表中的一个标记物上。仅有"任务时某脑区激活"的单项研究不够。
  - 结论：

| 候选 | 决定 | 说明 |
|---|---|---|
| PER-UFOV-001 有效视野 | 暂缓 | 未见稳定的神经标记物 |
| CTL-DSST-001 数字符号替换 | 暂缓 | 少量 fMRI 研究，无特征性标记物 |
| CTL-TMT-001 连线测验 | 暂缓 | 少量 fNIRS/fMRI 研究，纸笔测验的计算机化版本差异大 |
| MEM-OSPAN-001 操作广度 | 暂缓 | 主要作为工作记忆容量的行为测量；神经研究多改用 n-back/Sternberg |
| LAN-SPR-001 自定步速阅读 | 排除 | 本质是行为（阅读时间）方法；其神经记录对应做法（逐词呈现 ERP）已由 LAN-SC-001、LAN-N400-001、LAN-P600-001 覆盖 |
| CTL-RAVEN-001 瑞文推理 | 收录（P3） | 矩阵推理的额顶网络激活有多项独立 fMRI 研究，标记物 MK.BOLD_frontoparietal |
| MEM-DS-001 数字广度 | 收录（P3） | 标记物 MK.frontal_midline_theta；第一遍结束时若仍不满足上述口径，转为暂缓 |

  - 被暂缓的候选：策展人在常规检索中若发现满足口径的文献，记入本包 `status.csv` 的 `blockers` 列并在例会上提出，可恢复收录。
- **理由**：方法说明 §2 第 3 条要求范式至少诱发一种可在知识库中记录的标记物；用统一口径可以避免按个人印象逐个判断。暂缓而非排除，是因为 S-001 检索受限，尚不能断言这些任务没有神经研究。
- **影响**：包 A 1 项、包 C 3 项、包 D 3 项。

## 六、维护者补充事项

### D-024 记得/知道并入新旧再认（维护者提议）
- **问题**：MEM-RK-001 记得/知道与 MEM-ON-001 新旧再认的标记物完全相同（FN400、顶叶新旧效应），是否独立？
- **决定**：并入 MEM-ON-001，作为变体"Remember/know judgements"。
- **理由**：记得/知道只是改变了再认判断的报告方式；FN400 与顶叶新旧效应本身就是熟悉性与回忆的标记物，R/K 范式探测的构念与新旧再认相同。MEM-SRC-001 来源记忆有独立标记物（晚期右额效应），MEM-DRM-001 探测错误记忆这一不同构念，均保持独立。
- **影响**：MEM-RK-001 不建文件（包 D）。

### D-025 社会激励延迟并入金钱激励延迟（维护者提议）
- **问题**：SOC-SID-001 社会激励延迟是否独立？
- **决定**：并入 EMO-MID-001，作为变体"Social incentive delay (social reward cues)"。
- **理由**：SID 是 MID 的直接改编，只把金钱奖赏换成社会性奖赏（笑脸、赞许），标记物（纹状体奖赏 BOLD）与构念（奖赏预期）不变，属于刺激改变。
- **影响**：SOC-SID-001 不建文件；EMO-MID-001 由包 E 编写，同包处理。

## 七、其余候选与流程

### D-026 确认其余候选收录
- **问题**：未在上述各条中讨论的候选（含 S-001 中标为"收录（新增，待确认）"的 HED 来源候选）是否收录？
- **决定**：全部确认 `收录`（共 187 个收录，含 D-012、D-013、D-015、D-016、D-018 – D-021、D-023 中确认的独立条目）。"新增，待确认"标记取消；P3 长尾范式按计划在第二遍补骨架。
- **理由**：这些候选在任务单中都列出了可能的标记物，初看满足纳入标准；第一遍核对中若发现不满足（例如找不到任何神经记录研究），按 D-023 的口径提出暂缓。
- **影响**：`candidates.csv` 中这些行的 `decision_ref` 为 D-026。

### D-028 神经标记物登记表与规范命名
- **问题**：209 个候选的 `likely_markers` 是自由文本，同一标记物有多种叫法；5 个包并行编写，需要统一的标记物 ID 和归属。
- **决定**：
  1. 以 `curation/registry/markers.csv` 为标记物的**唯一登记表**（本次 111 个），`curation/registry/paradigm_markers.csv` 给出每个收录范式**必须使用**的标记物 ID。策展人填写 `markers` 字段时只能使用登记表中的 ID。
  2. **归属规则**：标记物由 `candidates.csv` 行序中第一个使用它的收录候选所在的包负责编写（`owner_pkg`），其他包只引用。维护者已为全部新标记物建立骨架文件，owner 直接覆盖。
  3. **同义词归并**（节选，完整见登记表 notes 列）：P300/P3 → MK.P3b；mu 抑制、中线 SMR ERD、运动相关 β 调制 → MK.SMR_ERD；RewP、MFN → MK.FRN；光驱动、频率标记（视觉闪烁）→ MK.SSVEP；准备电位 → MK.MRCP。
  4. **区分**而非归并的：MK.alpha_posterior（后部 α 功率）、MK.alpha_lateralization（α 偏侧化）、MK.frontal_alpha_asymmetry（额叶 α 不对称）、MK.frontal_alpha_anesthesia；MK.frontal_midline_theta 与 MK.theta_drowsiness；MK.high_gamma（颅内）与 MK.gamma_power（头皮）；MK.N2_frontocentral（冲突/抑制）与 MK.N2_posterior；MK.P3b 与 MK.NoGo_P3；MK.SSVEP、MK.SSMVEP、MK.FPVS_oddball。
  5. **血流动力学标记物按脑区/网络分组**（如 MK.BOLD_striatum_reward、MK.BOLD_dlPFC、MK.BOLD_vmPFC_value、MK.HbO_prefrontal），具体子区在 `generators` 与 `relation` 中说明，不为每个任务单设 BOLD 标记物。以 `BOLD_` 命名但登记了 fNIRS 的（如 MK.BOLD_frontoparietal、MK.BOLD_motor_network），fNIRS 测得的同区 HbO 归入该标记物。
  6. 不登记的：分析方法（编码模型、MVPA、TRF 本身）、无法落到具体信号的描述（"节律调制""多标记物组合""被训练节律"）。
  7. **新增标记物**：策展人在本包 `marker_requests.csv` 中申请，写明规范 ID、类型、模态、理由；若登记表中没有同义项，可在本包 PR 中直接建文件（成为其 owner），维护者合并时把它补进登记表。对已登记标记物的修改（如为 MK.SMR_ERD 补充"动作理解"构念）由使用包向 owner 提出。
- **理由**：同一信号多种叫法会让图谱出现重复节点；先建登记表可避免 5 个包各自创建同义标记物，也让第一遍骨架 PR 能直接通过校验。
- **影响**：所有包；`knowledge/markers/` 新增 107 个骨架文件（4 个已有文件不变）。

### D-029 策展人写入范围
- **问题**：5 个包并行提交，需要避免互相覆盖与冲突。
- **决定**：策展人只能写：
  1. `paradigms/<本包的族>/*`（A：perception、steady_state；B：motor、imagery、stimulation；C：error、control；D：memory、language；E：emotion、social、state）；
  2. `knowledge/markers/` 中 `owner_pkg` 为本包的文件，以及本包新申请且登记表中不存在的标记物文件；
  3. `curation/work/pkg_<X>/*`。

  不得修改：`curation/candidates.csv`、`curation/registry/*`、`knowledge/regions.yaml`、`knowledge/constructs.yaml`、`taxonomy/*`、`schema/*`、`scripts/*` 以及其他包的文件。需要新增脑区或构念、修改候选或登记表的，写入本包 worklog 并在例会提出，由维护者统一修改。
- **理由**：共享文件由维护者单点写入，可避免并行 PR 冲突；每个包的进度、检索记录和新候选放在本包目录，维护者每周汇总进 `candidates.csv` 与 `search_protocol.md`。
- **影响**：所有包；PR 模板中加入写入范围自查项。

### D-030 并入候选的处理方式
- **问题**：被并入的候选如何体现在图谱中？
- **决定**：
  1. 被并入的候选**不建文件**，在目标范式的 `variants` 中写一条变体（`name` 用英文，必须有 `source`），候选的英文名或常用别名加入目标范式的 `aliases`。
  2. 被并入候选的 ID **作废但不复用**；`candidates.csv` 的 `status` 标为"不建条目（作为变体）"。
  3. 变体由**目标范式所在包**编写。跨包并入（D-017：LAN-PHON-001 → PER-MMN-001）时，原包在本包 worklog 中列出交接的文献线索（R 编号），目标包写入。
  4. 被并入候选的 `likely_markers` 若有目标范式没有的标记物，已在 `paradigm_markers.csv` 中合并进目标范式（如 IMG-VIS-001 加入 MK.BOLD_category_selective）。
- **理由**：保持"变体 = 同一范式"的数据模型，同时不丢失候选上的文献与检索名称。
- **影响**：14 个被并入候选及其 12 个目标范式（SSR-SSVEP-001、MOT-ME-001、MOT-MI-001、IMG-AUD-001、IMG-VIS-001、IMG-CMD-001、PER-ODD-001、PER-MMN-001、EMO-FILM-001、SOC-JA-001、MEM-ON-001、EMO-MID-001）。

---

## 下次例会候议（不影响本次判定）

维护者在整理登记表时注意到以下几对候选标记物与构念高度重叠，第一遍中请相关策展人留意，第二次例会讨论是否并入：

- ERR-TE-001 时间估计 与 ERR-GAM-001 赌博反馈（均为 MK.FRN，结果评价）
- MEM-SME-001 后续记忆效应 与 MEM-FR-001 自由回忆（SME 是一种分析设计，可用于任何编码任务）
- MOT-SRT-001 序列反应时 与 MOT-MSL-001 运动序列学习（内隐 vs 外显）
- CTL-SART-001 SART 与 CTL-GNG-001 Go/NoGo（均为 MK.NoGo_P3）
- SSR-SWEEP-001 扫描 VEP 与 SSR-SSVEP-001（同一标记物，构念为视敏度阈值）

---

# 第一遍骨架冲刺（sprint 1）合并后的决议草案 D-031 – D-056

> 起草：维护者（maintainer），2026-10-03，合并 `curation/pkg-A` – `curation/pkg-E` 之后。依据：5 个包的 `worklog.md`、`status.csv`、`new_candidates.csv`、`marker_requests.csv`、`search_log.md` 以及维护者的跨包查重（名称、别名、ID、标记物集合比较）。
> 状态：以下各条均为 **草案，待负责人确认**。标为"已执行"的，维护者已在 `integration` 分支上按草案修改了文件（可回退）；标为"仅记录"的，文件未改，等例会决定。
> 编号规则沿用 D-001 – D-030：被否决的条目保留原文并追加修订说明，编号不复用。

## 汇总

| 类别 | 决议 | 执行情况 |
|---|---|---|
| 出处规则 | D-031、D-032、D-055 | 源头与首个神经记录研究的区分（`notes` 约定，schema 0.3 提议 `first_neural_source`）；TBD 的写法与集中补源；文献线索 QA 标记 |
| 状态取值 | D-033 | 统一 status.csv 与 candidates.csv 的状态词 |
| 跨包重复（已合并） | D-034 – D-036 | STA-CLAS / STM-CLAS、MEM-CIT / SOC-CIT、IMG-WORD → LAN-VF：各保留 1 个文件，另 3 个 ID 作废 |
| 跨包/包内边界（保留文件） | D-037 – D-043 | 11 组相邻范式，各自给出倾向，待例会 |
| 策展人提议的变体 | D-044 | MEM-DE-001 → MEM-CD-001、LAN-SIGN-001 → LAN-SC-001 |
| 分类体系 | D-045 – D-049 | 新增草案词条 `pharmacological`、`optical_stimulation`；建 STM-PBM-001；DBS-LFP、内感受、价值决策族、族归属 |
| 标记物 | D-050 – D-052 | 18 个新申请标记物登记；PET 归入血流动力学标记物；PEN、创造力 α、IFG 等问题 |
| 候选与流程 | D-053、D-054、D-056 | 85 个新候选的处理；种子条目格式；CTL-STR-001 别名冲突 |
| 标识符与粒度（已确认） | D-057 | 两级 ID：范式类 `<族>-<简称>` 与具体范式 `<族>-<简称>-<序号>`；4 条给号准则；schema 0.2 |

---

## 八、出处规则

### D-031 范式源头与首个神经记录研究的区分
- **问题**：多个包的 `first_source` 只能找到行为学或 EMG/MEP 研究（B：MOT-SACC Javal 1878、MOT-BIMAN、MOT-SRT、MOT-MIRR、IMG-ROT 为行为学；STM-PAS、STM-TDCS、STM-PHTMS 为 MEP），或者反过来，填的是较晚的神经研究而不是范式源头（E：SOC-CYB、SOC-SELF、SOC-VPT、SOC-TPP、EMO-SOUND、STA-MED、STA-HYPN、STA-PSY、EMO-THREAT 共 9 条）。另有源头"弱"的：PER-CAT-001（R0059 为理论章节）、SSR-FFR-001（Worden & Marsh 1968 可能不是人类记录）、PER-OLF-001（R0046 为动物嗅球研究，未采用）、MEM-DMS-001 与 MEM-NAV-001（源头为动物研究）。
- **决定**：
  1. `first_source` 指**第一次描述该任务程序（刺激、任务、时序）的出版物**，可以是行为学研究、临床测验手册或 EMG/MEP 研究，不要求有神经记录。理论文章、综述、只"提到"现象而没有任务程序的文献（如 Javal 1878 之于眼跳任务）不算源头，只能作占位并标记 `qa_flag=weak_origin`。
  2. 源头是动物研究的，若人类版本的程序有明确的首篇文献，用人类首篇作 `first_source`，动物研究写入 `notes`；否则保留动物源头并在 `notes` 注明"animal origin"。
  3. 若首个**人脑**记录研究（EEG/MEG/fNIRS/fMRI/PET/颅内）与源头不是同一篇，在 `notes` 中单起一句：`First neural recording: <引文> (R####)`。MEP 是外周肌电读出，不算人脑记录。
  4. 已填为"较晚神经研究"的 9 条（包 E），本轮不改 `first_source`，`notes` 中已追加 D-031 说明；第二遍把它们移到 `First neural recording:` 一句，并补源头。
  5. schema 0.3 提议中新增可选字段 `first_neural_source`（结构与 `source` 相同），届时把 `First neural recording:` 句机器化迁移。**本次不改 schema。**
- **理由**：范式的定义（方法说明 §1）以刺激–任务–时序为核心，任务的发明常早于神经记录；把两者混在一个字段里，会让"源头"统计失真。用 `notes` 中固定句式记录，不需要改 schema，迁移时可用正则提取。
- **影响**：已执行——在 MOT-SACC-001、MOT-BIMAN-001、MOT-SRT-001、MOT-MIRR-001、IMG-ROT-001、STM-PAS-001、STM-TDCS-001、STM-PHTMS-001、PER-CAT-001、SSR-FFR-001 和包 E 的 9 条的 `notes` 中追加了 D-031 说明。MOT-OBS-001（R0995 TMS-MEP 为源头、R0845 MEG 在 notes）与本规则一致，维持。ERR-AWARE-001 选 R0195 而非 R0094（ERN 源头）符合第 1 款，维持。

### D-032 TBD 源头的写法与集中补源
- **问题**：合并后 37 个条目 `first_source.citation` 为 TBD（A 27、C 1、D 7、E 2；B 0）。各包写法不一。
- **决定**：
  1. 统一写法：`citation: 'TBD: <一句原因>'`，不填 `doi`/`year`，`verified: false`；`status.csv` 记为"阻塞"。校验脚本不区分 TBD，QA 报告与覆盖度报告单独统计（`scripts/coverage_report.py`）。
  2. 第二冲刺开头由维护者在有数据库访问（PubMed/Europe PMC 机构访问或 Zotero 群组库）时集中补源，策展人不再为 TBD 消耗 WebSearch 配额；补源结果经 `literature.csv` 分配 R 编号后再写入条目。
  3. 列表见 `curation/reports/coverage_M1.md`。
- **理由**：S-002 中 PubMed 检索页、E-utilities、Europe PMC、Crossref 检索接口普遍返回 403/429 或被 robots 禁止（见 `search_protocol.md` S-002），继续在受限渠道上检索效率很低。
- **影响**：37 个条目；包 A 负担最重（临床诱发电位类范式 ABR、AEP、PRVEP、FVEP、GATE 等）。

## 九、状态取值

### D-033 统一进度状态词
- **问题**：各包 README 规定 `status.csv` 的 status 取"待认领 / 编写中 / 待审核 / 已合并（骨架）/ 已审核（完整）/ 提请暂缓"，而本冲刺指令要求用"第一遍完成 / 阻塞"，C、D 在 worklog 中指出了不一致；`candidates.csv` 的 status 另有"不建条目（作为变体）"等写法。
- **决定**：从里程碑 M1 起，`candidates.csv` 的 `status` 只用以下取值：
  - `待认领`：未开始；
  - `第一遍完成`：骨架文件已合并，校验通过，无阻塞；
  - `阻塞`：骨架文件已合并，但 first_source 为 TBD 或有待例会的问题（原因写在 `status.csv` 的 blockers）；
  - `并入`：不建文件，作为目标范式变体（含原"不建条目（作为变体）"以及本次因重复而作废的 ID）；
  - `排除`；`暂缓`（含"提请暂缓"）。
  
  第二遍再增加 `待审核`、`已审核`。各包 `status.csv` 沿用本冲刺取值，README 表格在第二冲刺开工前由维护者改写。
- **理由**：一个列一套词，统计和看板才能直接用；冲刺内的取值已经被 5 个包一致使用，改动最小。
- **影响**：已执行——`candidates.csv` 全部 294 行按各包 `status.csv` 更新。

## 十、跨包重复（已合并）

### D-034 闭环听觉刺激：保留 STA-CLAS-001，作废 STM-CLAS-001
- **问题**：包 B（STM-CLAS-001，stimulation 族）和包 E（STA-CLAS-001，state 族）各自把"睡眠慢振荡闭环听觉刺激"作为新候选建了文件，名称、标记物（MK.slow_wave、MK.sleep_spindle）、源头（Ngo et al. 2013）完全相同。
- **决定**：保留 **STA-CLAS-001**（state 族），合并两份别名与贡献者，`notes` 中记录 B 的检索线索 N16；STM-CLAS-001 文件删除，ID 作废不复用，candidates.csv 中记为"并入 STA-CLAS-001"。与 MEM-TMR-001 互不并入：TMR 回放与记忆内容相关的线索，CLAS 使用无内容的声音、依相位定时，二者构念不同（记忆巩固的内容特异性 vs 睡眠慢振荡本身）。
- **理由**：刺激是普通听觉刺激而非脑刺激设备，被调节和读出的都是睡眠状态标记物，归 state 与 STA-SLP-001、STA-DREAM-001 相邻；stimulation 族的条目都以电、磁、超声等直接作用于神经组织的刺激为核心。
- **影响**：已执行。包 B、E。

### D-035 隐匿信息测试：保留 MEM-CIT-001，作废 SOC-CIT-001
- **问题**：包 D（MEM-CIT-001）与包 E（SOC-CIT-001）各自新增了基于 P300 的隐匿信息测试，源头同为 Farwell & Donchin 1991。
- **决定**：保留 **MEM-CIT-001**（memory 族），并入 SOC-CIT-001 的别名（brain fingerprinting、ERP lie detection、P300-based CIT）与线索 S13；SOC-CIT-001 删除，ID 作废。与 PER-ODD-001 的独立性另议（D-038）。
- **理由**：探测项之所以"稀少"只取决于被试是否记得相关信息，构念是对隐匿信息的再认；文献中也称"memory detection"。社会/欺骗是应用场景。
- **影响**：已执行。包 D、E。

### D-036 词语生成（IMG-WORD-001）并入言语流畅性（LAN-VF-001）
- **问题**：IMG-WORD-001（包 B，imagery 族，D-001 保留在 imagery）的别名含 verbal fluency、verb generation，标记物（MK.HbO_prefrontal）与 LAN-VF-001 相同，`first_source`（Petersen et al. 1988, R0082）就是 LAN-VG-001 的源头。
- **决定**：IMG-WORD-001 并入 **LAN-VF-001**，作为变体"fNIRS / EEG-fNIRS mental-task BCI: covert word generation"；LAN-VF-001 的 `bci_category` 改为 `[active, none]`，`recording_modality` 加 EEG，数据集（Shin et al. EEG+NIRS 开放数据）随之迁移；"verb generation"别名只保留在 LAN-VG-001。IMG-WORD-001 删除，ID 作废。本条修订 D-001 的"影响"列表（心算、心理旋转仍留在 imagery）。
- **理由**：标记物与构念（词汇提取）都相同，区别只是用途（BCI 心理任务），按 D-003 的先例用 `bci_category` 表达，不构成独立范式。
- **影响**：已执行。包 B、D。

## 十一、边界待议（文件保留）

### D-037 运动类相邻范式
- **问题**：B 提出 MOT-LIBET-001 与 MOT-MRCP-001 / MOT-IB-001、MOT-PURS-001 与 MOT-SACC-001、MOT-SMS-001 与 SSR-BEAT-001 / SOC-JA-001 的边界。
- **决定（倾向）**：全部保留独立。MOT-LIBET-001 探测"意图觉知时间"（W 判断）这一构念，MOT-MRCP-001 只看准备电位本身，MOT-IB-001 看动作–结果时间压缩，三者共用 MK.MRCP 但构念不同；MOT-PURS-001 与眼跳是不同的眼动系统，标记物也不同（PURS 只用 MK.BOLD_oculomotor，无 MK.presaccadic_potential）；MOT-SMS-001 为单人感觉运动同步，SSR-BEAT-001 为节拍感知、SOC-JA-001 为人际协调。
- **理由**：按 §1，标记物或构念任一改变即为独立范式。
- **影响**：仅记录，待例会确认。

### D-038 Oddball 结构的相邻范式：SOC-NAME-001、MEM-CIT-001 与 PER-ODD-001
- **问题**：SOC-NAME-001（自己名字 P3）、MEM-CIT-001（隐匿信息 P3）都只用 MK.P3b，结构上是 oddball。
- **决定（倾向）**：暂保留独立。二者中引起 P3b 的不是任务指定的靶，而是刺激对被试的个人意义（自我相关 / 知情再认），构念与 PER-ODD-001 的靶检测不同；在意识障碍评估和测谎中各有独立文献脉络。若例会认为"P3b 不变即变体"，则二者转为 PER-ODD-001 的变体（由包 A 编写）。
- **理由**：§1 的判定看构念；但构念差异是否足够，需要例会统一口径（同类问题还有 STM-TAVNS-001 用 MK.P3b 作结果指标）。
- **影响**：仅记录。包 A、D、E。

### D-039 音位类：LAN-PCAT-001 与 PER-MMN-001
- **问题**：D 提出新候选 LAN-PCAT-001（音位范畴化）与 D-017 中并入 PER-MMN-001 的音位 MMN 变体的边界。
- **决定**：LAN-PCAT-001 **独立**。它以颅内高 γ（MK.high_gamma）在颞上回的范畴化编码为标记物，任务是主动范畴判断；音位 MMN 是被动 oddball 下的 MK.MMN。标记物不同，按 §1 独立。两条目 `notes` 互相引用（第二遍）。
- **理由**：标记物不同。
- **影响**：决定（草案）；不改文件。

### D-040 社会注视：SOC-EYE-001 与 SOC-GAZE-001
- **问题**：E 提出 SOC-EYE-001（真人对视，超扫描 fNIRS 脑间同步）可改为 SOC-GAZE-001 的 `Hyperscanning:` 变体。
- **决定（倾向）**：暂保留独立。SOC-GAZE-001 是注视线索/注视跟随（标记物 N170、P1、pSTS BOLD），SOC-EYE-001 的任务是相互对视，单脑 fMRI 也有对视研究，任务本身不同于注视线索；D-021 只把"超扫描配置"作为变体，不意味着任务相同。若第二遍发现 SOC-EYE 的文献全部是超扫描且任务与联合注意相同，再转为 SOC-GAZE-001 或 SOC-JA-001 的 `Hyperscanning:` 变体。
- **理由**：先按任务判定，配置（超扫描）不作判定依据（D-021）。
- **影响**：仅记录。包 E。

### D-041 包 A 的疑似变体：SSR-FPAS-001、PER-ACC-001、SSR-SWEEP-001、PER-VMMN-001
- **问题**：A 自己提出 SSR-FPAS-001（听觉快速周期刺激）可能是 SSR-FPVS-001 的听觉变体，PER-ACC-001（声学变化复合波）可能是 PER-AEP-001 的变体；SSR-SWEEP-001 是维护者在 D-030 后的候议项。
- **决定（倾向）**：
  - SSR-FPAS-001、PER-VMMN-001 **独立**，各自保留 MK.FPAS_oddball、MK.vMMN。本图谱已按"感觉通道不同 → 标记物不同 → 范式不同"处理 SSVEP / ASSR / SSSEP，保持一致；§1"仅改变刺激模态按变体"的表述与此先例冲突，建议例会把 §1 修订为"刺激模态改变但标记物（含其发生源）不变时，为变体"。
  - PER-ACC-001 **倾向并入** PER-AEP-001（标记物 N1/P2 完全相同，区别是诱发事件为声音内部的变化而非起始），待例会；未改文件。
  - SSR-SWEEP-001 **倾向独立**（标记物同为 MK.SSVEP，但构念为视敏度/对比度阈值，用途是临床视力评估），待例会。
- **理由**：保持已有先例一致；对标记物完全相同的 PER-ACC 采用 §1 原文。
- **影响**：仅记录。包 A。

### D-042 包 C、D 内部及跨包的其他相邻范式
- **问题**：ERR-AAF-001（音高扰动反馈）与 LAN-SIS-001（说话诱发抑制 / 改变听觉反馈）别名重叠（"altered auditory feedback""pitch perturbation"）；CTL-CONF-001 与 ERR-AWARE-001（均 MK.Pe）；ERR-OGNG-001 与 CTL-GNG-001；LAN-SL-001 与 LAN-AGL-001 / LAN-HIER-001；LAN-SWITCH-001 与 CTL-SW-001；STA-CLAS-001 与 MEM-TMR-001（见 D-034）。另 D-030 后候议的 ERR-TE/ERR-GAM、MEM-SME/MEM-FR、MOT-SRT/MOT-MSL、CTL-SART/CTL-GNG 仍未讨论。
- **决定（倾向）**：
  - ERR-AAF-001 与 LAN-SIS-001：二者都是"自身发声的听觉反馈监测"，倾向**合并**，保留 LAN-SIS-001（language 族，名称已含 altered auditory feedback），ERR-AAF-001 作为变体"Pitch-shift perturbation response"；ERR-AAF-001 的 first_source 本就是 TBD。若例会认为扰动响应探测的是"感觉预测误差"（error 族构念），则保留 ERR-AAF-001 并把 LAN-SIS-001 中的 AAF 别名移除。未改文件。
  - 其余各对保留独立（构念不同：信心判断 vs 错误觉知；正交化学习 vs 抑制；统计学习 vs 人工语法；语言切换 vs 任务切换），第二遍在各条目 `notes` 中互相引用。
- **理由**：AAF 与 SIS 标记物（N1 抑制/增强）和刺激操纵高度重叠，其余各对构念不同。
- **影响**：仅记录。包 C、D。

### D-043 MEM-DS-001 数字广度的 D-023 复核
- **问题**：D-023 规定 MEM-DS-001 "第一遍结束时若仍不满足口径转为暂缓"。D 找到 2 条 EEG/ERP 线索（DN06 δ/θ 振荡；DN07 ERP 兼容的倒背数字广度），未核原文。
- **决定**：MEM-DS-001 保持收录，状态"阻塞"，第二冲刺第一周内由审核人核对 DN06、DN07 原文：两项均为独立、同行评议的人类神经记录研究且效应方向一致 → 解除阻塞；否则转为暂缓。ERR-CAUS-001、CTL-WASON-001（C 报告线索中没有神经记录研究支持 MK.BOLD_dlPFC）按同一口径在第二遍复核。
- **理由**：延长一个冲刺的复核期，是因为 S-002 检索受限，不足以否定。
- **影响**：MEM-DS-001、ERR-CAUS-001、CTL-WASON-001。

## 十二、策展人提议的变体

### D-044 MEM-DE-001 并入 MEM-CD-001，LAN-SIGN-001 并入 LAN-SC-001
- **问题**：D 提出的新候选 MEM-DE-001（延迟估计）和 LAN-SIGN-001（手语句子理解）建议并入，并已在目标范式中写成变体。
- **决定**：同意。两者只改变报告方式或输入模态，标记物与构念不变。candidates.csv 中登记为"并入 MEM-CD-001""并入 LAN-SC-001"，ID 作废不复用。
- **理由**：§1。
- **影响**：已执行（candidates.csv）。

## 十三、分类体系

### D-045 新增草案刺激模态 `pharmacological`；药物诱导状态的收录
- **问题**：STA-ANES-001（麻醉）与 STA-PSY-001（致幻剂状态）没有对应的刺激模态，分别暂用 cognitive_task、resting_state；E 问药物诱导状态是否算"范式"。
- **决定**：
  1. 在 `taxonomy/stimulus_modality.yaml` 末尾增加草案词条 `pharmacological`（药物给予），标注"待例会确认"。STA-ANES-001 改为 `[pharmacological]`，STA-PSY-001 改为 `[pharmacological, resting_state]`。
  2. 药物诱导状态在有标准的"给药 + 记录"程序（剂量、时间进程、对照/安慰剂）时作为 state 族范式收录，与 STA-ANES-001 一致；只把药物作为被试分组变量的研究不单独成条。
- **理由**：不加词条会让这两个条目的模态字段失真；作为草案词条加入，若例会否决，回退只涉及 2 个文件。
- **影响**：已执行。taxonomy、STA-ANES-001、STA-PSY-001。

### D-046 新增草案刺激模态 `optical_stimulation`；建 STM-PBM-001
- **问题**：B 的新候选 STM-PBM-001（经颅光生物调节同步脑电）因词表无光刺激词条而未建文件。注意"photic stimulation"在临床脑电中指闪光（视觉）刺激，已由 visual 与 SSR-SSVEP-001 的光驱动变体覆盖。
- **决定**：增加草案词条 `optical_stimulation`（"组织光刺激，不含视觉光刺激"），避免与 photic stimulation 混淆；维护者按 B 的线索（Neurophotonics 6(2):025013，DOI 10.1117/1.NPh.6.2.025013，题名 + DOI；另一条 PMC8460746）建 **STM-PBM-001** 骨架，标记物 MK.alpha_posterior，first_source 只写可见字段、`verified: false`，状态"阻塞"（作者/年份未见，是否最早未知）。
- **理由**：B 的线索有 DOI，足以建骨架；词条名避免歧义。
- **影响**：已执行。taxonomy、`paradigms/stimulation/STM-PBM-001.yaml`。

### D-047 DBS 局部场电位（再议 D-027）
- **问题**：STM-ADBS-001 与新标记物 MK.subthalamic_beta 同样需要 DBS-LFP 记录模态。
- **决定**：M1 仍按 D-027 记为 `other`，在 `notes` 写"DBS lead LFP"；下一版词表讨论中提议新增 `DBS-LFP`，涉及 STM-DBSEP-001、STM-ADBS-001、MK.ERNA、MK.subthalamic_beta。
- **理由**：一个记录模态的增加应和下一版词表讨论一起进行，`other` 不丢信息。
- **影响**：仅记录。

### D-048 内感受刺激模态与睡眠
- **问题**：A 的 PER-RREP-001（呼吸相关诱发电位）暂记 somatosensory，PER-HBD-001 记 cognitive_task；E 的睡眠分期暂用 resting_state。
- **决定**：M1 不加词条；下一版词表讨论中一并提议 `interoceptive`（内感受）与 `sleep`（睡眠，作为"无外部刺激的状态"）。当前取值保持并在 `notes` 中说明。
- **理由**：涉及的条目少，等下一版词表讨论时一起处理，避免词表频繁变动。
- **影响**：仅记录。

### D-049 价值决策类范式与族归属
- **问题**：C 新增的价值决策类任务（CTL-DD、CTL-MIXG、CTL-FORAGE、CTL-VBC、CTL-AMBIG，以及原有 CTL-IGT、CTL-BART、CTL-EFF）都放在 control 族；C 问是否设 decision 族。另有族归属疑问：ERR-AAF-001（error 或 language，见 D-042）、STM-VIB-001（stimulation 或 motor）、EMO-TOUCH-001（emotion 或 perception）、SOC-CIT（已并入 MEM-CIT，见 D-035）。
- **决定（倾向）**：M1 **不新增族**，价值决策类留在 control；下一版词表讨论中讨论"决策与价值"族（前缀 DEC），届时一并评估 ERR 族中以奖赏学习为主的条目（ERR-BANDIT、ERR-TS、ERR-PRT、ERR-APC、ERR-INST）。STM-VIB-001 留 stimulation（外加机械刺激诱发运动错觉），EMO-TOUCH-001 留 emotion（构念为触觉的情感成分）。
- **理由**：新增族会改动 ID 前缀，代价大，应在下一次 schema 与词表修订中一次完成；目前 control 族 33 条中价值决策约 8 条，尚可接受。
- **影响**：仅记录。

## 十四、标记物

### D-050 新申请标记物登记与 PET 的归属
- **问题**：sprint 1 中各包按 D-028 第 7 条新建了 18 个标记物文件（A 10：MK.vMMN、MK.MLR、MK.ORN、MK.GEP、MK.SPN、MK.Pd、MK.RREP、MK.intermodulation、MK.SSEP_nociceptive、MK.FPAS_oddball；B 5：MK.corticokinematic_coherence、MK.perturbation_N1、MK.BOLD_olfactory_cortex、MK.BOLD_vestibular_cortex、MK.subthalamic_beta；D 2：MK.CPS、MK.BOLD_left_IFG；E 1：MK.BOLD_posterior_insula）。C 与 E 指出 PET 研究（CTL-RNG-001、SOC-ANIM-001）使用的 BOLD 标记物只登记了 fMRI。
- **决定**：
  1. 18 个新标记物全部登记，owner 为申请包；合并时无同名冲突（没有两个包建同一标记物）。
  2. 血流动力学标记物的 `recording_modality` 可以包含 PET（局部脑血流 rCBF），与 D-028 第 5 条对 fNIRS 的处理一致；为实际有 PET 范式使用的 6 个标记物加 PET：MK.BOLD_dlPFC、MK.BOLD_TPJ、MK.BOLD_mPFC、MK.BOLD_auditory_cortex、MK.BOLD_visual_cortex、MK.BOLD_category_selective。下一版词表讨论中可考虑把 `BOLD_` 前缀改为中性的 `hemo_`（不在本次）。
  3. `markers.csv` 的 `used_by` 由维护者从范式文件重新生成，不再手工维护。
- **理由**：登记表须与文件一致；PET 归入同区标记物避免为每种血流测量方法单设标记物。
- **影响**：已执行。登记表 129 个标记物；CTL-RNG-001 的阻塞原因解除（保留"线索为 PET/TMS"说明）。

### D-051 标记物的同义与范围问题
- **问题**：(a) D：MK.BOLD_left_IFG 是否并入 MK.BOLD_language_network；(b) C：ERR-VRPE-001 的预测误差负波（PEN）暂映射到 MK.ErrP，是否单设 MK.PEN；(c) C：CTL-AUT-001、CTL-RAT-001 的创造力相关 α 升高在额区，却使用 MK.alpha_posterior；(d) D：MEM-RPRIM-001 是否专设 MK.repetition_suppression；(e) E：STA-NF-001 的 rtfMRI/fNIRS 变体反馈的脑区信号没有标记物；(f) A：SSR-RVS-001 使用 B 的 MK.oscillatory_entrainment，其描述只写了 tACS。
- **决定**：
  - (a) **不并入**。MK.BOLD_left_IFG 在 MEM-RPT-001 中指示的是前摄干扰的解决（认知控制），MK.BOLD_language_network 指示语言加工，构念不同；在两者的 `notes` 中互相说明（第二遍）。
  - (b) 本轮**不单设** MK.PEN，保留 MK.ErrP，在 MK.ErrP 别名中加入"prediction error negativity (PEN)"由 owner C 第二遍处理；若第二遍发现 PEN 的潜伏期/分布与交互 ErrP 系统性不同，再申请。
  - (c) 倾向第二遍新登记 **MK.alpha_task_synchronization**（任务相关额/顶 α 同步，内部注意），CTL-AUT-001、CTL-RAT-001 改用；本轮不改。
  - (d) 倾向第二遍登记 MK.repetition_suppression（fMRI 适应 + 重复相关 ERP 减小），本轮不改。
  - (e) 按 D-020，第二遍为 rtfMRI 神经反馈申请"被调节脑区 BOLD"的通用标记物或复用 MK.BOLD_stimulated_region 的命名方式，本轮不改。
  - (f) 请 owner B 第二遍把 MK.oscillatory_entrainment 的描述扩展到"节律性感觉刺激（视觉/听觉）引起的夹带"。
- **理由**：(a) 构念不同不应归并（D-028 第 4 条）；其余为第二遍工作，避免第一遍临时新增导致登记表膨胀。
- **影响**：仅记录。

### D-052 跨包标记物使用的通知
- **问题**：E、C、D 的 worklog 列出若干跨包引用（MK.BOLD_mPFC、MK.BOLD_dACC、MK.high_gamma、MK.N2_frontocentral、MK.BOLD_striatum_reward、MK.P3b 等）。
- **决定**：引用不需要 owner 同意；owner 通过重新生成的 `markers.csv` `used_by` 列了解新使用者，并在第二遍编写 `indexes` 时考虑这些用途。修改他包 owner 的标记物仍需向 owner 提出（D-028 第 7 条）。
- **理由**：减少跨包沟通量。
- **影响**：已执行（used_by 重新生成）。

## 十五、候选与流程

### D-053 sprint 1 新候选的登记
- **问题**：5 个包共提出 85 个新候选（A 18、B 17、C 17、D 17、E 16），其中 82 个已由策展人建骨架文件（D 的 2 个建议并入、B 的 STM-PBM-001 未建）。
- **决定**：
  1. 全部登记进 `candidates.csv`，新编号 C210 – C294，`decision_ref` 为 D-053（另有专条的指向专条）。
  2. 判定：收录 81（含维护者代建的 STM-PBM-001，D-046；合并后 81 个文件）；并入 4（STM-CLAS-001 → STA-CLAS-001，D-034；SOC-CIT-001 → MEM-CIT-001，D-035；MEM-DE-001 → MEM-CD-001、LAN-SIGN-001 → LAN-SC-001，D-044）。另有原候选 IMG-WORD-001（C 编号不变）改为"并入 LAN-VF-001"（D-036）。
  3. 新候选的"收录"同 D-026 一样是初步判定，第二遍发现不满足纳入标准时按 D-023 口径提请暂缓。
- **理由**：每个新候选都有至少一条本次检索实际看到的线索，且已查重。
- **影响**：已执行。

### D-054 种子条目改为块状 YAML
- **问题**：A、B 用 `yaml.safe_dump` 重写了种子条目 PER-ODD-001、SSR-SSVEP-001、MOT-MI-001，格式由流式改为块状。
- **决定**：接受。维护者逐字段比较了 main 与合并后的版本：原有键值全部保留，`notes` 原文为新 `notes` 的前缀，`description.zh` 只去掉了折行产生的空格。今后维护者修改的文件也统一用块状 YAML（`sort_keys=False, allow_unicode=True, width=120`）。
- **理由**：内容无损；统一格式便于以后脚本化修改。
- **影响**：已执行（无需改动）。

### D-055 文献线索的 QA 标记与错配线索改配
- **问题**：策展人报告了一批有问题的线索：错配（D：MEM-RC-001 的 R0031、R0151、R0267、R0402；LAN-HIER-001 的 R0216、R0321、R0381、R0419；LAN-READ-001 的线索无神经记录）；书目矛盾（R0154 卷期与 DOI 不符；E：R0683、R0533、R0788 DOI 与题名/期刊不符，R0831 DOI 为占位符；B：R0820 文章号与 DOI 不符）；可疑 PMID（B：R0874、R0972，以及 R0956、R1045、R1051）；题名问题（R0562 为占位题名，R1064 题名凭记忆补写）；内容不符（R0176 与镜像描摹无关，R0024 挂在 IMG-VIS-001 下，R0062 为猴研究，R0229 的 url 指向 TMR 页面）；弱源头（R0001、R0059、R0046）。
- **决定**：
  1. `literature.csv` 新增 `qa_flag` 列，只为有问题的行填写，取值（可用 `;` 并列）：`misassigned`（错配，已改配）、`doi_mismatch`、`doi_placeholder`、`volume_mismatch`、`pmid_suspect`、`title_placeholder`、`title_from_memory`、`url_mismatch`、`off_topic`、`animal_study`、`weak_origin`、`behaviour_only`、`verify_species`、`secondhand`（转引）。
  2. 错配线索在 `paradigm_literature.csv` 中**改配**：R0031、R0151、R0267、R0402 → MEM-CD-001（变化检测/视觉工作记忆容量文献；R0151 原已挂 MEM-CD-001，删除重复行）；R0216 → PER-MMN-001（Näätänen 2001 语音 MMN 综述，与 D-017 音位 MMN 变体相关）；R0321、R0381、R0419 → LAN-PCAT-001（言语知觉文献）。LAN-READ-001 的 R0033、R0048、R0311 保留但标 `behaviour_only`（R0255 含 ERP，不标）。
  3. 有问题的书目字段**不在本次修改**（未核原文，避免以错改错），由审核人核对原文后更正并去掉标记。
- **理由**：错配线索会污染每个范式的文献计数和 Zotero 标签；用标记而不是删除，保留了审计轨迹。
- **影响**：已执行——见 `curation/literature.csv` 的 `qa_flag` 列和 `paradigm_literature.csv`。

### D-056 CTL-STR-001 别名与 D-019 冲突
- **问题**：`candidates.csv` 中 CTL-STR-001 的 aliases 含 "Emotional Stroop (variant)"，与 D-019（不给 Stroop 加情绪 Stroop 变体）冲突；C 已从条目文件中删除。
- **决定**：从 `candidates.csv` 中删除该别名。
- **理由**：与 D-019 保持一致。
- **影响**：已执行。

---

# 第二冲刺（sprint 2）前的结构决议 D-057

> 起草：维护者（maintainer），2026-10-03。依据：负责人（yifan）对"范式粒度"的指示。
> 状态：**已确认（负责人，2026-10-03）**。本条与 D-001 – D-056 的草案状态无关，直接生效；由它引起的对旧决议的复核在 sprint 2 进行（见"影响"第 4 款）。
> **勘误（维护者，2026-10-03，D-067）**：原"给号示例"中 MOT-MI-003 写作"单侧上肢 11 类动作想象（如肘屈伸、前臂旋前/旋后、手抓握/张开）"，把两个数据集混在了一起：所列动作出自 Ofner et al. 2017（6 种动作 + 休息 = 7 类），11 类出自 Jeong et al. 2020。示例已按 sprint 2 的实际文件改为 MOT-MI-003 = 7 类（Ofner 2017）、MOT-MI-011 = 11 类（Jeong 2020）。给号规则（第 1 – 7 款）未改，确认状态不变；勘误本身请负责人知悉（D-067）。

## 十六、标识符与粒度

### D-057 两级范式标识符：范式类与具体范式（已确认（负责人，2026-10-03）；给号示例已勘误（维护者，2026-10-03，见 D-067），规则未改）
- **问题**：schema 0.1 中一个 `<范式族>-<简称>-<序号>` 文件既承担"机制"（标记物、构念、源头），又承担"可复现的任务配置"（类别集、提示、时序、反馈、数据集）。按 D-030 与文件开头的判定基准，只要标记物与构念不变，改变类别集、刺激编码、时序结构或反馈方式的做法都被写成 `variants`。结果：(1) MOT-MI-001 一个文件同时代表左/右手二分类、四分类（左手/右手/双脚/舌头）与下肢想象，`trial_structure.conditions` 只能写并集，无法对应到具体数据集；(2) `variants` 中混有参数微调（如高频 SSVEP）与完全不同的协议（P300 speller、RSVP），无法复现、无法统计；(3) 序号 `-001` 实际上从未被使用过第二个值。
- **决定**：
  1. **范式类（paradigm class）** = `<范式族>-<简称>`，例如 `MOT-MI`。范式类描述共同机制：标记物、构念、该类的源头文献（`first_source`）、描述。范式类登记在 `paradigms/_classes.yaml`（schema `schema/paradigm_class.schema.json`），不单独建文件。
  2. **具体范式（concrete paradigm / protocol）** = `<范式族>-<简称>-<序号>`，例如 `MOT-MI-001`。一个具体范式是**一个可复现的任务配置**，有自己的类别集、提示、时序、反馈与数据集，即 `paradigms/<族>/<ID>.yaml` 文件；文件中的 `class` 字段必须等于去掉 `-<序号>` 的 ID，`protocol` 块写明配置要素。
  3. **给号规则**：同一范式类下，以下 4 项中**任一**改变即分配新序号：
     1. **类别/条件集**：解码或对比的类别、目标、条件的数量或身份改变；
     2. **刺激或提示类型**：含刺激编码方案（如 SSVEP 的单纯频率编码 vs 联合频率–相位编码；P300 的行/列闪烁 vs 棋盘格闪烁）；
     3. **试次结构**：如同步（提示驱动）vs 异步（自定步调）；单试次 vs 组块；
     4. **反馈方式**：无 / 离散 / 连续；开环 vs 闭环。
  4. **只改参数的不给新号**：时长、ISI、试次数、同一编码方案内的具体频率值、电极数、被试人群等，仍写在参数范围（`trial_structure`）或 `variants` 中。`variants` 从此**只用于参数级变化**。
  5. **永久性**：序号永久有效、不复用；被撤销的具体范式标 `deprecated`。`-001` 应为该范式类**最早发表或公认的标准配置**；后续配置按认定顺序取 `-002`、`-003` ……，序号不表示优劣或时间先后之外的任何含义。
  6. **范式类之间的边界不变**：标记物或构念改变 → 独立的范式类（方法说明 §1，D-001 – D-056 中的"独立"判定继续有效）；本条只在范式类**内部**细分。
  7. 被并入候选的作废 ID（如 MOT-GAIT-001、PER-RSVP-001）**不复活**；若复核后它们对应的做法成为独立的具体范式，在目标范式类下取新序号。
- **给号示例（运动想象，MOT-MI）**：

| ID | 具体范式 | 区别于兄弟协议的依据 |
|---|---|---|
| `MOT-MI` | 范式类：提示性运动想象（标记物 MK.SMR_ERD；源头 Pfurtscheller & Neuper 1997） | — |
| `MOT-MI-001` | 左手 / 右手二分类，视觉提示，同步试次 | 标准配置（最早发表） |
| `MOT-MI-002` | 左手 / 右手 / 双脚 / 舌头四分类（如 BCI Competition IV 2a） | 准则 1：类别集由 2 类变为 4 类 |
| `MOT-MI-003` | 单侧上肢多关节动作想象：肘屈/伸、前臂旋后/旋前、手张开/握拳 6 种动作 + 休息，共 7 类（Ofner et al. 2017） | 准则 1：类别身份与数量改变 |
| `MOT-MI-011` | 单侧上肢 11 类动作想象（Jeong et al. 2020，GigaScience；类别名待从原文补全） | 准则 1：类别集（11 类）不同于 -001 与 -003 |

  （勘误注：本表 2026-10-03 初稿把 -003 写成"11 类上肢"，与实际文件不符，已按 D-067 更正；-004 – -010 的其他 MI 具体范式见 `curation/registry/concrete_paradigms.csv`。）

  只改变想象时长（如 3 s → 4 s）或试次数的研究不给新号，写入 MOT-MI-001 的 `trial_structure` 参数范围；"左/右手二分类 + 连续光标反馈"则因准则 4 取新号。
- **理由**：BCI 的可复现性、数据集对接和性能比较都以具体协议为单位（类别数决定信息传输率，编码方案决定解码方法），而机制知识（标记物、构念、源头）以范式类为单位。两级 ID 让两者各有其位：图谱节点数不因协议增多而重复机制信息，协议也不再淹没在自由文本的 `variants` 里。保留现有 `-001` 文件与 ID，迁移成本最低（schema 0.2 只新增字段）。
- **影响**：
  1. **schema 0.2**：`paradigm.schema.json` 新增必填 `class`、可选 `protocol`（`n_classes`、`classes`、`cue`、`stimulus_coding`、`paradigm_timing`、`feedback`、`distinguishing`；有 `protocol` 时 `distinguishing` 必填）；新增 `paradigm_class.schema.json` 与 `paradigms/_classes.yaml`；标记物与词表文件的 `schema_version` 同步迁移到 `"0.2"`（内容不变）。校验、图谱导出与覆盖度报告随之更新。
  2. **迁移**：267 个现有文件全部加 `class`、`schema_version: "0.2"`，其余内容不变；为每个现有 ID 生成一个范式类（名称、描述、标记物、源头、别名、状态取自该 `-001` 文件，`contributors: [maintainer]`）。现有文件暂无 `protocol`，校验以警告形式列出，不报错。
  3. **方法说明 §1、§6** 重写（变体 = 参数级变化；标识符表增加范式类与 4 条给号准则）；`_template.yaml`、`CONTRIBUTING.md`、PR 模板、Issue 表单同步更新。
  4. **修订以下旧决议**——它们按"标记物与构念不变即变体"把不同的**任务配置**并成了 `variants`，sprint 2 中由各包逐条复核：留作参数级变体，或拆为新的具体范式（记入本包 `sprint2/split_log.csv`，写明准则编号）：
     - 文件开头的**判定基准**与 **D-030**（并入候选的数据模型）：此后只用于判断是否为独立的范式类；
     - **D-002** 光驱动（临床阶梯频率闪光，无目标选择：准则 1、3）、**D-003** 多目标频率标记注意（准则 1、2）、**D-004** 高频/不可见 SSVEP（预计仍为参数级变体，需确认是否改变编码方案）—— SSR-SSVEP；
     - **D-005** 单指运动解码（准则 1）—— MOT-ME；**D-014** 下肢/足部运动想象（准则 1）—— MOT-MI；步态行走（准则 1、3）—— MOT-ME；
     - **D-006** 音乐想象、**D-007** 类别特异视觉想象、**D-008** 空间导航想象（准则 1、2）—— IMG-AUD、IMG-VIS、IMG-CMD；
     - **D-011** RSVP 目标检测（准则 2、3）—— PER-ODD；**D-012** 触觉 P300 BCI 与稳态振动触觉注意变体（准则 2）—— PER-ODD、SSR-SSSEP；
     - **D-015** 错误觉知中写成变体的 Flanker / 反向眼跳觉知报告（准则 2）—— ERR-AWARE；
     - **D-017** 音位对比 MMN（准则 2）—— PER-MMN；**D-018** 音乐/音乐视频情绪诱发（准则 2）—— EMO-FILM；
     - **D-020** STA-NF 的 rtfMRI / fNIRS 神经反馈变体（准则 4 与反馈信号）；**D-021** 超扫描与 **D-022** 混合 BCI（记录配置或组合方式本身不是给号准则，但其中任务配置若满足准则 1–4 则给号）；
     - **D-024** 记得/知道判断（准则 1：报告类别）—— MEM-ON；**D-025** 社会激励延迟（准则 2：奖赏提示类型）—— EMO-MID；
     - **D-036** 词语生成心理任务 BCI（准则 3、4）—— LAN-VF；**D-044** 延迟估计（准则 1、3）—— MEM-CD，手语句子理解（准则 2）—— LAN-SC；
     - 待议倾向 **D-041**（PER-ACC-001 → PER-AEP-001）与 **D-042**（ERR-AAF-001 → LAN-SIS-001）：例会判定若为"并入"，则按本条在目标范式类下给号而不是写成变体；
     - 未对应决议、由种子或策展人写入的配置级变体同样复核：PER-ODD-001 "P300 speller (row/column matrix)"、SSR-SSVEP-001 "SSVEP-based BCI"、PER-MVEP-001 "Motion-onset VEP BCI"、IMG-CMD-001 "Bedside EEG motor-imagery command following"、MOT-ME-001 "Paced finger tapping"、SOC-TOM-001 定位任务、MEM-FR-001 RAVLT、MEM-META-001 JOL、MEM-NAV-001 虚拟放射臂迷宫、LAN-P600-001 花园路径句、LAN-PN-001 图词干扰、EMO-FC-001 恐惧泛化、SOC-TRUST-001 超扫描信任博弈（共 35 个变体，全部列入 sprint 2 复核）。
  5. D-001 – D-056 中"独立收录"的判定（D-012、D-013、D-015、D-016、D-019、D-020、D-037 – D-043 等）在范式类层面继续有效，不受本条影响。
  6. **写入流程**：策展人不直接修改 `paradigms/_classes.yaml`（共享文件，避免 5 个包合并冲突），范式类的修改写入 `curation/work/pkg_<X>/sprint2/class_updates.yaml`，由维护者统一合入（D-029 的补充）。

---

# 第二冲刺（sprint 2）合并后的决议草案 D-058 – D-071

> 起草：维护者（maintainer），2026-10-03。依据：5 个包的 `curation/work/pkg_<X>/sprint2/worklog.md`、`split_log.csv`、`class_updates.yaml`，维护者 QA（`curation/reports/qa_sprint2.md`）。
> 状态：除 D-071（流程记录，已执行）外均为**草案，待负责人确认**。标"已执行"的部分是不依赖口径的平凡修正；标"确认后执行"的部分在确认前不改文件。
> **2026-10-05 更新**：负责人授权专家裁定里程碑 M2 收尾前必须决定的四条——D-058、D-061、D-062、D-063——均已确认（见各条状态行与"裁定说明"），文件已按裁定修改并纳入里程碑 M2。其余各条（D-059、D-060、D-064 – D-070）仍为草案，待例会。

## 十七、给号准则的口径

### D-058 准则 1 的粒度：同质目标的个数是参数（已确认（专家裁定，负责人授权，2026-10-05））
> 状态：已确认（专家裁定，负责人授权，2026-10-05）
- **问题**：D-057 准则 1 写"类别、目标、条件的**数量或身份**改变即给新号"。字面执行会把同一编码方案下只改目标个数的做法（SSVEP 键盘 12 vs 40 个字符、P300 矩阵 6×6 vs 8×9、触觉 P300 的 2/4/6 个振动器）都拆成新具体范式，而 D-057 第 4 款又把"同一编码方案内的取值"列为参数，两条互相冲突。包 A 报告：SSR-SSVEP-005（JFPM 40 目标）与 -006（JFPM 12 目标）只因目标集不同而分号；SSR-SSVEP-007 只比频率编码多一个静息类。包 A 的 PER-ODD-006、SSR-SSVEP-005 的 distinguishing 也把目标数写成准则 1。
- **决定**（提议的具体阈值）：
  1. **同质目标集**——各目标可互换、由同一刺激/编码方案区分、解码方法相同的选择任务（SSVEP/c-VEP 键盘、P300 矩阵或单项闪烁、听觉/触觉 P300 的方向或位置、目标数可调的视觉搜索等）——**目标个数是参数**，写在 `trial_structure` / `variants`，不给新号。`protocol.n_classes` 写标准配置的目标数（无标准配置时可不写）。
  2. **异质类别集**——每一类是不同的心理任务、身体部位、刺激类别或条件（MI 的左手/右手/双脚/舌头、上肢各关节动作、情绪类别、CS+/CS−/泛化刺激等）——类别**身份或数量**的任何改变都是准则 1（MOT-MI-002/-003/-006/-008/-010/-011 维持不变）。
  3. 不论同质与否，**加入或去掉一个"非控制/静息/空闲"类**（或类似的拒识类）改变解码问题（需要检测非控制状态），按准则 1 给号。
  4. 目标个数的改变若同时伴随**编码方案或刺激布局本身的改变**（如行/列 → 棋盘格分组），按准则 2 给号，不以目标数为依据。
  5. 目标数为参数的情况下，"有独立的公开数据集"不单独构成给号理由；数据集挂在对应的具体范式的 `datasets` 下。
- **按本条处理**：
  - **SSR-SSVEP-006**（JFPM 12 目标，Nakanishi 2015 数据集）：与 -005 只差同质目标数，且 `feedback: none` 只是数据集页面未写反馈，不是协议差异 → **降为 SSR-SSVEP-005 的参数级变体**（"12-target JFPM layout (Nakanishi et al. 2015)"），数据集移到 -005；-006 文件标 `status: deprecated`、notes 写"merged into SSR-SSVEP-005 per D-058"，序号不复用。（确认后执行。）
  - **SSR-SSVEP-007**（频率编码 + 静息类）：按第 3 款**保留**。
  - PER-ODD-006、SSR-SSVEP-005、PER-ODD-008、PER-ODD-009 的 distinguishing 中"准则 1：目标数/类别为方向或位置"一句删去或改写为参数说明（确认后由包 A 修改）；PER-ODD-003/-005/-006/-008/-009、SSR-CVEP-001/-002、SSR-SSVEP-002/-005/-008 未写 `n_classes` 的情况可接受。
  - STA-SCP-002（SCP 拼写装置）：两类 SCP 与 -001 相同，但输出变为逐字符选择且有独立发表的协议（Birbaumer 1999），按第 2 款"条件身份改变"（选择/拒绝字母组）**保留**。
- **理由**：信息传输率与解码方法由编码方案和类别性质决定，同质目标个数只是界面规模；把它当准则 1 会让 SSVEP、P300 拼写器按键盘尺寸无限细分，而 MI 的类别集确实决定了不同的解码问题。阈值可用"各目标是否可互换"一句话判断。
- **影响**：方法说明 §6 准则 1 加一句"同质目标的个数为参数"（确认后修改中英文两版）；`check_siblings.py` 不受影响。
- **裁定说明**（2026-10-05）：按草案确认，无修改。要点：同质、可互换的目标集——目标个数是参数；异质类别集——身份或数量改变即准则 1；加入/去掉静息/空闲/非控制类属准则 1；布局或编码方案改变属准则 2；数据集本身从不构成给号理由。**已执行**（维护者，2026-10-05）：SSR-SSVEP-006 标 `status: deprecated`（notes 写 "merged into SSR-SSVEP-005 per D-058"，文件保留）；12 目标布局作为 SSR-SSVEP-005 的参数级变体，Nakanishi2015 数据集随之移入，R1267 的关联改到 -005（角色 dataset）；PER-ODD-006/-008/-009 与 SSR-SSVEP-005 的 distinguishing 改写，不再以目标数为准则 1；方法说明中英文 §6 准则 1 加入一句规则；`check_siblings.py`、`build_graph.py`、`coverage_report.py` 跳过 deprecated 条目（覆盖度报告第 1 节单列计数）。

### D-059 准则 3 的范围：试次内结构、试次间依赖与多阶段设计（草案，待负责人确认）
- **问题**：`protocol.paradigm_timing` 只有 synchronous / asynchronous / block / continuous 四个取值，但 sprint 2 中有若干具体范式以准则 3 给号，其结构改变无法用这四个值表达：EMO-FC-003（第二天消退回忆测试）、SOC-TRUST-002/-003（与同一伙伴多轮互动、结果依赖历史）、ERR-ERRP-002（试次中没有用户指令阶段）、ERR-GAM-003（没有选择阶段）、MOT-SACC-002（插入延迟期）、CTL-SW-003（无外部线索、自主选择任务）。另有两处尚未拆分：PER-FACE-001 中 fMRI 组块定位器与 ERP 事件相关设计合在一起（包 A 问题 4），MEM-MST-001 中连续再认与学习—测试两阶段合在一起（包 D 问题 2）。
- **决定**：
  1. 准则 3 涵盖：(a) 同步 / 异步 / 连续 / 组块（`paradigm_timing`）；(b) **单试次（事件相关）vs 组块设计**；(c) **试次内阶段的增删**——加入或去掉提示、指令、选择、反应、延迟期等阶段；(d) **试次间依赖**——结果依赖与同一对象的互动历史（重复博弈）或自适应难度；(e) **多阶段/多日设计**中作为独立测试阶段的环节（如消退回忆、睡眠后测试）。
  2. 只改**数量**的不算：轮数、阶段时长、会话数、组块长度是参数。
  3. 以 (b)–(e) 给号时，distinguishing 必须写明是哪一项（如"准则 3(d)：多轮依赖"），供 `check_siblings.py` 的 REVIEW 列表人工复核。schema 0.3 可考虑给 `protocol` 加可选字段 `structure`（自由文本）记录 (b)–(e)。
  4. 据此：EMO-FC-003、SOC-TRUST-002、SOC-TRUST-003、ERR-ERRP-002、ERR-GAM-003、MOT-SACC-002、CTL-SW-003 **保留**；PER-FACE-001 的组块定位器与 ERP 事件相关设计、MEM-MST-001 的两种呈现方式在 sprint 3 有各自出处时**拆分**（-001 保留最早者）。
- **理由**：D-057 的准则 3 原文就包含"单试次 vs 组块"；试次阶段与试次间依赖改变的是数据如何分段、标签如何定义，影响可复现性和解码方法，与"只改时长"有本质区别。
- **影响**：确认后在方法说明 §6 准则 3 补一句说明；各包在 sprint 3 补写 distinguishing 中的子项字母。

### D-060 刺激模态改变属于准则 2（草案，待负责人确认）
- **问题**：包 D 问：同一范式类中视觉版 → 听觉版（或书面 → 口语、语音 → 手语）是否算准则 2。D 已按准则 2 给号 LAN-CPS-002（书面逗号）、LAN-LOC-002（听觉定位器）、LAN-SC-002（手语），而 LAN-LDT、LAN-N400、LAN-AGL 的听觉版本因无线索只记为提议。另一方面，文件开头的判定基准写"仅改变刺激模态……按变体处理"。
- **决定**：
  1. **是**。D-057 准则 2 为"刺激或提示类型"，刺激的感觉模态是刺激类型最基本的一层，模态改变即准则 2，给新序号。文件开头判定基准中"仅改变刺激模态按变体处理"一句，依 D-057 修订注**只用于范式类层面**（模态改变不产生新的范式类），不适用于范式类内部。
  2. 同理，在以反馈事件为诱发刺激的范式（ERR 族 ErrP、反馈负波）中，**反馈的感觉模态**（视觉 / 振动 / 电肌肉刺激）改变按准则 2；反馈的**方式**（无/离散/连续）仍按准则 4。
  3. **记录模态**不是给号准则（D-057 第 4 款："电极数、被试人群等"同属参数；STA-NF-002 的 fNIRS 版本留作变体、SOC-JA 超扫描留作变体的做法正确）。
  4. 同一研究中作为**条件**并列出现的几种模态（如 ERR-VRPE-001 的视觉/振动/EMS 条件，R1258）属于该研究的条件集，暂留在原具体范式的 `variants` / 条件中；当有研究以某一模态作为其协议本身时再给号。
- **理由**：与 D-057 "刺激或提示类型"的字面一致；跨模态版本通常对应不同的数据集与不同的早期成分。
- **影响**：LAN-CPS-002、LAN-LOC-002、LAN-SC-002、CTL-SIM-002（听觉 → 视觉）、PER-ODD-008/-009（听觉、触觉 P300）等的给号得到确认；LAN-LDT、LAN-N400、LAN-AGL 的听觉版本在有出处时给号。确认后方法说明 §6 准则 2 补"含刺激的感觉模态"。

## 十八、标记物与源头

### D-061 具体范式的标记物：记录"有文献记载"的标记物，继承需标注（已确认（专家裁定，负责人授权，2026-10-05））
> 状态：已确认（专家裁定，负责人授权，2026-10-05）
- **问题**：schema 要求每个具体范式 `markers` 至少一项。sprint 2 中有两类情况：(1) **最早配置是行为学测验**，神经标记物只在后来的配置中测得，却沿用了类标记物：MEM-CD-001（全视野变化检测，MK.CDA 来自偏侧化版本）、MEM-FR-002（RAVLT）、MEM-NBK-004（双 n-back 训练）、LAN-VF-001（测验版）、CTL-STR-001（卡片版，N450 只见于单试次版本）、ERR-TS-002（Kool 2016 行为学）、CTL-ANT-002（ANT-I 行为学）；(2) **替代标记物**：CTL-CPT-003 用 MK.DMN_connectivity 近似 gradCPT 中的默认网络活动，STA-NF-002 用 MK.BOLD_amygdala 代表"被训练脑区的 BOLD"。另外 MEM-SWM 的类标记物 MK.CDA 没有任何 MEM-SWM 具体范式使用。
- **决定**：
  1. 具体范式的 `markers` 写**该配置有文献记载会诱发的标记物**（不要求出自 first_source，可以出自后续用同一配置的研究，notes 写明线索）。
  2. 若该配置本身没有神经记录（最早配置为行为学测验），**仍保留类标记物**以满足 schema，但 notes 必须含固定短语 `marker inherited from class`，并写明在哪个兄弟配置中测得。维护者在 sprint 3 用脚本统计此短语。
  3. **替代标记物**（登记表中最接近的项）允许暂用，notes 写固定短语 `stand-in marker`；同时由使用包提交 marker_requests（CTL-CPT-003 → 拟议 MK.BOLD_DMN 或"默认网络活动"；STA-NF-002 → 不新建泛化的"目标脑区 BOLD"，改为写 first_source 实际训练的脑区对应的标记物，如无则申请）。
  4. **范式类的 `markers` = 其具体范式 `markers` 的并集**（不变式）。类中有而无具体范式使用的标记物只能在对应配置建档前暂留：MEM-SWM 的 MK.CDA 暂留，sprint 3 由包 D 建"偏侧化空间延迟反应"配置（MEM-SWM-002）或从类中删去。本次合并时 MOT-GRASP 类已补 MK.low_freq_kinematics（已执行）。
  5. **schema 0.3 提议**：具体范式增加可选字段 `marker_basis: documented | inherited | stand_in`（默认 documented），把第 2、3 款的 notes 短语结构化；`validate.py` 增加"类标记物 ⊇ 具体范式标记物"的检查。
- **理由**：把 markers 改为可选会让图谱的 elicits 边失去覆盖（约 10 个行为学 -001 没有任何边），而无标注的继承会让人误以为该配置已被神经记录。标注 + 后续结构化兼顾两者。
- **影响**：确认后各包在 sprint 3 给上述文件补固定短语（CTL-STR-001、ERR-TS-002、CTL-ANT-002、MEM-CD-001、MEM-FR-002、MEM-NBK-004、LAN-VF-001；替代项 CTL-CPT-003、STA-NF-002）。
- **裁定说明**（2026-10-05）：按草案确认；执行时间由"sprint 3"提前到发布前。**已执行**（维护者，2026-10-05）：7 个行为学配置的 notes 加固定短语 `marker inherited from class` 并写明测得该标记物的兄弟配置（CTL-STR-001 → CTL-STR-002；ERR-TS-002 → ERR-TS-001；CTL-ANT-002 → CTL-ANT-001；MEM-CD-001 → MEM-CD-003；MEM-FR-002 → MEM-FR-001；MEM-NBK-004 → MEM-NBK-001/-003；LAN-VF-001 → LAN-VF-002/-003）；2 个替代项加 `stand-in marker`（CTL-CPT-003、STA-NF-002）。`validate.py` 新增**错误级**检查"类标记物 ⊇ 每个（非 deprecated）具体范式的标记物"（第 4 款不变式），现有文件 0 违反（MOT-GRASP 已在合并时补齐），无需扩充类标记物；MEM-SWM 的 MK.CDA 暂留，类 notes 已注明。第 5 款的 `marker_basis` 字段列入 schema 0.3 提议清单（见下文"schema 0.3 提议清单"），本版不改 schema。

### D-062 范式类的源头与 -001 的源头（已确认（专家裁定，负责人授权，2026-10-05））
> 状态：已确认（专家裁定，负责人授权，2026-10-05）
- **问题**：D-057 第 5 款要求 -001 为"最早发表或公认的标准配置"，而范式类也有 `first_source`。sprint 2 出现三种不一致：(1) **SSR-SSVEP**：临床光驱动（-003）早于 Regan 1966（-001 与类源头），但 -003 的 first_source 只是一份临床指南；(2) **MEM-TMR**：气味情境再激活（-002，DN52 = R1327，2007）早于 -001（Rudoy et al. 2009），包 D 在 class_updates 中把类源头改为 2007 研究；(3) **STA-SCP**：-001 改为二分类 SCP 训练（源头 TBD，所见最早 1992 年记录 R1333、R1334），原来的拼写装置（Birbaumer 1999）移到 -002，类源头仍是 1999 年拼写装置。
- **决定**：
  1. **范式类 `first_source` = 该类中最早的、书目可识别的配置的源头**（D-031 的口径：任务程序的最早描述），不一定是 -001 的源头。类的 notes 写明来自哪个具体范式。
  2. **-001 不因发现更早的配置而改号**（永久性）。-001 的 distinguishing 写"标准配置（公认）"而非"最早发表"，并在 notes 指向更早的兄弟。
  3. 只有当更早配置的源头是**原始研究且书目完整**时才改类源头；指南、综述、教科书、只有题名的记录不替换已有的原始研究。
  4. 据此：**MEM-TMR** 类源头改为 R1327（2007，已按 class_updates 合入；作者未见，`verified: false`）——保留；MEM-TMR-001 的 distinguishing 改为"标准配置（公认）"（确认后由包 D 修改）。**SSR-SSVEP** 类源头暂保持 Regan 1966，直到找到光驱动的原始研究（D-032 检索清单，候选为 1930 年代的光驱动报告，未检到）。**STA-SCP** 类源头暂保持 Birbaumer 1999（R1177），notes 注明"earlier configuration STA-SCP-001; origin TBD (earliest records seen 1992: R1333, R1334)"（确认后执行）。
- **理由**：类源头回答"这一机制最早怎样被研究"，-001 回答"标准做法是什么"；两者分开记录，既不违反 ID 永久性，也不让较晚的 BCI 应用冒充源头。
- **影响**：方法说明 §1 "范式类"一段补一句类源头的定义（确认后）；coverage 报告 §8.7 已分别统计类与具体范式的 TBD。
- **裁定说明**（2026-10-05）：按草案确认。定义：范式类 `first_source` = 该类中任一配置的、最早的、书目可识别的**原始研究**；`-001` = 标准配置（公认），永不改号；指南、综述、只有题名的记录不替换已有原始研究。**已执行**（维护者，2026-10-05）：MEM-TMR 类源头保持 R1327（2007），类 notes 注明来自 MEM-TMR-002；MEM-TMR-001 的 distinguishing 改为"标准配置（公认）/ canonical configuration"并指向更早的兄弟；SSR-SSVEP 类源头保持 Regan 1966，类 notes 说明 -003 的指南不替换原始研究；STA-SCP 类 notes 按草案写入；方法说明中英文 §1 加类源头定义句、§6 永久性一段相应改写。

### D-063 sprint 2 新建 ID 的含义冻结点（已确认（专家裁定，负责人授权，2026-10-05））
> 状态：已确认（专家裁定，负责人授权，2026-10-05）
- **问题**：D-057 规定序号永久、不复用，但 sprint 2 中有两处需要在发布前调整已建 ID 的**含义**：STA-SCP-001 由"拼写装置"改为"二分类 SCP 训练"（包 E，原拼写装置移到 -002）；IMG-MA-001/-002 若核实 Keirn & Aunon 1990（R0842）原始配置为五任务，两者角色需对调（包 B 问题 1）。
- **决定**：
  1. **v0.1.0 发布之前**，sprint 2 新建或改义的具体范式 ID 仍可调整含义或对调内容，条件是：在 split_log.csv 中记一行、文件 notes 写明、PR 草稿顶部注明。
  2. **v0.1.0 发布后**，ID 含义冻结；以后只能 deprecate + 新号。
  3. 据此接受 STA-SCP-001 的改义（schema 0.1 时的 STA-SCP-001 是骨架条目，从未有过 protocol）；IMG-MA 的对调由包 B 在核对 R0842 后决定，须在 v0.1.0 发布前完成，否则保持现状。
- **理由**：schema 0.1 的 ID 只表示范式类层面的条目，具体配置的含义在 sprint 2 才第一次写定；在第一个包含 protocol 的正式版本前允许修正，成本最低。
- **影响**：v0.1.0 发布前需完成 D-058（SSR-SSVEP-006）、D-063（IMG-MA）的处理。
- **裁定说明**（2026-10-05）：确认，**一处修订**：IMG-MA-001/-002 **不对调**。依 D-062，-001 是标准配置——BNCI2015_004 类 / fNIRS 心算 BCI 所用的"心算 vs 静息"二分类——与 Keirn & Aunon 1990（R0842）实际包含的任务集无关；R0842 只记为范式类源头候选。IMG-MA-002 的内容（类别表、与 R0842 的关系）在 sprint 3 核实，ID 含义不变。STA-SCP-001 的改义按草案接受。ID 含义自 v0.1.0 发布起冻结。**已执行**（维护者，2026-10-05）：IMG-MA-001 distinguishing 改为"Canonical configuration / 标准配置（公认）"并写明 R0842 仅为类源头候选；IMG-MA-002 distinguishing 与 notes 注明"内容待 sprint 3 核实"；IMG-MA、STA-SCP 类 notes 与 STA-SCP-001 notes 记录裁定；方法说明 §6 永久性一段加入冻结点。

### D-064 ERR-OBS 与 ERR-ERRP 的边界（草案，待负责人确认）
- **问题**：观察机器/光标的错误（R0714 引用的 Ullsperger et al. 2007、Gentsch et al. 2009）现归 ERR-ERRP-002（监视型 ErrP，BNCI 013-2015）；ERR-OBS-003 是 VR 中化身的动作错误。包 C 问边界在哪里。
- **决定**：
  1. **ERR-OBS**：被观察者是**另一个行动者**（他人或第三人称化身）在**其自己的任务**上出错，观察者自身的任务不受影响；读出为观察性 ERN/oERN、观察性 Pe。
  2. **ERR-ERRP**：出错的是**被试所依赖或监督的装置/界面**（光标、机械臂、拼写器、自主运行的设备），不论错误由被试指令触发（-001、-003、-004）还是被试只是监视（-002）；读出为交互 ErrP。观察机器错误的研究归 ERR-ERRP-002。
  3. **第一人称化身**（被试在 VR 中体验为"自己的身体"）的错误更接近自我监控，归 ERR-OBS-003 暂不变，但 ERR-OBS-003 的 classes 若只含第一人称条件，sprint 3 需复核是否应为 ERR-ERRP 的新配置；第三人称化身留在 ERR-OBS。
- **理由**：以"出错的主体是谁、对被试的后果是什么"划界，与 BCI 用途（监督装置）一致，也与两类标记物文献的分野一致。
- **影响**：ERR-OBS、ERR-ERRP 类描述补一句边界说明（确认后由包 C 写 class_updates）；D-037 – D-042 的类边界不受影响。

### D-065 情绪面孔–词冲突任务（Etkin 2006）新建范式类（草案，待负责人确认）
- **问题**：包 E 问 Etkin et al. 2006（R0349）的情绪面孔–词冲突任务应作为 EMO-EST-002 还是新范式类。
- **决定**：**新建范式类**，暂定 `EMO-ECONF`（情绪冲突任务 / emotional conflict task），不作为 EMO-EST-002。EMO-EST（情绪 Stroop）测的是情绪词对无关任务（报颜色）的**注意偏向**，无任务相关的冲突；Etkin 任务中任务相关维度（面孔表情）与无关维度（情绪词）**冲突**，构念是情绪冲突的监测与解决，主要标记物为喙部 ACC / 杏仁核 BOLD 及冲突适应效应。按文件开头的判定基准（构念改变 → 独立范式类），应另立范式类。包 E 在 sprint 3 建 `EMO-ECONF-001`（first_source R0349 待核）与类条目（class_updates `action: add`），标记物如登记表无合适项则提交申请。
- **理由**：构念不同；与 D-019（情绪 Stroop 独立于 Stroop）同一口径。
- **影响**：EMO-EST-001 notes 中的说明保留；candidates.csv 在建档时新增候选行。

### D-066 新具体范式的 first_source 质量（草案，待负责人确认）
- **问题**：新具体范式多由公开数据集页面找到，first_source 常是数据集文献、综述或所见最早文献：包 A——PER-ODD-008（AMUSE 数据集文献 R1270，2011；更早的 AMUSE 论文未见）、SSR-SSVEP-006（数据集比较研究 R1267）、SSR-SSSEP-002（综述）；PER-ODD-002 对 Squires et al. 1975 的归属只依据 Wikipedia（R1272）；SSR-SSVEP-005（R1274）、PER-MMN-003（R1275）作者未见；PER-CUE-002 与 -001 共用 Posner 1980。包 C——ERR-OBS-002/-003、ERR-GAM-003 只有 R0714 的转引（R1319 – R1321），ERR-ERRP-002 题名未见（R1310），ERR-ADAPT-002（R1001）无作者/年份。包 E——EMO-FC-002、EMO-REG-002、SOC-GAZE-002、SOC-PAIN-002、STA-MW-002 只有题名，EMO-FILM-003 作者由 URL 推断。另有 64 个具体范式 first_source 为 TBD。
- **决定**：
  1. **允许**以数据集文献、综述或所见最早文献作为新具体范式的 first_source，但：`literature.csv` 中该行加 `qa_flag`（数据集/综述 → `weak_origin`；Wikipedia 或他文转引 → `secondhand`；题名未见 → `title_placeholder`）；文件 notes 写"earliest seen; origin not established"。本次登记的 R1266 – R1343 已按此标记（已执行）。
  2. 只有题名、无作者/年份的条目可以留在 draft，但**不能**进入 `reviewed`（D-033）；审核人核对原文时补全。
  3. **同一出处服务两个兄弟**（PER-CUE-001/-002 共用 Posner 1980；MOT-MI-003 与 MOT-ME-005 共用 Ofner 2017；MOT-MRCP-002/-003 共用 Jochumsen 2019）在该研究确实同时报告了两种配置时是允许的，notes 写明各自对应的实验/条件。
  4. TBD 继续按 D-032 集中处理，不在拆分时消耗检索；sprint 3 优先：P1 核心类（MOT-MI、PER-ODD、SSR-SSVEP、ERR-ERRP、MEM-NBK、LAN-OVS）的 TBD。
- **理由**：拆分阶段的目标是协议可复现，数据集文献正是协议细节的来源；用 qa_flag 区分"协议出处"与"源头"，不阻塞拆分。
- **影响**：QA 抽样中 6 / 50 有书目问题，见 `qa_sprint2.md`；`literature.csv` 中 sprint 2 新行带 qa_flag 的 23 条。

### schema 0.3 提议清单（由已确认决议产生，本版不改 schema）
- `protocol.marker_basis: documented | inherited | stand_in`（默认 documented），把 D-061 第 2、3 款的固定短语 `marker inherited from class` / `stand-in marker` 结构化；`validate.py` 届时按字段而非 notes 短语统计。（D-061 第 5 款，2026-10-05 列入。）
- `protocol.structure`（自由文本）记录准则 3 的子项 (b)–(e)（D-059 第 3 款，待 D-059 确认）。
- 词表：`interoceptive`、`sleep` 刺激模态（D-048）。
- `source.source_check: {bibliographic: <date>|null, content: <date>|null}`（可选），把 D-072 的两级核实短语结构化；`verified: true` ⇔ `content` 非空。（D-072 第 5 款，2026-10-07 列入。）

## 十九、各包的其余事项

### D-067 D-057 给号示例勘误（草案，待负责人知悉；勘误已执行）
- **问题**：包 B 指出 D-057 的 MI 示例与实际文件不符：示例把 MOT-MI-003 写成"单侧上肢 11 类动作想象（如肘屈伸、前臂旋前/旋后、手抓握/张开）"，而这组动作出自 Ofner et al. 2017（6 种动作 + 休息 = 7 类，MOABB Ofner2017，R1288），11 类出自 Jeong et al. 2020（GigaScience，R1292，类别名未在所见页面列出）。包 B 已按出处建 MOT-MI-003 = Ofner 2017、MOT-MI-011 = Jeong 2020。
- **决定**：
  1. 示例改为实际编号：MOT-MI-003 = 7 类上肢动作想象（Ofner 2017），MOT-MI-011 = 11 类上肢动作想象（Jeong 2020）。D-057 标题与状态行注明"给号示例已勘误，规则未改"，**确认状态不变**（勘误不改变任何给号规则）。
  2. 方法说明中英文 §6 增加与实际文件一致的 MI 给号示例表（原 §1 / §6 只引用 -001、-002，未写 -003，无需改动原句）。
  3. MOT-MI-011 的 11 个类别名由包 B 在 sprint 3 从原文补全（`protocol.classes` 目前为空）。
- **理由**：示例是给策展人照抄的，必须与文件一致；勘误由维护者执行，负责人知悉即可。
- **影响**：已执行——`curation/decisions.md`（D-057 标题、状态行、示例表）、`docs/methodology.md` 与 `docs/methodology.zh-CN.md` §6。

### D-068 包 B 的待核对项（草案，待负责人确认）
- **问题**：(1) IMG-MA：MOABB 两页对 BNCI2015_004 的类别列表不一致（IMG-MA-002 `classes` 空缺）；(2) 若干 protocol 字段来自现有文件描述或题名、未对照原文（notes 标 "to be checked"：MOT-ATT-001/-002、MOT-GRASP-001/-002/-004、MOT-HW-001、IMG-SPI-001/-002、IMG-CMD-002、MOT-FORCE-001 反馈未填）；(3) MOT-TRACK-001 的 first_source（R0889，"Decoding three-dimensional hand kinematics from EEG"）可能是三维中心外伸运动而非追踪；(4) MOT-HW 改名为"书写（尝试或实际执行）"以容纳 MOT-HW-002（健康被试实际书写，Crell & Müller-Putz 2024）；(5) MOT-MI-004 外骨骼行走 MI 数据库的类别集未核对。
- **决定**：
  1. IMG-MA：`classes` 保持空缺，直到核对 Scherer et al. 2015（R1301）原文；若 Keirn & Aunon 1990（R0842）原始为五任务，按 D-063 在 v0.1.0 发布前对调 -001/-002 内容。
  2. "to be checked" 字段保留，notes 已标；这些文件在核对前不能进入 `reviewed`。MOT-FORCE-001 的 `feedback` 在核对后补写。
  3. MOT-TRACK-001：核对 R0889；若为中心外伸，则 R0889 改配到 MOT-REACH（作为 MOT-REACH 的线索），MOT-TRACK-001 first_source 改 TBD。
  4. **接受** MOT-HW 改名（已按 class_updates 合入）：范式类的机制是书写轨迹的解码，"尝试"与"实际执行"的区别主要是被试人群（瘫痪 vs 健康），按 D-057 第 4 款属于参数；MOT-HW-002 与 -001 的区别依准则 1、2、4（已写）。MOT-ATT（尝试运动）与 MOT-ME（执行运动）作为两个范式类的划分不受影响（D-037）。
  5. MOT-MI-004：核对外骨骼行走数据库的类别集；若与"足部想象 vs 静息"不同，按准则 1 另给号。
- **影响**：包 B sprint 3 任务。

### D-069 包 C 的其余事项（草案，待负责人确认）
- **问题**：(1) ERP CORE 数据集凭记忆归入 CTL-FLK-002（箭头版），页面未写刺激类型；(2) ERR-VRPE-001 新增的 EMS 力反馈条件、ERR-ADAPT 终点反馈 vs 连续光标反馈是否构成新序号；(3) ERR-GAM-002 的准则 1 论据（-001 中金额是否为因素）待核；(4) D-042 若 ERR-AAF 并入 LAN-SIS，线索 R1259 交包 D。
- **决定**：
  1. ERP CORE 暂留 CTL-FLK-002，数据集条目 notes 已写"from memory, to be checked"；核对 ERP CORE 论文（R1317）后若为字母版则移回 CTL-FLK-001。
  2. EMS 条件按 D-060 第 4 款暂留 ERR-VRPE-001 的条件/变体；ERR-ADAPT 中"终点（离散）反馈 vs 连续光标反馈"是准则 4，有出处时给 ERR-ADAPT 新号。
  3. ERR-GAM-002 保留（准则 2 已足够：门与固定金额箭头 vs 标有金额的选项）；准则 1 一句在核对 Gehring & Willoughby 2002 后保留或删去。
  4. D-042 维持待议；若并入，在 LAN-SIS 下取 LAN-SIS-003（包 D）。
- **影响**：包 C sprint 3 任务。

### D-070 包 E 的其余事项（草案，待负责人确认）
- **问题**：(1) AMIGOS 用影片（非音乐视频）但用维度评分，暂挂 EMO-FILM-002；(2) LEMON 是否为睁/闭眼交替组块未核对，暂挂 STA-REST-002；(3) EMO-FILM 纯音乐诱发暂作 -002 的变体；(4) EMO-FILM 的 class_updates 把 6 个原有类别名删掉了。
- **决定**：
  1. AMIGOS：影片刺激 + 维度评分，与 -001（离散情绪影片）差准则 1、与 -002（音乐视频）差准则 2，应为**新具体范式 EMO-FILM-005**；核对 AMIGOS 数据集论文后由包 E 建档，在此之前留在 -002，notes 已写"placement provisional"。
  2. LEMON：核对数据集论文；若为单一条件连续静息，移回 STA-REST-001。
  3. 纯音乐诱发（无视频）相对 -002 改变刺激类型（准则 2），有出处时另给号。
  4. EMO-FILM 类别名按"并集"规则**保留**原有 6 个（已执行，见 D-071）。
- **影响**：包 E sprint 3 任务。

## 二十、流程

### D-071 sprint 2 合并与登记（流程记录，已执行）
- **内容**：
  1. **合并**：`git merge --no-ff sprint2/pkg-A … pkg-E`（"Merge pkg X sprint 2 (split into concrete paradigms)"），**无冲突**（各包只改本包文件与 `curation/work/pkg_<X>/`）。具体范式 267 → 405（A 59 → 89、B 49 → 84、C 52 → 73、D 53 → 83、E 54 → 76），新建 138 个；范式类 267 个不变（无 add / deprecate）。
  2. **class_updates**：74 条 `modify` 全部合入 `paradigms/_classes.yaml`（A 15、B 10、C 12、D 24、E 13）；结构校验：ID 均已登记、字段均在 schema 内、标记物均已登记、均在本包范围内。冲突 1 处：EMO-FILM 的更新删去了 6 个原有别名（仍为 EMO-FILM-001 的别名），按"别名取并集"保留。维护者补 MOT-GRASP 类的 MK.low_freq_kinematics。每条合入的类在 notes 记来源、`contributors` 加策展人。
  3. **标记物**：sprint 2 **没有新的标记物申请**（各包 marker_requests.csv 无新增行）；替代标记物见 D-061。`markers.csv` 从文件重新生成并新增 `used_by_class`、`n_classes`、`n_concrete` 列；`paradigm_markers.csv` 新增 `class`、`class_marker_ids` 列（405 行）。
  4. **文献**：78 条新线索登记为 R1266 – R1343（`found_via=curator_search_s2`），来源为各包 search_log（A：S2Axx；B：S2B-L01 – L17；C：S_SPULER2015 等；D：new_leads DN47 – DN53；E：S2-01 – S2-12、F03、F06）及文件 notes / first_source；S_KELLY2013 = 已有 R0578；R1093 补书目（Proudfit 2015，DOI 10.1111/psyp.12370；题名按 PDF 文件名，`title_placeholder`）。`paradigm_literature.csv` 新增新线索关联、97 条 first_source 关联、220 条 notes 中 R 编号的关联。notes 中的临时线索编号（S2B-L..、S_..、DN47 – DN53）替换为 R 编号，检索编号后注 `[=R….]`。
  5. **candidates.csv** 新增 `class`、`n_concrete` 列（267 行有类；27 行并入/排除/暂缓的作废 ID 留空）；新建 `curation/registry/concrete_paradigms.csv`（405 行）。
  6. **QA**：`scripts/check_siblings.py`（新）对全部范式类做兄弟比较：0 对完全相同、35 对待人工复核（见 `qa_sprint2.md`）；平凡修正 12 个过时的 -001 distinguishing、PER-ODD-001 的 `stimulus_coding` 误用、2 个 `n_classes`。
- **影响**：纳入里程碑 M2。

## 二十一、出处核实（第三冲刺）

### D-072 两级出处核实：书目核实与内容核实（已确认（专家裁定，负责人授权，2026-10-07））
> 状态：已确认（专家裁定，负责人授权，2026-10-07）。草案见 `curation/verification/README.md`（2026-10-05）。
- **问题**：方法说明 §3 只有一个开关 `verified: true`，含义是"对照原始文献核实"。第三冲刺用 Crossref / OpenAlex 接口核对了 682 条 first_source / 变体源的**书目字段**（题名、作者、年份、期刊、卷期页、DOI/PMID），但审核人没有读原文，不能确认该文献确实描述了该范式且是最早的。若把书目核实写成 `verified: true`，会把两件事混为一谈。
- **决定**：
  1. 出处核实分**两级**。**书目核实**（bibliographic）：条目的书目字段与 Crossref、OpenAlex 或 PubMed 的权威记录一致，必要时按记录更正。**内容核实**（content）：对照原文全文，确认该文献描述了该范式/配置，且按 D-031、D-062 的口径是最早的。
  2. `verified: true` **仍只表示内容核实**（方法说明 §3 的含义不变）。书目核实不改 `verified`。
  3. 书目核实的结果记在两处：`curation/verification/sources_check.csv`（一行一条源，`check_status` ∈ confirmed / corrected / mismatch / not_found / tbd_resolved / tbd_open，附 `pkg_reviewer`、`source_api`、`matched_doi`、`corrected_fields`）；以及条目 notes（具体范式 / 范式类）或变体 `note` 中的固定短语 `bibliography confirmed (<API>, <date>)` 或 `bibliography corrected (<API>, <date>)`。confirmed / corrected / tbd_resolved 的条目**必须**含该短语；mismatch / not_found / tbd_open 的条目**不得**含该短语。`scripts/verification_report.py` 检查这一一致性。
  4. 书目核实只校核记录本身；接口给出的年份若为在线年，与卷期对应的印刷年优先（D 包"年份口径"）；记录与条目题名或第一作者不一致者不写入（记 mismatch 或 not_found）。
  5. **schema 0.3 提议**：`source` 对象增加可选字段 `source_check: {bibliographic: <date>|null, content: <date>|null}`，把第 3 款的短语结构化；届时 `verified: true` ⇔ `source_check.content` 非空。本版不改 schema。
- **理由**：书目核实可以用接口批量做、可复核；内容核实需要全文和领域判断。分开记录既让里程碑 M3 的 682 条校核结果有处可查，又不让 `verified` 贬值。
- **影响**：方法说明中英文 §3 加一句两级定义；`curation/verification/README.md` 的表即为本决议的操作版；`coverage_report.py` 的 TBD 统计不变。
- **裁定说明**（2026-10-07）：按草案确认，补第 4 款（年份口径、不一致不写入）。**已执行**（维护者，2026-10-07）：682 行 `sources_check.csv` 合并；83 条 tbd_resolved 条目补短语 `bibliography confirmed (<API>, 2026-10-05; origin candidate, content unverified)`；`verification_report.py` 短语一致性检查 0 缺、0 多；`verified: true` 计 0。

### D-073 "凭记忆的候选 DOI、由接口记录确认"的处理（已确认（专家裁定，负责人授权，2026-10-07））
> 状态：已确认（专家裁定，负责人授权，2026-10-07）
- **问题**：第三冲刺中 Crossref / OpenAlex 的**书目检索**接口被代理持续以 429 拒绝（见 `search_protocol.md` S-004），只有"按 DOI / PMID 取记录"可用。对只有题名的行和 TBD 行，包 A（69 行，逐行在 `source_api` 注明 "DOI candidate from curator memory, record title matched"）、包 E（13 个 DOI + 4 个 TBD 候选，`fetch_log.md` #71–#88 说明）、包 D（5 个 "DOI-record probe"）、包 B（5 个 TBD 候选，直接按 DOI 取记录）采用了同一替代办法：审核人凭记忆写出候选 DOI，取回权威记录，只有记录题名（题名-only 行）或作者/题名/年份（TBD 行）与条目一致时才写入 YAML。这与方法说明 §3 "不推测任何标识符"在字面上有张力。
- **决定**：
  1. **允许**。写入 YAML 的不是"推测的标识符"，而是接口返回的权威记录——候选 DOI 只是查询键；记录与条目不一致者一律不写入（包 A 的 PER-ORN-001 首个候选、包 B 的 IMG-MA-001 Keirn & Aunon 1990 即为未写入的例子）。
  2. 这类条目的 notes（或变体 `note`）**必须**含固定短语 `origin candidate recalled, record confirmed via <API>`（API ∈ Crossref / OpenAlex / PubMed），`sources_check.csv` 的 `note` 加 "D-073: candidate from memory, record confirmed by API"。
  3. 这类条目在**内容核实前不得**标 `verified: true`；TBD 候选（tbd_resolved）尤其如此——记录一致只说明"这篇文献存在且书目正确"，不说明它是该范式的最早描述（D-031、D-062 第 3 款）。
  4. 审核人应逐行标注（包 A 的做法）；若只在工作日志中整体说明（包 E、D、B），维护者按日志能确定的范围整体标注，并在冲刺报告中注明这一局限。
- **理由**：在检索接口不可用时，这是唯一能把题名-only 记录补成完整书目的办法；把它写成固定短语，内容核实时可以优先复查。
- **影响**：**已执行**（维护者，2026-10-07）：108 条（A 69、E 26、D 8、B 5；含对应范式类与变体）加 D-073 短语；`verification_report.py` 统计该短语。包 B 的 5 条 tbd_resolved 与包 E 的类条目按第 4 款整体标注。

### D-074 书目核实遗留清单（not_found / tbd_open）→ 第四冲刺（草案，待负责人确认）
> 状态：草案，待负责人确认
- **内容**：第三冲刺 682 行中 **not_found 35 行、tbd_open 12 行**（合计 47 行；mismatch 0）。按包：A 7（not_found 5、tbd_open 2）、B 6（not_found 6）、C 23（not_found 15、tbd_open 8）、D 5（not_found 3、tbd_open 2）、E 6（not_found 6）。按实体：具体范式 30（not_found 21、tbd_open 9）、范式类 17（not_found 14、tbd_open 3）。
  - **因限流未检查**（包 C，15 行 = 9 个具体范式 + 6 个类，记为 not_found 但实为"未检查"）：CTL-MRP-001、CTL-WASON-001、ERR-ERRP-001、ERR-GAM-001、ERR-GAM-003、ERR-OBS-002、ERR-OBS-003、ERR-OGNG-001、ERR-PRT-001 及类 CTL-MRP、CTL-WASON、ERR-ERRP、ERR-GAM、ERR-OGNG、ERR-PRT。检索词已在 `sources_check.csv` 的 note 中。
  - **Crossref / OpenAlex 无记录**（20 行）：测验手册与指南（LAN-VF-001 / LAN-VF、MEM-FR-002、STA-SLP-001、STA-SLP-002 / STA-SLP、STA-MATB-001 / STA-MATB 的 NASA TM、SSR-SSVEP-003 的临床指南）、只有题名或"作者 年份"的转引（IMG-MA-001 / IMG-MA 的 R0842、PER-CAT-001 / PER-CAT、SSR-FPAS-001 / SSR-FPAS、MOT-SACC-001 / MOT-SACC、MOT-SMS-001 / MOT-SMS、STA-MW-002）。
  - **TBD 仍开放**（12 行，9 个具体范式 + 3 个类）：SSR-SWEEP-001 / SSR-SWEEP、CTL-FLK-002、CTL-SIM-002、CTL-STR-002、CTL-SW-003、ERR-AAF-001 / ERR-AAF、ERR-ERRP-003、ERR-GAM-002、MEM-PA-001 / MEM-PA。
- **提议**：全部转入第四冲刺，前提是取得机构数据库访问（Web of Science / Scopus / PsycINFO 或图书馆代理），以及 Crossref 的 polite pool（mailto 参数）或 OpenAlex API key 以避开限流。顺序：先做包 C 的 15 行"未检查"（书目检索即可），再做手册 / 指南（改用 WorldCat / 出版社记录，接受无 DOI 的完整书目），最后做 TBD 开放行（D-031 口径，需读原文）。
- **影响**：`coverage_M3.md` 的 TBD 计数（具体范式 9、范式类 3）即为 TBD 开放行；47 行在 `sources_check.csv` 中保留原 note 不动，第四冲刺在同一文件追加新行（不覆盖）。
