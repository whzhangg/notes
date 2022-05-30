# Fortran

Created: September 30, 2021 8:58 PM
Description: fortran notes, mainly from self-study fortran
Tags: Programming, fortran

## Self-study fortran
### General Syntax and compile
Grammar Rules:
- case insensitive, upper and lower case are not important
- blank lines and spaces are not important
- comments are leaded by `!`
- statements can be in the same line if they are separated by `;`
- to exit a program use stop statement, which accept some text `stop ‘program now stop’`
- break a long line with  `&`

To compile fortran program, use command:
```bash
gfortran -o ex1 ex1.f90
# -o : specify the output of the program
```

### Variable and expressions
##### variable declaration
variable should start with character and may contain characters, digits or underscore (case is insensitive)

variables should be declared before use: variables are declared at the start of the program before any executable statements. 
For example:  
```fortran
real :: velocity   ! defines variable of real value
integer :: r, s, t ! more than one variable, separated by commas
implicit none
```

**implicit none** statement declares that *all variables must be defined before use*. It should always be included

##### variable options
we can give difference options in the variable declaration followed by comma `,` after variable type, until '`::`':
```fortran
real, parameter :: g = 9.8
```

##### variable types
| kind | example |
| -- | -- |
|integer | |
|real||
|complex   |`complex, parameter :: i = (0,1)`|
|character |`character (len=10) :: word` |
|logical   |`logical :: l1 ; l1 = x > 1.0`|
For character type, length need to be declared to allocate memory, 
  
### Internal functions
Fortran has various built-in mathematical functions, they are listed here [[fortran built in functions]]




### Logical controls
##### If statement
```fortran
! inline if
if (logical_expression) action 

if (logical expression) then
	action
else if ( expression ) then
	action
else
	action
end if
```

Logical expression operators:
```fortran
.lt. equivalent to <
.le. equivalent to <=
.eq. equivalent to ==
.ge. equivalent to >=
.gt. equivalent to >
.ne. equivelent to /=
.not.
.and.
.or.
```


Named if: we can name the if clauses by `name:if`, for example:
```fortran
outer: if (a /= 0.0) then
	inner: if (d < 0.0) then
		write(*,*) ’Invalid input data d negative’
	else inner
		x = b * sqrt(d) / a
	end if inner
else outer
	write(*,*) ’Invalid input data a zero’
end if outer
```

##### Loops
A fortran for loop has the following structure:
```fortran
do var = start, stop, [,step]
	action
end do
```
- `var` is an integer variable and need to declared before hand.
- `start` and `stop` is the initial and final value
- `step` increment, otherwise just unity
- to exit, use the exit command `if (n>10) exit`

##### Do while
```fortran
do while (conditions)
	actions
end do
```

### Arrays
##### Declare a array
To define a matrix or array, give the dimension in the parentheses. Each element of the array can be addressed by the index, and the index *starts at 1*. For example:
```fortran
real :: v(3) ! a vector
real :: a(3,3) ! a matrix
real :: x ! number

do i=1, 3
	x = x + v(i) * v(i)
end do
```
Arrays can also specified by dimension options
```fortran
real, dimension(10,11) :: a
```

##### Declare array of unknown size
we can define array of unknown size with *allocatable* property, but we need to specify a certain shape (dimension). We also need to deallocate the memory after usage. 
```fortran
! to define an array of unknown size
real, dimension(:), allocatable :: a
integer m = 10

allocate(a(m))
a = 0.0 ! assign value automatically assign all the elements
deallocate(a)
```

##### Selection and slicing
Most of the normal operation can be applied in an element by element fashion. 

Example of slicing and element selection:
```fortran
Z(m:n) ! is an array of length n-m+1 from Z, starting at m and end at n
Z(m:n:c) ! increment by c
X(1:5) = Y(2:6) ! copy the value of y(2:6) to x(1:5)
a(2,:) = z ! copy the vector z to second row of a  
```

Using where and elsewhere: 
```fortran
real, dimension(1000) :: a

where (a > 0.0)
	a = log(a)    ! the operation is on the whole array but only parts satisfying
elsewhere ! the condition is modified
	a = 0.0
end where
```

##### Matrix operations
Fortran has the following method built-in

| function | behavior |
| -- | -- |
| dot_product(A,B) |  inner product of two vector
| matmul(A,B) |  matrix multiplication
| maxval(A) |  |
| minval(A) |  |
| product(A) | product of the elements of an array
| sum(A) | sum of the elements


### File I/O
##### Read and write
Fortran use number to specify which stream to write or read:
```fortran
read( stream, label [, end=end][, err=err]) list
write(stream, label) list
```

