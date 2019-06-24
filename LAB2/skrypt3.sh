#!/bin/bash

	if [ $# -ne 2 ]
then

	echo "niepoprawna liczba argumentów"

	exit 1

	fi 


	if [ ! -d $1 ] || [ ! -f $2 ]	
then
	echo "1 parameter powinien być katalogiem a 2 plikiem regularnym"

	exit 1
	
	fi


	ln -s `realpath $2` `readlink -m $1`
	



