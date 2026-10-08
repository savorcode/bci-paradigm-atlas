<!-- PR 描述草稿 · EMO-FILM-001 · curator_e · 2026-10-03 -->

Closes #

## 内容 / Summary

- 范式 / Paradigm：`EMO-FILM-001` 自然刺激情绪诱发（影片、音乐、音乐视频） / Naturalistic emotion elicitation (film, music, music video)
- 工作包 / Package：E
- 类型 / Kind：第一遍骨架
- 新增或修改的标记物 / Markers touched：`MK.affective_band_power`, `MK.frontal_alpha_asymmetry`
- 写入的变体（含被并入候选，D-030）/ Variants added：Music and music-video emotion elicitation (e.g. DEAP, AMIGOS datasets)

## 出处核对表 / Source verification table

| 字段 / Field | 文献（线索编号或 DOI）/ Source | 页码 / Page | 原文 / Verbatim quote |
|---|---|---|---|
| first_source | R0918: Emotion elicitation using films. Cognition and Emotion. (doi:10.1080/02699939508408966) | 待核对原文 | 待核对原文 |
| description (en/zh) | 策展人依据线索标题与摘要撰写，待对照原文 / written from leads: R0853, R0862, R0909, R0918, R1036, R1069, R1079 | 待核对原文 | 待核对原文 |
| markers: MK.frontal_alpha_asymmetry | curation/registry/paradigm_markers.csv | 待核对原文 | 待核对原文 |
| markers: MK.affective_band_power | curation/registry/paradigm_markers.csv | 待核对原文 | 待核对原文 |
| variants[0] Music and music-video emotion elicitation (e.g. DEAP, AMIGOS datasets) | R0862: Brain correlates of music-evoked emotions. (PMID 24552785) | 待核对原文 | 待核对原文 |
| datasets[0] | SEED (SJTU Emotion EEG Dataset) family incl. SEED-IV/SEED-VII (candidates.csv datasets 列 / dataset lead, name only) | 待核对原文 | 待核对原文 |
| datasets[1] | DEAP: a database for emotion analysis using physiological signals (candidates.csv datasets 列 / dataset lead, name only) | 待核对原文 | 待核对原文 |
| datasets[2] | AMIGOS: A Dataset for Affect, Personality and Mood Research on Individuals and Groups (candidates.csv datasets 列 / dataset lead, name only) | 待核对原文 | 待核对原文 |
| interop.bids_task | `emotionfilm` 策展人拟定 / curator-chosen label | 待核对原文 | 待核对原文 |

## 线索核对 / Lead check

- 使用的线索 / Leads used：R0853, R0862, R0909, R0918, R1036, R1069, R1079
- 线索有误之处 / Errors found in leads：第一遍未发现（未对照原文）

## 自查 / Checklist

- [x] 本地 `python scripts/validate.py` 0 problem(s)
- [x] 只修改了本包写入范围内的文件（`paradigms/<本包族>/`、owner 为本包的 `knowledge/markers/`、`curation/work/pkg_E/`；D-029）
- [x] `markers` 只使用 `curation/registry/paradigm_markers.csv` 中的 ID，或已在 `marker_requests.csv` 中申请
- [x] 所有出处 `verified: false`（由审核人核实后改为 true）
- [x] 查不到的字段已删除或留空，没有根据记忆或推测填写任何文献、DOI、数字
- [ ] 没有转引：每条出处都对照原文核对过（第一遍未对照原文，页码与原文待核对）
- [ ] 混合 BCI / 超扫描变体使用 `Hybrid:` / `Hyperscanning:` 前缀（D-022、D-021）（不适用）
- [x] 已更新本包 `status.csv`、`worklog.md`
- [ ] 提交已签署（`git commit -s`，DCO）

## 审核人 / Reviewer

- 交叉审核包 / Cross-review package：D 审 E
- [ ] 审核人已对照原文核实源头文献与描述
