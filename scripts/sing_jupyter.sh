#!/bin/bash
############################################################################
### this script launches the singularity service for project combeffect
############################################################################


### get flag ptions
### https://stackoverflow.com/questions/7069682/how-to-get-arguments-with-flags-in-bash
### https://stackoverflow.com/questions/16483119/an-example-of-how-to-use-getopts-in-bash
N_PORT=8888
usage() { echo "Usage: $0 [-p <PORT Number>]" 1>&2; exit 1; }
while getopts ':p:' flag; do
  case "${flag}" in
    p) 
        N_PORT=$OPTARG 
        ;;
    *) usage ;;
  esac
done
shift $((OPTIND -1))

### set environment
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
source ${SCRIPT_DIR}/config_project.sh
FD_HOME=${FD_SING}/home

### Show
echo "N_PORT:         ${N_PORT}"
echo "Mount HOME:     ${FD_HOME}"
echo "Mount REPO:     ${FD_REPO}"
echo "Mount WORK:     ${FD_WORK}"
echo "Mount DATA:     ${FD_DATA}"
echo "Mount ReddyLab: ${FD_RLAB}"
echo "Singularity:    ${FP_SIF}"
echo 

### execute
singularity exec \
    -H ${FD_HOME}:/home \
    -B ${FD_REPO}:/mount/repo \
    -B ${FD_WORK}:/mount/work \
    -B ${FD_DATA}:/mount/data \
    -B ${FD_RLAB}:/mount/reddylab \
    -B /data:/data \
    ${FP_SIF} \
    jupyter lab --NotebookApp.token="543@Psk" --NotebookApp.notebook_dir=/home --no-browser --ip=0.0.0.0 --port=${N_PORT}