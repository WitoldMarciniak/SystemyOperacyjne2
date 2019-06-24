#!/bin/bash

var=0


	for i in $(ls $1);

	do x="$i"

	if [ -r $x ] && [ -w $x ] 
	then

	touch $x	
	var=$((var +  1))
	

	fi

	done	

	echo $var
