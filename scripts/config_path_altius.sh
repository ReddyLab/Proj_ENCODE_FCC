#!/bin/bash

#########################################
### set workspace info
### =====================================

SERVER="Altius"
PROJECT="ENCODE FCC"

#########################################
### set base working folder
### =====================================

FD_RLAB="/net/seq/data2/projects/reddylab"
FD_BASE="/net/seq/data2/projects/reddylab/Kuei"

FD_REPO="${FD_BASE}/repo"
FD_WORK="${FD_BASE}/work"
FD_DATA="${FD_BASE}/data"
FD_ENVS="${FD_BASE}/envs"
FD_BINS="${FD_BASE}/bins"
FD_TEMP="${FD_BASE}/temp"
FD_SING="${FD_BASE}/container"

#########################################
### set project folder
### =====================================
FD_PRJ=${FD_REPO}/Proj_ENCODE_FCC

FD_RES=${FD_PRJ}/results
FD_EXE=${FD_PRJ}/scripts
FD_DAT=${FD_PRJ}/data
FD_NBK=${FD_PRJ}/notebooks
FD_DOC=${FD_PRJ}/docs
FD_LOG=${FD_PRJ}/log
FD_REF=${FD_PRJ}/references

#########################################
### set additional folder/files
### =====================================

### Genome directory
FD_GEN=${FD_DATA}/annotation/genome/hg38

### Configuration file path
FP_CNF=${FD_EXE}/config_project.sh

### Singularity image file path
FP_PRJ_SIF=${FD_SING}/project/singularity_proj_encode_fcc.sif

#########################################
### helper function: show environment
### =====================================

show_env() {
    echo "You are working on             ${SERVER}"
    echo "BASE DIRECTORY (FD_BASE):      ${FD_BASE}" 
    echo "REPO DIRECTORY (FD_REPO):      ${FD_REPO}"
    echo "WORK DIRECTORY (FD_WORK):      ${FD_WORK}"
    echo "DATA DIRECTORY (FD_DATA):      ${FD_DATA}"
    echo "CONTAINER DIR. (FD_SING):      ${FD_SING}"
    echo
    echo "You are working with           ${PROJECT}"
    echo "PATH OF PROJECT (FD_PRJ):      ${FD_PRJ}"
    echo "PROJECT RESULTS (FD_RES):      ${FD_RES}"
    echo "PROJECT SCRIPTS (FD_EXE):      ${FD_EXE}"
    echo "PROJECT DATA    (FD_DAT):      ${FD_DAT}"
    echo "PROJECT NOTE    (FD_NBK):      ${FD_NBK}"
    echo "PROJECT DOCS    (FD_DOC):      ${FD_DOC}"
    echo "PROJECT LOG     (FD_LOG):      ${FD_LOG}"
    echo "PROJECT REF     (FD_REF):      ${FD_REF}"
    echo "PROJECT IMAGE   (FP_PRJ_SIF):  ${FP_PRJ_SIF}"
    echo "PROJECT CONF.   (FP_CNF):      ${FP_CNF}"
    echo
}