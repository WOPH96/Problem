#!/opt/homebrew/bin/zsh

if [ -z $1 ] ; then
    echo "insert the paramter as a name of problem"
    exit 0
fi

#crete
mkdir $1
touch $1/$1.py
touch $1/$1_input.txt
echo "import sys" >> $1/$1.py
echo "sys.stdin = open('$1_input.txt','r')" >> $1/$1.py

#open
code $1/$1.py
code $1/$1_input.txt
cd $1