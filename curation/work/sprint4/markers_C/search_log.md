# Sprint 4 markers_C search log (curator_c)

Record retrieval via WebFetch only (curl to api.crossref.org / api.openalex.org / ebi.ac.uk is refused by the egress proxy with 403). The shared WebFetch proxy returns frequent HTTP 429; requests were paced with 40-60 s pauses.

## WebFetch
- crossref 10.1126/science.1100301 -> OK Ridderinkhof, Ullsperger, Crone, Nieuwenhuis 2004 Science 306(5695):443-447
- crossref 10.1523/JNEUROSCI.2924-05.2005 -> 429
- crossref 10.1016/j.neuron.2018.11.016 -> CLIENT_ERROR
- crossref 10.1126/science.1247200 -> 429
- crossref 10.1111/j.1467-9280.1994.tb00630.x -> OK Dehaene, Posner, Tucker 1994 Psychol Sci 5(5):303-305
- crossref 10.1111/j.1467-9280.1993.tb00586.x -> OK Gehring, Goss, Coles, Meyer, Donchin 1993 Psychol Sci 4(6):385-390
- openalex doi:10.1523/JNEUROSCI.2924-05.2005 -> CLIENT_ERROR
- openalex doi:10.1016/j.neuron.2018.11.016 -> 429
- openalex doi:10.1126/science.1247200 -> CLIENT_ERROR
- crossref 10.1523/jneurosci.2924-05.2005 (lowercase) -> CLIENT_ERROR
- crossref works?filter=doi:10.1523/JNEUROSCI.2924-05.2005&select=... -> 429
- crossref 10.1016/0013-4694(91)90062-9 -> OK Falkenstein, Hohnsbein, Hoormann, Blanke 1991 EEG Clin Neurophysiol 78(6):447-455
- crossref 10.1037/0033-295X.111.4.931 -> OK Yeung, Botvinick, Cohen 2004 Psychol Rev 111(4):931-959
- crossref 10.1037/0033-295X.109.4.679 -> OK Holroyd & Coles 2002 Psychol Rev 109(4):679-709
- crossref 10.1126/science.1247200 (retry) -> 429
- crossref 10.1126/science.1066893 -> OK Gehring & Willoughby 2002 Science 295(5563):2279-2282
- crossref 10.1002/hbm.21182 -> OK Foti, Weinberg, Dien, Hajcak 2011 Hum Brain Mapp 32(12):2207-2216
- crossref 10.1016/j.neuroimage.2011.05.037 -> 429
- crossref 10.1037/bul0000006 -> OK Sambrook & Goslin 2015 Psychol Bull 141(1):213-235
- crossref 10.1016/j.neubiorev.2012.05.008 -> OK Walsh & Anderson 2012 Neurosci Biobehav Rev 36(8):1870-1884
- crossref 10.1162/jocn.1997.9.6.788 -> OK Miltner, Braun, Coles 1997 J Cogn Neurosci 9(6):788-798
- crossref 10.1111/psyp.12370 -> CLIENT_ERROR (Proudfit 2015 dropped)
- crossref filter doi:10.1523/JNEUROSCI.3474-13.2014 (my remembered DOI for Becker 2014) -> 429
- pubmed ?term=<doi> -> reCAPTCHA, no content
- jneurosci.org/content/34/8/3005 (publisher page, used only to find the DOI) -> Becker et al. 2014 J Neurosci 34(8):3005-3012, DOI is 10.1523/JNEUROSCI.3684-13.2014 (remembered DOI 3474 was wrong)
- crossref filter doi:10.1523/jneurosci.3684-13.2014 -> CLIENT_ERROR
- openalex works/https://doi.org/10.1523/jneurosci.3684-13.2014 -> CLIENT_ERROR
- openalex doi:10.1037/bul0000006 -> OK (test that OpenAlex works; Sambrook 2015, OpenAlex year 2014 = online date)
- openalex filter doi:10.1523/jneurosci.3684-13.2014 -> CLIENT_ERROR
- europepmc search DOI:10.1523/JNEUROSCI.3684-13.2014 -> 429
- openalex doi:10.1126/science.1247200 (Bonini 2014, remembered DOI) -> CLIENT_ERROR; never retrieved, not cited
- crossref 10.1038/nn1239 -> OK van Schie, Mars, Coles, Bekkering 2004 Nat Neurosci 7(5):549-554
- crossref 10.1027/0269-8803.19.4.281 -> OK Bates, Patel, Liddle 2005 J Psychophysiol 19(4):281-288
- crossref 10.3389/fnins.2014.00208 -> OK Chavarriaga, Sobolewski, Millan 2014 Front Neurosci 8:208
- crossref 10.1109/TBME.2007.908083 -> 429
- openalex doi:10.1109/TBME.2007.908083 -> OK Ferrez & Millan 2008 IEEE TBME 55(3):923-929
- crossref 10.1109/TNSRE.2010.2053387 -> OK Chavarriaga & Millan 2010 IEEE TNSRE 18(4):381-388
- crossref 10.3389/fnhum.2015.00155 -> OK Spuler & Niethammer 2015 Front Hum Neurosci 9:155
- crossref 10.1016/j.cogbrainres.2004.02.010 (remembered DOI for Herrmann 2004) -> WRONG paper (Grabner et al. 2004); rejected, Herrmann 2004 not cited
- crossref works?query.bibliographic=Herrmann ... LORETA -> irrelevant results
- crossref 10.1162/08989290260045837 -> ROBOTS_DISALLOWED
- openalex doi:10.1162/08989290260045837 -> 429, then retry OK van Veen & Carter 2002 J Cogn Neurosci 14(4):593-602
- crossref 10.1007/s00429-010-0261-1 -> OK Ullsperger, Harsay, Wessel, Ridderinkhof 2010 Brain Struct Funct 214(5-6):629-643
- crossref 10.3389/fnhum.2012.00088 -> OK Wessel 2012 Front Hum Neurosci 6:88
- crossref 10.1111/1469-8986.3850752 -> CLIENT_ERROR
- openalex doi:10.1111/1469-8986.3850752 -> OK Nieuwenhuis, Ridderinkhof, Blom, Band, Kok 2001 Psychophysiology 38(5):752-760
- openalex doi:10.1523/JNEUROSCI.4015-10.2010 (Steinhauser & Yeung 2010) -> CLIENT_ERROR; all J Neurosci DOIs fail in both APIs, not cited
- openalex works?search=... -> CLIENT_ERROR (search/filter endpoints fail through WebFetch)
- crossref 10.3389/fnhum.2012.00065 -> 429
- openalex doi:10.3389/fnhum.2012.00065 -> OK Murphy, Robertson, Allen, Hester, O'Connell 2012 Front Hum Neurosci 6:65
- crossref 10.7554/eLife.67556 (Desender 2021) -> 429; dropped
- crossref 10.1007/s11065-021-09513-4 -> OK Soskic, Jovanovic, Styles, Kappenman, Kovic 2022 Neuropsychol Rev 32(3):577-600
- openalex doi:10.1111/psyp.13570 -> OK Hajcak & Foti 2020 Psychophysiology 57(7):e13570
- openalex doi:10.1111/j.1469-8986.2007.00602.x -> OK Folstein & Van Petten, Psychophysiology 45(1):152-170 (OpenAlex year 2007 = online; volume year 2008)
- crossref 10.3758/CABN.3.1.17 -> 429
- openalex doi:10.3758/CABN.3.1.17 -> OK Nieuwenhuis, Yeung, van den Wildenberg, Ridderinkhof 2003 CABN 3(1):17-26
- crossref 10.1016/S1388-2457(01)00691-5 -> 429
- openalex doi:10.1016/S1388-2457(01)00691-5 -> OK Bokura, Yamaguchi, Kobayashi 2001 Clin Neurophysiol 112(12):2224-2232
- openalex doi:10.1016/S0001-6918(99)00008-6 -> OK Falkenstein, Hoormann, Hohnsbein 1999 Acta Psychol 101(2-3):267-291
- openalex doi:10.1097/00001756-199903170-00003 -> OK Ishii et al. 1999 NeuroReport 10(4):675-679 (11 authors incl. Asada)
- openalex doi:10.1016/S0304-3940(99)00679-5 -> OK Asada, Fukuda, Tsunoda, Yamaguchi, Tonoike 1999 Neurosci Lett 274(1):29-32
- openalex doi:10.1016/j.neuroimage.2005.04.014 -> OK Onton, Delorme, Makeig 2005 NeuroImage 27(2):341-356
- openalex doi:10.1016/j.tics.2014.04.012 -> OK Cavanagh & Frank 2014 Trends Cogn Sci 18(8):414-421
- openalex doi:10.1111/j.1469-8986.2011.01293.x -> OK Cavanagh, Zambrano-Vazquez, Allen, Psychophysiology 49(2):220-238 (online 2011, issue 2012)
- openalex doi:10.1093/cercor/7.4.374 -> OK Gevins 1997 Cereb Cortex 7(4):374-385 (OpenAlex record lists only the first author; co-authors Smith ME, McEvoy L, Yu D added from the article byline -- flag for full-text check)
- openalex doi:10.1046/j.1460-9568.2002.01975.x -> OK Jensen & Tesche 2002 Eur J Neurosci 15(8):1395-1399
- openalex doi:10.1038/nrn2532 -> OK Lau, Phillips, Poeppel 2008 Nat Rev Neurosci 9(12):920-933
- openalex doi:10.1146/annurev.psych.093008.131123 -> OK Kutas & Federmeier, Annu Rev Psychol 62(1):621-647 (OpenAlex year 2010 = online; volume year 2011)
- openalex doi:10.1006/nimg.2002.1268 -> 429
- openalex doi:10.1006/nimg.2002.1268 (retry) -> OK Halgren, Dhond, Christensen, Van Petten, Marinkovic, Lewine, Dale 2002 NeuroImage 17(3):1101-1116
- openalex doi:10.1038/372260a0 -> OK Nobre, Allison, McCarthy 1994 Nature 372(6503):260-263
- openalex doi:10.1126/science.7350657 -> OK Kutas & Hillyard 1980 Science 207(4427):203-205
- openalex doi:10.1038/nn1504 -> OK DeLong, Urbach, Kutas 2005 Nat Neurosci 8(8):1117-1121
- openalex doi:10.7554/eLife.33468 -> OK Nieuwland, Politzer-Ahles, Heyselaar, et al. (23 authors) 2018 eLife 7 (article e33468)
- openalex doi:10.1093/brain/122.6.1033 -> OK Friederici 1999 Brain 122(6):1033-1047 (record lists only first author; von Cramon DY, Kotz SA added from byline -- flag for full-text check)
- openalex doi:10.1016/0749-596X(92)90039-Z -> OK Osterhout & Holcomb 1992 J Mem Lang 31(6):785-806
- openalex doi:10.1080/01690969308407585 -> 429
- crossref 10.1080/01690969308407585 -> OK Hagoort, Brown, Groothusen 1993 Lang Cogn Process 8(4):439-483
- openalex doi:10.1016/j.brainres.2006.12.063 -> OK Kuperberg, Brain Res 1146:23-49 (OpenAlex year 2006 = online; volume year 2007)
- openalex doi:10.1016/j.brainres.2012.01.055 -> OK Brouwer, Fitz, Hoeks 2012 Brain Res 1446:127-143
- openalex doi:10.1016/j.jml.2004.10.002 -> OK Kim & Osterhout, J Mem Lang 52(2):205-225 (OpenAlex year 2004 = online; volume year 2005)
- openalex doi:10.1093/cercor/bhl017 -> 429; crossref same DOI -> 429; openalex works/https://doi.org/... -> CLIENT_ERROR
- openalex doi:10.1016/j.biopsycho.2012.04.005 -> OK Sabatinelli, Keil, Frank, Lang, Biol Psychol 92(3):513-519 (online 2012, volume year 2013)
- openalex doi:10.1080/87565640903526504 -> OK Hajcak, MacNamara, Olvet 2010 Dev Neuropsychol 35(2):129-155
- openalex doi:10.1016/S0301-0511(99)00044-7 -> OK Cuthbert, Schupp, Bradley, Birbaumer, Lang 2000 Biol Psychol 52(2):95-111
- openalex doi:10.1111/1469-8986.3720257 -> OK Schupp, Cuthbert, Bradley, Cacioppo, Ito, Lang 2000 Psychophysiology 37(2):257-261
- openalex doi:10.3758/CABN.6.4.291 -> OK Hajcak & Nieuwenhuis 2006 CABN 6(4):291-297
- openalex doi:10.1093/CERCOR/BHL017 -> OK Sabatinelli, Lang, Keil, Bradley, Cereb Cortex 17(5):1085-1091 (online 2006, volume year 2007); abstract: LPP correlates with BOLD in lateral occipital, inferotemporal and parietal visual cortex
- openalex doi:10.1016/J.BIOPSYCHO.2012.04.005 (abstract request) -> abstract null in record; amygdala claim not used
- pmc.ncbi.nlm.nih.gov/articles/PMC3447123 -> reCAPTCHA, no content
- openalex doi:10.1016/j.neuroimage.2011.05.037 -> OK Carlson, Foti, Mujica-Parodi, Harmon-Jones, Hajcak 2011 NeuroImage 57(4):1608-1616
- openalex doi:10.1016/S0301-0511(03)00107-8 -> OK Miltner, Lemke, Weiss, Holroyd, Scheffers, Coles 2003 Biol Psychol 64(1-2):157-166
- openalex doi:10.1016/S0028-3932(03)00165-5 (remembered DOI for Stemmer 2004 ACC-lesion ERN) -> CLIENT_ERROR; not cited
- openalex doi:10.1038/74999 (remembered DOI for Gehring & Knight 2000) -> WRONG paper (Honore 2000 Nat Med); rejected, not cited

## WebSearch (7 of 25 used)
1. "Herrmann Römmler Ehlis Heidrich Fallgatter 2004 Source localization (LORETA) of the error-related-negativity doi" -> no DOI found; Herrmann 2004 dropped
2. "Murphy Robertson Allen Hester O'Connell 2015 electrophysiological signal ... error awareness doi" -> identified as 2012, 10.3389/fnhum.2012.00065 (frontiersin link)
3. "meta-analysis late positive potential emotion regulation reappraisal doi" -> no usable meta-analysis identified; not pursued
4. "Šoškić How to do better N400 studies Neuropsychology Review doi" -> confirmed paper exists; DOI then checked in Crossref
5. "Hajcak Foti 2020 Significance?... Significance! ... doi" -> lab PDF links; DOI checked in OpenAlex
6. "Sabatinelli Keil Frank Lang 2013 ... amygdala LPP abstract" -> PMC3447123 (blocked by reCAPTCHA); amygdala generator not added

