def get_frag_astarr(sample, fpath_db = FPATH_DB_ASTARR):
    """sample fragments from ATAC-STARR-seq with probability proportion to count"""
    with sqlite3.connect(fpath_db) as conn:
        ### query the fragment annotations
        cursor = conn.cursor()
        query  = f"""
            SELECT *
            FROM   Count Cnt
            WHERE  Cnt.sample = '{sample}'
            """
        cursor = cursor.execute(query)
        rows   = cursor
        
        ### generate fragments
        for row in rows:
            ### parse info
            frg, sample, count = row
            
            ### repeat the each fragment based on its count
            for _ in range(count):
                yield frg, sample
                
                
def get_frag_tmpra(fpath_db = FPATH_DB_TMPRA):
    """sample fragments from TileMPRA with probability proportion to fold change"""
    with sqlite3.connect(fpath_db) as conn:
        ### query the fragment annotations
        cursor = conn.cursor()
        query  = """
            SELECT Cnt.fragment, Cnt.count_input, Cnt.count_output, Cnt.log2fc 
            FROM   Count Cnt"""
        cursor = cursor.execute(query)
        rows   = cursor

        ### generate fragments
        for row in rows:
            ### parse info
            frg, inp, out, log2fc = row
            
            ### repeat the each fragment based on its ratio
            ratio = np.exp2(log2fc)
            count = np.ceil(ratio).astype(np.int)
            for _ in range(count):
                yield frg, inp, out, log2fc