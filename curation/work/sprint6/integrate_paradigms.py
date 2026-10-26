"""Register the sprint-6 paradigm classes: literature leads, paradigm–literature links, candidates,
concrete-paradigm and paradigm–marker registries, and marker usage. Run once from the repository root."""
import csv
import glob
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
W = ROOT / "curation" / "work" / "sprint6"
PKG = {"perception": "A", "steady_state": "A", "motor": "B", "imagery": "B", "stimulation": "B", "error": "C",
       "control": "C", "memory": "D", "language": "D", "emotion": "E", "social": "E", "state": "E"}
HELD = ("STM-ICMS", "STM-PHOS", "STM-ESM")


def rows(path):
    with open(path, encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def append(path, fields, new):
    with open(path, "a", encoding="utf-8", newline="") as fh:
        csv.DictWriter(fh, fieldnames=fields, lineterminator="\r\n").writerows(new)


classes = []
for g in ("P1", "P2", "P3"):
    classes += [c for c in yaml.safe_load(open(W / f"paradigms_{g}" / "classes_new.yaml", encoding="utf-8")) if c["id"] not in HELD]
cids = {c["id"] for c in classes}
concrete = {}
for p in sorted(glob.glob(str(ROOT / "paradigms" / "*" / "*.yaml"))):
    d = yaml.safe_load(open(p, encoding="utf-8"))
    if isinstance(d, dict) and d.get("class") in cids:
        concrete[d["id"]] = d

# 1. literature leads and paradigm-literature links
lit_path = ROOT / "curation" / "literature.csv"
lit = rows(lit_path)
lit_fields = list(lit[0].keys())
by_doi = {r["doi"].lower(): r["ref_id"] for r in lit if r["doi"]}
nxt = max(int(r["ref_id"][1:]) for r in lit) + 1
links, new_lit = [], []
for g in ("P1", "P2", "P3"):
    for s in rows(W / f"paradigms_{g}" / "sources.csv"):
        ids = [x for x in s["paradigm_id"].split(";") if x and not x.startswith(HELD)]
        pids = [x for x in ids if x in concrete]
        if not pids:
            continue
        doi = (s.get("doi") or "").strip()
        rid = by_doi.get(doi.lower()) if doi else None
        if not rid:
            rid = f"R{nxt:04d}"
            nxt += 1
            c = s["citation"].strip()
            parts = [x.strip() for x in c.split(". ")]
            new_lit.append({**{k: "" for k in lit_fields}, "ref_id": rid, "authors": parts[0] if len(parts) > 2 else "",
                            "year": s.get("year", ""), "title": parts[1] if len(parts) > 2 else c,
                            "venue": ". ".join(parts[2:]).rstrip(".") if len(parts) > 2 else "", "doi": doi,
                            "url": f"https://doi.org/{doi}" if doi else "", "found_via": "curator_search_s6",
                            "source_page": f"curation/work/sprint6/paradigms_{g}", "paradigms": ";".join(pids),
                            "verified": "false", "qa_flag": "" if doi else "no_doi"})
            if doi:
                by_doi[doi.lower()] = rid
        role = "first_source" if s["ref_role"] == "first_source" else "key_reference"
        for pid in pids:
            links.append({"proposed_id": pid, "ref_id": rid, "role": role, "found_via": "curator_search_s6"})
append(lit_path, lit_fields, new_lit)
pl_path = ROOT / "curation" / "paradigm_literature.csv"
seen = {(r["proposed_id"], r["ref_id"]) for r in rows(pl_path)}
uniq = []
for r in links:
    if (r["proposed_id"], r["ref_id"]) not in seen:
        seen.add((r["proposed_id"], r["ref_id"]))
        uniq.append(r)
append(pl_path, ["proposed_id", "ref_id", "role", "found_via"], uniq)

# 2. candidates
cand_path = ROOT / "curation" / "candidates.csv"
cand = rows(cand_path)
cf = list(cand[0].keys())
cn = max(int(r["candidate_id"][1:]) for r in cand) + 1
new_c = []
for c in classes:
    ps = [d for d in concrete.values() if d["class"] == c["id"]]
    cats = {x for d in ps for x in d.get("bci_category") or []}
    rel = "核心" if cats & {"active", "reactive"} else ("相关" if "passive" in cats else "基础")
    n_refs = sum(1 for r in uniq if r["proposed_id"].startswith(c["id"] + "-"))
    new_c.append({**{k: "" for k in cf}, "candidate_id": f"C{cn:03d}", "pkg": PKG[c["family"]], "family": c["family"],
                  "proposed_id": c["id"] + "-001", "class": c["id"], "n_concrete": str(len(ps)), "name_zh": c["name"]["zh"],
                  "name_en": c["name"]["en"], "aliases": "; ".join(c.get("aliases") or []),
                  "likely_markers": "; ".join(c.get("markers") or []),
                  "recording_modality": "; ".join(sorted({m for d in ps for m in d.get("recording_modality") or []})),
                  "bci_relevance": rel, "priority": "2" if rel != "基础" else "3", "decision": "收录", "decision_ref": "D-078",
                  "n_refs": str(n_refs), "n_first_source": "1", "datasets": "; ".join(sorted({(x.get("name") if isinstance(x, dict) else str(x)) for d in ps for x in d.get("datasets") or []})),
                  "status": "第一遍完成", "note": "sprint 6 新增范式类"})
    cn += 1
append(cand_path, cf, new_c)

# 3. concrete-paradigm and paradigm-marker registries
cp_path = ROOT / "curation" / "registry" / "concrete_paradigms.csv"
cpf = list(rows(cp_path)[0].keys())
cmark = {c["id"]: c.get("markers") or [] for c in classes}
new_cp, new_pm = [], []
for pid, d in sorted(concrete.items()):
    pr = d.get("protocol") or {}
    fs = d.get("first_source") or {}
    new_cp.append({"id": pid, "class": d["class"], "family": d["family"], "pkg": PKG[d["family"]], "name_zh": d["name"]["zh"],
                   "name_en": d["name"]["en"], "n_classes": str(pr.get("n_classes", "")), "classes": "; ".join(pr.get("classes") or []),
                   "cue": pr.get("cue", ""), "stimulus_coding": pr.get("stimulus_coding", ""), "paradigm_timing": pr.get("paradigm_timing", ""),
                   "feedback": pr.get("feedback", ""), "distinguishing": pr.get("distinguishing", ""),
                   "first_source_status": "TBD" if str(fs.get("citation", "")).startswith("TBD") else "待核实",
                   "datasets": "; ".join((x.get("name") if isinstance(x, dict) else str(x)) for x in d.get("datasets") or []),
                   "contributors": "; ".join(d.get("contributors") or []), "status": d.get("status", "draft")})
    new_pm.append({"proposed_id": pid, "class": d["class"], "marker_ids": ";".join(d.get("markers") or []),
                   "class_marker_ids": ";".join(cmark[d["class"]])})
append(cp_path, cpf, new_cp)
append(ROOT / "curation" / "registry" / "paradigm_markers.csv", ["proposed_id", "class", "marker_ids", "class_marker_ids"], new_pm)

# 4. marker usage counts for the markers the new paradigms use
mk_path = ROOT / "curation" / "registry" / "markers.csv"
mk = rows(mk_path)
mkf = list(mk[0].keys())
use_c, use_p = defaultdict(set), defaultdict(set)
for p in glob.glob(str(ROOT / "paradigms" / "*" / "*.yaml")):
    d = yaml.safe_load(open(p, encoding="utf-8"))
    if isinstance(d, dict) and d.get("status") != "deprecated" and "class" in d:
        for m in d.get("markers") or []:
            use_p[m].add(d["id"])
            use_c[m].add(d["class"])
touched = {m for d in concrete.values() for m in d.get("markers") or []}
for r in mk:
    m = r["marker_id"]
    if m in touched:
        r.update(used_by_class=";".join(sorted(use_c[m])), used_by=";".join(sorted(use_p[m])),
                 n_classes=str(len(use_c[m])), n_concrete=str(len(use_p[m])))
with open(mk_path, "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=mkf, lineterminator="\r\n")
    w.writeheader()
    w.writerows(mk)
print(f"classes {len(classes)}, concrete {len(concrete)}, literature +{len(new_lit)}, links +{len(uniq)}, candidates +{len(new_c)}, markers touched {len(touched)}")
