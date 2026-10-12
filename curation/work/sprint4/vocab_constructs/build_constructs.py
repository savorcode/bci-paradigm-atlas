"""Build knowledge/constructs.yaml (sprint 4, vocabulary curator - constructs).

Run from repo root:  python3 curation/work/sprint4/vocab_constructs/build_constructs.py
Writes knowledge/constructs.yaml and curation/work/sprint4/vocab_constructs/mapping.csv.
Cognitive Atlas ids below were all returned by the Cognitive Atlas API (see fetch_log.md); none is invented.
"""
import csv
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
ids = json.load(open(ROOT / "curation/work/sprint4/vocab_ids.json", encoding="utf-8"))["constructs"]

# existing atlas definitions (kept verbatim)
existing = {t["id"]: t for t in yaml.safe_load(open(ROOT / "knowledge/constructs.yaml", encoding="utf-8"))["terms"]}

PARENT_OVERRIDE = {"CN.novelty_orienting": "CN.orienting", "CN.sustained_visual_attention": "CN.sustained_attention"}

DEF = {
    "CN.perception": "Construction of representations of the external world and the body from sensory input.",
    "CN.attention": "Selection and prioritisation of relevant information under limited processing capacity.",
    "CN.memory": "Encoding, maintenance, updating and retrieval of information over time.",
    "CN.language": "Comprehension and production of words, sentences and their meaning.",
    "CN.cognitive_control": "Processes that monitor ongoing behaviour for conflict and errors and adjust it toward current goals.",
    "CN.motor": "Selection, preparation, execution and simulation of bodily movements.",
    "CN.affect": "Evaluation of outcomes and stimuli in terms of value, motivation and emotion.",
    "CN.mental_imagery": "Generation and manipulation of quasi-perceptual or abstract internal representations in the absence of corresponding external input.",
    "CN.hmi": "Perception, evaluation and expression of intent by a human interacting with a machine or interface.",
    "CN.brain_state": "Global states of the brain such as arousal, vigilance, sleep and large-scale rhythmic activity.",
    "CN.social": "Processing of information about other agents and oneself in a social context.",
    "CN.early_visual": "Initial cortical processing of low-level visual features such as luminance, contrast, orientation and spatial frequency.",
    "CN.object_recognition": "Integration of visual features into representations that identify the category or identity of an object.",
    "CN.face_perception": "Specialised visual processing of the structure of faces.",
    "CN.auditory_change": "Automatic detection of a deviation between incoming sounds and a regularity extracted from preceding auditory input.",
    "CN.neural_entrainment": "Alignment of the phase of neural activity to the rhythm of periodic sensory stimulation.",
    "CN.spatial_attention": "Allocation of attention to a location in space, enhancing processing of stimuli at that location.",
    "CN.target_selection": "Selection of a target among competing distractors for prioritised processing.",
    "CN.orienting": "Involuntary shift of attention toward a salient or unexpected stimulus.",
    "CN.sustained_attention": "Maintenance of attentional focus on a task over an extended period.",
    "CN.working_memory": "Short-term maintenance and manipulation of information in the service of ongoing tasks.",
    "CN.semantic_integration": "Integration of the meaning of a word or stimulus with the preceding semantic context.",
    "CN.syntactic_processing": "Construction and revision of the grammatical structure of a sentence.",
    "CN.inner_speech": "Covert generation of speech without overt articulation.",
    "CN.conflict_monitoring": "Detection of competition between simultaneously active response tendencies.",
    "CN.error_monitoring": "Detection and evaluation of one's own erroneous actions.",
    "CN.response_inhibition": "Suppression or cancellation of a prepotent or already initiated response.",
    "CN.anticipation": "Preparation for an expected upcoming event, such as a stimulus following a warning signal.",
    "CN.motor_preparation": "Selection and preparation of a specific movement before it is executed.",
    "CN.reward_prediction_error": "Signal of the difference between an obtained outcome and the expected outcome.",
    "CN.emotional_salience": "Enhanced motivated attention to emotionally significant stimuli.",
    "CN.visual_imagery": "Generation of a visual representation from memory or description in the absence of the corresponding visual input.",
    "CN.language_to_imagery": "Construction of a mental image of a scene or object from a verbal description.",
    "CN.machine_error_perception": "Recognition by an observer that a machine or interface has acted contrary to the observer's intention or expectation.",
    "CN.intent_selection": "Expression of a choice among several options through attention or mental imagery for use by an interface.",
    "CN.cortical_idling": "State of cortical rhythmic activity, typically posterior alpha, that predominates when a cortical area is not engaged in processing sensory input.",
    "CN.early_auditory": "Initial cortical processing of acoustic features such as onset, pitch and intensity.",
    "CN.somatosensation": "Processing of touch, proprioception, temperature and pain from the body.",
    "CN.chemosensation": "Perception of chemical stimuli through smell and taste.",
    "CN.sensory_gating": "Reduction of neural responses to repeated or irrelevant sensory input.",
    "CN.interoception": "Sensing and representation of signals about the internal physiological state of the body.",
    "CN.multisensory_integration": "Combination of information from different sensory modalities into a unified percept.",
    "CN.perceptual_awareness": "Conscious experience of a stimulus, as distinct from its unconscious processing.",
    "CN.perceptual_organization": "Grouping and segregation of sensory elements into coherent objects, figures and streams.",
    "CN.prediction_violation": "Neural signalling of a mismatch between sensory input and an internal prediction.",
    "CN.distractor_suppression": "Active suppression of task-irrelevant stimuli that compete for attention.",
    "CN.episodic_encoding": "Formation of a memory trace for a specific event in its spatial and temporal context.",
    "CN.recognition_memory": "Judgement that a stimulus has been encountered before, based on familiarity or recollection.",
    "CN.prospective_memory": "Remembering to carry out an intended action at a future time or event.",
    "CN.spatial_navigation": "Representation of spatial relations and their use to find one's way through an environment.",
    "CN.memory_consolidation": "Stabilisation of newly encoded memories over time, notably during sleep.",
    "CN.speech_tracking": "Tracking of the temporal and hierarchical structure of continuous speech, from the acoustic envelope to linguistic units.",
    "CN.phonological_processing": "Processing of the sound structure of language, such as phonemes and syllables.",
    "CN.prosody": "Processing of the rhythm, stress and intonation of speech.",
    "CN.speech_production": "Planning and articulation of spoken language.",
    "CN.task_switching": "Reconfiguration of task set when shifting between different tasks.",
    "CN.evidence_accumulation": "Gradual integration of sensory evidence toward a decision threshold.",
    "CN.metacognition": "Monitoring and evaluation of one's own cognitive processes, such as confidence in a decision.",
    "CN.movement_kinematics": "Control and representation of the trajectory, velocity and force of continuous movements.",
    "CN.sensorimotor_integration": "Use of sensory feedback to guide and adjust motor output.",
    "CN.value_decision": "Choice among options based on their subjective value, risk or uncertainty.",
    "CN.threat_fear": "Detection of and response to threatening stimuli, including fear learning.",
    "CN.emotional_state": "Ongoing affective state characterised by its valence and arousal.",
    "CN.auditory_imagery": "Generation of an auditory representation, such as a tune or voice, in the absence of sound.",
    "CN.mental_arithmetic": "Mental calculation and other internal manipulation of symbolic or spatial content.",
    "CN.mentalizing": "Attribution of mental states such as beliefs, desires and intentions to others.",
    "CN.self_processing": "Processing of information related to oneself, such as one's own name, face or traits.",
    "CN.social_interaction": "Coordination of behaviour and attention with other people during real-time interaction.",
    "CN.social_perception": "Perception of socially relevant cues such as gaze direction and biological motion.",
    "CN.vigilance": "Level of tonic alertness, ranging from full wakefulness to drowsiness.",
    "CN.sleep": "Recurring state of reduced responsiveness organised into distinct stages.",
    "CN.consciousness_level": "Overall level of wakefulness and responsiveness, as altered in anaesthesia or disorders of consciousness.",
    "CN.spontaneous_thought": "Thought that arises without an external task, such as mind wandering.",
    "CN.cortical_excitability": "Responsiveness of cortical tissue to direct stimulation such as transcranial magnetic stimulation.",
    "CN.self_regulation": "Voluntary modulation of one's own brain activity guided by real-time feedback.",
}

