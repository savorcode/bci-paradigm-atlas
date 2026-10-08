# 包 E「情绪、社会与脑状态」· sprint 3 书目核实 · 工作日志

- 审核人：curator_d（交叉审核：D 审 E）
- 日期：2026-10-05
- 分支：`sprint3/pkg-E`
- 依据：`curation/verification/README.md`（两级核实，D-072 草案）、`curation/verification/queue_pkg_E.csv`（135 行）、方法说明 §3–§4、D-031、D-062
- 级别：**仅书目核实**。所有 `verified` 仍为 false；书目一致不等于内容核实通过。

## 1. 结果汇总

| check_status | 具体范式 | 变体 | 范式类 | 合计 |
|---|---|---|---|---|
| confirmed | 25 | 0 | 21 | 46 |
| corrected | 43 | 5 | 30 | 78 |
| tbd_resolved | 4 | 0 | 1 | 5 |
| not_found | 4 | 0 | 2 | 6 |
| mismatch | 0 | 0 | 0 | 0 |
| **合计** | 76 | 5 | 54 | 135 |

- 改了 `first_source` / 变体 `source` 书目字段的 YAML 文件：**49 个**（每个有 `pr/<ID>.md`）；另 27 个文件只在 `notes` 追加了核实句。
- 范式类 54 条全部写入 `class_updates.yaml`（未直接改 `_classes.yaml`）：30 条带 `first_source` 更正、1 条 TBD 候选（EMO-EST）、其余只追加 notes。
- 取数 100 次，详见 `fetch_log.md`。`python3 scripts/validate.py`：0 errors / 0 warnings。

## 2. 做法与偏离说明

1. **数据源**。Crossref 按 DOI 取记录对并发/连续请求频繁 429，代理拒绝的 URL 一律不再访问；改用 README 列为可用回退源的 OpenAlex（`works/doi:`、`works/pmid:`）。因此 notes 中的核实句写实际使用的来源：`bibliography confirmed (OpenAlex, 2026-10-05)` 或 `(Crossref, 2026-10-05)`，句式与 README 一致，便于正则提取。
2. **PubMed** 文章页第一次访问即被代理拒绝（429），之后未再访问；因此**没有新增任何 `pmid`**（规则：只在 PubMed 上看到才加）。OpenAlex 记录里出现的 PMID 写在 `sources_check.csv` 的 note 中供维护者参考。
3. **只有题名的引文**（EMO-FACE-001、EMO-FC-001、EMO-IAPS-001、SOC-PAIN-001、SOC-GAZE-001、SOC-PAIN-002 等）用 PMID 或 Crossref 检索取得记录，题名完全一致时才按 house style 重写并加 DOI。
4. **凭记忆的 DOI**。Crossref 书目检索对较长查询串返回与查询无关的默认列表（fetch_log #68、#95–#97），OpenAlex 检索接口 429；13 条无 DOI 行是审核人凭记忆写出 DOI、取回记录后核对题名 / 第一作者 / 年份一致才写入（fetch_log 末尾列出）。记录与引文不一致者一律未写。
5. **年份取印刷卷年份**。OpenAlex 的 `publication_year` 对在线先发表的论文给的是上网年（EMO-FC-002、EMO-REG-002、SOC-GAZE-002、SOC-PAIN-002、STA-HYPN-001、EMO-FILM-004），引文按卷期对应的印刷年写，并在 note 与 PR 草稿注明；EMO-STRESS-001 的 OpenAlex 年份 2008 为 Karger 上网年，保留 1993。
6. **house style**：`Author AB, Author CD. Title. Journal. Year;Vol(Issue):Pages.`；"et al." 一律按记录展开（STA-PSY-001 26 位作者）。记录本身只列一位作者的（Montague 2002）照记录写并注明。

## 3. 值得维护者注意的更正

- **SOC-JA-001**：原引文把 Kelso 列为第一作者且无年份；记录为 Tognoli E, Lagarde J, DeGuzman GC, Kelso JAS, PNAS 2007;104(19):8190-8195。
- **STA-HYPN-001**：原引文 "Spiegel DR et al."；记录第一作者为 Jiang H（Spiegel D 末位），Cereb Cortex 2017;27(8):4083-4093。
- **STA-MED-001**：用 1966 年原始论文（Kasamatsu A, Hirai T. Folia Psychiatr Neurol Jpn 20(4):315-336，doi:10.1111/j.1440-1819.1966.tb02646.x）替换了 1973 年 J Am Inst Hypnosis 的转载记录（worklog 已标"1966 原文未核"，作者顺序也反了）。这超出同一记录的字段补全，请确认。
- **SOC-TPP-001**：原引文无作者；记录为 Fehr E, Fischbacher U.
- **EMO-FILM-002 变体**（Koelsch 2014）与 **STA-NF-002 变体**（Klein et al. 2024）的记录类型分别为 Review / Perspective，不是源头研究——与变体 note 的说法一致，书目已补全，源头仍待找。
- **STA-REST-001**：OpenAlex 的该 DOI 记录损坏（题名/作者属于另一篇），改用 Crossref 记录。
- **EMO-STRESS-002**：OpenAlex 给出 DOI 10.1139/jpn.0541，Crossref 未能确认，未写入。

## 4. TBD

| 条目 | 结果 | 候选 |
|---|---|---|
| EMO-EST-001（类 EMO-EST 同） | tbd_resolved | Gotlib IH, McCann CD. Construct accessibility and depression. J Pers Soc Psychol 1984;47(2):427-439（R0137 综述所引的最早情绪 Stroop；Watts et al. 1986 为另一候选，未取回） |
| EMO-FILM-004（SEED-IV） | tbd_resolved | Zheng WL, Liu W, Lu Y, Lu BL, Cichocki A. EmotionMeter. IEEE Trans Cybern 2019;49(3):1110-1122（SEED 主页指定引用） |
| STA-DRV-002（SEED-VIG） | tbd_resolved | Zheng WL, Lu BL. A multimodal approach to estimating vigilance using EEG and forehead EOG. J Neural Eng 2017;14(2):026017（SEED 主页指定引用） |
| STA-SCP-001 | tbd_resolved | Elbert T, Rockstroh B, Lutzenberger W, Birbaumer N. Biofeedback of slow cortical potentials. I. EEG Clin Neurophysiol 1980;48(3):293-301（notes 中的 "memory-only lead"，早于 R1333/R1334） |
| 类 STA-SCP | confirmed（Birbaumer 1999） | 按 D-062 未改类源头；1980 候选写入类 notes，是否替换由维护者决定 |

均为 `verified: false`，notes 写 "candidate origin found by bibliographic search; content unverified"。tbd_open：0。

## 5. not_found（引文原样保留，只追加 notes）

- STA-MATB-001 / 类 STA-MATB：NASA TM 104174（NTRS 19920007912）无 Crossref 记录。
- STA-MW-002：2004 年书章无记录；Crossref 只有 2001 年 PsycEXTRA 会议记录（Schooler JW, Reichle ED, Halpern DV，题名用 "meta-awareness"），作者线索记入 note。
- STA-SLP-001 / 类 STA-SLP：Rechtschaffen & Kales 1968 手册无记录。
- STA-SLP-002：AASM 2007 手册无记录。

## 6. 提交

按族各一次提交（emotion、social、state）+ 过程文件一次提交；哈希见最终回复。
