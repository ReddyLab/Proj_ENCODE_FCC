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
FP_CNF=$1
source ${FP_CNF}

### setup input and output
FP_INP1=$2
FP_INP2=$3
FP_OUT=$4

### show input file
echo "Input: " ${FP_INP1}
echo
echo "show first few lines of input"
fun_cat ${FP_INP1} | head
echo
echo "Input: " ${FP_INP2}
echo
echo "show first few lines of input"
fun_cat ${FP_INP2} | head
echo

### execute
bedtools closest \
    -a ${FP_INP1} \
    -b ${FP_INP2} \
    -d \
| gzip -c \
> ${FP_OUT}

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

