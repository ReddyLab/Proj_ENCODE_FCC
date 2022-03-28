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

### parse argument
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('sample',    type=str, help='Sample')
parser.add_argument('replicate', type=str, help='Replicate')
args = parser.parse_args()

##################################################
### Global variables
### ++++++++++++++++++++++++++++++++++++++++++++++

### samples
SAMPLE    = args.sample
REPLICATE = args.replicate

### set file directory
FD_INP = os.path.join(FD_RES, "source", "starrseq")
FD_OUT = os.path.join(FD_RES, "KS91_K562_ASTARRseq", "fragment")

### set file name (INPUT)
### KS91_K562_hg38_ASTARRseq_Input_rep1.masked.dups_marked.GATA1.fragment_counts.stranded.bed
#FN_INP = f"KS91_K562_hg38_ASTARRseq_{SAMPLE}_{REPLICATE}.masked.dups_marked.GATA1.fragment_counts.unstranded.bed"
#FN_OUT = f"KS91_K562_hg38_ASTARRseq_{SAMPLE}_{REPLICATE}.GATA1.unstranded.bed"

### set file name (OUTPUT)
### KS91_K562_hg38_ASTARRseq_Output_rep1.f3q10.sorted.with_umis.dups_marked.GATA1.fragment_counts.unstranded.bed
FN_INP = f"KS91_K562_hg38_ASTARRseq_{SAMPLE}_{REPLICATE}.f3q10.sorted.with_umis.dups_marked.GATA1.fragment_counts.unstranded.bed"
FN_OUT = f"KS91_K562_hg38_ASTARRseq_{SAMPLE}_{REPLICATE}.GATA1.unstranded.bed"

### set file path
FP_INP = os.path.join(FD_INP, FN_INP)
FP_OUT = os.path.join(FD_OUT, FN_OUT)

### show info
print("Global variables:")
print("Sample:      ", SAMPLE)
print("Replicate:   ", REPLICATE)
print("Input  file: ", FP_INP)
print("Output file: ", FP_OUT)
print()

##################################################
### Helper function
### ++++++++++++++++++++++++++++++++++++++++++++++

### helper function to process each row
def prep_line(line):
    """..."""
    lst = line.strip().split('\t')
    count = int(lst[4])
    line  = '\t'.join(lst[:4])
    return count, line

##################################################
### Main
### ++++++++++++++++++++++++++++++++++++++++++++++

with open(FP_INP, 'r') as finp, open(FP_OUT, 'w') as fout:
    #n_line = 5
    #lines  = it.islice(finp, n_line)
    lines = finp
    for idx, line in enumerate(lines):
        count, line = prep_line(line)
        tmp = [line] * count
        tmp = "\n".join(tmp)
        fout.write(tmp)
        fout.write("\n")
    

