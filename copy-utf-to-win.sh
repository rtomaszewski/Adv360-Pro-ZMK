#!/bin/bash

windir="/mnt/c/Users/rados/Downloads/_zmk"
lindir="/home/rado/Adv360-Pro-ZMK/firmware"

while true; do
  echo -n "."; sleep 1s

  if [ $(ls $lindir/*.uf2 2>/dev/null | wc -l) -ne 0 ] ; then 
    echo ,; sleep 1s; #to make sure that the files are actually writen and closed; 
                      # we wouldn't like to copy corrupted/truncated files
    echo; echo $(date)
    mv -v $lindir/*.uf2 $windir/ 
    echo ; echo
  fi
done
