#!/bin/bash

##WITOLD MARCINIAK NR INDEKSU: 226194


var="/"
## 1 ZADANIE

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

if [ -L $1/$var ] && [ -f $1/$var ]
then
	##[ `realpath $1/$var` != `readlink $1/$var` ]

	firstletter=${`readlink $1/$var`:0:1}	
	
	if [ firstletter != var ]

	then

	rm `readlink -m $1/$var`
	rm $1/$var

	fi

fi
done



## 2 ZADANIE

for var in `ls -a $1`
do

	if [ $1/$var -ef $2 ]
	then

	echo "$1/$var"

	fi
done



