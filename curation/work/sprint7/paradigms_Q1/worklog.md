# Worklog - sprint 7, group Q1 (2026-10-17)

Curators: curator_a (perception: PER-GAZSEL, PER-IDEAF), curator_b (motor: MOT-BRAKE, MOT-KMI, MOT-SWAL, MOT-SATT), curator_e (state: STA-PROBE, STA-GAME).

## Result

8 new classes, 12 concrete paradigms. Provisional short codes from the gap list were kept; all were checked against `paradigms/_classes.yaml`, the paradigm files and the sprint 7 work folders and are unused.

| Class | Family | Class origin | Concrete paradigms |
|---|---|---|---|
| MOT-BRAKE | motor | Haufe et al. 2011 | -001 car following, sudden lead-vehicle braking |
| MOT-KMI | motor | Gu et al. 2009 | -001 imagined speed (fast/slow); -002 imagined force load with voice feedback (Wang et al. 2017) |
| MOT-SWAL | motor | Hamdy et al. 1999 | -001 cued water swallowing (PET); -002 swallow imagery vs idle (Yang et al. 2014) |
| MOT-SATT | motor | Schafer & Marcus 1973 | -001 self- vs externally delivered clicks/flashes |
| PER-GAZSEL | perception | Shishkin et al. 2016 | -001 intentional vs spontaneous fixations in a gaze-controlled game |
| PER-IDEAF | perception | Macdonald & Lavie 2011 | -001 critical-trial tone under visual load; -002 auditory alarm oddball in a landing task (Giraudet et al. 2015) |
| STA-PROBE | state | Kramer et al. 1995 | -001 ignored two-tone oddball probes; -002 single-stimulus probes during game play (Allison & Polich 2008) |
| STA-GAME | state | Pellouchoud et al. 1999 | -001 play vs watch vs rest |

`python3 scripts/validate.py`: the only errors in these files are the expected "class not registered in paradigms/_classes.yaml" messages (12). `classes_new.yaml` validates against `schema/paradigm_class.schema.json` when wrapped as a registry file.

## Duplicate and overlap checks

Searched class ids, names, aliases and descriptions in `paradigms/_classes.yaml` and the concrete files for braking, driving, swallowing, attenuation, self-generated, gaze/dwell/Midas, probe, deafness/alarm, game, force, speed and kinetic/kinematic.

- **MOT-BRAKE**: STA-DRV (drowsiness in monotonous driving; STA-DRV-002 continuous PERCLOS labels) and MOT-MRCP (self-paced movement preparation) are related but neither detects an event-triggered braking intention. New class.
- **MOT-KMI**: MOT-MI concrete paradigms are body-part class sets; MOT-FORCE is executed isometric force tracking. Imagined speed/force of one effector is new. Yuan et al. 2010 kept as a parameter variant of -001.
- **MOT-SWAL**: no class covers swallowing (MOT-ME is limb/finger; language classes cover speech articulation). New class.
- **MOT-SATT**: closest is **MOT-IB** (intentional binding), whose class description lists N1 attenuation to self-caused tones as a neural correlate; LAN-SIS (speech only) and PER-OMIT (omissions) also overlap. Created as a separate class because the construct and contrast differ (sensory prediction measured as self vs external response difference, no timing judgement). Flagged for the maintainer: an alternative is to make MOT-IB and MOT-SATT one class with two concrete paradigms.
- **PER-GAZSEL**: LAN-READ uses fixation-related potentials in reading; MOT-SACC records saccade-related activity; PER-CVA covers gaze-independent covert visual attention. New class. Zander et al. 2010 (gaze pointing plus a separate BCI command) is a hybrid in the sense of D-022 and is not used as the origin.
- **PER-IDEAF**: PER-IB is the visual counterpart; STA-PROBE uses ignored probes but does not test awareness. New class.
- **STA-PROBE**: STA-MATB and MEM-NBK manipulate workload without probes; PER-ODD requires attention to the oddball. New class.
- **STA-GAME**: STA-ENG (passive video, ISC) and STA-MATB (fixed battery) differ; ERR-ERRP-004 uses a game only as a vehicle for inserted errors. New class.

