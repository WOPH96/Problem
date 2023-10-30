#!/bin/zsh
if [ $# -ne 1 ]; then
    msg="no_msg"
else
    msg=$1
fi
git add .
git commit -m "$msg"
git push