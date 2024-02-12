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
    
    ### show table names
    print("\nShow table names...")
    res = list_table(cur)
    for x in res:
        print(x)
    
    ### show table index
    print("\nShow table indices...")
    res = list_index(cur)
    for x in res:
        print(x)
        
    ### check table size
    print("\nShow table sizes...")
    tables = ("Fragment", "Motif", "Count", "Annotation", "Coverage")
    for table in tables:
        res = get_table_size(cur, table)
        print(f"{table}: {res}")
    
    ### show rows
    print("\nShow table: Sample...")
    rows = get_table_rows(cur, "Sample")
    for row in rows:
        print(row)
    
    tables = ("Fragment", "Motif", "Count", "Annotation", "Coverage")
    for table in tables:
        print(f"\nShow table: {table}...")
        rows = get_table_rows(cur, table)
        rows = it.islice(rows, 5)
        for row in rows:
            print(row)
    
    ### close database connection
    con.commit()
    con.close()
    
if __name__ == "__main__":
    args = parse_args()
    main(**vars(args))