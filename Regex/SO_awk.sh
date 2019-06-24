#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Podano zla liczbe parametrow"
    exit 1
fi

# Check if first and second parameters are direcotories
if [ ! -f $1 ]; then
    echo "Podany argument nie jest zwyklym plikiem"
    exit 1
fi

cat $1 | awk '  BEGIN { suma = 0; liczba_liczb = 0 };\
                $0 !~ /^\s*$/ {print $0};\
                {if ( match( $0, /(=)(\s*)("?)(\w+)("?)(\s*)(;*)/, tab ) ) {print tab[4]} };\
                {if ( match( $0, /[^"].*[=+*\\\-\s](\d+\.?\d*)[^\d]/, liczba ) ) {suma+=$liczba[1]}; {liczba_liczb+=1} };\
                END { printf("Srednia %f\nSuma %f\nLicznik %d\n", suma/liczba_liczb, suma, liczba_liczb) }'




