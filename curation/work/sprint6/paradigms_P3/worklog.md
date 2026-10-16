# Worklog, sprint 6, group P3: emotion, social, language and state (2026-10-16)

Curators: curator_e (EMO, SOC, STA), curator_d (LAN).

## Result

| Provisional | Created | Family | Concrete paradigms | First source (year) |
|---|---|---|---|---|
| EMO-STARTLE | EMO-STARTLE | emotion | -001 | Vrana, Spence & Lang (1988) |
| EMO-AAT | EMO-AAT | emotion | -001, -002 | Solarz (1960); -002 Rinck & Becker (2007) |
| SOC-CONV | SOC-DIAL (renamed) | social | -001 | Jiang et al. (2012) |
| SOC-PGG | SOC-PGG | social | -001, -002 | Marwell & Ames (1979); -002 Fehr & Gächter (2000) |
| LAN-RA | LAN-RA | language | -001 | Forster & Chambers (1973) |
| LAN-SIGN | not created | language | - | duplicate of LAN-SC-002 |
| STA-FAT | STA-FAT | state | -001 | Lorist et al. (2000) |
| STA-SD | STA-SD | state | -001 | Patrick & Gilbert (1896) |

`python3 scripts/validate.py`: the only errors in these files are the expected "class ... is not registered in paradigms/_classes.yaml" (9 files). classes_new.yaml validates against schema/paradigm_class.schema.json. Class markers are the union of the concrete-paradigm markers (D-061).

## Duplicate checks

- **LAN-SIGN, skipped.** LAN-SC-002 "Sign language sentence comprehension" already exists (signed sentences vs non-sign gesture baseline, fMRI), and the LAN-SC class lists "sign language comprehension" and "sign language sentence comprehension" as aliases. LAN-SC-001 notes that a LAN-SIGN candidate was proposed earlier and resolved by moving it to LAN-SC-002. No new configuration identified, so no proposal row.
- **EMO-STARTLE.** No existing class or alias mentions startle except EMO-THREAT-001, which notes that startle-based threat-of-shock work was not surfaced. Picture-viewing affective startle is a separate mechanism (probe reflex modulation), so a new class. Startle in threat-of-shock (NPU) designs could later be a variant of EMO-THREAT.
- **EMO-AAT.** Only ERR-OGNG (Go-to-win / NoGo-to-avoid) and ERR-INST mention "avoid", in a reinforcement sense. No overlap.
- **SOC-CONV -> SOC-DIAL.** Hyperscanning appears as aliases of SOC-JA (joint action) and SOC-EYE (eye contact); neither involves verbal exchange. New class. Renamed because SOC-CONV is one letter from the existing SOC-CONF (conformity).
- **SOC-PGG.** SOC-TRUST lists "public goods game (related)" as an alias but has no public goods concrete paradigm; the n-player group-account structure differs from dyadic trust and prisoner's dilemma games. New class; the maintainer should drop the alias from SOC-TRUST when merging.
- **LAN-RA.** Partial overlap with LAN-OVS (overt/attempted speech production; description says "read aloud or repeat prompted ... words"). LAN-OVS is defined by articulatory decoding for speech neuroprostheses (MK.high_gamma, MK.motor_cortical_spiking, ECoG/intracortical), whereas LAN-RA is the psycholinguistic print-to-speech naming task (latency effects of frequency, lexicality, regularity; fMRI/PET). Kept as a new class; maintainer may judge otherwise. LAN-PN (picture naming) is the pictorial counterpart.
- **STA-FAT.** Checked STA-DRV (monotonous driving drowsiness, alias "driving simulator fatigue"), STA-PVT, CTL-SART, CTL-CPT, STA-MATB. None takes elapsed time on task as its defining contrast. New class.
- **STA-SD.** STA-PVT mentions sleep loss in its description, and STA-REST-001 lists the sleep deprivation EEG dataset (no URL). Sleep deprivation is a state manipulation used with several outcome tasks, not covered as a protocol. New class.

## Decisions

- **EMO-AAT-002** created (D-057 criteria 2 and 4): instruction by an irrelevant feature (picture format) instead of valence, and continuous zoom feedback. This is the joystick version most used in clinical and training research.
- **SOC-PGG-002** created (criterion 3): added peer punishment stage (Fehr & Gächter 2000).
- **STA-FAT**: carrier tasks (task switching in Lorist et al. 2000; letter-detection attention task in Boksem et al. 2005) are recorded as variants, not separate serial numbers, because the defining manipulation is elapsed time on task. Flag for maintainer review.
- **SOC-DIAL-001 variant** Bögels et al. 2015 (single-brain EEG, question-answer turn-taking) kept as a variant pending review; it may deserve its own serial number (criteria 1;3).
- **LAN-RA-001 variant** Petersen et al. 1988 (PET block design) kept as a variant; possible separate serial number under criterion 3.

## Markers

- EMO-STARTLE: MK.P3a (probe P3, Schupp et al. 1997). The main measure, startle eyeblink EMG, has no marker; request MK.startle_blink in marker_requests.csv (peripheral; type not in taxonomy/marker_types.yaml).
- EMO-AAT: MK.frontal_alpha_asymmetry as the closest marker (approach/withdrawal motivation). No EEG study of the AAT retrieved; link needs evidence.
- SOC-DIAL: MK.interbrain_synchrony (Jiang et al. 2012).
- SOC-PGG: MK.FRN, MK.BOLD_striatum_reward, taken over from SOC-TRUST by analogy; no PGG-specific neural source retrieved.
- LAN-RA: MK.BOLD_language_network.
- STA-FAT: MK.frontal_midline_theta, MK.alpha_posterior (Boksem et al. 2005 theta and lower-alpha increases).
- STA-SD: MK.theta_drowsiness (Cajochen et al. 1995), MK.slow_wave (Borbély et al. 1981).

## Uncertainties and open issues

- Trial durations of EMO-STARTLE-001 (6-s pictures, 50-ms probe, 10-20-s ITI) are typical standard values, not confirmed in the 1988 paper.
- EMO-AAT, SOC-PGG and LAN-RA phase durations are not given; the retrieved records did not contain them.
- EMO-AAT-002 zoom and format instruction described from the standard version; check against Rinck & Becker 2007.
- SOC-PGG-002 group size, endowment and rounds not checked.
- Patrick & Gilbert 1896: content not checked (no abstract in the records); hours awake not recorded.
- Xiang et al. 2024 dataset: hours of deprivation not available from the records.
- STA-FAT first_source is the earliest EEG/ERP protocol found, not the origin of behavioural mental fatigue research (D-031 practice).
- Marwell & Ames 1979 may not be the very first public goods experiment.
- No public datasets verified for EMO-STARTLE, EMO-AAT, SOC-DIAL, SOC-PGG, LAN-RA or STA-FAT.
- Crossref failures: four requests (one upper-case DOI form, two rate limits, one unknown error) were completed through the OpenAlex API. One DOI recalled from memory for Jiang et al. 2012 did not resolve and was replaced by the OpenAlex record.
