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
from prep_line   import *
from prep_index  import *
from prep_check  import *

print = partial(print, flush=True)

# https://stackoverflow.com/questions/49456158/integer-in-python-pandas-becomes-blob-binary-in-sqlite
sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))

### ++++++++++++++++++++++++++++++++++++++
### Helper function
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def prep_line(line):
    """Function to process each line"""
    ### parse info: Chrom, Start, Stop, Name, Score, Strand
    key = f"{line[0]}_{line[1]}_{line[2]}"
    val = [key, *line[0:3], *line[6:14]]
    return val

### ++++++++++++++++++++++++++++++++++++++
### Main function
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def parse_args():
    """Parse arguments from command line"""
    
    ### set arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--table',    help='foo help')
    parser.add_argument('--database', help='foo help')
    parser.add_argument('--finp',     help='foo help')
    parser.add_argument('--header',     action='store_true', help='foo help')
    parser.add_argument('--compressed', action='store_true', help='foo help')
    parser.add_argument('--verbose',    action='store_true', help='foo help')
    
    ### parse arguments and return
    args=parser.parse_args()
    return args

def main(table = None, database = None, finp = None, header = False, compressed = False, verbose = False):
    """Main function"""
    
    ### Set variables
    fpath_dtb = database
    fpath_inp = finp
    sample    = get_sample(fpath_inp)
    
    ### Set functions
    if compressed:
        fopen = gzip.open
        fopen = partial(fopen, mode="rt")
    else:
        fopen = open
        fopen = partial(fopen, mode="r")
    
    prep_line = dct_prep_line[table]
    prep_line = partial(prep_line, sample=sample)
    insert_table = dct_insert_table[table]
    
    ### create database connection
    con = sqlite3.connect(fpath_dtb, isolation_level=None)
    con.execute('PRAGMA journal_mode = OFF;')
    con.execute('PRAGMA synchronous = 0;')
    con.execute('PRAGMA cache_size = 1000000;')
    con.execute('PRAGMA locking_mode = EXCLUSIVE;')
    con.execute('PRAGMA temp_store = MEMORY;')
    cur = con.cursor()
    
    ### read file and insert lines into table
    if (verbose):
        print(f"\nInsert...")
        print(f"    Table:  {table}")
        print(f"    Input:  {fpath_inp}")
        print(f"    Sample: {sample}")
        
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        with fopen(fpath_inp) as file:
            lines = gen_lines(file, n_lines=3)
            for line in lines:
                print(line)

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        with fopen(fpath_inp) as file:
            lines = gen_lines(file, n_lines=3, remove_header=header)
            lines = map(prep_line, lines)
            for line in lines:
                print(line)

    with fopen(fpath_inp) as file:
        lines = gen_lines(file, n_lines=None, remove_header=header)
        lines = map(prep_line, lines)
        insert_table(cur, lines)
            
    ### close database connection
    con.commit()
    con.close()
        
if __name__ == "__main__":
    args = parse_args()
    main(**vars(args))