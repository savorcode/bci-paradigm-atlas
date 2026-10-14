# 冲刺 5：知识层第二轮

分支 `knowledge/layer-2`（基于 main `3538e8d`）。规则、证据等级和出处要求与冲刺 4 相同，见 `curation/work/sprint4/README.md`。

## 本轮内容

1. **词表**：按 D-076 新增构念 9 个、脑区 2 个；`BR.temporoparietal_junction` 标为 deprecated，改用 `BR.TPJ`。冲刺 4 中暂挂在相近 ID 下的关联，改挂到新 ID。
2. **标记物第二批**：30 个，按具体范式中的使用次数挑选。
3. **过程记录整理**：统一检索记录中的术语。

## 可用 ID

冲刺 4 README 中的 81 个构念、43 个脑区，加上：

| ID | 中文 | 上位 |
|---|---|---|
| `CN.perceptual_learning` | 知觉学习 | CN.perception |
| `CN.perceptual_discrimination` | 知觉辨别 | CN.perception |
| `CN.auditory_selective_attention` | 听觉选择性注意 | CN.attention |
| `CN.emotion_regulation` | 情绪调节 | CN.affect |
| `CN.approach_motivation` | 趋近-回避动机 | CN.affect |
| `CN.reward_anticipation` | 奖赏预期 | CN.affect |
| `CN.empathy` | 共情 | CN.social |
| `CN.social_decision` | 社会决策 | CN.social |
| `CN.voice_perception` | 嗓音知觉 | CN.social_perception |
| `BR.OFA` | 枕叶面孔区 | BR.visual_cortex |
| `BR.SEF` | 辅助眼区 | BR.frontal_cortex |

不再使用：`BR.temporoparietal_junction`（用 `BR.TPJ`）。

## 第二批标记物（30）

| 组 | 标记物 |
|---|---|
| F 感知与注意 | MK.cVEP、MK.alpha_lateralization、MK.VAN、MK.SEP_N20、MK.N2pc、MK.P2_visual、MK.N2_posterior、MK.FFR、MK.ASSR、MK.mVEP |
| G 记忆、控制与状态 | MK.theta_drowsiness、MK.parietal_old_new、MK.hippocampal_theta、MK.NoGo_P3、MK.FN400、MK.Dm、MK.switch_positivity、MK.N450、MK.CPP、MK.presaccadic_potential |
| H 情绪、语言与社会 | MK.EPN、MK.BOLD_pSTS、MK.speech_envelope_tracking、MK.linguistic_structure_tracking、MK.ERAN、MK.CPS、MK.interbrain_synchrony、MK.ISC、MK.HEP、MK.omission_response |

过程文件：`markers_F/`、`markers_G/`、`markers_H/`、`vocab/`。
