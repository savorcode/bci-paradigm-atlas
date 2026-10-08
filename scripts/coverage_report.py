# Copyright 2026 思维刻度 SavorCode
# SPDX-License-Identifier: Apache-2.0
"""Write a Markdown coverage report of the atlas (counts, TBD sources, marker sharing, zero-coverage gaps, classes).

    python scripts/coverage_report.py                       # print to stdout
    python scripts/coverage_report.py --version 0.1.0 --out curation/reports/coverage_v0.1.0.md

Reads paradigms and markers through scripts/atlas.py and the term lists in taxonomy/. Concrete paradigms with
`status: deprecated` are counted once in section 1 and excluded from all other statistics. The work package of a
paradigm is taken from curation/candidates.csv (column `pkg`) when that file exists; otherwise it is shown as "-".
Section 7 compares paradigm classes (paradigms/_classes.yaml) with concrete paradigms (D-057); the package of a
class is the package of its concrete paradigms.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import date

from atlas import ROOT, load, terms


def is_tbd(source: dict) -> bool:
    return str(source.get("citation", "")).strip().upper().startswith("TBD")


def table(header: list[str], rows: list[list]) -> list[str]:
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return out


def counts(title: str, counter: Counter, vocab: dict[str, dict] | None, total: int, note: str = "") -> list[str]:
    keys = list(vocab) if vocab else [k for k, _ in counter.most_common()]
    keys += [k for k in counter if k not in keys]
    rows = []
    for k in keys:
        label = f"{k}（{vocab[k]['zh']}）" if vocab and k in vocab else k
        rows.append([label, counter.get(k, 0), f"{100 * counter.get(k, 0) / total:.1f}%" if total else "-"])
    lines = [f"### {title}", ""]
    if note:
        lines += [note, ""]
    return lines + table(["取值", "范式数", "占比"], rows) + [""]


def cross(title: str, rows_vocab: list[str], cols: list[str], pairs: Counter) -> tuple[list[str], list[tuple]]:
    zeros = []
    rows = []
    for r in rows_vocab:
        line = [r]
        for c in cols:
            n = pairs.get((r, c), 0)
            line.append(n if n else "·")
            if not n:
                zeros.append((r, c))
        rows.append(line)
    return [f"### {title}", ""] + table([""] + cols, rows) + ["", "（· = 0）", ""], zeros


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--version", default="", help="version label used in the title")
    ap.add_argument("--out", default="", help="output path (default: stdout)")
    ap.add_argument("--shared", type=int, default=3, help="threshold for 'markers used by >= N paradigms'")
    args = ap.parse_args()

    a = load()
    ps_all = {pid: d for pid, (_, d) in sorted(a.paradigms.items())}
    deprecated = [pid for pid, d in ps_all.items() if d["status"] == "deprecated"]
    ps = {pid: d for pid, d in ps_all.items() if pid not in deprecated}  # active concrete paradigms only
    ms = {mid: d for mid, (_, d) in sorted(a.markers.items())}
    fam, rec, stim = terms("families"), terms("recording_modality"), terms("stimulus_modality")
    mtypes = terms("marker_types")
    bci_vocab = {k: {"zh": z} for k, z in (("active", "主动"), ("reactive", "反应式"), ("passive", "被动"), ("none", "非 BCI"))}

    pkg, pkg_cls = {}, {}
    cand_path = ROOT / "curation" / "candidates.csv"
    if cand_path.exists():
        with open(cand_path, encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                pkg[r["proposed_id"]] = r["pkg"]
                if r.get("class"):
                    pkg_cls[r["class"]] = r["pkg"]
    # concrete paradigms added after the candidate was registered inherit the package of their class (D-057)
    pkg_of = {pid: pkg.get(pid) or pkg_cls.get(d.get("class", ""), "-") for pid, d in ps.items()}

    used_by: dict[str, list[str]] = defaultdict(list)
    for pid, d in ps.items():
        for m in d["markers"]:
            used_by[m].append(pid)
    n = len(ps)
    tbd = [pid for pid, d in ps.items() if is_tbd(d["first_source"])]
    tbd_var = [(pid, v["name"]) for pid, d in ps.items() for v in d.get("variants", []) if is_tbd(v["source"])]
    n_var = sum(len(d.get("variants", [])) for d in ps.values())
    edges = sum(len(d["markers"]) for d in ps.values())

    L = [f"# 覆盖度报告{' v' + args.version if args.version else ''}", "",
         f"> 由 `scripts/coverage_report.py` 生成（{date.today().isoformat()}），数据来自 `paradigms/`、`knowledge/markers/`、"
         "`taxonomy/` 与 `curation/candidates.csv`（包归属）。请勿手工修改本文件，重新运行脚本即可。", "",
         "## 1. 总数", ""]
    L += table(["项目", "数量"], [
        ["范式文件（具体范式，不含 deprecated）", n],
        ["status: deprecated 的范式文件（并入其他具体范式，序号不复用）", f"{len(deprecated)}" + (f"（{', '.join(deprecated)}）" if deprecated else "")],
        ["范式类（paradigms/_classes.yaml）", len(a.classes)],
        ["有 `protocol` 的具体范式", sum(1 for d in ps.values() if d.get("protocol"))], ["标记物文件", len(ms)], ["范式–标记物关联（elicits）", edges],
        ["每个范式的平均标记物数", f"{edges / n:.2f}" if n else "-"], ["变体", n_var],
        ["first_source 为 TBD 的范式", f"{len(tbd)}（{100 * len(tbd) / n:.1f}%）" if n else 0],
        ["出处已核实（verified: true）的 first_source", sum(1 for d in ps.values() if d["first_source"].get("verified"))],
        ["status: reviewed 的范式", sum(1 for d in ps.values() if d["status"] == "reviewed")],
        ["未被任何范式使用的标记物", sum(1 for m in ms if not used_by[m])],
    ]) + ["", "## 2. 分布", ""]

    L += counts("2.1 范式族", Counter(d["family"] for d in ps.values()), fam, n)
    pk = Counter(pkg_of.values())
    L += counts("2.2 工作包", pk, {k: {"zh": "包 " + k} for k in sorted(pk)}, n)
    L += counts("2.3 记录模态", Counter(v for d in ps.values() for v in d["recording_modality"]), rec, n,
                "一个范式可有多个记录模态，占比按范式数计算，合计可超过 100%。")
    L += counts("2.4 刺激模态", Counter(v for d in ps.values() for v in d["stimulus_modality"]), stim, n,
                "一个范式可有多个刺激模态。")
    L += counts("2.5 BCI 类别", Counter(v for d in ps.values() for v in d["bci_category"]), bci_vocab, n)
    mt = Counter(d["type"] for d in ms.values())
    mte = Counter(ms[m]["type"] for d in ps.values() for m in d["markers"])
    L += ["### 2.6 标记物类型", ""] + table(["类型", "标记物数", "范式–标记物关联数"], [
        [f"{k}（{mtypes[k]['zh']}）" if k in mtypes else k, mt.get(k, 0), mte.get(k, 0)]
        for k in list(mtypes) + [k for k in mt if k not in mtypes]]) + [""]

    by_pkg_fam = Counter((pkg_of[p], d["family"]) for p, d in ps.items())
    L += ["### 2.7 包 × 族", ""] + table(["包", "族", "范式数", "TBD"], [
        [k[0], k[1], c, sum(1 for p in tbd if pkg_of[p] == k[0] and ps[p]["family"] == k[1])]
        for k, c in sorted(by_pkg_fam.items())]) + [""]

    L += ["## 3. first_source 为 TBD 的范式", "",
          f"共 {len(tbd)} 个" + (f"；另有 {len(tbd_var)} 个变体的出处为 TBD" if tbd_var else "") + "。", ""]
    L += table(["包", "ID", "名称", "族"], [[pkg_of[p], p, ps[p]["name"]["zh"], ps[p]["family"]] for p in
                                         sorted(tbd, key=lambda x: (pkg_of[x], x))]) + [""]
    for p, v in tbd_var:
        L.append(f"- 变体 TBD：{p} · {v}")
    if tbd_var:
        L.append("")

    shared = sorted(((m, u) for m, u in used_by.items() if len(u) >= args.shared), key=lambda x: (-len(x[1]), x[0]))
    L += [f"## 4. 被 ≥{args.shared} 个范式使用的标记物", "", f"共 {len(shared)} 个。", ""]
    L += table(["标记物", "类型", "范式数", "涉及族数", "范式"], [
        [m, ms[m]["type"], len(u), len({ps[p]["family"] for p in u}), ", ".join(u)] for m, u in shared]) + [""]

    dist = Counter(len(used_by[m]) for m in ms)
    L += ["## 5. 每个标记物的范式数", "", "### 5.1 分布", ""]
    L += table(["使用该标记物的范式数", "标记物数"], [[k, dist[k]] for k in sorted(dist)]) + [""]
    L += ["### 5.2 全表", ""] + table(["标记物", "类型", "范式数", "范式"], [
        [m, ms[m]["type"], len(used_by[m]), ", ".join(used_by[m]) or "—"] for m in ms]) + [""]

    L += ["## 6. 零覆盖空白", "", "下表中的 · 表示该组合目前没有任何范式。并非每个空格都是缺口（例如 PET × 稳态响应在方法上不适用），"
          "但它们是第二遍和新候选检索的检查清单。", ""]
    fams = list(fam)
    t, z_rec = cross("6.1 记录模态 × 族", list(rec), fams,
                     Counter((r, d["family"]) for d in ps.values() for r in d["recording_modality"]))
    L += t
    t, z_stim = cross("6.2 刺激模态 × 族", list(stim), fams,
                      Counter((s, d["family"]) for d in ps.values() for s in d["stimulus_modality"]))
    L += t
    t, z_bci = cross("6.3 BCI 类别 × 族", list(bci_vocab), fams,
                     Counter((b, d["family"]) for d in ps.values() for b in d["bci_category"]))
    L += t
    t, z_mt = cross("6.4 标记物类型 × 族（按范式–标记物关联）", list(mtypes), fams,
                    Counter((ms[m]["type"], d["family"]) for d in ps.values() for m in d["markers"]))
    L += t
    unused_terms = [f"recording_modality: {k}" for k in rec if not any(k in d["recording_modality"] for d in ps.values())]
    unused_terms += [f"stimulus_modality: {k}" for k in stim if not any(k in d["stimulus_modality"] for d in ps.values())]
    unused_terms += [f"marker type: {k}" for k in mtypes if not mt.get(k)]
    L += ["### 6.5 汇总", ""] + table(["交叉表", "零格数", "总格数"], [
        ["记录模态 × 族", len(z_rec), len(rec) * len(fams)], ["刺激模态 × 族", len(z_stim), len(stim) * len(fams)],
        ["BCI 类别 × 族", len(z_bci), len(bci_vocab) * len(fams)], ["标记物类型 × 族", len(z_mt), len(mtypes) * len(fams)]]) + [""]
    L += ["没有任何范式使用的词表取值：" + ("；".join(unused_terms) if unused_terms else "无"), ""]
    no_bci_fam = [f for f in fams if not any(d["family"] == f and set(d["bci_category"]) - {"none"} for d in ps.values())]
    L += ["没有任何 BCI 用途（active / reactive / passive）范式的族：" + ("、".join(no_bci_fam) if no_bci_fam else "无"), ""]

    # 7. classes vs concrete paradigms (D-057)
    inst: dict[str, list[str]] = defaultdict(list)
    for pid, d in ps.items():
        inst[d.get("class", pid.rsplit("-", 1)[0])].append(pid)
    cls = {cid: a.classes.get(cid, {"family": ps[v[0]]["family"]}) for cid, v in inst.items()} | {
        cid: c for cid, c in a.classes.items() if cid not in inst}
    pkg_of_cls = {cid: "/".join(sorted({pkg_of[p] for p in inst.get(cid, [])})) or "-" for cid in cls}

    def proto_n(pids: list[str]) -> int:
        return sum(1 for p in pids if ps[p].get("protocol"))

    def cvc_rows(keyf, keys) -> list[list]:
        rows = []
        for k in keys:
            cs = [c for c in cls if keyf(c) == k]
            if not cs:
                continue
            pids = [p for c in cs for p in inst.get(c, [])]
            rows.append([k, len(cs), len(pids), f"{len(pids) / len(cs):.2f}", sum(1 for c in cs if len(inst.get(c, [])) > 1),
                         proto_n(pids)])
        return rows

    hdr = ["", "范式类", "具体范式", "具体范式 / 类", "≥2 个具体范式的类", "有 protocol"]
    L += ["## 7. 范式类与具体范式（D-057）", "",
          "范式类 `<族>-<简称>` 记录共同机制，具体范式 `<族>-<简称>-<序号>` 是一个可复现的任务配置（类别集、提示/编码、"
          "试次结构、反馈任一不同即另取序号）。schema 0.2 迁移时每个 schema 0.1 文件生成一个范式类，因此迁移刚完成时两者一一对应；"
          "sprint 2 的拆分会使比值上升。", ""]
    L += ["### 7.1 按族", ""] + table(["族"] + hdr[1:], cvc_rows(lambda c: cls[c]["family"], list(fam))) + [""]
    L += ["### 7.2 按工作包", ""] + table(["包"] + hdr[1:], cvc_rows(lambda c: pkg_of_cls[c], sorted(set(pkg_of_cls.values()))))
    L += [""]
    pd = Counter(len(v) for v in inst.values())
    pd[0] = sum(1 for c in cls if c not in inst)
    L += ["### 7.3 每个范式类的具体范式数", ""] + table(["具体范式数", "范式类数"], [[k, pd[k]] for k in sorted(pd) if pd[k]])
    L += [""]
    pp = Counter(proto_n(inst.get(c, [])) for c in cls)
    L += ["### 7.4 每个范式类中已写 `protocol` 的具体范式数", ""] + table(
        ["有 protocol 的具体范式数", "范式类数"], [[k, pp[k]] for k in sorted(pp)]) + [""]
    multi = sorted((c for c in cls if len(inst.get(c, [])) > 1), key=lambda c: (-len(inst[c]), c))
    if multi:
        L += ["### 7.5 有多个具体范式的范式类", ""] + table(["范式类", "具体范式数", "具体范式"], [
            [c, len(inst[c]), ", ".join(sorted(inst[c]))] for c in multi]) + [""]

    # 8. protocol fields (D-057)
    protos = {pid: d.get("protocol") or {} for pid, d in ps.items()}
    L += ["## 8. 具体范式的 `protocol` 字段", ""]
    tim_vocab = {k: {"zh": z} for k, z in (("synchronous", "同步"), ("asynchronous", "异步"), ("block", "组块"),
                                           ("continuous", "连续"))}
    fb_vocab = {k: {"zh": z} for k, z in (("none", "无/开环"), ("discrete", "离散"), ("continuous", "连续"))}
    L += counts("8.1 试次结构（paradigm_timing）", Counter(str(p.get("paradigm_timing") or "（未填）") for p in protos.values()),
                tim_vocab, n)
    L += counts("8.2 反馈方式（feedback）", Counter(str(p.get("feedback") or "（未填）") for p in protos.values()), fb_vocab, n)
    fbp = Counter((pkg_of[pid], str(p.get("feedback") or "（未填）")) for pid, p in protos.items())
    tmp = Counter((pkg_of[pid], str(p.get("paradigm_timing") or "（未填）")) for pid, p in protos.items())
    pk_keys = sorted(set(pkg_of.values()))
    fbk = list(fb_vocab) + ["（未填）"]
    tik = list(tim_vocab) + ["（未填）"]
    L += ["### 8.3 工作包 × 反馈方式 / 试次结构", ""] + table(["包"] + fbk + tik, [
        [k] + [fbp.get((k, f), 0) for f in fbk] + [tmp.get((k, t), 0) for t in tik] for k in pk_keys]) + [""]
    def nbin(v):
        if not v:
            return "（未填）"
        return str(v) if v <= 6 else ("7–12" if v <= 12 else ">12")
    nb = Counter(nbin(p.get("n_classes")) for p in protos.values())
    L += counts("8.4 类别/条件数（n_classes）", nb, {k: {"zh": "类/条件" if k != "（未填）" else "未写 n_classes"} for k in ["1", "2", "3", "4", "5", "6", "7–12", ">12", "（未填）"]}, n)
    fields = ["n_classes", "classes", "cue", "stimulus_coding", "paradigm_timing", "feedback", "distinguishing"]
    L += ["### 8.5 字段填写率", "", "`stimulus_coding` 只在有编码方案时填写（如 SSVEP、c-VEP、P300 拼写器），未填不算缺项。", ""]
    L += table(["字段", "已填", "未填", "未填的具体范式（最多 15 个）"], [
        [f, sum(1 for p in protos.values() if p.get(f) not in (None, "", [])),
         sum(1 for p in protos.values() if p.get(f) in (None, "", [])),
         ", ".join([pid for pid, p in protos.items() if p.get(f) in (None, "", [])][:15]) if f != "stimulus_coding" else "—"]
        for f in fields]) + [""]
    top = sorted(inst, key=lambda c: (-len(inst[c]), c))[:15]
    L += ["### 8.6 具体范式最多的范式类（前 15）", ""] + table(["范式类", "名称", "包", "具体范式数", "TBD 源头", "反馈方式"], [
        [c, a.classes.get(c, {}).get("name", {}).get("zh", ""), pkg_of_cls[c], len(inst[c]),
         sum(1 for p in inst[c] if p in tbd),
         "/".join(sorted({str(protos[p].get("feedback") or "?") for p in inst[c]}))] for c in top]) + [""]
    tbd_pk = Counter(pkg_of[p] for p in tbd)
    all_pk = Counter(pkg_of.values())
    cls_tbd = [c for c, t in a.classes.items() if is_tbd(t.get("first_source", {}))]
    L += ["### 8.7 TBD 源头", "", f"具体范式 first_source 为 TBD：{len(tbd)} 个；范式类 first_source 为 TBD：{len(cls_tbd)} 个。", ""]
    L += table(["包", "具体范式", "TBD", "占比"], [[k, all_pk[k], tbd_pk.get(k, 0),
                                               f"{100 * tbd_pk.get(k, 0) / all_pk[k]:.1f}%"] for k in pk_keys]) + [""]

    text = "\n".join(L).rstrip() + "\n"
    if args.out:
        out = ROOT / args.out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT).as_posix()}")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
