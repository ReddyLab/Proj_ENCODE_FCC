### ++++++++++++++++++++++++++++++++++++++
### Set environment
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
import numpy as np
import os, sys, time, gzip, glob
import argparse
import sqlite3

from functools   import partial
from prep_insert import *

# https://stackoverflow.com/questions/49456158/integer-in-python-pandas-becomes-blob-binary-in-sqlite
sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))


### ++++++++++++++++++++++++++++++++++++++
### Helper function and query
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

query_insert = """
    INSERT OR IGNORE INTO Annotation
        (fragment, binding)
    VALUES 
        (?,?)
    """

def prep_line(line):
    """Function to process each line"""
    ### parse info: Chrom, Start, Stop, Name, Score, Strand
    fragment = f"{line[0]}_{line[1]}_{line[2]}"
    binding  = f"{line[6]}_{line[7]}_{line[8]}_{line[9]}"
    return fragment, binding

### ++++++++++++++++++++++++++++++++++++++
### Main function
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def parse_args():
    """Parse arguments from command line"""
    
    ### set arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--assay',  help='foo help')
    parser.add_argument('--folder', help='foo help')
    parser.add_argument('--region', help='foo help')
    parser.add_argument('--sample', help='foo help')
    parser.add_argument('--strand', help='foo help')
    parser.add_argument('--prefix', help='foo help')
    
    ### parse arguments and return
    args=parser.parse_args()
    return args

def main(assay = None, folder = None, region = None, sample = None, strand = None, prefix = None):
    """Main function"""
    ### Get input file directory
    fglob = os.path.join(FD_RES, assay, folder, f"*{sample}*{region}*{strand}*")
    fpath = glob.glob(fglob)[0]
    fpath_inp = fpath
    
    ### Set output file directory
    fdiry = os.path.join(FD_RES, assay, "database")
    fname = f"{prefix}_{region}.db"
    fpath = os.path.join(fdiry, fname)
    fpath_dtb = fpath
    
    ### Show arguments
    print(f"Show arguments:")
    print(f"ASSAY:     {assay}")
    print(f"FOLDER:    {folder}")
    print(f"REGION:    {region}")
    print(f"SAMPLE:    {sample}")
    print(f"STRAND:    {strand}")
    print(f"FPATH_INP: {fpath_inp}")
    print(f"FPATH_DTB: {fpath_dtb}")
    print()
    
    ### read file and insert lines into table
    fun = prep_line
    with gzip.open(fpath_inp, "rt") as file:
        ### Set line generator
        lines = gen_lines(file, n_lines=5, remove_header=True)
        lines = map(fun, lines)
        for line in lines:
            print(line)
            
        ### Setup a database connection
        """
        con = sqlite3.connect(fpath_dtb, isolation_level=None)
        con.execute('PRAGMA journal_mode = OFF;')
        con.execute('PRAGMA synchronous = 0;')
        con.execute('PRAGMA cache_size = 1000000;')
        con.execute('PRAGMA locking_mode = EXCLUSIVE;')
        con.execute('PRAGMA temp_store = MEMORY;')
        
        ### Insertion
        con.executemany(query_insert, lines)
        con.commit()
        
        ### Close database connection
        con.close()
        """
        
if __name__ == "__main__":
    args = parse_args()
    main(**vars(args))