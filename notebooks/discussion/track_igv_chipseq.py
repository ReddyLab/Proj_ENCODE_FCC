### set environment
from track_path_chipseq_encode import DCT_TRACK_PATH as DCT_TRACK_PATH_ENCODE

### init: tracks and parameteres
DCT_TRACK_ENCODE = dict()
DCT_TRACK_LOCAL  = dict()

DCT_TRACK_COLOR  = {
    "signal": "#525252",
    "region": "#525252"
}

DCT_TRACK_HEIGHT = {
    "signal":    50,
    "region":    30,
}

### =====================================
### Track: ENCODE
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track_import = DCT_TRACK_PATH_ENCODE
dct_track_result = DCT_TRACK_ENCODE
dct_track_height = DCT_TRACK_HEIGHT
dct_track_color  = DCT_TRACK_COLOR

for txt_track_index, dct_track_path in dct_track_import.items():
    ### init
    dct_track_out = dict()
    
    ### set track labels
    dct_track_label = {
        "signal":    f"ChIP-seq ({txt_track_index}; K562)",
        "region":    f"ChIP-seq ({txt_track_index}; Peak)",
    }
    
    for key, value in dct_track_path.items():
        ### get track parameters
        num_track_height = dct_track_height[key]
        txt_track_label  = dct_track_label[key]
        txt_track_color  = dct_track_color[key]
        txt_track_path   = value
        
        ### create a new track
        dct_track = {
            "name":     txt_track_label, 
            "path":     txt_track_path,
            "url":      txt_track_path,
            "height":   num_track_height,
            "color":    txt_track_color,
            "altColor": txt_track_color,
        }

        ### set track display model
        if key == "region":
            dct_track["displayMode"] = "SQUISHED"
                    
        ### collect the track for different track type
        dct_track_out[key] = dct_track
        
    ### collect the track
    dct_track_result[txt_track_index] = dct_track_out
