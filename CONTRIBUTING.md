# Contributing

**English** | [简体中文](#参与贡献)

Contributions from researchers and developers are welcome: new paradigms, neural markers, regions and constructs, corrections, and additional evidence for existing links. Please read [docs/methodology.md](docs/methodology.md) before contributing.

## Workflow

1. Open an issue for new paradigms or markers, or for changes to vocabularies, so that scope and naming can be agreed first.
2. Fork the repository and create a branch.
3. Add or edit files:
   - Paradigm: copy `paradigms/_template.yaml` to `paradigms/<family>/<ID>.yaml`. Each file is one *concrete paradigm* (protocol) `<FAMILY>-<SHORT>-<NNN>` of a *paradigm class* `<FAMILY>-<SHORT>` registered in `paradigms/_classes.yaml` (see [Numbering](#numbering-concrete-paradigms)).
   - Marker: add `knowledge/markers/MK.<name>.yaml`. Every marker referenced by a paradigm must exist.
   - Region or construct: add a term to `knowledge/regions.yaml` or `knowledge/constructs.yaml`.
4. Validate locally:
   ```bash
   pip install -r scripts/requirements.txt
   python scripts/validate.py
   ```
5. Open a pull request. Sign off your commits (`git commit -s`) under the [Developer Certificate of Origin](https://developercertificate.org/).

## Numbering concrete paradigms

Identifiers have two levels (methodology §1, §6; decision D-057). A **paradigm class** `<FAMILY>-<SHORT>` (e.g. `MOT-MI`) carries the shared mechanism: markers, constructs, origin publication, description. A **concrete paradigm** `<FAMILY>-<SHORT>-<NNN>` (e.g. `MOT-MI-001` left/right hand, `MOT-MI-002` left hand/right hand/feet/tongue) is one reproducible task configuration. Give a new serial number when any of these changes:

1. the class/condition set (number or identity of classes, targets or conditions);
2. the stimulus or cue type, including the coding scheme (e.g. SSVEP frequency vs joint frequency–phase coding; P300 row/column vs checkerboard);
3. the trial structure (synchronous vs asynchronous; single-trial vs block);
4. the feedback mode (none / discrete / continuous; open vs closed loop).

Parameter changes alone (durations, ISI, number of trials, values within the same scheme) stay in `variants` or parameter ranges. State the criterion in `protocol.distinguishing` and in the pull request. Serial numbers are permanent and never reused; `-001` is the earliest published or canonical configuration. A new class needs an entry in `paradigms/_classes.yaml`.

## Review

New entries start as `draft`. A maintainer verifies each source against the original publication, sets `verified: true` on the source, and changes the entry to `reviewed` once all sources are verified.

## Credit

All contributors are listed in the entries they contribute to. Authorship criteria for the review paper will be published in `paper/AUTHORSHIP.md` before the paper is made public.

---

# 参与贡献

欢迎研究者和开发者参与贡献：新的范式、神经标记物、脑区与认知构念，对已有条目的修正，以及为已有关联补充证据。贡献前请阅读[方法说明](docs/methodology.zh-CN.md)。

## 流程

1. 新增范式、标记物或修改词表前，请先开 Issue，就范围和命名达成一致。
2. Fork 仓库并新建分支。
3. 新增或修改文件：
   - 范式：复制 `paradigms/_template.yaml` 到 `paradigms/<范式族>/<ID>.yaml`。每个文件是一个**具体范式**（协议）`<范式族>-<简称>-<序号>`，所属**范式类** `<范式族>-<简称>` 登记在 `paradigms/_classes.yaml`（见下文"具体范式的编号"）。
   - 标记物：新增 `knowledge/markers/MK.<名称>.yaml`。范式引用的标记物必须已存在。
   - 脑区或构念：在 `knowledge/regions.yaml` 或 `knowledge/constructs.yaml` 中添加条目。
4. 本地校验：
   ```bash
   pip install -r scripts/requirements.txt
   python scripts/validate.py
   ```
5. 提交 PR。提交时请签署（`git commit -s`），遵循 DCO。

## 具体范式的编号

标识符分两级（方法说明 §1、§6；决议 D-057）。**范式类** `<范式族>-<简称>`（如 `MOT-MI`）记录共同机制：标记物、构念、源头文献、描述。**具体范式** `<范式族>-<简称>-<序号>`（如 `MOT-MI-001` 左/右手二分类、`MOT-MI-002` 左手/右手/双脚/舌头四分类）是一个可复现的任务配置。以下任一改变即分配新序号：

1. 类别/条件集（类别、目标或条件的数量或身份）；
2. 刺激或提示类型，含编码方案（如 SSVEP 频率编码 vs 联合频率–相位编码；P300 行/列闪烁 vs 棋盘格闪烁）；
3. 试次结构（同步 vs 异步；单试次 vs 组块）；
4. 反馈方式（无 / 离散 / 连续；开环 vs 闭环）。

只改参数（时长、ISI、试次数、同一方案内的取值）的写入 `variants` 或参数范围。依据的准则写在 `protocol.distinguishing` 和 PR 中。序号永久有效、不复用；`-001` 为最早发表或公认的标准配置。新的范式类需要在 `paradigms/_classes.yaml` 中登记。

## 审核

新条目状态为 `draft`。维护者对照原始文献核实每条出处并标记 `verified: true`，全部出处核实后将条目改为 `reviewed`。

## 致谢与署名

所有贡献者都会记录在其贡献的条目中。综述论文的作者资格标准将在论文公开前于 `paper/AUTHORSHIP.md` 中公布。
