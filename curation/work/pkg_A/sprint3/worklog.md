# 包 A「感知与稳态」sprint 3 工作日志 — 出处书目核实

- 审核人 / Reviewer：curator_e（交叉审核：包 A 由 curator_a 编写）
- 日期：2026-10-05
- 分支 / 工作树：`sprint3/pkg-A`，`/home/claude/work/wt3_A`
- 依据：`curation/verification/README.md`（两级核实，本冲刺仅书目级，`verified` 保持 false）、`queue_pkg_A.csv`（150 行）、方法说明 §3–§4、D-031、D-062。

## 1. 结果汇总

| check_status | 行数 | 其中 concrete | class | variant |
|---|---|---|---|---|
| confirmed | 56 | 36 | 19 | 1 |
| corrected | 30 | 17 | 11 | 2 |
| tbd_resolved | 57 | 31 | 26 | 0 |
| not_found | 5 | 3 | 2 | 0 |
| tbd_open | 2 | 1 | 1 | 0 |
| mismatch | 0 | — | — | — |
| **合计** | **150** | 88 | 59 | 3 |

- 改动的 YAML 文件：50 个具体范式文件（17 corrected + 31 tbd_resolved + 2 含变体源更正的文件 SSR-CVEP-003、SSR-SSVEP-004）；另有 37 个文件只在 `notes` 追加 `bibliography confirmed (...)` 标签。`paradigms/_classes.yaml` 未直接修改，56 条类修改写在 `class_updates.yaml`。
- `python3 scripts/validate.py`：405 paradigms, 267 classes … 0 problem(s), 0 warning(s)。
- 抓取次数：106（预算 ~170），见 `fetch_log.md`。

## 2. 工具可达性（与 README 表的差异）

| 来源 | 本次实际 |
|---|---|
| Crossref `works/<DOI>` | 可用，但约每 10 次请求后被限流（429，含代理层 429）；限流后改用 OpenAlex 同记录 |
| Crossref `works?query.bibliographic=` | 全程 429（4 次尝试，未重试同一 URL） |
| OpenAlex `works/doi:` 与 `works/pmid:` | 可用，偶发 429 |
| OpenAlex `works?search=` / `filter=title.search` | 全程 429 |
| PubMed 文章页 | 返回 Google reCAPTCHA 页面，不可用；PMID 行改用 OpenAlex `works/pmid:` |

因此**书目检索端点在本次会话中不可用**。对无 DOI 的行（题名-only 行与 TBD 行），采用的替代办法是：取审核人记忆中的候选 DOI/PMID，抓取其权威记录，**只有当记录题名与 YAML 题名完全一致（题名-only 行）或该记录是明确的原始研究（TBD 行）时才采用**；候选来源在 `sources_check.csv` 的 `source_api` 与 `note` 中逐行注明（"DOI candidate from curator memory, record title matched"）。未命中的候选（PER-ORN-001 的第一个 DOI 指向 Alain, Arnott & Picton 2001）记为失败查询，不写入。

## 3. 判定口径

- `confirmed`：题名（忽略大小写/标点/变音符）、第一作者、年份、期刊四项一致即确认，不改写引文（即便缺卷期页，也不视为错误）；只在 `notes` 追加标签。
- `corrected`：同一篇文献但引文**缺作者/缺年份/"et al."未展开/作者缺漏**，或题名-only 记录找到权威记录；按统一格式 `Author AB, Author CD. Title. Journal. Year;Vol(Issue):Pages.` 重写 `citation`，补 `doi`、`year`。`pmid` 不新增（PubMed 不可达，OpenAlex 的 pmid 只写在 `sources_check.csv` 的 `matched_pmid`）。
- 来源标签按实际接口写：`(Crossref, 2026-10-05)` 或 `(OpenAlex, 2026-10-05)`。
- `tbd_resolved`：按 D-031 第 1 款取**最早描述任务程序的原始研究**（可为行为学/心理物理研究），写 `citation+doi+year`，`verified: false`，notes 加 "candidate origin found by bibliographic search (...); content unverified"。
- 类条目：按 D-062，类源头 = 类中最早的、书目可识别的原始研究；本包所有类的 first_source 与 `-001` 相同，故复用 `-001` 的记录（不额外抓取），并在 notes 注明 "(class origin taken from <ID>-001, D-062)"。PER-BR 类取 Wheatstone 1838（-001）而非 Lansing 1964（-002）；SSR-SSVEP 类维持 D-062 裁定（Regan 1966）。

## 4. 值得维护者注意的条目

1. **年份口径**（在线日期 vs 印刷卷期）：PER-MMN-003（Clin Neurophysiol 115(1)，写 2004；OpenAlex 在线 2003-12-04）、SSR-FPVS-001（Neuropsychologia 52，写 2014；OpenAlex 2013）、PER-AAD-001（Cereb Cortex 25(7)，Crossref issued 2015；YAML 原无年份）、SSR-SSSEP-002（Front Hum Neurosci 9:716，写 2016）。
2. **非原始研究作源头**：SSR-SSSEP-002 的 first_source 是综述（Ahn, Kim & Jun 2016）；只做书目更正，是否替换由维护者决定（D-031/D-062）。
3. **TBD 候选中的优先权问题**：PER-ABR-001 用 Jewett & Williston 1971，但 Sohmer & Feinmesser 1967（抓取被 429 拒绝，未重试）更早；PER-IC-001 用 Kanizsa 1976（Sci Am），原始 1955 意大利文无记录；PER-VMMN-001 用 Tales 1999，Czigler & Csibra 1990 或更早；SSR-FPVS-001 用 Liu-Shuang 2014，Heinrich 2009 或更早；PER-MVEP-001 用 Kuba & Kubová 1992，Clarke 1972 运动反转 VEP 未查。均写在 `sources_check.csv` 的 note 中。
4. **行为学源头 + 首个神经记录**（D-031 第 3 款，待第二遍写 `First neural recording:` 句）：PER-ADDS-001（Theeuwes 1992 → Hickey 2009）、PER-AMASK-001（Wegel & Lane 1924）、PER-BR-001（Wheatstone 1838 → Lansing 1964 / Tong 1998）、PER-CB-001（Rensink 1997）、PER-IB-001（Mack & Rock 1998 → Pitts 2012）。
5. **not_found**（5 行）：PER-CAT / PER-CAT-001（1982 书章，无 DOI）、SSR-FPAS / SSR-FPAS-001（2019 会议摘要）、SSR-SSVEP-003（题名-only 指南）。检索端点恢复后可再查。
6. **tbd_open**（2 行）：SSR-SWEEP / SSR-SWEEP-001，候选 Regan 1973、Tyler et al. 1979（Invest Ophthalmol，无 DOI），未能抓到记录。
7. 无 `mismatch`：所有已填 DOI 都指向 YAML 所述论文。
8. SSR-FFR-002 第一作者按 OpenAlex 规范名写为 Russo-Ponsaran NM；期刊署名为 Russo N。

## 5. 文件

- `sources_check.csv`（150 行）、`class_updates.yaml`（56 条 modify）、`fetch_log.md`（106 次抓取）、`pr/<ID>.md`（50 个改动文件各一份）。
- 提交：按 ~25 行一次的 wip 提交（rows 1–25 … 101–125）+ 收尾提交；包含 perception 与 steady_state 两族的 YAML 改动与过程文件。