No item was skipped as a duplicate, so `proposals.csv` was not needed.

## Decisions and uncertainties

1. **Class origin versus -001 (D-062).** For every class the -001 file carries the class origin. PER-IDEAF's origin (Macdonald & Lavie 2011) is behavioural; its markers come from Molloy et al. 2015 (MEG, listed as a variant of -001) and Giraudet et al. 2015 (-002), following the PER-IB precedent.
2. **Numbering (D-057).** Second numbers were given where the configuration changes clearly: MOT-KMI-002 (criterion 1 force vs speed classes; criterion 4 discrete feedback), MOT-SWAL-002 (criteria 1 and 2: imagery vs execution, animated cue), STA-PROBE-002 (criterion 2: single-stimulus probes instead of an oddball sequence), PER-IDEAF-002 (criteria 2 and 3: repeated alarm oddball in an operational task instead of a single critical-trial tone). Candidates not built: MOT-BRAKE with several braking situations (Kim et al. 2014), MOT-SATT tactile version (Blakemore et al. 1998; no fitting marker), contingent motor-auditory design with motor-only control (no source retrieved), Molloy et al. 2015 repeated-tone design (full text not read), Space Fortress / difficulty-graded game play.
3. **Origins that remain provisional.**
   - MOT-KMI: Gu, Dremstrup & Farina 2009 (Clin Neurophysiol) appeared the same year; whether it used imagined movements was not checked.
   - MOT-SWAL: Zald & Pardo 1999 (PET) and the 1998 conference abstract of Hamdy et al. were not compared; for -002, the 2012 conference paper of the Yang/Guan group and Kober & Wood 2014 (fNIRS) were not retrieved.
   - STA-PROBE: earlier probe-evoked-potential work (1970s-1980s) was not searched; the abstract of Kramer et al. 1995 was not available, so its design is described from two later papers that cite it.
   - STA-GAME: Smith, McEvoy & Gevins 1999 (record only) and the Space Fortress literature (Mane & Donchin 1989) may hold an earlier game-EEG study.
   - MOT-BRAKE and MOT-SATT: the original articles were not read; protocol details come from the BNCI dataset description, a later replication and the bibliographic records.
4. **Missing durations.** Phase durations were filled only where a source that was read states them (MOT-KMI-002, MOT-SWAL-002, STA-PROBE-002, PER-IDEAF-002, PER-GAZSEL analysis window). Other phases carry a note instead of a guessed duration.
5. **Markers.** Only registry markers were used. Stand-ins: MK.CNV for the SPN-like expectancy negativity of PER-GAZSEL (MK.SPN in the registry is the symmetry SPN), MK.BOLD_motor_network for PET rCBF in MOT-SWAL-001, MK.SMR_ERD for MOT-SWAL-002 (the classifier used wavelet features, not an ERD analysis), MK.P3a for the P3 to ignored probes. Two marker requests filed (`marker_requests.csv`).
6. **Bibliographic notes.** Crossref and OpenAlex list only the first author for Gu et al. 2009 (Front Neurosci); the full author list and article number 62 come from the publisher page. Kim et al. 2014 has online year 2014 and issue year 2015 (volume 12); the online year is used. Shishkin et al. 2016 was confirmed through OpenAlex because the Crossref request was rate-limited.
7. **stimulus_modality for MOT-SWAL-001.** `somatosensory` stands for the oral water bolus; `gustatory` was considered and rejected.
8. **Datasets.** Only BNCI 002-2016 (MOT-BRAKE-001) was confirmed as public. Liang et al. 2023 state that their data are available on request only; no public dataset was found for the other classes in the pages read.
