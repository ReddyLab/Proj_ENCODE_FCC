

### ++++++++++++++++++++++++++++++++++++++++++++++++++
### set workspace info
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SERVER="Duke Server: HARDAC"
PROJECT="ENCODE FCC"

### ++++++++++++++++++++++++++++++++++++++++++++++++++
### set work folder
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FD_RLAB="/data/reddylab"
FD_BASE="/data/reddylab/Kuei"

FD_WORK="${FD_BASE}/work"
FD_DATA="${FD_BASE}/data"
FD_REPO="${FD_BASE}/repo"
FD_SING="${FD_BASE}/container"

### ++++++++++++++++++++++++++++++++++++++++++++++++++
### set project folders
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FD_PRJ=${FD_REPO}/Proj_ENCODE_FCC

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
    echo "You are working on             ${SERVER}"
    echo "BASE DIRECTORY (FD_BASE):      ${FD_BASE}" 
    echo "REPO DIRECTORY (FD_REPO):      ${FD_REPO}"
    echo "WORK DIRECTORY (FD_WORK):      ${FD_WORK}"
    echo "DATA DIRECTORY (FD_DATA):      ${FD_DATA}"
    echo "CONTAINER DIR. (FD_SING):      ${FD_SING}"
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
    echo "PROJECT IMAGE   (FP_PRJ_SIF):  ${FP_PRJ_SIF}"
    echo
}

### ++++++++++++++++++++++++++++++++++++++++++++++++++
### addition: processed data
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### ReddyLab directory
FD_ALEX=/data/reddylab/Alex
FD_KEITH=/data/reddylab/Keith

### whole genome fragment counts of ATAC-STARR
FD_WGS_ASTARR_KS91_INP=${FD_ALEX}/encode4_duke/processing/atac_seq/210401_KS91_K562ASTARR_NovaSeq.hg38-pe-blacklist-removal
FD_WGS_ASTARR_KS91_OUT=${FD_ALEX}/encode4_duke/processing/starr_seq/210401_KS91_K562ASTARR_NovaSeq.hg38-pe-umis
FD_WGS_ASTARR_KS274_OUT=${FD_KEITH}/encode4_duke/processing/starr_seq/240311_KS274_ASTARR_Output_Nextseq-pe-umis

### whole genome fragment counts of WHG-STARR
FD_WGS_WSTARR=${FD_ALEX}/encode4_duke/data/starr_seq

### STARR-seq fragment counts for GATA/MYC regions
FD_ENCODE4_JAMBOREE_STARR=${FD_ALEX}/encode4_duke/ipynbs/jamborees/20211025_MPRA_STARR_Jamboree/data/gata1_myc/starrseq/fragments

### ++++++++++++++++++++++++++++++++++++++++++++++++++
### addition: processed data
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### whole genome fragment counts of WHG-STARR
FP_WGS_WSTARR=($(ls ${FD_WGS_WSTARR}/fragments/*.fragments.counts.txt.gz))

### whole genome fragment counts of ATAC-STARR
FP_WGS_ASTARR_KS91_INP_FRAGS=($(ls ${FD_WGS_ASTARR_KS91_INP}/merged2/*fragments.counts.txt.gz))
FP_WGS_ASTARR_KS91_INP_BWIGS=($(ls ${FD_WGS_ASTARR_KS91_INP}/merged2/*exclude_dups.cpm.bw))
FP_WGS_ASTARR_KS91_OUT_FRAGS=($(ls ${FD_WGS_ASTARR_KS91_OUT}/*.f3q10.fragments.counts.txt.gz))
FP_WGS_ASTARR_KS91_OUT_BWIGS=($(ls ${FD_WGS_ASTARR_KS91_OUT}/*.with_umis.dedup.cpm.bw))

FP_WGS_ASTARR_KS91=("${FP_WGS_ASTARR_KS91_INP_FRAGS[@]}" "${FP_WGS_ASTARR_KS91_INP_BWIGS[@]}" "${FP_WGS_ASTARR_KS91_OUT_FRAGS[@]}" "${FP_WGS_ASTARR_KS91_OUT_BWIGS[@]}")

FP_WGS_ASTARR_KS274_OUT_FRAGS=($(ls ${FD_WGS_ASTARR_KS274_OUT}/K562*.fragments.bedpe))
FP_WGS_ASTARR_KS274_OUT_BWIGS=($(ls ${FD_WGS_ASTARR_KS274_OUT}/K562*.with_umis.dedup.rpkm.bw))

FP_WGS_ASTARR_KS274=("${FP_WGS_ASTARR_KS274_OUT_FRAGS[@]}" "${FP_WGS_ASTARR_KS274_OUT_BWIGS[@]}")

### ASTARR MACS peaks
### KS91_K562_hg38_ASTARRseq_Input_allReps.masked.dedup.sorted_peaks.narrowPeak
### KS91_K562_hg38_ASTARRseq_Input.all_reps.masked.union_narrowPeak.q5.bed
### KS91_K562_hg38_ASTARRseq_Input.q5.in_all.max_overlaps.bed
FP_WGS_ASTARR_KS91_INP_PEAKS=(
    ${FD_WGS_ASTARR_KS91_INP}/KS91_K562_hg38_ASTARRseq_Input.all_reps.masked.union_narrowPeak.q5.bed
    ${FD_WGS_ASTARR_KS91_INP}/KS91_K562_hg38_ASTARRseq_Input.q5.in_all.max_overlaps.bed
)