# (trm_id, concept name, confidence, note); None -> no adequate match (confidence low)
CA = {
    "CN.early_visual": ("trm_4a3fd79d0b4b5", "visual perception", "medium", "broader than early (low-level) visual processing"),
    "CN.object_recognition": ("trm_4a3fd79d0aab0", "object recognition", "high", ""),
    "CN.face_perception": ("trm_4a3fd79d0a300", "face perception", "high", ""),
    "CN.auditory_change": (None, None, "low", "tried 'auditory deviance detection', 'change detection', 'deviance detection': no concept"),
    "CN.neural_entrainment": (None, None, "low", "tried 'entrainment', 'neural entrainment': no concept; 'rhythm' (trm_4a3fd79d0afc3) exists but is not equivalent"),
    "CN.spatial_attention": ("trm_557b4abe521af", "spatial selective attention", "high", ""),
    "CN.target_selection": ("trm_4a3fd79d0b4cd", "visual search", "medium", "as in factory seed; 'selective attention' trm_4a3fd79d0b043 is the broader alternative"),
    "CN.orienting": ("trm_4a3fd79d0b5fb", "attention shifting", "medium", "'orienting', 'orienting response', 'attentional orienting', 'attentional capture' not found; attention shifting does not specify involuntary"),
    "CN.sustained_attention": ("trm_4a3fd79d0b311", "sustained attention", "high", ""),
    "CN.context_updating": ("trm_55b6b9a666604", "working memory updating", "medium", "'context updating' not found"),
    "CN.working_memory": ("trm_4a3fd79d0b5a7", "working memory", "high", ""),
    "CN.semantic_integration": ("trm_4a3fd79d0b87a", "semantic processing", "medium", "broader than integration"),
    "CN.syntactic_processing": ("trm_4a3fd79d0b34b", "syntactic processing", "high", ""),
    "CN.inner_speech": (None, None, "low", "tried 'inner speech', 'subvocal rehearsal': no concept"),
    "CN.conflict_monitoring": ("trm_4a3fd79d09e13", "conflict detection", "high", "'conflict monitoring' not found; near-synonym"),
    "CN.error_monitoring": ("trm_4a3fd79d0a20c", "error detection", "medium", "covers detection, not post-error evaluation"),
    "CN.response_inhibition": ("trm_4a3fd79d0af66", "response inhibition", "high", ""),
    "CN.anticipation": ("trm_4a3fd79d09849", "anticipation", "high", ""),
    "CN.motor_preparation": ("trm_4a3fd79d0a9a1", "motor planning", "medium", "'motor preparation' not found; 'response selection' trm_4a3fd79d0af71 (factory seed) is an alternative"),
    "CN.motor_imagery": (None, None, "low", "'motor imagery' (queried twice) and 'imagined movement' returned errors; factory seed lists 'motor imagery' but no id could be retrieved - recheck"),
    "CN.reward_prediction_error": ("trm_4b6525253c63f", "reward processing", "medium", "'reward prediction error', 'prediction error' not found"),
    "CN.emotional_salience": ("trm_4a3fd79d0b020", "salience", "medium", "'emotional arousal' not found; salience is not emotion-specific"),
    "CN.visual_imagery": ("trm_4a3fd79d0b487", "visual imagery", "high", ""),
    "CN.language_to_imagery": (None, None, "low", "no specific concept; 'mental imagery' trm_4a3fd79d0a8fc is only a broad parent-level match"),
    "CN.machine_error_perception": (None, None, "low", "no specific concept; 'performance monitoring' trm_4a3fd79d0ac30 / 'error detection' refer to own errors"),
    "CN.intent_selection": ("trm_4a3fd79d0a67d", "intention", "medium", "broad"),
    "CN.cortical_idling": (None, None, "low", "tried 'resting state', 'rest': no concept"),
    "CN.early_auditory": ("trm_4a3fd79d09ab2", "auditory perception", "medium", "broader than early auditory processing"),
    "CN.somatosensation": ("trm_4a3fd79d0b160", "somatosensation", "high", "nociception not covered separately"),
    "CN.chemosensation": ("trm_4a3fd79d0aabc", "olfaction", "medium", "covers smell only; 'taste' not found"),
    "CN.sensory_gating": (None, None, "low", "tried 'sensory gating': no concept"),
    "CN.interoception": ("trm_4fe39e4388409", "interoception", "high", ""),
    "CN.multisensory_integration": ("trm_4e31ced566649", "multisensory integration", "high", ""),
    "CN.perceptual_awareness": ("trm_4ff36d79c26c6", "visual awareness", "medium", "'awareness' not found; visual only"),
    "CN.perceptual_organization": (None, None, "low", "tried 'perceptual organization', 'perceptual grouping', 'gestalt grouping': no concept"),
    "CN.prediction_violation": ("trm_4a3fd79d0b306", "surprise", "medium", "'prediction error' not found; 'expectancy' trm_4ebfe9a465449 also exists"),
    "CN.attention_allocation": ("trm_4a3fd79d09925", "attentional resources", "medium", "'divided attention' trm_4a3fd79d0a116 and 'attention capacity' trm_4a3fd79d0990e also exist"),
    "CN.distractor_suppression": ("trm_4c3e04d656f06", "interference resolution", "medium", "not attention-specific"),
    "CN.episodic_encoding": ("trm_4a3fd79d0b8e5", "encoding", "medium", "not episodic-specific"),
    "CN.recognition_memory": ("trm_4a3fd79d0b967", "recognition", "medium", "'recognition memory' not found; 'familiarity' trm_4a3fd79d0b8fc also exists"),
    "CN.prospective_memory": ("trm_4a3fd79d0ae70", "prospective memory", "high", ""),
    "CN.spatial_navigation": ("trm_4a3fd79d0aa00", "navigation", "medium", "'spatial memory' trm_4a3fd79d0b1d5 covers the relational-memory part"),
    "CN.memory_consolidation": ("trm_4a3fd79d0b920", "memory consolidation", "high", ""),
    "CN.speech_tracking": ("trm_4a3fd79d0b1f7", "speech perception", "medium", "broader; no tracking-specific concept"),
    "CN.phonological_processing": ("trm_52b5f1ef4f9cc", "phonological processing", "high", ""),
    "CN.prosody": ("trm_4a3fd79d0ae64", "prosody", "high", ""),
    "CN.speech_production": ("trm_4a3fd79d0b247", "speech production", "high", ""),
    "CN.task_switching": ("trm_4a3fd79d0b613", "task switching", "high", ""),
    "CN.evidence_accumulation": (None, None, "low", "tried 'evidence accumulation', 'perceptual decision making': no concept; 'decision making' too broad"),
    "CN.metacognition": ("trm_4a3fd79d0a920", "metacognition", "high", ""),
    "CN.motor_execution": ("trm_557b4a7315f1b", "response execution", "medium", ""),
    "CN.movement_kinematics": ("trm_4a3fd79d0a972", "motor control", "medium", "broad"),
    "CN.sensorimotor_integration": (None, None, "low", "tried 'sensorimotor integration', 'visuomotor coordination': no concept"),
    "CN.value_decision": ("trm_4a3fd79d0a038", "decision making", "medium", "broad; not value-specific"),
    "CN.threat_fear": ("trm_4a3fd79d0b689", "fear", "high", ""),
    "CN.emotional_state": ("trm_4a3fd79d0a17f", "emotion", "medium", "'valence' trm_4a3fd79d0b429 and 'arousal' trm_4a3fd79d09883 also exist"),
    "CN.auditory_imagery": ("trm_4a3fd79d09a6c", "auditory imagery", "high", ""),
    "CN.mental_arithmetic": ("trm_4a3fd79d0a8ed", "mental arithmetic", "high", ""),
    "CN.mentalizing": ("trm_4a3fd79d0b392", "theory of mind", "high", "'mentalizing' not found; synonym"),
    "CN.self_processing": (None, None, "low", "'self referential processing' not found; 'self knowledge' trm_5154b39a3193d is narrower"),
    "CN.social_interaction": (None, None, "low", "'social interaction' not found; 'joint attention' trm_4b75ed06c917d covers only a part"),
    "CN.social_perception": ("trm_kYtw4QBOKCbsM", "biological motion", "medium", "'social perception' not found; covers biological motion only"),
    "CN.vigilance": (None, None, "low", "tried 'vigilance', 'alertness': no concept; 'arousal'/'fatigue' (trm_52583e52d5e7a) are related but not equivalent"),
    "CN.sleep": ("trm_5159c70d0e98e", "sleep", "high", ""),
    "CN.consciousness_level": ("trm_4a3fd79d09e35", "consciousness", "medium", "not level-specific"),
    "CN.spontaneous_thought": (None, None, "low", "tried 'mind wandering', 'mind-wandering', 'spontaneous thought', 'daydreaming': no concept"),
    "CN.cortical_excitability": (None, None, "low", "tried 'cortical excitability': no concept (physiological, outside Cognitive Atlas scope)"),
    "CN.self_regulation": (None, None, "low", "tried 'self regulation', 'self-regulation', 'neurofeedback': no concept; 'self control' trm_4ee8facd77dfc is not equivalent"),
    "CN.novelty_orienting": ("trm_4a3fd79d0aa47", "novelty detection", "medium", "detection rather than orienting"),
    "CN.sustained_visual_attention": ("trm_4a3fd79d0b311", "sustained attention", "medium", "not modality-specific"),
}


