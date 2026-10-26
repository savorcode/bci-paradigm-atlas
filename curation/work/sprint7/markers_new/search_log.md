# Sprint 7, new markers (D-079): search log (curator_m, 2026-10-17)

## Web searches (2)

| # | Query | Outcome |
|---|---|---|
| 1 | Funayama Grillon Davis Phelps 2001 double dissociation affective modulation of startle unilateral temporal lobectomy doi | No DOI for Funayama et al. found; led to Buchanan, Tranel & Adolphs 2004 (University of Iowa repository page), DOI 10.1037/0735-7044.118.2.429 |
| 2 | P2p numerical distance effect parietal ERP number comparison Dehaene 1996 latency right parietal | Hyde & Spelke 2012 (Hum Brain Mapp) PDF on the Harvard Lab for Developmental Studies site; read for P2p latency window, right-lateralization and the studies it cites (Dehaene 1996, Temple & Posner 1998, Libertus et al. 2007, Pinel et al. 2001) |

Other candidates came from the sprint 6 marker requests (Varela 1981, Zatorre 2002, Dehaene 1996, Vrana 1988, Blumenthal 2005, Schupp 1997), the EMO-STARTLE-001 notes (Lang 1990) and the curator's reading list.

## Record look-ups

Crossref API (https://api.crossref.org/works/<DOI>), retrieved OK: 10.1093/brain/119.6.1991; 10.1111/j.1469-8986.1991.tb01999.x; 10.1007/s002130100810; 10.1016/0028-3932(81)90005-1; 10.1152/jn.00424.2009; 10.3758/BF03206172; 10.1162/jocn.1996.8.1.47; 10.1006/nimg.2001.0913.

OpenAlex API (https://api.openalex.org/works/doi:<DOI>), retrieved OK: 10.1037/1528-3542.1.3.276 (Crossref fetch error first); 10.1037/0735-7044.118.2.429; 10.1037/0021-843x.97.4.487; 10.1037/0033-295x.97.3.377; 10.1111/j.1469-8986.2005.00271.x; 10.1523/JNEUROSCI.3963-08.2009; 10.1523/JNEUROSCI.1161-11.2011; 10.1016/j.neuroimage.2016.02.065; 10.1111/ejn.14186; 10.1016/j.cortex.2019.05.012 (no abstract; not cited); 10.1016/0013-4694(89)90192-2; 10.1016/0028-3932(72)90063-2 (no abstract); 10.1523/JNEUROSCI.23-13-05799.2003; 10.1038/nn904; 10.1073/pnas.0510480103; 10.1111/j.1460-9568.2006.05025.x; 10.1002/hbm.21352; 10.1073/pnas.95.13.7836; 10.1016/j.neuroimage.2010.10.009.

Failures and rejections:
- 10.1162/089892901750363217: Crossref record is Kinder & Shanks 2001 (amnesia model), not Funayama et al. 2001 as expected. DOI discarded; Funayama et al. not cited.
- 10.1146/annurev.ne.15.030192.002033 (Davis 1992, amygdala in fear and anxiety): Crossref and OpenAlex both returned HTTP 429. Not cited.
- 10.1523/JNEUROSCI.0113-09.2009 (Busch, Dubois & VanRullen 2009): OpenAlex and Crossref both returned HTTP 429. Not cited.
- 10.1186/1744-9081-3-1 (Libertus, Woldorff & Brannon 2007): OpenAlex returned 429; the Crossref record has authors, journal and volume but an empty title field. Not cited.
- 10.1111/ejn.14186, 10.1002/hbm.21352, 10.1016/j.neuroimage.2010.10.009: OpenAlex gives the online year; the issue year is cited.