- `stream` is a number previously linked to a file, a character variable or `*` *, where `*`* indicate the default value (terminal) if stream is a character vaiable, the result is stored in that variable
- `label` is a number of a format statement, or `*` for the free format
- `list` a list of items to be transferred, separated by commas, text string is enclosed in quotation marks
- `end or err` controls moves in the even that end of data is reached or error is encountered

##### Defining a format
We can define a label to represent a format by an integer:
```fortran
label format (format descriptors)
```
- label is an integer, which will be used in the read or write statement
- format descriptors is a comma separeted list of items describing how the output is to be presented, possibly including text items. The latter should be enclosed in sing implicit nonele quotation marks as in character strings

This table lists how formats are specified:

| string | result |
| -- | -- |
|nIw | to output integer
|nFw.d | to output real or complex number in fixed point form
|nEw.d | to output real or complex in exponential form
| nESw.d |  output in scientific form
| nENw.d |  output in engineering form
|Aw |to output non-numerical item (character)
| Lw | to output logicals 
| nX | to print n spaces
| / | print a blank line


Here I, F, E, A specifies type, and n, w, d specifies the number of repeation, width of the field including the signes and spaces, and the number of digits. For example:
```fortran
write (stdout, ‘(1x, a46, 10x, f8.3, 13x, a1)’) ...
```

##### Open file streams
```fortran
open(stream, file=name, err=escape, action=action, iostat = ierr )
! stream  : the identifier which appear in read or write statement
! escape  : statement which control is transferred
! action  : one of “read”,“write” or “readwrite”
! name    : filename
```

For example:
```fortran
program fileio
implicit none
integer :: i

open(20, file=’cubes.dat’)
do i=1,100
	write(20,1) i, i*i, i**3
end do
close(20)

1 format(i4,i6,i8)   ! define a format
end program fileio
```

##### More on File IO functions
See this short notes [[fortran IO functions]]

##### Functions related to strings:

| function | result |
| -- | -- |
|`trim` |removes trailing blank characters of a string
|`adjustl` |left adjust a string by removing the leading spaces
|`cycle` |The cycle statement causes the loop to skip the remainder of its body, and immediately retest its condition prior to reiterating.
|`index(string, substring)` |find the starting position of a substring in a string, In fortran, index start from 1


##### Namelist
Fortran namelist namelist provide a convenient way to read variables from file.


To define a namelist, use: 
```fortran
NAMELIST /name/ variables
```
where *name* is the name of the namelist, *variables* are a list of variable names. The namelist file should contain the name starting with `&name` and end with `/`

```fortran
! ** example
real :: a,b
integer :: i,j

NAMELIST /input/ a,b,i,j ! defines a namelist

open(10,file=‘data.dat’)
read(10,nml=input) ! read file according to namelist, refering with “input”
write(*,nml=input) ! namelist can also be written
close(10)
end

! namelist data file
&input
b=12.3
i=4
a=13.2
j=12
/
```

  


  

### Functions and Subroutines
##### Subroutines vs. Functions
*Subroutines* and *Functions* are the main way to structure fortran programs. The main difference between them is that functions return a value but subroutine does not.
In general:
- the type of the function name must be declared both where it is defined and in the segment from which it is called
- Functions are called like the intrinsic functions but subroutins are accessed by call

##### Functions
Each function starts with the keyword “function” and ends with “end function”. We call functions defined this way *internal functions*. Function appear in the program after the word `contains` which indicates the start of the definition. 
```fortran
function name(arg1,arg2,…)
! declarations, including those for arguments
actions
end function name
```
Within the function, the function name is treated as a variable, which is the value returned. The function name need to be declared as other variables:
```fortran
function f(x)
	real :: f, x
	f = x**3 + x
end function f
```
We can use return statement to terminate a function or subroutine

##### Subroutines
Subroutines are similar to function but do not return any values but they act on the program directly: 
```fortran
subroutine name(arg1,arg2,…)
! declarations, including those for arguments
actions
end subroutin name
```
Subroutines are defined after contains. The following program use a subroutine:
```fortran
program swapmain
	implicit none
	real :: a, b
	read(*,*) a, b  ! Read in two values
	call swap(a,b)
	write(*,*) a,b

contains
	subroutine swap(x, y)
		real :: x, y, temp
		temp = x
		x = y
		y = temp
	end subroutine swap
end program swapmain
```

##### Local and global variables
We have the following rules in the scope of variables:
- variables defined within a given routine are local
- variable defined in the main program is available to all internal routine, therefore they are global
- to pass array of non-known size to function, use size() internal function to get the size of the array
- vaiable passing: what is passed to the subroutine are the pointers of the memory locations containing the calling arguments, not the actual values. As a consequence, the subroutine cannot tell the difference between a variable and array but it is possible that the compilers can catch the error

