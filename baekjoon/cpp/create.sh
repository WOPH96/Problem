#!/opt/homebrew/bin/zsh

if [ -z $1 ] ; then
    echo "insert the paramter as a name of problem"
    exit 0
fi

#crete
mkdir $1
touch $1/$1.cpp
touch $1/$1_input.txt
echo "#include <bits/stdc++.h>
using namespace std;
int main()
{
    std::ios_base::sync_with_stdio(false);
    return 0;
}" >> $1/$1.cpp


#open
code $1/$1.cpp
code $1/$1_input.txt
cd $1