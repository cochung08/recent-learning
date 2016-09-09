#!/bin/tcsh

#$ -cwd
#$ -o mpiOutput.log 
#$ -j y
#$ -S /bin/tcsh
#$ -q  gpu

#$ -pe gpu_2_procs_per_task 2
#$ -l gpu=1

module load /cm/shared/modulefiles/cuda/cuda75/toolkit/7.5
module load /cm/shared/modulefiles/cuda/cuda75/openmpi/gcc/1.10.2

nvprof --analysis-metrics -o  nbody-analysis.nvprof ./a.out --benchmark -numdevices=2 -i=1