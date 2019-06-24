#!/bin/bash



find $1 !((-type f -name) "*.txt" -a !(-executable)) | while read var

do

echo "elo"




done
