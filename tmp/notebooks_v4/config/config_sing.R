### basic
library("tidyverse")
library("vroom")
library("pryr")

### visualization
library("RColorBrewer")
library("cowplot")
library("gridExtra")
library("grid")

### workspace info
SERVER = "Singularity: singularity_proj_encode_fcc"
#SERVER = "Duke Server: DCC"
#SERVER = "Duke Server: HARDAC"

## main paths
FD_BASE="/data/reddylab/Kuei"
FD_WORK="/data/reddylab/Kuei/out"
FD_CODE="/data/reddylab/Kuei/code"
FD_SING="/data/reddylab/Kuei/singularity"
FD_RLAB="/data/reddylab"

### set other working paths
FD_BIN = file.path(FD_BASE, "bin")
FD_ANN = file.path(FD_BASE, "annotation")

### set project related paths
FD_PRJ = file.path(FD_CODE, "Proj_CombEffect_ENCODE_FCC")
FD_RES = file.path(FD_WORK, "proj_combeffect_encode_fcc")
FD_LOG = file.path(FD_WORK, "proj_combeffect_encode_fcc", "log")
FP_SIF = file.path(FD_SING, "ingularity_proj_combeffect.sif")

### helper function to print out the path info
show_env = function(){
    cat("You are in", SERVER, "\n")
    cat("BASE DIRECTORY (FD_BASE):", FD_BASE, "\n")
    cat("WORK DIRECTORY (FD_WORK):", FD_WORK, "\n")
    cat("CODE DIRECTORY (FD_CODE):", FD_CODE, "\n")
    
    cat("PATH OF PROJECT (FD_PRJ):", FD_PRJ, "\n")
    cat("PATH OF RESULTS (FD_RES):", FD_RES, "\n")
    cat("PATH OF LOG     (FD_LOG):", FD_LOG, "\n")
    
    #cat("PATH OF EXECUTABLE:", FD_BIN,  "\n")
    #cat("PATH OF ANNOTATION:", FD_ANN,  "\n")
    cat("")
}
