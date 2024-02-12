### set environment
from collections import defaultdict
from track_path_starrmpra_region_local   import DCT_TRACK_PATH as DCT_TRACK_PATH_LOCAL
from track_path_starrmpra_region_dropbox import DCT_TRACK_PATH as DCT_TRACK_PATH_ONLINE

### init: tracks and parameteres
DCT_TRACK_ONLINE = defaultdict(lambda: dict())
DCT_TRACK_LOCAL  = defaultdict(lambda: dict())

DCT_TRACK_HEIGHT = {
    "signal":    50,
    "region":    30,
}

### =====================================
### Setup track parameters
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### init: list of parameters
lst_track_label = list()
lst_track_index = list()
lst_track_color = list()

### ASTARR
txt_track_label = "ASTARR (Enhancer call)"
txt_track_index = "ASTARR_A"
txt_track_color = "#e41a1c"

lst_track_label.append(txt_track_label)
lst_track_index.append(txt_track_index)
lst_track_color.append(txt_track_color)

### WSTARR
txt_track_label = "WSTARR (Enhancer call)"
txt_track_index = "WSTARR_A"
txt_track_color = "#377eb8"

lst_track_label.append(txt_track_label)
lst_track_index.append(txt_track_index)
lst_track_color.append(txt_track_color)

### TMPRA
txt_track_label = "Tiling MPRA (Enhancer call)"
txt_track_index = "TMPRA_A"
txt_track_color = "#4daf4a"

lst_track_label.append(txt_track_label)
lst_track_index.append(txt_track_index)
lst_track_color.append(txt_track_color)

### LMPRA
txt_track_label = "LentiMPRA (Enhancer call)"
txt_track_index = "LMPRA_A"
txt_track_color = "#a65628"

lst_track_label.append(txt_track_label)
lst_track_index.append(txt_track_index)
lst_track_color.append(txt_track_color)

### ATAC
txt_track_label = "ATAC (MACS Peaks)"
txt_track_index = "ATAC"
txt_track_color = "#525252"

lst_track_label.append(txt_track_label)
lst_track_index.append(txt_track_index)
lst_track_color.append(txt_track_color)

### =====================================
### Create tracks
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### init tracks
#dct_track_import = DCT_TRACK_PATH_LOCAL
#dct_track_result = DCT_TRACK_LOCAL

lst_track_import = [
    DCT_TRACK_PATH_LOCAL,
    DCT_TRACK_PATH_ONLINE
]

lst_track_result = [
    DCT_TRACK_LOCAL,
    DCT_TRACK_ONLINE
]

### init track parameteres
dct_track_height = DCT_TRACK_HEIGHT
txt_track_type   = "region"

### setup tracks
for dct_track_import, dct_track_result in zip(lst_track_import, lst_track_result):
    for txt_track_label, txt_track_index, txt_track_color in zip(
        lst_track_label, 
        lst_track_index, 
        lst_track_color):

        ### get track and parameters
        txt_track_path   = dct_track_import[txt_track_index][txt_track_type]
        num_track_height = dct_track_height[txt_track_type]

        ### create a track
        dct_track = {
            "name":     txt_track_label,
            "path":     txt_track_path,
            "url":      txt_track_path,
            "height":   num_track_height,
            "color":    txt_track_color,
            "altColor": txt_track_color,
        }
        
        ### set track display model
        if txt_track_type == "region":
            dct_track["displayMode"] = "SQUISHED"
            
        ### collect the track
        dct_track_result[txt_track_index][txt_track_type] = dct_track
