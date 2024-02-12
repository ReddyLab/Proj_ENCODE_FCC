#!/usr/bin/env python

"""Table information

TABLE: Sample
    sample,   TEXT PRIMARY KEY, 
    treatment TEXT,
    replicate TEXT,
    size      INTEGER

TABLE: Fragment(
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

TABLE: Motif(
    binding TEXT PRIMARY KEY, 
    chrom   TEXT,
    start   INTEGER,
    end     INTEGER,
    motif   TEXT,
    score   REAL

TABLE: Count (
    fragment TEXT, 
    sample   TEXT,
    count    INTEGER,
    FOREIGN KEY (fragment) REFERENCES Fragment (fragment),
    FOREIGN KEY (sample)   REFERENCES Sample   (sample)
            
TABLE: Annotation (
    fragment TEXT, 
    binding  TEXT,
    FOREIGN KEY (fragment) REFERENCES Fragment (fragment),
    FOREIGN KEY (binding)  REFERENCES Motif    (binding),
    UNIQUE (fragment, binding) ON CONFLICT IGNORE
            
TABLE: Coverage(
    chrom    TEXT,
    location INTEGER,
    depth    INTEGER,
    sample   TEXT,
    FOREIGN KEY (sample) REFERENCES Sample (sample)
"""

import sqlite3


def index_table_fragment(cursor):
    query  = "DROP INDEX IF EXISTS idx_frg_loc"
    cursor = cursor.execute(query)
    
    query  = "CREATE INDEX idx_frg_loc ON Fragment (start, end)"
    cursor = cursor.execute(query)
    return cursor

def index_table_motif(cursor):
    query  = "DROP INDEX IF EXISTS idx_mtf_loc"
    cursor = cursor.execute(query)
    query  = "DROP INDEX IF EXISTS idx_mtf"
    cursor = cursor.execute(query)
    
    query  = """CREATE INDEX idx_mtf_loc ON Motif (start, end)"""
    cursor = cursor.execute(query)
    query  = """CREATE INDEX idx_mtf ON Motif (motif)"""
    cursor = cursor.execute(query)
    return cursor
    
def index_table_count(cursor):
    query  = "DROP INDEX IF EXISTS idx_cnt_frg"
    cursor = cursor.execute(query)
    query  = "DROP INDEX IF EXISTS idx_cnt_sam"
    cursor = cursor.execute(query)
    
    query  = "CREATE INDEX idx_cnt_frg ON Count (fragment)"
    cursor = cursor.execute(query)
    query  = "CREATE INDEX idx_cnt_sam ON Count (sample)"
    cursor = cursor.execute(query)
    return cursor

def index_table_annotation(cursor):
    query  = "DROP INDEX IF EXISTS idx_ant_frg"
    cursor = cursor.execute(query)
    query  = "DROP INDEX IF EXISTS idx_ant_mtf"
    cursor = cursor.execute(query)
    
    query  = "CREATE INDEX idx_ant_frg ON Annotation (fragment)"
    cursor = cursor.execute(query)
    query  = "CREATE INDEX idx_ant_mtf ON Annotation (binding)"
    cursor = cursor.execute(query)
    return cursor

def index_table_coverage(cursor):
    query  = "DROP INDEX IF EXISTS idx_cov_loc"
    cursor = cursor.execute(query)
    
    query  = "CREATE INDEX idx_cov_loc ON Coverage (location)"
    cursor = cursor.execute(query)
    return cursor

dct_index_table = {
    "Fragment":   index_table_fragment,
    "Motif":      index_table_motif,
    "Count":      index_table_count,
    "Annotation": index_table_annotation,
    "Coverage":   index_table_coverage
}