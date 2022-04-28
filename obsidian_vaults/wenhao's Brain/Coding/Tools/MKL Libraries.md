### Intel MKL

the main functions supported by MKL are:
- BLAS and LAPACK
- ScaLAPACK, BLACS, PBLAS
- FFT
- VML  vector math library
- VSL  vector statistical lib

**Environmental variable associated with MKL library**
MKL use some environment variables. In the `mkl/bin/`, we can find the scripts to set up the related variables. they are also listed below:
```bash
$INCLUDE
$MKLROOT
$LD_LIBRARY_PATH
$MIC_LD_LIBRARY_PATH  # for mic architecture only
$MANPATH
$LIBRARY_PATH
$CPATH
$NLSPATH
```

Structure of MKL library ( in NIMS NMS )

| folder | files |
| ---- | --- |
|bin           | contains the scripts to set up environmental variables
|include       | .h and .f90 files as header file ( .f90 file specifies the interface )
|include/fftw  | .h and .f90 files for fft
|lib/intel64   | .a and .so files of the library
    

**Linking programs with MKL library**
Intel compiler support the following options

| option | meaning |
| ---- | --- |
|- -mkl (or -mkl=parallel)   | link the standard theaded MKL
|- -mkl=sequential           | sequential version of MKL
|- -mkl=cluster              | cluster components but use intel MPI