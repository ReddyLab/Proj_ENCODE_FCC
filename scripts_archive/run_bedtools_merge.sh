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
source ${FD_EXE}/config_project.sh

### setup input and output
FP_INP=$2
FP_OUT=$3

### show input file
echo "Input: " ${FP_INP}
echo
echo "show first few lines of input"
fun_cat ${FP_INP} | head
echo

### execute
bedtools merge \
    -i ${FP_INP} \
    -c 4,5 \
    -o distinct,distinct \
| gzip -c \
> ${FP_OUT}
echo

### show output file
echo
echo "Output: " ${FP_OUT}
echo
echo "show first few lines of output:"
fun_cat ${FP_OUT} | head
echo

### print end message
timer=`date +%s`
runtime=$(echo "${timer} - ${timer_start}" | bc -l)
echo
echo 'Done!'
echo "Run Time: $(displaytime ${runtime})"

