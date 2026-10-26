# Worklog, curator J (sprint 6, 2026-10-16)

Markers: MK.tES_power_aftereffect, MK.ABR, MK.BOLD_left_IFG, MK.BOLD_olfactory_cortex, MK.BOLD_posterior_insula, MK.BOLD_vestibular_cortex, MK.CCEP, MK.DBS_cortical_EP. All eight had no generators/indexes; none is an alias of a factory marker.

## Decisions per marker

- **MK.tES_power_aftereffect**: generic stimulation marker. Generator set to BR.visual_cortex (grade C, scalp topography), standing for the stimulated region in the dominant alpha-tACS design (posterior montages). No meta-analysis of EEG aftereffects found, so CN.cortical_excitability is B (two studies from one laboratory plus one independent replication). CN.neural_entrainment is C and phrased as a dissociation (Vossen et al. 2015).
- **MK.ABR**: only wave V mapped (BR.inferior_colliculus, B: Møller/Jannetta intracranial plus independent Hashimoto et al. 1981). Waves I-III generators lack ids (vocab request). The Starr and Hamilton lesion study could not be retrieved and is not cited. CN.early_auditory B (Gorga et al. 2006; JCIH 2007). The Stapells 2000 meta-analysis has no DOI record and was not cited.
- **MK.BOLD_left_IFG**: BR.IFG and CN.working_memory graded A on the Nee, Wager and Jonides 2007 meta-analysis plus primary studies. Semantic selection filed under CN.semantic_integration (B). Interference resolution requested as a construct.
- **MK.BOLD_olfactory_cortex**: Seubert et al. 2013 meta-analysis supports A for amygdala/piriform, lateral OFC and insula clusters, and for CN.chemosensation. Piriform has no id, so BR.amygdala is used. Odour imagery C (single study).
- **MK.BOLD_posterior_insula**: BR.posterior_insula A (Kurth et al. 2010; Morrison 2016). CN.somatosensation A (Morrison 2016 meta-analysis plus primary studies). CN.interoception B (narrative review plus primary study). No interoception meta-analysis record could be retrieved.
- **MK.BOLD_vestibular_cortex**: two ALE meta-analyses give A for BR.posterior_insula (OP2/PIVC). BR.TPJ is B. CN.multisensory_integration is B, because the meta-analyses localise vestibular cortex rather than test integration directly.
- **MK.CCEP**: generator location depends on the stimulated pair. The language-network example (STG and IFG) is curated, graded B because Trébaul et al. 2018 is independent of the Matsumoto/Yamao group. CN.language is B. That rests on one group's primary study and review, which is a borderline case for review.
- **MK.DBS_cortical_EP**: restricted to STN DBS, the best-studied target. BR.M1 B (ECoG plus independent scalp EEG). CN.cortical_excitability B.

## Uncertainties

- Kurth et al. 2010: the abstract was not available in the records consulted. The sensorimotor mid-posterior insula assignment rests on the curator's reading of the paper and should be checked against the full text.
- Valentin et al. 2002: both the Crossref and OpenAlex author fields list only the first author. The co-authors in the citation come from the repository citation in the OpenAlex record.
- JCIH 2007: the record has no author field. The corporate author is given as printed on the statement.
- Kasten et al. 2016: Crossref gives no article number. 245 is taken from the DOI suffix.
- BOLD markers were reformatted from flow style to block style by the YAML dump. Field contents are unchanged apart from the appended `notes` sentence.

## Validation

The validator shows 0 problems in curator J files. The 2 remaining problems concern STM-ICMS paradigm files outside this scope.
