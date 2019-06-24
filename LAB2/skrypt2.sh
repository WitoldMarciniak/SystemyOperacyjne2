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




for var in `ls -a $1`
do

	if [ $1/$var -ef $2 ]
	then

	echo "$1/$var"

	fi
done

