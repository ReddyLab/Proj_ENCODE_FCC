### set environment
from track_path_starrmpra_signal_original_local   import DCT_TRACK_PATH as DCT_TRACK_PATH_LOCAL
from track_path_starrmpra_signal_original_dropbox import DCT_TRACK_PATH as DCT_TRACK_PATH_ONLINE

### init: tracks and parameteres
DCT_TRACK_ONLINE = dict()
DCT_TRACK_LOCAL  = dict()

txt_color_signal = "#525252"
txt_color_region = "#525252"
DCT_TRACK_COLOR  = {
    "signal":    txt_color_signal,
    "region":    txt_color_region,
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

### init track parameteres
dct_track_color = DCT_TRACK_COLOR

### setup tracks
for dct_track_import, dct_track_result in zip(lst_track_import, lst_track_result):
    for txt_track_index, dct_track_path in dct_track_import.items():
        ### init
        dct_track_out = dict()

        ### set track labels
        dct_track_label = {
            "signal":   f"{txt_track_index}",
            "region":   f"{txt_track_index}",
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
