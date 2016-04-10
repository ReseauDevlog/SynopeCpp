#!/usr/bin/env sh
rm -f tp1_variables_fonctions.exe \
&& g++ -Wall -Wextra -Wshadow tp1_variables_fonctions.cpp -o tp1_variables_fonctions.exe \
&& ./tp1_variables_fonctions.exe | tee tp1_variables_fonctions.log \
&& diff tp1_variables_fonctions.ref tp1_variables_fonctions.log

