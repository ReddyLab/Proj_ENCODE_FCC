#!/bin/bash

#########################################
### Wrapper of PLACEHOLDER_CMD container
### =====================================

IMAGE=PLACEHOLDER_IMG

CMD="PLACEHOLDER_CMD"
ARGS="$@"

singularity exec   \
    -B ${PWD}      \
    -B /data:/data \
    -B /gpfs:/gpfs \
    ${IMAGE} ${CMD} ${ARGS}
