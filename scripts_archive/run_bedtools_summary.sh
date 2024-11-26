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
FP_GEN=$3
FP_OUT=$4

### show input file
echo "Input (FP_INP):" 
echo ${FP_INP}
echo
echo "show first few lines of input"
fun_cat ${FP_INP} | head
echo
echo "Input: (FP_GEN):"
echo ${FP_GEN}
echo
echo "show first few lines of input"
fun_cat ${FP_GEN} | head
echo

### execute
bedtools summary \
    -i ${FP_INP} \
    -g ${FP_GEN} \
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

