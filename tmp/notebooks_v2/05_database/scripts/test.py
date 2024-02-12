### ++++++++++++++++++++++++++++++++++++++
### Set environment
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
import numpy  as np
import os, sys, time, gzip, glob
import argparse
import sqlite3

from functools  import partial
from prep_config import *
from prep_reset  import *
from prep_create import *
from prep_check  import *

print = partial(print, flush=True)

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
    parser.add_argument('--verbose',  action='store_true', help='foo help')
    
    ### parse arguments and return
    args=parser.parse_args()
    return args

def main(assay = None, region = None, database = None, verbose = False):
    """Main function"""
    
    ### Set output file directory
    #fdiry = os.path.join(FD_RES, assay, "database")
    #fname = f"{prefix}_{region}.db"
    #fpath = os.path.join(fdiry, fname)
    fpath_dtb = database
    
    ### Show arguments
    if (verbose):
        print(f"Show arguments:")
        print(f"Assay:     {assay}")
        print(f"REGION:    {region}")
        print(f"FPATH_DTB: {fpath_dtb}")
        print()
    
if __name__ == "__main__":
    args = parse_args()
    main(**vars(args))