#!/bin/bash


if [ "$#" -ne 1 ]; then
	echo "Error! Wrong number of parameters!"
	exit 1
fi


if [ ! -f $1 ]; then
	echo "Error! Parameter must be file!"
	exit 1
fi




cat $1 | awk '
{gsub(" ","",$0);gsub("\t","",$0);gsub("\n","",$0);print $0}' 	
