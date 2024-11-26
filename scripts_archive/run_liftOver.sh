#!/bin/bash

FD_UCSC=/data/common/shared_conda_envs/ucsc/bin
CMD=${FD_UCSC}/liftOver
ARGS="$@"

${CMD} ${ARGS}

