### set environment
import os
from collections import defaultdict

###
#DCT_TRACK_PATH  = dict()
DCT_TRACK_PATH = defaultdict(lambda: dict())

### ASTARR (JIN WOO)
ID_TRACK  = "ASTARR"
URL_TRACK = "https://data.cyverse.org/dav-anon/iplant/home/ohjinwoo94/KS91_K562_bs5_log2ratio.bw"
DCT_TRACK_PATH[ID_TRACK]["signal"] = URL_TRACK

### TMPRA (GATA/MYC; JIN WOO)
ID_TRACK  = "TMPRA_OL43"
URL_TRACK = "https://data.cyverse.org/dav-anon/iplant/home/ohjinwoo94/GATA-MYC_Tile_K562_K562_20210130.hg38.Z_bp.bw"
DCT_TRACK_PATH[ID_TRACK]["signal"] = URL_TRACK

### TMPRA (FEN/FADS; JIN WOO)
ID_TRACK  = "TMPRA_OL13"
URL_TRACK = "https://data.cyverse.org/dav-anon/iplant/home/ohjinwoo94/FEN1_FADS123_MPRA_tiling.Z_bp.bw"
DCT_TRACK_PATH[ID_TRACK]["signal"] = URL_TRACK

### TMPRA (LMO2; JIN WOO)
ID_TRACK  = "TMPRA_OL45"
URL_TRACK = "https://data.cyverse.org/dav-anon/iplant/home/ohjinwoo94/OL45_K562_20220628.Z_bp.bw"
DCT_TRACK_PATH[ID_TRACK]["signal"] = URL_TRACK
