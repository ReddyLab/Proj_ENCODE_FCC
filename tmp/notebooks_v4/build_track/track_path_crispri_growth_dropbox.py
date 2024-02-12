### set envrionment
from collections import defaultdict

### init: tracks
DCT_TRACK_PATH = defaultdict(lambda: dict())

### CRISPRi-Growth signals
txt_track_index = "Growth"
txt_track_fpath = "https://www.dropbox.com/s/r3zbytf9zxrffbm/CRISPRi_growth.K562.Gersbach.hg38.ZScore.unstranded.bw?dl=0"
txt_track_type  = "signal"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### CRISPRi-Growth regions
txt_track_index = "Growth"
txt_track_fpath = "https://www.dropbox.com/s/55b5wcyfzf2agqa/CRISPRi_growth.K562.Gersbach.hg38.dhs.region_call.signif_guides.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath
