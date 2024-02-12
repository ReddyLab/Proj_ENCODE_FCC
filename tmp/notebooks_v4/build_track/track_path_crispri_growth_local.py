### set envrionment
import os
from collections import defaultdict

###
FD_TRACKHUB     = "/mount/work/trackhub/proj_combeffect_encode_fcc"
FD_TRACK_SIGNAL = "track_crispri_growth/track_signal"
FD_TRACK_REGION = "track_crispri_growth/track_region"

###
DCT_TRACK_PATH = defaultdict(lambda: dict())

###
fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_SIGNAL)
fname = "CRISPRi_growth.K562.Gersbach.hg38.ZScore.unstranded.bw"
fpath = os.path.join(fdiry, fname)

dct = DCT_TRACK_PATH
idn = "signal"
dct["Growth"][idn] = fpath

###
fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_REGION)
fname = "CRISPRi_growth.K562.Gersbach.hg38.dhs.region_call.signif_guides.bed.gz"
fpath = os.path.join(fdiry, fname)

dct = DCT_TRACK_PATH
idn = "region"
dct["Growth"][idn] = fpath

    
