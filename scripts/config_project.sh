### get path of the script
### Stackoverflow: how-can-i-get-the-source-directory-of-a-bash-script-from-within-the-script-itself
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

### set environment
source ${SCRIPT_DIR}/config_venv_wrapper.sh
source ${SCRIPT_DIR}/config_func.sh

### Hack to handle broken pipes - IGNORE.
cleanup () {
    :
}
trap "cleanup" SIGPIPE

