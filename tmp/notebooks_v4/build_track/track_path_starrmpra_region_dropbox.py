### set environment
from collections import defaultdict

### init: tracks
DCT_TRACK_PATH = defaultdict(lambda: dict())

### ASTARR
txt_track_index = "ASTARR_AB"
txt_track_fpath = "https://www.dropbox.com/s/7145dpjjd4dj1rj/enhancer_zscore_junke.peak.ASTARR_AB.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

txt_track_index = "ASTARR_A"
txt_track_fpath = "https://www.dropbox.com/s/4fmz5jgz2i2owwv/enhancer_zscore_junke.peak.ASTARR_A.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

txt_track_index = "ASTARR_R"
txt_track_fpath = "https://www.dropbox.com/s/0a0c7cpj2whetze/enhancer_zscore_junke.peak.ASTARR_R.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### WSTARR
txt_track_index = "WSTARR_AB"
txt_track_fpath = "https://www.dropbox.com/s/6wxo2x1san174w0/enhancer_zscore_junke.peak.WSTARR_AB.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

txt_track_index = "WSTARR_A" 
txt_track_fpath = "https://www.dropbox.com/s/w5t0lx7b5ubv6na/enhancer_zscore_junke.peak.WSTARR_A.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

txt_track_index = "WSTARR_R"
txt_track_fpath = "https://www.dropbox.com/s/kgw9fpplvp6h0wp/enhancer_zscore_junke.peak.WSTARR_R.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### TMPRA
txt_track_index = "TMPRA_A"
txt_track_fpath = "https://www.dropbox.com/s/y41bu4p4vfnhgq7/enhancer_zscore_junke.peak.TMPRA_A.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

txt_track_index = "TMPRA_R"
txt_track_fpath = "https://www.dropbox.com/s/bxbx4gj9phl3tya/enhancer_zscore_junke.peak.TMPRA_R.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### LMPRA
txt_track_index = "LMPRA_A"
txt_track_fpath = "https://www.dropbox.com/s/n57q1c02i9cwn24/enhancer_zscore_junke.peak.LMPRA_A.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

txt_track_index = "LMPRA_AB"
txt_track_fpath = "https://www.dropbox.com/s/dekif2sd0yrefkm/enhancer_zscore_junke.peak.LMPRA_AB.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

txt_track_index = "LMPRA_R"
txt_track_fpath = "https://www.dropbox.com/s/grtd286r6gro8vu/enhancer_zscore_junke.peak.LMPRA_R.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath

### ATAC
txt_track_index = "ATAC"
txt_track_fpath = "https://www.dropbox.com/s/mol02qgqrq5uusx/KS91_K562_hg38_ASTARRseq_Input.all_reps.masked.union_narrowPeak.q5.bed.gz?dl=0"
txt_track_type  = "region"

DCT_TRACK_PATH[txt_track_index][txt_track_type] = txt_track_fpath
