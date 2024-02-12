### set envrionment
import os
from collections import defaultdict

###
FD_TRACKHUB = "/mount/work/trackhub/proj_combeffect_encode_fcc"
FD_TRACK    = "track_annotation"

###
DCT_TRACK_PATH = defaultdict(lambda: dict())

### =====================================
### Annotation: TSS_POL2
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "TSS_POL2"

fdiry = os.path.join(FD_TRACKHUB, FD_TRACK)
fname = "K562.TSS.selected_by_highest_Pol2_signal.bed.gz"
fpath = os.path.join(fdiry, fname)

idn_track = "region"
txt_track = fpath
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### Annotation: TSS_POL2_RNAseq
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "TSS_POL2_RNAseq"

fdiry = os.path.join(FD_TRACKHUB, FD_TRACK)
fname = "K562.TSS.selected_by_highest_Pol2_signal.filtered_by_RNAseq_TPM.bed.gz"
fpath = os.path.join(fdiry, fname)

idn_track = "region"
txt_track = fpath
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### Annotation: cCREs
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "ccres"

fdiry = os.path.join(FD_TRACKHUB, FD_TRACK)
fname = "K562.ENCSR913HQX.ENCFF286VQG.ccres.cat2name.bed.gz"
fpath = os.path.join(fdiry, fname)

idn_track = "region"
txt_track = fpath
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track

### =====================================
### Annotation: cCREs
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "ccres_PLS_ELS"

fdiry = os.path.join(FD_TRACKHUB, FD_TRACK)
fname = "K562.ENCSR913HQX.ENCFF286VQG.ccres.cat2name.PLS_ELS.bed.gz"
fpath = os.path.join(fdiry, fname)

idn_track = "region"
txt_track = fpath
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track


### =====================================
### Annotation: ChromHMM
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track = dict()
txt_gene  = "chromhmm"

fdiry = os.path.join(FD_TRACKHUB, FD_TRACK)
fname = "K562.ENCSR365YNI.ENCFF106BGJ.ChromHMM.bed.gz"
fpath = os.path.join(fdiry, fname)

idn_track = "region"
txt_track = fpath
dct_track[idn_track] = txt_track

DCT_TRACK_PATH[txt_gene] = dct_track