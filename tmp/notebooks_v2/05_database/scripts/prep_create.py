#!/usr/bin/env python

""" Short description of this Python module.
https://gist.github.com/NicolasBizzozzero/6d4ca63f8482a1af99b0ed022c13b041

TABLE: Sample
    sample    TEXT PRIMARY KEY, 
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

def create_table_sample(cursor):
    query = """
        CREATE TABLE IF NOT EXISTS Sample(
            sample    TEXT PRIMARY KEY, 
            treatment TEXT,
            replicate TEXT,
            size      INTEGER
        );"""
    cursor = cursor.execute(query)
    return cursor
    
def create_table_fragment(cursor):
    query = """
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
        );"""
    cursor = cursor.execute(query)
    return cursor
    
def create_table_motif(cursor):
    query = """
        CREATE TABLE IF NOT EXISTS Motif(
            binding TEXT PRIMARY KEY, 
            chrom   TEXT,
            start   INTEGER,
            end     INTEGER,
            motif   TEXT,
            score   REAL
        );"""
    cursor = cursor.execute(query)
    return cursor
    
def create_table_count(cursor):
    query = """
        CREATE TABLE IF NOT EXISTS Count (
            fragment TEXT, 
            sample   TEXT,
            count    INTEGER,
            FOREIGN KEY (fragment) REFERENCES Fragment (fragment),
            FOREIGN KEY (sample)   REFERENCES Sample   (sample)
        );"""
    cursor = cursor.execute(query)
    return cursor

def create_table_annotate(cursor):
    query = """
        CREATE TABLE IF NOT EXISTS Annotation (
            fragment TEXT, 
            binding  TEXT,
            FOREIGN KEY (fragment) REFERENCES Fragment (fragment),
            FOREIGN KEY (binding)  REFERENCES Motif    (binding),
            UNIQUE (fragment, binding) ON CONFLICT IGNORE
        );"""
    cursor = cursor.execute(query)
    return cursor
    
def create_table_coverage(cursor):
    query = """CREATE TABLE IF NOT EXISTS Coverage(
        chrom    TEXT,
        location INTEGER,
        depth    INTEGER,
        sample   TEXT,
        FOREIGN KEY (sample) REFERENCES Sample (sample)
        );"""
    cursor = cursor.execute(query)
    return cursor
    