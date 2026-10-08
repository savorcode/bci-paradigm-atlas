# 工作日志 · 包 D 记忆与语言 · sprint 2

> 每次工作追加一节（最新在下）。写：写了哪些 `protocol`、拆出了哪些具体范式（对应 `split_log.csv` 行）、保留了哪些变体及理由、`class_updates.yaml` 的改动、遇到的问题、待例会事项、跨包交接。

<!-- 模板
## YYYY-MM-DD · <策展人>
- protocol：
- 拆分 / 保留：
- class_updates：
- 核对线索：
- 问题 / 待例会：
- 交接给其他包：
-->

## 2026-10-03 · curator_d（sprint 2：D-057 拆分）

- protocol：本包 53 个范式类的 `-001` 全部写了 `protocol`（n_classes、classes、cue、必要时 stimulus_coding、paradigm_timing、feedback、distinguishing）。混合了多个配置的 `-001` 收窄到标准配置并改写描述/条件：MEM-CD、MEM-CIT、MEM-DF、MEM-DMS、MEM-DS、MEM-FR、MEM-META、MEM-NAV、MEM-NBK、MEM-ON、MEM-PA、MEM-PM、MEM-SWM、MEM-TMR、LAN-AGL、LAN-CPS、LAN-LDT、LAN-LOC、LAN-N400、LAN-OVS、LAN-P600、LAN-PHA、LAN-PN、LAN-SIS、LAN-SL、LAN-SWITCH、LAN-VF。被移到兄弟协议的别名从 `-001` 删去。
- 拆分 / 保留：具体范式 53 → 83（新建 30 个文件，见 `split_log.csv`）。
  - 9 个待复核变体全部判为配置级并拆出：MEM-CD-002（延迟估计，准则 1）、MEM-FR-002（RAVLT，1;3）、MEM-META-002（JOL，1;3）、MEM-NAV-002（虚拟放射臂迷宫，1;2;4）、MEM-ON-002（记得/知道，1）、LAN-P600-002（花园路径句，1）、LAN-PN-002（图词干扰，2;1）、LAN-SC-002（手语，2）、LAN-VF-002（BCI 默想生词，1;3——维护者初判 3;4，但 Shin 等数据集为开环，不主张准则 4）。作废 ID（MEM-DE-001、MEM-RK-001、LAN-SIGN-001、IMG-WORD-001）未复活。
  - 从 `-001` 描述中拆出的配置：MEM-CD-003（偏侧化 CDA）、MEM-DF-002（list method）、MEM-NAV-003（虚拟水迷宫）、MEM-PA-002（视空间配对联想）、LAN-CPS-002（阅读逗号）、LAN-SIS-002（改变听觉反馈）。
  - 新发现的配置：MEM-CIT-002（CTP）、MEM-DS-002（倒背）、MEM-MST-002（偶然编码重复抑制）、MEM-NBK-002/003/004（含 0-back 的多负荷组块、双通道、自适应训练）、MEM-PM-002（时间型）、MEM-TMR-002（气味情境再激活）、LAN-LOC-002（听觉定位）、LAN-N400-002（完形概率分级）、LAN-OVS-002/003（小词表单词、大词表句子）、LAN-PRIME-002（掩蔽启动）、LAN-SWITCH-002（接受性切换）、LAN-VF-003（fNIRS 组块设计）。
  - P1 核心类：MEM-NBK 4 个、LAN-OVS 3 个具体范式。
  - 保留为变体：LAN-OVS-003 的合成语音/虚拟形象输出；MEM-NAV-002 的 4-on-8 版本（写在 notes）。
  - 提议未给号（无线索或仅 1 项研究）12 条；LAN-SIS 的音高扰动（D-042）待例会，若并入给 LAN-SIS-003。
- class_updates：24 条。23 条只补别名并集；MEM-TMR 改描述（两种线索）、加 MK.BOLD_hippocampus、并提议把类源头改为 2007 年气味研究（DN52，早于 -001 的 Rudoy 2009）。
- 核对线索：
  - R0979（fNIRS 言语流畅性综述）原是 LAN-VF BCI 变体的 source，但内容是临床 fNIRS，改配到 LAN-VF-003；LAN-VF-002 的 first_source 改用 Shin et al. 2018（DN50）。
  - R1000（图词干扰）是 2024 年综述，不能作源头（D-031 §1），LAN-PN-002 记 TBD。
  - Shin et al. 2018 的 PMC 页返回 reCAPTCHA，数据集中 n-back 的负荷水平未核对，未写入。
  - DN52 页面未显示作者；DN53 只有“Scott et al., 2017”，LAN-LOC-002 first_source 中的姓名首字母需核对。
- 问题 / 待例会：
  1. **-001 的标记物与行为学源头**：按 D-057 第 5 款 -001 取最早发表的配置，但若干最早配置是行为学测验（MEM-CD-001 全视野变化检测、MEM-FR-002 RAVLT、MEM-NBK-004 训练、LAN-VF-001 测验），其神经标记物只在后来的配置中测得；`markers` 必填，暂沿用类标记物并在 notes 说明。建议例会决定：具体范式的 `markers` 是否允许写“继承类标记物”，或改为可选。
  2. **-001 不是最早**：MEM-TMR-002（2007）早于 MEM-TMR-001（2009）；序号不变，类源头改动写在 class_updates。MEM-MST-001 中连续再认与学习—测试两种呈现暂合在一起，待核对 R0373 与 R0565 后可能再拆。
  3. **类标记物无人使用**：MEM-SWM 的 MK.CDA 在 MEM-SWM-001 收窄为 Corsi 后无具体范式使用（依赖尚未建文件的偏侧化空间延迟反应配置）。
  4. 刺激模态（视觉 vs 听觉）的改变是否算准则 2：本包对 LAN-CPS、LAN-LOC、LAN-SC 按准则 2 给号（刺激类型本质不同）；LAN-LDT、LAN-N400、LAN-AGL 的听觉版本因无线索只记为提议。请例会给出统一口径。
- 交接给其他包：
  - 包 C：ERR-AAF-001 与 LAN-SIS 的 D-042 若判并入，本包给 LAN-SIS-003。
  - 包 E / 维护者：MEM-NBK-002 为被动式 BCI 心理负荷标准协议，STA 族如有负荷监测范式可引用。
