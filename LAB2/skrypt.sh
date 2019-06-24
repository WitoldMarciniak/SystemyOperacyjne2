#!/bin/bash


if [ $# -ne 2 ] 
then
	echo "Niepoprawna liczba argumentow!"
	exit 1
fi

if [ ! -d $1 ]||[ ! -d $2 ]
then
	echo "$1 i/lub $2 nie jest katalogiem!"
	exit 1
fi

if [ $1 -ef $2 ]
then
	echo "$1 i $2 to ten sam katalog!"
	exit 1
fi
 
for plik in `ls -a $1`
do
	if [ -L $1/$plik ] && ! [ -e $1/$plik ]
	then
		echo "Usuwanie $1/$plik"
		rm 1$/$plik
	fi
	
	if [ -d $1/$plik ] || [ -f $1/$plik ]
	then
		ln -s `readlink -m $1/$plik` $2
	fi
done














