#!/bin/bash

### Check which duke server I am at and load the corresponding modules

if echo $(pwd -P) | grep -q "gpfs"; then
    #echo "You are on Duke Server: HARDAC"
    module load bedops
fi

