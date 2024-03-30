### set environment
import os
from collections import defaultdict

DCT_TRACK_PATH = defaultdict(lambda: dict())

### ASTARR
ID_TRACK = "ASTARR_KS91_INP1"
FD_TRACK = "/mount/work/proj_combeffect_encode_fcc/data/processed/KS91_K562_hg38_ASTARRseq_210401/fragments"
FN_TRACK = "KS91_K562_hg38_ASTARRseq_Input_rep1.masked.exclude_dups.cpm.bw"
FP_TRACK = os.path.join(FD_TRACK, FD_TRACK, FN_TRACK)
DCT_TRACK_PATH[ID_TRACK]["signal"] = FP_TRACK

ID_TRACK = "ASTARR_KS91_INP2"
FD_TRACK = "/mount/work/proj_combeffect_encode_fcc/data/processed/KS91_K562_hg38_ASTARRseq_210401/fragments"
FN_TRACK = "KS91_K562_hg38_ASTARRseq_Input_rep2.masked.exclude_dups.cpm.bw"
FP_TRACK = os.path.join(FD_TRACK, FD_TRACK, FN_TRACK)
DCT_TRACK_PATH[ID_TRACK]["signal"] = FP_TRACK