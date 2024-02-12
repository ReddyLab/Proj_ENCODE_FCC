### set envrionment
from collections import defaultdict

### init: tracks
DCT_TRACK_PATH = defaultdict(lambda: dict())

#txt_track_index = ...
#txt_track_fpath = ...
#txt_track_type  = "signal"

### ASTARR
txt_track_index = "ASTARR"
txt_track_fpath = "https://www.dropbox.com/s/cf3twad05jffz9d/STARRseq_ATAC.K562.TR.hg38.pLog2FC.mean.SUBSET.unstranded.bw?dl=0"
txt_track_type  = "signal"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### WSTARR
txt_track_index = "WSTARR"
txt_track_fpath = "https://www.dropbox.com/s/xx5m06d8ura06m7/STARRseq_WHG.K562.TR.hg38.pLog2FC.mean.SUBSET.unstranded.bw?dl=0"
txt_track_type  = "signal"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### TMPRA
txt_track_index = "TMPRA"
txt_track_fpath = "https://www.dropbox.com/s/283ddjnmdc5jp2b/MPRA_Tiling.K562.Tewhey.hg38.Log2FC_norm.mean.MERGE.stranded_pos.bw?dl=0"
txt_track_type  = "signal"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### LMPRA
txt_track_index = "LMPRA"
txt_track_fpath = "https://www.dropbox.com/s/zxu7p49kmroj5q7/MPRA_Lenti.K562.Nadav.hg38.ZScore.mean.SUBSET.unstranded.bw?dl=0"
txt_track_type  = "signal"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### ATAC
txt_track_index = "ATAC"
txt_track_fpath = "https://www.dropbox.com/s/kd5wgdc5dbsaox0/STARRseq_ATAC.K562.TR.hg38.Input.mean.SUBSET.unstranded.bw?dl=0"
txt_track_type  = "signal"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

