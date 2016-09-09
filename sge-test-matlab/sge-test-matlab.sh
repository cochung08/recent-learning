#!/bin/bash
#
#$ -cwd
##$ -j y
#$ -S /bin/bash
#$ -o output/out.txt
#$ -e output/err.txt
##$ -t 1-10
#
# . /etc/profile
module load /cm/shared/apps/matlab/R2012b
 
matlab -nodisplay -nojvm < test-matlab.m