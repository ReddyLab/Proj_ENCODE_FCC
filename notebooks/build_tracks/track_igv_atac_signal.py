### set environment
from collections import defaultdict
from track_path_starrmpra_signal_original_local   import DCT_TRACK_PATH as DCT_TRACK_PATH_LOCAL
from track_path_starrmpra_signal_original_dropbox import DCT_TRACK_PATH as DCT_TRACK_PATH_ONLINE

### init: tracks
DCT_TRACK_ONLINE = defaultdict(lambda: dict())
DCT_TRACK_LOCAL  = defaultdict(lambda: dict())

### init: parameters
DCT_TRACK_HEIGHT = {
    "signal":    50,
    "region":    30,
}

### init: list of parameters
lst_track_index = list()
lst_track_label = list()
lst_track_color = list()

### ===================================
### Track: ATAC (ASTARR Input)
### -----------------------------------

###
dct_index2label = {
    "ASTARR_Input_rep1_signal": "ATAC (rep1)",
    "ASTARR_Input_rep2_signal": "ATAC (rep2)",
    "ASTARR_Input_rep3_signal": "ATAC (rep3)",
    "ASTARR_Input_rep4_signal": "ATAC (rep4)",
    "ASTARR_Input_rep5_signal": "ATAC (rep5)",
    "ASTARR_Input_rep6_signal": "ATAC (rep6)"
}
txt_track_color = "#525252"

###
for txt_track_index, txt_track_label in dct_index2label.items():
    lst_track_index.append(txt_track_index)
    lst_track_label.append(txt_track_label)
    lst_track_color.append(txt_track_color)

### ===================================
### Build tracks
### -----------------------------------

### init: track input and output
lst_track_import = [
    DCT_TRACK_PATH_LOCAL,
    #DCT_TRACK_PATH_ONLINE
]
lst_track_result = [
    DCT_TRACK_LOCAL,
    #DCT_TRACK_ONLINE
]

### init: track parameteres
dct_track_height = DCT_TRACK_HEIGHT
txt_track_type   = "signal"

### setup tracks
for dct_track_import, dct_track_result in zip(lst_track_import, lst_track_result):
    for txt_track_index, txt_track_label, txt_track_color in zip(
        lst_track_index, 
        lst_track_label, 
        lst_track_color):

        ### get track and parameters
        dct_track_path   = dct_track_import[txt_track_index]
        txt_track_path   = dct_track_path["path"]
        txt_track_type   = dct_track_path["type"]
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

        ### collect the track
        dct_track_result[txt_track_index] = dct_track