#!/bin/bash

### print start message
timer_start=`date +%s`
echo "Hostname:          " $(hostname)
echo "Slurm Array Index: " ${SLURM_ARRAY_TASK_ID}
echo "Time Stamp:        " $(date +"%m-%d-%y+%T")
echo

### arguement
FP_INP=${1}
FP_OUT=${2}

### setup input and output
source ../config/config_duke.sh

### show input file
echo "Input: " ${FP_INP}
echo
echo "show first few lines of input"
fun_head ${FP_INP}
echo

### execute
bedtools merge \
    -i ${FP_INP} \
| gzip -c \
> ${FP_OUT}

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

