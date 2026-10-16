# Search log - sprint 7, group Q2 (2026-10-17)

Web searches: 10 of 30 allowed. Bibliographic records: Crossref API (`https://api.crossref.org/works/<DOI>` and title search `https://api.crossref.org/works?query.bibliographic=...`), OpenAlex API (`https://api.openalex.org/works/doi:<DOI>` and `works?search=`) where Crossref returned HTTP 429 or no record. Several requests were rate-limited (HTTP 429) and not repeated.

## Web searches

| # | Query | Outcome |
|---|---|---|
| W01 | Davis Wallace 1942 "standardized hyperventilation" electroencephalogram Archives of Neurology and Psychiatry | No direct hit; JAMA page found was an unrelated Davis 1943 paper (blood sugar). BSCN hyperventilation guideline (PDF, no DOI) noted for the 3 min duration. Paper then found by Crossref title search (C15) |
| W02 | Hashimoto 1987 somatosensory evoked potentials elicited by air-puff stimuli high-speed air control system | Hashimoto 1987 not found; PubMed hit "Short-latency cortical potentials evoked by tactile air-jet stimulation of body and face in man" (PubMed page could not be read; record taken from Crossref, C12) |
| W03 | Pratt Starr 1979 mechanically and electrically evoked somatosensory potentials in normal humans Neurology | Only repository PDFs; records found by Crossref title search (C13) |
| W04 | BNCI Horizon 2020 "Music BCI" dataset Treder polyphonic attention EEG | Treder et al. 2014 accepted manuscript (Aalborg repository, musicBCI_11.pdf), Cardiff ORCA abstract, MAD-EEG Zenodo records 4537750/4537751 |
| W05 | OpenNeuro Healthy Brain Network EEG release surroundSupp task ds005505 | HBN-EEG preprint (bioRxiv 10.1101/2024.10.03.615261), EEGDash catalogue |
| W06 | "ds005505" OpenNeuro "Healthy Brain Network" EEG Release 1 | NEMAR forum page for ds005505 links it to the HBN-EEG manuscript; task list not on the page |
| W07 | Müller Andersen 2006 PNAS feature-selective attention red blue dots flickering frequencies SSVEP trial duration | Aberdeen research portal abstract (stimulus and results; no frequency values) |
| W08 | bnci-horizon-2020.eu database "Music" Treder Blankertz auditory attention instruments dataset download | No public dataset of Treder et al. 2014 found; ADASP page for MAD-EEG |
| W09 | Kekoni 1997 "Rate effect and mismatch responses in the somatosensory system" stimuli | CORE record with an abstract (vibratory stimuli for ERP, electric for MEG; deviants in site or frequency) |
| W10 | Zhang Maye Gao Hong Engel Gao 2010 independent BCI covert non-spatial visual selective attention | Hamburg-Eppendorf research portal abstract (two superimposed counter-rotating surfaces, online, 18 participants, 72.6%) |

## Pages read

| URL | Outcome |
|---|---|
| https://vbn.aau.dk/ws/files/197609875/musicBCI_11.pdf | Treder et al. 2014 methods: Synth-Pop and Jazz, 40 s clips, 3-7 deviants per instrument, visual cue with preview, counting task, 210 clips, 11 participants |
| https://orca.cardiff.ac.uk/id/eprint/115686/ | Treder et al. 2014 abstract (multi-streamed oddball, 91% offline accuracy) |
| https://zenodo.org/record/4537751 | MAD-EEG dataset: 8 participants, 20-channel EEG, attention to a target instrument |
| https://adasp.telecom-paris.fr/resources/2020-09-21-mad-eeg-database/ | MAD-EEG overview only; protocol details not given |
| https://www.biorxiv.org/content/10.1101/2024.10.03.615261v2 and .full.pdf | HBN surround suppression task: four flashing peripheral disks, 25 Hz, two runs of about 3.6 min; accession table not in the text |
| https://nemar-dev.ucsd.edu/forum/nemar-datasets/ds005505/971 | ds005505 = HBN-EEG |
| https://abdn.elsevierpure.com/en/publications/feature-selective-attention-enhances-color-signals-in-early-visua | Müller et al. 2006 abstract |
| https://fis.uke.de/portal/de/publications/an-independent-braincomputer-interface-using-covert-nonspatial-visual-selective-attention(...).html | Zhang et al. 2010 abstract |
| https://core.ac.uk/works/6197256 | Somatosensory MMN abstract (stimulus types) |
| https://jamanetwork.com/journals/archneurpsyc/article-abstract/649507 | Unrelated (Davis 1943, blood sugar); not used |
| https://pubmed.ncbi.nlm.nih.gov/6208008/ | Page content not readable; not used |

