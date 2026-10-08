# 第一遍骨架 QA（交叉审核模拟）· sprint 1

> 维护者（maintainer），2026-10-03。范围：合并 5 个包后的 `integration` 分支。方法见第 1 节；所有结论都未对照原文（第一遍出处一律 `verified: false`），"一致"只表示条目与线索表内部一致。

## 1. 方法

- **抽样**：每包从本包全部范式文件中随机抽 8 个（`random.Random(20261003)`，按 ID 排序后抽样），共 40 个，占 267 个文件的 15%。
- **检查项**（脚本 + 人工）：
  1. **schema**：用 `scripts/validate.py` 的同一套 JSON Schema 校验单个文件。
  2. **first_source 与线索一致**：`status.csv` 的 `first_source_ref` 为 R 编号时，比较条目的 DOI、年份、PMID、题名与 `literature.csv` 中该行；为 `search` 时，确认 `literature.csv` 中已有 `found_via=curator_search` 的对应行（本次合并新增）；TBD 单列。另人工判断该文献是否真的是"任务程序的最早描述"（D-031）。
  3. **描述准确、中性**：人工通读中英文描述，与范式名称、标记物、源头题名对照；脚本扫描评价性词语（best、gold standard、powerful、robust、novel 等）。
  4. **标记物与登记表一致**：条目 `markers` 与 S-001 版 `paradigm_markers.csv`（合并前 `485deb8`）比较；新候选核对标记物已登记；每个标记物的 `recording_modality` 至少有一项出现在范式的 `recording_modality` 中。
  5. **PR 草稿存在**：`curation/work/pkg_<X>/pr/<ID>.md`。
- **全量补充检查**（全部 267 个文件，脚本）：PR 草稿、标记物偏离登记表、过时 notes、`verified: true`、引文标点。

## 2. 结果汇总

| 检查项 | 抽样 40 个 | 全量 267 个 |
|---|---|---|
| schema 有效 | 40 / 40 | 267 / 267（`validate.py` 0 问题） |
| first_source 与线索一致 | R 编号 12 个全部一致；检索所得 22 个均已有文献行；TBD 6 个 | TBD 37 个（见覆盖度报告） |
| 源头存疑（D-031，非任务源头或非最早） | 11 个 | — |
| 书目不完整 / 作者存疑 / 转引 | 4 个（IMG-CMD、LAN-SIS 只有题名；STA-HYPN 作者存疑；IMG-OLF 转引） | — |
| 描述准确、中性 | 40 / 40（1 个评价词误报："novel word" 为范式名） | — |
| 标记物与登记表一致 | 40 / 40；模态匹配 40 / 40 | 偏离 S-001 登记 0 个 |
| PR 草稿存在 | 40 / 40 | 266 / 267 → 维护者补建 STM-PBM-001 后 267 / 267 |
| `verified: true` | 0 | 0 |

**结论**：第一遍骨架在形式上质量良好（schema、标记物、PR 草稿、出处标注全部合规，所有包都严格使用了登记表 ID）。主要问题集中在**源头的选择**：抽样中 11 / 40（28%）的 `first_source` 是较晚的神经研究或非任务描述，加上 6 个 TBD，约 43%（17 / 40）的抽样条目在第二遍需要重新确定源头。这与各包自报的问题一致，说明 D-031 的规则需要在第二冲刺开工前确认。

## 3. 逐条结果（抽样 40 个）

