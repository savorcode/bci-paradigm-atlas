# Sprint 5 markers_G search log (curator G)

Date: 2026-10-14. Web search calls used: 13 of 25. Record look-ups via the Crossref API (api.crossref.org/works/<DOI>), with the OpenAlex API (api.openalex.org/works/doi:<DOI> or /works/pmid:<PMID>) as fallback when Crossref returned an error or a 429 rate limit. PubMed and PMC pages returned a browser-check page and could not be read.

## Web searches

1. "NoGo P3 source localization midcingulate pre-SMA Huster review ..." -> Huster et al. 2013 DOI 10.1016/j.ijpsycho.2012.08.001; Hong et al. 2017 (Sci Rep) link
2. "Enriquez-Geppert Konrad Pantev Huster 2010 Conflict and inhibition ... NeuroImage doi" -> neurosynth PMID 20188191
3. "Wessel Aron 2015 onset of the frontocentral P3 ..." -> Univ. Iowa repository record, DOI 10.1111/psyp.12374
4. "Bridger ... The FN400 is functionally distinct from the N400 ..." -> links only; not pursued (enough FN400 sources)
5. "Karayanidis Jamadar 2010 Advance preparation in task-switching ..." -> DOI 10.3389/fpsyg.2010.00025
6. "Jamadar Hughes Fulham Michie Karayanidis 2010 spatial and temporal dynamics ..." -> neurosynth PMID 20123028
7. "Nicholson Karayanidis Poboka Heathcote Michie 2005 ..." -> UTAS eCite record, DOI 10.1111/j.1469-8986.2005.00350.x
8. "Lavric Mizon Monsell 2008 Neurophysiological signature ..." -> no DOI found; not cited
9. "Pisauro Fouragnan Retzler Philiastides 2017 ..." -> DOI 10.1038/ncomms15808 (from repository PDF name)
10. "Herding Ludwig von Lautz Spitzer Blankenburg 2019 ..." -> PMID 31302254
11. "presaccadic potential EEG MEG source localization frontal eye field ..." -> Hinkley 2010 (MEG high-gamma, different signal) and Sestieri 2008 (stimulus-locked MEG); neither cited
12. "Tran Craig 2020 influence of mental fatigue on brain activity ... results" -> Macquarie repository abstract (theta g about 1.0)
13. "Huster 2013 Electroencephalography of response inhibition tasks abstract P3 midcingulate ..." -> Hong et al. 2017, Sci Rep, article page


## Record look-ups and page reads

