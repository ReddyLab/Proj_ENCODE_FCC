### ++++++++++++++++++++++++++++++++++++++++++++++++++++
### Set environment
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### Hack to handle broekn pipes - IGNORE.
cleanup () {
    :
}
trap "cleanup" SIGPIPE

### Treat unset variables as an error, and immediately exit.
set -u

### workspace info
SERVER=Singularity

### main paths
FD_BASE=/data/reddylab/Kuei
FD_WORK=/data/reddylab/Kuei/out
FD_CODE=/data/reddylab/Kuei/code
FD_SING=/data/reddylab/Kuei/singularity
FD_RLAB=/data/reddylab

### set other working paths
FD_ANN=${FD_BASE}/annotation
FD_BIN=${FD_BASE}/bin
FD_SRC=${FD_BASE}/source
FD_BAC=${FD_BASE}/backup

### ++++++++++++++++++++++++++++++++++++++++++++++++++++
### Set relative paths specific for the projects
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### set project related paths
FD_PRJ=${FD_CODE}/Proj_CombEffect_ENCODE_FCC/notebooks
FD_RES=${FD_WORK}/proj_combeffect_encode_fcc/results
FD_LOG=${FD_WORK}/proj_combeffect_encode_fcc/log
FP_SIF=${FD_SING}/singularity_proj_combeffect.sif

### load helper functions
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
source ${SCRIPT_DIR}/config_func.sh

### helper function to print out the path info
show_env() {
    echo "You are on Duke Server: ${SERVER}"
    echo "BASE DIRECTORY:     ${FD_BASE}" 
    echo "WORK DIRECTORY:     ${FD_WORK}"
    echo "CODE DIRECTORY:     ${FD_CODE}"
    echo "SING DIRECTORY:     ${FD_SING}"
    echo "PATH OF SOURCE:     ${FD_SRC}"
    echo "PATH OF EXECUTABLE: ${FD_BIN}"
    echo "PATH OF ANNOTATION: ${FD_ANN}"
    echo "PATH OF PROJECT:    ${FD_PRJ}"
    echo "PATH OF RESULTS:    ${FD_RES}"
    echo
}