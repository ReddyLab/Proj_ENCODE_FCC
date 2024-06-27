#!/bin/bash

###
function fun_identify_server {

    ### identify Singularity environment
    ### https://stackoverflow.com/questions/71524077/how-to-verify-if-in-singularityapptainer-container
    if [ -d /.singularity.d ]; then
        echo "Singularity"   
    fi
    
    ### identify Duke HARDAC environment 
    if echo $(pwd -P) | grep -q "gpfs"; then
        echo "HARDAC"
    fi

}

### Hardcoding for testing
function fun_set_server {
    echo "HARDAC"
    #echo "Singularity"
    #echo "DCC"
}

###
function fun_get_server {
    fun_identify_server
    #fun_set_server
}