# 工作日志 · 包 E 情绪、社会与脑状态 · sprint 2

> 每次工作追加一节（最新在下）。写：写了哪些 `protocol`、拆出了哪些具体范式（对应 `split_log.csv` 行）、保留了哪些变体及理由、`class_updates.yaml` 的改动、遇到的问题、待例会事项、跨包交接。

<!-- 模板
## YYYY-MM-DD · <策展人>
- protocol：
- 拆分 / 保留：
- class_updates：
- 核对线索：
- 问题 / 待例会：
- 交接给其他包：
-->

## 2026-10-03 · curator_e（sprint 2，D-057 拆分）
- **protocol**：本包 54 个 `-001` 全部写入 `protocol`（n_classes/classes/cue/paradigm_timing/feedback/distinguishing）。混合了多个配置的 `-001` 收窄为标准配置并改写描述与名称：EMO-FILM、EMO-STRESS、EMO-THREAT、EMO-FACE、EMO-FC、EMO-REG、SOC-TOM、SOC-TRUST、SOC-DICT、SOC-GAZE、SOC-PAIN、SOC-NAME、STA-NF、STA-SCP、STA-REST、STA-SLP、STA-MW、STA-DRV。
- **拆分**：新建 22 个具体范式（split_log.csv 中"已建文件"且非 -001 的行）：EMO-FILM-002/003/004、EMO-FC-002/003、EMO-MID-002、EMO-STRESS-002、EMO-FACE-002、EMO-REG-002、SOC-TOM-002、SOC-TRUST-002/003、SOC-DICT-002、SOC-GAZE-002、SOC-PAIN-002、SOC-NAME-002、STA-NF-002、STA-SCP-002、STA-REST-002、STA-SLP-002、STA-MW-002、STA-DRV-002。具体范式 54 → 76。
- **变体复核（README 表 8 条）**：转为新号 6 条——EMO-FC 恐惧泛化 → -002（准则 1）；EMO-FILM 音乐/音乐视频 → -002（准则 1、2；纯音乐暂作 -002 的变体，提议另号）；EMO-MID 社会激励延迟 → -002（准则 2）；SOC-TOM 定位任务 → -002（准则 1、3）；SOC-TRUST 超扫描多轮信任 → -003（准则 3，超扫描本身仍为 -003 的变体）；STA-NF rtfMRI → -002（准则 1、3）。保留为变体 2 条——SOC-JA 超扫描（记录配置，D-021）；STA-NF fNIRS（移到 -002 下，仅记录模态不同）。新增参数级变体：SOC-TOM-001 Sally-Anne。
- **STA-SCP 重排**：-001 改为二分类 SCP 训练（无拼写），原 Birbaumer 1999 拼写装置移到 -002；-001 first_source 改为 TBD（源头 Elbert 等 1980 未检到）。请维护者确认这一 -001 改义（序号未被使用过，未违反永久性）。
- **D-031**：SOC-CYB（Williams, Cheung & Choi 2000）、EMO-THREAT（Schmitz & Grillon 2012 协议文）已改 first_source，原神经研究移入 notes 的 "First neural recording:" 句；STA-NF-001 由 TBD 改为 Sterman & Friar 1972（最早见到的记录）。其余 D-031 条目（EMO-SOUND、SOC-SELF、SOC-VPT、SOC-TPP、STA-MED、STA-HYPN、STA-PSY）未检到源头，first_source 不变（D-032：不再为 TBD 消耗检索）。
- **class_updates.yaml**：13 条 modify（STA-NF、STA-SCP、SOC-CYB、EMO-THREAT、EMO-FILM、EMO-FACE、EMO-REG、EMO-MID、EMO-FC、STA-MW、STA-SLP、STA-DRV、SOC-GAZE；后四条之外均含描述泛化或源头修改）；无新范式类。
- **TBD first_source（具体范式）**：EMO-EST-001（原有）、EMO-FILM-004、STA-SCP-001、STA-DRV-002。
- **核对线索**：新出处均 verified: false；只见标题的（EMO-FC-002、EMO-REG-002、SOC-GAZE-002、SOC-PAIN-002、STA-MW-002）未填作者与年份。EMO-FILM-003 作者由 URL 推断，已在 notes 注明。
- **问题 / 待例会**：(1) EMO-EST 情绪面孔-词冲突（Etkin 2006）是 EMO-EST-002 还是新范式类；(2) STA-NF-002 的反馈信号标记物（目标脑区 BOLD）无通用登记项，暂用 MK.BOLD_amygdala；(3) AMIGOS 用影片而非音乐视频，暂挂 EMO-FILM-002；(4) LEMON 是否为睁闭眼交替组块待核。
- **交接**：EMO-FC-003 使用 MK.frontal_midline_theta（包 B 所有）；无其他跨包修改。
