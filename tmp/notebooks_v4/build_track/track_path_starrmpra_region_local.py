### set environment
import os
from collections import defaultdict

###
FD_TRACKHUB    = "/mount/work/trackhub"
FD_TRACK       = "proj_combeffect_encode_fcc/track_starrmpra/track_region"
DCT_TRACK_PATH = defaultdict(lambda: dict())

### ASTARR
ID_TRACK = "ASTARR_AB"
FN_TRACK = "enhancer_zscore_junke.peak.ASTARR_AB.bed.gz"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
DCT_TRACK_PATH[ID_TRACK]["region"] = FP_TRACK

ID_TRACK = "ASTARR_A"
FN_TRACK = "enhancer_zscore_junke.peak.ASTARR_A.bed.gz"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
DCT_TRACK_PATH[ID_TRACK]["region"] = FP_TRACK

ID_TRACK = "ASTARR_R"
FN_TRACK = "enhancer_zscore_junke.peak.ASTARR_R.bed.gz"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
DCT_TRACK_PATH[ID_TRACK]["region"] = FP_TRACK

### WSTARR
ID_TRACK = "WSTARR_AB"
FN_TRACK = "enhancer_zscore_junke.peak.WSTARR_AB.bed.gz"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
DCT_TRACK_PATH[ID_TRACK]["region"] = FP_TRACK

ID_TRACK = "WSTARR_A"
FN_TRACK = "enhancer_zscore_junke.peak.WSTARR_A.bed.gz"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
DCT_TRACK_PATH[ID_TRACK]["region"] = FP_TRACK

ID_TRACK = "WSTARR_R"
FN_TRACK = "enhancer_zscore_junke.peak.WSTARR_R.bed.gz"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
DCT_TRACK_PATH[ID_TRACK]["region"] = FP_TRACK

### TMPRA
ID_TRACK  = "TMPRA_A"
FN_TRACK  = "enhancer_zscore_junke.peak.TMPRA_A.bed.gz"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
DCT_TRACK_PATH[ID_TRACK]["region"] = FP_TRACK

ID_TRACK  = "TMPRA_R"
FN_TRACK  = "enhancer_zscore_junke.peak.TMPRA_R.bed.gz"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
DCT_TRACK_PATH[ID_TRACK]["region"] = FP_TRACK

### LMPRA
ID_TRACK  = "LMPRA_AB"
FN_TRACK  = "enhancer_zscore_junke.peak.LMPRA_AB.bed.gz"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
DCT_TRACK_PATH[ID_TRACK]["region"] = FP_TRACK

ID_TRACK  = "LMPRA_A"
FN_TRACK  = "enhancer_zscore_junke.peak.LMPRA_A.bed.gz"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
DCT_TRACK_PATH[ID_TRACK]["region"] = FP_TRACK

ID_TRACK  = "LMPRA_R"
FN_TRACK  = "enhancer_zscore_junke.peak.LMPRA_R.bed.gz"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
DCT_TRACK_PATH[ID_TRACK]["region"] = FP_TRACK

### ATAC
ID_TRACK  = "ATAC"
FN_TRACK  = "KS91_K562_hg38_ASTARRseq_Input.all_reps.masked.union_narrowPeak.q5.bed.gz"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
DCT_TRACK_PATH[ID_TRACK]["region"] = FP_TRACK
