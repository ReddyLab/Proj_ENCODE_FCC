### import library: basic
library("tidyverse")
library("vroom")
library("pryr")

### import library: visualization
library("RColorBrewer")
library("cowplot")
library("gridExtra")
library("grid")

### workspace info
PROJECT = "ENCODE FCC"
SERVER  = "Singularity: singularity_proj_encode_fcc"
#SERVER = "Duke Server: DCC"
#SERVER = "Duke Server: HARDAC"

### set workspace info
SERVER="Singularity"
PROJECT="ENCODE FCC"

### main paths
FD_BASE="/mount"
FD_WORK="/mount/work"
FD_REPO="/mount/repo"
FD_DATA="/mount/data"
FD_RLAB="/mount/reddylab"

### set project related paths
FD_PRJ = file.path(FD_REPO, "Proj_CombEffect_ENCODE_FCC")

FD_RES = file.path(FD_PRJ,  "results")
FD_EXE = file.path(FD_PRJ,  "scripts")
FD_DAT = file.path(FD_PRJ,  "data")
FD_NBK = file.path(FD_PRJ,  "notebooks")
FD_DOC = file.path(FD_PRJ,  "docs")
FD_LOG = file.path(FD_PRJ,  "log")
FD_APP = file.path(FD_PRJ,  "app")
FD_REF = file.path(FD_PRJ,  "references")

### helper function to print out the path info
show_env = function(){
    cat("You are working on       ", SERVER,  "\n")
    cat("BASE DIRECTORY (FD_BASE):", FD_BASE, "\n") 
    cat("REPO DIRECTORY (FD_REPO):", FD_REPO, "\n")
    cat("WORK DIRECTORY (FD_WORK):", FD_WORK, "\n")
    cat("DATA DIRECTORY (FD_DATA):", FD_DATA, "\n")
    cat("\n")
    
    cat("You are working with     ", PROJECT, "\n") 
    cat("PATH OF PROJECT (FD_PRJ):", FD_PRJ,  "\n") 
    cat("PROJECT RESULTS (FD_RES):", FD_RES,  "\n") 
    cat("PROJECT SCRIPTS (FD_EXE):", FD_EXE,  "\n") 
    cat("PROJECT DATA    (FD_DAT):", FD_DAT,  "\n") 
    cat("PROJECT NOTE    (FD_NBK):", FD_NBK,  "\n") 
    cat("PROJECT DOCS    (FD_DOC):", FD_DOC,  "\n") 
    cat("PROJECT LOG     (FD_LOG):", FD_LOG,  "\n") 
    cat("PROJECT APP     (FD_APP):", FD_APP,  "\n") 
    cat("PROJECT REF     (FD_REF):", FD_REF,  "\n") 
    cat("\n")
}

