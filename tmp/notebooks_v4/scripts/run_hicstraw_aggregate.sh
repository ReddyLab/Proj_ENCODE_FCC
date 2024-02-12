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

TXT_NORMALIZATION=$4 # 'RU'
NUM_RESOLUTION=$5    # 100
NUM_WINDOW_SIZE=$6   # 10,000
TXT_DATA_TYPE=oe

### show I/O file
echo "Input: " ${FP_INP}
echo
echo "show first few lines of input"
fun_head ${FP_INP}
echo

### execute
FD_RUN=${FD_PRJ}/notebooks/scripts
FP_RUN=${FD_RUN}/run_sing_proj_encode_fcc.sh

${FP_RUN} python ${FD_RUN}/run_hicstraw_aggregate.py \
    --fpath_hic     ${FP_HIC} \
    --fpath_inp     ${FP_INP} \
    --fpath_out     ${FP_OUT} \
    --normalization ${TXT_NORMALIZATION} \
    --resolution    ${NUM_RESOLUTION}    \
    --window_size   ${NUM_WINDOW_SIZE}   \
    --data_type     ${TXT_DATA_TYPE}
    
### show output file
echo
echo "Output: " ${FP_OUT}
echo

### print end message
timer=`date +%s`
runtime=$(echo "${timer} - ${timer_start}" | bc -l)
echo
echo 'Done!'
echo "Run Time: $(displaytime ${runtime})"

