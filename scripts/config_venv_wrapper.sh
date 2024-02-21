### get path of the script
### Stackoverflow: how-can-i-get-the-source-directory-of-a-bash-script-from-within-the-script-itself
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

### identify Singularity environment
### https://stackoverflow.com/questions/71524077/how-to-verify-if-in-singularityapptainer-container
if [ -d /.singularity.d ]; then

    ### get workspace env
    source ${SCRIPT_DIR}/config_path_sing.sh
    
fi

### identify Duke HARDAC environment 
if echo $(pwd -P) | grep -q "gpfs"; then

    ### get workspace env
    NODE=all
    source ${SCRIPT_DIR}/config_path_duke_hardac.sh
    
fi

### identify Duke DCC environment

