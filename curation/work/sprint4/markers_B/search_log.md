# Search log — curator_b, sprint 4 (2026-10-12)

Tooling note: `curl` from the sandbox to api.crossref.org / api.openalex.org / eutils is blocked by the egress proxy (403 CONNECT); all record checks were done with HTTP request. Crossref via HTTP request returned HTTP 429 on most attempts, so OpenAlex (`api.openalex.org/works/doi:<DOI>`) was used as the primary record source (allowed fallback). PubMed / PMC pages returned a reCAPTCHA interstitial (unusable).

## web search (9 calls)
| # | query | outcome |
|---|---|---|
| 1 | low-frequency EEG movement kinematics decoding review source localization Kobler Müller-Putz positions velocities | Found Kobler 2018 Sci Rep, Srisrisawang 2022 (not used) |
| 2 | lateralized readiness potential generator primary motor cortex MEG dipole source analysis Praamstra | Found Leuthold & Jentzsch 2002 (St Andrews portal) |
| 3 | Leuthold Jentzsch 2002 "Distinguishing neural sources..." Biological Psychology doi | Confirmed portal page |
| 4 | Nagai Critchley 2004 "Brain activity relating to the CNV" fMRI NeuroImage doi | PMID 15050551 (neurosynth) |
| 5 | Brunia van Boxtel 2001 "Wait and see" IJP doi CNV SPN | No usable DOI; van Boxtel & Brunia 1994 page lacked DOI — dropped |
| 6 | Hamano Lüders Ikeda 1997 cortical generators of the CNV subdural electrodes doi | Not found; led to Bareš 2007 SEEG CNV |
| 7 | CNV generators intracranial recordings SMA anterior cingulate review doi | Bareš, Nestrašil, Rektor 2007 (UMN portal) |
| 8 | Boveroux 2010 propofol "Breakdown of within- and between-network..." Anesthesiology doi | ULiège pages → DOI 10.1097/ALN.0b013e3181f697f5 |
| 9 | Murphy ... 2009 "Source modeling sleep slow waves" PNAS doi | Wisconsin lab page → DOI 10.1073/pnas.0807933106 |

