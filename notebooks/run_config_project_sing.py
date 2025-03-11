import sys, os

PROJECT = "ENCODE FCC"
SERVER  = "Singularity: singularity_proj_encode_fcc"

FD_RLAB="/data/reddylab"
FD_BASE="/data/reddylab/Kuei"
FD_REPO="/data/reddylab/Kuei/repo"
FD_WORK="/data/reddylab/Kuei/work"
FD_DATA="/data/reddylab/Kuei/data"

### set project related paths
FD_PRJ = os.path.join(FD_REPO, "Proj_ENCODE_FCC")

FD_RES = os.path.join(FD_PRJ, "results")
FD_EXE = os.path.join(FD_PRJ, "scripts")
FD_DAT = os.path.join(FD_PRJ, "data")
FD_NBK = os.path.join(FD_PRJ, "notebooks")
FD_DOC = os.path.join(FD_PRJ, "docs")
FD_LOG = os.path.join(FD_PRJ, "log")
FD_REF = os.path.join(FD_PRJ, "references")

def show_env():
    print("You are working on       ", SERVER)
    print("BASE DIRECTORY (FD_BASE):", FD_BASE) 
    print("REPO DIRECTORY (FD_REPO):", FD_REPO)
    print("WORK DIRECTORY (FD_WORK):", FD_WORK)
    print("DATA DIRECTORY (FD_DATA):", FD_DATA)
    print("\n")
    
    print("You are working with     ", PROJECT) 
    print("PATH OF PROJECT (FD_PRJ):", FD_PRJ) 
    print("PROJECT RESULTS (FD_RES):", FD_RES) 
    print("PROJECT SCRIPTS (FD_EXE):", FD_EXE) 
    print("PROJECT DATA    (FD_DAT):", FD_DAT) 
    print("PROJECT NOTE    (FD_NBK):", FD_NBK) 
    print("PROJECT DOCS    (FD_DOC):", FD_DOC) 
    print("PROJECT LOG     (FD_LOG):", FD_LOG)  
    print("PROJECT REF     (FD_REF):", FD_REF) 
    print("")