"""Emulate step 4 of paradigm_factory.knowledge.bridge.attach_atlas (marker -> construct / region edges)
for an atlas checkout, and report how many bridge D-level links are superseded by atlas evidence.
Usage: python factory_yield.py <factory src/paradigm_factory> <atlas knowledge dir> [<old atlas knowledge dir>]"""
import glob, sys, yaml
from collections import Counter
from pathlib import Path

def run(F: Path, K: Path):
    br = yaml.safe_load(open(F / "knowledge/bridge.yaml", encoding="utf-8"))
    ca, ma = br.get("construct_alias") or {}, br.get("marker_alias") or {}
    fm = yaml.safe_load(open(F / "graph/data/markers.yaml", encoding="utf-8"))
    cons = {c["id"] for c in yaml.safe_load(open(F / "graph/data/constructs.yaml", encoding="utf-8"))}
    cons |= {c["id"] for c in br.get("constructs_extra") or []}
    cons |= {ca.get(t["id"], t["id"]) for t in yaml.safe_load(open(K / "constructs.yaml", encoding="utf-8"))["terms"]}
    have = {(m["id"], x["c"]) for m in fm for x in m.get("indexes") or []}
    fmids = {m["id"] for m in fm}
    marks = {}
    for p in sorted(glob.glob(str(K / "markers/*.yaml"))):
        d = yaml.safe_load(open(p, encoding="utf-8"))
        marks[d["id"]] = d
    merged = {a: ma.get(a, a) if ma.get(a, a) in fmids else a for a in marks}
    edges, superseded, gens = Counter(), [], Counter()
    bridge_pairs = []
    mrow = br.get("markers") or {}
    for aid, d in marks.items():
        mid = merged[aid]
        for ix in d.get("indexes") or []:
            cid = ca.get(ix.get("construct", ""), ix.get("construct", ""))
            if cid in cons and (mid, cid) not in have:
                have.add((mid, cid)); edges["atlas_" + str(ix.get("evidence"))] += 1
        for g in d.get("generators") or []:
            gens[g.get("evidence")] += 1
        for cid, w in (mrow.get(aid) or {}).get("idx") or []:
            bridge_pairs.append((mid, cid))
    for mid, rows in (br.get("marker_extra_idx") or {}).items():
        for cid, w in rows:
            bridge_pairs.append((mid, cid))
    used = 0
    for mid, cid in bridge_pairs:
        if cid not in cons:
            continue
        if (mid, cid) in have:
            superseded.append((mid, cid))
        else:
            have.add((mid, cid)); used += 1
    return dict(atlas_edges=sum(edges.values()), by_grade=dict(edges), generator_edges=sum(gens.values()),
                bridge_D_total=len(bridge_pairs), bridge_D_used=used, bridge_D_superseded=len(superseded),
                markers_with_atlas_evidence=sum(1 for d in marks.values() if d.get("indexes") or d.get("generators")),
                superseded=superseded)

if __name__ == "__main__":
    F = Path(sys.argv[1]); new = run(F, Path(sys.argv[2]))
    old = run(F, Path(sys.argv[3])) if len(sys.argv) > 3 else None
    for k in ("markers_with_atlas_evidence", "atlas_edges", "by_grade", "generator_edges", "bridge_D_total", "bridge_D_used", "bridge_D_superseded"):
        print(f"{k}: {old[k] if old else '-'} -> {new[k]}")
    print("superseded pairs:", "; ".join(f"{m}->{c}" for m, c in new["superseded"]))
