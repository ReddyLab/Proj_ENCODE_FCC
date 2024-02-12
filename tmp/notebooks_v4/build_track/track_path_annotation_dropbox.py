### set envrionment
from collections import defaultdict

### init: tracks
DCT_TRACK_PATH = defaultdict(lambda: dict())

### =====================================
### Annotation: TSS_POL2
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
txt_track_index = "TSS_POL2"
txt_track_fpath = "https://www.dropbox.com/s/k4tyfmukig60y43/K562.TSS.selected_by_highest_Pol2_signal.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### =====================================
### Annotation: TSS_POL2_RNAseq
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
txt_track_index = "TSS_POL2_RNAseq"
txt_track_fpath = "https://www.dropbox.com/scl/fi/tk1m9d2myidh5v6d88e5b/K562.TSS.selected_by_highest_Pol2_signal.filtered_by_RNAseq_TPM.bed.gz?rlkey=yffcq7cbeh2lelzmf3oiwrdoe&dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath


### =====================================
### Annotation: cCREs
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
txt_track_index = "ccres"
txt_track_fpath = "https://www.dropbox.com/s/72x40xz89tgvqil/K562.ENCSR913HQX.ENCFF286VQG.ccres.cat2name.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### =====================================
### Annotation: cCREs (PLS, pELS, dELS)
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
txt_track_index = "ccres_PLS_ELS"
txt_track_fpath = "https://www.dropbox.com/scl/fi/vn0wgxxj6rwnipgi6xas7/K562.ENCSR913HQX.ENCFF286VQG.ccres.cat2name.PLS_ELS.bed.gz?rlkey=aih8f72ntmk3jtyzaw02rn6rv&dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### =====================================
### Annotation: ChromHMM
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"K562.ENCSR365YNI.ENCFF106BGJ.ChromHMM.bed.gz"

txt_track_index = "chromhmm"
txt_track_fpath = "https://www.dropbox.com/s/5yf1p1hs0g3dwyb/K562.ENCSR365YNI.ENCFF106BGJ.ChromHMM.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath
