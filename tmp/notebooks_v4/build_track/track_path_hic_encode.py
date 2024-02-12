### set environment
from collections import defaultdict

### get the URLs
URL_HIC_INTACT_MATRIX_ENCSR479XDG = "https://www.encodeproject.org/files/ENCFF621AIY/@@download/ENCFF621AIY.hic"
URL_HIC_INTACT_MATRIX_DEEP        = "https://s3.us-east-1.wasabisys.com/aiden-suhas/hic_files/FINAL_GRCh38_processing/K562/total/inter.hic"

URL_HIC_INTACT_LOOP_ENCSR479XDG = "https://www.encodeproject.org/files/ENCFF256ZMD/@@download/ENCFF256ZMD.bedpe.gz"
URL_HIC_INTACT_LOOP_DEEP        = "https://www.dropbox.com/sh/13ihnis7exi9lrp/AADgaBk0RoNDRAC62F5QpPFDa/K562/3.15.23/localizedList_primary_10.bedpe?dl=0"

### init
DCT_TRACK_PATH = defaultdict(lambda: dict())

### =====================================
### Hi-C (intact): ENCSR479XDG
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

idn = "ENCSR479XDG"
key = "matrix"
val = URL_HIC_INTACT_MATRIX_ENCSR479XDG
DCT_TRACK_PATH[idn][key] = val

idn = "ENCSR479XDG"
key = "loop"
val = URL_HIC_INTACT_LOOP_ENCSR479XDG
DCT_TRACK_PATH[idn][key] = val

### =====================================
### Hi-C (intact): Deep
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

idn = "Deep"
key = "matrix"
val = URL_HIC_INTACT_MATRIX_DEEP
DCT_TRACK_PATH[idn][key] = val

idn = "Deep"
key = "loop"
val = URL_HIC_INTACT_LOOP_DEEP
DCT_TRACK_PATH[idn][key] = val