- Crossref 10.1111/psyp.13554 -> fetch error; OpenAlex -> OK Tran et al. 2020 Psychophysiology 57(5):e13554
- Crossref 10.1093/sleep/18.10.890 -> fetch error; OpenAlex -> OK Cajochen et al. 1995 Sleep 18(10):890-894
- Crossref 10.1016/S0304-3940(03)00033-8 -> OK Strijkstra et al. 2003 Neurosci Lett 340(1):17-20
- Crossref 10.1016/S0306-4522(00)00409-7 -> OK Finelli et al. 2000 Neuroscience 101(3):523-529
- Crossref 10.1016/S0301-0511(00)00085-5 -> OK Lal & Craig 2001 Biol Psychol 55(3):173-194
- Macquarie repository page (Tran 2020) -> abstract read: theta and alpha increase with fatigue
- Crossref 10.1016/j.tics.2007.04.004 -> OK Rugg & Curran 2007 TICS 11(6):251-257
- Crossref 10.1016/j.neuropsychologia.2008.01.004 -> OK Vilberg & Rugg 2008 Neuropsychologia 46(7):1787-1799
- Crossref 10.1093/brain/119.3.889 -> 429; OpenAlex -> OK Wilding & Rugg 1996 Brain 119(3):889-905
- Crossref 10.3758/BF03209340 -> 429; OpenAlex -> OK Curran 2000 Mem Cognit 28(6):923-938
- Crossref 10.1016/j.tics.2007.04.002 -> OK Paller, Voss, Boehm 2007 TICS 11(6):243-250
- OpenAlex 10.1126/science.285.5433.1582 -> OK Fernández et al. 1999 Science 285(5433):1582-1585
- OpenAlex 10.1016/j.neuroimage.2010.09.045 -> OK Kim, NeuroImage 54(3):2446-2461 (record year 2010 = online; issue 54(3) is 2011, cited as 2011)
- Crossref 10.1016/S1364-6613(00)01845-3 -> OK Paller & Wagner 2002 TICS 6(2):93-102
- OpenAlex 10.1016/0013-4694(87)90124-6 -> OK Paller, Kutas, Mayes 1987 EEG Clin Neurophysiol 67(4):360-371
- OpenAlex 10.1038/21645 -> 429; Crossref -> OK Kahana et al. 1999 Nature 399(6738):781-784
- OpenAlex 10.1002/hipo.20109 -> OK Ekstrom et al. 2005 Hippocampus 15(7):881-889
- Crossref 10.1523/JNEUROSCI.5001-07.2008 -> 429; OpenAlex -> OK Cornwell et al. 2008 J Neurosci 28(23):5983-5990
- Crossref 10.1016/j.tics.2019.12.006 -> OK Herweg, Solomon, Kahana 2020 TICS 24(3):208-227
- Crossref 10.1002/hipo.20937 -> OK Lega, Jacobs, Kahana 2012 Hippocampus 22(4):748-761
- Crossref 10.1016/j.ijpsycho.2012.08.001 -> OK Huster et al. 2013 Int J Psychophysiol 87(3):217-233; OpenAlex record has no abstract
- OpenAlex 10.1016/j.neuroimage.2010.01.058 -> resolved to an unrelated paper (van Wingen 2010, BDNF); candidate DOI rejected, not cited
- PubMed 20188191 -> OK abstract (P3 differences localised to inferior frontal cortex); DOI 10.1016/j.neuroimage.2010.02.043
- Crossref 10.1016/j.neuroimage.2010.02.043 -> OK Enriquez-Geppert et al. 2010 NeuroImage 51(2):877-887
- Univ. Iowa repository (Wessel & Aron) -> DOI 10.1111/psyp.12374
- Crossref 10.1111/psyp.12374 -> OK Wessel & Aron 2015 Psychophysiology 52(4):472-480
- Crossref 10.1016/S0001-6918(99)00008-6 -> OK Falkenstein et al. 1999 Acta Psychol 101(2-3):267-291
- PMC5575050 (Hong 2017) -> browser-check page, unreadable; Springer article page -> OK (midcingulate main P3 source; IFG contributes)
- Crossref 10.1038/s41598-017-08807-z -> 429; OpenAlex -> OK Hong et al. 2017 Sci Rep 7(1):9662
- Crossref 10.1016/S0028-3932(99)00106-2 -> 429; OpenAlex -> OK Liotti et al. 2000 Neuropsychologia 38(5):701-711
- Crossref 10.1162/jocn.2008.20020 -> 429; OpenAlex -> OK Hanslmayr et al. J Cogn Neurosci 20(2):215-225 (record date 2007 online; issue 2008, cited as 2008); abstract: ACC source
- Crossref 10.1016/j.ijpsycho.2014.06.007 -> OK Larson, Clayson, Clawson 2014 Int J Psychophysiol 93(3):283-297
- Crossref 10.3389/fpsyg.2010.00025 -> OK but author list incomplete (Karayanidis only); OpenAlex -> full author list from repository citation, Front Psychol 1:25
- Frontiers full text (Karayanidis 2010) -> switch positivity centro-parietal; Jamadar 2010 sPPC correlation
- PubMed 20123028 -> browser-check page; OpenAlex pmid:20123028 -> DOI 10.1016/j.neuroimage.2010.01.090
- Crossref 10.1016/j.neuroimage.2010.01.090 -> OK Jamadar et al. 2010 NeuroImage 51(1):432-449
- UTAS eCite record -> DOI 10.1111/j.1469-8986.2005.00350.x
- Crossref 10.1111/j.1469-8986.2005.00350.x -> OK Nicholson et al. 2005 Psychophysiology 42(5):540-554
- Crossref 10.1038/nn.3248 -> OK O'Connell, Dockree, Kelly 2012 Nat Neurosci 15(12):1729-1735
- Crossref 10.1523/JNEUROSCI.3355-13.2013 -> OK Kelly & O'Connell 2013 J Neurosci 33(50):19434-19441
- Crossref 10.1038/ncomms15808 -> OK Pisauro et al. 2017 Nat Commun 8(1):15808 (abstract: posterior medial frontal cortex)
- OpenAlex pmid:31302254 -> DOI 10.1016/j.neuroimage.2019.116011; no abstract; neuinfo record read for abstract
- Crossref 10.1016/j.neuroimage.2019.116011 -> OK Herding et al. 2019 NeuroImage 201:116011
- Crossref 10.1016/j.tins.2018.06.005 -> OK O'Connell et al. 2018 Trends Neurosci 41(11):838-852
- Crossref 10.1016/0006-8993(82)91115-5 -> OK Kurtzberg & Vaughan 1982 Brain Res 243(1):1-9
- Crossref 10.1111/1469-8986.00106 -> OK Richards 2003 Psychophysiology 40(6):878-894; OpenAlex abstract: presaccadic sources BA 8, 10, 11
- Crossref 10.1016/S0013-4694(96)96569-4 -> 429; OpenAlex -> OK Everling et al. 1997 EEG Clin Neurophysiol 102(4):356-362 (no abstract in record)
- PMC3041007 (Hinkley 2010) and PMC2525985 (Sestieri 2008) -> read; not cited (different signal / no presaccadic analysis)
