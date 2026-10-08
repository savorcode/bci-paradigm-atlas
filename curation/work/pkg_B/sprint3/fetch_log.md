# 包 B sprint 3 · 抓取日志 / fetch log（curator_a，2026-10-05）

共 103 次 WebFetch（成功 84，被拒/错误 19）。只用 WebFetch；未用 WebSearch。被拒的 URL 一律不重试；同一文献改用另一来源（Crossref ↔ OpenAlex）。

## 可达性观察 / Endpoint behaviour

- Crossref `works/<DOI>`：可用，但约每隔几次就被代理以 429 拒绝（"rate limited"），之后约 1 分钟内对该主机的请求多被拒。
- Crossref `works?query.bibliographic=`：同上；URL 过长（含 select= 参数）时代理返回 403。本次只成功 5 次检索。
- OpenAlex `works/doi:<DOI>` 与 `works/pmid:<PMID>`：可用（偶发 429）；是本次的主要来源。
- OpenAlex `works?search=` / `works?filter=title.search:`：6 次尝试全部 429（匿名池对列表接口限流）。因此多数无 DOI 条目改为"按候选 DOI 取记录并与引文逐项比对"（仅当题名、第一作者、年份、卷页一致时才写入 DOI）。
- PubMed 文章页：返回 reCAPTCHA 页面，不可用；PMID 行全部改用 OpenAlex `pmid:` 查询，`matched_pmid` 一律留空（未在 PubMed 上看到）。

## 逐条记录 / Entries

