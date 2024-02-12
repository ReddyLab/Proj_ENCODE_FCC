### set environment
from track_path_chipseq_encode import DCT_TRACK_PATH as DCT_TRACK_PATH_ENCODE

### init: tracks and parameteres
DCT_TRACK_ENCODE = dict()
DCT_TRACK_LOCAL  = dict()

txt_color_signal = "#525252"
txt_color_region = "#525252"
DCT_TRACK_COLOR  = {
    "signal":    txt_color_signal,
    "region":    txt_color_region,
}

### =====================================
### Track: ENCODE
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track_import = DCT_TRACK_PATH_ENCODE
dct_track_result = DCT_TRACK_ENCODE
dct_track_color  = DCT_TRACK_COLOR

for txt_track_index, dct_track_path in dct_track_import.items():
    ### init
    dct_track_out = dict()
    
    ### set track labels
    dct_track_label = {
        "signal":   f"{txt_track_index}",
        "region":   f"{txt_track_index}",
        "interact": f"{txt_track_index}",
    }
    
    for txt_track_type, txt_track_track in dct_track_path.items():
        ### get track parameters
        txt_track_label  = dct_track_label[txt_track_type]
        txt_track_color  = dct_track_color[txt_track_type]
        
        ### create a new track
        dct_track = {
            "name":  txt_track_label, 
            "url":   txt_track_track,
            "color": txt_track_color,
        }

        ### set track display model
        if txt_track_type == "region":
            dct_track["displayMode"] = "SQUISHED"
        
        ### collect the track for different track type
        dct_track_out[txt_track_type] = dct_track
        
    ### collect the track
    dct_track_result[txt_track_index] = dct_track_out
