import sqlite3

def get_table_rows(cursor, table_name):
    query  = f"SELECT * FROM {table_name}"
    cursor = cursor.execute(query)
    return cursor

def get_table_size(cursor, table_name):
    query  = f"SELECT count(*) FROM {table_name}"
    cursor = cursor.execute(query)
    return cursor.fetchall()[0][0]

def list_table(cursor):
    query  = "SELECT name FROM sqlite_master WHERE type ='table'"
    cursor = cursor.execute(query)
    return cursor.fetchall()

def list_index(cursor):
    query  = "SELECT name FROM sqlite_master WHERE type ='index'"
    cursor = cursor.execute(query)
    return cursor.fetchall()