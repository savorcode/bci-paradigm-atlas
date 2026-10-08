# 包 C sprint 3 取数日志 / fetch log（curator_b，2026-10-05）

工具：WebFetch（Crossref REST、OpenAlex、PubMed 文章页）。每行一次请求；被拒（429/403）的 URL 不重试，改用其他接口或改写查询。

共 83 次请求。

| # | URL | 结果 | 说明 |
|---|---|---|---|
| 1 | `https://api.crossref.org/works/10.1162/089892902317361886` | ok | record found |
| 2 | `https://api.crossref.org/works/10.1016/j.bandc.2004.02.012` | ok | record found |
| 3 | `https://api.crossref.org/works/10.1016/0042-6989(78)90218-3` | ok | record found |
| 4 | `https://api.crossref.org/works/10.1016/j.visres.2013.02.007` | ok | record found |
| 5 | `https://api.crossref.org/works/10.1037/1076-898x.8.2.75` | ok | record found |
| 6 | `https://api.crossref.org/works/10.1038/203380a0` | ok | record found |
| 7 | `https://api.crossref.org/works/10.1523/JNEUROSCI.0797-14.2015` | ok | record found |
| 8 | `https://api.crossref.org/works/10.1037/h0043220` | ok | record found |
| 9 | `https://api.crossref.org/works/10.1001/archpsyc.1996.01830120037008` | ok | record found (only first author listed) |
| 10 | `https://api.crossref.org/works/10.1093/cercor/bhs261` | ok | record found (issued 2012 online) |
| 11 | `https://api.crossref.org/works/10.1901/jeab.1991.55-233` | ok | record found |
| 12 | `https://api.crossref.org/works/10.1371/journal.pone.0006598` | ok | record found |
| 13 | `https://api.crossref.org/works/10.3758/bf03203267` | 429 | rate limited (parallel burst); not retried, OpenAlex fallback |
| 14 | `https://api.crossref.org/works/10.1126/science.1216930` | ok | record found |
| 15 | `https://api.crossref.org/works/10.1016/0001-6918(69)90065-1` | ok | record found |
| 16 | `https://api.crossref.org/works/10.1016/0010-0277(94)90018-3` | ok | record found |
| 17 | `https://api.crossref.org/works/10.1126/science.1134239` | 429 | rate limited (parallel burst); not retried, OpenAlex fallback |
| 18 | `https://api.crossref.org/works/10.1038/sj.mp.4001217` | ok | record found |
| 19 | `https://api.crossref.org/works/10.1523/jneurosci.12-12-04745.1992` | ok | record found |
| 20 | `https://api.crossref.org/works/10.1523/JNEUROSCI.3355-13.2013` | ok | record found |
| 21 | `https://api.crossref.org/works/10.1037/h0048850` | ok | record found |
| 22 | `https://api.crossref.org/works/10.1016/s0028-3932(97)00015-8` | ok | record found |
| 23 | `https://api.crossref.org/works/10.1037/h0020586` | ok | record found |
| 24 | `https://api.openalex.org/works/doi:10.3758/bf03203267` | ok | record found (OpenAlex fallback) |
| 25 | `https://api.openalex.org/works/doi:10.1126/science.1134239` | ok | record found (OpenAlex fallback) |
| 26 | `https://api.crossref.org/works/10.1037/0033-295x.91.3.295` | ok | record found |
| 27 | `https://api.crossref.org/works/10.1037/h0054651` | ok | record found |
| 28 | `https://api.crossref.org/works/10.1037/0096-3445.124.2.207` | ok | record found |
| 29 | `https://api.crossref.org/works/10.1098/rstb.1982.0082` | ok | record found |
| 30 | `https://api.crossref.org/works/10.1523/JNEUROSCI.2131-07.2007` | ok | record found |
| 31 | `https://api.crossref.org/works/10.1101/262576` | ok | record found (bioRxiv preprint, posted 2018-02-09) |
| 32 | `https://api.crossref.org/works/10.1037/0096-1523.26.1.141` | ok | record found |
| 33 | `https://api.crossref.org/works/10.1111/1469-8986.3850752` | 429 | rate limited; not retried, PubMed fallback |
| 34 | `https://api.crossref.org/works/10.1038/nature04766` | ok | record found |
| 35 | `https://api.crossref.org/works/10.1080/14640748408401502` | 429 | rate limited (proxy); not retried, OpenAlex fallback |
| 36 | `https://pubmed.ncbi.nlm.nih.gov/11577898/` | empty | page returned no article content (JS shell); PubMed not usable via WebFetch |
| 37 | `https://api.openalex.org/works/doi:10.1080/14640748408401502` | ok | record found (OpenAlex fallback) |
| 38 | `https://api.crossref.org/works/10.1523/JNEUROSCI.0822-10.2010` | ok | record found |
| 39 | `https://api.crossref.org/works/10.7554/eLife.46975` | ok | record found |
| 40 | `https://api.openalex.org/works/doi:10.1111/1469-8986.3850752` | ok | record found (OpenAlex fallback; pmid 11577898 confirmed) |
| 41 | `https://api.crossref.org/works/10.1109/TNSRE.2010.2053387` | ok | record found |
| 42 | `https://api.crossref.org/works/10.3389/fnhum.2015.00155` | ok | record found |
| 43 | `https://api.crossref.org/works/10.1126/science.1094285` | ok | record found |
| 44 | `https://api.crossref.org/works/10.1038/nn1239` | ok | record found |
| 45 | `https://api.crossref.org/works/10.1101/lm.1.2.106` | ok | record found |
| 46 | `https://api.crossref.org/works/10.1523/jneurosci.22-11-04563.2002` | ok | record found |
| 47 | `https://api.crossref.org/works/10.1126/science.1102941` | ok | record found |
| 48 | `https://api.crossref.org/works/10.1162/jocn.1997.9.6.788` | ok | record found |
| 49 | `https://api.crossref.org/works/10.1016/j.neuron.2011.02.027` | ok | record found |
| 50 | `https://api.crossref.org/works/10.1371/journal.pcbi.1005090` | ok | record found |
| 51 | `https://api.crossref.org/works/10.1145/3290605.3300657` | ok | record found (proceedings-article, pages 1-11) |
| 52 | `https://api.crossref.org/works/10.3389/fnrgo.2024.1411305` | ok | record found |
| 53 | `https://api.crossref.org/works?query.bibliographic=Hsu+Bhatt+Adolphs+Tranel+Camerer+Neural+Systems+Responding+to+Degrees+of+Uncertainty+in+Human+Decision-Making+2005&rows=3&select=...` | ok | irrelevant hits (long query mis-ranked); re-queried shorter |
| 54 | `https://api.crossref.org/works?query.bibliographic=Bunge+Wendelken+Badre+Wagner+Analogical+reasoning+...+2005&rows=3` | 403 | proxy: URL exceeds maximum length; re-queried shorter |
| 55 | `https://api.crossref.org/works?query.bibliographic=Fink+Grabner+Benedek+The+creative+brain+...+2009&rows=3` | 403 | proxy: URL exceeds maximum length; re-queried shorter |
| 56 | `https://api.crossref.org/works?query.bibliographic=Telford+The+refractory+phase+of+voluntary+and+associative+responses+1931&rows=3` | ok | top hit 10.1037/h0073262 matches |
| 57 | `https://api.crossref.org/works?query.bibliographic=Hsu+Camerer+degrees+of+uncertainty+human+decision-making+Science+2005&rows=3` | ok | top hit 10.1126/science.1115327 matches |
| 58 | `https://api.crossref.org/works?query.bibliographic=Bunge+Analogical+reasoning+and+prefrontal+cortex+2005&rows=3` | ok | top hit 10.1093/cercor/bhh126 matches (Crossref lists first author only; issued 2004 online) |
| 59 | `https://api.crossref.org/works?query.bibliographic=Fink+Grabner+The+creative+brain+EEG+fMRI+2009&rows=3` | ok | top hit 10.1002/hbm.20538 matches (issued 2008 online) |
| 60 | `https://api.crossref.org/works?query.bibliographic=Eimer+Schlaghecken+Effects+of+masked+stimuli+on+motor+activation+1998&rows=3` | 429 | proxy rate limit; not retried; re-queried later with different wording |
| 61 | `https://api.crossref.org/works?query.bibliographic=Eimer+Schlaghecken+masked+stimuli+motor+activation+behavioral+electrophysiological+1998&rows=3` | 429 | proxy rate limit; not retried; OpenAlex search fallback |
| 62 | `https://api.crossref.org/works?query.bibliographic=Penrose+Raven+A+new+series+of+perceptual+tests+preliminary+communication+1936&rows=3` | ok | top hit 10.1111/j.2044-8341.1936.tb00690.x matches |
| 63 | `https://api.openalex.org/works?search=Eimer+Schlaghecken+Effects+of+masked+stimuli+on+motor+activation&per-page=3` | 429 | OpenAlex rate limited; not retried |
| 64 | `https://api.crossref.org/works?query.bibliographic=Jahanshahi+Dirnberger+dorsolateral+prefrontal+cortex+random+number+generation+positron+emission+tomography+2000&rows=3` | ok | irrelevant hits (long query truncated by proxy); re-queried shorter |
| 65 | `https://api.crossref.org/works?query.bibliographic=Jahanshahi+random+number+generation+PET+2000&rows=3` | 429 | proxy rate limit; not retried |
| 66 | `https://api.crossref.org/works?query.bibliographic=Jahanshahi+dorsolateral+prefrontal+random+number+generation+NeuroImage+2000&rows=3` | ok | top hit 10.1006/nimg.2000.0647 matches |
| 67 | `https://api.crossref.org/works?query.bibliographic=Meiran+Reconfiguration+of+processing+mode+prior+to+task+performance+1996&rows=3` | ok | top hit 10.1037/0278-7393.22.6.1423 matches |
| 68 | `https://api.crossref.org/works?query.bibliographic=Goel+Buchel+Frith+Dolan+Dissociation+of+mechanisms+underlying+syllogistic+reasoning+2000&rows=3` | 429 | proxy rate limit; not retried; re-queried with different wording later |
| 69 | `https://api.crossref.org/works?query.bibliographic=Goel+Dolan+syllogistic+reasoning+NeuroImage+2000&rows=3` | 429 | proxy rate limit; not retried |
| 70 | `https://api.openalex.org/works?search=Goel+Dolan+syllogistic+reasoning+dissociation+mechanisms&per-page=3` | 429 | OpenAlex rate limited; not retried |
| 71 | `https://api.crossref.org/works?query.bibliographic=Goel+syllogistic+reasoning+dissociation+NeuroImage+2000&rows=3` | 429 | proxy rate limit; not retried |
| 72 | `https://api.crossref.org/works?query.bibliographic=Goel+Buchel+Frith+Dolan+syllogistic+reasoning+2000&rows=3` | 429 | proxy rate limit (global WebFetch budget); not retried |
| 73 | `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AUTH:"Goel V" AND TITLE:"syllogistic reasoning" AND PUB_YEAR:2000&format=json` | 429 | proxy rate limit (global); Europe PMC not retried |
| 74 | `https://api.crossref.org/works?query.bibliographic=Goel+Dolan+Dissociation+of+mechanisms+underlying+syllogistic+reasoning&rows=3` | ok | top hit 10.1006/nimg.2000.0636 matches |
| 75 | `https://api.crossref.org/works?query.bibliographic=Grant+Berg+behavioral+analysis+degree+of+reinforcement+Weigl-type+card+sorting+1948&rows=3` | 429 | proxy rate limit (global); not retried; re-queried later with different wording |
| 76 | `https://api.crossref.org/works?query.bibliographic=Grant+Berg+1948+Weigl-type+card+sorting+problem&rows=3` | ok | top hit 10.1037/h0059831 matches |
| 77 | `https://api.crossref.org/works?query.bibliographic=Krakauer+Learning+of+visuomotor+transformations+for+vectorial+planning+of+reaching+trajectories+2000&rows=3` | ok | irrelevant hits (query >~90 chars is truncated by proxy); re-queried shorter |
| 78 | `https://api.crossref.org/works?query.bibliographic=Krakauer+visuomotor+transformations+vectorial+planning+reaching+2000&rows=3` | ok | top hit 10.1523/jneurosci.20-23-08916.2000 matches |
| 79 | `https://api.crossref.org/works?query.bibliographic=O'Doherty+Temporal+difference+models+reward-related+learning+human+brain+Neuron+2003&rows=3` | ok | top hit 10.1016/s0896-6273(03)00169-7 matches title/venue/year (citation had no authors) |
| 80 | `https://api.crossref.org/works?query.bibliographic=Hester+Garavan+error+processing+errors+made+with+and+without+awareness+2005&rows=3` | 429 | Crossref 429; not retried; re-queried with different wording |
| 81 | `https://api.crossref.org/works?query.bibliographic=Hester+Foxe+Molholm+Shpaner+Garavan+NeuroImage+2005+error+awareness&rows=3` | 429 | proxy rate limit; not retried |
| 82 | `https://api.crossref.org/works?query.bibliographic=Hester+Garavan+2005+Neural+mechanisms+involved+in+error+processing&rows=3` | ok | top hit 10.1016/j.neuroimage.2005.04.035 matches |
| 83 | `https://api.crossref.org/works?query.bibliographic=Ferrez+Millan+2008+Error-related+EEG+potentials+simulated+brain-computer+interaction&rows=3` | 429 | proxy rate limit; not retried; search budget exhausted - remaining rows marked not checked |
