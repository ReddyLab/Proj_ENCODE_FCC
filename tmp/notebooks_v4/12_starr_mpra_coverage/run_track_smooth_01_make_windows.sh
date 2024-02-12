#!/bin/bash

### print start message
timer_start=`date +%s`
echo "Hostname:          " $(hostname)
echo "Slurm Array Index: " ${SLURM_ARRAY_TASK_ID}
echo "Time Stamp:        " $(date +"%m-%d-%y+%T")
echo

### setup input and output
source ../config/config_duke.sh
VAL_WINDOW=$1
VAL_SPAN=$2
FP_INP=$3
FP_OUT=$4

### show I/O file
echo "Input: " ${FP_INP}
echo
echo "show first few lines of input"
zcat ${FP_INP} | head -5
echo

### execute
bedtools makewindows -b ${FP_INP} -w ${VAL_WINDOW} -s ${VAL_SPAN} | gzip -c > ${FP_OUT}

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

