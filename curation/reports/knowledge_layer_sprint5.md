# 知识层第五冲刺报告

> 分支 `knowledge/layer-2`，2026-10-14。决策见 D-075、D-076（已确认）、D-077（草案）。过程文件在 `curation/work/sprint5/`。

## 一句话

按 D-076 补齐 11 个新词，合并 TPJ 重复 ID，再为 30 个标记物补上来源脑区和反映的构念。有出处关联的标记物从 51 个增加到 81 个；接入范式工厂后，被图谱证据替换的 D 级临时值从 68 条增加到 99 条。

## 数量

| 项目 | 冲刺 4 结束 | 现在 |
|---|---|---|
| 构念 | 81 | 90（新增 9 个，7 个对上 Cognitive Atlas） |
| 脑区 | 43 | 45（新增 BR.OFA、BR.SEF；BR.temporoparietal_junction 弃用） |
| 有关联的标记物 | 51 | 81 |
| 生成源（标记物 → 脑区） | 92 | 137（A 36 / B 52 / C 49） |
| 反映构念（标记物 → 构念） | 142 | 207（A 52 / B 102 / C 53） |
| 文献线索 | 1,537 | 1,654（新增 117 条 R1559–R1675） |

冲刺 4 中暂挂在相近 ID 下的 13 条关联已改挂到新词，例如 N170 的生成源由 BR.LOC 改为 BR.OFA，额叶 α 不对称改为反映 CN.approach_motivation；LPP 与前岛叶在保留原关联的同时，分别增加 CN.emotion_regulation 与 CN.empathy。

本轮 30 个标记物：

- F 感知与注意：cVEP、α 偏侧化、VAN、SEP N20、N2pc、视觉 P2、后部 N2、FFR、ASSR、mVEP
- G 记忆、控制与状态：困倦 θ、顶叶新旧效应、海马 θ、NoGo P3、FN400、Dm、转换正波、N450、CPP、眼跳前电位
- H 情绪、语言与社会：EPN、pSTS BOLD、语音包络跟随、语言结构跟随、ERAN、CPS、脑间同步、ISC、HEP、省略反应

## 工厂“让位”核对

用 `curation/work/sprint4/factory_yield.py` 复算（工厂 `bridge.yaml` 版本 2026-10-08）：

| 指标 | 冲刺 4 结束 | 现在 |
|---|---|---|
| 图谱写入的“反映构念”边 | 111 | 173（A 46 / B 80 / C 47） |
| 图谱写入的“生成源”边 | 92 | 137 |
| 桥接表 D 级关联（共 220 条）实际使用 | 152 | 121 |
| 被图谱证据替换的 D 级关联 | 68 | 99 |

## 出处核查

- 每个 DOI 都经 Crossref 或 OpenAlex 取回记录核对；Crossref 限流时改用 OpenAlex。取回后发现指向别的文章的 2 个候选 DOI 已弃用。
- 维护者抽查 15 个：均指向所引文章；2 处小差异不改（Grosbras 2012 在 OpenAlex 记为在线首发年 2011；Holzgrefe 在 OpenAlex 记为 Holzgrefe-Lang）。
- 所有出处 `verified: false`。需优先对照原文的：Liotti 2000、Everling 1997、Sammler 2013（ERAN → STG）、Holzgrefe 2013。

## 遗留问题

1. 新的词表申请 6 条（D-077）。
2. 证据偏弱的生成源：视觉 P2、后部 N2 只有头皮分布（C）；cVEP 的 V1 生成源借用多焦 VEP 研究；CPS 的两条生成源只有音乐 CPS 的源定位。
3. `CN.approach_motivation`、`CN.social_decision` 没有 Cognitive Atlas 对应；BR.OFA、BR.SEF 的 HCP / AAL3 对应置信度低。
4. 工厂已有先验的关联仍以工厂权重为准（同冲刺 4 报告第 5 条）。
5. 其余 48 个标记物待下一轮，多为单一范式使用的专用标记物。
