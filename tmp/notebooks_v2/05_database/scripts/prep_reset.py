import sqlite3

def reset_table_sample(cursor):
    query = "DROP TABLE IF EXISTS Sample"
    cursor = cursor.execute(query)
    return cursor
    
def reset_table_fragment(cursor):
    query = "DROP TABLE IF EXISTS Fragment"
    cursor = cursor.execute(query)
    return cursor
    

def reset_table_motif(cursor):
    query = "DROP TABLE IF EXISTS Motif"
    cursor = cursor.execute(query)
    return cursor
    

def reset_table_count(cursor):
    query = "DROP TABLE IF EXISTS Count"
    cursor = cursor.execute(query)
    return cursor
    

def reset_table_annotate(cursor):
    query = "DROP TABLE IF EXISTS Annotation"
    cursor = cursor.execute(query)
    return cursor
    

def reset_table_coverage(cursor):
    query = "DROP TABLE IF EXISTS Coverage"
    cursor = cursor.execute(query)
    return cursor
    