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
fdiry = os.path.join(FD_RES, "KS91_K562_ASTARRseq", 'database')
fname = "fragment_astarr_gata1.db"
FPATH_DB = os.path.join(fdiry, fname)

### file dir  of table
FDIRY_IN = os.path.join(FD_RES, "KS91_K562_ASTARRseq", "fragment_nuc")

### set Samples
fun     = np.core.defchararray.add
idx     = np.arange(1,6).astype("str")
INPUT   = reduce(fun, ["Input_rep", idx])
idx     = np.arange(1,5).astype("str")
OUTPUT  = reduce(fun, ["Output_rep", idx])
SAMPLES = np.concatenate([INPUT, OUTPUT])

### show info
print("Global variables:")
print("Database:       ", FPATH_DB)
print("Table directory:", FDIRY_IN)
print()

##################################################
### Helper function
### ++++++++++++++++++++++++++++++++++++++++++++++

def prep_line(line):
    lst = line.decode('ASCII').strip().split('\t')  
    key = "_".join(lst[0:3])
    val = lst[0:3] + lst[5:-1]
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

query_reset_table = "DROP TABLE IF EXISTS Fragment"
query_reset_index = "DROP INDEX IF EXISTS idx_frag_loc"

query_table = ("""
    CREATE TABLE IF NOT EXISTS Fragment(
        fragment TEXT PRIMARY KEY, 
        chrom    TEXT,
        start    INTEGER,
        end      INTEGER,
        pct_at   REAL,
        pct_gc   REAL,
        num_A    INTEGER,
        num_C    INTEGER,
        num_G    INTEGER,
        num_T    INTEGER,
        num_N    INTEGER,
        num_oth  INTEGER
    );""")

query_index  = """CREATE INDEX idx_frag_loc ON Fragment (start, end)"""
query_insert = ("""
    INSERT OR IGNORE INTO Fragment
        (fragment, chrom, start, end, pct_at, pct_gc,
         num_A, num_C, num_G, num_T, num_N, num_oth) 
    VALUES 
        (?,?,?,?,?,?,?,?,?,?,?,?)
    """)

##################################################
### Create Table
### ++++++++++++++++++++++++++++++++++++++++++++++

### init
fdiry_in = FDIRY_IN
fpath_db = FPATH_DB
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
    
    ### loop through each fragment bed files
    for sample in SAMPLES:
        ### init
        fname_in = f"KS91_K562_hg38_ASTARRseq*{sample}*GATA1*.bed.gz"
        fglob_in = os.path.join(fdiry_in, fname_in)
        fpath_in = glob.glob(fglob_in)[0]
         
        ### show progress
        print(fpath_in)

        ### read file
        with gzip.open(fpath_in, "rb") as file:
            ### init
            header = file.readline()
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

    ### create index
    print("Create index...")
    cursor = conn.cursor()
    query  = query_index
    cursor = cursor.execute(query)
    print("Done!\n")

with sqlite3.connect(fpath_db) as conn:
    ### show created table info
    cursor = conn.cursor()
    query = "select count(*) from Fragment"
    cursor.execute(query)
    print("#Rows Table:", cursor.fetchall())
    
    ### show that the table is created
    cursor = conn.cursor()
    cursor = cursor.execute("SELECT * FROM Fragment")
    print("Show the first 10 lines in the table:")
    rows   = it.islice(cursor, 10)
    for row in rows:
        print(row)