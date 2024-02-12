##################################################
### Set environment
### ++++++++++++++++++++++++++++++++++++++++++++++

### basic
import sys
sys.path.append('/mount/project')
from config_sing import *

### update print
from functools import partial
print = partial(print, flush=True)

### specific tools
from functools import reduce
import itertools as it
import sqlite3
# https://stackoverflow.com/questions/49456158/integer-in-python-pandas-becomes-blob-binary-in-sqlite
sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))

##################################################
### Global variables
### ++++++++++++++++++++++++++++++++++++++++++++++

### file path of fragment database
fdiry = os.path.join(FD_RES, "Tewhey_K562_TileMPRA", 'database')
fname = "fragment_tilempra_gata1.db"
FPATH_DB = os.path.join(fdiry, fname)

### file dir  of table
FDIRY_IN = os.path.join(FD_RES, "Tewhey_K562_TileMPRA", "count")
FNAME_IN = "Tile_K562_20210130.GATA1.unstranded.bed"

### show info
print("Global variables:")
print("Database:       ", FPATH_DB)
print("Table directory:", FDIRY_IN)
print("Table file name:", FNAME_IN)
print()

##################################################
### Helper function
### ++++++++++++++++++++++++++++++++++++++++++++++

### helper function to process each row
def prep_line(line):
    """..."""
    ### parse info and get fragment and motif ID
    lst = line.strip().split('\t') 
    key = "_".join(lst[:3])
    val = lst[6:]
    
    return [key] + val

### helper function to get a chunk of file
def get_chunks(gen, rows=10000):
    """Divides the data into #rows in each list"""
    iterable = iter(gen)
    while True:
        x = list(it.islice(iterable, rows))
        if not x:
            return
        yield x

##################################################
### Set SQL query
### ++++++++++++++++++++++++++++++++++++++++++++++

query_reset_table = "DROP TABLE IF EXISTS Count"

query_table = """
    CREATE TABLE IF NOT EXISTS Count (
        fragment       TEXT PRIMARY KEY, 
        log2fc         REAL,
        count_input    REAL,
        count_output   REAL,
        log10pval      REAL,
        log10fdr       REAL,
        lfc_se         REAL,
        FOREIGN KEY (fragment) REFERENCES Fragment (fragment)
    );"""

query_insert = ("""INSERT OR IGNORE INTO Count
    (fragment, log2fc, count_input, count_output, log10pval, log10fdr, lfc_se)
    VALUES 
    (?,?,?,?,?,?,?)""")

##################################################
### Create Table
### ++++++++++++++++++++++++++++++++++++++++++++++

### init
fpath_in  = os.path.join(FDIRY_IN, FNAME_IN)
fpath_db  = FPATH_DB
count_tot = 0

with sqlite3.connect(fpath_db) as conn:
    ### reset
    cursor = conn.cursor()
    query  = query_reset_table
    cursor = cursor.execute(query)

    ### create table 
    cursor = conn.cursor()
    query  = query_table
    cursor = cursor.execute(query)
    
    ### show progress
    print(fpath_in)

    ### read file
    with open(fpath_in, "r") as file:
        ### init
        count  = 0

        ### set query
        query  = query_insert

        ### set lines and chunks
        #n_chunk = 3
        #n_lines = 10
        #lines   = it.islice(file, n_lines)
        lines   = file
        n_chunk = 1000000
        chunks  = get_chunks(lines, rows=n_chunk)
        
        for chunk in chunks:
            ### preprocess lines
            fun = prep_line
            lst = list(map(fun, chunk))

            ### insert
            cursor = cursor.executemany(query, lst)
            #for tmp in lst:
            #    print(tmp)
            #print("+++++++++++++++")

            ### count
            count_tot += len(lst)
            count     += len(lst)
        
        ### show results for each file
        print("# Rows:", count)

    ### show results after looping all files
    print("\n# Rows (Total):", count_tot)

with sqlite3.connect(fpath_db) as conn:
    ### show created table info
    cursor = conn.cursor()
    query = "select count(*) from Count"
    cursor.execute(query)
    print("#Rows Table:", cursor.fetchall())
    
    ### show that the table is created
    cursor = conn.cursor()
    cursor = cursor.execute("SELECT * FROM Count")
    print("Show the first 10 lines in the table:")
    rows   = it.islice(cursor, 10)
    for row in rows:
        print(row)