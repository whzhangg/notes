# Intel Compilers

Created: October 1, 2021 7:14 PM
Description: described some options using the interl mkl and compilers
Tags: Programming, c++, fortran

For intel MKL, see this "incomplete" note: [[MKL Libraries]]

#### Using libraries

There are two kind of library files:
1. `.so`  (shared object)
	A library that is automatically linked into a program when the program starts, and exists as a standalone file. The library is included in the linking list at compile time (ie: `LDOPTS+=-lmylib` for a library file named mylib.so). The library must be *present at compile time, and when the application starts.*
2. `.a`   (static library)
	A library that is merged into the actual program itself at build time for a single (larger) application containing the application code and the library code that is automatically linked into a program when the program is built, and the final binary containing both the main program and the library itself exists as a single standalone binary file. 
	The library is included in the linking list at compile time (ie: `LDOPTS+=-lmylib` for a library file named mylib.a). The library must be present at compile time.

**Static library**
Creating a static library:
```bash
ifort -c source1.f90 source2.f90 source3.f90
xiar rc my_lib.a source1.o source1.o source1.o
```
The first line creates the object file `source1.o` and the second line create the actual library file with xiar tool

Using static library (
We use -L option at compile time to specify library file: 
```bash
ifort -L/home/mylib/ main.f90 my_lib.a
```

**Shared library**

Creating shared library:
```bash
ifort -shared -fpic octagon.f90 -o octagon.so
```
We can Install the shared library with shared libraries by setting the environmental variable *LD_LIBRARY_PATH*

#### Using the Intel compiler (ifort)

Syntax of the ifort command is  `ifort [options] filenames`. `ifort` command will invokes both the compiler and linker. the ifort driver does the following things:
1. call the fortran compiler to process fortran files
2. pass linker options to the linker
3. pass object files created by the compiler to the linker
4. pass libraries to linker
5. call the linker to create executables or library files

**Input files**
compiler will search input file in PATH or working directory, or by specifying directory path

**Options**
- option is specified by one or more letters preceded by `-`.
- options can *not be combined* to a single `-`, each options need to have its own `-`.
- options can take arguments, if space is included in a string, they need to be inclosed in quotation marks
- arguments and options can be combined or a space between option and its arguments can be entered
- options are *case-sensitive*
- option names can be abbreviated as long as they are uniquely identifiable
- compiler options *can appear in any order*

**Environment Variables used by ifort**

| variable | meaning |
| --------- | -----------|
|PATH               | directory to search for binary executables|
|TMP, TMPDIR, TEMP | location to store temporary files, default is /tmp|
|LD_LIBRARY_PATH    | location for shared objects ( .so )|
|CPATH              | specifies the path for include and module files|
|LIBRARY_PATH      | specifies the path for libraries to be used during the link phase|
    

**List of common ifort compiler options**
Here we gather some common compiler options. Note that each options has its own syntax, for example `-Ldir` or `-march=processor`, therefore, *one way to give an option does not necessary apply to other options* and it's better to check individually about the compiler options.

| option | meaning |
| -- | -- |
|-c            | prevent linking (create only object files etc.)
|-dryrun       | driver tool commands shown but not executed
|-fast         | maximize speed across entire program
|-help         | display all options
|-I (-Idir)    | (i) specified an additional directory for the include path
|-l (-lstring) | (l) tell the linker to search for a specified library when linking
|-L (-Ldir)    | (L) tell the linker to search for libraries in a specified directory before searching standard directories
|-mkl          | enable intel mkl option
|-module       | directory where module files should be placed when created and where they should be searched for 
|-O            | (uc-o) specifies the optimization for applications
|-o            | (lc-o) specifies the name of output file
|-X            | remove standard directories from the include file search path