## HTTP request — record checks
| url | outcome |
|---|---|
| api.crossref.org/works/10.1093/brain/121.12.2271 | 429 first; later OK — record lists only "Crone, N." as author |
| api.crossref.org/works/10.1093/brain/121.12.2301 | OK — only "Crone, N." |
| api.crossref.org/works/10.1523/JNEUROSCI.5212-05.2006 | 429 (source dropped) |
| api.crossref.org/works/10.1097/ALN.0b013e3181f697f5 | OK (Boveroux 2010, 16 authors, 113(5):1038-1053) |
| api.openalex.org/works?filter=doi:... (batch, 3 attempts) | URL too long / fetch error — batching abandoned |
| openalex doi:10.1093/brain/121.12.2271, 121.12.2301 | OK (single author in record) |
| openalex doi:10.1016/0306-4522(94)90263-1 | OK Salmelin & Hari 1994 |
| openalex doi:10.1002/hbm.20585 | OK Ritter 2009 (OpenAlex year 2008 = online; vol 30 = 2009) |
| openalex doi:10.1037/bul0000031 | OK Fox 2016 (vol 142) |
| openalex doi:10.1016/j.neuroimage.2005.12.003 | OK Pfurtscheller 2006 |
| openalex doi:10.1073/pnas.0913697107 | OK Miller 2010 |
| openalex doi:10.1016/S0167-8760(96)00066-9 | OK Pfurtscheller 1996 |
| openalex doi:10.1016/S1388-2457(99)00141-8 | OK (existing source re-checked) |
| openalex doi:10.1016/S0304-3940(97)00889-6 | OK (existing source re-checked) |
| openalex doi:10.1371/journal.pbio.1001080 | 429, then OK but WRONG paper (amyloid) — intended Ray & Maunsell 2011; dropped |
| openalex doi:10.1523/JNEUROSCI.2041-09.2009 | OK Manning 2009 (retrieved, not cited) |
| openalex doi:10.1016/j.pneurobio.2012.06.008 | 429, then OK Lachaux 2012 (retrieved, not cited) |
| openalex doi:10.1038/nature11020 | OK Mesgarani & Chang 2012 |
| openalex doi:10.1371/journal.pbio.1001251 | 429, then OK Pasley 2012 |
| openalex doi:10.1038/nature11911 | OK Bouchard 2013 |
| openalex doi:10.1126/science.1110948 | OK but WRONG paper (Niessing 2005) — intended Mukamel 2005; dropped |
| openalex doi:10.1523/JNEUROSCI.3886-06.2007 | OK Miller 2007 |
| openalex doi:10.1016/S0079-6123(06)59019-3 | OK Crone 2006 |
| openalex doi:10.1523/JNEUROSCI.6107-09.2010 | OK Bradberry 2010 (record N=4 authors) |
| openalex doi:10.1523/JNEUROSCI.5171-07.2008 | OK Waldert 2008 |
| openalex doi:10.1088/1741-2560/4/3/012 | OK Schalk 2007 |
| openalex doi:10.3389/fnhum.2022.830221 | OK Srisrisawang 2022 (not cited) |
| openalex doi:10.1038/s41598-018-36326-y | OK Kobler 2018 |
| openalex doi:10.1371/journal.pone.0061976 | 429 — Antelis 2013 not cited |
| openalex doi:10.1523/JNEUROSCI.02-11-01527.1982 | OK Georgopoulos 1982 |
| openalex doi:10.1126/science.3749885 | OK Georgopoulos 1986 |
| openalex doi:10.1038/nature04970 | OK Hochberg 2006 |
| openalex doi:10.1038/nature04968 | OK Santhanam 2006 |
| openalex doi:10.1016/S0140-6736(12)61816-9 | OK Collinger 2013 |
| openalex doi:10.1038/nature11129 | OK Churchland 2012 |
| openalex doi:10.1523/JNEUROSCI.5212-05.2006 | fetch error (likely 404) — Churchland 2006 dropped |
| openalex doi:10.1038/s41586-023-06377-x | OK Willett 2023 |
| openalex doi:10.1056/NEJMoa2314132 | OK Card 2024 |
| openalex doi:10.1038/s41586-021-03506-2 | OK Willett 2021 |
| openalex doi:10.1037/0096-1523.14.3.331 | OK Gratton 1988 |
| openalex doi:10.1111/j.1469-8986.1989.tb01916.x | 429, then OK Coles 1989 |
| openalex doi:10.1037/0096-1523.16.1.164 | OK De Jong 1990 |
| openalex works?search=... (2 attempts) | fetch error — search endpoint unusable |
| openalex doi:10.1016/S0926-6410(99)00008-8 | fetch error — Praamstra 1999 MEG LRP not cited |
| research-portal.st-andrews.ac.uk (Leuthold & Jentzsch) | OK, DOI 10.1016/S0301-0511(02)00032-7 |
| openalex doi:10.1016/S0301-0511(02)00032-7 | OK (OpenAlex title lacks subtitle; subtitle from publisher portal) |
| openalex doi:10.1016/j.clinph.2006.04.025 | OK Shibasaki & Hallett 2006 |
| openalex doi:10.1093/brain/115.4.1017 | OK Ikeda 1992 |
| openalex doi:10.1111/j.1469-8986.1996.tb00839.x | fetch error ×2 — Kopp 1996 not cited |
| openalex doi:10.1007/BF00412364 | OK Kornhuber & Deecke 1965 |
| openalex doi:10.1016/S1053-8119(03)00291-X | OK Cunnington 2003 (title truncated by tool; subtitle completed from known title) |
| openalex doi:10.1088/1741-2560/8/6/066009 | OK Niazi 2011 |
| openalex doi:10.1073/pnas.1210467109 | OK Schurger 2012 |
| openalex doi:10.1093/brain/106.3.623 | OK Libet 1983 |
| openalex doi:10.1038/203380a0 | OK Walter 1964 |
| openalex doi:10.1016/S0167-8760(01)00160-X | WRONG paper (Gordon 2001) — intended Brunia & van Boxtel 2001; dropped |
| openalex doi:10.1016/j.neuroimage.2003.11.013 | WRONG paper (Iacoboni 2004) — dropped |
| openalex pmid:15050551 | OK Nagai 2004 → DOI 10.1016/j.neuroimage.2003.10.036 |
| tilburguniversity repository item (van Boxtel & Brunia 1994) | no DOI — not cited |
| openalex doi:10.1126/science.1257753 | 429, then WRONG paper (Meyer & Schvaneveldt) — Rohrbaugh 1976 dropped |
| openalex doi:10.1037/h0032177 | OK Tecce 1972 |
| pmc.ncbi.nlm.nih.gov/articles/PMC2932695; openalex pmcid:PMC2932695 | reCAPTCHA / 429 / fetch error — not used |
| experts.umn.edu (Bareš 2007); muni.cz page | OK, DOI 10.1016/j.brainresbull.2006.10.012 |
| openalex doi:10.1016/j.brainresbull.2006.10.012 | OK Bareš 2007 (OpenAlex year 2006 online; vol 71 = 2007) |
| openalex doi:10.1152/physrev.00042.2018 | OK Fernandez & Lüthi 2020 (vol 100) |
| openalex doi:10.1126/science.8235588 | OK Steriade 1993 Science |
| openalex doi:10.1073/pnas.0703084104 | OK Schabus 2007 |
| openalex doi:10.1523/JNEUROSCI.2604-11.2011 | OK Andrillon 2011 |
| openalex doi:10.1016/j.neuropsychologia.2023.108661 | OK Kumral 2023 (no abstract in record) |
| openalex doi:10.1523/JNEUROSCI.13-08-03252.1993 | OK Steriade, Nuñez, Amzica 1993 |
| openalex doi:10.1523/JNEUROSCI.1318-04.2004 | OK Massimini 2004 (record swaps vol/issue: 24(31)) |
| openalex doi:10.1073/pnas.0809933106 | fetch error — wrong DOI guess for Murphy 2009 |
| openalex doi:10.1073/pnas.0807933106 | OK Murphy 2009 |
| openalex doi:10.1016/j.neuron.2011.02.043 | OK Nir 2011 (no abstract; not cited) |
| openalex doi:10.1073/pnas.0801819105 | OK Dang-Vu 2008 |
| openalex doi:10.1111/jsr.12371 | OK Borbély 2016 |
| openalex doi:10.1038/nature05278 | OK Marshall 2006 |
| openalex doi:10.1016/j.neuron.2013.03.006 | OK Ngo 2013 |
| openalex doi:10.1073/pnas.1221180110 | OK Purdon 2013 |
| openalex doi:10.1073/pnas.98.2.676 | OK Raichle 2001 |
| openalex doi:10.1073/pnas.0135058100 | OK Greicius 2003 (vol 100) |
| openalex doi:10.1523/JNEUROSCI.4004-09.2009 | OK Laird 2009 |
| openalex doi:10.1016/j.neuroimage.2015.02.039 | OK Fox KCR 2015 |
| openalex doi:10.1016/j.neuroimage.2011.05.028 | OK Qin & Northoff 2011 |
| openalex doi:10.1162/jocn.2008.21029 | OK Spreng 2009 (vol 21) |
| openalex doi:10.1093/brain/awp313 | OK Vanhaudenhuyse 2010 (vol 133) |
| openalex doi:10.1097/ALN.0b013e3181f697f5 | server error ×2 → confirmed via Crossref |
| coma.uliege.be, orbi.uliege.be (Boveroux) | bibliographic details |
| openalex doi:10.1196/annals.1440.011 | OK Buckner 2008 |
| pubmed.ncbi.nlm.nih.gov/?term=... (2) | reCAPTCHA / error |
