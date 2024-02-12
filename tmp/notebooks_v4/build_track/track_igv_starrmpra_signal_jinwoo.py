### set environment
from collections import defaultdict
from track_path_starrmpra_signal_jinwoo import DCT_TRACK_PATH as DCT_TRACK_PATH_JINWOO

### init: tracks and parameteres
DCT_TRACK_JINWOO = defaultdict(lambda: dict())

DCT_TRACK_COLOR  = {
    "signal": "#525252",
    "region": "#525252"
}

DCT_TRACK_HEIGHT = {
    "signal":    50,
    "region":    30,
}

### =====================================
### setup tracks
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### init: list of parameters
lst_track_label = list()
lst_track_index = list()

### ASTARR (JIN WOO)
txt_track_label = "ASTARR (Log2FC; Jin Woo)"
txt_track_index = "ASTARR"

lst_track_label.append(txt_track_label)
lst_track_index.append(txt_track_index)

### TMPRA (GATA/MYC; JIN WOO)
txt_track_label = "TMPRA (ZScore; GATA/MYC; Jin Woo)"
txt_track_index = "TMPRA_OL43"

lst_track_label.append(txt_track_label)
lst_track_index.append(txt_track_index)

### TMPRA (FEN/FADS; JIN WOO)
txt_track_label = "TMPRA (ZScore; FADS/FEN; Jin Woo)"
txt_track_index = "TMPRA_OL13"

lst_track_label.append(txt_track_label)
lst_track_index.append(txt_track_index)

### TMPRA (LMO2; JIN WOO)
txt_track_label = "TMPRA (ZScore; OL45; Jin Woo)"
txt_track_index = "TMPRA_OL45"

lst_track_label.append(txt_track_label)
lst_track_index.append(txt_track_index)

### =====================================
### Track: JINWOO
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### init the tracks
dct_track_import = DCT_TRACK_PATH_JINWOO
dct_track_result = DCT_TRACK_JINWOO
dct_track_height = DCT_TRACK_HEIGHT
dct_track_color  = DCT_TRACK_COLOR

### create tracks
txt_track_type  = "signal"
for txt_track_label, txt_track_index in zip(
    lst_track_label, 
    lst_track_index):
    
    ### get track and parameters
    txt_track_path   = dct_track_import[txt_track_index][txt_track_type]
    num_track_height = dct_track_height[txt_track_type]
    txt_track_color  = dct_track_color[txt_track_type]
    
    
    ### create a track
    dct_track = {
        "name":     txt_track_label, 
        "path":     txt_track_path,
        "url":      txt_track_path,
        "height":   num_track_height,
        "color":    txt_track_color,
        "altColor": txt_track_color,
    }
            
    ### collect the track
    dct_track_result[txt_track_index][txt_track_type] = dct_track