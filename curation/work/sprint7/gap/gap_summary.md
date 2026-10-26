# Gap analysis - sprint 7 (2026-10-17)

Purpose: a ranked list of experimental paradigms that are not yet in the atlas, as the input to the next collection round.

Compared against: `paradigms/_classes.yaml` (284 classes, names and aliases), all concrete paradigm files (names, aliases, variant names), `curation/candidates.csv` including rows marked 暂缓 / 排除 / 并入, and decisions D-009, D-010, D-022, D-023, D-058, D-060, D-065, D-078 and D-079.

Files in this folder:

| File | Content |
|---|---|
| `gap_candidates.csv` | 54 qualifying candidates, ranked |
| `gap_excluded.csv` | 316 items judged not to qualify, with reasons (questionnaires, behaviour-only tests, umbrella terms, items blocked by earlier decisions) |
| `cogatlas_scan.csv` | decision for every Cognitive Atlas task scanned (852 rows) |
| `search_log.md` | catalogue requests and web searches |

## 1. Cognitive Atlas scan

| | Tasks |
|---|---|
| Listed by Cognitive Atlas (header count) | 857 |
| Retrieved and judged | 852 |
| Covered by an existing class or concrete paradigm | 481 |
| Mapped to a new gap candidate | 70 (48 candidates) |
| Questionnaire, rating scale, interview or test battery | 184 |
| Behaviour-only test (no marker under the D-023 standard) | 74 |
| Umbrella label, design manipulation or method | 42 |
| Non-human method | 1 |

Of the 551 entries that describe an experimental paradigm (all entries minus questionnaires, behaviour-only tests, umbrella terms and the non-human method), 481 (87 %) are already covered. Matching was by name, alias and mechanism; for example "cups task" and "devil's task" were matched to the risk classes, "Sternberg Recent Probes" to MEM-RPT, and "word stem completion" to MEM-RPRIM.

## 2. Candidates per family

| Family | 核心 | 相关 | 基础 | Total |
|---|---|---|---|---|
| perception | 4 | 4 | 14 | 22 |
| control | 0 | 0 | 6 | 6 |
| motor | 3 | 1 | 1 | 5 |
| emotion | 0 | 2 | 2 | 4 |
| state | 1 | 1 | 1 | 3 |
| social | 0 | 1 | 2 | 3 |
| error | 0 | 0 | 3 | 3 |
| language | 0 | 0 | 3 | 3 |
| memory | 0 | 1 | 1 | 2 |
| stimulation | 0 | 1 | 1 | 2 |
| steady_state | 0 | 1 | 0 | 1 |
| imagery | 0 | 0 | 0 | 0 |
| **Total** | **8** | **12** | **34** | **54** |

By source: Cognitive Atlas 48, BNCI Horizon 2020 2, OpenNeuro 1, reviews 3. MOABB contributed no new class: all its paradigm groups (motor imagery, P300/ERP, SSVEP, c-VEP, resting state) are covered.

Priority: 5 candidates at priority 1, 14 at priority 2, 35 at priority 3.

Ranking order: BCI relevance first (核心, then 相关, then 基础), then use in public datasets, then the approximate number of recent studies.

## 3. Recommended for this round (24)

Balanced across families; 8 are 核心.

| Rank | ID | Name | BCI relevance | Priority |
|---|---|---|---|---|
| 1 | MOT-BRAKE | Emergency braking intention during simulated driving | 核心 | 1 |
| 2 | PER-MUSAT | Selective attention to one instrument in polyphonic music | 核心 | 1 |
| 3 | PER-FBA | Feature-based attention | 核心 | 1 |
| 4 | STA-PROBE | Irrelevant-probe workload assessment | 核心 | 1 |
| 5 | MOT-KMI | Motor imagery of kinetic and kinematic parameters | 核心 | 1 |
| 6 | PER-GAZSEL | Gaze-based selection intention | 核心 | 2 |
| 7 | PER-IDEAF | Inattentional deafness to auditory alarms | 核心 | 2 |
| 8 | MOT-SWAL | Swallowing (executed and imagined) | 核心 | 2 |
| 9 | PER-SURR | Visual surround suppression | 相关 | 2 |
| 10 | PER-TONIC | Tonic pain | 相关 | 2 |
| 11 | EMO-CREAC | Drug and food cue reactivity | 相关 | 2 |
| 13 | MEM-VTWM | Vibrotactile frequency discrimination and working memory | 相关 | 2 |
| 14 | MOT-SATT | Sensory attenuation of self-generated stimuli | 相关 | 2 |
| 15 | SOC-DECEP | Instructed deception | 相关 | 2 |
| 16 | SSR-BINB | Binaural beat stimulation | 相关 | 3 |
| 17 | EMO-FRUST | Frustration induction | 相关 | 3 |
| 18 | PER-SMMN | Somatosensory mismatch negativity | 相关 | 3 |
| 19 | STA-GAME | Video-game play | 相关 | 3 |
| 20 | STM-TACEP | Mechanical tactile evoked potentials | 相关 | 3 |
| 24 | STA-RESP | Respiratory challenge (hyperventilation, breath-hold) | 基础 | 2 |
| 30 | ERR-PROTO | Category learning (prototype distortion) | 基础 | 3 |
| 31 | CTL-NEGP | Negative priming | 基础 | 3 |
| 33 | CTL-BEADS | Information sampling before decision (beads task) | 基础 | 3 |
| 47 | LAN-DISC | Discourse coherence | 基础 | 3 |

