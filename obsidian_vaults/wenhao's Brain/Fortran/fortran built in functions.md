### A List of fortran functions
We use the following convention:
```
A   -> any
R   -> real or integer
X,Y -> real
Z   -> complex
W   -> real or complex
```

| function | meaning |
| -- | -- |
|abs(A) | absolute value
|aimag(Z) | imaginary part of Z
|int(A) | convert to integer, complex part will be 0 if exist
|kind(A) | return the kind of the argument
|anint(X) |nearest integer as real
|floor(X) | greatest integer smaller than X
|complx(X,[Y]) | convert to conplex, y=0 if not given
|conjg(Z) | complex conjugate of Z
|exp(W) | | 
|log(W) | natural logarithm
|log10(X) | | 
|max(R1,R2,...) | | 
|min(R1,R2,...) | | 
|mod(R1,R2) |remainder of R1 on division by R2, (R1-int(R1/R2)R2)
|modulo(R1,R2) | R1 modulo R2, (R1-floor(R1/R2)R2)
|nint(X) |nearest integer
|real(A) |convert to real
|sign(R1,R2) |absolute value of R1 multiplied by the sign of R2
|sqrt(W) | | 
|acos(X) | | 
|asin(X) | | 
|atan(X) | | 
|cos(X) | | 
|sin(X) | | 
|tan(X) | | 
|tanh(X) | | 
|sinh(X) | | 
|cosh(X) | | 
