#!/bin/bash

### print start message
timer_start=`date +%s`
echo "Hostname:          " $(hostname)
echo "Slurm Array Index: " ${SLURM_ARRAY_TASK_ID}
echo "Time Stamp:        " $(date +"%m-%d-%y+%T")
echo

### setup input and output
source ../config/config_duke.sh
FP_INP1=$1
FP_INP2=$2
FP_OUT=$3

### show I/O file
echo "Input: " ${FP_INP1}
echo
echo "show first few lines of input"
fun_head ${FP_INP1}
echo
echo "Input: " ${FP_INP2}
echo
echo "show first few lines of input"
fun_head ${FP_INP2}
echo

### execute
bedtools -h

### show output file
echo
echo "Output: " ${FP_OUT}
echo
echo "show first few lines of output:"
fun_head ${FP_OUT}
echo

### print end message
timer=`date +%s`
runtime=$(echo "${timer} - ${timer_start}" | bc -l)
echo
echo 'Done!'
echo "Run Time: $(displaytime ${runtime})"

