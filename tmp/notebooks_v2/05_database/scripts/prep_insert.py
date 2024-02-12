#!/usr/bin/env python

"""Table information

TABLE: Sample
    sample,   TEXT PRIMARY KEY, 
    treatment TEXT,
    replicate TEXT,
    size      INTEGER

TABLE: Motif(
    binding TEXT PRIMARY KEY, 
    chrom   TEXT,
    start   INTEGER,
    end     INTEGER,
    motif   TEXT,
    score   REAL

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

def insert_table_sample(cursor, generator):
    query = "INSERT INTO Sample (sample, treatment, replicate, size) VALUES (?, ?, ?, ?)"
    cursor.executemany(query, generator)
    return cursor

def insert_table_fragment(cursor, generator):
    query ="""
        INSERT OR IGNORE INTO Fragment
            (fragment, chrom, start, end, pct_at, pct_gc,
             num_A, num_C, num_G, num_T, num_N, num_oth) 
        VALUES 
            (?,?,?,?,?,?,?,?,?,?,?,?);
        """
    cursor.executemany(query, generator)
    return cursor

def insert_table_motif(cursor, generator):
    query = """
        INSERT OR IGNORE INTO Motif 
            (binding,chrom,start,end,motif,score)
        VALUES 
            (?,?,?,?,?,?)
        """
    cursor.executemany(query, generator)
    return cursor

def insert_table_count(cursor, generator):
    query = """
        INSERT OR IGNORE INTO Count
            (fragment, sample, count)
        VALUES 
            (?,?,?)
        """
    cursor.executemany(query, generator)
    return cursor

def insert_table_annotation(cursor, generator):
    query = """
        INSERT OR IGNORE INTO Annotation
            (fragment, binding)
        VALUES 
            (?,?)
        """
    cursor.executemany(query, generator)
    return cursor

def insert_table_coverage(cursor, generator):
    query = """
        INSERT OR IGNORE INTO Coverage
            (chrom, location, depth, sample)
        VALUES 
            (?,?,?,?)
        """
    cursor.executemany(query, generator)
    return cursor

dct_insert_table = {
    "Sample":     insert_table_sample,
    "Fragment":   insert_table_fragment,
    "Motif":      insert_table_motif,
    "Count":      insert_table_count,
    "Annotation": insert_table_annotation,
    "Coverage":   insert_table_coverage
}