# Contributing

**English** | [简体中文](#参与贡献)

Contributions from researchers and developers are welcome: new paradigms, neural markers, regions and constructs, corrections, and additional evidence for existing links. Please read [docs/methodology.md](docs/methodology.md) before contributing.

## Workflow

1. Open an issue for new paradigms or markers, or for changes to vocabularies, so that scope and naming can be agreed first.
2. Fork the repository and create a branch.
3. Add or edit files:
   - Paradigm: copy `paradigms/_template.yaml` to `paradigms/<family>/<ID>.yaml`.
   - Marker: add `knowledge/markers/MK.<name>.yaml`. Every marker referenced by a paradigm must exist.
   - Region or construct: add a term to `knowledge/regions.yaml` or `knowledge/constructs.yaml`.
4. Validate locally:
   ```bash
   pip install -r scripts/requirements.txt
   python scripts/validate.py
   ```
5. Open a pull request. Sign off your commits (`git commit -s`) under the [Developer Certificate of Origin](https://developercertificate.org/).

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
   - 范式：复制 `paradigms/_template.yaml` 到 `paradigms/<范式族>/<ID>.yaml`。
   - 标记物：新增 `knowledge/markers/MK.<名称>.yaml`。范式引用的标记物必须已存在。
   - 脑区或构念：在 `knowledge/regions.yaml` 或 `knowledge/constructs.yaml` 中添加条目。
4. 本地校验：
   ```bash
   pip install -r scripts/requirements.txt
   python scripts/validate.py
   ```
5. 提交 PR。提交时请签署（`git commit -s`），遵循 DCO。

## 审核

新条目状态为 `draft`。维护者对照原始文献核实每条出处并标记 `verified: true`，全部出处核实后将条目改为 `reviewed`。

## 致谢与署名

所有贡献者都会记录在其贡献的条目中。综述论文的作者资格标准将在论文公开前于 `paper/AUTHORSHIP.md` 中公布。