| # | URL | 结果 / outcome | 备注 / note |
|---|---|---|---|
| 1 | `https://api.crossref.org/works/10.1371/journal.pone.0123727` | OK | IMG-MA-002: Scherer R, Faller J, Friedrich EVC, Opisso E, Costa U, Kübler A, Müller-Putz GR. Individually Adapted Imagery Improves Brain-Computer Interface Performance in End-Users with Disability. PLOS ONE 2015;10(5):e0123727 |
| 2 | `https://api.crossref.org/works/10.1126/science.171.3972.701` | OK | IMG-ROT-001: Shepard RN, Metzler J. Science 1971;171(3972):701-703 confirmed |
| 3 | `https://api.crossref.org/works/10.1371/journal.pone.0064784` | 429 proxy rejected | IMG-SAO-001 |
| 4 | `https://api.openalex.org/works/doi:10.1371/journal.pone.0064784` | OK | IMG-SAO-001: Yao L, Meng J, Zhang D, Sheng X, Zhu X. PLoS ONE 2013;8(6):e64784; PMID 23762253 confirmed |
| 5 | `https://api.crossref.org/works/10.1523/ENEURO.0455-22.2023` | OK | IMG-TACT-001: Yakovlev L, Syrov N, Miroshnikov A, Lebedev M, Kaplan A. eNeuro 2023;10(6):ENEURO.0455-22.2023 confirmed |
| 6 | `https://api.crossref.org/works/10.1126/science.284.5411.167` | OK | IMG-VIS-001: Kosslyn SM, Pascual-Leone A, Felician O, Camposano S, Keenan JP, Thompson WL, Ganis G, Sukel KE, Alpert NM. The Role of Area 17 in Visual Imagery: Convergent Evidence from PET and rTMS. Science 1999;284(5411):167-170 |
| 7 | `https://api.crossref.org/works/10.1038/s41598-019-43594-9` | OK | MOT-ATT-003: Ofner P, Schwarz A, Pereira J, Wyss D, Wildburger R, Müller-Putz GR. Attempted Arm and Hand Movements can be Decoded from Low-Frequency EEG from Persons with Spinal Cord Injury. Sci Rep 2019;9(1):7134 |
| 8 | `https://api.crossref.org/works/10.1152/ajpregu.1984.246.6.r1000` | OK | MOT-BIMAN-001: Kelso JA. Am J Physiol Regul Integr Comp Physiol 1984;246(6):R1000-R1004 |
| 9 | `https://api.crossref.org/works/10.1016/0013-4694(91)90040-B` | OK | MOT-CURSOR-001: Wolpaw JR, McFarland DJ, Neat GW, Forneris CA. Electroencephalogr Clin Neurophysiol 1991;78(3):252-259 |
| 10 | `https://api.crossref.org/works/10.1073/pnas.0403504101` | OK | MOT-CURSOR-002: Wolpaw JR, McFarland DJ. PNAS 2004;101(51):17849-17854 |
| 11 | `https://api.crossref.org/works/10.3389/fnins.2020.00849` | 429 proxy rejected | MOT-GRASP-003 |
| 12 | `https://api.openalex.org/works/doi:10.3389/fnins.2020.00849` | OK | MOT-GRASP-003: Schwarz A, Escolano C, Montesano L, Müller-Putz GR. Analyzing and Decoding Natural Reach-and-Grasp Actions Using Gel, Water and Dry EEG Systems. Front Neurosci 2020;14:849; PMID 32903775 |
| 13 | `https://api.crossref.org/works/10.1101/2020.07.01.183384` | OK | MOT-HW-001: Willett FR, Avansino DT, Hochberg LR, Henderson JM, Shenoy KV. High-performance brain-to-text communication via imagined handwriting. bioRxiv 2020 (posted-content) |
| 14 | `https://api.openalex.org/works/doi:10.1016/j.compbiomed.2024.109132` | OK | MOT-HW-002: Crell MR, Müller-Putz GR. Comput Biol Med 2024;182:109132; PMID 39332118 |
| 15 | `https://api.crossref.org/works/10.1038/nn827` | OK | MOT-IB-001: Haggard P, Clark S, Kalogeras J. Nat Neurosci 2002;5(4):382-385 |
| 16 | `https://api.openalex.org/works/doi:10.1093/brain/106.3.623` | OK | MOT-LIBET-001: Libet B, Gleason CA, Wright EW, Pearl DK. Brain 1983;106(3):623-642; PMID 6640273 |
| 17 | `https://api.crossref.org/works/10.1016/s0926-6410(00)00022-7` | OK | MOT-ME-004: Jäncke L, Loose R, Lutz K, Specht K, Shah NJ. Cogn Brain Res 2000;10(1-2):51-66 |
| 18 | `https://api.openalex.org/works/doi:10.1371/journal.pone.0182578` | OK | MOT-ME-005/MOT-MI-003: Ofner P, Schwarz A, Pereira J, Müller-Putz GR. PLoS ONE 2017;12(8):e0182578; PMID 28797109 |
| 19 | `https://api.crossref.org/works/10.1016/S0304-3940(97)00889-6` | 429 (target) | MOT-MI-001 |
| 20 | `https://api.openalex.org/works/doi:10.1016/S0304-3940(97)00889-6` | OK | MOT-MI-001: Pfurtscheller G, Neuper C. Neurosci Lett 1997;239(2-3):65-68; PMID 9469657 |
| 21 | `https://api.openalex.org/works/doi:10.1016/j.neuroimage.2005.12.003` | OK | MOT-MI-002: Pfurtscheller G, Brunner C, Schlögl A, Lopes da Silva FH. NeuroImage 2006;31(1):153-159; PMID 16443377 |
| 22 | `https://api.crossref.org/works/10.1109/tnsre.2012.2189584` | OK | MOT-MI-007: Faller J, Vidaurre C, Solis-Escalante T, Neuper C, Scherer R. IEEE TNSRE 2012;20(3):313-319 |
| 23 | `https://api.openalex.org/works/doi:10.1371/journal.pone.0162657` | OK | MOT-MI-008: Zhou B, Wu X, Lv Z, Zhang L, Guo X. PLoS ONE 2016;11(9):e0162657; PMID 27631789 |
| 24 | `https://api.crossref.org/works/10.1109/TBME.2004.827072` | OK | MOT-MI-010: Schalk G, McFarland DJ, Hinterberger T, Birbaumer N, Wolpaw JR. IEEE TBME 2004;51(6):1034-1043 |
| 25 | `https://api.openalex.org/works/doi:10.1093/gigascience/giaa098` | OK | MOT-MI-011: Jeong JH et al. GigaScience 2020;9(10); PMID 33034634 |
| 26 | `https://api.crossref.org/works/10.1037/0735-7044.107.6.899` | OK | MOT-MIRR-001: Gabrieli JDE, Corkin S, Mickel SF, Growdon JH. Behav Neurosci 1993;107(6):899-910 |
| 27 | `https://api.openalex.org/works/doi:10.1007/bf00412364` | OK | MOT-MRCP-001: Kornhuber HH, Deecke L. Pflügers Arch 1965;284(1):1-17; PMID 14341490 |
| 28 | `https://api.crossref.org/works/10.3390/brainsci9060127` | OK | MOT-MRCP-002/-003: Jochumsen M et al. (9 authors). Self-Paced Online vs. Cue-Based Offline BCIs for Inducing Neural Plasticity. Brain Sci 2019;9(6):127 |
| 29 | `https://api.openalex.org/works/doi:10.1073/pnas.95.3.861` | OK | MOT-MSL-001: Karni A, Meyer G, Rey-Hipolito C, Jezzard P, Adams MM, Turner R, Ungerleider LG. PNAS 1998;95(3):861-868; PMID 9448252 |
| 30 | `https://api.crossref.org/works/10.3389/fneur.2019.01227` | OK | MOT-MVF-001: Chang CS et al. Front Neurol 2019;10:1227 |
| 31 | `https://api.openalex.org/works/doi:10.1016/j.neuroimage.2014.11.026` | OK | MOT-PASS-001: Bourguignon M et al. NeuroImage 106:382-390; OpenAlex year 2014 (online); PMID 25463469 |
| 32 | `https://api.crossref.org/works/10.1016/j.neuroimage.2014.11.026` | 429 proxy rejected | MOT-PASS-001 (year check) |
| 33 | `https://api.openalex.org/works/doi:10.1016/j.neulet.2014.06.017` | OK | MOT-PERT-001: Varghese JP et al. Neurosci Lett 2014;578:33-38; PMID 24970752 |
| 34 | `https://api.openalex.org/works/doi:10.1037/0096-1523.14.3.331` | OK | MOT-RT-001: Gratton G et al. JEP:HPP 1988;14(3):331-344 |
| 35 | `https://api.openalex.org/works/doi:10.1016/0010-0285(87)90002-8` | OK | MOT-SRT-001: Nissen MJ, Bullemer P. Cogn Psychol 1987;19(1):1-32 |
| 36 | `https://api.crossref.org/works/10.1093/brain/awh246` | OK | STM-CCEP-001: Matsumoto R et al. Brain 2004;127(10):2316-2330 |
| 37 | `https://api.openalex.org/works/doi:10.1117/1.NPh.6.2.025013` | OK | STM-PBM-001: Wang X, Dmochowski JP, Zeng L, Kallioniemi E, Husain M, Gonzalez-Lima F, Liu H. Neurophotonics 2019;6(2):025013; PMID 31259198 |
| 38 | `https://api.crossref.org/works/10.1117/1.NPh.6.2.025013` | OK | STM-PBM-001 confirmed article-number 025013, issue 02, 2019 |
| 39 | `https://api.openalex.org/works/doi:10.1016/j.brs.2017.11.016` | OK | STM-PHTMS-001: Zrenner C, Desideri D, Belardinelli P, Ziemann U. Brain Stimul 11(2):374-389; online 2017-11-24, print 2018; PMID 29191438 |
| 40 | `https://api.crossref.org/works/10.3389/fnhum.2018.00202` | 429 proxy rejected | STM-TAVNS-001 |
| 41 | `https://api.openalex.org/works/doi:10.3389/fnhum.2018.00202` | OK | STM-TAVNS-001: Ventura-Bort C et al. Front Hum Neurosci 2018;12:202; PMID 29977196 |
| 42 | `https://api.openalex.org/works/doi:10.1111/j.1469-7793.2000.t01-1-00633.x` | OK | STM-TDCS-001: Nitsche MA, Paulus W. J Physiol 2000;527(3):633-639; PMID 10990547 |
| 43 | `https://api.openalex.org/works/doi:10.1097/00004424-199806000-00004` | OK | STM-TMSFMRI-001: Bohning DE et al. (9 authors). Invest Radiol 1998;33(6):336-340; PMID 9647445 |
| 44 | `https://api.openalex.org/works/doi:10.1038/nn.3620` | OK | STM-TUS-001: Legon W et al. Nat Neurosci 2014;17(2):322-329; PMID 24413698 |
| 45 | `https://api.openalex.org/works/doi:10.1111/j.1460-9568.2007.05587.x` | OK | STM-VIB-001: Naito E et al. Eur J Neurosci 2007;25(11):3476-3487; PMID 17553017 |
| 46 | `https://pubmed.ncbi.nlm.nih.gov/16959998/` | BLOCKED (reCAPTCHA page) | IMG-CMD-001; PubMed article pages not usable this session, switched to OpenAlex pmid: lookups |
| 47 | `https://api.openalex.org/works/pmid:16959998` | OK | IMG-CMD-001: Owen AM, Coleman MR, Boly M, Davis MH, Laureys S, Pickard JD. Detecting Awareness in the Vegetative State. Science 2006;313(5792):1402; doi 10.1126/science.1130197 |
| 48 | `https://api.openalex.org/works/pmid:22078855` | OK | IMG-CMD-002: Cruse D, Chennu S, Chatelle C, Bekinschtein TA, Fernández-Espejo D, Pickard JD, Laureys S, Owen AM. Lancet 2011;378(9809):2088-2094; doi 10.1016/s0140-6736(11)61224-5 |
| 49 | `https://api.openalex.org/works/pmid:27244745` | OK | IMG-SAO-002: Yao L, Sheng X, Zhang D, Jiang N, Farina D, Zhu X. IEEE TNSRE 25(1):81-90; OpenAlex year 2016 (early access); doi 10.1109/tnsre.2016.2572226 |
| 50 | `https://api.crossref.org/works/10.1109/tnsre.2016.2572226` | 429 proxy rejected | IMG-SAO-002 (year check) |
| 51 | `https://api.openalex.org/works/pmid:17229403` | OK | MOT-ATT-001: Müller-Putz GR, Zimmermann D, Graimann B, Nestinger K, Korisek G, Pfurtscheller G. Brain Res 1137(1):84-91; OpenAlex year 2006 (online); doi 10.1016/j.brainres.2006.12.052 |
| 52 | `https://api.openalex.org/works/pmid:23185489` | OK | MOT-ATT-002: Cruse D, Chennu S, Fernández-Espejo D, Payne WL, Young GB, Owen AM. PLoS ONE 2012;7(11):e49933; doi 10.1371/journal.pone.0049933 |
| 53 | `https://api.openalex.org/works/pmid:28220753` | OK | MOT-CURSOR-003: Pandarinath C et al. (9 authors). eLife 2017;6:e18554; doi 10.7554/elife.18554 |
| 54 | `https://api.openalex.org/works/pmid:8788955` | OK | MOT-FORCE-001: Conway BA, Halliday DM, Farmer SF, Shahani U, Maas P, Weir AI, Rosenberg JR. J Physiol 1995;489(3):917-924; doi 10.1113/jphysiol.1995.sp021104 |
| 55 | `https://api.openalex.org/works/pmid:21763434` | OK | MOT-GRASP-001: Pistohl T, Schulze-Bonhage A, Aertsen A, Mehring C, Ball T. NeuroImage 59(1):248-260; OpenAlex year 2011 (online); doi 10.1016/j.neuroimage.2011.06.084 |
| 56 | `https://api.openalex.org/works/pmid:25273279` | OK | MOT-GRASP-002: Bleichner MG, Freudenburg ZV, Jansma JM, Aarnoutse EJ, Vansteensel MJ, Ramsey NF. Brain Struct Funct 221(1):203-216; OpenAlex year 2014 (online); doi 10.1007/s00429-014-0902-x |
| 57 | `https://api.openalex.org/works/pmid:11781201` | OK | MOT-ME-001: Szurhaj W, Labyt E, Bourriez JL, Cassim F, Defebvre L, Hauser JJ, Guieu JD, Derambure P. 2001; Spec Issue:59-66; journal name and DOI absent from OpenAlex record |
| 58 | `https://api.openalex.org/works/pmid:22255564` | OK | MOT-ME-002: Onaran I, Ince NF, Cetin AE. Conf Proc IEEE EMBS 2011;2011:5424-5427; doi 10.1109/iembs.2011.6091341 |
| 59 | `https://api.openalex.org/works/pmid:19028138` | OK | MOT-MI-004: Pfurtscheller G, Solis-Escalante T. Clin Neurophysiol 120(1):24-29; OpenAlex year 2008 (online); doi 10.1016/j.clinph.2008.09.027 |
| 60 | `https://api.openalex.org/works/pmid:7666169` | OK | MOT-OBS-001: Fadiga L, Fogassi L, Pavesi G, Rizzolatti G. J Neurophysiol 1995;73(6):2608-2611; doi 10.1152/jn.1995.73.6.2608 |
| 61 | `https://api.openalex.org/works/pmid:10400972` | OK | MOT-PURS-001: Petit L, Haxby JV. J Neurophysiol 1999;82(1):463-471; doi 10.1152/jn.1999.82.1.463 |
| 62 | `https://api.openalex.org/works/pmid:7143039` | OK | MOT-REACH-001: Georgopoulos AP, Kalaska JF, Caminiti R, Massey JT. J Neurosci 1982;2(11):1527-1537; doi 10.1523/jneurosci.02-11-01527.1982 |
| 63 | `https://api.openalex.org/works/pmid:19965033` | OK | MOT-TRACK-001: Bradberry TJ, Gentili RJ, Contreras-Vidal JL. Conf Proc IEEE EMBS 2009:5010-5013; doi 10.1109/iembs.2009.5334606 |
| 64 | `https://api.openalex.org/works/pmid:33018632` | OK | MOT-TRACK-002: Martínez-Cagigal V, Kobler RJ, Mondini V, Hornero R, Müller-Putz GR. EMBC 2020:2981-2985; doi 10.1109/embc44109.2020.9175723 |
| 65 | `https://api.openalex.org/works/pmid:11160520` | OK | STM-GVS-001: Bense S, Stephan T, Yousry TA, Brandt T, Dieterich M. J Neurophysiol 2001;85(2):886-899; doi 10.1152/jn.2001.85.2.886 |
| 66 | `https://api.crossref.org/works?query.bibliographic=Zatorre%20Halpern%201996%20Hearing%20in%20the%20mind%27s%20ear%20PET%20investigation%20of%20musical%20imagery%20and%20perception&rows=3&select=...` | 403 proxy (URL too long) | IMG-AUD-001 |
| 67 | `https://api.crossref.org/works?query.bibliographic=Zatorre+Halpern+1996+Hearing+in+the+mind%27s+ear&rows=3&select=...` | 429 proxy rejected | IMG-AUD-001 |
| 68 | `https://api.openalex.org/works?search=Hearing+in+the+mind%27s+ear+musical+imagery+PET+Zatorre&per-page=3&select=...` | 429 (target) | IMG-AUD-001; OpenAlex list/search endpoint returned 429 on every attempt this session (6 attempts, rows 68, 70, 72, 74, 79, 82) |
| 69 | `https://api.crossref.org/works?query.bibliographic=Zatorre+Halpern+Hearing+in+the+mind%27s+ear+1996&rows=2` | OK | IMG-AUD-001: top hit 10.1162/jocn.1996.8.1.29 Zatorre RJ, Halpern AR, Perry DW, Meyer E, Evans AC. J Cogn Neurosci 1996;8(1):29-46 (match) |
| 70 | `https://api.openalex.org/works?filter=title.search:hearing%20in%20the%20mind%27s%20ear,publication_year:1996&select=...` | 429 (target) | IMG-AUD-001 |
| 71 | `https://api.crossref.org/works?query.bibliographic=Halpern+Zatorre+When+that+tune+runs+through+your+head+1999&rows=2` | 429 proxy rejected | IMG-AUD-002 |
| 72 | `https://api.openalex.org/works?search=When%20that%20tune%20runs%20through%20your%20head%20PET%20auditory%20imagery&per-page=2` | 429 (target) | IMG-AUD-002 |
| 73 | `https://api.crossref.org/works?query.bibliographic=Halpern+Zatorre+tune+runs+through+your+head+auditory+imagery+1999&rows=2` | OK | IMG-AUD-002: top hit 10.1093/cercor/9.7.697, Cereb Cortex 1999;9(7):697-704 (match; Crossref record lists only Halpern AR as author) |
| 74 | `https://api.openalex.org/works?search=hearing%20in%20the%20mind%27s%20ear%20musical%20imagery&per-page=2` | 429 (target) | (retry of search endpoint with a shorter query) |
| 75 | `https://api.crossref.org/works?query.bibliographic=Monti+Willful+modulation+of+brain+activity+in+disorders+of+consciousness+2010&rows=2` | OK | IMG-CMD-003: top hit is the NEJM correspondence 10.1056/nejmc1003229 (362(20):1936-1938), not the article; second hit Faculty Opinions -> no direct match |
| 76 | `https://api.openalex.org/works/doi:10.1056/NEJMoa0905370` | OK | IMG-CMD-003: Monti MM, Vanhaudenhuyse A, Coleman MR, Boly M, Pickard JD, Tshibanda L, Owen AM, Laureys S. NEJM 2010;362(7):579-589; PMID 20130250 (candidate DOI verified against record) |
| 77 | `https://api.crossref.org/works?query.bibliographic=Keirn+Aunon+A+new+mode+of+communication+between+man+and+his+surroundings+1990&rows=2` | 429 proxy rejected | IMG-MA-001 |
| 78 | `https://api.openalex.org/works?filter=title.search:new%20mode%20of%20communication%20between%20man%20and%20his%20surroundings&per-page=2` | 429 (target) | IMG-MA-001 |
| 79 | `https://api.crossref.org/works?query.bibliographic=Keirn+Aunon+new+mode+of+communication+man+surroundings+1990&rows=2` | 429 proxy rejected | IMG-MA-001 |
| 80 | `https://api.openalex.org/works/doi:10.1109/10.64464` | OK | IMG-MA-001 memory lead: Keirn ZA, Aunon JI. A new mode of communication between man and his surroundings. IEEE TBME 1990;37(12):1209-1214; PMID 2149711 -- title differs from the YAML citation "A new mode of EEG based communication" (R0842, Monash URL) |
| 81 | `https://api.openalex.org/works/doi:10.1016/j.neuroimage.2004.09.035` | OK | IMG-OLF-001: Djordjevic J, Zatorre RJ, Petrides M, Boyle JA, Jones-Gotman M. NeuroImage 24(3):791-801; OpenAlex year 2004 (online), print 2005; PMID 15652314 |
| 82 | `https://api.openalex.org/works/doi:10.1016/j.neunet.2009.05.008` | OK | IMG-SPI-001: DaSalla CS, Kambara H, Sato M, Koike Y. Neural Netw 2009;22(9):1334-1339; PMID 19497710 |
| 83 | `https://api.openalex.org/works/doi:10.1038/s41597-022-01147-2` | OK | IMG-SPI-002: Nieto N, Peterson V, Rufiner HL, Kamienkowski JE, Spies RD. Sci Data 2022;9(1):52; PMID 35165308 (author spelling Kamienkowski, not Kamienkoski) |
| 84 | `https://api.openalex.org/works/doi:10.1109/ICASSP.2015.7178118` | OK | IMG-SPI-003: Zhao S, Rudzicz F. Classifying phonological categories in imagined and articulated speech. ICASSP 2015:992-996 |
| 85 | `https://api.openalex.org/works/doi:10.1162/08989290051137549` | OK | IMG-VIS-002: O'Craven KM, Kanwisher N. Mental imagery of faces and places activates corresponding stimulus-specific brain regions. J Cogn Neurosci 2000;12(6):1013-1023; PMID 11177421 |
| 86 | `https://api.openalex.org/works/doi:10.1038/sdata.2014.47` | OK | MOT-GRASP-004: Luciw MD, Jarocka E, Edin BB. Sci Data 2014;1:140047; PMID 25977798 |
| 87 | `https://api.openalex.org/works/doi:10.1523/JNEUROSCI.5330-05.2006` | OK | MOT-SACC-002: Schluppeck D, Curtis CE, Glimcher PW, Heeger DJ. J Neurosci 2006;26(19):5098-5108; PMID 16687501 |
| 88 | `https://api.openalex.org/works/doi:10.3791/51403` | OK | STM-ADBS-001: Little S, Pogosyan A, Neal S, Zrinzo L, Hariz M, Foltynie T, Limousin P, Brown P. Controlling Parkinson's disease with adaptive deep brain stimulation. J Vis Exp 2014;(89):51403; PMID 25077449; PMCID 4217393 (= lead N10) |
| 89 | `https://api.openalex.org/works/doi:10.1002/ana.25234` | OK | STM-DBSEP-001: Sinclair NC et al. Ann Neurol 2018;83(5):1027-1031; PMID 29727475 |
| 90 | `https://api.openalex.org/works/doi:10.1093/brain/123.3.572` | OK | STM-PAS-001: Stefan K (record lists first author only). Brain 2000;123(3):572-584; PMID 10686179 |
| 91 | `https://api.openalex.org/works/doi:10.1136/jnnp.10.3.134` | OK | STM-SEP-001: Dawson GD. JNNP 1947;10(3):134-140; PMID 21610884 |
| 92 | `https://api.openalex.org/works/doi:10.1371/journal.pone.0013766` | OK | STM-TACS-001: Zaehle T, Rach S, Herrmann CS. PLoS ONE 2010;5(11):e13766; PMID 21072168 |
| 93 | `https://api.openalex.org/works/doi:10.1097/00001756-199711100-00024` | OK | STM-TEP-001: Ilmoniemi RJ, Virtanen J, Ruohonen J, Karhu J, Aronen HJ, Näätänen R, Katila T. Neuroreport 1997;8(16):3537-3540; PMID 9427322 |
| 94 | `https://api.openalex.org/works/doi:10.1038/s41593-023-01456-8` | OK | STM-TI-001: Violante IR et al. (14 authors). Nat Neurosci 2023;26(11):1994-2004; PMID 37857775 |
| 95 | `https://api.crossref.org/works?query.bibliographic=Javal+Essai+sur+la+physiologie+de+la+lecture+Annales+d%27oculistique+1878&rows=3` | OK | MOT-SACC-001: no matching record (hits: 2010 CUP reprint of Javal's book; unrelated 1878/1906 items) -> not_found |
| 96 | `https://api.crossref.org/works?query.bibliographic=Mayville+Neural+correlates+of+human+sensorimotor+coordination+EEG+MEG+functional+MRI+2000&rows=3` | OK | MOT-SMS-001: no matching record (dissertation not indexed) -> not_found |
| 97 | `https://api.openalex.org/works/doi:10.1097/00004691-199907000-00010` | OK | MOT-MI-005 TBD candidate: Neuper C, Schlögl A, Pfurtscheller G. Enhancement of left-right sensorimotor EEG differences during feedback-regulated motor imagery. J Clin Neurophysiol 1999;16(4):373-382; PMID 10478710 |
| 98 | `https://api.openalex.org/works/doi:10.1016/S0745-7138(05)80015-X` | 404 | MOT-MI-005 TBD second query (Pfurtscheller, Flotzinger, Kalcher 1993 J Microcomput Appl) -- DOI not resolvable, not retried |
| 99 | `https://api.openalex.org/works/doi:10.1109/TBME.2004.827088` | OK | MOT-MI-006 TBD candidate: Dornhege G, Blankertz B, Curio G, Müller KR. Boosting bit rates in noninvasive EEG single-trial classifications by feature combination and multiclass paradigms. IEEE TBME 2004;51(6):993-1002; PMID 15188870 |
| 100 | `https://api.openalex.org/works/doi:10.1016/j.neuroimage.2007.01.051` | OK | MOT-MI-009 TBD candidate: Blankertz B, Dornhege G, Krauledat M, Müller KR, Curio G. The non-invasive Berlin Brain-Computer Interface: fast acquisition of effective performance in untrained subjects. NeuroImage 2007;37(2):539-550; PMID 17475513 |
| 101 | `https://api.openalex.org/works/doi:10.1152/jn.00105.2010` | OK | MOT-ME-003 TBD candidate: Gwin JT, Gramann K, Makeig S, Ferris DP. Removal of movement artifact from high-density EEG recorded during walking and running. J Neurophysiol 2010;103(6):3526-3534; PMID 20410364 |
| 102 | `https://api.openalex.org/works/doi:10.1523/JNEUROSCI.5171-07.2008` | 429 proxy rejected | MOT-REACH-002 TBD candidate |
| 103 | `https://api.crossref.org/works/10.1523/jneurosci.5171-07.2008` | OK | MOT-REACH-002 TBD candidate: Waldert S, Preissl H, Demandt E, Braun C, Birbaumer N, Aertsen A, Mehring C. Hand movement direction decoded from MEG and EEG. J Neurosci 2008;28(4):1000-1008 |
