# Worklog - sprint 7, group Q3 (2026-10-17)

Curators: curator_c (ERR-PROTO, CTL-NEGP, CTL-BEADS), curator_d (MEM-VTWM, LAN-DISC), curator_e (EMO-CREAC, EMO-FRUST, SOC-DECEP).

## Result

| Class | Family | Concrete paradigms | first_source (year) | Markers |
|---|---|---|---|---|
| EMO-CREAC | emotion | -001 open-loop drug cue exposure; -002 rtfMRI craving neurofeedback (criterion 4) | Grant et al. 1996 (earliest seen, weak_origin) | MK.BOLD_striatum_reward, MK.LPP, MK.P3b; -002 MK.BOLD_dACC |
| EMO-FRUST | emotion | -001 omission of expected reward; -002 Affective Pacman with ignored input (criteria 2, 3, 4) | Abler et al. 2005 (earliest seen, weak_origin) | MK.BOLD_anterior_insula, MK.affective_band_power; -002 also MK.SMR_ERD |
| MEM-VTWM | memory | -001 two-interval flutter comparison | Preuschhof et al. 2006 (first human neural study; animal origin) | MK.SSSEP, MK.BOLD_frontoparietal (new marker requested) |
| SOC-DECEP | social | -001 instructed lying to autobiographical questions | Spence et al. 2001 | MK.BOLD_dlPFC, MK.BOLD_dACC, MK.BOLD_anterior_insula |
| ERR-PROTO | error | -001 multi-category feedback learning; -002 A/not-A after exposure (criteria 1, 3, 4) | Posner & Keele 1968 (behavioural) | MK.BOLD_visual_cortex |
| CTL-NEGP | control | -001 identity negative priming with overlapping pictures | Tipper 1985 (behavioural) | MK.N2_frontocentral |
| CTL-BEADS | control | -001 beads task, draws to decision | Huq et al. 1988 (behavioural) | MK.BOLD_anterior_insula, MK.BOLD_frontoparietal |
| LAN-DISC | language | -001 discourse-dependent anomaly in short stories | van Berkum et al. 1999 | MK.N400 |

8 classes, 11 concrete paradigms. Provisional short IDs from the gap list were kept; all were checked unused.

## Duplicate checks and boundaries

No existing class or concrete paradigm covers any of the eight; no proposals.csv was needed.

- EMO-CREAC vs EMO-IAPS: IAPS uses normatively rated affective pictures; cue-reactivity cues are defined by their link to the participant's craving (drug use, hunger). STA-MW-002 only cites a craving study in its sources.
- EMO-FRUST vs EMO-STRESS and EMO-MID: stress induction is social-evaluative; MID contrasts reward anticipation, whereas EMO-FRUST-001 contrasts omitted versus received expected rewards. Possible overlap to watch: if EMO-MID-00x files ever list a "reward omission" condition, the maintainer may consider whether EMO-FRUST-001 should be a MID configuration. Kept separate here because the construct (frustration) and the marker (anterior insula) differ.
- MEM-VTWM vs MEM-DMS: DMS is item recognition; VTWM is a parametric (quantity) comparison. Not the same as the vibrotactile P300 / SSSEP classes, which use vibration as a BCI stimulus without a memory demand.
- SOC-DECEP vs MEM-CIT: MEM-CIT carries the alias "ERP lie detection" but tests recognition of concealed knowledge; instructed lying contrasts the act of lying. SOC-TOM covers understanding of others' false beliefs and deception.
- ERR-PROTO vs ERR-PCL and PER-CAT: ERR-PCL is probabilistic cue-outcome learning; PER-CAT is perception of natural object categories without learning.
- CTL-NEGP vs CTL-FLK / CTL-STR / LAN-PRIME / MEM-RPRIM: those measure within-trial conflict or facilitation; negative priming measures carry-over inhibition of an ignored distractor.
- CTL-BEADS vs CTL-PDM: evidence in PDM arrives at a fixed rate; in the beads task the participant decides how much to sample.
- LAN-DISC vs LAN-N400 / LAN-SC: those manipulate words within a single sentence.

## Numbering decisions (D-057, D-058, D-060)

