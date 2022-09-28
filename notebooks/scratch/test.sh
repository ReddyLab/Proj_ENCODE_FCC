#!/bin/bash

### get file path
### Stackoverflow: how-can-i-get-the-source-directory-of-a-bash-script-from-within-the-script-itself
source /gpfs/fs1/data/reddylab/Kuei/GitRepo/Proj_CombEffect_ENCODE_FCC/notebooks/config_duke.sh

for arg in "$@"
do
  echo "$arg"
done
