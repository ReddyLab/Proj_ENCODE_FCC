#!/bin/bash

### get file path
### Stackoverflow: how-can-i-get-the-source-directory-of-a-bash-script-from-within-the-script-itself
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
source ${SCRIPT_DIR}/config_duke.sh
 
### execute
singularity exec \
    -H ${PWD}:/home \
    -B ${FD_WORK}:/mount/work \
    -B ${FD_PRJ}:/mount/project \
    -B ${FD_RLAB}:/mount/reddylab \
    ${FD_SING}/singularity_proj_combeffect.sif "$@"

