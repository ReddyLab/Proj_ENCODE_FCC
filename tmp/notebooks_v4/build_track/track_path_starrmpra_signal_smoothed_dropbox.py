### set envrionment
from collections import defaultdict

### init: tracks
DCT_TRACK_PATH = defaultdict(lambda: dict())

### ASTARR
txt_track_index = "ASTARR"
txt_track_fpath = "https://www.dropbox.com/s/gypyez8qwy60lcs/STARRseq_ATAC.K562.TR.hg38.pLog2FC.mean.SUBSET.unstranded.bw?dl=0"
txt_track_type  = "signal"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### WSTARR
txt_track_index = "WSTARR"
txt_track_fpath = "https://www.dropbox.com/s/8wzefevm0vmoy4p/STARRseq_WHG.K562.TR.hg38.pLog2FC.mean.SUBSET.unstranded.bw?dl=0"
txt_track_type  = "signal"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### TMPRA
txt_track_index = "TMPRA"
txt_track_fpath = "https://www.dropbox.com/s/92yk3vo2j77v6tc/MPRA_Tiling.K562.Tewhey.hg38.Log2FC_norm.mean.MERGE.stranded_pos.bw?dl=0"
txt_track_type  = "signal"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### LMPRA
txt_track_index = "LMPRA"
txt_track_fpath = "https://www.dropbox.com/s/7u9i0q98gxl5z71/MPRA_Lenti.K562.Nadav.hg38.ZScore.mean.SUBSET.unstranded.bw?dl=0"
txt_track_type  = "signal"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath
