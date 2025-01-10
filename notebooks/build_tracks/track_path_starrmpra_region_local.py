### set environment
import os
from collections import defaultdict

### init: tracks and 
DCT_TRACK_PATH = defaultdict(lambda: dict())

### init: file directory
FD_TRACKHUB    = "/mount/work/trackhub/proj_encode_fcc"
FD_TRACK       = "track_starrmpra/track_region"

### ===================================
### Track: ATAC (ASTARR Input)
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

dct = {
    "ASTARR_Input_region_overlap": "STARRseq_ATAC.K562.TR.hg38.input.rep_all.max_overlaps.q5.bed.gz",
    "ASTARR_Input_region_union":   "STARRseq_ATAC.K562.TR.hg38.input.rep_all.union.q5.bed.gz"
}

for ID_TRACK, FN_TRACK in dct.items():
    FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
    DCT_TRACK_PATH[ID_TRACK]["path"] = FP_TRACK
    DCT_TRACK_PATH[ID_TRACK]["type"] = "region"
    
dct = {
    "ASTARR_Input_rep1_region": "STARRseq_ATAC.K562.TR.hg38.input.rep1.narrowpeak.bed.gz",
    "ASTARR_Input_rep2_region": "STARRseq_ATAC.K562.TR.hg38.input.rep2.narrowpeak.bed.gz",
    "ASTARR_Input_rep3_region": "STARRseq_ATAC.K562.TR.hg38.input.rep3.narrowpeak.bed.gz",
    "ASTARR_Input_rep4_region": "STARRseq_ATAC.K562.TR.hg38.input.rep4.narrowpeak.bed.gz",
    "ASTARR_Input_rep5_region": "STARRseq_ATAC.K562.TR.hg38.input.rep5.narrowpeak.bed.gz",
    "ASTARR_Input_rep6_region": "STARRseq_ATAC.K562.TR.hg38.input.rep6.narrowpeak.bed.gz"
}

for ID_TRACK, FN_TRACK in dct.items():
    FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
    DCT_TRACK_PATH[ID_TRACK]["path"] = FP_TRACK
    DCT_TRACK_PATH[ID_TRACK]["type"] = "region"


dct = {
    "ASTARR_Input_rep1_summit": "STARRseq_ATAC.K562.TR.hg38.input.rep1.summit.bed.gz",
    "ASTARR_Input_rep2_summit": "STARRseq_ATAC.K562.TR.hg38.input.rep2.summit.bed.gz",
    "ASTARR_Input_rep3_summit": "STARRseq_ATAC.K562.TR.hg38.input.rep3.summit.bed.gz",
    "ASTARR_Input_rep4_summit": "STARRseq_ATAC.K562.TR.hg38.input.rep4.summit.bed.gz",
    "ASTARR_Input_rep5_summit": "STARRseq_ATAC.K562.TR.hg38.input.rep5.summit.bed.gz",
    "ASTARR_Input_rep6_summit": "STARRseq_ATAC.K562.TR.hg38.input.rep6.summit.bed.gz"
}

for ID_TRACK, FN_TRACK in dct.items():
    FP_TRACK = os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK)
    DCT_TRACK_PATH[ID_TRACK]["path"] = FP_TRACK
    DCT_TRACK_PATH[ID_TRACK]["type"] = "region"