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
FDIRY_IN = os.path.join(FD_RES, "Tewhey_K562_TileMPRA", "annotation")
FNAME_IN = "Tile_K562_20210130.GATA1.unstranded.bed.gz"

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
    ### decode
    lst = line.decode('ASCII').strip().split('\t')
    
    ### parse info and get fragment and motif ID
    fragment = "_".join(lst[:3])
    binding  = "_".join(lst[4:8])
    overlap  = int(lst[-1])
    
    ### calc motif lengths
    #mtf_len  = int(lst[6]) - int(lst[5])
    #return mtf_len == overlap, fragment, binding
    #if mtf_len == overlap:
    #    return fragment, binding
    return fragment, binding

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

query_reset_table = "DROP TABLE IF EXISTS Annotation"
query_reset_index = "DROP INDEX IF EXISTS idx_annot_frag"

query_table = """
    CREATE TABLE IF NOT EXISTS Annotation (
        fragment TEXT, 
        binding  TEXT,
        FOREIGN KEY (fragment) REFERENCES Fragment (fragment),
        FOREIGN KEY (binding)  REFERENCES Motif    (binding),
        UNIQUE (fragment, binding) ON CONFLICT IGNORE
    );"""

query_index = "CREATE INDEX idx_annot_frag ON Annotation (fragment)"

query_insert = """
    INSERT OR IGNORE INTO Annotation
        (fragment, binding)
    VALUES 
        (?,?)
    """

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
    query  = query_reset_index
    cursor = cursor.execute(query)

    ### create table 
    cursor = conn.cursor()
    query  = query_table
    cursor = cursor.execute(query)
    
    ### show progress
    print(fpath_in)

    ### read file
    with gzip.open(fpath_in, "rb") as file:
        ### init
        count = 0

        ### set query
        query = query_insert

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

    ### create index
    print("Create index...")
    cursor = conn.cursor()
    query  = query_index
    cursor = cursor.execute(query)
    print("Done!\n")

#with sqlite3.connect(fpath_db) as conn:
    ### show created table info
    cursor = conn.cursor()
    query = "select count(*) from Annotation"
    cursor.execute(query)
    print("#Rows Table:", cursor.fetchall())
    
    ### show that the table is created
    cursor = conn.cursor()
    cursor = cursor.execute("SELECT * FROM Annotation")
    rows   = it.islice(cursor, 10)
    for row in rows:
        print(row)
    
