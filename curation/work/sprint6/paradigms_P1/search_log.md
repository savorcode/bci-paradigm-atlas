# Search log - sprint 6, group P1 (curator_b, 2026-10-16)

Web searches: 11 of 30 allowed. Bibliographic records: Crossref API (`https://api.crossref.org/works/<DOI>`), OpenAlex API (`https://api.openalex.org/works/doi:<DOI>`) where Crossref returned HTTP 429.

## Web searches

| # | Query / URL | Outcome |
|---|---|---|
| W01 | Flesher 2016 intracortical microstimulation human somatosensory cortex, stimulus parameters | Abstract (Barrow repository) and authors' manuscript on the Schwartz lab site; protocol parameters taken from the manuscript (several units misprinted, noted in STM-ICMS-001) |
| W02 | history of visual cortical prosthesis, Foerster 1929, Brindley & Lewin 1968, Dobelle | Webvision chapter (Fernández & Normann): Foerster 1929 first report of phosphenes on stimulation of the occipital pole; Brindley & Lewin 1968 first implanted prosthesis; Dobelle 1974-76; Schmidt et al. 1996 intracortical. Foerster not retrieved as a record |
| W03 | Fernández 2021 JCI Utah array occipital cortex | VU repository abstract: 96-channel array, 57-year-old blind participant, threshold 66.8 +/- 36.5 uA, ~6 months. PMC page blocked by a browser check |
| W04 | Terney et al. 2008 tRNS title + DOI | DOI not in results; a remembered DOI (10.1523/JNEUROSCI.2848-08.2008) resolved to an unrelated paper (Ray et al. 2008, high-gamma) and was discarded; correct DOI 10.1523/JNEUROSCI.4248-08.2008 confirmed by OpenAlex record (authors and title match). Frontiers event abstract (Moliadze et al. 2008) gave the MEP read-out schedule |
| W05 | "No frequency-specific effect of tRNS on resting EEG" | Ke, Lo & Tseng 2024, J Integr Neurosci, DOI 10.31083/j.jin2303059 |
| W06 | electrical stimulation mapping parameters (50 Hz, pulse width, train length, afterdischarges) | Conference slides only (not citable); used to find a review |
| W07 | Ritaccio, Brunner & Schalk 2018 ESM review | Author PDF on neurotechcenter.org: 50/60 Hz, biphasic constant current, 1-2 s trains for sensorimotor sites, <=10 s for language, afterdischarge monitoring, high-gamma ECoG mapping as alternative, historical precursors (Bartholow 1874, Sciamanna 1882, Krause, Foerster, Penfield 1937) |
| W08 | Biasiucci 2018 BCI-FES stroke protocol | UNIGE repository abstract: sham-FES control, lasting recovery 6-12 months, connectivity change; task (imagined vs attempted) not stated |
| W09 | Beauchamp 2020 dynamic stimulation of visual cortex, parameters | bioRxiv preprint full text: 200 Hz, 0.1 ms/phase, 50-200 ms per electrode, 4AFC 15/23 correct, blind participant with RNS strips |
| W10 | Esser et al. 2006 combined TMS/EEG LTP | Citation only (lab publication page); PMC follow-up paper blocked; rTMS parameters not extracted |
| W11 | Flesher 2021 Science tactile BCI robotic arm | bioRxiv preprint full text: ARAT 27 trials/session, torque 0.1-0.5 Nm -> 14-64 uA at 100 Hz, grasp time 13.8 -> 5.8 s |

## Bibliographic record checks

| DOI | API | Result |
|---|---|---|
| 10.1126/scitranslmed.aaf8083 | Crossref | ok (no page/article number in record) |
| 10.1126/science.abd0380 | Crossref | ok |
| 10.1101/653428 | Crossref | ok (preprint of 10.1126/science.abd0380) |
| 10.1038/nrn3724 | Crossref | ok |
| 10.1113/jphysiol.1968.sp008519 | Crossref | ok |
| 10.1172/JCI151331 | Crossref | ok |
| 10.1016/j.cell.2020.04.033 | Crossref | ok |
| 10.1101/462697 | Crossref | ok (preprint of 10.1016/j.cell.2020.04.033) |
| 10.1093/brain/117.4.847 | Crossref | ok |
| 10.1016/j.neuron.2004.12.033 | Crossref | ok |
| 10.1016/j.brainresbull.2005.11.003 | Crossref -> OpenAlex | Crossref HTTP 429; OpenAlex ok (publication_year 2005) |
| 10.1523/JNEUROSCI.2848-08.2008 | Crossref -> OpenAlex | Crossref HTTP 429; OpenAlex: different paper (Ray et al. 2008) - discarded |
| 10.1523/JNEUROSCI.4248-08.2008 | OpenAlex | ok (Terney et al. 2008) |
| 10.31083/j.jin2303059 | Crossref | ok |
| 10.1155/2016/3616807 | Crossref | ok |
| 10.1093/brain/60.4.389 | Crossref | ok |
| 10.3171/jns.1989.71.3.0316 | Crossref | ok |
| 10.1097/WNP.0000000000000440 | Crossref | ok |
| 10.1038/s41586-023-06094-5 | Crossref | ok |
| 10.1016/S0304-3940(03)00947-9 | Crossref | ok |
| 10.1038/s41467-018-04673-z | Crossref | ok |
| 10.3389/fnpro.2010.00003 | Crossref, OpenAlex | title matches; both records list only one author (Pfurtscheller G) |
| 10.1088/1741-2560/7/2/026007 | Crossref -> OpenAlex | Crossref HTTP 429; OpenAlex ok |
| 10.1109/TBME.2011.2116018 | Crossref | ok |
