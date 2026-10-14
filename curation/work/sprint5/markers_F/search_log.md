# Sprint 5 markers_F search log (curator F)

Date: 2026-10-14. Web search calls used: 3 of 25. Record look-ups via the Crossref API (https://api.crossref.org/works/<DOI>) and, when Crossref was rate limited or failed, the OpenAlex API (https://api.openalex.org/works/doi:<DOI>). Most candidate DOIs came from curation/literature.csv, the sprint 4 process files and the curator's reading list; each one was retrieved before citing.

## Record look-ups

- Crossref 10.1016/S1388-2457(99)00135-2 -> OK Slotnick et al. 1999 Clin Neurophysiol 110(10):1793-1800
- Crossref 10.1088/1741-2560/6/4/046002 -> OK but WRONG paper (Bin et al. 2009, SSVEP/CCA BCI, not c-VEP) -> rejected, not cited
- Crossref 10.1371/journal.pone.0133797 -> OK Thielen et al. 2015 PLoS One 10(7):e0133797
- Crossref 10.1088/1741-2552/ac38cf -> OK Martínez-Cagigal et al. 2021 J Neural Eng 18(6):061002
- Crossref 10.1523/JNEUROSCI.0875-06.2006 -> OK Thut et al. 2006 J Neurosci 26(37):9494-9502
- Crossref 10.1523/JNEUROSCI.20-06-j0002.2000 -> OK Worden et al. 2000 J Neurosci 20(6):RC63
- Crossref 10.1088/1741-2560/8/2/025015 -> 429 rate limited; OpenAlex -> OK Bin et al. 2011 J Neural Eng 8(2):025015
- Crossref 10.1016/j.neuron.2008.09.010 -> 429; OpenAlex -> OK Siegel et al. 2008 Neuron 60(4):709-719
- Crossref 10.3389/fnhum.2010.00186 -> OK Jensen & Mazaheri 2010 Front Hum Neurosci 4 (article 186 from DOI suffix)
- Crossref 10.1523/JNEUROSCI.1954-19.2019 -> fetch error; OpenAlex -> OK Wöstmann et al. 2019 J Neurosci 39(49):9797-9805
- Crossref 10.1016/j.cub.2009.08.062 -> OK Sauseng et al. 2009 Curr Biol 19(21):1846-1852
- Crossref 10.1186/1743-0003-8-24 -> 429; OpenAlex -> OK Treder et al. 2011 J Neuroeng Rehabil 8(1):24
- Crossref 10.1016/j.concog.2020.102917 -> OK Förster et al. 2020 Conscious Cogn 80:102917
- OpenAlex 10.1016/j.neubiorev.2009.12.002 -> OK Koivisto & Revonsuo, Neurosci Biobehav Rev 34(6):922-934 (OpenAlex year 2009 = online; volume 34 is the 2010 print year, cited as 2010)
- OpenAlex 10.1016/j.tics.2021.05.009 -> OK Dembski et al. 2021 Trends Cogn Sci 25(8):660-670
- Crossref 10.3389/fnhum.2012.00211 -> OK Liu et al. 2012 Front Hum Neurosci 6 (article 211 from DOI suffix)
- OpenAlex 10.1152/jn.1989.62.3.694 -> OK Allison et al. 1989 J Neurophysiol 62(3):694-710
- OpenAlex 10.1126/science.3975600 -> OK Wood et al. 1985 Science 227(4690):1051-1053
- Crossref 10.1016/j.clinph.2008.03.016 -> OK Cruccu et al. 2008 Clin Neurophysiol 119(8):1705-1719
- OpenAlex 10.1007/s00134-020-06198-w -> OK Sandroni et al. 2020 Intensive Care Med 46(10):1803-1851
- OpenAlex 10.1093/cercor/10.12.1233 -> OK Hopf et al. 2000 Cereb Cortex 10(12):1233-1241 (authorship field lists only first author; full list Hopf, Luck, Girelli, Hagner, Mangun, Scheich, Heinze from the record's repository citation)
- OpenAlex 10.1523/JNEUROSCI.3564-03.2004 -> OK Hopf et al. 2004 J Neurosci 24(8):1822-1832
- Crossref 10.1037/0096-1523.20.5.1000 -> OK Luck & Hillyard 1994 JEP:HPP 20(5):1000-1014
- OpenAlex 10.1016/0013-4694(96)95711-9 -> OK Eimer 1996 Electroencephalogr Clin Neurophysiol 99(3):225-234
- OpenAlex 10.1016/j.tics.2014.05.005 -> OK Eimer 2014 Trends Cogn Sci 18(10):526-535
- OpenAlex 10.1111/j.1469-8986.1994.tb02218.x -> OK Luck & Hillyard 1994 Psychophysiology 31(3):291-308
- OpenAlex 10.1162/089892901753294400 -> 429; Crossref -> 429; OpenAlex retry -> OK Carretié et al. 2001 J Cogn Neurosci 13(8):1109-1128
- Crossref 10.1016/j.biopsycho.2007.11.006 -> OK Olofsson et al. 2008 Biol Psychol 77(3):247-265
- OpenAlex 10.1037/0022-3514.85.4.616 -> 429; Crossref -> OK Ito & Urland 2003 J Pers Soc Psychol 85(4):616-626
- OpenAlex 10.1016/j.clinph.2003.11.021 -> OK Crowley & Colrain 2004 Clin Neurophysiol 115(4):732-744
- OpenAlex 10.1126/science.424760 -> OK Ritter et al. 1979 Science 203(4387):1358-1361
- OpenAlex 10.1111/j.1469-8986.2007.00602.x -> OK Folstein & Van Petten, Psychophysiology 45(1):152-170 (OpenAlex year 2007 = online; cited with 2008 print year of volume 45)
- Crossref 10.1016/j.cub.2015.12.049 -> OK Loughnane et al. 2016 Curr Biol 26(4):496-502
- OpenAlex 10.1038/ncomms11070 -> OK Coffey et al. 2016 Nat Commun 7(1):11070
- OpenAlex 10.1016/j.neuroimage.2018.03.060 -> OK Bidelman 2018 Neuroimage 175:56-69 (no abstract in record)
- OpenAlex 10.1038/s41467-019-13003-w -> OK Coffey et al. 2019 Nat Commun 10(1):5036
- Crossref 10.1097/AUD.0b013e3181cdb272 -> OK Skoe & Kraus 2010 Ear Hear 31(3):302-324
- OpenAlex 10.1162/jocn.2008.20131 -> OK Song et al. 2008 J Cogn Neurosci 20(10):1892-1902
- OpenAlex 10.1016/j.cogbrainres.2005.05.004 -> OK Krishnan et al. 2005 Cogn Brain Res 25(1):161-168
- Crossref 10.1073/pnas.0701498104 -> 429; OpenAlex -> OK Musacchia et al. 2007 PNAS 104(40):15894-15898
- OpenAlex 10.3109/14992020309101316 -> OK Picton et al. 2003 Int J Audiol 42(4):177-219
- OpenAlex 10.1152/jn.91346.2008 -> OK Brugge et al. 2009 J Neurophysiol 102(4):2358-2374
- OpenAlex 10.1121/1.429600 -> OK Ross et al. 2000 J Acoust Soc Am 108(2):679-691
- OpenAlex 10.1001/jamapsychiatry.2016.2619 -> OK but title without subtitle; Crossref -> OK Thuné et al. 2016 JAMA Psychiatry 73(11), title "... : A Meta-analysis", page field "1145" only (cited as given)
- OpenAlex 10.1213/00000539-199011000-00002 -> OK Plourde & Picton 1990 Anesth Analg 71(5):460-468
- OpenAlex 10.1016/j.neulet.2007.04.072 -> OK Skosnik et al. 2007 Neurosci Lett 420(3):223-228
- OpenAlex 10.1016/j.jneumeth.2011.02.007 -> OK Kim et al. 2011 J Neurosci Methods 197(1):180-185
- OpenAlex 10.1007/BF00228404 -> OK Probst et al. 1993 Exp Brain Res 93(2):345-351 (last page recorded as "51", read as 351)
- OpenAlex 10.1016/j.visres.2006.09.020 -> OK Kuba et al. Vision Res 47(2):189-202 (OpenAlex year 2006 = online; cited 2007)
- OpenAlex 10.1088/1741-2560/5/4/011 -> OK Guo et al. 2008 J Neural Eng 5(4):477-485
- OpenAlex 10.1016/j.clinph.2009.06.026 -> 429; Crossref -> OK Hong et al. 2009 Clin Neurophysiol 120(9):1658-1666

## Web searches and page reads

- web search "Coffey 2016 MEG frequency-following response sources cochlear nucleus inferior colliculus medial geniculate right auditory cortex" -> PMC4820836, RePEc record
- PMC4820836 -> redirect, then browser check page (no content)
- RePEc abstract page for 10.1038/ncomms11070 -> abstract confirms sources in cochlear nucleus, inferior colliculus, medial geniculate and right-asymmetric auditory cortex
- web search "visual awareness negativity source localization MEG lateral occipital ventral visual cortex study" -> Liu et al. 2012 Front Hum Neurosci (10.3389/fnhum.2012.00211)
- DOAJ record of Liu et al. 2012 -> abstract: MEG, sustained posterior seen-vs-unseen difference 190-350 ms, sources in bilateral LO complex and right posterior inferotemporal cortex
- web search "visual P2 component neural generators source localization anterior P2 ERP" -> no usable source-localization study for the visual anterior P2; generator left at scalp topography, grade C
