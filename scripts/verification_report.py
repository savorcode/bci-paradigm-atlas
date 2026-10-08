# Copyright 2026 思维刻度 SavorCode
# SPDX-License-Identifier: Apache-2.0
"""Summarise the bibliographic verification of first sources (D-072): sources_check.csv against the atlas.

    python scripts/verification_report.py                      # print to stdout
    python scripts/verification_report.py --out curation/reports/verification_sprint3_counts.md

Reads curation/verification/sources_check.csv (one row per checked source: concrete paradigm first_source, variant
source or class first_source) and the atlas (scripts/atlas.py). Prints, per work package and per entity type, the
counts by check_status; the sources still TBD in the atlas (citation starting with "TBD"); the entries whose
`verified` flag is true (content verification per methodology §3 - expected 0 after a bibliographic-only sprint);
and a consistency check between check_status and the notes phrase `bibliography confirmed|corrected` (D-072) and
the D-073 phrase for records fetched from a recalled DOI candidate.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict

from atlas import ROOT, load

CHECK_FILE = ROOT / "curation" / "verification" / "sources_check.csv"
STATUSES = ["confirmed", "corrected", "tbd_resolved", "tbd_open", "not_found", "mismatch"]
OK = {"confirmed", "corrected", "tbd_resolved"}
PHRASE = re.compile(r"bibliography (confirmed|corrected)")
D073 = "origin candidate recalled, record confirmed via"


def is_tbd(source: dict) -> bool:
    return str(source.get("citation", "")).strip().upper().startswith("TBD")


def table(header: list[str], rows: list[list]) -> list[str]:
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return out


def notes_of(row: dict, atlas) -> str | None:
    """Notes text that should carry the D-072 phrase for this row (None if the entity is missing)."""
    if row["entity_type"] == "class":
        t = atlas.classes.get(row["entity_id"])
        return None if t is None else str(t.get("notes", ""))
    if row["entity_id"] not in atlas.paradigms:
        return None
    d = atlas.paradigms[row["entity_id"]][1]
    if row["entity_type"] == "variant":
        for v in d.get("variants", []):
            if v.get("name") == row.get("variant_name"):
                return str(v.get("note", ""))
        return None
    return str(d.get("notes", ""))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default="", help="output path (default: stdout)")
    ap.add_argument("--check", default=str(CHECK_FILE), help="sources_check.csv path")
    args = ap.parse_args()

    atlas = load()
    with open(args.check, encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    pkgs = sorted({r["pkg"] for r in rows})
    types = ["concrete", "variant", "class"]

    lines = ["# 出处书目核实汇总 / Bibliographic verification summary", "",
             f"来源：`{CHECK_FILE.relative_to(ROOT)}`（{len(rows)} 行）；图谱：{len(atlas.paradigms)} 个具体范式、{len(atlas.classes)} 个范式类。", ""]

    # 1. counts per package x status
    lines += ["## 1. 各包按 check_status 计数", ""]
    by_pkg = Counter((r["pkg"], r["check_status"]) for r in rows)
    body = [[p] + [by_pkg.get((p, s), 0) for s in STATUSES] + [sum(by_pkg.get((p, s), 0) for s in STATUSES)] for p in pkgs]
    body.append(["合计"] + [sum(by_pkg.get((p, s), 0) for p in pkgs) for s in STATUSES] + [len(rows)])
    lines += table(["包"] + STATUSES + ["合计"], body) + [""]

    # 2. counts per entity type x status, per package
    lines += ["## 2. 各包按实体类型与 check_status 计数", ""]
    by_pt = Counter((r["pkg"], r["entity_type"], r["check_status"]) for r in rows)
    body = []
    for p in pkgs:
        for t in types:
            n = [by_pt.get((p, t, s), 0) for s in STATUSES]
            if sum(n):
                body.append([p, t] + n + [sum(n)])
    for t in types:
        n = [sum(by_pt.get((p, t, s), 0) for p in pkgs) for s in STATUSES]
        body.append(["合计", t] + n + [sum(n)])
    lines += table(["包", "实体类型"] + STATUSES + ["合计"], body) + [""]

    # 3. remaining TBD in the atlas
    tbd_concrete = sorted(pid for pid, (_, d) in atlas.paradigms.items()
                          if d.get("status") != "deprecated" and is_tbd(d.get("first_source", {})))
    tbd_class = sorted(cid for cid, t in atlas.classes.items() if is_tbd(t.get("first_source", {})))
    status_of = {(r["entity_type"], r["entity_id"]): r["check_status"] for r in rows}
    lines += ["## 3. 图谱中仍为 TBD 的 first_source", "",
              f"具体范式 {len(tbd_concrete)} 个，范式类 {len(tbd_class)} 个。", ""]
    lines += table(["实体类型", "ID", "sources_check 状态"],
                   [["concrete", i, status_of.get(("concrete", i), "-")] for i in tbd_concrete]
                   + [["class", i, status_of.get(("class", i), "-")] for i in tbd_class]) + [""]

    # 4. not_found / tbd_open backlog from the check file
    backlog = [r for r in rows if r["check_status"] in ("not_found", "tbd_open", "mismatch")]
    lines += ["## 4. 未核实清单（not_found / tbd_open / mismatch）", "", f"{len(backlog)} 行。", ""]
    lines += table(["包", "实体类型", "ID", "状态", "备注（截断）"],
                   [[r["pkg"], r["entity_type"], r["entity_id"] + (f" / {r['variant_name']}" if r.get("variant_name") else ""),
                     r["check_status"], r["note"][:120].replace("|", "/")] for r in backlog]) + [""]

    # 5. verified: true
    ver = [("concrete", pid) for pid, (_, d) in atlas.paradigms.items() if d.get("first_source", {}).get("verified") is True]
    ver += [("concrete-variant", f"{pid} / {v.get('name')}") for pid, (_, d) in atlas.paradigms.items()
            for v in d.get("variants", []) if (v.get("source") or {}).get("verified") is True]
    ver += [("class", cid) for cid, t in atlas.classes.items() if t.get("first_source", {}).get("verified") is True]
    lines += ["## 5. `verified: true` 的条目（内容核实，方法说明 §3）", "", f"{len(ver)} 条（书目核实冲刺后应为 0）。", ""]
    if ver:
        lines += table(["实体类型", "ID"], [list(v) for v in ver]) + [""]

    # 6. phrase consistency
    missing, forbidden, d073, unresolved = [], [], 0, []
    for r in rows:
        txt = notes_of(r, atlas)
        if txt is None:
            unresolved.append(r)
            continue
        has = bool(PHRASE.search(txt))
        if r["check_status"] in OK and not has:
            missing.append(r)
        if r["check_status"] not in OK and has and r["entity_type"] != "concrete":
            forbidden.append(r)
        if D073 in txt:
            d073 += 1
    # concrete files whose first_source failed but whose notes carry the phrase (for a variant check) are listed separately
    concrete_forbidden = [r for r in rows if r["check_status"] not in OK and r["entity_type"] == "concrete"
                          and notes_of(r, atlas) and PHRASE.search(notes_of(r, atlas))]
    lines += ["## 6. notes 短语一致性（D-072 / D-073）", "",
              f"- confirmed/corrected/tbd_resolved 但 notes 缺 `bibliography confirmed|corrected`：{len(missing)}",
              f"- not_found/tbd_open/mismatch 但 notes 含该短语：{len(forbidden) + len(concrete_forbidden)}",
              f"- 含 D-073 短语 `{D073} <API>` 的条目：{d073}",
              f"- sources_check 行在图谱中找不到对应实体：{len(unresolved)}", ""]
    for title, lst in (("缺短语", missing), ("不应有短语", forbidden + concrete_forbidden), ("找不到实体", unresolved)):
        if lst:
            lines += [f"### {title}", ""] + table(["包", "实体类型", "ID", "状态"],
                                                  [[r["pkg"], r["entity_type"], r["entity_id"], r["check_status"]] for r in lst]) + [""]

    text = "\n".join(lines) + "\n"
    if args.out:
        (ROOT / args.out).write_text(text, encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        print(text, end="")
    print(f"# {len(rows)} rows; TBD concrete {len(tbd_concrete)}, class {len(tbd_class)}; verified:true {len(ver)}; "
          f"phrase missing {len(missing)}, forbidden {len(forbidden) + len(concrete_forbidden)}")


if __name__ == "__main__":
    main()
