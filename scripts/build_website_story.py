# Copyright 2026 思维刻度 SavorCode
# SPDX-License-Identifier: Apache-2.0
"""Export the data behind the one-page project site (website/index.html) to website/story-data.json.

Usage:  python scripts/build_website_story.py
The file holds counts, the 12 families, every active paradigm with its markers, and every marker that has
generators or indexes (with the first source of each link). Rebuild it after atlas changes; CI checks it is current.
为单页项目网站导出数据（website/story-data.json）。图谱数据变化后重新运行；CI 会检查是否最新。
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter

from atlas import ROOT, load, read_yaml, terms

DEEP = {"BR.striatum", "BR.amygdala", "BR.thalamus", "BR.inferior_colliculus", "BR.hippocampus", "BR.insula",
        "BR.anterior_insula", "BR.posterior_insula", "BR.parahippocampal", "BR.STN", "BR.dorsal_striatum"}
TEMPORAL = {"BR.pSTS", "BR.A1", "BR.STG", "BR.MTG", "BR.ATL"}
# Paradigms shown first for well-known markers (the textbook example of each signal).
PINS = {"P3b": ["PER-ODD-001", "PER-ODD-002"], "SMR_ERD": ["MOT-MI-001", "MOT-MI-002", "MOT-ME-001"],
        "SSVEP": ["SSR-SSVEP-001"], "N400": ["LAN-N400-001"], "ERN": ["CTL-FLK-001"], "MMN": ["PER-MMN-001"]}


def lobe(rid: str, parent: str | None) -> str:
    if rid in DEEP:
        return "deep"
    if rid == "BR.cerebellum":
        return "cerebellum"
    if rid in TEMPORAL:
        return "temporal"
    if rid in ("BR.M1", "BR.S1", "BR.sensorimotor_cortex"):
        return "central"
    if rid in ("BR.dACC", "BR.frontal_cortex") or parent == "BR.frontal_cortex":
        return "frontal"
    if rid in ("BR.parietal_cortex", "BR.PCC") or parent == "BR.parietal_cortex":
        return "parietal"
    if rid == "BR.visual_cortex" or parent == "BR.visual_cortex":
        return "occipital"
    return "deep"


def short_source(src: dict) -> list[str]:
    """First author + year, journal, DOI of a Vancouver-style source."""
    c = src.get("citation", "")
    author = re.split(r"[ ,.]", c.strip(), maxsplit=1)[0]
    journals = re.findall(r"([A-Z][^.;:?!]{1,60}?)\.?\s+\d{4}[;.,]", c)
    return [f"{author} {src.get('year', '')}".strip(), (journals[-1].strip() if journals else "")[:42], src.get("doi", "")]


def stamp_assets() -> None:
    """Add a content hash to the CSS/JS/data references so browsers fetch new files after each update."""
    web = ROOT / "website"
    for name, page in (("story-data.json", "story.js"), ("story.css", "index.html"), ("story.js", "index.html")):
        digest = hashlib.sha1((web / name).read_bytes().replace(b"\r\n", b"\n")).hexdigest()[:8]
        path = web / page
        text = path.read_text(encoding="utf-8")
        new = re.sub(r"\./" + re.escape(name) + r"(\?v=[0-9a-f]+)?", f"./{name}?v={digest}", text)
        if new != text:
            path.write_text(new, encoding="utf-8")


def main() -> int:
    atlas = load()
    regions = {t["id"]: t for t in read_yaml(ROOT / "knowledge" / "regions.yaml")["terms"]}
    constructs = {t["id"]: t for t in read_yaml(ROOT / "knowledge" / "constructs.yaml")["terms"]}
    classes = read_yaml(ROOT / "paradigms" / "_classes.yaml")["terms"]
    active = {pid: d for pid, (_, d) in atlas.paradigms.items() if d.get("status") != "deprecated"}

    users: dict[str, list[dict]] = {}
    for d in active.values():
        for m in d.get("markers") or []:
            users.setdefault(m, []).append(d)

    markers = []
    for mid, (_, d) in sorted(atlas.markers.items()):
        if not (d.get("generators") or d.get("indexes")):
            continue
        us = sorted(users.get(mid, []), key=lambda x: ((x["markers"] or []).index(mid), not x["id"].endswith("-001"), x["id"]))
        short = mid[3:]
        for pid in reversed(PINS.get(short, [])):
            hit = [x for x in us if x["id"] == pid]
            us = hit + [x for x in us if x["id"] != pid]
        markers.append({
            "id": short, "zh": d["name"]["zh"], "en": d["name"]["en"], "type": d["type"], "n": len(us),
            "ex": [[x["id"], x["name"]["zh"], x["name"]["en"]] for x in us[:4]],
            "g": [[g["region"], g["evidence"], len(g["sources"]), *short_source(g["sources"][0])] for g in d.get("generators") or []],
            "x": [[x["construct"], x["evidence"], len(x["sources"]), *short_source(x["sources"][0])] for x in d.get("indexes") or []],
        })
    used_r = {g[0] for m in markers for g in m["g"]}
    used_c = {x[0] for m in markers for x in m["x"]}
    fams = terms("families")
    families = [{"p": f["prefix"], "zh": f["zh"], "en": f["en"], "c": sum(1 for c in classes if c["family"] == fid),
                 "n": sum(1 for d in active.values() if d["family"] == fid)} for fid, f in fams.items()]
    with open(ROOT / "curation" / "literature.csv", encoding="utf-8-sig", newline="") as fh:
        n_lit = sum(1 for _ in csv.DictReader(fh))
    ev = Counter(e[1] for m in markers for e in m["g"] + m["x"])
    data = {
        "S": {"classes": len(classes), "paradigms": len(active), "markers": len(atlas.markers), "linked": len(markers),
              "regions": sum(1 for t in regions.values() if t.get("status") != "deprecated"), "constructs": len(constructs),
              "lit": n_lit, "links": sum(len(m["g"]) + len(m["x"]) for m in markers), "ev": dict(sorted(ev.items()))},
        "F": families,
        "M": markers,
        "R": {k: [regions[k]["zh"], regions[k]["en"], lobe(k, regions[k].get("parent"))] for k in sorted(used_r)},
        "C": {k: [constructs[k]["zh"], constructs[k]["en"]] for k in sorted(used_c)},
        "P": [[pid, d["name"]["zh"], d["name"]["en"], [m[3:] for m in (d.get("markers") or [])][:4]] for pid, d in sorted(active.items())],
    }
    out = ROOT / "website" / "story-data.json"
    out.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    stamp_assets()
    print(f"{len(active)} paradigms, {len(markers)} linked markers, {data['S']['links']} links -> {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
