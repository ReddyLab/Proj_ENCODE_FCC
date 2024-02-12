###
from track_path_hic_encode import DCT_TRACK_PATH as DCT_TRACK_PATH_ENCODE

###
DCT_TRACK_ENCODE = dict()

### =====================================
### Intact Hi-C: ENCODE
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track_import = DCT_TRACK_PATH_ENCODE
dct_track_result = DCT_TRACK_ENCODE

for txt_track_index, dct_track_path in dct_track_import.items():
    dct_track_out    = dict()
    dct_track_label  = {"loop": f"Intact Hi-C ({txt_track_index})"}
    dct_track_height = {"loop": 200}
    dct_track_color  = {"loop": "#225ea8"}
    
    txt_track_type   = "loop"
    num_track_height = dct_track_height[txt_track_type]
    txt_track_label  = dct_track_label[txt_track_type]
    txt_track_color  = dct_track_color[txt_track_type]
    txt_track_path   = dct_track_path[txt_track_type]

    dct_track = {
        "name":     txt_track_label, 
        "path":     txt_track_path,
        "url":      txt_track_path,
        "height":   num_track_height,
        "color":    txt_track_color,
        "altColor": txt_track_color,
        "arcOrientation": "false",
    }
    
    dct_track_out[txt_track_type] = dct_track

    dct_track_result[txt_track_index] = dct_track_out
