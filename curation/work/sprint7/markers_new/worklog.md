# Sprint 7, new markers (D-079): worklog (curator_m, 2026-10-17)

Scope: four markers requested in sprint 6 (`paradigms_P2/marker_requests.csv`, `paradigms_P3/marker_requests.csv`) and approved under D-079: MK.startle_blink, MK.prestimulus_alpha_phase, MK.auditory_spatial_ERP, MK.P2p_numerical_distance. All new files `status: draft`; all sources `verified: false`. Links in links.csv.

## Taxonomy

- Added marker type `peripheral_physiology` (reflex EMG, skin conductance, cardiac) to taxonomy/marker_types.yaml; used by MK.startle_blink. No new recording modality: orbicularis oculi EMG is recorded as `other`, as in EMO-STARTLE-001.

## Decisions

- **MK.startle_blink**: the reflex is generated in the brainstem (no region id in the vocabulary, and none invented). BR.amygdala entered for the affective modulation only, graded B on two independent lesion studies (Angrilli 1996; Buchanan 2004). Indexes: CN.emotional_state B (Vrana 1988; Lang 1990; Bradley 2001; one group, no meta-analysis retrieved), CN.threat_fear B (Grillon 1991; Bradley 2001; Buchanan 2004), CN.approach_motivation C (motivational priming account, one group), CN.sensory_gating B (prepulse inhibition review, Braff 2001). Signature taken from the startle EMG guidelines (Blumenthal 2005), cited in notes.
- **MK.prestimulus_alpha_phase**: type `oscillatory` (the request said "oscillation", which is not a taxonomy term). Generator BR.visual_cortex capped at C (scalp topography; TMS phosphene study is causal for occipital excitability, not a source estimate). Temporal framing mapped to CN.perceptual_organization (no time-perception construct); audiovisual SJ mapped to CN.multisensory_integration (Ikumi 2019, ~13 Hz). All indexes C.
- **MK.auditory_spatial_ERP**: umbrella marker for location effects on N1/P2 and location MMN. Generator BR.STG B (MEG-fMRI and MMN source estimates in posterior STG / planum temporale, plus fMRI). Sound location mapped to CN.early_auditory (B) for lack of a spatial-hearing construct; CN.auditory_change B; CN.spatial_attention C (single study).
- **MK.P2p_numerical_distance**: generator BR.IPS C (one ERP source study, Hyde & Spelke 2012; fMRI evidence indirect). Numerical magnitude mapped to CN.mental_arithmetic (B; three laboratories). The direction of the distance-related amplitude change is left out of the relation pending full-text checks.

## Paradigm marker lists

- PER-TIME-001: MK.alpha_posterior replaced by MK.prestimulus_alpha_phase (stand-in indexed power, not phase; Milton & Pleydell-Pearce 2016 find the timing effect independent of alpha amplitude).
- PER-TIME-002: MK.AV_interaction_ERP replaced by MK.prestimulus_alpha_phase (no study linking the AV interaction ERP to SJ was retrieved; Ikumi 2019 used the audiovisual SJ task).
- PER-AUDLOC-001: MK.N1_auditory replaced by MK.auditory_spatial_ERP; MK.BOLD_auditory_cortex kept (fMRI, Zatorre 2002).
- CTL-NUM-001: MK.P2p_numerical_distance added; MK.BOLD_frontoparietal kept (fMRI distance effect in IPS, Pinel 2001).
- EMO-STARTLE-001: MK.startle_blink added; MK.P3a kept (probe P3, Schupp 1997).
- Notes lines of the five paradigms updated to match.

## Class marker lists (for the maintainer)

class_marker_updates.csv lists the changes to paradigms/_classes.yaml. Until they are made, scripts/validate.py reports five class-superset errors (D-061) on the five paradigm files; with the listed changes applied to a scratch copy the validator reports 0 problems. The removals for PER-TIME and PER-AUDLOC are safe because no other concrete paradigm of those classes uses the removed markers; CTL-NUM keeps MK.LRP for CTL-NUM-002. The EMO-STARTLE class notes still describe MK.P3a as the closest marker and could be updated at the same time.

## Uncertainties

- Butler 1972: no abstract in the record; the spatial-separation effect on N1 is stated from the curator's reading.
- Busch et al. 2009, Davis 1992 and Libertus et al. 2007 would strengthen three links but could not be retrieved (rate limits, empty title); candidates for the next pass.
- The vocabulary changes approved in D-079 (for example BR.auditory_brainstem) were not used; if a brainstem region id is added later, MK.startle_blink could take a brainstem generator.
