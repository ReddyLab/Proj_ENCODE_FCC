#!/bin/bash

### Source the configuration file
FP_CNF=/data/reddylab/Kuei/repo/Proj_ENCODE_FCC/config/config_project.sh
source ${FP_CNF}

### From the configuration file, Get the singularity file path
FP_SIF=${FP_PRJ_SIF}

### Set home and port for jupyter
FD_HOME=${FD_SING}/home
NUM_PORT=9220

### Run jupyter in singularity environment
singularity exec \
    -H ${FD_HOME}:/home \
    -B ${FD_REPO}:/mount/repo \
    -B ${FD_WORK}:/mount/work \
    -B ${FD_DATA}:/mount/data \
    -B ${FD_RLAB}:/mount/reddylab \
    -B /data:/data \
    ${FP_SIF} \
    jupyter lab --NotebookApp.token="543@Psk" --NotebookApp.notebook_dir=/home --no-browser --ip=0.0.0.0 --port=${NUM_PORT}