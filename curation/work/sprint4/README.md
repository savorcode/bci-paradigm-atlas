# 冲刺 4：知识层（构念、脑区、标记物关联）

分支 `knowledge/layer-1`（基于 main `05462c2`）。提交作者 savorcode01。

## 规则

1. **构念 ID 与范式工厂一致**：工厂内置构念 + 桥接表 `constructs_extra` + 图谱原有 6 个，共 81 个（11 个领域根节点）。新增构念须先在 `vocab_requests.csv` 申请。
2. **脑区 ID**：工厂内置 23 个 + 图谱原有 5 个 + 新增 15 个，共 43 个。`atlas_refs` 写 Brodmann、AAL3、HCP-MMP1.0 对应标签，`coordinate_space: MNI152`。
3. **标记物关联**：`generators`（来源脑区）与 `indexes`（反映的构念），每条至少 1 篇出处，DOI 必须经 Crossref 取回记录核对；`verified: false`（尚未对照全文）。
4. **证据等级**（方法说明 §5）：A = 元分析 / 系统综述，或跨实验室跨模态重复；B = 多项独立研究；C = 单项研究或间接证据；D = 理论推测。叙述性综述单独不构成 A。
5. **来源脑区的方法**写在 `note`：`method: intracranial | lesion | EEG-fMRI | MEG/EEG source | fMRI localization | scalp topography`，颅内记录与病灶证据最强，仅头皮地形最弱（最高 C）。

## 构念 ID（81）

| ID | 中文 | 上位 |
|---|---|---|
| `CN.perception` | 感知 | （根） |
| `CN.attention` | 注意 | （根） |
| `CN.memory` | 记忆 | （根） |
| `CN.language` | 语言 | （根） |
| `CN.cognitive_control` | 认知控制 | （根） |
| `CN.motor` | 运动 | （根） |
| `CN.affect` | 价值与情绪 | （根） |
| `CN.mental_imagery` | 心理意象 | （根） |
| `CN.hmi` | 人机交互认知 | （根） |
| `CN.brain_state` | 脑状态 | （根） |
| `CN.early_visual` | 早期视觉加工 | CN.perception |
| `CN.object_recognition` | 物体识别 | CN.perception |
| `CN.face_perception` | 面孔知觉 | CN.object_recognition |
| `CN.auditory_change` | 听觉变化检测 | CN.perception |
| `CN.neural_entrainment` | 神经节律跟随 | CN.perception |
| `CN.spatial_attention` | 空间选择性注意 | CN.attention |
| `CN.target_selection` | 目标选择 | CN.attention |
| `CN.orienting` | 注意定向（非自主） | CN.attention |
| `CN.sustained_attention` | 持续注意 | CN.attention |
| `CN.context_updating` | 情境更新 | CN.memory |
| `CN.working_memory` | 工作记忆 | CN.memory |
| `CN.semantic_integration` | 语义整合 | CN.language |
| `CN.syntactic_processing` | 句法加工 | CN.language |
| `CN.inner_speech` | 内部言语 | CN.language |
| `CN.conflict_monitoring` | 冲突监测 | CN.cognitive_control |
| `CN.error_monitoring` | 错误监测 | CN.cognitive_control |
| `CN.response_inhibition` | 反应抑制 | CN.cognitive_control |
| `CN.anticipation` | 预期与准备 | CN.cognitive_control |
| `CN.motor_preparation` | 运动准备 | CN.motor |
| `CN.motor_imagery` | 运动想象 | CN.motor |
| `CN.reward_prediction_error` | 奖赏预测误差 | CN.affect |
| `CN.emotional_salience` | 情绪显著性 | CN.affect |
| `CN.visual_imagery` | 视觉意象 | CN.mental_imagery |
| `CN.language_to_imagery` | 语言驱动的意象生成 | CN.visual_imagery |
| `CN.machine_error_perception` | 机器错误感知 | CN.hmi |
| `CN.intent_selection` | 意图选择 | CN.hmi |
| `CN.cortical_idling` | 皮层静息节律 | CN.brain_state |
| `CN.early_auditory` | 早期听觉加工 | CN.perception |
| `CN.somatosensation` | 体感与痛觉 | CN.perception |
| `CN.chemosensation` | 嗅觉与味觉 | CN.perception |
| `CN.sensory_gating` | 感觉门控 | CN.perception |
| `CN.interoception` | 内感受 | CN.perception |
| `CN.multisensory_integration` | 多感觉整合 | CN.perception |
| `CN.perceptual_awareness` | 知觉觉知 | CN.perception |
| `CN.perceptual_organization` | 知觉组织 | CN.perception |
| `CN.prediction_violation` | 感觉预测与预测误差 | CN.perception |
| `CN.attention_allocation` | 注意资源分配 | CN.attention |
| `CN.distractor_suppression` | 干扰抑制 | CN.attention |
| `CN.episodic_encoding` | 情景记忆编码 | CN.memory |
| `CN.recognition_memory` | 再认记忆（熟悉感与回想） | CN.memory |
| `CN.prospective_memory` | 前瞻记忆 | CN.memory |
| `CN.spatial_navigation` | 空间导航与关系记忆 | CN.memory |
| `CN.memory_consolidation` | 记忆巩固（睡眠） | CN.memory |
| `CN.speech_tracking` | 言语与语言结构跟踪 | CN.language |
| `CN.phonological_processing` | 语音加工 | CN.language |
| `CN.prosody` | 韵律加工 | CN.language |
| `CN.speech_production` | 言语产生 | CN.language |
| `CN.task_switching` | 任务切换 | CN.cognitive_control |
| `CN.evidence_accumulation` | 证据累积（知觉决策） | CN.cognitive_control |
| `CN.metacognition` | 元认知与决策信心 | CN.cognitive_control |
| `CN.motor_execution` | 运动执行 | CN.motor |
| `CN.movement_kinematics` | 运动学与连续运动控制 | CN.motor |
| `CN.sensorimotor_integration` | 感觉运动整合 | CN.motor |
| `CN.value_decision` | 价值与风险决策 | CN.affect |
| `CN.threat_fear` | 威胁与恐惧 | CN.affect |
| `CN.emotional_state` | 情绪状态与效价 | CN.affect |
| `CN.auditory_imagery` | 听觉意象 | CN.mental_imagery |
| `CN.mental_arithmetic` | 心算与心理操作 | CN.mental_imagery |
| `CN.social` | 社会认知 | （根） |
| `CN.mentalizing` | 心智化（心理理论） | CN.social |
| `CN.self_processing` | 自我相关加工 | CN.social |
| `CN.social_interaction` | 人际协调与互动 | CN.social |
| `CN.social_perception` | 社会知觉（目光、生物运动） | CN.social |
| `CN.vigilance` | 警觉度与困倦 | CN.brain_state |
| `CN.sleep` | 睡眠 | CN.brain_state |
| `CN.consciousness_level` | 意识水平 | CN.brain_state |
| `CN.spontaneous_thought` | 自发思维与默认网络 | CN.brain_state |
| `CN.cortical_excitability` | 皮层兴奋性与刺激响应 | CN.brain_state |
| `CN.self_regulation` | 脑活动自我调节（神经反馈） | CN.brain_state |
| `CN.novelty_orienting` | 新异性定向 | （根） |
| `CN.sustained_visual_attention` | 持续视觉注意 | （根） |

