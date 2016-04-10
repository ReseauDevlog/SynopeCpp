#!/usr/bin/env sh
rm -f tp0_code_initial.exe \
&& g++ -Wall -Wextra -Wshadow tp0_code_initial.cpp -o tp0_code_initial.exe \
&& ./tp0_code_initial.exe | tee tp0_code_initial.log
