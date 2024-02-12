### set environment
from track_path_encode_e2g_local   import DCT_TRACK_PATH as DCT_TRACK_PATH_LOCAL
from track_path_encode_e2g_dropbox import DCT_TRACK_PATH as DCT_TRACK_PATH_ONLINE

### init: tracks and parameteres
DCT_TRACK_ONLINE = dict()
DCT_TRACK_LOCAL  = dict()

DCT_TRACK_COLOR  = {
    "region_active":                "#525252",
    "region_total":                 "#525252",
    "loop_tss_original_active":     "#525252",
    "loop_tss_original_total":      "#525252",
    "loop_tss_updated_active":      "#525252",
    "loop_tss_updated_total":       "#525252",
    "interact_tss_original_active": "#525252",
    "interact_tss_original_total":  "#525252",
    "interact_tss_updated_active":  "#525252",
    "interact_tss_updated_total":   "#525252",
}

DCT_TRACK_HEIGHT = {
    "region_active":                30,
    "region_total":                 30,
    "loop_tss_original_active":     250,
    "loop_tss_original_total":      250,
    "loop_tss_updated_active":      250,
    "loop_tss_updated_total":       250,
    "interact_tss_original_active": 250,
    "interact_tss_original_total":  250,
    "interact_tss_updated_active":  250,
    "interact_tss_updated_total":   250,
}

### =====================================
### Create tracks
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### init tracks
lst_track_import = [
    DCT_TRACK_PATH_LOCAL,
    DCT_TRACK_PATH_ONLINE
]

lst_track_result = [
    DCT_TRACK_LOCAL,
    DCT_TRACK_ONLINE
]

### init track parameters
dct_track_height = DCT_TRACK_HEIGHT
dct_track_color  = DCT_TRACK_COLOR

### setup tracks
for dct_track_import, dct_track_result in zip(lst_track_import, lst_track_result):
    for txt_track_index, dct_track_path in dct_track_import.items():
        ### init
        dct_track_out = dict()

        ### set track labels
        #dct_track_label = {
        #    "interact_original": f"CRISPR EP Benchmark",
        #    "interact_updated":  f"CRISPR EP Benchmark",
        #    "region": f"CRISPR EP Benchmark (Region)",
        #}
        txt_track_label  = "CRISPR EP Benchmark"
        
        for txt_track_type, txt_track_track in dct_track_path.items():
            ### get track parameters
            num_track_height = dct_track_height[txt_track_type]
            #txt_track_label  = dct_track_label[txt_track_type]
            txt_track_color  = dct_track_color[txt_track_type]

            ### create a new track
            dct_track = {
                "name":     txt_track_label, 
                "path":     txt_track_track,
                "url":      txt_track_track,
                "height":   num_track_height,
                "color":    txt_track_color,
                "altColor": txt_track_color,
            }

            ### set track display model
            if txt_track_type == "region":
                dct_track["displayMode"] = "SQUISHED"

            ### collect the track for different track type
            dct_track_out[txt_track_type] = dct_track

        ### collect the track
        dct_track_result[txt_track_index] = dct_track_out
