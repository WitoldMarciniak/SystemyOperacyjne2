#!/bin/bash

# Check the number of arhuments
if [ "$#" -ne 1 ]; then
	echo "Error! Wrong number of parameters!"
	exit 1
fi

# Check if first and second parameters are direcotories
if [ ! -f $1 ]; then
	echo "Error! Parameter must be directory!"
	exit 1
fi

# Script contents
cat $1 | gawk 'BEGIN {line_num=1; files_found=0}\
	{sub(  /(void)(\s*)(\w*)/, "double", $1 )}\
	/#include[ ]*((<.*>)|(\".*\"))/ {includes[files_found]=$0;\
		includes[files_found]=gensub( /.*([<"])(.*)([>"]).*/, "\\2", 1, includes[files_found] );\
		files_found+=1};\
	NF != 0 {print line_num ". " $0; line_num+=1};\
	END {for ( key in includes ) print includes[key]}'\

