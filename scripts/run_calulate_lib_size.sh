#!/bin/bash

### print start message
timer_start=`date +%s`
echo "Hostname:          " $(hostname)
echo "Slurm Array Index: " ${SLURM_ARRAY_TASK_ID}
echo "Time Stamp:        " $(date +"%m-%d-%y+%T")
echo

### setup env:
###     get project root path
###     load helper functions
FD_PRJ=$1
FD_EXE=${FD_PRJ}/scripts
source ${FD_EXE}/config_func.sh

### set input and output files
FP_INP=$2
FP_OUT=$3

### execute
###     count the total counts and append the results to the output file
FN_INP=$(basename ${FP_INP})
zcat ${FP_INP} \
|   awk -v OFS=, -v FNAME=${FN_INP} '{sum += $5} END {print FNAME, NR, sum}' \
>>  ${FP_OUT}

### show I/O file
echo "Output file: ${FP_OUT}"
echo
echo "show lines of file"
fun_cat ${FP_OUT}
echo

### print end message
timer=`date +%s`
runtime=$(echo "${timer} - ${timer_start}" | bc -l)
echo
echo 'Done!'
echo "Run Time: $(displaytime ${runtime})"
