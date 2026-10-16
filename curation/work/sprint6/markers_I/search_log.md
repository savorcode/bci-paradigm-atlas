# Sprint 6, markers I: search log (curator I, 2026-10-16)

## Web searches (5 of 25 allowed)

| # | Query | Outcome |
|---|---|---|
| 1 | Tobimatsu 1999 steady-state vibration somatosensory evoked potentials ... Clinical Neurophysiology doi | Tobimatsu record not found; led to Snyder 1992 profile page (DOI 10.1016/0168-5597(92)90007-X) |
| 2 | steady-state somatosensory evoked potential MEG source primary somatosensory cortex SII generators vibrotactile | Vakorin et al. 2019 (Front Neural Circuits), MEG source S1 -> SII |
| 3 | Hinterberger 2005 "Neuronal mechanisms underlying control of a brain-computer interface" slow cortical potential fMRI regions | Max Planck publication page (poster abstract of the same EEG-fMRI study) |
| 4 | concurrent TMS-fMRI review overview of previous studies stimulation target primary motor cortex BOLD at stimulated site | Rafiei & Rahnev 2022 (eNeuro) and Mizutani-Tiebel et al. 2022 (Front Psychiatry); Bestmann et al. 2008 DOI |
| 5 | Hinterberger Veit Wilhelm Weiskopf 2005 slow cortical potentials EEG fMRI basal ganglia positivity premotor pubmed abstract | no journal abstract; IGPP page was an unrelated 2016 review (not used) |

Other candidates came from curation/literature.csv (Boccia 2014, Epstein 2008, Epstein 2017, Zaehle 2010, Ahn 2016) and from the curator's reading list.

## Record look-ups

Crossref API (https://api.crossref.org/works/<DOI>), retrieved OK: 10.1016/j.cub.2013.12.041; 10.1371/journal.pone.0013766; 10.1016/j.cub.2011.05.049; 10.3389/fnhum.2013.00279; 10.1126/science.1117256; 10.1126/scitranslmed.3006294 (no article number in record, taken from OpenAlex API); 10.1016/j.clinph.2019.01.001; 10.1152/physrev.1990.70.1.1; 10.1038/18581; 10.1111/j.1460-9568.2005.04092.x; 10.1542/peds.2005-2478; 10.1016/S0926-6410(02)00066-6; 10.1523/JNEUROSCI.2875-08.2008; 10.1007/s10548-014-0365-7; 10.1016/j.tics.2010.06.008; 10.1162/0898929054475172; 10.1007/s11065-014-9247-8; 10.1016/j.tics.2008.07.004; 10.1038/nn.4656; 10.1038/33402; 10.1126/science.1130197; 10.1056/NEJMoa0905370; 10.1162/08989290051137549; 10.1016/j.neuroimage.2009.12.112; 10.1016/j.neubiorev.2011.07.004; 10.1126/science.1097011; 10.1016/j.neuroimage.2016.12.052; 10.1016/j.neubiorev.2013.03.017; 10.1016/j.cogbrainres.2004.01.004; 10.1016/0168-5597(92)90007-X; 10.3389/fncir.2018.00118; 10.1523/ENEURO.0163-22.2022; 10.3389/fpsyt.2022.825205.

Crossref API failures (HTTP 429, or fetch error), confirmed via OpenAlex API (https://api.openalex.org/works/doi:<DOI>):
- 10.1097/00001756-199711100-00024 (Ilmoniemi 1997): 429 -> OpenAlex OK (PMID 9427322)
- 10.1162/089892999563544 (Giard & Peronnet 1999): 429 -> OpenAlex OK (PMID 10511637)
- 10.1109/TNSRE.2005.863842 (Müller-Putz 2006): 429 -> OpenAlex OK (PMID 16562629)
- 10.3389/fnhum.2015.00716 (Ahn 2016): fetch error -> OpenAlex OK (PMID 26834611)
- 10.1007/s00221-008-1601-8 (Bestmann 2008): 429 -> OpenAlex OK (PMID 18936922; no abstract in record)
- 10.1111/j.1460-9568.2005.04092.x: OpenAlex abstract look-up returned 429 (Crossref record already retrieved)

Pages consulted for content (not cited as records): profiles.wustl.edu Snyder 1992 profile (abstract: dipoles in or near somatosensory cortex); PMC6341058 (Vakorin 2019 abstract: S1 origin, propagation to SII, thalamus, motor cortex); is.tuebingen.mpg.de/publications/2798 (poster abstract of the Hinterberger EEG-fMRI study); PMC9410768 and PMC9069063 returned a browser check page (no content; abstracts read from Crossref records instead).
