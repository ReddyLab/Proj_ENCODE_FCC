### set correct path based on the server I am at
FD_WORK=/mount/work
FD_RLAB=/mount/reddylab
FD_PRJ=/mount/project

### set working paths
FD_SRC=${FD_WORK}/source
FD_EXE=${FD_WORK}/exe
FD_ANN=${FD_WORK}/annotation

### set project related paths
FD_RES=${FD_WORK}/out/proj_combeffect_encode_fcc
FD_LOG=${FD_RES}/log

show_env() {
    echo "You are in singularity_proj_combeffect"
    echo "BASE DIRECTORY:     ${FD_WORK}" 
    echo "PATH OF SOURCE:     ${FD_SRC}"
    echo "PATH OF EXECUTABLE: ${FD_EXE}"
    echo "PATH OF ANNOTATION: ${FD_ANN}"
    echo "PATH OF PROJECT:    ${FD_PRJ}"
    echo "PATH OF RESULTS:    ${FD_RES}"
    echo
}

### load helper functions
source ${FD_PRJ}/config_func.sh