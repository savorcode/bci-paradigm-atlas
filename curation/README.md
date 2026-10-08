# curation/：收录工作目录

| 文件 | 内容 | 谁用 |
|---|---|---|
| `candidates.csv` | 294 个候选范式总表（C001–C209 为 S-001，C210–C294 为 sprint 1 策展人新增）：所属包、族、ID、中英文名、别名、可能的标记物、模态、优先级、判定、文献数、数据集线索、待办。`status` 取值：待认领 / 第一遍完成 / 阻塞 / 并入 / 排除 / 暂缓（D-033） | 所有人；维护者每周更新 status |
| `literature.csv` | 1,244 条文献线索（作者、年份、标题、期刊、DOI、PMID、链接、来源渠道），全部 `verified=false`；R1095 起为 sprint 1 策展人检索所得（`found_via=curator_search`）；`qa_flag` 列标记有问题的线索（D-055） | 策展人、审核人 |
| `paradigm_literature.csv` | 范式与文献的对应关系，以及文献在该范式下的角色（源头候选、综述、方法等） | 脚本与统计 |
| `packages/pkg_*.md` | 5 个工作包的任务单：每个范式的标记物、判定、文献线索、HED 页、数据集、待办 | 对应包的策展人 |
| `zotero/pkg_*.ris` | 每个包的文献，可直接导入 Zotero。标签含范式 ID、族、角色 | 策展人导入群组库 |
| `search_protocol.md` | 检索记录（PRISMA-ScR） | 维护者、论文方法部分 |
| `decisions_pending.md` | 待例会判定的事项：并入、排除、独立性、分类体系 | 第一次例会 |
| `decisions.md` | 例会决议 D-xxx（问题 / 决定 / 理由 / 影响）；`candidates.csv` 的 `decision_ref` 指向这里 | 所有人 |
| `registry/markers.csv` | 规范神经标记物登记表：ID、类型、模态、负责编写的包（owner_pkg）、使用范式 | 所有人；仅维护者修改 |
| `registry/paradigm_markers.csv` | 每个收录范式必须使用的标记物 ID | 策展人 |
| `work/pkg_*/` | 各包工作目录：写入范围说明、工作日志、检索记录、进度、新候选、标记物申请、PR 草稿 | 对应包的策展人 |
| `work/maintainer/` | 维护者工作日志 | 维护者 |

**优先级**
- P1 核心：BCI 直接使用的范式
- P2 标准：有成熟神经标记物的范式
- P3 长尾：以行为测量为主或使用较少的范式

**导入 Zotero**：文件 → 导入 → 选择 `pkg_X.ris` → 导入到群组库中对应包的文件夹。之后可以按标签（如 `PER-ODD-001`）筛选出某个范式的全部文献。