## Bibliographic API records

| # | Request | Outcome |
|---|---|---|
| C01 | Crossref 10.1088/1741-2560/11/2/026009 | Treder et al. 2014, J Neural Eng 11(2):026009 |
| C02 | Crossref 10.1073/pnas.0606358103 (DOI noted for Müller et al. 2006 before the check) | HTTP 429; OpenAlex also 429. Not used |
| C03 | Crossref title search "Feature-selective attention enhances color signals..." | Müller et al. 2006, DOI 10.1073/pnas.0606668103, PNAS 103(38):14250-14254 (the DOI in C02 was not the paper's DOI) |
| C04 | Crossref 10.1088/1741-2560/7/1/016010 | Zhang et al. 2010, J Neural Eng 7(1):016010 |
| C05 | Crossref 10.1038/nn876 | Saenz, Buracas & Boynton 2002, Nat Neurosci 5(7):631-632 |
| C06 | Crossref 10.1073/pnas.86.23.9631 | Chubb, Sperling & Solomon 1989, PNAS 86(23):9631-9635 |
| C07 | Crossref 10.1152/jn.00774.2014 | Vanegas, Blangero & Kelly 2015, J Neurophysiol 113(4):1100-1109 |
| C08 | Crossref 10.1093/cercor/bhv043 | Schulz et al. 2015, Cereb Cortex 25(11):4407-4414 |
| C09 | Crossref 10.1016/S0002-8703(36)90370-8 | HTTP 429; OpenAlex record: Hines & Brown 1936, Am Heart J 11(1):1-9 |
| C10 | Crossref 10.1016/S0301-0511(97)05249-6 | Kekoni et al. 1997, Biol Psychol 46(2):125-142 |
| C11 | Crossref 10.1016/j.clinph.2004.09.014; 10.1371/journal.pone.0286023; 10.1038/scientificamerican1073-94 | Schwarz & Taylor 2005; Ingendoh, Posny & Heine 2023; Oster 1973 |
| C12 | Crossref title search "Short-latency cortical potentials evoked by tactile air-jet..." | Schieppati & Ducati 1984, EEG Clin Neurophysiol 58(5):418-425. Crossref 10.1016/0013-4694(87)90021-1 (a DOI tried for Hashimoto 1987) returned an error; not used |
| C13 | Crossref title search "Mechanically and electrically evoked somatosensory potentials in normal humans" | Pratt et al. 1979 (Neurology abstract, 1 page), Kakigi & Shibasaki 1984, Pratt & Starr 1981, Pratt, Politoske & Starr 1980 |
| C14 | Crossref title search "Somatosensory response to mechanical stimulation as recorded in the human EEG" | Larsson & Prevec 1970, EEG Clin Neurophysiol 28(2):162-172 |
| C15 | Crossref title search "Factors affecting changes produced in electroencephalogram by standardized hyperventilation" | Davis 1942, Arch Neurol Psychiatry 47(4):606 (one author in the record) |
| C16 | Crossref 10.1001/archneurpsyc.1935.02250240002001 | Gibbs 1935 (epilepsy EEG); hyperventilation content not confirmed, not cited |
| C17 | Crossref 10.1161/01.STR.29.12.2641 | Kastrup et al. 1998, Stroke 29(12):2641-2645 |
| C18 | Crossref 10.1016/j.brainres.2017.12.037; 10.1016/j.neubiorev.2017.05.003 | Salvati & Beenhakker 2019; Urback, MacIntosh & Goldstein 2017 |
| C19 | Crossref 10.1038/sdata.2017.181 | Alexander et al. 2017 (HBN resource); not cited |
| C20 | Crossref 10.1038/sdata.2017.40 | HTTP 429; OpenAlex record: Langer et al. 2017, Sci Data 4:170040 |
| C21 | Crossref 10.1101/2024.10.03.615261 | Error; OpenAlex record: Shirazi et al. 2024 (bioRxiv preprint) |
| C22 | OpenAlex search "MAD-EEG ..." | Cantisani et al. 2019, SMM 2019 pp. 51-55, DOI 10.21437/smm.2019-11 |
| C23 | Crossref title search "Chen Dworkin Topographic brain measures of human pain..." | HTTP 429; not cited |
| C24 | Europe PMC search for PubMed 6208008 | HTTP 429; not used |
