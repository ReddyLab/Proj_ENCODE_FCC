##################################################
### Set environment
### ++++++++++++++++++++++++++++++++++++++++++++++

### basic
import sys
sys.path.append('/mount/project')
from config_sing import *

### update print
import itertools as it
from functools import partial
print = partial(print, flush=True)

### parse argument
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file_input',  type=str, help='Input file')
parser.add_argument('file_output', type=str, help='Output file')
args = parser.parse_args()

##################################################
### Global variables
### ++++++++++++++++++++++++++++++++++++++++++++++

### get the file path
FP_INP = args.file_input
FP_OUT = args.file_output

### show info
#print("Global variables:")
#print("Input  file: ", FP_INP)
#print("Output file: ", FP_OUT)
#print()


##################################################
### Helper function
### ++++++++++++++++++++++++++++++++++++++++++++++

### helper function to process each row
def prep_line(line):
    """preprocess line and get count"""
    ### parse info
    chrom, start, end, name, count, strand = line.strip().split('\t')
    
    ### get new line
    line  = [chrom, start, end, name, "1", strand]
    line  = '\t'.join(line)

    ### get count
    count = int(count)
    
    return count, line

##################################################
### Main
### ++++++++++++++++++++++++++++++++++++++++++++++

with open(FP_INP, 'r') as finp, open(FP_OUT, 'w') as fout:
    #n_line = 10
    #lines  = it.islice(finp, n_line)
    lines = finp
    for idx, line in enumerate(lines):
        count, line = prep_line(line)
        tmp = [line] * count
        tmp = "\n".join(tmp)
        fout.write(tmp)
        fout.write("\n")