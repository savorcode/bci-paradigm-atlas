# Search log - sprint 7 gap analysis (2026-10-17)

Web searches: 10 of 15 allowed. Catalogue pages and APIs were read directly; each request is listed below.

## Catalogue requests

| # | Source | Request | Outcome |
|---|---|---|---|
| C01 | Cognitive Atlas API | `https://www.cognitiveatlas.org/api/v-alpha/task` | One JSON document holding the full task list; could be read only up to "pantomime task" (about 160 entries). Requests starting at later character offsets also stopped there. Not used for the count; used to confirm task IDs |
| C02 | Cognitive Atlas task browse pages | `https://www.cognitiveatlas.org/tasks/a` to `/tasks/z` (26 pages) | Read in full. Counts per letter: A 48, B 36, C 86, D 37, E 31, F 36, G 18, H 17, I 31, J 2, K 5, L 22, M 65, N 46, O 26, P 80, Q 0, R 48, S 99, T 40, U 6, V 30, W 36, X 0, Y 2, Z 3 |
| C03 | Cognitive Atlas full list | `https://www.cognitiveatlas.org/tasks` | Header total 857; two entries beginning with a digit ("2-stage decision task", "2nd-order rule acquisition") and one entry with no name. Total retrieved: 852 |
| C04 | MOABB | `https://neurotechx.github.io/moabb/dataset_summary.html` | Tables for motor imagery (18 datasets), P300/ERP (16), SSVEP (7), c-VEP (6), resting state (3) and compound datasets (5). Dataset names were not included in the page text; paradigm groups and class counts were. All groups covered |
| C05 | BNCI Horizon 2020 | `https://bnci-horizon-2020.eu/database/data-sets` | 32 data sets (001-2014 to 002-2025). New: 002-2016 emergency braking during simulated driving; 006-2015 music BCI. The rest are covered or concrete-level variants |
| C06 | OpenNeuro | `https://openneuro.org/search/modality/eeg` | Page content loads with JavaScript; no dataset titles or task names returned |
| C07 | OpenNeuro query interface | GraphQL request for EEG datasets and task names | Request failed |
| C08 | EEGDash catalogue (mirror of OpenNeuro and NEMAR) | `https://eegdash-readme.static.hf.space/index.html` | Category counts only (visual 300, auditory 59, multimodal 35, resting 22, motor 17, tactile 16, sleep 13, anaesthesia 4, unclassified 207); few task names |
| C09 | EEGDash dataset summary | `https://eegdash.org/dataset_summary.html` | 997 datasets with stimulus and category labels, not task names; used only to confirm category spread |
| C10 | Review (Wang, Jiang & Li 2025) | arXiv 2503.16471 (PDF) | Read; interaction paradigms listed (classic, hybrid, visual, auditory, tactile, olfactory, passive, speech and handwriting). Nothing new beyond hybrids (D-022) |
| C11 | Review (Tai et al. 2024) | Frontiers article page, doi 10.3389/fnins.2023.1345961 (the PMC copy was blocked by a browser check and the EPUB link returned a server error) | Read; new: motor imagery of kinetic/kinematic parameters (force, speed). Coordinated multi-limb imagery is a MOT-MI concrete variant |
| C12 | Review (Alimardani & Hiraki 2020) | Frontiers PDF, doi 10.3389/frobt.2020.00125 | Read; passive-BCI tasks. New: auditory attentional errors in flight (inattentional deafness). Rest covered (ErrP, workload, emotion elicitation) |
| C13 | Preprint on multisensory BCI protocols | arXiv 2507.18401 | Not a paradigm review; bimodal and trimodal P300/SSEP variants only. Not used |

## Web searches

| # | Query | Outcome |
|---|---|---|
| W01 | OpenNeuro EEG dataset list tasks BIDS "task-" NEMAR | NEMAR paper and portal; no static task listing |
| W02 | EEGDash dataset summary OpenNeuro EEG datasets table tasks | EEGDash catalogue page (C08) |
| W03 | eegdash.org dataset_summary "ds00" task names list | Single-dataset pages only; led to C09 |
| W04 | review of EEG-based brain-computer interface paradigms 2024 new paradigms beyond MI P300 SSVEP | Wang et al. 2025 (C10); Tai et al. 2024; Abiri et al. 2019 (older, not used) |
| W05 | "Brain-computer interface paradigms and neural coding" Frontiers in Neuroscience 2024 | Article page for Tai et al. 2024 (C11) |
| W06 | passive brain-computer interface review neuroadaptive paradigms workload auditory probe implicit control 2023 2024 | Alimardani & Hiraki 2020 (C12); Zander & Kothe passive BCI papers |
| W07 | 2025 review emerging non-invasive BCI paradigms visual imagery olfactory tactile auditory neural engineering | Non-invasive BCI state-of-the-art review (PMC copy, not readable); arXiv 2507.18401 (C13) |
| W08 | eye-brain-computer interface gaze dwell intention EEG fixation-related negativity review hybrid gaze BCI | Shishkin et al. 2016, doi 10.3389/fnins.2016.00528 (empirical); FRP-based BMI work. Cited in the why_new text of PER-GAZSEL |
| W09 | "Binaural beats to entrain the brain" systematic review EEG PLOS ONE 2023 doi | Ingendoh et al. 2023, PLOS ONE (PMID 37205669). DOI 10.1371/journal.pone.0286023 recalled and matching the PMC record title; to be checked against the Crossref API before the class is built |
| W10 | real-time dialogue between experimenters and dreamers during REM sleep Konkoly 2021 Current Biology lucid dreaming EEG | Konkoly et al. 2021 confirmed. Empirical paper, not a catalogue entry; recorded as a lead in the summary, not ranked |

## Local comparison

- Class list: 284 terms in `paradigms/_classes.yaml` (IDs, English and Chinese names, aliases).
- Concrete paradigms: 428 files under `paradigms/<family>/` (names, aliases, variant names).
- Candidates: 312 rows in `curation/candidates.csv` (284 收录, 5 暂缓, 3 排除, 20 并入).
- Used short codes collected from classes, candidates and the sprint work folders (316 IDs) to keep proposed shorts unique.
- Keyword checks against all paradigm files confirmed that none of the 54 candidates is described in an existing class, concrete paradigm or variant.

## Bibliographic checks still to do

None of the DOIs in `gap_candidates.csv` has been checked against the Crossref API in this pass. The source DOIs for the three reviews come from the publisher pages read in C11 and C12 and from the arXiv record (C10, no DOI); the binaural-beat review DOI comes from the search result (W09). First sources for each new class will be collected and checked in the collection round.
