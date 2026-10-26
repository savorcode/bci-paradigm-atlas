# Search log - sprint 7, group Q1 (2026-10-17)

Web searches: 13 of the 30 allowed. Bibliographic lookups used the Crossref API (title queries and `works/<DOI>` records) and the OpenAlex API (title search and `works/doi:<DOI>`). Both APIs rate-limited bursts of requests (HTTP 429) several times; requests were then repeated one at a time.

## Web searches

| # | Query | Outcome |
|---|---|---|
| 1 | Haufe Treder Blankertz "EEG potentials predict upcoming emergency brakings during simulated driving" | BNCI 002-2016 description page; Liang et al. 2023 (PMC); press coverage |
| 2 | Shishkin 2016 "EEG negativity in fixations used for gaze-based control" eye-brain-computer interface | Frontiers full text and PMC record of Shishkin et al. 2016 |
| 3 | Kramer Trejo Humphrey 1995 "task-irrelevant auditory probes" mental workload | Roy et al. 2016 (Front Hum Neurosci, PMC) and related probe studies |
| 4 | Schafer Marcus 1973 "Self-stimulation alters human sensory brain responses" Science | No direct hit (brain-stimulation reward pages); record then found through the Crossref API |
| 5 | Haufe 2011 emergency braking ... "100 km/h" ... inter-stimulus interval | Nguyen & Chung 2019 (Sensors) and press items; no timing of the original |
| 6 | first study EEG motor imagery of different force levels or speeds ... review 10.3389/fnins.2023.1345961 | Wang et al. 2017 (JNER), Yuan et al. 2010 (PMC), speed-imagery papers |
| 7 | Gu Dremstrup Farina 2009 "Single-trial discrimination of type and speed of wrist movements" | Gu et al. 2009 Frontiers (ALS, imagined speed) full text page |
| 8 | motor imagery of swallowing EEG brain-computer interface dysphagia ... Yang Guan Ang 2014 Kober | Authors' copy of Yang et al. 2014 (J Neural Eng) and the 2012 conference paper |
| 9 | first functional neuroimaging study of volitional swallowing 1999 Hamdy PET ... Zald Pardo | PubMed/University pages for Zald & Pardo 1999 and Hamdy 1999 (PubMed page did not render) |
| 10 | Smith McEvoy Gevins 1999 "strategy development and skill acquisition" EEG video game | No page confirming the task; record only (Crossref) |
| 11 | Giraudet St-Louis Scannella Causse 2015 "P300 event-related potential as an indicator of inattentional deafness" | PMC full text (read), HAL record (blocked by bot protection) |
| 12 | "Assessment of mental workload with task-irrelevant auditory probes" abstract ... | No abstract of Kramer et al. 1995 found |
| 13 | Macdonald Lavie 2011 "inattentional deafness" visual perceptual load ... | PMC page (browser check, not readable), later Lavie-group papers |

## Pages and API records read

| Source | Outcome |
|---|---|
| BNCI Horizon 2020 002-2016 description.txt | Read: 18 participants, 3 x 45 min, event markers, channels, reference publication Haufe et al. 2011 |
| PMC full text, Liang et al. 2023 | Read: braking every 15-60 s, P300-like positivity and fronto-central negative shift, no public data |
| arXiv 2207.12669 (Liang et al.) | Read: no extra detail on the Haufe protocol |
| PMC full text, Nguyen & Chung 2019 | Read: no Haufe protocol details; not cited |
| Frontiers full text, Gu et al. 2009 | Read: 4 ALS patients, fast vs slow imagined wrist extension, MRCP timing |
| JNER full text, Wang et al. 2017 | Read: protocol, timing, feedback, results |
| PMC3036745 | Browser check page; not readable |
| Authors' copy, Yang et al. 2014 | Read: timing, classes, participants, results |
| Frontiers full text, Shishkin et al. 2016 | Read: participants, analysis window, negativity, classification |
| PMC full text, Roy et al. 2016 | Read: single-probe design during MATB-II, history of the technique |
| PMC full text, Allison & Polich 2008 | Read: game, probe parameters, conditions, ERP results |
| PMC full text, Giraudet et al. 2015 | Read: protocol, tone parameters, miss rates, ERP results |
| Frontiers PDFs fnhum.2016.00519 / 00073 | Server error |
| PubMed 10200226 | Empty page |
| Europe PMC REST (Macdonald & Lavie abstract) | Rate-limited (HTTP 429); not read |
| Crossref works records (24 DOIs) | Retrieved; see sources.csv |
| Crossref works/10.3389/fnins.2016.00528 | Rate-limited; OpenAlex record used instead |
| Crossref title queries (several long queries) | Returned unrelated items; repeated with shorter queries or OpenAlex search |
| OpenAlex abstracts (Kramer 1995, Allison & Polich 2008) | abstract_inverted_index empty |
