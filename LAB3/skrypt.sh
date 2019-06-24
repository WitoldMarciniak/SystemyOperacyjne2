#!/bin/bash


##Witold Marciniak 226194

if [ $# -ne 1 ]
then
	echo "niepoprawna liczba argumentow!"
	exit 1
fi

if [ ! -d $1 ]
then
	echo "$1 nie jest katalogiem!"
	exit 1

fi


##a)
find $1 -maxdepth 3 -type f -mmin -5 -name "*.png" -print

##b)
find $1 -type d "(" ! -readable -o -perm 022 ")" -printf "%d:%p\n"
##c)
find -L $1 -xtype l -type d -exec rm {} +


