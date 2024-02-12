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
    parser.add_argument('--verbose',  action='store_true', help='foo help')
    
    ### parse arguments and return
    args=parser.parse_args()
    return args

def main(database = None, verbose = False):
    """Main function"""
    
    ### Set variables
    fpath_dtb = database
    
    ### create database connection
    con = sqlite3.connect(fpath_dtb)
    cur = con.cursor()
    
    ### indexing tables
    for table, index_table in dct_index_table.items():
        if (verbose):
            print(f"\nIndex table {table}...")
        index_table(cur)
    
    ### close database connection
    con.commit()
    con.close()
    
if __name__ == "__main__":
    args = parse_args()
    main(**vars(args))