#!/bin/bash

var=0
	
	for i in $(ls $1);
	


	do x="$i"
	
	

	for j in $(cat $2); 
		
	
	do j="$j"
	
	var=0
	
	if [ $x != $j ] && [ $var -eq 0 ]

	then

	var=$((var + 1)) 
	
	echo Plik Ktory jest
	
	echo $j

	fi

	
	done
	

	done
