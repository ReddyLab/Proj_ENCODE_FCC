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
FDIRY_IN = os.path.join(FD_RES, "KS91_K562_ASTARRseq", "count")

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

### helper function to process each row
def prep_line(line, sample):
    """parse info and arrange each row for table"""
    #lst = line.decode('ASCII').strip().split('\t')
    lst = line.strip().split('\t')

    ### parse info and get fragment and motif ID
    fragment = "_".join(lst[:3])
    count    = lst[-1]

    return fragment, sample, count

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
query_reset_index = "DROP INDEX IF EXISTS idx_count_sample"

query_table = """
    CREATE TABLE IF NOT EXISTS Count (
        fragment TEXT, 
        sample   TEXT,
        count    INTEGER,
        FOREIGN KEY (fragment) REFERENCES Fragment (fragment),
        FOREIGN KEY (sample)   REFERENCES Sample   (sample)
    );"""

query_index = "CREATE INDEX idx_count_sample ON Count (sample)"

query_insert = ("""INSERT OR IGNORE INTO Count
    (fragment, sample, count)
    VALUES 
    (?,?,?)""")


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
        fname_in = f"KS91_K562_hg38_ASTARRseq*{sample}*GATA1*.bed"
        fglob_in = os.path.join(fdiry_in, fname_in)
        fpath_in = glob.glob(fglob_in)[0]
         
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
                fun = partial(prep_line, sample=sample)
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
            print("# Fragments:", count)

    ### show results after looping all files
    print("\n# Fragments (Total):", count_tot)

    ### create index
    print("Create index...")
    cursor = conn.cursor()
    query  = query_index
    cursor = cursor.execute(query)
    print("Done!\n")

with sqlite3.connect(fpath_db) as conn:
    ### show created table info
    cursor = conn.cursor()
    query = "select count(*) from Count"
    cursor.execute(query)
    print("#Rows Table:", cursor.fetchall())
    
    ### show that the table is created
    #cursor = conn.cursor()
    #cursor = cursor.execute("SELECT * FROM Count")
    #for row in cursor.fetchall():
    #    print(row)
    