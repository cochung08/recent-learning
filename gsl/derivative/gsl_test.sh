#!/bin/bash
#
g++ -c derivative.cpp
if [ $? -ne 0 ]; then
  echo "Errors compiling derivative.cpp"
  exit
fi
#
g++ derivative.o -lm -lgsl -lgslcblas
if [ $? -ne 0 ]; then
  echo "Errors linking and loading derivative.o."
  exit
fi
#
rm derivative.o
#
mv a.out derivative
./derivative #> derivative_output.txt
rm derivative
#
echo "Program output written to derivative_output.txt"
