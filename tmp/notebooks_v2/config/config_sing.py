### basic
import numpy     as np
import pandas    as pd
import itertools as it
import matplotlib.pyplot as plt
import os, sys, time, gzip, glob

from collections import Counter
from functools   import partial, reduce

###
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
    print("Library imported:")
    print("    numpy, pandas, itertools,")
    print("    os, sys, time, gzip, glob,")
    print("    functools.partial/reduce,")
    print("    collections.Counter,")
    print("    matplotlib.pyplot")
    print()