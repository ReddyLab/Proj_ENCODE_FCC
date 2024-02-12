#!/usr/bin/python
"""
Script: Generate virtual 4C track from the coordinate specified
Author: Kuei-Y. Ko
"""

### ==================================================================
### Set environment and arguments
### ==================================================================

### set environment
import numpy  as np
import pandas as pd
import hicstraw

### set arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--chrom", type=str)
parser.add_argument("--x1",    type=int)
parser.add_argument("--y1",    type=int)
parser.add_argument("--x2",    type=int)
parser.add_argument("--y2",    type=int)
parser.add_argument("--fpath_out",      type=str)
parser.add_argument("--fpath_hic",      type=str)
parser.add_argument("--normalization",  type=str)
parser.add_argument("--resolution",     type=int)
parser.add_argument("-v", "--verbose", action="store_true")

### show arguments
args = parser.parse_args()
if (args.verbose):
    print("Arguments:")
    for arg in vars(args):
        print("- ", arg, ":", getattr(args, arg))
    print(flush=True)

### ==================================================================
### Extract hi-c sub matrix given the coordinate
### ==================================================================

### connect to a hic file
hic = hicstraw.HiCFile(args.fpath_hic)
assert args.resolution in hic.getResolutions(), f"Hi-C data does not have the resolution specified;\nexpect: {hic.getResolutions()};\ngot{args.resolution}"

### create hic object
mat_object = hic.getMatrixZoomData(
    args.chrom, 
    args.chrom, 
    "observed", 
    args.normalization, 
    "BP", 
    args.resolution)

### extract hic sub matrix
mat_numpy = mat_object.getRecordsAsMatrix(
    args.x1,
    args.y1,
    args.x2,
    args.y2
)

### show progress
if (args.verbose):
    print("Matrix generated.")
    print("- Shape:", mat_numpy.shape)
    print(flush=True)

### ==================================================================
### create 1D vectors and combine them into a dataframe
### ==================================================================

### summarize the extracted matrix into a 1D vector
vec_track = np.sum(mat_numpy, axis=1)
vec_chrom = np.repeat(args.chrom, len(vec_track))
vec_start = np.arange(args.x1, args.y1 + args.resolution, args.resolution)
vec_end   = vec_start + args.resolution

### concatenate into a dataframe
dat_track = pd.DataFrame(
    list(zip(
        vec_chrom, 
        vec_start, 
        vec_end, 
        vec_track)),
    columns =['Chrom', 'Start', 'End', 'Score']
)

### show progress
if (args.verbose):
    print("DataFrame generated.")
    print("- Shape:", dat_track.shape)
    print(flush=True)

### save the results
dat_track.to_csv(args.fpath_out, sep="\t", header=False, index=False)
