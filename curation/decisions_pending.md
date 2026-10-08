# 待例会判定事项

> **2026-10-02 更新**：以下全部事项已在 `decisions.md` 中起草决议 D-001 – D-030（草案，待负责人确认），并同步到 `candidates.csv` 的 `decision` / `decision_ref` 列。本文件保留为原始议题记录。

> 下列事项由初始收集提出，需在第一次例会上逐条确认。确认后，把结论写入 `decisions.md`（编号 D-xxx），并同步更新 `candidates.csv` 的 decision 列。

## 一、建议并入（7 项）

| 候选 | 建议并入 | 理由 |
|---|---|---|
| SSR-PD-001 闪光光驱动 | SSR-SSVEP-001 | 临床脑电对闪烁诱发 SSVEP 的叫法，机制相同 |
| SSR-FT-001 多目标频率标记注意 | SSR-SSVEP-001 | 标记物相同；如果图谱要区分认知研究与 BCI 控制，也可以保留为独立范式 |
| SSR-SSVEPHF-001 高频 SSVEP | SSR-SSVEP-001 | 只改变了刺激频率 |
| MOT-FING-001 单指运动解码 | MOT-ME-001 | 任务相同，只是解码粒度不同 |
| IMG-MUS-001 音乐想象 | IMG-AUD-001 | 属于听觉想象的子类 |
| IMG-FACE-001 面孔与场景想象 | IMG-VIS-001 | 属于类别特异性的视觉想象 |
| IMG-NAV-001 空间导航想象 | IMG-CMD-001 | 主要作为 Owen 指令跟随范式的第二个任务使用 |

## 二、建议排除（2 项）

| 候选 | 理由 |
|---|---|
| STM-ICMS-001 皮层内微刺激感觉反馈 | 主要读出是被试的知觉报告，而不是脑记录信号，可能不满足纳入标准 3 |
| STM-ECS-001 皮层电刺激功能定位 | 读出的是行为（言语中断、运动），而不是神经记录 |

## 三、是否独立成条（需讨论）

| 候选 | 问题 |
|---|---|
| PER-RSVP-001 RSVP | 标记物与 Oddball 相同（P3b），但时间结构不同 |
| PER-TACT-001 触觉空间注意 | 与 Oddball 及 SSSEP 的关系 |
| SSR-SSMVEP-001 稳态运动 VEP | 刺激由闪烁换成了运动，是否构成独立范式 |
| MOT-GAIT-001 下肢运动想象 | 是否作为运动想象的变体 |
| ERR-AWARE-001 错误觉知 | 是否作为 Flanker 或反向眼跳范式的附加测量 |
| LAN-LDT-001 / LAN-PRIME-001 | 词汇判断与语义启动是否合并 |
| LAN-PHON-001 音位辨别 | 是否作为 MMN 的语言变体 |
| EMO-MUS-001 / EMO-FILM-001 | 两种情绪诱发是否合并 |
| EMO-EST-001 情绪 Stroop | 是否作为 Stroop 的变体 |
| STA-SCP-001 / STA-NF-001 | 慢皮层电位自我调节是否作为神经反馈的子类 |
| SOC-HYP-001 / SOC-JA-001 | 超扫描与联合动作是否合并 |

## 四、分类体系问题

| 事项 | 问题 |
|---|---|
| STA-HYB-001 混合 BCI | 现有 12 个族中没有对应的族：新增 `hybrid` 族，还是改为跨族标签？ |
| IMG-MA-001 心算 | 归入 imagery 还是 control（判例 D-001 草案） |
| 7 个以行为测量为主的任务（PER-UFOV、CTL-DSST、CTL-RAVEN、CTL-TMT、MEM-OSPAN、LAN-SPR 等） | 是否有成熟的神经标记物；没有则按纳入标准 3 排除 |
