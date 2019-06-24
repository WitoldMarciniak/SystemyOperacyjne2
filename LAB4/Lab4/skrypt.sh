#!/bin/bash


##Witold Marciniak 226194

if [ $# -ne 2 ]
then
	echo "niepoprawna liczba argumentow!"
	exit 1
fi

if [ ! -d $1 ]
then
	echo "$1 nie jest katalogiem!"
	exit 1

fi

if [ ! -f $2 ]
then

	echo "$2 nie jest plikiem!"
fi


find $1 -type f -or -type d |  while read var

do


	if [ -f "$var" ]; then

	size=$(stat -c '%i' "$var")
	divider=10

	##new=$size/$divider

	##var="$size/$divider" | bc -l 

	var=$((size/divider))
	

	else 
	
	var=$(stat -c '%n' "$var" | tr '[A-Z]' '[N-ZA-M]') 
	
	


	fi

done | tee $2 | head -50 | sort 
  
##cat $2 | head -50 | sort 


