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
### Main function
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def parse_args():
    """Parse arguments from command line"""
    
    ### set arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--database', help='foo help')
    parser.add_argument('--finp',     help='foo help')
    parser.add_argument('--verbose',  action='store_true', help='foo help')
    
    ### parse arguments and return
    args=parser.parse_args()
    return args

def main(database = None, finp = None, verbose = False):
    """Main function"""
    
    ### Set variables
    fpath_dtb = database
    fpath_inp = finp
    insert_table = dct_insert_table["Sample"]
    
    ### create database connection
    con = sqlite3.connect(fpath_dtb)
    cur = con.cursor()
    
    ### read file and insert lines into table
    if (verbose):
        print(f"\nInsert...")
        print(f"    Table:  Sample")
        print(f"    Input:  {fpath_inp}")
    
    dat_sample = pd.read_table(fpath_inp, sep=",")
    dat_sample = dat_sample.loc[:,["Sample", "Group", "Rep", "Count"]]
    lines = dat_sample.to_records(index=False)
    insert_table(cur, lines)
    
    ### close database connection
    con.commit()
    con.close()
        
if __name__ == "__main__":
    args = parse_args()
    main(**vars(args))