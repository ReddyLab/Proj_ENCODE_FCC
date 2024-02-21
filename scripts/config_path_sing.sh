### set workspace info
SERVER="Singularity: singularity_proj_encode_fcc"
PROJECT="ENCODE FCC"

### set work folder
FD_RLAB="/mount/reddylab"
FD_BASE="/mount"

FD_WORK="${FD_BASE}/work"
FD_DATA="${FD_BASE}/data"
FD_REPO="${FD_BASE}/repo"


### set project folders
FD_PRJ=${FD_REPO}/Proj_CombEffect_ENCODE_FCC

FD_RES=${FD_PRJ}/results
FD_EXE=${FD_PRJ}/scripts
FD_DAT=${FD_PRJ}/data
FD_NBK=${FD_PRJ}/notebooks
FD_DOC=${FD_PRJ}/docs
FD_LOG=${FD_PRJ}/log
FD_APP=${FD_PRJ}/app
FD_REF=${FD_PRJ}/references




### fun show environment
show_env() {
    echo "You are working on             ${SERVER}"
    echo "BASE DIRECTORY (FD_BASE):      ${FD_BASE}" 
    echo "REPO DIRECTORY (FD_REPO):      ${FD_REPO}"
    echo "WORK DIRECTORY (FD_WORK):      ${FD_WORK}"
    echo "DATA DIRECTORY (FD_DATA):      ${FD_DATA}"
    echo
    echo "You are working with           ${PROJECT}"
    echo "PATH OF PROJECT (FD_PRJ):      ${FD_PRJ}"
    echo "PROJECT RESULTS (FD_RES):      ${FD_RES}"
    echo "PROJECT SCRIPTS (FD_EXE):      ${FD_EXE}"
    echo "PROJECT DATA    (FD_DAT):      ${FD_DAT}"
    echo "PROJECT NOTE    (FD_NBK):      ${FD_NBK}"
    echo "PROJECT DOCS    (FD_DOC):      ${FD_DOC}"
    echo "PROJECT LOG     (FD_LOG):      ${FD_LOG}"
    echo "PROJECT APP     (FD_APP):      ${FD_APP}"
    echo "PROJECT REF     (FD_REF):      ${FD_REF}"
    echo
}
