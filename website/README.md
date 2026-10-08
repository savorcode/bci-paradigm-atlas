# BCI Paradigm Atlas project page

Project presentation website: https://savorcode-website.vercel.app/

This static site reuses the SavorCode visual identity, navy/white palette, responsive layout, and continuous smoke–neural impulse–apple animation. It presents the public atlas, links directly to its source entries and methodology, and distinguishes the open atlas from the planned Paradigm Factory platform.

## Preview

From this directory, run `python3 -m http.server 8890 --bind 127.0.0.1` and open http://127.0.0.1:8890/. No build step or dependencies are required. Asset URLs are relative so the site also works under a project subpath.

## Publish

The existing Vercel project is `savorcode-website`. Deploy this directory only. Do not publish the repository root, research platform, local credentials, or curation workspaces. Local Vercel project settings and environment files are excluded from version control.

The homepage numbers describe the **v0.1.0 / 2026-10-08** release, not live counters. Update the version, counts, evidence-status note, and release link together when a new release is published. All entries remain draft in this version; bibliographic checking does not establish content verification.

## Checks

Validate JavaScript syntax, relative asset paths, local anchors and GitHub source paths. Preview desktop and narrow mobile widths, exercise each example tab, and preserve animation pause, reduced-motion, and offscreen behavior. The hero animation is artistic and does not represent measured data.

Brand artwork and fonts are supplied by SavorCode. Repository licenses do not grant trademark rights to the SavorCode identity.

## Editorial scope

The page introduces **BCI Paradigm Atlas**, not the company service offering. The hero title is 脑机范式图谱. Sections cover project motivation, the two-layer data model, real Oddball/MI/SSVEP records, all 12 families, validation and export usage, evidence grading and review status, version roadmap, and contribution instructions. Sources: README.zh-CN.md, docs/methodology.zh-CN.md, taxonomy/families.yaml and evidence_grades.yaml, the linked paradigm/marker YAML records, scripts/build_graph.py, CONTRIBUTING.md, and the v0.1.0 release/coverage reports. Paradigm Factory is only described in a brief relationship note. Hero rendering and motion controls remain unchanged.
