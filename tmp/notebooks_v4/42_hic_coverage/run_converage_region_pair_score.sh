#!/bin/bash

### print start message
timer_start=`date +%s`
echo "Hostname:          " $(hostname)
echo "Slurm Array Index: " ${SLURM_ARRAY_TASK_ID}
echo "Time Stamp:        " $(date +"%m-%d-%y+%T")
echo

### set I/O
source ../config/config_duke.sh
FP_HIC=$1
FP_INP=$2
FP_OUT=$3

TXT_CHROMOSOME=$4    # chr11
TXT_NORMALIZATION=$5 # 'RU'
VAL_RESOLUTION=$6    # 100

### show I/O file
echo "Input: " ${FP_INP}
echo
echo "show first few lines of input"
zcat ${FP_INP} | head -5
echo

### execute
RUN_SING=${FD_PRJ}/notebooks/sing_proj_encode_fcc.sh

${RUN_SING} python run_coverage_region_pair_score.py \
    --fpath_hic ${FP_HIC} \
    --fpath_inp ${FP_INP} \
    --fpath_out ${FP_OUT} \
    --chromosome    ${TXT_CHROMOSOME}    \
    --normalization ${TXT_NORMALIZATION} \
    --resolution    ${VAL_RESOLUTION}

### show output file
echo
echo "Output: " ${FP_OUT}
echo
echo "show first few lines of output:"
zcat ${FP_OUT} | head -5
echo

### print end message
timer=`date +%s`
runtime=$(echo "${timer} - ${timer_start}" | bc -l)
echo
echo 'Done!'
echo "Run Time: $(displaytime ${runtime})"
