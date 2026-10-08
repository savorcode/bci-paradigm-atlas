# BCI Paradigm Atlas project page

Project presentation website: https://savorcode-website.vercel.app/

This static site reuses the SavorCode visual identity, navy/white palette, responsive layout, and animated knowledge-graph hero. It presents the public atlas, links directly to its source entries and methodology, and distinguishes the open atlas from the planned Paradigm Factory platform.

## Preview

From this directory, run `python3 -m http.server 8890 --bind 127.0.0.1` and open http://127.0.0.1:8890/. No build step or dependencies are required. Asset URLs are relative so the site also works under a project subpath.

## Publish

The existing Vercel project is `savorcode-website`. Deploy this directory only. Do not publish the repository root, research platform, local credentials, or curation workspaces. Local Vercel project settings and environment files are excluded from version control.

The homepage numbers describe the **v0.1.0 / 2026-10-08** release, not live counters. Update the version, counts, evidence-status note, and release link together when a new release is published. All entries remain draft in this version; bibliographic checking does not establish content verification.

## Checks

Validate JavaScript syntax, relative asset paths, local anchors and GitHub source paths. Preview desktop and narrow mobile widths, exercise each example tab, and preserve animation pause, reduced-motion, and offscreen behavior. The hero animation is artistic and does not represent measured data.

Brand artwork and fonts are supplied by SavorCode. Repository licenses do not grant trademark rights to the SavorCode identity.

## Editorial scope

The page introduces **BCI Paradigm Atlas**, not the company service offering. The hero title is 脑机范式图谱. Sections cover project motivation, the two-layer data model, real Oddball/MI/SSVEP records, all 12 families, validation and export usage, evidence grading and review status, version roadmap, and contribution instructions. Sources: README.zh-CN.md, docs/methodology.zh-CN.md, taxonomy/families.yaml and evidence_grades.yaml, the linked paradigm/marker YAML records, scripts/build_graph.py, CONTRIBUTING.md, and the v0.1.0 release/coverage reports. Paradigm Factory is only described in a brief relationship note. Motion pause, reduced-motion and offscreen controls are retained.

## Open-source community interface

Section 03 uses horizontal tabs, a shared two-column inspector, and a searchable catalog of all 404 active protocols. The search filters by name, ID, alias, marker, family, and recording modality, with six results per page. Rebuild `website/catalog.json` using `python scripts/build_website_catalog.py` after atlas source changes; the generator reuses `scripts/atlas.py`. Keep version labels aligned with the release represented by the data.

Quickstart commands can be copied. Contribution links open the existing paradigm Issue template and contribution guide. Subscription links lead to GitHub Watch setup and the main-branch Atom commit feed; users complete Watch on GitHub themselves. The page does not collect email addresses or claim a subscription has been created.

Design references: LeRobot on Hugging Face (https://huggingface.co/lerobot) and Nerfstudio on GitHub (https://github.com/nerfstudio-project/nerfstudio). The navigation/action hierarchy emphasizes trying, using and contributing. Brand assets and the hero layout are preserved.

## Knowledge-graph hero

The unlabeled automatic canvas animation uses a curated v0.1.0 subset of real paradigm → marker, region → marker and marker → construct relationships embedded in `main.js`. Circles, hubs, squares and diamonds distinguish entity kinds. Curved links carry quiet pulses; the force-derived layout gently drifts in depth. Positions, sizes and motion are artistic, not measurements, evidence strengths or a complete graph. No pointer interaction is required.
