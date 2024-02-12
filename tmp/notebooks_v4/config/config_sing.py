import os, sys


###
SERVER = "Singularity: singularity_proj_encode_fcc"

### main paths
FD_BASE="/data/reddylab/Kuei"
FD_WORK="/data/reddylab/Kuei/out"
FD_CODE="/data/reddylab/Kuei/code"
FD_SING="/data/reddylab/Kuei/singularity"
FD_RLAB="/data/reddylab"

### set project related paths
FD_PRJ = os.path.join(FD_CODE, "Proj_CombEffect_ENCODE_FCC")
FD_RES = os.path.join(FD_WORK, "proj_combeffect_encode_fcc")
FD_LOG = os.path.join(FD_WORK, "proj_combeffect_encode_fcc", "log")
FP_SIF = os.path.join(FD_SING, "ingularity_proj_combeffect.sif")

### helper function to print out the path info
def show_env():
    print("You are in", SERVER)
    print("BASE DIRECTORY (FD_BASE):", FD_BASE)
    print("WORK DIRECTORY (FD_WORK):", FD_WORK)
    print("CODE DIRECTORY (FD_CODE):", FD_CODE)
    
    print("PATH OF PROJECT (FD_PRJ):", FD_PRJ)
    print("PATH OF RESULTS (FD_RES):", FD_RES)
    print("PATH OF LOG     (FD_LOG):", FD_LOG)
    
    print("")
