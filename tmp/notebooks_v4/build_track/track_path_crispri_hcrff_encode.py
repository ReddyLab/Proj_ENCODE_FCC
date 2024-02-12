"""
GATA1,HDAC6
FADS1,FADS2,FADS3,FEN1
CAPRIN1,CAT,LMO2
HBE1,HBG1,HBG2,HBS1L,MYB
MYC,PVT1
"""

### set environment
from collections import defaultdict

###
DCT_TRACK_PATH = defaultdict(lambda: dict())

### =====================================
### CRISPRi-HCRFF: GATA1
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "GATA1"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF669ISH/@@download/ENCFF669ISH.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF596QFD/@@download/ENCFF596QFD.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF413WYU/@@download/ENCFF413WYU.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF669VYC/@@download/ENCFF669VYC.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: HDAC6
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "HDAC6"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF514PCW/@@download/ENCFF514PCW.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF607OIW/@@download/ENCFF607OIW.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF632PQY/@@download/ENCFF632PQY.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF845MNY/@@download/ENCFF845MNY.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: FADS1
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "FADS1"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF090IXH/@@download/ENCFF090IXH.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF161WBO/@@download/ENCFF161WBO.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF786ZPA/@@download/ENCFF786ZPA.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF195DPB/@@download/ENCFF195DPB.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: FADS2
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "FADS2"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF923ZPB/@@download/ENCFF923ZPB.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF734CNO/@@download/ENCFF734CNO.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF149IDL/@@download/ENCFF149IDL.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF996MMO/@@download/ENCFF996MMO.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: FADS3
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "FADS3"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF186CEY/@@download/ENCFF186CEY.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF499QYP/@@download/ENCFF499QYP.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF227DUX/@@download/ENCFF227DUX.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF971KDY/@@download/ENCFF971KDY.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: FEN1
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "FEN1"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF666DNQ/@@download/ENCFF666DNQ.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF571LUW/@@download/ENCFF571LUW.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF151MNC/@@download/ENCFF151MNC.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF489EXK/@@download/ENCFF489EXK.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: CAPRIN1
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "CAPRIN1"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF444UXP/@@download/ENCFF444UXP.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF994KKV/@@download/ENCFF994KKV.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF863AVQ/@@download/ENCFF863AVQ.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF862YSB/@@download/ENCFF862YSB.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: CAT
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "CAT"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF965PMF/@@download/ENCFF965PMF.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF918VCM/@@download/ENCFF918VCM.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF619FXH/@@download/ENCFF619FXH.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF412KTS/@@download/ENCFF412KTS.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: LMO2
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "LMO2"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF114EMW/@@download/ENCFF114EMW.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF756AUB/@@download/ENCFF756AUB.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF469FXP/@@download/ENCFF469FXP.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF042QJU/@@download/ENCFF042QJU.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: HBG1
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "HBG1"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF422LBX/@@download/ENCFF422LBX.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF270GAZ/@@download/ENCFF270GAZ.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF811PPJ/@@download/ENCFF811PPJ.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF913IUB/@@download/ENCFF913IUB.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: HBG2
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "HBG2"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF110XZR/@@download/ENCFF110XZR.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF052MDO/@@download/ENCFF052MDO.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF910PDZ/@@download/ENCFF910PDZ.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF003BEC/@@download/ENCFF003BEC.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: HBE1
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "HBE1"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF283BAT/@@download/ENCFF283BAT.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF375NHR/@@download/ENCFF375NHR.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF845YHV/@@download/ENCFF845YHV.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF021TZQ/@@download/ENCFF021TZQ.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: HBS1L
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "HBS1L"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF130XRV/@@download/ENCFF130XRV.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF279WUO/@@download/ENCFF279WUO.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF337VVS/@@download/ENCFF337VVS.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF302POA/@@download/ENCFF302POA.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: MYB
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "MYB"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF706HXQ/@@download/ENCFF706HXQ.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF825RTL/@@download/ENCFF825RTL.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF091IOP/@@download/ENCFF091IOP.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF299NVY/@@download/ENCFF299NVY.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: MYC
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "MYC"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF309PDY/@@download/ENCFF309PDY.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF336DNM/@@download/ENCFF336DNM.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF240IPT/@@download/ENCFF240IPT.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF456WGW/@@download/ENCFF456WGW.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### CRISPRi-HCRFF: PVT1
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "PVT1"

idn_track = "signal_R1"
txt_track = "https://www.encodeproject.org/files/ENCFF298GWM/@@download/ENCFF298GWM.bigWig"
dct_track[idn_track] = txt_track

idn_track = "signal_R2"
txt_track = "https://www.encodeproject.org/files/ENCFF191XOT/@@download/ENCFF191XOT.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF005DTR/@@download/ENCFF005DTR.bed.gz"
dct_track[idn_track] = txt_track

idn_track = "interact"
txt_track = "https://www.encodeproject.org/files/ENCFF853CKU/@@download/ENCFF853CKU.bigInteract"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track