# 工作日志 · 包 C 错误监测与认知控制

> 每次工作追加一节（最新在下）。写：做了什么、核对了哪些线索（R 编号）、遇到的问题、需要例会讨论或需要其他包处理的事项（含 D-030 跨包交接的线索）。

<!-- 模板
## YYYY-MM-DD · <策展人>
- 完成：
- 核对线索：
- 问题 / 待例会：
- 交接给其他包：
-->

## 2026-10-03 · curator_c（第一遍骨架 + 扩充候选）

### 完成
- 读：methodology、CONTRIBUTING、schema（paradigm/common/marker）、taxonomy、_template、种子条目、decisions.md（D-001–D-030）、本目录 README、任务单、candidates.csv（C 包 37 行）、markers.csv / paradigm_markers.csv、literature.csv / paradigm_literature.csv。
- 范式骨架：35 个收录候选 + 17 个新增候选 = 52 个文件（`paradigms/error/` 19 个，`paradigms/control/` 33 个）。CTL-DSST-001、CTL-TMT-001 按 D-023 暂缓，不建文件。本包无"并入"候选，故无 D-030 变体；按 D-015 在 ERR-AWARE-001 中写入 1 个变体（反向眼跳错误觉知，R0205）。
- 标记物：覆盖本包 17 个骨架文件（name/aliases/type/modality 沿用登记表，新写 description；12 个 ERP/节律标记物写了教科书级 signature，均在 notes 中注明待核对；5 个 BOLD 标记物不写 signature）。未新建标记物文件，`marker_requests.csv` 无新增。
- 新增候选 17 个（见 `new_candidates.csv`）：ERR-CHGPT、ERR-PRT、ERR-OGNG、ERR-APC、ERR-VRPE、ERR-AAF、CTL-MSIT、CTL-MRP、CTL-CONF、CTL-MIXG、CTL-FORAGE、CTL-VBC、CTL-RNG、CTL-ANAL、CTL-AUT、CTL-AMBIG、CTL-SYLL（均 `-001`）。已对照全部 5 个包的名称与别名查重。每个都至少有 1 条本次 WebSearch/WebFetch 实际看到的线索；全部按"收录"处理，待例会确认。
- 检索：WebSearch 25 次（配额 30），WebFetch 30 次（见 `search_log.md`）。

### 决定与约定
- first_source：取线索中最能代表最早提出该范式的文献；citation 按 "Authors. Title. Venue. Year." 由 literature.csv 字段拼接，只填线索中已有的 doi/pmid/year；全部 `verified: false`。literature.csv 中 "X et al." 原样保留。
- 线索中没有可信源头、用检索补的（first_source_ref = search）：ERR-INST-001（O'Doherty et al. 2004）、CTL-DD-001（Rachlin et al. 1991）、CTL-DT-001（Telford 1931，转引自 Millisecond 任务页的参考文献表）、CTL-WCST-001（Grant & Berg 1948）、CTL-RAVEN-001（Penrose & Raven 1936，转引自 Wikipedia）。**请维护者把这 5 条以及新增候选的线索补进 literature.csv 并分配 R 编号**；条目 notes 中以 `S_*` 键 + URL 标识。
- ERR-AWARE-001 的 first_source 选 R0195（Scheffers & Coles 2000）而非任务单标为源头候选的 R0094（Gehring 1990，是 ERN 的源头而非觉知范式）。
- ERR-ERRP-001 选 R0403（2008）；R1085（"You are wrong!"）可能更早但线索无作者/年份。
- trial_structure 一律未填（第一遍未读原文，避免凭记忆填数字）。
- bci_category：ERR-ERRP、ERR-OBS、ERR-VRPE 为 passive，其余为 none（不对 BCI 用途作推测）。
- CTL-STR-001 别名中删去 "Emotional Stroop (variant)"（D-019）。
- status.csv 的 status 按本次指令用"第一遍完成 / 阻塞"，与 README 中的取值表（待认领 / 编写中 / ……）不一致，请维护者确认以哪一套为准。

### 阻塞
- ERR-AAF-001：first_source 为 TBD（唯一线索是 2016 年研究；为 Burnett et al. 1998 做的检索没有找到原文）。
- CTL-RNG-001：线索是 PET/TMS，而 MK.BOLD_dlPFC 在登记表中只登记了 fMRI；需决定 PET rCBF 是否归入该标记物（D-028 第 5 条只提到 fNIRS）。
- ERR-CAUS-001、CTL-WASON-001：线索中没有任何神经记录研究支持登记表给的 MK.BOLD_dlPFC，第二遍要按 D-023 口径核查，否则提请暂缓。

### 待例会
1. ERR-VRPE-001 的"预测误差负波（PEN）"暂映射到 MK.ErrP；是否单独登记 MK.PEN？
2. CTL-AUT-001 与 CTL-RAT-001 用 MK.alpha_posterior，但创造力研究报告的 α 升高也在额区；是否需要单独的"任务相关 α 同步"标记物？
3. CTL-AMBIG-001 用到 MK.BOLD_amygdala（E 包），眶额效应没有对应标记物；CTL-MRP-001 用 MK.LRP（B 包）；ERR-AAF-001 用 MK.N1_auditory / MK.P2_auditory（A 包）。只是引用，不修改。
4. 族归属有疑问：ERR-AAF-001（也可归 language，LAN-OVS-001 附近）；CTL-DD/MIXG/FORAGE/VBC/AMBIG 等价值决策类目前都放在 control，与任务单对 CTL-DD-001 的备注一致，建议在下一版词表讨论中讨论是否设 decision 族。
5. 可能的重叠：CTL-CONF-001 与 ERR-AWARE-001（均 MK.Pe）；ERR-OGNG-001 与 CTL-GNG-001；ERR-TE-001 与 ERR-GAM-001、CTL-SART-001 与 CTL-GNG-001（维护者已列入候议）。

### 交接给其他包
- 无跨包并入。新增候选引用了 A（MK.N1_auditory、MK.P2_auditory）、B（MK.LRP）、E（MK.BOLD_amygdala）的标记物，供其 owner 在 used_by 中知悉。
