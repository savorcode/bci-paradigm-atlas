# 包 A sprint 3 出处核实：抓取日志 / Fetch log (curator_e, 2026-10-05)

Tool: WebFetch only (Bash has no egress). Crossref and OpenAlex single-record endpoints worked; both bibliographic **search** endpoints and the PubMed article page were refused (429 / reCAPTCHA) for the whole session, so title-only and TBD rows were resolved by fetching a DOI/PMID record known to the checker and accepting it only when the record title matched (noted per row in sources_check.csv). Refused URLs were never retried.

| # | URL | outcome |
|---|---|---|
| 1 | https://api.crossref.org/works/10.1093/cercor/bht355 | OK: O'Sullivan 2014 Cereb Cortex 25(7):1697-1706 |
| 2 | https://api.crossref.org/works/10.1037/0096-1523.18.3.849 | 429 (parallel burst) -> OpenAlex fallback |
| 3 | https://api.crossref.org/works/10.1126/science.1063414 | OK: Downing 2001 Science 293(5539):2470-2473 |
| 4 | https://api.crossref.org/works/10.1038/35784 | 429 (parallel burst) -> OpenAlex fallback |
| 5 | https://api.crossref.org/works/10.1006/cogp.1998.0681 | OK: Chun & Jiang 1998 Cogn Psychol 36(1):28-71 |
| 6 | https://api.crossref.org/works/10.1080/00335558008248231 | OK: Posner 1980 QJEP 32(1):3-25 |
| 7 | https://api.openalex.org/works/doi:10.1037/0096-1523.18.3.849 | OK: Raymond 1992 JEP:HPP 18(3):849-860 |
| 8 | https://api.openalex.org/works/doi:10.1038/35784 | OK: Botvinick & Cohen 1998 Nature 391(6669):756; pmid 9486643 |
| 9 | https://api.crossref.org/works/10.1523/JNEUROSCI.0875-06.2006 | OK: Thut 2006 J Neurosci 26(37):9494-9502 |
| 10 | https://api.crossref.org/works/10.1007/bf00998623 | OK: Whitehead 1977 Biofeedback Self-Regul 2(4):371-392 |
| 11 | https://api.crossref.org/works/10.1111/j.1469-8986.1981.tb02486.x | OK: Schandry 1981 Psychophysiology 18(4):483-488 |
| 12 | https://api.crossref.org/works/10.1371/journal.pbio.0050260 | OK: Del Cul 2007 PLoS Biol 5(10):e260 |
| 13 | https://api.crossref.org/works/10.1016/0001-6918(78)90006-9 | OK: Naatanen 1978 Acta Psychol 42(4):313-329 |
| 14 | https://api.crossref.org/works/10.1163/156856888x00122 | OK: Pylyshyn & Storm 1988 Spatial Vision 3(3):179-197 |
| 15 | https://api.crossref.org/works/10.1038/264746a0 | OK: McGurk & MacDonald 1976 Nature 264(5588):746-748 |
| 16 | https://api.crossref.org/works/10.1088/1741-2560/5/4/011 | OK: Guo 2008 J Neural Eng 5(4):477-485 |
| 17 | https://api.crossref.org/works/10.1016/0010-0285(77)90012-3 | OK: Navon 1977 Cogn Psychol 9(3):353-383 |
| 18 | https://api.crossref.org/works/10.1126/science.150.3700.1187 | OK: Sutton 1965 Science 150(3700):1187-1188 |
| 19 | https://api.crossref.org/works/10.1016/0013-4694(75)90263-1 | OK: Squires 1975 EEG Clin Neurophysiol 38(4):387-401 |
| 20 | https://api.crossref.org/works/10.1016/0013-4694(88)90149-6 | OK: Farwell & Donchin 1988 EEG Clin Neurophysiol 70(6):510-523 |
| 21 | https://api.crossref.org/works/10.1037/0278-7393.2.5.509 | OK: Potter 1976 JEP:HLM 2(5):509-522 |
| 22 | https://api.crossref.org/works/10.1016/j.clinph.2012.12.050 | OK: Acqualagna & Blankertz 2013 Clin Neurophysiol 124(5):901-908 |
| 23 | https://api.crossref.org/works/10.1016/j.clinph.2010.01.030 | OK: Townsend 2010 Clin Neurophysiol 121(7):1109-1120 |
| 24 | https://api.crossref.org/works/10.1016/j.jneumeth.2007.03.005 | OK: Hoffmann 2008 J Neurosci Methods 167(1):115-125 |
| 25 | https://api.crossref.org/works/10.3389/fnins.2011.00112 | OK: Schreuder 2011 Front Neurosci 5 (article no. not in record) |
| 26 | https://api.crossref.org/works/10.3389/fnins.2010.00019 | OK (partial): Brouwer 2010 Front Neurosci; authors truncated in record |
| 27 | https://api.crossref.org/works/10.1523/JNEUROSCI.5821-12.2013 | OK: SanMiguel 2013 J Neurosci 33(20):8633-8639 |
| 28 | https://api.crossref.org/works/10.1073/pnas.93.6.2382 | OK: DeYoe 1996 PNAS 93(6):2382-2386 |
| 29 | https://api.crossref.org/works/10.1016/j.neuroimage.2007.09.034 | OK: Dumoulin & Wandell 2008 NeuroImage 39(2):647-660 |
| 30 | https://api.crossref.org/works/10.1152/jn.01125.2002 | 429 proxy rate limit -> OpenAlex fallback |
| 31 | https://api.openalex.org/works/doi:10.1152/jn.01125.2002 | OK: Talavage 2004 J Neurophysiol 91(3):1282-1296; pmid 14614108 |
| 32 | https://api.crossref.org/works/10.1016/0010-0285(80)90005-5 | OK: Treisman & Gelade 1980 Cogn Psychol 12(1):97-136 |
| 33 | https://api.crossref.org/works/10.1016/j.jneumeth.2011.02.007 | 429 proxy rate limit -> OpenAlex fallback |
| 34 | https://api.openalex.org/works/doi:10.1016/j.jneumeth.2011.02.007 | OK: Kim 2011 J Neurosci Methods 197(1):180-185; pmid 21335029 |
| 35 | https://api.crossref.org/works/10.1523/JNEUROSCI.0411-11.2011 | OK: Nozaradan 2011 J Neurosci 31(28):10234-10240 |
| 36 | https://api.openalex.org/works/doi:10.1371/journal.pone.0133797 | OK: Thielen 2015 PLoS ONE 10(7):e0133797; pmid 26208328 |
| 37 | https://api.crossref.org/works/10.1016/j.neuroimage.2023.120446 | OK: Cabrera Castillos 2023 NeuroImage 284:120446 |
| 38 | https://api.openalex.org/works/doi:10.1016/0013-4694(68)90085-0 | OK: Worden & Marsh 1968 EEG Clin Neurophysiol 25(1):42-52; pmid 4174782 |
| 39 | https://api.crossref.org/works/10.1111/ejn.12663 | OK: Boremanse 2014 Eur J Neurosci 40(6):2987-2997 |
| 40 | https://api.openalex.org/works/doi:10.1523/JNEUROSCI.3977-10.2011 | OK: Mouraux 2011 J Neurosci 31(16):6079-6087; pmid 21508233 |
| 41 | https://api.crossref.org/works/10.3389/fnhum.2015.00716 | 429 -> OpenAlex fallback |
| 42 | https://api.openalex.org/works/doi:10.3389/fnhum.2015.00716 | OK: Ahn, Kim, Jun 2016 Front Hum Neurosci 9:716; pmid 26834611 (review) |
| 43 | https://api.crossref.org/works/10.1016/0013-4694(66)90088-5 | 429 -> OpenAlex fallback |
| 44 | https://api.openalex.org/works/doi:10.1016/0013-4694(66)90088-5 | OK: Regan 1966 EEG Clin Neurophysiol 20(3):238-248; pmid 4160391 |
| 45 | https://api.openalex.org/works/doi:10.1109/86.847819 | OK: Middendorf 2000 IEEE Trans Rehabil Eng 8(2):211-214; pmid 10896190 |
| 46 | https://api.openalex.org/works/doi:10.1073/pnas.93.10.4770 | OK: Morgan 1996 PNAS 93(10):4770-4774; pmid 8643478 |
| 47 | https://api.openalex.org/works/doi:10.1371/journal.pone.0140703 | OK: Nakanishi 2015 PLoS ONE 10(10):e0140703; pmid 26479067 |
| 48 | https://api.openalex.org/works/doi:10.1016/j.neucom.2016.01.007 | OK: Kalunga 2016 Neurocomputing 191:55-68 (6 authors) |
| 49 | https://pubmed.ncbi.nlm.nih.gov/1763252/ | REFUSED: Google reCAPTCHA page (PubMed blocked for this client); PubMed not used further |
| 50 | https://api.openalex.org/works/pmid:1763252 | OK: Bromm & Treede 1991 Rev Neurol (Paris) 147(10):625-643; no DOI |
| 51 | https://api.openalex.org/works/pmid:7342998 | OK: Lawson & Gaillard 1981 Biol Psychol 13:281-288; doi 10.1016/0301-0511(81)90043-0 |
| 52 | https://api.openalex.org/works/pmid:14706481 | OK: Naatanen, Pakarinen, Rinne, Takegata; Clin Neurophysiol 115(1):140-144; doi 10.1016/j.clinph.2003.04.001 (OpenAlex year 2003 = online date; print Jan 2004) |
| 53 | https://api.openalex.org/works/pmid:15016991 | OK: Hasson, Nir, Levy, Fuhrmann Alpert, Malach 2004 Science 303(5664):1634-1640; doi 10.1126/science.1089506 |
| 54 | https://api.crossref.org/works?query.bibliographic=Bentin+Electrophysiological+Studies+of+Face+Perception+in+Humans+1996&rows=3&select=... | 429 |
| 55 | https://api.openalex.org/works?search=Electrophysiological Studies of Face Perception in Humans&per-page=3 | 429 |
| 56 | https://api.openalex.org/works/doi:10.1016/j.clinph.2003.04.001 | OK: publication_date 2003-12-04 (online); 115(1):140-144 |
| 57 | https://api.crossref.org/works/10.1016/j.clinph.2003.04.001 | 429 |
| 58 | https://api.openalex.org/works?filter=title.search:40-Hz auditory potential... | 429 (OpenAlex search endpoints throttled; single-work endpoint still OK) |
| 59 | https://api.crossref.org/works?query.bibliographic=Galambos+Makeig+Talmachoff+A+40-Hz+auditory+potential... | 429 proxy |
| 60 | https://api.openalex.org/works?search=40-Hz auditory potential recorded from the human scalp | 429 |
| 61 | https://api.openalex.org/works/doi:10.1126/science.1089506 | OK (probe): Hasson 2004 |
| 62 | https://api.openalex.org/works/doi:10.1162/jocn.1996.8.6.551 | OK: Bentin, Allison, Puce, Perez, McCarthy 1996 J Cogn Neurosci 8(6):551-565; pmid 20740065 (title matches PER-FACE-001) |
| 63 | https://api.crossref.org/works/10.1073/pnas.0809667106 | 429 |
| 64 | https://api.openalex.org/works/doi:10.1073/pnas.0809667106 | OK: Bekinschtein et al. 2009 PNAS 106(5):1672-1677; pmid 19164526 (title matches PER-LG-001) |
| 65 | https://api.openalex.org/works/doi:10.1037/0096-1523.27.5.1072 | OK but different paper (Alain, Arnott, Picton 2001 'Bottom-up and top-down influences...'); not PER-ORN-001 title |
| 66 | https://api.openalex.org/works/doi:10.1121/1.1434942 | OK: Alain, Schuler, McDonald 2002 JASA 111(2):990-995; pmid 11863201 (title matches PER-ORN-001) |
| 67 | https://api.openalex.org/works/doi:10.1017/S0048577299971056 | OK: Sussman, Ritter, Vaughan 1999 Psychophysiology 36(1):22-34; pmid 10098377 (matches PER-STREAM-001) |
| 68 | https://api.openalex.org/works/doi:10.1073/pnas.78.4.2643 | OK: Galambos, Makeig, Talmachoff 1981 PNAS 78(4):2643-2647; pmid 6941317 (matches SSR-ASSR-001) |
| 69 | https://api.openalex.org/works/doi:10.1371/journal.pone.0039707 | OK: Xie, Xu, Wang, Zhang, Zhang 2012 PLoS ONE 7(6):e39707; pmid 22724028 (matches SSR-SSMVEP-001) |
| 70 | https://api.openalex.org/works/doi:10.1073/pnas.1508080112 | OK: Chen, Wang, Nakanishi, Gao, Jung, Gao 2015 PNAS 112(44):E6058-E6067; pmid 26483479 (matches SSR-SSVEP-005) |
| 71 | https://api.openalex.org/works/doi:10.1162/imag_a_00223 | OK: Ladouce, Dehais 2024 Imaging Neuroscience 2; pmid 40800282 (matches SSR-SSVEP-004 variant) |
| 72 | https://api.openalex.org/works/doi:10.1177/000348946707600211 | 429 proxy (Sohmer & Feinmesser 1967 candidate; not retried) |
| 73 | https://api.openalex.org/works/doi:10.1093/brain/94.4.681 | OK: Jewett & Williston 1971 Brain 94(4):681-696 'Auditory-evoked far fields averaged from the scalp of humans'; pmid 5132966 (PER-ABR) |
| 74 | https://api.openalex.org/works/doi:10.1097/00003446-199808000-00004 | OK: Ostroff, Martin, Boothroyd 1998 Ear Hear 19(4):290-297; pmid 9728724 (PER-ACC) |
| 75 | https://api.openalex.org/works/doi:10.3758/BF03211656 | OK: Theeuwes 1992 Percept Psychophys 51(6):599-606; pmid 1620571 (PER-ADDS) |
| 76 | https://api.openalex.org/works/doi:10.1152/jn.1939.2.6.494 | OK: Davis PA 1939 J Neurophysiol 2(6):494-499 (PER-AEP) |
| 77 | https://api.openalex.org/works/doi:10.1103/PhysRev.23.266 | OK: Wegel & Lane 1924 Phys Rev 23(2):266-285 (PER-AMASK) |
| 78 | https://api.openalex.org/works/doi:10.1098/rstl.1838.0019 | OK: Wheatstone 1838 Phil Trans R Soc Lond 128:371-394 (PER-BR) |
| 79 | https://api.openalex.org/works/doi:10.1126/science.146.3649.1325 | OK: Lansing 1964 Science 146(3649):1325-1327; pmid 14207465 (PER-BR-002) |
| 80 | https://api.openalex.org/works/doi:10.1111/j.1467-9280.1997.tb00427.x | OK: Rensink, O'Regan, Clark 1997 Psychol Sci 8(5):368-373 (PER-CB) |
| 81 | https://api.openalex.org/works/doi:10.1016/j.jneumeth.2009.01.016 | OK: van Gerven & Jensen 2009 J Neurosci Methods 179(1):78-84; pmid 19428515 (PER-CVA-002) |
| 82 | https://api.openalex.org/works/doi:10.1016/0013-4694(61)90132-8 | 429 proxy |
| 83 | https://api.crossref.org/works/10.1016/0013-4694(61)90132-8 | OK: Ciganek L 1961 EEG Clin Neurophysiol 13(2):165-172 'The EEG response (evoked potential) to light stimulus in man' (PER-FVEP) |
| 84 | https://api.crossref.org/works/10.1016/0168-5597(85)90055-3 | 429 proxy |
| 85 | https://api.openalex.org/works/doi:10.1016/0168-5597(85)90055-3 | OK: Kobal 1985 EEG Clin Neurophysiol/Evoked Potentials Section 62(6):449-454; pmid 2415341 (PER-GEP) |
| 86 | https://api.openalex.org/works/doi:10.7551/mitpress/3707.001.0001 | OK: Mack & Rock 1998 Inattentional Blindness, MIT Press (book) (PER-IB) |
| 87 | https://api.openalex.org/works/doi:10.1038/scientificamerican0476-48 | OK: Kanizsa 1976 Sci Am 234(4):48-52; pmid 1257734 (PER-IC) |
| 88 | https://api.openalex.org/works/doi:10.1126/science.128.3333.1210 | OK: Geisler, Frishkopf, Rosenblith 1958 Science 128(3333):1210-1211; pmid 13592309 (PER-MLR) |
| 89 | https://api.openalex.org/works/doi:10.1162/089892999563544 | OK: Giard & Peronnet 1999 J Cogn Neurosci 11(5):473-490; pmid 10511637 (PER-MSI-002) |
| 90 | https://api.openalex.org/works/doi:10.1007/BF00161234 | OK: Kuba & Kubova 1992 Doc Ophthalmol 80(1):83-89; pmid 1505342 (PER-MVEP-001) |
| 91 | https://api.openalex.org/works/doi:10.1016/0168-5597(88)90023-8 | OK: Kobal & Hummel 1988 EEG Clin Neurophysiol/EP Section 71(4):241-250; pmid 2454788 (PER-OLF) |
| 92 | https://api.openalex.org/works/doi:10.1126/science.155.3768.1436 | OK: Sutton, Tueting, Zubin, John 1967 Science 155(3768):1436-1439; pmid 6018511 (PER-OMIT-001) |
| 93 | https://api.openalex.org/works/doi:10.1016/S0140-6736(72)91155-5 | OK: Halliday, McDonald, Mushin 1972 Lancet 299(7758):982-985; pmid 4112367 (PER-PRVEP) |
| 94 | https://api.openalex.org/works/doi:10.1152/jappl.1986.60.6.1843 | OK: Davenport, Friedman, Thompson, Franzen 1986 J Appl Physiol 60(6):1843-1848; pmid 3722053 (PER-RREP) |
| 95 | https://api.openalex.org/works/doi:10.1111/j.1469-8986.1987.tb00353.x | OK: Damen & Brunia 1987 Psychophysiology 24(6):700-713; pmid 3438435 (PER-SPN) |
| 96 | https://api.openalex.org/works/doi:10.1113/jphysiol.1977.sp012025 | 429 proxy (Desmedt & Robertson 1977 candidate for PER-TACT; not retried) |
| 97 | https://api.crossref.org/works/10.1113/jphysiol.1977.sp012025 | OK: Desmedt & Robertson 1977 J Physiol 271(3):761-782 (PER-TACT) |
| 98 | https://api.openalex.org/works/doi:10.1097/00001756-199911080-00020 | OK: Tales, Newton, Troscianko, Butler 1999 NeuroReport 10(16):3363-3367; pmid 10599846 (PER-VMMN) |
| 99 | https://api.openalex.org/works/doi:10.1038/35002078 | OK: Belin, Zatorre, Lafaille, Ahad, Pike 2000 Nature 403(6767):309-312; pmid 10659849 (PER-VOICE) |
| 100 | https://api.openalex.org/works/doi:10.1016/0745-7138(92)90045-7 | OK: Sutter 1992 J Microcomput Appl 15(1):31-45 (SSR-CVEP-001) |
| 101 | https://api.openalex.org/works/doi:10.1016/j.clinph.2004.04.003 | OK: Russo(-Ponsaran), Nicol, Musacchia, Kraus 2004 Clin Neurophysiol 115(9):2021-2030; pmid 15294204 (SSR-FFR-002) |
| 102 | https://api.openalex.org/works/doi:10.1016/j.neuropsychologia.2013.10.022 | OK: Liu-Shuang, Norcia, Rossion; Neuropsychologia 52:57-72 (OpenAlex year 2013 = online; print vol 52 = 2014); pmid 24200921 (SSR-FPVS) |
| 103 | https://api.openalex.org/works/doi:10.1162/jocn_a_00288 | OK: Mathewson, Prudhomme, Fabiani, Beck, Lleras, Gratton 2012 J Cogn Neurosci 24(12):2321-2333; pmid 22905825 (SSR-RVS) |
| 104 | https://api.openalex.org/works/doi:10.1016/0168-5597(92)90007-X | OK: Snyder 1992 EEG Clin Neurophysiol/EP Section 84(3):257-268; pmid 1375885 (SSR-SSSEP-001) |
| 105 | https://api.openalex.org/works/doi:10.1155/2009/864564 | OK: Parini, Maggi, Turconi, Andreoni 2009 Comput Intell Neurosci 2009:864564; pmid 19421416 (SSR-SSVEP-008) |
| 106 | https://api.openalex.org/works/pmid:7104417 | OK: Adler, Pachtman, Franks, Pecevich, Waldo, Freedman 1982 Biol Psychiatry 17(6):639-654; no DOI (PER-GATE) |

Total fetches: 106 (budget ~170).
