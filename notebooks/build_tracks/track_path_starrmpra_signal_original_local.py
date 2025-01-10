### set environment
import os
from collections import defaultdict

### init: tracks
DCT_TRACK_PATH = defaultdict(lambda: dict())

### init: file directory
#FD_TRACKHUB    = "/data/reddylab/Kuei/work/trackhub/proj_encode_fcc"
FD_TRACKHUB    = "/mount/work/trackhub/proj_encode_fcc"
FD_TRACK       = "track_starrmpra/track_signal_original"

### ===================================
### Track: ATAC (ASTARR Input)
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

dct = {
    "ASTARR_Input_rep1_signal": "STARRseq_ATAC.K562.TR.hg38.Input_rep1.cpm.WHG.unstranded.bw",
    "ASTARR_Input_rep2_signal": "STARRseq_ATAC.K562.TR.hg38.Input_rep2.cpm.WHG.unstranded.bw",
    "ASTARR_Input_rep3_signal": "STARRseq_ATAC.K562.TR.hg38.Input_rep3.cpm.WHG.unstranded.bw",
    "ASTARR_Input_rep4_signal": "STARRseq_ATAC.K562.TR.hg38.Input_rep4.cpm.WHG.unstranded.bw",
    "ASTARR_Input_rep5_signal": "STARRseq_ATAC.K562.TR.hg38.Input_rep5.cpm.WHG.unstranded.bw",
    "ASTARR_Input_rep6_signal": "STARRseq_ATAC.K562.TR.hg38.Input_rep6.cpm.WHG.unstranded.bw"
}

for ID_TRACK, FN_TRACK in dct.items():
    FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
    DCT_TRACK_PATH[ID_TRACK]["path"] = FP_TRACK
    DCT_TRACK_PATH[ID_TRACK]["type"] = "signal"
