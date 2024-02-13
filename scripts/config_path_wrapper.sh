### get path of the script
### Stackoverflow: how-can-i-get-the-source-directory-of-a-bash-script-from-within-the-script-itself
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

### identify Singularity environment
### https://stackoverflow.com/questions/71524077/how-to-verify-if-in-singularityapptainer-container
if [ -d /.singularity.d ]; then
    ### workspace info
    SERVER="Singularity"
    echo "in singularity"
fi

### identify Duke HARDAC environment 
if echo $(pwd -P) | grep -q "gpfs"; then
    ### workspace info
    SERVER=HARDAC
    NODE=all
    
    ### get directories
    source ${SCRIPT_DIR}/config_path_duke_hardac.sh
fi

