### ====================================================
### Set environment
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### Hack to handle broekn pipes - IGNORE.
cleanup () {
    :
}
trap "cleanup" SIGPIPE

### Treat unset variables as an error, and immediately exit.
###     set -u          => Treat unset variables as an error when substituting
###     set -e          => Exit immediately if a command exits with a non-zero status
###     set -o pipefail => Exit immediately if any command in a pipeline exits with a non-zero status.
###                        Prevents errors in a pipeline from being masked
### Reference
###     https://jasonfleetwoodboldt.com/courses/shell-scripting/shell-scripting-set-euo-pipefail-failsafe/
###     https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425

#set -euo pipefail
set -u

### ====================================================
### Identify the environment and set main working paths
###     Check which duke server I am at
###     set correct path based on the server I am at
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### identify Duke HARDAC environment 
if echo $(pwd -P) | grep -q "gpfs"; then
    ### workspace info
    SERVER=HARDAC
    NODE=all
   
    ### main paths
    FD_BASE=/data/reddylab/Kuei
    FD_WORK=/data/reddylab/Kuei/out
    FD_CODE=/data/reddylab/Kuei/code
    FD_SING=/data/reddylab/Kuei/singularity
    FD_BACK=/data/reddylab/Kuei/backup
    FD_RLAB=/data/reddylab
    
    ### set other working paths
    FD_ANN=${FD_BASE}/annotation
    FD_BIN=${FD_BASE}/bin
    
fi

### identify Duke DCC  environment
### identify Duke DASH environment

### ====================================================
### Set relative paths specific for the projects
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### set project related paths
FD_PRJ=${FD_CODE}/Proj_CombEffect_ENCODE_FCC
FD_RES=${FD_WORK}/proj_combeffect_encode_fcc
FD_LOG=${FD_WORK}/proj_combeffect_encode_fcc/log
FP_SIF=${FD_SING}/singularity_proj_encode_fcc.sif

### load helpers
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
source ${SCRIPT_DIR}/config_func.sh
source ${SCRIPT_DIR}/config_path.sh

### ====================================================
### helper function to print out the path info
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

show_env() {
    echo "You are on Duke Server: ${SERVER}"
    echo "BASE DIRECTORY (FD_BASE): ${FD_BASE}" 
    echo "WORK DIRECTORY (FD_WORK): ${FD_WORK}"
    echo "CODE DIRECTORY (FD_CODE): ${FD_CODE}"
    echo "SING DIRECTORY (FD_SING): ${FD_SING}"
    
    echo "PATH OF PROJECT (FD_PRJ): ${FD_PRJ}"
    echo "PATH OF RESULTS (FD_RES): ${FD_RES}"
    echo "PATH OF LOG     (FD_LOG): ${FD_LOG}"
    echo
}

