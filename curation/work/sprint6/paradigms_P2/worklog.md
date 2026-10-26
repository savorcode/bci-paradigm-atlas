# Worklog - sprint 6, group P2 (perception, attention and memory), 2026-10-16

Curators: curator_a (perception: PER-TIME, PER-CROWD, PER-AUDLOC), curator_d (memory: MEM-PR, MEM-AI, MEM-CSPAN), curator_c (control: CTL-TMT, CTL-NUM).

## Classes created (8 classes, 11 concrete paradigms)

| Class | Family | Concrete | First source |
|---|---|---|---|
| PER-TIME | perception | -001 TOJ; -002 audiovisual SJ | Hirsh & Sherrick 1961; -002 Stone et al. 2001 |
| PER-CROWD | perception | -001 peripheral letter crowding | Bouma 1970 |
| PER-AUDLOC | perception | -001 free-field sound localization | Lord Rayleigh 1907 |
| MEM-PR | memory | -001 Sperling tone-cued partial report | Sperling 1960 |
| MEM-AI | memory | -001 AB-BC-AC with object pairs | Preston et al. 2004 |
| MEM-CSPAN | memory | -001 reading span; -002 operation span | Daneman & Carpenter 1980; -002 Turner & Engle 1989 |
| CTL-TMT | control | -001 Parts A and B | Reitan 1958 |
| CTL-NUM | control | -001 digit comparison; -002 parity judgement (SNARC) | Moyer & Landauer 1967; -002 Dehaene et al. 1993 |

## Duplicate checks

Searched paradigm ids, names and aliases in all paradigm files and in the class registry for: temporal order, simultaneity, crowding, sound localization, spatial hearing, azimuth, partial report, iconic, Sperling, associative inference, transitive, AB-BC, operation/complex/reading span, trail making, number comparison, numerical distance, SNARC, numerosity.

- No existing class or concrete paradigm covers any of the eight.
- PER-AUDLOC: auditory spatial P300 BCI (AMUSE) exists as PER-ODD-008, and location deviants are part of the multi-feature MMN (PER-MMN-003). Both are passive or oddball designs; the active localization judgement is new, so the class was created with a note. While checking, found that Schreuder, Blankertz & Tangermann 2010 (PLoS ONE) predates the PER-ODD-008 first_source (2011); recorded in proposals.csv for the owner.
- PER-CROWD vs CTL-FLK (Eriksen flanker): different mechanism (recognition limit vs response conflict); no overlap.
- MEM-PR vs MEM-CD (change detection, incl. retro-cue): different store (iconic vs visual working memory); kept separate.
- MEM-AI vs MEM-PA (paired associates): MEM-PA tests direct pairs only; the defining A-C inference is new.
- MEM-CSPAN vs MEM-DS (digit span) and MEM-SB: simple span and memory scanning have no interleaved processing task.
- CTL-TMT vs CTL-SW (task switching): shared construct (set shifting), different procedure (self-paced timed test vs cued RT trials).

## Decisions

- Provisional ID MEM-OSPAN renamed MEM-CSPAN (complex span), so that the earliest complex span task (reading span, 1980) can be -001 and operation span (1989) -002 under D-057 (criterion 2, processing task). MEM-CSPAN is unused.
- PER-TIME-002 (SJ) created as a separate serial number: the response classes differ (simultaneous/not vs which first), criterion 1.
- CTL-NUM-002 (SNARC parity judgement) created: task and class set differ (odd/even with reversed hand mapping), criterion 1.
- Kept as variants, flagged for the maintainer in proposals.csv: automated OSPAN (possible criterion 4, feedback), vernier crowding with EEG (possible criterion 2), comparison with a fixed standard (possible criterion 2). The Ruff et al. 2007 hemifield postcue design is a variant of MEM-PR-001 (two cue classes instead of three rows; possibly criterion 1).
- bci_category is none for all files: none of these paradigms is used as a BCI control paradigm in the retrieved sources; the spatial auditory BCI belongs to PER-ODD-008.
- Origins (D-031): CTL-TMT's true origin (Partington's Pathways Test; Army Individual Test Battery, 1944) has no retrievable record, so Reitan 1958 is used as the standard first source. MEM-AI: Bunsey & Eichenbaum 1996 (rats, with a human comparison) is the earlier transitive association design; Preston et al. 2004 is the first retrieved human AB-BC-AC task and is used. PER-TIME-002: SJ is much older than Stone et al. 2001, but no earlier record was retrieved. PER-AUDLOC: Rayleigh 1907 is partly theoretical; the procedure follows Makous & Middlebrooks 1990.

## Markers

Only existing registry markers used. Provisional links (closest available; noted in each file):
- MK.alpha_posterior (PER-TIME-001): power marker used for an alpha-phase account; MK.prestimulus_alpha_phase requested.
- MK.AV_interaction_ERP (PER-TIME-002): no retrieved study links it to SJ.
- MK.N1_auditory (PER-AUDLOC-001): no localization-specific study retrieved; MK.auditory_spatial_ERP requested.
- MK.BOLD_frontoparietal (CTL-NUM-001): intraparietal involvement, no fMRI study retrieved; MK.P2p_numerical_distance requested.
- MK.LRP (CTL-NUM-002): no retrieved SNARC-LRP study.
- MK.alpha_posterior for MEM-CSPAN-001 (reading span) is inferred from an operation span EEG study.
Supported by retrieved studies: MK.N1_visual (Chicherov et al. 2014), MK.BOLD_frontoparietal and MK.BOLD_visual_cortex for MEM-PR (Ruff et al. 2007), MK.BOLD_hippocampus and MK.BOLD_mPFC (Preston et al. 2004; Zeithamova & Preston 2010), MK.alpha_posterior and MK.frontal_midline_theta for operation span (Scharinger et al. 2017; theta weaker), MK.HbO_prefrontal (Fujiki et al. 2013), MK.BOLD_auditory_cortex (Zatorre et al. 2002).

## Uncertainties

- Several protocol values come from secondary descriptions or general knowledge of the papers and are marked "to be checked" in the files: Sperling exposure and array details; reading span set sizes; automated OSPAN letter duration (800 ms) and time limit (mean + 2.5 SD); TMT 5-minute discontinuation; Makous & Middlebrooks noise-burst duration. Phase durations marked "typical" are not from the first sources.
- Crossref returned HTTP 429 for four DOIs; three were taken from OpenAlex, and Schreuder et al. 2010 succeeded on a later Crossref retry. The OpenAlex record for Ruff et al. 2007 lists the authors in a different order than the published article; the published order is used.
- Fujiki et al. 2013: Crossref and OpenAlex records lack given names for most co-authors; the citation is copied as in the records.
- No public datasets were verified for any of the eight classes; `datasets` omitted.
- validate.py: the only errors in these files are the expected "class not registered in paradigms/_classes.yaml" for the 11 new concrete paradigms. classes_new.yaml was checked against the class schema, and class markers are a superset of their concrete paradigms' markers (D-061).
