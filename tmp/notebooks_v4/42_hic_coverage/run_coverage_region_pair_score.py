### Set environment
import numpy as np
import itertools as it
import functools
import os, sys, gzip
import argparse
import hicstraw
import re

print = functools.partial(print, flush=True)

### Parse arguments and set global variables
parser = argparse.ArgumentParser()
parser.add_argument('--fpath_hic',     type=str, required=True)
parser.add_argument('--fpath_inp',     type=str, required=True)
parser.add_argument('--fpath_out',     type=str, required=True)
parser.add_argument('--normalization', type=str, required=True)
parser.add_argument('--resolution',    type=int, required=True)
parser.add_argument('--chromosome',    type=str, required=True)

args = parser.parse_args()
FP_HIC=args.fpath_hic
FP_INP=args.fpath_inp
FP_OUT=args.fpath_out

TXT_CHROMOSOME    = args.chromosome
TXT_NORMALIZATION = args.normalization
VAL_RESOLUTION    = args.resolution

### Import data: Hi-C
hic = hicstraw.HiCFile(FP_HIC)
mat_object = hic.getMatrixZoomData(
    TXT_CHROMOSOME, 
    TXT_CHROMOSOME, 
    "observed", 
    TXT_NORMALIZATION, 
    "BP", 
    VAL_RESOLUTION)

### Read data and write results to output file
with gzip.open(FP_INP,'rt') as finp, gzip.open(FP_OUT,'wt') as fout:
    
    ### set read lines
    #lines_inp = it.islice(finp, 30)
    lines_inp = finp
    
    ### progress each line
    for line_idx, line_inp in enumerate(lines_inp):
    
        ### parse info
        line_inp = line_inp.strip()
        txt_chrom1, val_start1, val_end1, txt_chrom2, val_start2, val_end2 = re.split(":|-|\t", line_inp)
        
        ### show progress
        if (line_idx % 1_000_000) == 0:
            print("Process Line:", line_idx)
        
        ### get hic matrix
        mat_numpy = mat_object.getRecordsAsMatrix(
            int(val_start1),
            int(val_end1),
            int(val_start2),
            int(val_end2)
        )
        
        ### get nonzero submatrix of hic
        idx_nonzero  = np.nonzero(mat_numpy)
        mat_nonzero  = mat_numpy[idx_nonzero]
        is_not_empty = np.any(mat_nonzero)
        
        ### calculate descriptive stats on nonzero values
        if(is_not_empty):
            ### calculate values
            lst = [
                np.mean(mat_nonzero),
                np.std(mat_nonzero),
                np.quantile(mat_nonzero, 0.25),
                np.quantile(mat_nonzero, 0.5),
                np.quantile(mat_nonzero, 0.75),
                np.min(mat_nonzero),
                np.max(mat_nonzero),
                mat_nonzero.flatten().shape[0]/mat_numpy.flatten().shape[0]
            ]
            ### round values
            fun = lambda x: np.round(x, decimals = 5)
            lst = list(map(fun, lst))
            
            ### concatenate results into line for output file
            txt_scores = "\t".join(map(str, lst))
            txt_name   = "|".join( map(str, line_inp.split()))
            txt_loc    = "\t".join([
                txt_chrom1, val_start1, val_end1, 
                txt_chrom2, val_start2, val_end2])
            
            line_out = "\t".join([txt_loc, txt_name, txt_scores])
            line_out = line_out + "\n"
            fout.write(line_out)
