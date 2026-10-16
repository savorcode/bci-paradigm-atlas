# Worklog - sprint 6, group P1 (curator_b, 2026-10-16)

Assignment: STM-ICMS, STM-PHOS, STM-SCS, STM-RTMS, STM-TRNS, STM-ESM, MOT-FES, MOT-HYB.

## Outcome

| Provisional ID | Result | Files |
|---|---|---|
| STM-ICMS | class created | STM-ICMS-001 (open-loop percept mapping / psychophysics, Flesher 2016), STM-ICMS-002 (closed-loop tactile feedback in BCI arm control, Flesher 2021) |
| STM-PHOS | class created | STM-PHOS-001 (single-electrode phosphene mapping, Brindley & Lewin 1968), STM-PHOS-002 (dynamic sequential stimulation for form vision, Beauchamp 2020) |
| STM-RTMS | class created | STM-RTMS-001 (regular rTMS, Pascual-Leone 1994), STM-RTMS-002 (theta-burst, Huang 2005) |
| STM-TRNS | class created | STM-TRNS-001 (Terney 2008) |
| STM-ESM | class created | STM-ESM-001 (sensorimotor mapping, Penfield & Boldrey 1937), STM-ESM-002 (language mapping during naming, Ojemann 1989) |
| STM-SCS | not created - proposal | MOT-ATT concrete paradigm (proposals.csv) |
| MOT-FES | not created - proposals | MOT-MI (and possibly MOT-ATT) concrete paradigms (proposals.csv) |
| MOT-HYB | not created - proposals | `Hybrid:` variants per D-022 (proposals.csv) |

Class entries: classes_new.yaml (5 classes). Validation: `python3 scripts/validate.py` reports only the expected "class not registered" errors for the 9 new files; a trial merge of classes_new.yaml into a copy of the registry validates with 0 problems.

## Duplicate checks

Searched ids, names and aliases in paradigms/ and paradigms/_classes.yaml for: microstim, ICMS, phosphen, visual prosthes, spinal, rTMS, theta burst, random noise, tRNS, stimulation mapping, functional electrical, FES, hybrid, brain-spine, intracortical.

- No existing class or concrete paradigm covers ICMS, phosphenes, rTMS/TBS, tRNS or stimulation mapping. Neighbours checked: STM-TEP (single-pulse TMS-EEG, no conditioning), STM-PAS (paired peripheral + TMS), STM-PHTMS (EEG-phase-triggered TMS), STM-TMSFMRI (concurrent BOLD), STM-TDCS (constant current), STM-TACS (sinusoidal current), STM-CCEP (single-pulse electrical stimulation with recorded responses). rTMS and tRNS are distinct conditioning protocols at the same granularity as the existing tDCS/tACS/PAS classes.
- Earlier decisions found during the check (important, see open issues): candidate STM-ICMS-001 was excluded by D-009 and candidate STM-ECS-001 (= electrical stimulation mapping) by D-010, both for inclusion criterion 3 (behavioural/perceptual read-out); STA-HYB-001 (hybrid BCI) was deferred by D-022.
- STM-SCS (brain-spine interface): the decoded signal is cortical activity of attempted leg movement; spinal stimulation is the effector. Same markers and construct as MOT-ATT, so by the class rule (methodology section 1) it is a MOT-ATT configuration (criteria 1 and 4), not a stimulation class. Proposed as MOT-ATT-004.
- MOT-FES: BCI-triggered FES uses SMR ERD of imagined or attempted movement (MOT-MI / MOT-ATT markers); FES is the output and feedback. Configuration-level difference only (criterion 4). Proposed as concrete paradigms under MOT-MI (Pfurtscheller 2003 foot-MI switch -> grasp FES, close to MOT-MI-004) and MOT-MI or MOT-ATT (Biasiucci 2018 stroke rehabilitation). Existing related protocol: MOT-MRCP-003 (MRCP detection triggering peripheral nerve stimulation). Observation: Pfurtscheller 2003 is earlier than the MOT-MI-004 first_source (2009).
- MOT-HYB: D-022 (confirmed) rules that hybrid BCIs are combinations of existing paradigms, recorded as `Hybrid:` variants in each component; no new marker or construct. No `Hybrid:` variant has been written anywhere yet. Proposed variants for SSR-SSVEP-001 / MOT-MI-001 (Allison 2010) and PER-ODD-001 / SSR-SSVEP-008 (Panicker 2011).

## ID choices

- STM-ICMS kept: it denotes the same paradigm as the excluded candidate STM-ICMS-001, so reinstating it does not give the identifier a new meaning. If the maintainer reads D-009 "ID retained, not reused" strictly, rename the class (e.g. STM-ICMSS) before merge; no other file references the ID.
- STM-ESM used instead of the old candidate ID STM-ECS-001, which stays void.
- STM-PHOS, STM-RTMS, STM-TRNS: provisional IDs kept (unused).

## Decisions on content

- -002 files created where D-057 criteria clearly apply: ICMS closed loop (criterion 4, 3), PHOS dynamic sequential coding (criterion 2, 1), TBS (criterion 2), ESM language mapping during naming (criteria 1, 3).
- Origins from MEP studies (rTMS, TBS, tRNS) accepted under D-031; "First neural recording" given for rTMS (Esser et al. 2006), open for TBS and tRNS.
- Precursors named in reviews but not retrieved as records are listed in notes only, not cited: Foerster 1929 (phosphenes), Bartholow 1874 / Sciamanna 1882 / Krause / Foerster (ESM), early rTMS speech-arrest work.
- Protocol numbers for ICMS-002 and PHOS-002 come from the bioRxiv preprints (records retrieved, linked as preprints of the journal versions); flagged in notes for checking against the published methods.
- One remembered DOI for Terney et al. 2008 resolved to a different paper and was discarded (search_log W04).

## Markers

- Used (all existing): MK.motor_cortical_spiking (ICMS, closest), MK.BOLD_visual_cortex (PHOS, closest), MK.TEP (RTMS), MK.tES_power_aftereffect (TRNS), MK.CCEP and MK.high_gamma (ESM, closest).
- Requested: MK.cortical_stimulation_evoked_response (ICMS, PHOS), MK.afterdischarge (ESM) - marker_requests.csv.
- MK.tES_power_aftereffect description names only tACS/tDCS; should be extended to tRNS (marker owner).

## Open issues for the maintainer

1. D-009 and D-010 exclusions: the sprint 6 assignment reinstates ICMS and stimulation mapping. A decision record superseding D-009/D-010 (and stating how inclusion criterion 3 applies to "writing-in" paradigms whose read-out is perceptual or behavioural) is needed before the STM-ICMS and STM-ESM files are merged. The same question applies to STM-PHOS, which was never a candidate but has the same perceptual read-out.
2. Marker coverage for writing-in paradigms (requests above); current closest markers are placeholders.
3. Confirm that STM-SCS, MOT-FES and MOT-HYB should be handled as proposals (class rule and D-022) rather than as classes.
4. Esser et al. 2006: year 2005 in OpenAlex vs 2006 print volume.
5. Pfurtscheller 2010 "The hybrid BCI": registry records list one author only.
6. No public datasets were verified for any of the new paradigms; datasets fields left out.
