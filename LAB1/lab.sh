#!/bin/bash

var=0
	
	for i in $(cat $1);
	do x="$i"
	
	

		for j in $(ls $2); 
	do j="$j"
	
	var=0
	
		if [ $x != $j ] && [ $var -eq 0 ]

	then

	var=$((var + 1)) 
	
	echo Plik ktory jest w D
	
	echo $j

	fi

	
	done
	echo plik ktorego nie ma w D	
	echo $x
	done
