### set environment
import os

DCT_TRACK   = dict()
FD_TRACKHUB = "/mount/work/trackhub"
FD_TRACK    = "proj_combeffect_encode_fcc/track_starrmpra/track_signal_original"

### ASTARR
ID_LABEL  = "ASTARR (pLog2FC; Original)"
ID_TRACK  = "track_ASTARR"
FN_TRACK  = "STARRseq_ATAC.K562.TR.hg38.pLog2FC.mean.SUBSET.unstranded.bw"
TXT_COLOR = "#ff726e"
track = {
    "name":     ID_LABEL,
    "path":     os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK),
    "format":   "bigwig",
    "type":     "wig",
    "color":    TXT_COLOR,
    "altColor": TXT_COLOR,
}
DCT_TRACK[ID_TRACK] = track

### WSTARR
ID_LABEL  = "WSTARR (pLog2FC; Original)"
ID_TRACK  = "track_WSTARR"
FN_TRACK  = "STARRseq_WHG.K562.TR.hg38.pLog2FC.mean.SUBSET.unstranded.bw"
TXT_COLOR = "#8da0cb"
track = {
    "name":     ID_LABEL,
    "path":     os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK),
    "format":   "bigwig",
    "type":     "wig",
    "color":    TXT_COLOR,
    "altColor": TXT_COLOR,
}
DCT_TRACK[ID_TRACK] = track

### TMPRA
ID_LABEL  = "Tiling MPRA (Log2FC; Original)"
ID_TRACK  = "track_TMPRA"
FN_TRACK  = "MPRA_Tiling.K562.Tewhey.hg38.Log2FC_norm.mean.MERGE.stranded_pos.bw"
TXT_COLOR = "#66c2a5"
track = {
    "name":     ID_LABEL,
    "path":     os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK),
    "format":   "bigwig",
    "type":     "wig",
    "color":    TXT_COLOR,
    "altColor": TXT_COLOR,
}
DCT_TRACK[ID_TRACK] = track

### LMPRA
ID_LABEL  = "LentiMPRA (ZScore; Original)"
ID_TRACK  = "track_LMPRA"
FN_TRACK  = "MPRA_Lenti.K562.Nadav.hg38.ZScore.mean.SUBSET.unstranded.bw"
TXT_COLOR = "#ff8802"
track = {
    "name":     ID_LABEL,
    "path":     os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK),
    "format":   "bigwig",
    "type":     "wig",
    "color":    TXT_COLOR,
    "altColor": TXT_COLOR,
}
DCT_TRACK[ID_TRACK] = track

### ATAC
ID_LABEL  = "ATAC (CPM)"
ID_TRACK  = "track_ATAC"
FN_TRACK  = "STARRseq_ATAC.K562.TR.hg38.Input.mean.SUBSET.unstranded.bw"

track = {
    "name":     ID_LABEL,
    "path":     os.path.join(FD_TRACKHUB, FD_TRACK, FN_TRACK),
    "format":   "bigwig",
    "type":     "wig",
}
DCT_TRACK[ID_TRACK] = track