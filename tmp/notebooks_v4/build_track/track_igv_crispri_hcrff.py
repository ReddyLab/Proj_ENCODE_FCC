### set environment
from track_path_crispri_hcrff_encode import DCT_TRACK_PATH as DCT_TRACK_PATH_ENCODE
from track_path_crispri_hcrff_jinwoo import DCT_TRACK_PATH as DCT_TRACK_PATH_JINWOO
from track_path_crispri_hcrff_local  import DCT_TRACK_PATH as DCT_TRACK_PATH_LOCAL

### init: tracks and parameteres
DCT_TRACK_ENCODE = dict()
DCT_TRACK_JINWOO = dict()
DCT_TRACK_LOCAL  = dict()

txt_color_signal = "#f768a1"
#txt_color_signal = "#dd3497"
txt_color_region = "#dd3497"
DCT_TRACK_COLOR  = {
    "signal":    txt_color_signal,
    "signal_R1": txt_color_signal,
    "signal_R2": txt_color_signal,
    "region":    txt_color_region,
    "interact":  txt_color_region,
}

DCT_TRACK_HEIGHT = {
    "signal":    50,
    "signal_R1": 50,
    "signal_R2": 50,
    "region":    30,
    "interact":  70,
}

### =====================================
### Create tracks
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### init tracks
#dct_track_import = DCT_TRACK_PATH_LOCAL
#dct_track_result = DCT_TRACK_LOCAL

lst_track_import = [
    DCT_TRACK_PATH_ENCODE,
    DCT_TRACK_PATH_JINWOO,
    DCT_TRACK_PATH_LOCAL,
]

lst_track_result = [
    DCT_TRACK_ENCODE,
    DCT_TRACK_JINWOO,
    DCT_TRACK_LOCAL,
]

### init track parameteres
dct_track_height = DCT_TRACK_HEIGHT
dct_track_color  = DCT_TRACK_COLOR

### setup tracks
for dct_track_import, dct_track_result in zip(lst_track_import, lst_track_result):
    for txt_track_index, dct_track_path in dct_track_import.items():
        ### init
        dct_track_out = dict()

        ### set track labels
        dct_track_label = {
            "signal":    f"CRISPRi-HCRFF ({txt_track_index}; Z score)",
            "signal_R1": f"CRISPRi-HCRFF ({txt_track_index}; Log2FC)",
            "signal_R2": f"CRISPRi-HCRFF ({txt_track_index}; Log2FC)",
            "region":    f"CRISPRi-HCRFF ({txt_track_index}; CASA)",
            "interact":  f"CRISPRi-HCRFF ({txt_track_index}; Interact)",
        }

        for txt_track_type, txt_track_track in dct_track_path.items():
            ### get track parameters
            num_track_height = dct_track_height[txt_track_type]
            txt_track_label  = dct_track_label[txt_track_type]
            txt_track_color  = dct_track_color[txt_track_type]

            ### create a new track
            dct_track = {
                "name":     txt_track_label, 
                "path":     txt_track_track,
                "url":     txt_track_track,
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
