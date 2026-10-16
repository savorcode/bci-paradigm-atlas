# Sprint 7 proposals: worklog

Date: 2026-10-17. Scope: D-079 concrete-paradigm proposals and hybrid variants. Files edited only in the fields allowed for this task (new concrete files; variants, notes, first_source of existing files).

## Numbering
- MOT-ATT: -001 to -003 existed, so the brain-spine interface is MOT-ATT-004 and the stroke BCI-FES study MOT-ATT-005.
- MOT-MI: -001 to -011 existed, so the FES brain switch is MOT-MI-012.
- MEM-CSPAN-003, PER-CROWD-002, CTL-NUM-003 were the next free numbers.

## Decisions
1. **MOT-ATT-004** (Lorach et al. 2023). Criteria 1, 3, 4 vs MOT-ATT-001. Only MK.SMR_ERD is listed: the gamma-band information would be MK.high_gamma, which is not in the MOT-ATT class markers (class-superset rule, D-061); suggested to the maintainer.
2. **MOT-MI-012** (Pfurtscheller et al. 2003). Criterion 4 vs MOT-MI-004. The 2003 abstract could not be retrieved; detection details come from the 2005 follow-up abstract and are flagged for checking; paradigm_timing left out. The 2003 paper predates the MOT-MI-004 first_source (2009): suggestion recorded, MOT-MI-004 not edited.
3. **Stroke BCI-FES → MOT-ATT-005** (Biasiucci et al. 2018). The full text says patients were asked to *attempt* to extend the affected hand, so by the D-057 class rule this belongs to MOT-ATT, not MOT-MI. No earlier controlled BCI-FES study could be retrieved with a record; this remains the earliest retrieved one, and first_source may move later.
4. **Hybrid variants** (D-022): added to SSR-SSVEP-001 and MOT-MI-001 (Allison et al. 2010), PER-ODD-001 and SSR-SSVEP-008 (Panicker et al. 2011). None of these files had variants before; the schema format (name, source, note) was used, as in other files. Notes say the entries are cross-family hybrid markers, not parameter variants.
5. **D-057 re-checks**
   - MEM-CSPAN-003: per-set feedback (criterion 4), letters and matrix recall (criterion 2). Not parameter-only, so a new file; variant removed from -002. The aliases, trial_structure and distinguishing of -002 still describe the automated version and need the maintainer.
   - PER-CROWD-002: vernier offset target with line flankers (criterion 2), flanker-length conditions (criterion 1). New file; variant removed from -001.
   - CTL-NUM-003: single number vs fixed standard (criterion 2), larger/smaller classes (criterion 1). New file; variant removed from -001. Marker MK.P2p_numerical_distance (newly registered this sprint by another curator), so validate.py reports a class-superset error for CTL-NUM-003, as it already does for CTL-NUM-001, until the class gets this marker.
6. **PER-ODD-008**: first_source not moved. Schreuder, Blankertz & Tangermann 2010 was tested offline only, so it differs from the online configuration by criterion 4. The 2010 paper is recorded in notes as the earliest publication of the approach.

## Validation
`python3 scripts/validate.py`: 434 paradigms, 6 problems. One is from this task (CTL-NUM-003, the marker missing from the class, see 5); the other five come from parallel marker work (CTL-NUM-001, EMO-STARTLE-001, PER-AUDLOC-001, PER-TIME-001/-002: new markers not yet in their class markers). All need class updates in `_classes.yaml`, which is outside this task's scope. All other files touched here validate.
