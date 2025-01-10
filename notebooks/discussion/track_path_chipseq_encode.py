### set environment
from collections import defaultdict

###
DCT_TRACK_PATH = defaultdict(lambda: dict())

### =====================================
### K562 ATAC
### Lab: Michael Snyder, Stanford
### Exp: https://www.encodeproject.org/experiments/ENCSR868FGK/
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "ATAC"

idn_track = "signal"
txt_track = "https://www.encodeproject.org/files/ENCFF357GNC/@@download/ENCFF357GNC.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF086JCJ/@@download/ENCFF086JCJ.bigBed"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### ChIP-seq: POLR2A
### https://www.encodeproject.org/experiments/ENCSR388QZF/
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "POLR2A"

idn_track = "signal"
txt_track = "https://www.encodeproject.org/files/ENCFF914WIS/@@download/ENCFF914WIS.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF215CWW/@@download/ENCFF215CWW.bigBed"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### ChIP-seq: CTCF
### https://www.encodeproject.org/experiments/ENCSR000EGM/
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "CTCF"

idn_track = "signal"
txt_track = "https://www.encodeproject.org/files/ENCFF336UPT/@@download/ENCFF336UPT.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF660GHM/@@download/ENCFF660GHM.bed.gz"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### ChIP-seq: SMC3
### https://www.encodeproject.org/experiments/ENCSR000EGW/
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "SMC3"

idn_track = "signal"
txt_track = "https://www.encodeproject.org/files/ENCFF067OLL/@@download/ENCFF067OLL.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF582XIX/@@download/ENCFF582XIX.bigBed"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### ChIP-seq: GATA1
### https://www.encodeproject.org/experiments/ENCSR000EFT/
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "GATA1"

idn_track = "signal"
txt_track = "https://www.encodeproject.org/files/ENCFF331URE/@@download/ENCFF331URE.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF094CMK/@@download/ENCFF094CMK.bigBed"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### ChIP-seq: MYC
### https://www.encodeproject.org/experiments/ENCSR000EFT/
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "MYC"

idn_track = "signal"
txt_track = "https://www.encodeproject.org/files/ENCFF670SRV/@@download/ENCFF670SRV.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF295NDX/@@download/ENCFF295NDX.bigBed"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### ChIP-seq: EP300
### https://www.encodeproject.org/experiments/ENCSR000EFT/
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "EP300"

idn_track = "signal"
txt_track = "https://www.encodeproject.org/files/ENCFF363QJI/@@download/ENCFF363QJI.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF860OBO/@@download/ENCFF860OBO.bigBed"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### ChIP-seq: YY1
### https://www.encodeproject.org/experiments/ENCSR000BMH/
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "YY1"

idn_track = "signal"
txt_track = "https://www.encodeproject.org/files/ENCFF230VJT/@@download/ENCFF230VJT.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF052UCG/@@download/ENCFF052UCG.bigBed"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### ChIP-seq: H3K27ac
### https://www.encodeproject.org/experiments/ENCSR000AKP/
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "H3K27ac"

idn_track = "signal"
txt_track = "https://www.encodeproject.org/files/ENCFF469JMR/@@download/ENCFF469JMR.bigWig"
dct_track[idn_track] = txt_track

idn_track = "region"
txt_track = "https://www.encodeproject.org/files/ENCFF082RJM/@@download/ENCFF082RJM.bigBed"
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