| 包 | ID | schema | first_source ↔ 线索 | 描述 | 标记物 | PR 草稿 | 发现 | 处理 |
|---|---|---|---|---|---|---|---|---|
| A | PER-AAD-001 | 通过 | R0855: ok | 准确、中性 | 与 S-001 登记一致 | 有 | 源头存疑：R0855（单试次 EEG 注意解码）是 AAD-BCI 的代表研究，不是听觉选择性注意 N1 范式的源头 | 第二遍按 D-031 补源头；R0855 移至 notes |
| A | PER-AB-001 | 通过 | R0101: ok | 准确、中性 | 与 S-001 登记一致 | 有 | 引文标点 "blink?." 多余句点 | 已修正（平凡） |
| A | PER-BR-001 | 通过 | TBD | 准确、中性 | 与 S-001 登记一致 | 有 | first_source TBD | D-032 集中补源 |
| A | PER-GEP-001 | 通过 | TBD | 准确、中性 | 新候选（M1 登记） | 有 | first_source TBD；notes 写有"not yet in candidates.csv"（已过时） | notes 已改为 C 编号（平凡）；D-032 |
| A | PER-IC-001 | 通过 | TBD | 准确、中性 | 新候选（M1 登记） | 有 | first_source TBD；notes 过时 | notes 已修正（平凡）；D-032 |
| A | PER-NAVON-001 | 通过 | R0040: ok | 准确、中性 | 与 S-001 登记一致 | 有 | — | — |
| A | PER-SPN-001 | 通过 | TBD | 准确、中性 | 新候选（M1 登记） | 有 | first_source TBD；notes 过时 | notes 已修正（平凡）；D-032 |
| A | SSR-NSSEP-001 | 通过 | search -> R1104 | 准确、中性 | 新候选（M1 登记） | 有 | notes 过时 | notes 已修正（平凡） |
| B | IMG-CMD-001 | 通过 | R0893: ok | 准确、中性 | 与 S-001 登记一致 | 有 | 引文只有题名（R0893 线索无作者/年份字段） | 第二遍补全书目 |
| B | IMG-OLF-001 | 通过 | search -> R1125 | 准确、中性 | 新候选（M1 登记） | 有 | 源头为转引（Djordjevic 2005 只见于他文参考文献，B 已自报） | literature.csv 标 secondhand；审核人核原文 |
| B | IMG-SPI-001 | 通过 | search -> R1109 | 准确、中性 | 与 S-001 登记一致 | 有 | — | — |
| B | MOT-MIRR-001 | 通过 | R0106: ok | 准确、中性 | 与 S-001 登记一致 | 有 | 源头存疑：Gabrieli et al.（阿尔茨海默病研究）不是镜像描摹任务的最早描述 | D-031；第二遍补源头 |
| B | MOT-PASS-001 | 通过 | search -> R1119 | 准确、中性 | 新候选（M1 登记） | 有 | 源头可能不是最早的皮层-运动学相干研究 | 第二遍查 CKC 首报 |
| B | STM-ADBS-001 | 通过 | search -> R1128 | 准确、中性 | 新候选（M1 登记） | 有 | first_source 题名（Controlling Parkinson's Disease With Adaptive DBS）像评论/综述，非原始研究 | 审核人核原文，必要时换源头 |
| B | STM-PHTMS-001 | 通过 | search -> R1132 | 准确、中性 | 新候选（M1 登记） | 有 | 读出为 MEP（外周）；已按 D-031 在 notes 注明需补首个脑记录研究 | D-031 |
| B | STM-VIB-001 | 通过 | search -> R1130 | 准确、中性 | 新候选（M1 登记） | 有 | Naito et al. 2007 为神经研究，不是腱振动错觉的源头（B 已自报） | D-031；第二遍补源头 |
| C | CTL-CONF-001 | 通过 | search -> R1145 | 准确、中性 | 新候选（M1 登记） | 有 | 信心判断任务早于 Boldt & Yeung 2015；当前源头是"信心–Pe"研究 | D-031 复核 |
| C | CTL-CPT-001 | 通过 | R0003: ok | 准确、中性 | 与 S-001 登记一致 | 有 | — | — |
| C | CTL-SIM-001 | 通过 | R0016: ok | 准确、中性 | 与 S-001 登记一致 | 有 | — | — |
| C | CTL-VBC-001 | 通过 | search -> R1148 | 准确、中性 | 新候选（M1 登记） | 有 | 出价程序（BDM 拍卖）早于 Plassmann et al. 2007；当前源头是首个 fMRI 研究 | D-031 复核 |
| C | CTL-WCST-001 | 通过 | search -> R1136 | 准确、中性 | 与 S-001 登记一致 | 有 | — | — |
| C | ERR-CHGPT-001 | 通过 | search -> R1138 | 准确、中性 | 新候选（M1 登记） | 有 | — | — |
| C | ERR-ERRP-001 | 通过 | R0403: ok | 准确、中性 | 与 S-001 登记一致 | 有 | C 自报 R1085 可能更早（无作者/年份） | 第二遍核对 |
| C | ERR-INST-001 | 通过 | search -> R1133 | 准确、中性 | 与 S-001 登记一致 | 有 | 当前源头为首个 fMRI 研究（O'Doherty 2004），非任务源头 | D-031 复核 |
| D | LAN-HIER-001 | 通过 | search -> R1161 | 准确、中性 | 与 S-001 登记一致 | 有 | 原线索全部错配（D 自报），已改配；源头由检索补得 | D-055 已执行 |
| D | LAN-NWL-001 | 通过 | TBD | 准确、中性 | 新候选（M1 登记） | 有 | first_source TBD；"novel" 为范式名，非评价性用语（误报） | D-032 |
| D | LAN-PN-001 | 通过 | R0914: ok | 准确、中性 | 与 S-001 登记一致 | 有 | 源头存疑：R0914（ECoG γ，2001）是神经研究，不是图片命名任务源头 | D-031；第二遍补源头 |
| D | LAN-SIS-001 | 通过 | search -> R1167 | 准确、中性 | 新候选（M1 登记） | 有 | 引文只有题名，无作者/年份 | 第二遍补全书目；与 ERR-AAF-001 的关系见 D-042 |
| D | MEM-DS-001 | 通过 | search -> R1158 | 准确、中性 | 与 S-001 登记一致 | 有 | 描述中"EEG 研究报告额中线 θ"依赖未核对的 DN06/DN07 | D-043 |
| D | MEM-MST-001 | 通过 | R0373: ok | 准确、中性 | 与 S-001 登记一致 | 有 | — | — |
| D | MEM-RMEM-001 | 通过 | TBD | 准确、中性 | 新候选（M1 登记） | 有 | first_source TBD | D-032 |
| D | MEM-SWM-001 | 通过 | R0023: ok | 准确、中性 | 与 S-001 登记一致 | 有 | — | — |
| E | EMO-DOT-001 | 通过 | R0072: ok | 准确、中性 | 与 S-001 登记一致 | 有 | — | — |
| E | EMO-SOUND-001 | 通过 | search -> R1170 | 准确、中性 | 与 S-001 登记一致 | 有 | first_source 为较晚神经研究（E 自报），notes 已加 D-031 说明 | D-031 |
| E | SOC-ANIM-001 | 通过 | search -> R1189 | 准确、中性 | 新候选（M1 登记） | 有 | 源头为 PET 研究；标记物原只登记 fMRI | D-050 已为 MK.BOLD_TPJ、MK.BOLD_mPFC 加 PET |
| E | SOC-EYE-001 | 通过 | search -> R1191 | 准确、中性 | 新候选（M1 登记） | 有 | 与 SOC-GAZE-001 的边界待议 | D-040 |
| E | SOC-SFB-001 | 通过 | search -> R1188 | 准确、中性 | 新候选（M1 登记） | 有 | — | — |
| E | STA-DREAM-001 | 通过 | search -> R1193 | 准确、中性 | 新候选（M1 登记） | 有 | 序列唤醒报告的程序早于 Siclari et al. 2017；当前源头为神经研究 | D-031 复核 |
| E | STA-HYPN-001 | 通过 | search -> R1195 | 准确、中性 | 新候选（M1 登记） | 有 | 作者字段 "Spiegel DR et al" 来自只列出 Spiegel 的机构页，首作者与姓名缩写可能有误；源头为较晚研究（E 自报） | 审核人核原文；D-031 |
| E | STA-SLP-001 | 通过 | search -> R1180 | 准确、中性 | 与 S-001 登记一致 | 有 | —（R&K 1968 为标准判读手册，作为源头可接受） | — |

