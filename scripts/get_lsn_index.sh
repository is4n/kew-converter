#! /bin/sh
mkdir $1/.cache/
cd $1/.cache
wget $2 -O lsn_index.html
