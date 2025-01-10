#!/bin/bash

### print start message
timer_start=`date +%s`
echo "Hostname:          " $(hostname)
echo "Slurm Array Index: " ${SLURM_ARRAY_TASK_ID}
echo "Time Stamp:        " $(date +"%m-%d-%y+%T")
echo

### get arguments
FP_CNF=${1}
FD_DOWNLOAD_DIRECTORY=${2}
FP_DOWNLOAD_FILE_LIST=${3}

### set environment
source ${FP_CNF}

### show I/O
cd   ${FD_DOWNLOAD_DIRECTORY}
echo "Change directory:"
echo $(pwd)
echo

### execute: download file
echo "Download files..."
xargs -L 1 curl -O -J -L < ${FP_DOWNLOAD_FILE_LIST}
echo

### print end message
timer=`date +%s`
runtime=$(echo "${timer} - ${timer_start}" | bc -l)
echo
echo 'Done!'
echo "Run Time: $(displaytime ${runtime})"
echo
