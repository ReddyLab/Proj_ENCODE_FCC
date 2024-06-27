#!/bin/bash

#########################################
### ...
### =====================================

### get path of the script
### Stackoverflow: how-can-i-get-the-source-directory-of-a-bash-script-from-within-the-script-itself
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

### get helper functions
source ${SCRIPT_DIR}/config_venv_wrapper.sh
source ${SCRIPT_DIR}/config_func.sh

### Hack to handle broken pipes - IGNORE.
### ex: suppress errors in `zcat ... | head`
cleanup () {
    :
}
trap "cleanup" SIGPIPE

#########################################
### Identify and set environment
### =====================================
ARG_SERVER=$(fun_get_server)

### if identify Singularity environment
if [[ ${ARG_SERVER} == "Singularity" ]]; then

    ### set workspace env
    source ${SCRIPT_DIR}/config_path_sing.sh
    
fi

### if identify Duke HARDAC environment 
if [[ ${ARG_SERVER} == "HARDAC" ]]; then

    ### set workspace env
    NODE=all
    source ${SCRIPT_DIR}/config_path_duke_hardac.sh
    
    ### APP: Container
    export PATH="${FD_EXE}/app_duke_hardac:$PATH"
    
    ### APP: UCSC
    export PATH="/data/common/shared_conda_envs/ucsc/bin:$PATH"
fi

### if identify Duke DCC environment
