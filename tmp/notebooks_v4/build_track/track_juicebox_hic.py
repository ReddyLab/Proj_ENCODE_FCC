###
from track_path_hic_encode import DCT_TRACK_PATH as DCT_TRACK_PATH_ENCODE

###
DCT_TRACK_ENCODE = dict()
DCT_TRACK_LOCAL  = dict()

###
DCT_TRACK_REFSEQ = {
    "url":    "https://hgdownload.soe.ucsc.edu/goldenPath/hg38/database/ncbiRefSeq.txt.gz",
    "type":   "annotation",
    "format": "refgene",
    "name":   " ",
    "color":  "#252525"
}

###
DCT_TRACK_NORM = {
    "ENCSR479XDG": "SCALE",
    "Deep":        "RU",
}

### =====================================
### Track: ENCODE
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track_import = DCT_TRACK_PATH_ENCODE
dct_track_result = DCT_TRACK_ENCODE

for txt_track_name, dct_track_path in dct_track_import.items():
    ### init
    dct_track_out = dict()
    
    ### set parameters
    dct_track_label = {
        "matrix": f"K562 intact Hi-C ({txt_track_name})",
        "loop":   f"K562 intact Hi-C ({txt_track_name})",
    }
    txt_track_norm = DCT_TRACK_NORM[txt_track_name]
    
    ###
    for key, value in dct_track_path.items():
        ###
        txt_track_label = dct_track_label[key]
        txt_track_path  = value
        
        ###
        if key == "matrix":
            dct_track = {
                "backgroundColor": "255,255,255",
                "name":          txt_track_label,
                "url":           txt_track_path,
                "normalization": txt_track_norm,
            }
        else:
            dct_track = {
                "name": txt_track_label,
                "url":  txt_track_path,
            }
        
        ###
        dct_track_out[key] = dct_track

    ###
    dct_track_result[txt_track_name] = dct_track_out