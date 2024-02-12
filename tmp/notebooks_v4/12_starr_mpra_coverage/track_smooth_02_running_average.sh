#!/bin/bash

### print start message
timer_start=`date +%s`
echo "Hostname:          " $(hostname)
echo "Slurm Array Index: " ${SLURM_ARRAY_TASK_ID}
echo "Time Stamp:        " $(date +"%m-%d-%y+%T")
echo

### setup input and output
source ../config/config_duke.sh
FP_REG=$1
FP_INP=$2
FP_OUT=$3

### show I/O file
echo "Region: " ${FP_REG}
echo
echo "show first few lines of input"
zcat ${FP_REG} | head -5
echo

### show I/O file
echo "Input: " ${FP_INP}
echo
echo "show first few lines of input"
zcat ${FP_INP} | head -5
echo

### execute
bedtools map \
    -a ${FP_REG} \
    -b ${FP_INP} \
    -c 4    \
    -o mean \
| grep -v $'\t\\.' \
> ${FP_OUT}

### show output file
echo
echo "Output: " ${FP_OUT}
echo
echo "show first few lines of output:"
cat ${FP_OUT} | head -5
echo

### print end message
timer=`date +%s`
runtime=$(echo "${timer} - ${timer_start}" | bc -l)
echo
echo 'Done!'
echo "Run Time: $(displaytime ${runtime})"

