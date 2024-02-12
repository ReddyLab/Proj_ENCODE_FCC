import os
import re
import csv
import itertools as it

### environment name
SERVER = "Singularity | singularity_proj_combeffect"
#SERVER = "Duke Server: DCC"
#SERVER = "Duke Server: HARDAC"

### set paths
FD_WORK = "/mount/work"
FD_RLAB = "/mount/reddylab"
FD_PRJ  = "/mount/project"

FD_SRC  = os.path.join(FD_WORK, "source")
FD_EXE  = os.path.join(FD_WORK, "exe")
FD_ANN  = os.path.join(FD_WORK, "annotation")
FD_RES  = os.path.join(FD_WORK, "out", "proj_combeffect_encode_fcc")

def show_env():
    print(f"You are in: {SERVER}")
    print(f"    BASE DIRECTORY:     {FD_WORK}") 
    print(f"    PATH OF SOURCE:     {FD_SRC}")
    print(f"    PATH OF EXECUTABLE: {FD_EXE}")
    print(f"    PATH OF ANNOTATION: {FD_ANN}")
    print(f"    PATH OF PROJECT:    {FD_PRJ}")
    print(f"    PATH OF RESULTS:    {FD_RES}")
    print()
    
def gen_lines(file, n_lines=10, delimiter='\t', remove_header=False):
    """generate lines lines from the file"""
    
    ### read lines using csv reader
    lines = csv.reader(file, delimiter=delimiter, quotechar='|')
    
    ### remove file header if needed
    if remove_header:
        next(lines)
    
    ### specify number of lines to generate
    lines = it.islice(lines, 0, n_lines)
    for line in lines:
        yield line
        
def get_sample(string):
    pattern = "(Input|Output)_rep."
    result  = re.search(pattern, string)
    if result:
        return result.group()
    else:
        return None