Family spread: perception 7, motor 4, state 3, emotion 2, control 2, memory 1, social 1, steady_state 1, error 1, language 1, stimulation 1. Rank 12 (PER-INTMOD) was left out only to keep perception from dominating; it is the first substitute.

## 4. Coverage caveats

1. **Cognitive Atlas retrieval.** The Cognitive Atlas API returns the whole task list as one JSON document, and it could only be read up to the entry "pantomime task" (about 160 tasks). The scan therefore used the A-Z browse pages. Their header gives 857 tasks; 852 were retrieved (pages H and S each list one entry fewer than their header count, one entry on the full list has no name, and the other two could not be traced). The 5 missing entries were not judged.
2. **Name-based judgement.** Coverage was judged from task names (and the atlas's names, aliases and variants), not from each Cognitive Atlas definition. Ambiguous names such as "categorization task", "image monitoring" or "selective attention task" were treated as umbrella terms or mapped to the nearest class, and some covered judgements could be challenged at review. The decision for each task is in `cogatlas_scan.csv`.
3. **Cognitive Atlas bias.** The catalogue is weighted toward fMRI tasks and clinical instruments; about a third of its entries are questionnaires or test batteries. It has almost no BCI paradigms, so the 核心 candidates come mainly from BNCI Horizon 2020 and the reviews.
4. **OpenNeuro.** The OpenNeuro EEG search page loads its results with JavaScript and returned no content; its query interface could not be reached. Only the EEGDash catalogue (which mirrors OpenNeuro and NEMAR) could be read, and it gives category labels rather than task names. The OpenNeuro check is therefore incomplete; only the Healthy Brain Network task set (surround suppression, contrast change detection, sequence learning, symbol search, movies, rest) was checked task by task.
5. **MOABB and BNCI** list datasets, not new paradigm types; apart from emergency braking and the music BCI, their entries were covered or are concrete-level variants (for example the Center Speller layout).
6. **Reviews.** Three reviews were used (Tai et al. 2024; Wang, Jiang & Li 2025, arXiv preprint; Alimardani & Hiraki 2020), plus a systematic review for binaural beats. Most paradigms they name are already in the atlas or are hybrids handled by D-022.
7. **Imagery family.** No new imagery class was found: every imagery task in the catalogues maps to IMG-* or MOT-MI. MOT-KMI is placed in motor because it is a motor-imagery configuration.
8. **Leads without a catalogue source.** These were noted during the work but are not in the ranked list, because none of the scanned catalogues or reviews lists them: two-way communication with lucid dreamers during REM sleep (Konkoly et al. 2021, doi 10.1016/j.cub.2021.01.026; closest STA-DREAM), prepulse inhibition, loudness dependence of auditory evoked potentials, peripersonal-space (audio-tactile looming) tasks, vection, stereoscopic-disparity VEP, cardiac-cycle-timed stimulation, figurative-language ERPs and responsive neurostimulation for epilepsy. They can be added if a later scan finds a source.
9. **Pending decisions.** EMO-ECONF (emotional conflict task, Etkin et al. 2006) was approved as a new class in D-065 but has not been built; it is not repeated here. PER-SMMN may end up as a PER-MMN concrete paradigm if D-060 (stimulus-modality change is criterion 2) is confirmed; STM-TACEP raises the same question for STM-SEP.
10. **Not re-proposed.** Items excluded or held by D-009, D-010, D-022, D-023 and D-078 (ICMS, electrical stimulation mapping, phosphenes, hybrid BCI, useful field of view, digit-symbol substitution, self-paced reading) are listed in `gap_excluded.csv` with their decision references.
11. **Short codes.** All proposed shorts were checked against the 284 class IDs, every ID in `candidates.csv` and the sprint work folders; none is in use. CUE and HIER were avoided because PER-CUE and LAN-HIER exist.