## 4. 已修正的平凡问题

| 问题 | 范围 | 处理 |
|---|---|---|
| notes 中写有 "not yet in candidates.csv"（新候选已登记后过时） | 全量 18 个（包 A 新候选），抽样中 4 个 | 改为 "registered in curation/candidates.csv as C2xx (D-053, milestone M1)" |
| PER-AB-001 引文 "An attentional blink?." 多余句点 | 1 个 | 删除句点 |
| 已作废 ID 的 PR 草稿（IMG-WORD-001、STM-CLAS-001、SOC-CIT-001） | 3 份 | 在文件顶部加"已作废"说明，保留原文 |
| STM-PBM-001 缺 PR 草稿（维护者代建条目） | 1 份 | 维护者补建 `curation/work/pkg_B/pr/STM-PBM-001.md` |

## 5. 未修正、移交第二遍的问题

1. **源头选择（D-031）**：PER-AAD-001、MOT-MIRR-001、MOT-PASS-001、STM-VIB-001、CTL-CONF-001、CTL-VBC-001、ERR-INST-001、LAN-PN-001、STA-DREAM-001、EMO-SOUND-001、STA-HYPN-001。抽样外的同类条目见 D-031 列表。建议第二遍每包先用 1 天把"源头 vs 首个神经记录"按 D-031 分开。
2. **需核原文**：STM-ADBS-001（源头可能是评论文章）、STA-HYPN-001（作者）、IMG-OLF-001（转引）、ERR-ERRP-001（R1085 可能更早）、MEM-DS-001（DN06/DN07，D-043）。
3. **书目不完整**：IMG-CMD-001、LAN-SIS-001 的引文只有题名。多为 S-001 web_search 线索的共性问题（线索本身没有作者/年份），建议维护者在有数据库访问时批量补全（D-032）。
4. **交叉审核分工**：第二遍按 PR 模板的"交叉审核包"（A 审 B、B 审 C、C 审 D、D 审 E、E 审 A）进行，每人每周至少对照原文核实 10 个源头。