We can use `Intent attribute` can be used to protect the variables in the functions and subroutines:
```fortran
subroutine name(arg1,arg2,..)
real, intent(in) :: arg1
real, intent(out) :: arg2
! 
end subroutine name
```

Also, `save attribute` allows the value of an variable to be retained between successive calls to the routine:
```fortran
subroutine count(counter)
integer :: counter
integer, save :: count = 0
	count = count + 1
	counter = count
end subroutine count
```

### Modules
##### Defining a module
module allows the separation of codes between files. The module is incorporated in the program by `use` statement. The structure of a module file is usually:
```fortran
module name
	declaration
contains
	subroutines
end module name
```
The variables declared in the module before the contains statement are global to the module and *become global in any routine which use the module*.

##### Compile with modules
Suppose we have two file “main.f90” and “mod.f90”, we compile the program by:
1. we first compile the module file, using the -c option, `gfortran -c mod.f90`, which produce `mod.o` file containing compiled code, extra file `mod.mod` is also created.
2. compile the whole program using `gfortran -o main.x main.f90 mod.o`
3. if we have more than one module, we should compile separate module and `gfortran -o test test.f90 para.o func.o`

##### public and private attribute
Parameter declared in the module is *global* in the current module, but we can give it *private* or *public* attribute to determined if they can be used in other files:
- private: available only in the current module
- public: available in all program segments that include this module

##### Libraries
when compiling with library we must tell where to find the library code with some prameters eg: `gfortran -o ex ex.f90 -lnag` (see [[Intel Compilers#Using libraries]])

### Interface block
Interface block are used when the main program is calling another function or subroutine and it can check if the function or subroutine is provided with the correct variable type.

Basic structure of interface block is:
```fortran
INTERFACE
	Function vector_add(a,b,c,n)
		real, intent(in) :: a(:),b(:),n
		real vector_add(size(a))
	end function vector_add
END INTERFACE
```

Interface block can be used to overload functions by specifying a name as a procedure to be called in the program. It contain different functions for different input variable types. Either one of the function will be actually called: 
```fortran
Interface vector_add
Function ivector_add(a,b,n)
	Implicit none
	integer, intent(in) :: a(:),b(:),n
	integer ivector_add(size(a))
end function ivector_add

function rvector_add(a,b,n)
	implicit none
	real, intent(in) :: a(:),b(:),n
	real rvector_add(size(a))
	end function rvector_add
end interface vector_add
```

As an example, the following shows an interface of mpi:
```fortran
interface comms_bcast
	module procedure comms_bcast_int
	module procedure comms_bcast_logical
	module procedure comms_bcast_real
	module procedure comms_bcast_cmplx
	module procedure comms_bcast_char
end interface comms_bcast
```

### Numerical precision and variables
##### kind
Accuracy in fortran variable accuracy can be specify by kind parameter. Each variable type correspond to a predefined type. 

The following function are related to `kind`:

| string | result |
| -- | -- |
|`kind(x)` |return the kind of the argument x
|`selected_int_kind(n)` |return the kind necessary to hold integer as large as 10^n
|`selected_real_kind(p[,r])` |return the kind necessary to hold real as from `10^-r` to `10^r` with precision `p`

Setting variable to a specific kind:
1. we need to get the proper kind parameter, `dp = kind(1.0d0)`.  (1.0d0 is a double precision format)
2. we can now use dp to specify new variable with high precision:
	```fortran
	integer, parameter :: dp=kind(1.0d0)
	real(kind = dp) :: x, y
	complex(kind = dp) :: z
	real(kind = dp), dimension(30) :: table

	! to specify a floating point constant with dp as suffix directly
	z = 1.0_dp
	```

  

### Others generic functions
##### continue
The continue statement is an odd statement in FORTRAN. It is an executable statement but it takes no action in the program. It’s primarily used as a *place holder* to span gaps created between branches or loops and the rest of the program.

##### goto
goto statement transfer control within a program [ref](http://userweb.eng.gla.ac.uk/peter.smart/com/com/f77-jump.htm)

##### statement label
Statement labels can be used to *mark positions* in the program to which control can be passed. Integer numbers in the range of 1-99999 can be used and they must be placed in column 1-5 at the start of the statements to transfer. As a common practice, put label on `CONTINUE` statement only, so that the only purpose of `goto` will be to transfer control.

```fortran
if (transport .and. tran_read_ht) goto 3003
...

3003 continue
! if the condition is true,
! goto will directly gump to the position of 3003 and continue,
! without executing all the code in the middle
```

##### Other functions:
`cpu_time(t)` return a real value representing the time passed
`CALL exit()` exit is a function call that also accept integer number as parameters (exit code)
- `exit(0)` → normal exit
- `exit(1)` → error occur (positive integer)