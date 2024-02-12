### set envrionment
import os
from collections import defaultdict

###
FD_TRACKHUB     = "/mount/work/trackhub/proj_combeffect_encode_fcc"
FD_TRACK_FOLDER = "track_encode_e2g"
FD_TRACK_REGION = "track_region"

###
DCT_TRACK_PATH = defaultdict(lambda: dict())

############################################################

###
fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region.active.bed.gz"
fpath = os.path.join(fdiry, fname)

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "region_active"
dct[txt][idn] = fpath

###
fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region.total.bed.gz"
fpath = os.path.join(fdiry, fname)

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "region_total"
dct[txt][idn] = fpath

############################################################

###
fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Original.active.bedpe.gz"
fpath = os.path.join(fdiry, fname)

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "loop_tss_original_active"
dct[txt][idn] = fpath

###
fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Original.total.bedpe.gz"
fpath = os.path.join(fdiry, fname)

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "loop_tss_original_total"
dct[txt][idn] = fpath

###
fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Updated.active.bedpe.gz"
fpath = os.path.join(fdiry, fname)

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "loop_tss_updated_active"
dct[txt][idn] = fpath

###
fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Updated.total.bedpe.gz"
fpath = os.path.join(fdiry, fname)

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "loop_tss_updated_total"
dct[txt][idn] = fpath

############################################################

###
fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Original.active.bigInteract"
fpath = os.path.join(fdiry, fname)

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "interact_tss_original_active"
dct[txt][idn] = fpath

###
fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Original.total.bigInteract"
fpath = os.path.join(fdiry, fname)

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "interact_tss_original_total"
dct[txt][idn] = fpath

###
fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Updated.active.bigInteract"
fpath = os.path.join(fdiry, fname)

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "interact_tss_updated_active"
dct[txt][idn] = fpath

###
fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Updated.total.bigInteract"
fpath = os.path.join(fdiry, fname)

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "interact_tss_updated_total"
dct[txt][idn] = fpath

