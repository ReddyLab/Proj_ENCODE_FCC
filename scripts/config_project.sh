### get path of the script
### Stackoverflow: how-can-i-get-the-source-directory-of-a-bash-script-from-within-the-script-itself
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

### set environment
source ${SCRIPT_DIR}/config_path_wrapper.sh
source ${SCRIPT_DIR}/config_func.sh

### set project folders
PROJECT="ENCODE FCC"
FD_PRJ=${FD_REPO}/Proj_CombEffect_ENCODE_FCC

FD_RES=${FD_PRJ}/results
FD_EXE=${FD_PRJ}/scripts
FD_DAT=${FD_PRJ}/data
FD_NBK=${FD_PRJ}/notebooks
FD_DOC=${FD_PRJ}/docs
FD_LOG=${FD_PRJ}/log
FD_APP=${FD_PRJ}/app
FD_REF=${FD_PRJ}/references

### set singularity
FP_PRJ_SIF=${FD_APP}/singularity_proj_encode_fcc.sif

### fun show environment
show_env() {
    echo "You are working on        ${SERVER}"
    echo "BASE DIRECTORY (FD_BASE): ${FD_BASE}" 
    echo "REPO DIRECTORY (FD_REPO): ${FD_REPO}"
    echo "WORK DIRECTORY (FD_WORK): ${FD_WORK}"
    echo "DATA DIRECTORY (FD_DATA): ${FD_DATA}"
    echo "CONTAINER DIR. (FD_SING): ${FD_SING}"
    echo
    echo "You are working with      ${PROJECT}"
    echo "PATH OF PROJECT (FD_PRJ): ${FD_PRJ}"
    echo "PROJECT RESULTS (FD_RES): ${FD_RES}"
    echo "PROJECT SCRIPTS (FD_EXE): ${FD_EXE}"
    echo "PROJECT DATA    (FD_DAT): ${FD_DAT}"
    echo "PROJECT NOTE    (FD_NBK): ${FD_NBK}"
    echo "PROJECT DOCS    (FD_DOC): ${FD_DOC}"
    echo "PROJECT LOG     (FD_LOG): ${FD_LOG}"
    echo "PROJECT APP     (FD_APP): ${FD_APP}"
    echo "PROJECT REF     (FD_REF): ${FD_REF}"
    echo "PROJECT IMAGE   (FP_SIF): ${FP_SIF}"
    echo
}