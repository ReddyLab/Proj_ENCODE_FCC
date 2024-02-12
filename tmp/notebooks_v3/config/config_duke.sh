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

### ++++++++++++++++++++++++++++++++++++++++++++++++++++
### Identify the environment and set main working paths
###     Check which duke server I am at
###     set correct path based on the server I am at
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

if echo $(pwd -P) | grep -q "gpfs"; then
    ### workspace info
    SERVER=HARDAC
    NODE=all
   
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
fi

if echo $(pwd -P) | grep -q "hpc"; then
    ### workspace info
    SERVER=DCC
    NODE=scavenger
    
    FD_PREFIX="/hpc"
    FD_WORK=/work/kk319
    FD_CODE=${FD_PREFIX}/home/kk319/GitRepo
    FD_RLAB=${FD_PREFIX}/group/reddylab
    FD_SING=${FD_RLAB}/Kuei/singularity
    
    ### set working paths
    FD_ANN=${FD_RLAB}/Kuei/annotation
    FD_SRC=${FD_RLAB}/Kuei/source
    FD_EXE=${FD_RLAB}/Kuei/exe
fi

### ++++++++++++++++++++++++++++++++++++++++++++++++++++
### Set relative paths specific for the projects
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### set project related paths
FD_PRJ=${FD_CODE}/Proj_CombEffect_ENCODE_FCC
FD_RES=${FD_WORK}/proj_combeffect_encode_fcc
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

### ++++++++++++++++++++++++++++++++++++++++++++++++++++
### Set additional directories
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### fragments | region
FD_ALEX=/data/reddylab/Alex
FD_REGION=${FD_ALEX}/encode4_duke/ipynbs/jamborees/20211025_MPRA_STARR_Jamboree/data/gata1_myc/starrseq/fragments


### fragments | whole genome
FD_WGS_WSTARR=/data/reddylab/Alex/encode4_duke/data/starr_seq/fragments
FP_WGS_WSTARR=($(ls ${FD_WGS_WSTARR}/*.fragments.counts.txt.gz))

FD_WGS_ASTARR_INP=${FD_ALEX}/encode4_duke/processing/atac_seq/210401_KS91_K562ASTARR_NovaSeq.hg38-pe-blacklist-removal/merged2
FD_WGS_ASTARR_OUT=${FD_ALEX}/encode4_duke/processing/starr_seq/210401_KS91_K562ASTARR_NovaSeq.hg38-pe-umis

FP_WGS_ASTARR_INP=($(ls ${FD_WGS_ASTARR_INP}/*counts.txt.gz))
FP_WGS_ASTARR_OUT=($(ls ${FD_WGS_ASTARR_OUT}/*f3q10.fragments.counts.txt.gz))
FP_WGS_ASTARR=("${FP_WGS_ASTARR_INP[@]}" "${FP_WGS_ASTARR_OUT[@]}")

### peaks
FN_PEAKS_ASTARR_INP=KS91_K562_hg38_ASTARRseq_Input.all_reps.masked.union_narrowPeak.q5.bed