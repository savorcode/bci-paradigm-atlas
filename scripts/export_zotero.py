# Copyright 2026 思维刻度 SavorCode
# SPDX-License-Identifier: Apache-2.0
"""Export the literature table as a Zotero RDF file with collections, for import into the team Zotero group library.

Usage:  python scripts/export_zotero.py [--out curation/zotero/bci_atlas_literature.rdf]
In Zotero: select the group library, then File > Import, choose the .rdf file. Zotero creates one collection named after
the file, containing:
  01 范式族 / <family>          literature linked to paradigms of that family (paradigm_literature.csv and literature.csv)
  02 标记物（知识层）/ <marker>  sources of marker generators and indexes
  03 词表（脑区与构念）          sources of region and construct terms
  04 未关联                      leads not yet linked to any paradigm, marker or term
An item appears once and may sit in several collections. Each item carries its atlas id (e.g. R0123) in Extra, and tags
for the paradigms / markers it supports, its qa_flag and found_via.
把文献表导出为带分类（collection）的 Zotero RDF，供导入团队群组库。数据以 curation/literature.csv 为准。
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path
from xml.sax.saxutils import escape

from atlas import ROOT, read_yaml

YEAR_SPLIT = re.compile(r"^(?P<j>.*?)\.?\s+(?P<y>\d{4});\s*(?P<v>[^(:]*)(\((?P<i>[^)]*)\))?(:(?P<p>[\w\-–]+))?")
TRAIL_VOL = re.compile(r"^(?P<j>.*?)[\s,]+(?P<v>\d+)\s*(\((?P<i>[^)]*)\))?\s*(:\s*(?P<p>[\w\-–]+))?\s*$")


def split_venue(venue: str) -> dict[str, str]:
    venue = venue.strip().rstrip(".")
    m = YEAR_SPLIT.match(venue)
    if m:
        return {"journal": m["j"].strip(), "volume": (m["v"] or "").strip(), "issue": m["i"] or "", "pages": m["p"] or ""}
    m = TRAIL_VOL.match(venue)
    if m and m["j"]:
        return {"journal": m["j"].strip().rstrip(","), "volume": m["v"], "issue": m["i"] or "", "pages": m["p"] or ""}
    return {"journal": venue, "volume": "", "issue": "", "pages": ""}


def split_authors(text: str) -> list[tuple[str, str]]:
    text = re.sub(r",?\s*et al\.?$", "", text.strip().strip('"'))
    initials = re.compile(r"[A-ZÀ-Ý][A-ZÀ-Ý.\s\-]{0,7}")
    people: list[tuple[str, str]] = []
    if ";" in text:  # "Surname, Given; Surname, Given"
        for part in [p.strip() for p in text.split(";") if p.strip() and not p.strip().startswith("et al")]:
            sur, _, given = part.partition(",")
            people.append((sur.strip(), given.strip()))
        return people
    sur, comma, given = text.partition(",")
    if comma and "," not in given and re.search(r"[a-z]", given) and not re.search(r"\s(&|and)\s", text):
        return [(sur.strip(), given.strip())]  # "Freeman, Walter J"
    for part in [p.strip() for p in re.split(r"[,;]", re.sub(r"\s(&|and)\s", ", ", text)) if p.strip() not in ("", "…")]:
        part = re.sub(r"^(&|and)\s+", "", part)
        toks = part.split()
        if people and not people[-1][1] and initials.fullmatch(part):
            people[-1] = (people[-1][0], part)  # "Dias, R." / "Javal, É" style
        elif len(toks) > 1 and re.fullmatch(r"[A-ZÀ-Ý.\-]{1,4}", toks[-1]):
            people.append((" ".join(toks[:-1]), toks[-1]))  # "Stroop JR" style
        else:
            people.append((part, ""))
    return people


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "curation" / "zotero" / "bci_atlas_literature.rdf"))
    args = ap.parse_args()

    with open(ROOT / "curation" / "literature.csv", encoding="utf-8-sig", newline="") as fh:
        refs = list(csv.DictReader(fh))
    fam = {t["prefix"]: t for t in read_yaml(ROOT / "taxonomy" / "families.yaml")["terms"]}

    paradigms: dict[str, set[str]] = defaultdict(set)
    for r in refs:
        for p in re.split(r"[;,\s]+", r.get("paradigms") or ""):
            if p:
                paradigms[r["ref_id"]].add(p)
    with open(ROOT / "curation" / "paradigm_literature.csv", encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            paradigms[row["ref_id"]].add(row["proposed_id"])

    coll: dict[tuple[str, str], set[str]] = defaultdict(set)  # (top, sub) -> ref ids
    tags: dict[str, set[str]] = defaultdict(set)
    for r in refs:
        rid = r["ref_id"]
        for p in paradigms[rid]:
            f = fam.get(p.split("-")[0])
            if f:
                coll[("01 范式族", f"{f['prefix']} {f['zh']}")].add(rid)
                tags[rid].add(p)
        if r.get("qa_flag"):
            tags[rid].add(f"qa:{r['qa_flag']}")
        for v in (r.get("found_via") or "").split(";"):
            if v:
                tags[rid].add(f"via:{v}")
    by_doi = {r["doi"].lower(): r["ref_id"] for r in refs if r.get("doi")}
    knowledge: list[tuple[str, str, dict]] = []  # (kind, id, source)
    for path in sorted((ROOT / "knowledge" / "markers").glob("*.yaml")):
        d = read_yaml(path)
        for x in (d.get("generators") or []) + (d.get("indexes") or []):
            knowledge += [("marker", d["id"], src) for src in x.get("sources") or []]
    for name in ("regions", "constructs"):
        for t in read_yaml(ROOT / "knowledge" / f"{name}.yaml")["terms"]:
            knowledge += [("term", t["id"], src) for src in t.get("sources") or []]
    for kind, kid, src in knowledge:
        rid = by_doi.get((src.get("doi") or "").lower())
        if not rid:
            continue
        coll[("02 标记物（知识层）", kid) if kind == "marker" else ("03 词表（脑区与构念）", "")].add(rid)
        tags[rid].add(kid)
    linked = set().union(*coll.values()) if coll else set()
    unlinked = {r["ref_id"] for r in refs} - linked
    if unlinked:
        coll[("04 未关联", "")] = unlinked

    out = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:z="http://www.zotero.org/namespaces/export#"'
        ' xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/"'
        ' xmlns:bib="http://purl.org/net/biblio#" xmlns:foaf="http://xmlns.com/foaf/0.1/"'
        ' xmlns:prism="http://prismstandard.org/namespaces/1.2/basic/">',
    ]
    e = lambda s: escape(str(s), {'"': "&quot;"})  # noqa: E731
    for r in refs:
        v = split_venue(r.get("venue") or "")
        is_article = bool(v["journal"])
        out.append(f'  <bib:{"Article" if is_article else "Document"} rdf:about="#{r["ref_id"]}">')
        out.append(f'    <z:itemType>{"journalArticle" if is_article else "document"}</z:itemType>')
        if is_article:
            out.append("    <dcterms:isPartOf><bib:Journal>")
            out.append(f"      <dc:title>{e(v['journal'])}</dc:title>")
            if v["volume"]:
                out.append(f"      <prism:volume>{e(v['volume'])}</prism:volume>")
            if v["issue"]:
                out.append(f"      <prism:number>{e(v['issue'])}</prism:number>")
            out.append("    </bib:Journal></dcterms:isPartOf>")
        people = split_authors(r.get("authors") or "")
        if people:
            out.append("    <bib:authors><rdf:Seq>")
            for sur, given in people:
                out.append(f"      <rdf:li><foaf:Person><foaf:surname>{e(sur)}</foaf:surname>"
                           f"{f'<foaf:givenName>{e(given)}</foaf:givenName>' if given else ''}</foaf:Person></rdf:li>")
            out.append("    </rdf:Seq></bib:authors>")
        out.append(f"    <dc:title>{e(r.get('title') or '')}</dc:title>")
        if r.get("year"):
            out.append(f"    <dc:date>{e(r['year'])}</dc:date>")
        if v["pages"]:
            out.append(f"    <bib:pages>{e(v['pages'])}</bib:pages>")
        if r.get("doi"):
            out.append(f"    <dc:identifier>DOI {e(r['doi'])}</dc:identifier>")
        if r.get("url"):
            out.append(f"    <dc:identifier><dcterms:URI><rdf:value>{e(r['url'])}</rdf:value></dcterms:URI></dc:identifier>")
        extra = [f"Atlas-ID: {r['ref_id']}"] + ([f"PMID: {r['pmid']}"] if r.get("pmid") else [])
        out.append(f"    <dc:description>{e(chr(10).join(extra))}</dc:description>")
        for t in sorted(tags[r["ref_id"]]):
            out.append(f"    <dc:subject>{e(t)}</dc:subject>")
        out.append(f'  </bib:{"Article" if is_article else "Document"}>')

    tops = sorted({t for t, _ in coll})
    for i, top in enumerate(tops):
        subs = sorted(s for t, s in coll if t == top and s)
        out.append(f'  <z:Collection rdf:about="#top{i}">')
        out.append(f"    <dc:title>{e(top)}</dc:title>")
        for j, _ in enumerate(subs):
            out.append(f'    <dcterms:hasPart rdf:resource="#top{i}_{j}"/>')
        for rid in sorted(coll.get((top, ""), ())):
            out.append(f'    <dcterms:hasPart rdf:resource="#{rid}"/>')
        out.append("  </z:Collection>")
        for j, sub in enumerate(subs):
            out.append(f'  <z:Collection rdf:about="#top{i}_{j}">')
            out.append(f"    <dc:title>{e(sub)}</dc:title>")
            for rid in sorted(coll[(top, sub)]):
                out.append(f'    <dcterms:hasPart rdf:resource="#{rid}"/>')
            out.append("  </z:Collection>")
    out.append("</rdf:RDF>")

    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    n_sub = sum(1 for _, s in coll if s)
    print(f"wrote {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}: {len(refs)} items, "
          f"{len(tops)} top collections, {n_sub} sub-collections, {len(unlinked)} unlinked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
