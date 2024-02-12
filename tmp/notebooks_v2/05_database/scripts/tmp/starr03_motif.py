### ++++++++++++++++++++++++++++++++++++++
### Set environment
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
import numpy  as np
import pandas as pd
import os, sys, time, gzip, glob
import argparse
import sqlite3

from functools  import partial
from prep_config import *
from prep_reset  import *
from prep_create import *
from prep_insert import *
from prep_index  import *
from prep_check  import *

print = partial(print, flush=True)

# https://stackoverflow.com/questions/49456158/integer-in-python-pandas-becomes-blob-binary-in-sqlite
sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))

### ++++++++++++++++++++++++++++++++++++++
### Helper function and query
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def prep_line(line):
    """Function to process each line"""
    ### parse info: Chrom, Start, Stop, Motif, Score
    key = f"{line[0]}_{line[1]}_{line[2]}_{line[3]}"
    val = [key, *line]
    return val

### ++++++++++++++++++++++++++++++++++++++
### Main function
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def parse_args():
    """Parse arguments from command line"""
    
    ### set arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--assay',  help='foo help')
    parser.add_argument('--chrom',  help='foo help')
    parser.add_argument('--region', help='foo help')
    parser.add_argument('--prefix', help='foo help')
    
    ### parse arguments and return
    args=parser.parse_args()
    return args

### ++++++++++++++++++++++++++++++++++++++
### Main function
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def parse_args():
    """Parse arguments from command line"""
    
    ### set arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--assay',    help='foo help')
    parser.add_argument('--region',   help='foo help')
    parser.add_argument('--database', help='foo help')
    parser.add_argument('--finp',     help='foo help')
    parser.add_argument('--verbose',  action='store_true', help='foo help')
    
    ### parse arguments and return
    args=parser.parse_args()
    return args

def main(assay = None, region = None, finp = None, database = None, verbose = False):
    """Main function"""
    
    ### Set variables
    fpath_dtb = database
    fpath_inp = finp
    
    ### create database connection
    con = sqlite3.connect(fpath_dtb)
    cur = con.cursor()
    
    ### read file and insert lines into table
    if (verbose):
        print("\nInsert: Motif...")
        print(f"Input File: {fpath_inp}")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
    with gzip.open(fpath_inp, "rt") as file:
        lines = gen_lines(file, n_lines=5)
        for line in lines:
            print(line)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
    fun = prep_line
    with gzip.open(fpath_inp, "rt") as file:
        lines = gen_lines(file, n_lines=5, remove_header=True)
        lines = map(fun, lines)
        for line in lines:
            print(line)

    ### close database connection
    con.close()
        
if __name__ == "__main__":
    args = parse_args()
    main(**vars(args))