## 脑区 ID（43）

| ID | English | 中文 |
|---|---|---|
| `BR.V1` | primary visual cortex (V1) | 初级视皮层 |
| `BR.extrastriate` | extrastriate visual cortex (V2–V4) | 纹外视皮层 |
| `BR.LOC` | lateral occipital complex | 外侧枕叶复合体 |
| `BR.FFA` | fusiform face area | 梭状回面孔区 |
| `BR.pSTS` | posterior superior temporal sulcus | 颞上沟后部 |
| `BR.A1` | primary auditory cortex / Heschl gyrus | 初级听皮层 |
| `BR.STG` | superior temporal gyrus | 颞上回 |
| `BR.MTG` | left posterior middle temporal gyrus | 左侧颞中回后部 |
| `BR.ATL` | anterior temporal lobe | 前颞叶 |
| `BR.IFG` | inferior frontal gyrus | 额下回 |
| `BR.IPS` | intraparietal sulcus | 顶内沟 |
| `BR.TPJ` | temporo-parietal junction | 颞顶联合区 |
| `BR.dACC` | dorsal anterior cingulate cortex | 背侧前扣带回 |
| `BR.preSMA` | pre-supplementary motor area | 前辅助运动区 |
| `BR.SMA` | supplementary motor area | 辅助运动区 |
| `BR.M1` | primary motor cortex | 初级运动皮层 |
| `BR.S1` | primary somatosensory cortex | 初级体感皮层 |
| `BR.DLPFC` | dorsolateral prefrontal cortex | 背外侧前额叶 |
| `BR.vmPFC` | ventromedial prefrontal / orbitofrontal cortex | 腹内侧前额叶 / 眶额皮层 |
| `BR.striatum` | ventral striatum | 腹侧纹状体 |
| `BR.amygdala` | amygdala | 杏仁核 |
| `BR.thalamus` | thalamus | 丘脑 |
| `BR.hippocampus` | hippocampus | 海马 |
| `BR.frontal_cortex` | Frontal cortex | 额叶皮层 |
| `BR.parietal_cortex` | Parietal cortex | 顶叶皮层 |
| `BR.temporoparietal_junction` | Temporoparietal junction (atlas id; same as factory BR.TPJ) | 颞顶联合区 |
| `BR.sensorimotor_cortex` | Sensorimotor cortex | 感觉运动皮层 |
| `BR.visual_cortex` | Visual cortex | 视觉皮层 |
| `BR.premotor` | Premotor cortex (PMd/PMv) | 运动前区 |
| `BR.FEF` | Frontal eye field | 额眼区 |
| `BR.precuneus` | Precuneus | 楔前叶 |
| `BR.PCC` | Posterior cingulate cortex | 后扣带回 |
| `BR.dmPFC` | Dorsomedial prefrontal cortex | 背内侧前额叶 |
| `BR.frontopolar` | Frontopolar cortex (BA10) | 额极 |
| `BR.anterior_insula` | Anterior insula | 前脑岛 |
| `BR.posterior_insula` | Posterior insula | 后脑岛 |
| `BR.parahippocampal` | Parahippocampal cortex / PPA | 海马旁回 |
| `BR.cerebellum` | Cerebellum | 小脑 |
| `BR.STN` | Subthalamic nucleus | 丘脑底核 |
| `BR.dorsal_striatum` | Dorsal striatum (caudate, putamen) | 背侧纹状体 |
| `BR.MT` | Middle temporal area (hMT+/V5) | 颞中区运动视觉区 |
| `BR.SII` | Secondary somatosensory cortex | 次级体感皮层 |
| `BR.OFC_lateral` | Lateral orbitofrontal cortex | 外侧眶额皮层 |
