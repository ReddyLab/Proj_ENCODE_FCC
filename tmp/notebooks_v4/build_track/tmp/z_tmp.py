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


### =====================================
### Track: Jin Woo
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track_import = DCT_TRACK_PATH_JINWOO
dct_track_result = DCT_TRACK_JINWOO

for txt_track_index, dct_track_path in dct_track_import.items():
    ### init
    dct_track_out = dict()
    
    ### set track labels
    dct_track_label = {
        "signal": f"CRISPRi-HCRFF ({txt_track_index}; Z score)",
        "region": f"CRISPRi-HCRFF ({txt_track_index}; CASA)",
    }
    
    ### set track heights
    dct_track_height = DCT_TRACK_HEIGHT
    
    ### set track colors
    dct_track_color = DCT_TRACK_COLOR
    
    for txt_track_type, txt_track_track in dct_track_path.items():
        ### get track parameters
        num_track_height = dct_track_height[txt_track_type]
        txt_track_label  = dct_track_label[txt_track_type]
        txt_track_color  = dct_track_color[txt_track_type]
        
        ### create a new track
        dct_track = {
            "name":     txt_track_label, 
            "path":     txt_track_track,
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


### =====================================
### Track: LOCAL
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dct_track_import = DCT_TRACK_PATH_LOCAL
dct_track_result = DCT_TRACK_LOCAL

for txt_track_index, dct_track_path in dct_track_import.items():
    ### init
    dct_track_out = dict()
    
    ### set track labels
    dct_track_label = {
        "signal": f"CRISPRi-HCRFF ({txt_track_index}; Z score)",
        "region": f"CRISPRi-HCRFF ({txt_track_index}; CASA)",
    }
    
    ### set track heights
    dct_track_height = DCT_TRACK_HEIGHT
    
    ### set track colors
    dct_track_color = DCT_TRACK_COLOR
    
    for txt_track_type, txt_track_track in dct_track_path.items():
        ### get track parameters
        num_track_height = dct_track_height[txt_track_type]
        txt_track_label  = dct_track_label[txt_track_type]
        txt_track_color  = dct_track_color[txt_track_type]
        
        ### create a new track
        dct_track = {
            "name":     txt_track_label, 
            "path":     txt_track_track,
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
