#!/bin/bash

### print start message
timer_start=`date +%s`
echo "Hostname:          " $(hostname)
echo "Slurm Array Index: " ${SLURM_ARRAY_TASK_ID}
echo "Time Stamp:        " $(date +"%m-%d-%y+%T")
echo

### setup input and output
source ../config/config_duke.sh
FP_INP_SCORE=$1
FP_INP_ANNOT=$2
FP_OUT=$3

#FP_INP_ANNOTS=($(ls ${FD_INP_ANNOT}/*rds))
#FP_INP_ANNOT=${FP_INP_ANNOTS[${SLURM_ARRAY_TASK_ID}]}

### execute
${FD_PRJ}/notebooks/sing_proj_encode_fcc.sh Rscript ./run_fgsea.R ${FP_INP_SCORE} ${FP_INP_ANNOT} ${FP_OUT}

### print end message
timer=`date +%s`
runtime=$(echo "${timer} - ${timer_start}" | bc -l)
echo
echo 'Done!'
echo "Run Time: $(displaytime ${runtime})"

