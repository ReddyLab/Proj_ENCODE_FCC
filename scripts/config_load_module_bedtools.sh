#!/bin/bash

### Check which duke server I am at and load the corresponding modules

if echo /gpfs/fs1/data/reddylab/Kuei/repo/Proj_CombEffect_ENCODE_FCC/notebooks/01_setup | grep -q "gpfs"; then
    #echo "You are on Duke Server: HARDAC"
    module load bedtools2
fi

if echo /gpfs/fs1/data/reddylab/Kuei/repo/Proj_CombEffect_ENCODE_FCC/notebooks/01_setup | grep -q "hpc"; then
    #echo "You are on Duke Server: DCC"
    module load Bedtools
fi

