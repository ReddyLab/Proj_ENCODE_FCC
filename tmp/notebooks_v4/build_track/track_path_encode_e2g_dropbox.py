### set envrionment
from collections import defaultdict

### init: tracks
DCT_TRACK_PATH = defaultdict(lambda: dict())

'''
### CRISPRi-E2G region
txt_track_index = "E2G"
txt_track_fpath = "https://www.dropbox.com/s/igommef7ox9s4fv/CRISPRi_e2g.K562.EPBenchmark.hg38.region.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### CRISPRi-E2G interact
txt_track_index = "E2G"
txt_track_fpath = "https://www.dropbox.com/s/mjqkcqsu4erg41n/CRISPRi_e2g.K562.EPBenchmark.hg38.region2TSS.bigInteract?dl=0"
txt_track_type  = "interact"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath
'''

'''
### ENCODE-E2G region
txt_track_index = "E2G"
txt_track_fpath = "https://www.dropbox.com/scl/fi/advxmsywvwsa9kuhnqdjp/ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region.bed.gz?rlkey=7191teqzse429awrvj8zui4i9&dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### ENCODE-E2G interact (Original)
txt_track_index = "E2G"
txt_track_fpath = "https://www.dropbox.com/scl/fi/ohhaqk1zh7fvszyejs38t/ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Original.bigInteract?rlkey=2v71ksnihroitnyu4oto1u299&dl=0"
txt_track_type  = "interact_original"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### ENCODE-E2G interact (Update)
txt_track_index = "E2G"
txt_track_fpath = "https://www.dropbox.com/scl/fi/4gkh3js5tsiqntits09v7/ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Updated.bigInteract?rlkey=zalp124hwu4qtv975kkbslb77&dl=0"
txt_track_type  = "interact_updated"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath
'''

############################################################

###
#fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
#fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region.active.bed.gz"
#fpath = os.path.join(fdiry, fname)
fpath = "https://www.dropbox.com/scl/fi/u985n8o39510m5440gomq/ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region.active.bed.gz?rlkey=w7szhaeb4tz74hqc33tq3nv42&dl=0"

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "region_active"
dct[txt][idn] = fpath

###
#fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
#fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region.total.bed.gz"
#fpath = os.path.join(fdiry, fname)
fpath = "https://www.dropbox.com/scl/fi/ybk64f2cca1ulbznc6a3v/ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region.total.bed.gz?rlkey=u1l3memxzu3d29x0v6ck2fuil&dl=0"

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "region_total"
dct[txt][idn] = fpath

############################################################

###
#fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
#fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Original.active.bedpe.gz"
#fpath = os.path.join(fdiry, fname)
fpath = "https://www.dropbox.com/scl/fi/8ymsacg2cj1fpqft2ojam/ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Original.active.bedpe.gz?rlkey=3lkid17qvqkj4zqdddunj3lmy&dl=0"

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "loop_tss_original_active"
dct[txt][idn] = fpath

###
#fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
#fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Original.total.bedpe.gz"
#fpath = os.path.join(fdiry, fname)
fpath = "https://www.dropbox.com/scl/fi/tqi8c27g96rd1k84nb5r3/ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Original.total.bedpe.gz?rlkey=gbtemcvzpc82x8h72a61gk8le&dl=0"

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "loop_tss_original_total"
dct[txt][idn] = fpath

###
#fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
#fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Updated.active.bedpe.gz"
#fpath = os.path.join(fdiry, fname)
fpath = "https://www.dropbox.com/scl/fi/1p9r3qvbyku9fvkw1qv04/ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Updated.active.bedpe.gz?rlkey=qrh20z56xmm3k164uz1xz580i&dl=0"

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "loop_tss_updated_active"
dct[txt][idn] = fpath

###
#fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
#fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Updated.total.bedpe.gz"
#fpath = os.path.join(fdiry, fname)
fpath = "https://www.dropbox.com/scl/fi/jqhh02rzta0j8m740n5iu/ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Updated.total.bedpe.gz?rlkey=c2mfp7khafou6b1nd1igfcu85&dl=0"

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "loop_tss_updated_total"
dct[txt][idn] = fpath

############################################################

###
#fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
#fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Original.active.bigInteract"
#fpath = os.path.join(fdiry, fname)
fpath = "https://www.dropbox.com/scl/fi/q0jqrrt0994sp808e1eyl/ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Original.active.bigInteract?rlkey=0lvflpp1sezx434zblsh4ptrc&dl=0"

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "interact_tss_original_active"
dct[txt][idn] = fpath

###
#fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
#fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Original.total.bigInteract"
#fpath = os.path.join(fdiry, fname)
fpath = "https://www.dropbox.com/scl/fi/fw79uyjxh4ykc1wvmv6oi/ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Original.total.bigInteract?rlkey=x42l21xh21dl3a5abt9n1e3hg&dl=0"

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "interact_tss_original_total"
dct[txt][idn] = fpath

###
#fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
#fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Updated.active.bigInteract"
#fpath = os.path.join(fdiry, fname)
fpath = "https://www.dropbox.com/scl/fi/55ya8nfwo4ewhhq7hqk7c/ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Updated.active.bigInteract?rlkey=3ckrgi2bmvnvxvgmohjmk5sbz&dl=0"

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "interact_tss_updated_active"
dct[txt][idn] = fpath

###
#fdiry = os.path.join(FD_TRACKHUB, FD_TRACK_FOLDER, FD_TRACK_REGION)
#fname = "ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Updated.total.bigInteract"
#fpath = os.path.join(fdiry, fname)
fpath = "https://www.dropbox.com/scl/fi/6ns8mzhecvqo1k8bucfjg/ENCODE_E2G.K562.EPCrisprBenchmark.hg38.region2TSS_Updated.total.bigInteract?rlkey=k3n2wcgzczadjrgyfkwzwq9yk&dl=0"

dct = DCT_TRACK_PATH
txt = "E2G"
idn = "interact_tss_updated_total"
dct[txt][idn] = fpath
