#!/bin/bash

### get file path
### Stackoverflow: how-can-i-get-the-source-directory-of-a-bash-script-from-within-the-script-itself
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
source ${SCRIPT_DIR}/config_project.sh
FP_SIF=${FP_PRJ_SIF}

### execute
singularity exec \
    -B ${FD_REPO}:/mount/repo \
    -B ${FD_WORK}:/mount/work \
    -B ${FD_DATA}:/mount/data \
    -B ${FD_RLAB}:/mount/reddylab \
    -B ${PWD}      \
    -B /data:/data \
    -B /gpfs:/gpfs \
    ${FP_SIF} \
    "$@"

# -H ${PWD}:/home \