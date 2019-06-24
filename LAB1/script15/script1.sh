#!/bin/bash

var=0

	for i in $(ls $1);

	do x="$i"

	if [ -x $x ]
	then
	
	var=$((var + 1))
	
	fi


	done

	echo $var


