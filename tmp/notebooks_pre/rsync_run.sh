#!/bin/bash
source config_rsync.sh

### set path
SRC=$1
DES=$2
echo

### show msg
echo "+++++++++++++++++++++++++++"
echo "Rsync (DRY)"
echo "    From: (HARDAC) " ${SRC}
echo "    To:   (DCC)    " ${DES}
echo

### rync dry run
rsync -azvh --delete --dry-run --exclude '*.ipynb_checkpoints*' ${SRC} ${DES}
echo

### show msg
echo "+++++++++++++++++++++++++++"
echo "Rsync (RUN)"

### rync run
while true; do
    read -p "Are you sure to perform rsync? " yn
    case $yn in
        [Yy]* ) echo -e "Rsync starts:\n"; rsync -azvh --delete --progress --exclude '*.ipynb_checkpoints*' ${SRC} ${DES}; echo; break;;
        [Nn]* ) echo -e "Rsync is not executed.\n"; exit;;
        * )     echo "Please answer yes or no.";;
    esac
done
