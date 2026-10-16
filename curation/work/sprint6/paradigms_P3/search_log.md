# Search log, sprint 6, group P3 (2026-10-16)

Web searches used: 8 of 30. Every cited DOI was checked against the Crossref API or, where Crossref failed or was rate-limited, the OpenAlex API.

## Web searches

| # | Query | Outcome |
|---|---|---|
| 1 | Jiang Dai Peng Zhu Liu Lu 2012 "Neural synchronization during face-to-face communication" Journal of Neuroscience doi | PubMed and PMC records found (both behind a browser check, unreadable). Correct DOI then taken from OpenAlex title search. |
| 2 | Jiang 2012 face-to-face dialog back-to-back monologue fNIRS hyperscanning task lasted minutes resting-state session methods | MPI record (abstract only); methods read on the Journal of Neuroscience article page (jneurosci.org/content/32/45/16064). |
| 3 | public goods game fMRI neural basis contributions free riding first neuroimaging study | Led to Krajbich et al. 2009 (Science); no standard neural PGG protocol identified. |
| 4 | public goods game EEG feedback-related negativity contributions group members ERP study | Only recent, specialised ERP studies (2022-2025); none cited. |
| 5 | "public goods game" fMRI striatum conditional cooperation contributions others ... | Several fMRI studies of cooperator types; none retrieved in detail, none cited. |
| 6 | OpenNeuro "A resting-state EEG dataset for sleep deprivation" Scientific Data ds004902 | Dataset paper (Xiang et al. 2024) and EEGDash listing of ds004902 (71 subjects). |
| 7 | Vrana Spence Lang 1988 startle probe slides 6 s white noise 50 ms 95 dB ... | Probe P3 paper (Schupp et al. 1997) found via KOPS Konstanz; probe parameters of the 1988 paper not confirmed. |
| 8 | Boksem Meijman Lorist 2005 "Effects of mental fatigue on attention: an ERP study" ... | Authors' PDF (boksem.nl); methods and results read. |

## Pages read

| URL | Outcome |
|---|---|
| pubmed.ncbi.nlm.nih.gov/23136442 ; pmc.ncbi.nlm.nih.gov/articles/PMC6621612 | Browser check page, no content. |
| forms.mpi.nl/node/46532 | Abstract of Jiang et al. 2012 only. |
| www.jneurosci.org/content/32/45/16064 | Jiang et al. 2012 methods: 10 pairs, 3-min eyes-closed rest, 4 conditions x 10 min with 30-s rests, ETG-4000, 20 + 3 channels, 10 Hz. Used for SOC-DIAL-001. |
| kops.uni-konstanz.de (Schupp et al. 1997 record) | Citation, DOI and abstract of probe P3 paper. |
| doaj.org (Xiang et al. 2024) | Dataset paper metadata; hours of deprivation not stated. |
| read.qxmd.com/read/38658675 | Abstract only; hours of deprivation not stated. |
| www.boksem.nl/pdf/boksem2005cbr.pdf | Boksem et al. 2005 full text: task, timing, 3 h without pauses, spectral and ERP results. Used for the STA-FAT-001 variant. |

## Bibliographic API checks

| DOI | API | Outcome |
|---|---|---|
| 10.1037/0021-843X.97.4.487 | Crossref | First request (upper-case DOI) failed; lower-case request succeeded; also OpenAlex. Vrana, Spence & Lang 1988. |
| 10.1037/0033-295x.97.3.377 | Crossref | OK. Lang, Bradley & Cuthbert 1990. |
| 10.1111/j.1469-8986.2005.00271.x | Crossref failed; OpenAlex OK | Blumenthal et al. 2005. |
| 10.1111/j.1469-8986.1997.tb02409.x | Crossref rate-limited; OpenAlex OK | Schupp et al. 1997. |
| 10.1037/h0047274 | Crossref | OK. Solarz 1960. |
| 10.1177/0146167299025002007 | Crossref | OK. Chen & Bargh 1999. |
| 10.1016/j.jbtep.2006.10.001 | Crossref | OK. Rinck & Becker 2007. |
| 10.1093/scan/nsn036 | Crossref | OK. Roelofs et al. 2009. |
| 10.1523/JNEUROSCI.1191-12.2012 | Crossref rate-limited; OpenAlex failed | DOI recalled from memory was wrong; not used. |
| 10.1523/jneurosci.2926-12.2012 | OpenAlex (title search and DOI lookup) OK; Crossref rate-limited | Jiang et al. 2012. |
| 10.1038/srep12881 | Crossref | OK. Bögels, Magyari & Levinson 2015. |
| 10.1086/226937 | Crossref | OK. Marwell & Ames 1979. |
| 10.1257/aer.90.4.980 | Crossref | OK. Fehr & Gächter 2000. |
| 10.1126/science.1177302 | OpenAlex (title search) | OK. Krajbich et al. 2009. |
| 10.1016/s0022-5371(73)80042-8 | Crossref | OK. Forster & Chambers 1973. |
| 10.1038/331585a0 | Crossref | OK. Petersen et al. 1988. |
| 10.1111/1469-8986.3750614 | Crossref; OpenAlex for abstract | OK. Lorist et al. 2000. |
| 10.1016/j.cogbrainres.2005.04.011 | Crossref; OpenAlex (no abstract) | OK. Boksem et al. 2005. |
| 10.1037/h0075739 | Crossref; OpenAlex (no abstract) | OK. Patrick & Gilbert 1896. |
| 10.1016/0013-4694(81)90225-x | Crossref; OpenAlex (no abstract) | OK. Borbély et al. 1981. |
| 10.1093/sleep/18.10.890 | OpenAlex | OK, with abstract. Cajochen et al. 1995. |
| 10.1038/s41597-024-03268-2 | Crossref | OK. Xiang et al. 2024; reference list gives OpenNeuro DOI 10.18112/openneuro.ds004902.v1.0.4. |
