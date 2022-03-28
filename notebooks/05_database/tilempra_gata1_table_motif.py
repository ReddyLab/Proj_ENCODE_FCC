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

### parse argument
import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    'chrom', 
    type=str, 
    help='Chromsome')
args = parser.parse_args()

##################################################
### Global variables
### ++++++++++++++++++++++++++++++++++++++++++++++

### chromsome
CHROM = args.chrom

### file path of fragment database
fdiry = os.path.join(FD_RES, "Tewhey_K562_TileMPRA", 'database')
fname = "fragment_tilempra_gata1.db"
FPATH_DB = os.path.join(fdiry, fname)

### set name of table files
fdiry = os.path.join(FD_ANN, "motif_cluster_jvierstra", "hg38_archetype_motifs_v1")
fname = f"{CHROM}_rm_mouse_merge.bed.gz"
FPATH_MTF = os.path.join(fdiry, fname)

### show info
print("Global variables:")
print("Chromsome:      ", CHROM)
print("Database:       ", FPATH_DB)
print("Table file name:", FPATH_MTF)
print()

##################################################
### Helper function
### ++++++++++++++++++++++++++++++++++++++++++++++

### helper function to process each row
def prep_line(line):
    lst = line.decode('ASCII').strip().split('\t')
    key = "_".join(lst[0:(len(lst)-1)])
    return [key] + lst

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

query_reset_table = "DROP TABLE IF EXISTS Motif"
query_reset_index = "DROP INDEX IF EXISTS idx_motif_loc"

query_table = """
    CREATE TABLE IF NOT EXISTS Motif(
        binding TEXT PRIMARY KEY, 
        chrom   TEXT,
        start   INTEGER,
        end     INTEGER,
        motif   TEXT,
        score   REAL
    );"""

query_index  = """CREATE INDEX idx_motif_loc ON Motif (start, end)"""
query_insert = """
    INSERT OR IGNORE INTO Motif 
        (binding,chrom,start,end,motif,score)
    VALUES 
        (?,?,?,?,?,?)
    """

##################################################
### Create Annotation Table
### ++++++++++++++++++++++++++++++++++++++++++++++

### init
fpath_db = FPATH_DB
fpath_gz = FPATH_MTF
count_tot = 0


with sqlite3.connect(fpath_db) as conn:
    ### reset
    cursor = conn.cursor()
    query  = query_reset_table
    cursor = cursor.execute(query)
    query  = query_reset_index
    cursor = cursor.execute(query)

    ### create table 
    cursor = conn.cursor()
    query  = query_table
    cursor = cursor.execute(query)
    
    with gzip.open(fpath_gz, "rb") as file:
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
        
    ### show results after looping all files
    print("\n# Annotation (Total):", count_tot)

    ### create index
    print("Create index...")
    cursor = conn.cursor()
    query  = query_index
    cursor = cursor.execute(query)
    print("Done!\n")

with sqlite3.connect(fpath_db) as conn:
    ### show created table info
    cursor = conn.cursor()
    query = "select count(*) from Motif"
    cursor.execute(query)
    print("#Rows Table:", cursor.fetchall())
    
    ### show that the table is created
    cursor = conn.cursor()
    cursor = cursor.execute("SELECT * FROM Motif")
    print("Show the first 10 lines in the table:")
    rows   = it.islice(cursor, 10)
    for row in rows:
        print(row)
    
    