### Set environment
import numpy as np
import itertools as it
import functools
import re, os, sys, gzip
import argparse
import hicstraw

print = functools.partial(print, flush=True)

### Parse arguments and set global variables

parser = argparse.ArgumentParser()
parser.add_argument('--fpath_hic',     type=str,  required=True) # description="file path / url of the hic file"
parser.add_argument('--fpath_inp',     type=str,  required=True) # description="bedpe file"
parser.add_argument('--fpath_out',     type=str,  required=True) # description="output npy file path"
parser.add_argument('--normalization', type=str,  required=True) # description="NONE, VC, VC_SQRT, KR, SCALE, etc"
parser.add_argument('--resolution',    type=int,  required=True) # description="resolution (bin size)"
parser.add_argument('--window_size',   type=int,  required=True) # description="window size"
parser.add_argument('--data_type',     type=str,  required=True) # description="'observed' or 'oe' (observed/expected)")
parser.add_argument('--verbose',       type=bool, default=True)
parser.add_argument('--num_line_show', type=int,  default=1)
parser.add_argument('--num_line_read', type=int,  default=None)

args = parser.parse_args()
TXT_FPATH_HIC     = args.fpath_hic
TXT_FPATH_INP     = args.fpath_inp
TXT_FPATH_OUT     = args.fpath_out

TXT_NORMALIZATION = args.normalization
NUM_RESOLUTION    = args.resolution
NUM_WINDOW_SIZE   = args.window_size
TXT_DATA_TYPE     = args.data_type

VERBOSE       = args.verbose
NUM_LINE_SHOW = args.num_line_show
NUM_LINE_READ = args.num_line_read

TXT_CHROM1 = None
TXT_CHROM2 = None
LST_MATRIX = []

### show global variables
if VERBOSE:
    print("===== Run script =====")
    print("Script: run_hicstraw_aggregate.py")
    print("")
    
    print("==== Arguments ====")
    print("Hi-C   file:   ", TXT_FPATH_HIC)
    print("Input  file:   ", TXT_FPATH_INP)
    print("Output file:   ", TXT_FPATH_OUT)
    print("")
    
    print("Normalization: ", TXT_NORMALIZATION)
    print("Data type:     ", TXT_DATA_TYPE)
    print("Resolution:    ", NUM_RESOLUTION)
    print("Window size:   ", NUM_WINDOW_SIZE)
    print("#Lines show:   ", NUM_LINE_SHOW)
    print("#Lines read:   ", NUM_LINE_READ)
    print("")
    
### Import data: Hi-C
hic = hicstraw.HiCFile(TXT_FPATH_HIC)

### read lines of input file
with open(TXT_FPATH_INP,'r') as finp:

    ### set read lines
    lines_inp = it.islice(finp, NUM_LINE_READ)
    lines_inp = finp
    
    ### get header
    cnames = lines_inp.readline()
    
    ### progress each line
    for line_idx, line_inp in enumerate(lines_inp):
        
        ### parse info
        line_inp = line_inp.strip()
        
        lst = re.split(":|-|\t", line_inp)
        txt_chrom1, num_start1, num_end1 = lst[0:3]
        txt_chrom2, num_start2, num_end2 = lst[3:6]
        txt_name = lst[6]
        
        ### update hic matrix object
        if (TXT_CHROM1 != txt_chrom1) or (TXT_CHROM2 != txt_chrom2):
            TXT_CHROM1 = txt_chrom1
            TXT_CHROM2 = txt_chrom2
            
            mat_object = hic.getMatrixZoomData(
                TXT_CHROM1, 
                TXT_CHROM2, 
                TXT_DATA_TYPE,
                TXT_NORMALIZATION, 
                "BP", 
                NUM_RESOLUTION)
        
        ### show progress
        if VERBOSE:
            if (line_idx % NUM_LINE_SHOW) == 0:
                print("Process Line:", line_idx)
                print(txt_chrom1, num_start1, num_end1)
                print(txt_chrom2, num_start2, num_end2)
                print("")
                
        ### get hic matrix
        mat_numpy = mat_object.getRecordsAsMatrix(
            int(num_start1) - NUM_WINDOW_SIZE,
            int(num_start1) + NUM_WINDOW_SIZE,
            int(num_start2) - NUM_WINDOW_SIZE,
            int(num_start2) + NUM_WINDOW_SIZE
        )
        
        ### collect hic matrix
        LST_MATRIX.append(mat_numpy)

### 
with open(TXT_FPATH_OUT, 'wb') as fout:
    arr = np.array(LST_MATRIX)
    np.save(fout, arr)

if VERBOSE:
    print("")
    print("==== Save results ====")
    print("Array shape:", arr.shape)
    print("")

