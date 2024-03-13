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

### setup input and output
FP_INP=$2

### show input file
echo "Input: " ${FP_INP}
echo
echo "show first few lines of input"
fun_cat ${FP_INP} | head
echo

### execute
bedtools --help
echo

### print end message
timer=`date +%s`
runtime=$(echo "${timer} - ${timer_start}" | bc -l)
echo
echo 'Done!'
echo "Run Time: $(displaytime ${runtime})"

