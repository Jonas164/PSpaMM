#!/bin/bash

MIN_SIZE=2
MAX_SIZE=102
ALPHA=1
BETA=0

echo "Deleting old pspamm.cpp and pspamm.h"
rm pspamm.cpp
rm pspamm.h
rm pspamm2.cpp
rm pspamm2.h
echo "#include \"pspamm.h\"" >> pspamm.cpp
echo "#include \"pspamm2.h\"" >> pspamm2.cpp

echo "#ifndef PSPAMM_H" >> pspamm.h   
echo "#define PSPAMM_H" >> pspamm.h
echo "#endif" >> pspamm.h

echo "#ifndef PSPAMM2_H" >> pspamm2.h   
echo "#define PSPAMM2_H" >> pspamm2.h
echo "#endif" >> pspamm2.h

echo "Generating first 70 pspamms"
for MAT_DIM in $(seq $MIN_SIZE 2 71);
do
    #Generate Source
    ./pspamm.py $MAT_DIM $MAT_DIM $MAT_DIM $MAT_DIM $MAT_DIM $MAT_DIM $ALPHA $BETA --arch arm --output_funcname "pspamm${MAT_DIM}x${MAT_DIM}" >> pspamm.cpp;
    echo "" >> pspamm.cpp #Newline

    #Generate Header
    echo "void pspamm${MAT_DIM}x${MAT_DIM} (const double* A, const double* B, double* C, double alpha, double beta, const double* prefetch);" >> pspamm.h
    echo $'\n\n' >> pspamm.h


    echo "${MAT_DIM}x${MAT_DIM} generated"
done


echo "Generating 70-100 pspamm into pspamm2"
for MAT_DIM in $(seq 72 2 $MAX_SIZE);
do
    #Generate Source
    ./pspamm.py $MAT_DIM $MAT_DIM $MAT_DIM $MAT_DIM $MAT_DIM $MAT_DIM $ALPHA $BETA --arch arm --output_funcname "pspamm${MAT_DIM}x${MAT_DIM}" >> pspamm2.cpp;
    echo "" >> pspamm2.cpp #Newline

    #Generate Header
    echo "void pspamm${MAT_DIM}x${MAT_DIM} (const double* A, const double* B, double* C, double alpha, double beta, const double* prefetch);" >> pspamm2.h
    echo $'\n\n' >> pspamm2.h


    echo "${MAT_DIM}x${MAT_DIM} generated"
done

mv pspamm.cpp ../Bachelorarbeit/BLAS
mv pspamm2.cpp ../Bachelorarbeit/BLAS
mv pspamm.h ../Bachelorarbeit/BLAS
mv pspamm2.h ../Bachelorarbeit/BLAS