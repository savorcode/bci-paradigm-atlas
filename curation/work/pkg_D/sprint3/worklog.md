# 包 D sprint 3 工作日志 — 书目核实（审核人 curator_c，交叉审核 C 审 D）

日期：2026-10-05　分支：sprint3/pkg-D　级别：书目核实（D-072），`verified` 一律保持 false。

## 做了什么

1. 读 `curation/verification/README.md`、`queue_pkg_D.csv`（137 行：83 具体范式、1 变体、53 范式类）、方法说明 §3–§4、D-031、D-062。
2. 逐行取权威记录：有 DOI 的走 Crossref `works/<DOI>`（Crossref 429 时用 OpenAlex `works/doi:` 兜底）；只有 PMID 的，PubMed 页面返回 reCAPTCHA，改用 OpenAlex `works/pmid:`；无标识符的走 Crossref 书目检索（检索接口限流严重，部分改用"候选 DOI 探针"：以候选 DOI 直接取记录，只在作者/题名/年份与条目一致时采用）。请求明细见 `fetch_log.md`（112 次请求，含失败）。
3. 比对题名、第一作者、年份、期刊、卷期页；按规则写 `check_status`，更正 YAML（Python yaml.safe_load/safe_dump，保留其余字段），`notes` 追加 `bibliography confirmed/corrected (<API>, 2026-10-05)`；类条目的改动写入 `class_updates.yaml`，不改 `_classes.yaml`；变体改范式文件内的 `variants[].source`。
4. TBD 行按 D-031 第 1 款找最早的任务程序描述（允许行为学研究与测验手册）；找到的写为 first_source（`verified: false`，notes 注明 "candidate origin found by bibliographic search; content unverified"，并保留原 TBD 文字）。
5. `python3 scripts/validate.py`：0 problem(s), 0 warning(s)。

## 结果

| check_status | 行数 |
|---|---|
| confirmed | 17 |
| corrected | 94 |
| tbd_resolved | 21 |
| tbd_open | 2 |
| not_found | 3 |
| mismatch | 0 |
| 合计 | 137 |

按族：memory — confirmed 10 / corrected 48 / tbd_resolved 12 / tbd_open 2 / not_found 1；language — confirmed 7 / corrected 46 / tbd_resolved 9 / not_found 2。

- 修改的 YAML 文件：83（paradigms/language 39、paradigms/memory 44；含 LAN-OVS-003 的变体源）。范式类改动 53 条在 `class_updates.yaml`。
- "corrected" 绝大多数是补全：原引文只有题名（PMID 线索行）或缺卷期页/作者；真正的数值错误只有 MEM-META-002（页码 267-270 → 267-271）和 MEM-SME-001（题名漏掉 "learning"）。
- 没有 DOI/PMID 指向另一篇文献的情况（mismatch 0）。
- TBD 解决（具体范式 15 条）：LAN-GEST-001, LAN-NWL-001, LAN-PN-002, LAN-PRIME-002, LAN-SWITCH-001, LAN-VF-003, MEM-DF-002, MEM-DS-002, MEM-NAV-003, MEM-NBK-002, MEM-PA-002, MEM-PM-002, MEM-RMEM-001, MEM-RPRIM-001, MEM-RPT-001；对应的类（LAN-GEST、LAN-NWL、LAN-SWITCH、MEM-RMEM、MEM-RPRIM、MEM-RPT）同步写入 class_updates。
- TBD 仍开放：MEM-PA-001, MEM-PA（Calkins 1894 "Association" 的 Crossref 记录未检到；三次查询见 sources_check 的 note）。
- not_found：LAN-VF-001, MEM-FR-002, LAN-VF（Benton 等 MAE 测验手册、Lezak 等手册，Crossref 无记录 / 检索被拒）。

## 年份口径

Crossref/OpenAlex 的 `issued`/`publication_year` 常为在线日期。原条目已写印刷年且与卷期一致的（LAN-HIER-001 2016、LAN-LOC-002 2017）保留印刷年并在 note 说明；原条目无年份的按接口年份写（MEM-CD-002 2022，LAN-GEST-001 2003），note 说明可能为在线年份。不引入任何接口与原条目都没有的年份。

## 请维护者注意（D-062 类源头）

- MEM-DF：-002 的候选源头 Bjork, LaBerge & Legrand 1968 早于类源头 Bjork 1970（-001）。按 D-062 第 3 款，内容未核实前不替换，已在 sources_check note 记录。
- LAN-PN：-002 的候选源头 Rosinski et al. 1975（行为学）早于类源头 Crone et al. 2001。同上，未替换。
- MEM-NAV-003 候选源头 Astur, Ortiz & Sutherland 1998 与类源头 Maguire 1998 同年，未替换；Crossref 题名以冒号结尾（记录缺副标题），内容核实时补全。
- LAN-OVS-003 notes 里"两篇 Nature 2023 哪篇先发表"的问题：两篇同期同日（2023-08-23，620(7976)），已在 sources_check note 记录；notes 原句未删。
- 规则上只在 PubMed 页面看到才加 PMID；本次未能打开 PubMed，故未新增任何 PMID（OpenAlex 返回的 PMID 只记在 fetch_log）。
- 变体与具体范式的 notes 标记里 API 名按实际来源写（Crossref 或 OpenAlex），没有把 OpenAlex 记录标成 Crossref。

## 输出文件

`curation/work/pkg_D/sprint3/`：sources_check.csv、class_updates.yaml、fetch_log.md、worklog.md、pr/<ID>.md（83 个改动文件各一份）。
