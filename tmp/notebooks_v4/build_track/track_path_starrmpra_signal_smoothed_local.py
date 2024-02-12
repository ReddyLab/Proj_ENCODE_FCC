### set environment
import os
from collections import defaultdict

###
FD_TRACKHUB    = "/mount/work/trackhub/proj_combeffect_encode_fcc"
FD_TRACK       = "track_starrmpra/track_signal_smooth_w1000_s1"
#DCT_TRACK_PATH = dict()
DCT_TRACK_PATH = defaultdict(lambda: dict())

### ASTARR
ID_TRACK = "ASTARR"
FN_TRACK = "STARRseq_ATAC.K562.TR.hg38.pLog2FC.mean.SUBSET.unstranded.bw"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)

DCT_TRACK_PATH[ID_TRACK]["signal"] = FP_TRACK

### WSTARR
ID_TRACK  = "WSTARR"
FN_TRACK  = "STARRseq_WHG.K562.TR.hg38.pLog2FC.mean.SUBSET.unstranded.bw"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)

DCT_TRACK_PATH[ID_TRACK]["signal"] = FP_TRACK

### TMPRA
ID_TRACK  = "TMPRA"
FN_TRACK  = "MPRA_Tiling.K562.Tewhey.hg38.Log2FC_norm.mean.MERGE.stranded_pos.bw"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)

DCT_TRACK_PATH[ID_TRACK]["signal"] = FP_TRACK

### LMPRA
ID_TRACK  = "LMPRA"
FN_TRACK  = "MPRA_Lenti.K562.Nadav.hg38.ZScore.mean.SUBSET.unstranded.bw"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)

DCT_TRACK_PATH[ID_TRACK]["signal"] = FP_TRACK

### ATAC
ID_TRACK  = "ATAC"
FN_TRACK  = "STARRseq_ATAC.K562.TR.hg38.Input.mean.SUBSET.unstranded.bw"
FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)

DCT_TRACK_PATH[ID_TRACK]["signal"] = FP_TRACK
