### basic
library("tidyverse")
library("vroom")
library("pryr")

### visualization
library("RColorBrewer")
library("cowplot")
library("gridExtra")
library("grid")

## main paths
FD_BASE="/data/reddylab/Kuei"
FD_WORK="/data/reddylab/Kuei/work"
FD_REPO="/data/reddylab/Kuei/repo"
FD_RLAB="/data/reddylab"

### set project related paths
FD_PRJ = file.path(FD_REPO, "Proj_CombEffect_ENCODE_FCC")
FD_DAT = file.path(FD_WORK, "proj_combeffect_encode_fcc", "data")
FD_RES = file.path(FD_WORK, "proj_combeffect_encode_fcc", "results")
FD_LOG = file.path(FD_WORK, "proj_combeffect_encode_fcc", "log")

### workspace info
SERVER = "Singularity: singularity_proj_encode_fcc"
#SERVER = "Duke Server: DCC"
#SERVER = "Duke Server: HARDAC"

### helper function to print out the path info
show_env = function(){
    cat("You are in", SERVER, "\n")
    cat("BASE DIRECTORY (FD_BASE):", FD_BASE, "\n")
    cat("WORK DIRECTORY (FD_WORK):", FD_WORK, "\n")
    cat("CODE DIRECTORY (FD_REPO):", FD_REPO, "\n")
    
    cat("PATH OF PROJECT (FD_PRJ):", FD_PRJ, "\n")
    cat("PATH OF RESULTS (FD_DAT):", FD_DAT, "\n")
    cat("PATH OF RESULTS (FD_RES):", FD_RES, "\n")
    cat("PATH OF LOG     (FD_LOG):", FD_LOG, "\n")
    
    cat("")
}
