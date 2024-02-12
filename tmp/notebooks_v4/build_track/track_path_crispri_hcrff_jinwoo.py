"""
GATA1,HDAC6
FADS1,FADS2,FADS3,FEN1
CAPRIN1,CAT,LMO2
HBE1,HBG1,HBG2,HBS1L,MYB
"""

### set environment
from collections import defaultdict

###
DCT_TRACK_PATH = defaultdict(lambda: dict())

###
TXT_GENES = [
    "GATA1", "HDAC6",
    "FADS1", "FADS2", "FADS3", "FEN1",
    "CAPRIN1", "CAT", "LMO2",
    "HBE1", "HBG1", "HBG2", "HBS1L", "MYB"
]

### =====================================
### CRISPRi-HCRFF: GATA1
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#dct_track = dict()
#txt_gene  = "GATA1"

#idn_track = "signal"
#url_track = "https://data.cyverse.org/dav-anon/iplant/home/ohjinwoo94/GATA1_HCRFF_rAVG.log2FC_2.bw"
#dct_track[idn_track] = url_track

#idn_track = "region"
#url_track = "https://data.cyverse.org/dav-anon/iplant/home/ohjinwoo94/GATA1_HCRFF_peaks.bb"
#dct_track[idn_track] = url_track

#DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

for txt_gene in TXT_GENES:
    ###
    dct_track = dict()
    
    idn_track =  "signal"
    txt_track = f"https://data.cyverse.org/dav-anon/iplant/home/ohjinwoo94/{txt_gene}_HCRFF_rAVG.log2FC_2.bw"
    dct_track[idn_track] = txt_track
    
    idn_track =  "region"
    txt_track = f"https://data.cyverse.org/dav-anon/iplant/home/ohjinwoo94/{txt_gene}_HCRFF_peaks.bb"
    dct_track[idn_track] = txt_track

    DCT_TRACK_PATH[txt_gene] = dct_track
