# Search log - sprint 7, group Q3 (2026-10-17)

Web searches used: 15 of 30. Bibliographic records: Crossref API (`api.crossref.org/works/<DOI>` and bibliographic queries) and OpenAlex API (`api.openalex.org/works/doi:<DOI>` and search). Both APIs repeatedly returned HTTP 429 (rate limited) on 2026-10-17; where a per-DOI Crossref request was refused, the OpenAlex record was used, and in two cases (Fox 1995, Lewis et al. 2016) only an OpenAlex search listing could be retrieved.

## Duplicate checks (repository)

| Query | Outcome |
|---|---|
| grep paradigms/ and _classes.yaml: cue reactiv, craving, smok, alcohol, nicotine, cocaine, food cue, addict | Only STA-MW-002 (craving and mind wandering, a source title). No cue-reactivity class. |
| frustrat | no hits |
| vibrotactile, flutter | vibrotactile P300/oddball, SSSEP, tactile classes; no frequency-comparison working memory task |
| decept, lying, lie | MEM-CIT (alias "ERP lie detection", concealed information), SOC-TOM (source title on children's understanding of deception). No instructed-lying class. |
| prototype, category learning, categor | PER-CAT (visual object categorisation), ERR-PCL (weather prediction); no prototype-distortion task |
| negative priming | no hits |
| beads, jumping to conclusion, information sampling | no hits |
| discourse, coheren, narrative | coherence hits are corticomuscular / interhemispheric coherence only; no discourse class |
| ids EMO-CREAC, EMO-FRUST, MEM-VTWM, SOC-DECEP, ERR-PROTO, CTL-NEGP, CTL-BEADS, LAN-DISC (and alternatives CUE, CRAV, LIE, CATL, NP, JTC, DCOH) | all unused |
| other sprint 7 work folders (Q1, Q2, proposals) | no use of these classes |

## Web searches

| # | Query | Outcome |
|---|---|---|
| 1 | first cue reactivity paradigm drug cues laboratory origin Carter Tiffany 1999 meta-analysis | Carter & Tiffany 1999 confirmed as standard review; no origin paper named |
| 2 | "Affective Pacman" frustrating game BCI experiments Reuderink Nijholt Poel | Paper (Springer/EUDL) and BNCI Horizon 2020 dataset 007-2014 description |
| 3 | Abler Walter Erk 2005 "Neural correlates of frustration" | PubMed record (DOI, abstract) |
| 4 | history of cue reactivity paradigm earliest studies 1970s 1980s | No origin found; PMC pages blocked by a browser check |
| 5 | Littel 2012 electrophysiological indices of substance-related cues meta-analysis | Found only as Erasmus doctoral thesis (no DOI); not cited |
| 6 | real-time fMRI neurofeedback nicotine craving Canterberry Hanlon 2013 | Hartwell et al. (J Psychiatry Neurosci 41(1):48) and Li et al. author copy |
| 7 | Hartwell 2016 J Psychiatry Neurosci individualized rtfMRI neurofeedback craving | Li et al. Addiction Biology author PDF (methods, timing, DOI) |
| 8 | Spitzer Wacker Blankenburg 2010 vibrotactile frequency working memory EEG beta | von Lautz et al. 2017 full text (trial timing) |
| 9 | Spence 2001 deception fMRI paradigm truth/lie cue | Only later papers; Spence protocol details not found |
| 10 | Phillips Edwards 1966 conservatism probability inference | LSE repository record (no DOI) |
| 11 | Christ et al. 2009 prefrontal cortex executive control deception meta-analysis | Washington University profile page with DOI and abstract |
| 12 | van Berkum Hagoort Brown 1999 discourse N400 presentation | MPI page; timing not obtained |
| 13 | negative priming ERP N2 P300 ignored repetition | Frings & Groh-Bordin 2007 (research portal record with abstract and DOI) |
| 14 | OpenNeuro beads task / jumping to conclusions | No public beads dataset found |
| 15 | OpenNeuro food cue reactivity or deception | OpenfMRI ds000157 (food vs non-food picture blocks); no deception dataset |

## Pages and API records read

| URL / record | Outcome |
|---|---|
| Crossref 10.1037/h0025953 | Posner & Keele 1968, record copied |
| Crossref query: Spence 2001 deception | 10.1097/00001756-200109170-00019; also NeuroImage 2001 conference abstract (not cited) |
| Crossref query: Huq Garety Hemsley 1988 | 10.1080/14640748808402300; PsycTESTS "Beads Task" entry (not cited) |
| Crossref query: Carter & Tiffany 1999 | 10.1046/j.1360-0443.1999.9433273.x |
| Crossref query: Li et al. rtfMRI craving | irrelevant hits; DOI found in the author PDF instead |
| Crossref queries: Tipper 1985; van Berkum 1999 | failed (fetch error; HTTP 429) |
| OpenAlex search: van Berkum 1999; Tipper 1985; St George 1994; Preuschhof 2006; Reber 1998; Abler 2005; Furl & Averbeck 2011; Grant 1996 | records found for all except St George 1994 (not found) and Abler 2005 (not in the first results) |
| OpenAlex search: Affective Pacman; Littel 2012; Li et al. 2012 | HTTP 429 / fetch error |
| BNCI 007-2014 description PDF (lampx.tugraz.at) | Affective Pacman dataset: 12 recorded, 10 public, 32-ch EEG, references with DOIs |
| PubMed 15858403 | Abler 2005 abstract and DOI |
| Drug cue article (mdwiki mirror) | Procedure overview; no origin |
| PMC4737433; PubMed 22458676 | blocked by browser check |
| Erasmus repository 32476 | Littel 2012 thesis abstract (P300/LPP meta-analysis); no DOI |
| J Psychiatry Neurosci node 85342 | Hartwell et al. methods (cue blocks 22 s, 4.4 s pictures); not cited (no Crossref record retrieved) |
| Li et al. author PDF (Yale course page) | Title, authors, DOI and cue/feedback timing |
| Frontiers 10.3389/fnhum.2017.00576 full text | Trial timing, 768 trials, primate origin of task |
| bioRxiv 10.1101/089847 | Later instructed-lying study; Spence protocol not described |
| LSE eprint 27235 | Phillips & Edwards 1966 record, no DOI |
| WUSTL profile: Christ et al. | DOI 10.1093/cercor/bhn189, abstract |
| OpenfMRI ds000157 | Food/non-food block design, 30 participants |
| Research portal record 123959 | Frings & Groh-Bordin 2007 citation and abstract |
| Crossref per-DOI: 10.1080/14640748808402300, 10.1523/JNEUROSCI.4236-11.2011, 10.1080/14640748508400920, 10.1073/pnas.93.21.12040, 10.1046/j.1360-0443.1999.9433273.x, 10.1111/j.1369-1600.2012.00449.x, 10.1007/978-3-642-02315-6_23, 10.1109/TNSRE.2011.2166562, 10.1097/00001756-200109170-00019, 10.1162/089892999563724, 10.1073/pnas.95.2.747, 10.1016/j.brainres.2007.07.093 | records copied |
| Crossref per-DOI refused (HTTP 429): 10.1097/00001756-200505120-00003, 10.1523/jneurosci.2767-06.2006, 10.1523/jneurosci.6041-09.2010, 10.3758/BF03210958, 10.1080/23273798.2016.1211300 | OpenAlex per-DOI used for the first three; Fox 1995 and Lewis 2016 rely on OpenAlex search listings |
| OpenAlex per-DOI: 10.1097/00001756-200505120-00003, 10.1523/jneurosci.2767-06.2006, 10.1523/jneurosci.6041-09.2010, 10.3389/fnhum.2017.00576, 10.1093/cercor/bhn189 | records copied (Christ et al.: OpenAlex year 2008, online first) |
| OpenAlex pmid:23578759 (de Ridder et al., ds000157 paper) | HTTP 429; not cited |
