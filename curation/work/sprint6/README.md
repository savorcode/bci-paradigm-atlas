# 冲刺 6：知识层第三批标记物 + 新增范式

分支 `knowledge/layer-4`（基于 main `729fb8d`）。规则、证据等级和出处要求同冲刺 4（`curation/work/sprint4/README.md`）。

## 可用 ID

构念与脑区以 `knowledge/constructs.yaml`、`knowledge/regions.yaml` 为准（92 个构念、47 个脑区，其中 `BR.temporoparietal_junction` 已弃用，用 `BR.TPJ`）。需要新词时写入各自的 `vocab_requests.csv`，先挂最近的已有 ID。

## 第三批标记物（24）

| 组 | 标记物 |
|---|---|
| I | MK.BOLD_stimulated_region、MK.AV_interaction_ERP、MK.BOLD_parahippocampal、MK.BOLD_premotor_parietal、MK.SCP、MK.SSSEP、MK.TEP、MK.oscillatory_entrainment |
| J | MK.tES_power_aftereffect、MK.ABR、MK.BOLD_left_IFG、MK.BOLD_olfactory_cortex、MK.BOLD_posterior_insula、MK.BOLD_vestibular_cortex、MK.CCEP、MK.DBS_cortical_EP |
| K | MK.ERNA、MK.FPAS_oddball、MK.FPVS_oddball、MK.FRP、MK.GEP、MK.LEP、MK.MLR、MK.N140_somatosensory |

## 新增范式类（24 个类，每类先建 -001）

按 D-057 两级 ID。先查重：与已有范式类或具体范式（含别名）重复的不新建，改记为已有类的具体范式或 variant，并在 worklog 说明。

| 组 | 范式类（暂定 ID） |
|---|---|
| P1 写入、刺激与运动 | STM-ICMS 皮层内微刺激人工触觉、STM-PHOS 视觉皮层刺激光幻视（视觉假体）、STM-SCS 脑–脊髓接口硬膜外刺激行走、STM-RTMS 重复 TMS / theta 爆发刺激、STM-TRNS 经颅随机噪声刺激、STM-ESM 皮层电刺激功能定位、MOT-FES 脑机接口驱动功能性电刺激康复、MOT-HYB 混合脑机接口 |
| P2 感知、注意与记忆 | PER-TIME 时间顺序与同时性判断、PER-CROWD 视觉拥挤效应、PER-AUDLOC 声源定位、MEM-PR 部分报告（图像记忆）、MEM-AI 联想推理、MEM-OSPAN 复杂广度（运算广度）、CTL-TMT 连线测验、CTL-NUM 数量比较与 SNARC |
| P3 情绪、社会、语言与状态 | EMO-STARTLE 情绪调制惊跳反射、EMO-AAT 趋近–回避任务、SOC-CONV 对话轮替（超扫描）、SOC-PGG 公共物品博弈、LAN-RA 朗读与词命名、LAN-SIGN 手语理解、STA-FAT 心理疲劳（任务时长效应）、STA-SD 睡眠剥夺 |

过程文件：`markers_I/`、`markers_J/`、`markers_K/`、`paradigms_P1/`、`paradigms_P2/`、`paradigms_P3/`。
