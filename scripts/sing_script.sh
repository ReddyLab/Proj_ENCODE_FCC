#!/bin/bash

### Source the configuration file
FP_CNF=/data/reddylab/Kuei/repo/Proj_ENCODE_FCC/config/config_project.sh
source ${FP_CNF}

### From the configuration file, Get the following:
### singularity file path and temporary directory
FP_SIF=${FP_PRJ_SIF}
FD_TMP=${FD_TEMP}

### Get the arguments
ARGS="$@"
#ARGS="${@:2}"

### Run the command in singularity environment
singularity exec   \
    --env NUMBA_CACHE_DIR=/tmp \
    -B ${FD_TMP}:/tmp \
    -B ${PWD}      \
    -B /data:/data \
    ${FP_SIF} ${ARGS}
