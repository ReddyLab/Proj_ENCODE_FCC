#!/bin/bash

FD_SING=/data/reddylab/Kuei/singularity/project
FN_SING=singularity_proj_encode_fcc.sif
FP_SING=${FD_SING}/${FN_SING}

### execute
singularity exec \
    -H ${PWD}:/home \
    -B /data:/data \
    ${FP_SING} \
    "$@"