- EMO-CREAC-002: same cue blocks as -001 but with intermittent feedback of ROI activity after each block, criterion 4. First source Li et al. (online 2012, print 2013).
- EMO-FRUST-002: frustration through an interactive game with randomly ignored input instead of reward omission (criterion 2), block design (criterion 3), continuous game feedback (criterion 4). Public data: BNCI Horizon 2020 007-2014.
- ERR-PROTO-002: one category with A/not-A judgements after exposure without feedback, versus several categories learned with feedback (criteria 1 and 4); test items in alternating blocks (criterion 3).
- Parameter-level variants: MEM-VTWM EEG (Spitzer 2010) and MEG (von Lautz 2017) versions (recording modality is not a criterion, D-060 point 3; response-modality cues do not change the comparison task); CTL-BEADS jar ratio and loss manipulation (Furl & Averbeck 2011); CTL-NEGP categorical negative priming (condition in the same study, D-060 point 4) and the ERP study of Frings & Groh-Bordin (configuration not read, kept as a variant pending check); EMO-CREAC substance type; LAN-DISC oscillatory analysis.
- Not numbered: food-cue reactivity (palatable food vs non-food pictures, OpenfMRI ds000157, 30 participants) is a candidate EMO-CREAC-003 (criterion 1/2), but its paper's record (de Ridder et al., PMID 23578759) could not be retrieved (HTTP 429), and the earliest food-cue imaging study was not searched. An auditory (spoken) discourse version would be a separate LAN-DISC concrete paradigm under D-060.

## Source quality and uncertainties

- weak_origin (D-031, D-066 "earliest seen; origin not established"): EMO-CREAC (behavioural/physiological cue-reactivity work predates Grant 1996; first laboratory procedure not identified), EMO-FRUST (behavioural frustration manipulations predate Abler 2005), EMO-CREAC-002 and ERR-PROTO-002 (earliest seen for that configuration).
- Animal origin: MEM-VTWM (monkey flutter-discrimination studies by Romo and colleagues, mentioned in von Lautz et al. 2017; not retrieved and not cited). The first human neural study is used, as D-031 point 2 prescribes.
- Behavioural first sources (allowed by D-031 point 1): ERR-PROTO-001, CTL-NEGP-001, CTL-BEADS-001. CTL-BEADS: Phillips & Edwards 1966 is a related earlier probability-inference task with a fixed sample (LSE repository record, no DOI), noted but not used as origin.
- LAN-DISC: St George, Mannes & Hoffman 1994 (title-dependent coherence of ambiguous paragraphs, ERP) may be an earlier sibling configuration; it was not found in OpenAlex and is not cited. To check (D-062).
- Phase durations are left empty where the first source's abstract or record does not give them (EMO-FRUST-001/-002, SOC-DECEP-001, ERR-PROTO-001/-002, CTL-BEADS-001, LAN-DISC-001). Timing in EMO-CREAC-001/-002 comes from Li et al. (author PDF); in MEM-VTWM-001 from von Lautz et al. 2017; CTL-NEGP-001 prime-probe interval from the Tipper 1985 abstract.
- Details stated from the usual account of the task and not checked in the full text: Posner & Keele training with feedback and number of prototypes; Huq et al. 85:15 ratio; Spence et al. question content and truth/lie cue.
- Christ et al. deception meta-analysis: OpenAlex lists 2008 (online first), the publisher listing 2009; 2009 is used.
- Lewis et al.: OpenAlex search listing gives 2016, volume 32 issue 5; the per-DOI record could not be retrieved, so the year should be rechecked.

## Markers

- Every marker used exists in knowledge/markers/. Closest-fit choices: MK.BOLD_striatum_reward (striatal/OFC cue response), MK.BOLD_dACC (ACC/mPFC craving ROI), MK.affective_band_power (EEG frustration state), MK.BOLD_frontoparietal (lateral prefrontal / parietal activity in VTWM and parietal evidence seeking in BEADS), MK.N2_frontocentral (enhanced N200 on ignored repetitions).
- Not sourced this round (gap-list readouts): N2/P3 for deceptive responses, FRN in feedback-based category learning, P3 to each bead draw, frontal alpha asymmetry and theta in frustration.
- One marker request: MK.parametric_prefrontal_beta (marker_requests.csv).

## API failures

Crossref per-DOI requests refused with HTTP 429 for 10.1097/00001756-200505120-00003, 10.1523/JNEUROSCI.2767-06.2006, 10.1523/JNEUROSCI.6041-09.2010, 10.3758/BF03210958 and 10.1080/23273798.2016.1211300; OpenAlex per-DOI records were used for the first three and OpenAlex search listings for Fox 1995 and Lewis et al. 2016. "bibliography confirmed" phrases name the API actually used.

## Validation

`python3 scripts/validate.py`: the only errors in Q3 files are the 11 expected "class ... is not registered in paradigms/_classes.yaml" messages. classes_new.yaml was checked separately against schema/paradigm_class.schema.json (no errors; all markers exist).
