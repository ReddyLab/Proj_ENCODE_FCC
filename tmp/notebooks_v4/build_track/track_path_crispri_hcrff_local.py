### set envrionment
import os, glob
from collections import defaultdict

###
FD_TRACKHUB     = "/mount/work/trackhub/proj_combeffect_encode_fcc"
FD_TRACK_SIGNAL = "track_crispri_hcrff/track_signal"
FD_TRACK_REGION = "track_crispri_hcrff/track_region"

###
DCT_TRACK_PATH = defaultdict(lambda: dict())

###
fdiry  = os.path.join(FD_TRACKHUB, FD_TRACK_SIGNAL)
fname  = "*bw"
fglob  = os.path.join(fdiry, fname)
fpaths = glob.glob(fglob)

dct = DCT_TRACK_PATH
idn = "signal"
for fpath in fpaths:
    fname = os.path.basename(fpath)
    lst   = fname.split(".")
    txt   = lst[5]
    dct[txt][idn] = fpath

###
fdiry  = os.path.join(FD_TRACKHUB, FD_TRACK_REGION)
fname  = "*bed"
fglob  = os.path.join(fdiry, fname)
fpaths = glob.glob(fglob)
    
dct = DCT_TRACK_PATH
idn = "region"
for fpath in fpaths:
    fname = os.path.basename(fpath)
    lst   = fname.split(".")
    txt   = lst[6]
    dct[txt][idn] = fpath
    
