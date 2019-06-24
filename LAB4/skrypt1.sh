#!/bin/bash

##Witold Marciniak


find $1 -type f -name "*.txt" -or -type f -executable | while read var

do

cat "$var" | tail -2 | head -1

	if [ -x "$var" ]; then

actualsize=$(wc -c <"$var")
var2=100
echo  "scale=3 ; $actualsize / $var2" | bc 

	else

	cat "$var" | sort | tee ss2.txt | head


fi










done


