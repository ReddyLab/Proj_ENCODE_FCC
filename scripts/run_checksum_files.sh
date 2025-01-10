#!/bin/bash

### print start message
timer_start=`date +%s`
echo "Hostname:          " $(hostname)
echo "Slurm Array Index: " ${SLURM_ARRAY_TASK_ID}
echo "Time Stamp:        " $(date +"%m-%d-%y+%T")
echo

### get arguments
FP_CNF=${1}
FD_CHECKSUM=${2}
FP_CHECKSUM_INP=${3}
FP_CHECKSUM_OUT=${4}

### set environment
source ${FP_CNF}

### show I/O
cd   ${FD_CHECKSUM}
echo "Change directory:"
echo $(pwd)
echo

### execute: checksum
echo "Checksum files..."
md5sum -c ${FP_CHECKSUM_INP} > ${FP_CHECKSUM_OUT}
echo

### print end message
timer=`date +%s`
runtime=$(echo "${timer} - ${timer_start}" | bc -l)
echo
echo 'Done!'
echo "Run Time: $(displaytime ${runtime})"
echo