def cap(s):
    return s[0].upper() + s[1:]


terms, rows = [], []
for cid, seed in ids.items():
    parent = PARENT_OVERRIDE.get(cid, seed.get("parent"))
    t = {"id": cid, "en": cap(seed["en"]), "zh": seed["zh"]}
    if cid in existing:
        t["en"] = existing[cid]["en"]
        t["definition"] = existing[cid]["definition"]
    else:
        t["definition"] = DEF[cid]
    if parent:
        t["parent"] = parent
        trm, name, conf, note = CA[cid]
        if trm:
            t["cognitive_atlas"] = f"{trm} ({name})"
        rows.append({"id": cid, "cognitive_atlas": f"{trm} ({name})" if trm else "", "parent": parent,
                     "confidence": conf, "note": note})
    else:
        rows.append({"id": cid, "cognitive_atlas": "", "parent": "", "confidence": "n/a", "note": "domain root; not mapped"})
    if seed.get("desc") and cid not in existing:
        t["notes"] = f"中文释义（范式工厂）：{seed['desc']}"
    terms.append(t)

assert len(terms) == 81 and set(DEF) | set(existing) >= set(ids)
idset = {t["id"] for t in terms}
assert all(t.get("parent", cid) in idset for t in terms for cid in [t["id"]])

out = {"schema_version": "0.2", "prefix": "CN", "terms": terms}
header = "# Cognitive constructs / 认知构念 (sprint 4: 81 ids aligned with the paradigm factory)\n"
with open(ROOT / "knowledge/constructs.yaml", "w", encoding="utf-8") as f:
    f.write(header)
    yaml.safe_dump(out, f, allow_unicode=True, sort_keys=False, width=120)

with open(HERE / "mapping.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["id", "cognitive_atlas", "parent", "confidence", "note"])
    w.writeheader()
    w.writerows(rows)
print("wrote", len(terms), "terms")
