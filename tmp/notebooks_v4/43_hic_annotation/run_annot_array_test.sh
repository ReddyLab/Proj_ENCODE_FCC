#!/bin/bash

### print start message
timer_start=`date +%s`
echo "Hostname:          " $(hostname)
echo "Slurm Array Index: " ${SLURM_ARRAY_TASK_ID}
echo "Time Stamp:        " $(date +"%m-%d-%y+%T")
echo

### setup input and output
source ../config/config_duke.sh
PREFIX=$1
FD_REG=$2
FD_ANT=$3
FD_OUT=$4

FP_REG=${FD_REG}/${PREFIX}.bed.gz

FP_ANTS=($(ls ${FD_ANT}/*.bed.gz))
FP_ANT=${FP_ANTS[SLURM_ARRAY_TASK_ID]}
FN_ANT=$(basename ${FP_INP})

FN_OUT=${PREFIX}.annotation.${FN_ANT}
FP_OUT=${FD_OUT}/${FN_OUT}

### show I/O file
echo "Input: " ${FP_REG}
echo
echo "show first few lines of input"
zcat ${FP_REG} | head -5
echo
echo "Input: " ${FP_ANT}
echo
echo "show first few lines of input"
zcat ${FP_ANT} | head -5
echo

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

