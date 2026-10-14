# Sprint 4 markers_D search log (curator_d)

web search calls used: 3 of 25. Candidate sources were mostly known landmark meta-analyses; every DOI was then fetched with HTTP request (Bash curl to these APIs is blocked by the proxy, as noted by curator_a). Abbreviations: CR = api.crossref.org/works/<DOI>, OA = api.openalex.org/works/doi:<DOI>.

## web search
- "meta-analysis fNIRS prefrontal working memory load n-back oxygenated hemoglobin doi" -> identified Herff et al. (fnhum.2013.00935); PMC8145788 page blocked by reCAPTCHA, not used
- "systematic review meta-analysis functional near-infrared spectroscopy working memory prefrontal activation load effect" -> no usable fNIRS WM meta-analysis; HbO -> working memory stays B
- "EEG emotion recognition meta-analysis systematic review band power frontal asymmetry gamma valence arousal" -> no meta-analysis; identified Zheng, Zhu & Lu "Identifying stable patterns over time" (SEED)

## HTTP request (record retrieval)
- CR 10.1016/j.neubiorev.2007.12.002 -> OK Sergerie 2008 NBR 32(4):811-830
- CR 10.1016/j.brainresrev.2007.10.012 -> OK Costafreda 2008 Brain Res Rev 58(1):57-70
- CR 10.1017/S0140525X11000446 -> OK Lindquist 2012 BBS 35(3):121-143
- CR 10.1038/mp.2015.88 -> OK Fullana (issued 2015, print 2016) Mol Psychiatry 21(4):500-508
- CR 10.1007/s00429-010-0255-z -> 429 rate limited; OA -> OK Kurth 2010 Brain Struct Funct 214(5-6):519-534
- CR 10.1038/nrn2555 -> OK Craig 2009 NRN 10(1):59-70
- CR 10.1016/j.neuroimage.2010.10.014 -> OK Lamm 2011 NeuroImage 54(3):2492-2502
- CR 10.1007/s00429-010-0262-0 -> OK Menon & Uddin 2010 Brain Struct Funct 214(5-6):655-667
- CR 10.1002/hbm.22649 -> OK Feng 2015 (issued 2014) HBM 36(2):591-602
- CR 10.1126/science.1082976 -> OK Sanfey 2003 Science 300(5626):1755-1758
- CR 10.1016/j.neuroimage.2013.02.063 -> OK Bartra 2013 NeuroImage 76:412-427
- CR 10.1016/j.neubiorev.2013.03.023 -> fetch error; OA -> OK Garrison 2013 NBR 37(7):1297-1310
- CR 10.1016/j.neubiorev.2010.12.012 -> OK Liu 2011 NBR 35(5):1219-1236
- CR 10.1126/science.1094285 -> OK O'Doherty 2004 Science 304(5669):452-454
- CR 10.1002/hbm.24184 -> OK Oldham 2018 HBM 39(8):3398-3418
- CR 10.1523/JNEUROSCI.21-16-j0002.2001 -> fetch error; OA -> OK Knutson 2001 J Neurosci 21(16):RC159
- CR 10.1093/scan/nst106 -> OK Clithero & Rangel (issued 2013, print 2014) SCAN 9(9):1289-1302
- CR 10.1523/JNEUROSCI.4089-09.2010 -> OK Hare 2010 J Neurosci 30(2):583-590
- CR 10.3758/CABN.7.1.1 -> OK Nee 2007 CABN 7(1):1-17
- CR 10.1016/j.tics.2004.10.003 -> fetch error; OA -> OK Botvinick 2004 TiCS 8(12):539-546
- CR 10.1126/science.1216930 -> OK Kolling 2012 Science 336(6077):95-98
- CR 10.1016/j.neuron.2013.07.007 -> OK Shenhav 2013 Neuron 79(2):217-240
- CR 10.1126/science.1089134 -> OK Eisenberger 2003 Science 302(5643):290-292
- CR 10.1093/scan/nsu110 -> fetch error; OA -> OK Rotgé (online 2014, print 2015) SCAN 10(1):19-27 (abstract checked: ventral and dorsal ACC; Cyberball mainly midcingulate)
- CR 10.1162/jocn_a_00233 -> OK Denny 2012 JOCN 24(8):1742-1752
- CR 10.1016/j.neuroimage.2005.12.002 -> OK Northoff 2006 NeuroImage 31(1):440-457
- CR 10.1016/j.neubiorev.2014.01.009 -> OK Schurz 2014 NBR 42:9-34
- CR 10.1002/hbm.20547 -> OK Van Overwalle (issued 2008, print 2009) HBM 30(3):829-858
- CR 10.1073/pnas.98.2.676 -> OK Raichle 2001 PNAS 98(2):676-682
- CR 10.1196/annals.1440.011 -> OK Buckner 2008 Ann NY Acad Sci 1124(1):1-38
- CR 10.1016/S1053-8119(03)00230-1 -> OK Saxe & Kanwisher 2003 NeuroImage 19(4):1835-1842
- CR 10.1177/1073858407304654 -> OK Decety & Lamm 2007 Neuroscientist 13(6):580-593
- CR 10.1007/s00429-014-0803-z -> OK Krall (issued 2014, print 2015) Brain Struct Funct 220(2):587-604
- CR 10.1006/nimg.2001.1009 -> OK Farrer & Frith 2002 NeuroImage 15(3):596-603
- CR 10.1006/nimg.2000.0612 -> OK Castelli 2000 NeuroImage 12(3):314-325
- CR 10.1016/j.neuroimage.2010.10.069 -> fetch error; OA -> OK Cui (OA year 2010, print 2011) NeuroImage 54(4):2808-2821
- CR 10.1016/j.neuroimage.2003.08.026 -> OK Okamoto 2004 NeuroImage 21(1):99-111
- CR 10.1088/1741-2560/8/6/066004 -> 429 rate limited; OA -> OK Power 2011 J Neural Eng 8(6):066004
- CR 10.3389/fnhum.2015.00003 -> OK Naseer & Hong 2015 (no article number in CR); OA -> article 3
- CR 10.3389/fnhum.2014.00076 -> OK Fishburn 2014 (no article number in CR); OA -> article 76
- OA 10.3389/fnhum.2013.00935 -> OK Herff 2014 Front Hum Neurosci 7:935
- CR 10.1016/S0361-9230(03)00066-2 -> OK Herrmann 2003 Brain Res Bull 61(1):51-56
- CR 10.1111/j.1467-9280.2005.01618.x -> OK Pizzagalli 2005 Psychol Sci 16(10):805-813
- CR 10.1016/j.biopsycho.2009.08.010 -> fetch error; OA -> OK Harmon-Jones (OA 2009, print 2010) Biol Psychol 84(3):451-462
- CR 10.1037/0021-843X.115.4.715 -> OK Thibodeau 2006 J Abnorm Psychol 115(4):715-729
- CR 10.1016/j.nicl.2017.07.006 -> OK van der Vinne 2017 NeuroImage Clin 16:79-87
- CR 10.1111/1469-8986.3840685 -> OK Allen 2001 Psychophysiology 38(4):685-693
- CR 10.1109/TAMD.2015.2431497 -> 429 rate limited; OA -> OK Zheng & Lu 2015 IEEE TAMD 7(3):162-175
- CR 10.1109/T-AFFC.2011.15 -> OK Koelstra 2012 IEEE TAC 3(1):18-31
- CR 10.1109/TAFFC.2017.2714671 -> fetch error; OA -> OK Alarcão & Fonseca (OA 2017, print 2019) IEEE TAC 10(3):374-393
- OA 10.1109/TAFFC.2017.2712143 -> OK Zheng, Zhu & Lu (OA 2017, print 2019) IEEE TAC 10(3):417-429
