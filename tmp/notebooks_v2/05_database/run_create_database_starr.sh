#!/bin/bash

#SBATCH --partition     all
#SBATCH --exclude       dl-01
#SBATCH --cpus-per-task 8
#SBATCH --mem           16G
#SBATCH --array         0-1

#######################################
### Start script
###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
source ../config/config_duke.sh

### print start message 
timer_start=`date +%s`
echo "Hostname:          " $(hostname) 
echo "Slurm Array Index: " ${SLURM_ARRAY_TASK_ID} 
echo "Time Stamp:        " $(date +"%m-%d-%y+%T") 
echo

#######################################
### Set global variables
###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ASSAY=$1
STRAND="unstranded"

REGIONS=(GATA1 MYC)
REGION=${REGIONS[${SLURM_ARRAY_TASK_ID}]}

CHROMS=(chrX chr8)
CHROM=${CHROMS[${SLURM_ARRAY_TASK_ID}]}

### file path of database
FDIRY=${FD_RES}/${ASSAY}/database
FNAME="fragment_${REGION}.db"
FP_DTB=${FDIRY}/${FNAME}

echo "Assay:    ${ASSAY}"
echo "Region:   ${REGION}"
echo "Database: ${FP_DTB}"

#######################################
### Initialization: Create tables
###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

../sing_proj_encode_fcc.sh python ./scripts/starr00_initialize.py \
    --database ${FP_DTB} \
    --verbose
    
#######################################
### Insert: Sample
###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FP_INP=${FD_RES}/${ASSAY}/coverage/library_size/library_size_summary.csv

echo "Insert Table: Sample"
echo "  Input: ${FP_INP}"

../sing_proj_encode_fcc.sh python ./scripts/starr01_sample.py \
    --database ${FP_DTB} \
    --finp     ${FP_INP}

#######################################
### Insert: Motif
###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FP_INP=${FD_ANN}/motif_cluster_jvierstra/hg38_archetype_motifs_v1/${CHROM}_rm_mouse_merge.bed.gz

echo "Insert Table: Motif"
echo "  Input: ${FP_INP}"

../sing_proj_encode_fcc.sh python ./scripts/starr02_insert.py \
    --table    Motif  \
    --database ${FP_DTB} \
    --finp     ${FP_INP} \
    --compressed

#######################################
### Insert: Fragment
###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FOLDER="fragment_nuc"
FPATHS=($(ls ${FD_RES}/${ASSAY}/${FOLDER}/*${REGION}*${STRAND}*))

echo "Insert Table: Fragment"

for FP_INP in ${FPATHS[@]}; do
    echo "  Input: ${FP_INP}"
    ../sing_proj_encode_fcc.sh python ./scripts/starr02_insert.py \
    --table    Fragment  \
    --database ${FP_DTB} \
    --finp     ${FP_INP} \
    --compressed \
    --header
done

#SAMPLE="Input_rep1"
#FP_INP=$(ls ${FD_RES}/${ASSAY}/${FOLDER}/*${SAMPLE}*${REGION}*${STRAND}*)
#../sing_proj_encode_fcc.sh python ./scripts/starr02_insert.py \
#    --table    Fragment  \
#    --database ${FP_DTB} \
#    --finp     ${FP_INP} \
#    --compressed \
#    --header     \
#    --verbose

#######################################
### Insert: Counts
###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FOLDER="fragment_nuc"
FPATHS=($(ls ${FD_RES}/${ASSAY}/${FOLDER}/*${REGION}*${STRAND}*))

echo "Insert Table: Count"
for FP_INP in ${FPATHS[@]}; do
    echo "  Input: ${FP_INP}"
    ../sing_proj_encode_fcc.sh python ./scripts/starr02_insert.py \
        --table    Count  \
        --database ${FP_DTB} \
        --finp     ${FP_INP} \
        --compressed \
        --header
done
    
#######################################
### Insert: Annotation
###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FOLDER="annotation"
FPATHS=($(ls ${FD_RES}/${ASSAY}/${FOLDER}/*${REGION}*${STRAND}*))

echo "Insert Table: Annotation"
for FP_INP in ${FPATHS[@]}; do
    echo "  Input: ${FP_INP}"
    ../sing_proj_encode_fcc.sh python ./scripts/starr02_insert.py \
        --table    Annotation  \
        --database ${FP_DTB} \
        --finp     ${FP_INP} \
        --compressed
done
    
#######################################
### Insert: Coverage
###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FOLDER="coverage"
FPATHS=($(ls ${FD_RES}/${ASSAY}/${FOLDER}/*${REGION}*${STRAND}*perbase*))

echo "Insert Table: Coverage"
for FP_INP in ${FPATHS[@]}; do
    echo "  Input: ${FP_INP}"
    ../sing_proj_encode_fcc.sh python ./scripts/starr02_insert.py \
        --table    Coverage  \
        --database ${FP_DTB} \
        --finp     ${FP_INP} \
        --compressed
done

#######################################
### Indexing
###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

../sing_proj_encode_fcc.sh python ./scripts/starr03_index.py \
    --database ${FP_DTB} \
    --verbose

#######################################
### Check results
###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

../sing_proj_encode_fcc.sh python ./scripts/starr04_check.py \
    --database ${FP_DTB}

#######################################
### End script
###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### print end message 
timer_stop=`date +%s` 
runtime=$(echo "${timer_stop} - ${timer_start}" | bc -l) 
echo 
echo 'Done!' 
echo "Run Time: $(displaytime ${runtime})"