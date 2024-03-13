SCRIPT_DIR1="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
echo ${SCRIPT_DIR1}

SCRIPT_DIR2=$(realpath "$0")
echo ${SCRIPT_DIR2}