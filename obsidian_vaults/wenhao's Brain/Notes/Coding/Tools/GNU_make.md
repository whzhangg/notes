# GNU Make

Created: January 13, 2022 11:10 AM
Description: Use the Power of GNU Make to Build Anything
Tags: bash

This is notes from the book by *Robert Mecklenburg,* ISBN: 978-0-596-00610-5

**Managing Projects with GNU Make**

## Basics
#### Basic Syntax

**Invoking make**
GNUmake assumes:
- all source code and make description file are located in a single directory
- make description file is named “makefile”, “Makefile” or “GNUMakefile” and is in the current directory
- `--just-print (-n)` option tells make to only display the command it will execute

**Comments**
- Comments start with `#`, leading space before the comments are ignored.
- `#` in the command line is passed to subshell for execution.
- Long lines can be continued using backslash `\`

**Rules**
- Each makefile contain a set of rules used to build a problem. The first rule is used as the default rule
- A rule consist of three parts: target, prerequisites and commands. If no prerequisites are listed, then targets are only updated if it does not exist.
- All prerequisites are made in sequence.
- Each command must begin with a tab character, which is passed to a subshell for execution. Command lines prefix with an `@` character will not be echoed, only its result are printed when command is run.

As an example:
```makefile
# first target as default target
count_words: count_words.o lexer.o -lfl              
    gcc count_words.o lexer.o -lfl -o count_words    
# when a reprequisite of theform -l<name> is seen, make will search for the file 
# in the form libNAME.so or libNAME.a in library folders

count_words.o: count_words.c
    gcc -c count_words.c
    
lexer.o: lexer.c
    gcc -c lexer.c
    
lexer.c: lexer.l
	flex -t lexer.l > lexer.c
```
    
**More on commands**
It should be noted that *command blocks are not a single script*. It seems that *each line is carried out by a subprocess separately*. This is important when it is necessary to change folders, as shown in the following case. Also see [this post](https://stackoverflow.com/questions/1789594/how-do-i-write-the-cd-command-in-a-makefile)
```makefile
# This will not work, pdflatex command is still execute in the current directory
%.pdf: %.tex
    cd $(<D)
    pdflatex $(<F)
    cd -
    
# this works as expected
%.pdf: %.tex
    cd $(<D); pdflatex $(<F); cd -
    
# this also works fine, using \ to breakline
%.pdf: %.tex
    cd $(<D); \
    pdflatex $(<F); \
    cd -
```

## Rules
Make manage the dependence by developing a *dependency graph*.
#### Wildcards in rules
make support wildcards which are are identical to bash:
- `~` represnet to current user’s home directory
- `*` expand to all characters, `?` represent any single character, `[...]` represent character class

*Wildcards in target or prerequisites are expanded by make, wildcards in command are expanded by subshell*. Therefore, shell will expand the wildcards much later than the wildcards in make is expanded, therefore the expansion could be different.

#### Explicit Rules
Explicit rules specify particular files as targets and prerequisites. 

- if multiple targets are given, they are interpreted as two separate rules with the same dependence and are handled independently 
    ```makefile
    vpath.o variable.o: make.h config.h getopt.h gettext.h dep.h
    # is equivalent to:
    vpath.o: make.h config.h getopt.h gettext.h dep.h
    variable.o: make.h config.h getopt.h gettext.h dep.h
    ```
- if multiply rules are given for the same targets, their prerequisites are appended together by make. However, they can be made explicitly different if we use double-colon. *Then, both will be executed when we call make*
    ```makefile
    file-list:: generate-list-script                
    		chmod +x $<                                 
    		generate-list-script $(files) > file-list  
    
    file-list:: $(files)
    		generate-list-script $(files) > file-list
    ```
    
#### Phony Targets and Special Targets
*Targets that does not represent file* are called phony targets.
Make is unable to distinguish phony targets from a file. i.e. If the phony pargets name coincide with a file, make will try to update the file

*.PHONY declaration* tell Make that a target file is not a real file:
```makefile
.PHONY: clean      # clean is known to make as a phony target
clean:
    rm -f *.out
```
    
*Phony target is always out of data and will always cause target to be remade* if they are used as prerequisites. But they are suitable to be used as prerquisites for other phony targets, since phony targets will always be made. Consider the following example:
```makefile
.PHONY: make-documentation 
make-documentation: df
    javadoc ...
    
.PHONY: df     # df will be a phony target that will be always made
df:
    df -k . | awk 'NR == 2 { printf( "%d available\n", $$4 ) }'
```

**Standard phony target**
The following table lists convention for phony targets:

| phony target | purpose |
| --- | ------- |
| all | build the application |
| install | create an installation of the application |
| clean | delete binary files generated |
| distclean | delete all generated file that is not in the original distribution |
| info | create a GNU info file |
| check | run tests |

**Other Special Targets**
a special target are phony targets that change make’s default behavior. The syntax of the special targets follow the normal targets `targt: prerequisites`. PHONY is a special target.
The useful special targets are:
    
|name | usage |
| --- | --- |
| .PHONY | the target is not files |
| .INTERMEDIATE | Prequisites will be identified as special files. Those files will be deleted automatically when make exits. If the file already exists when make considers updating the file, the file will not be deleted. |
| .SECONDARY | Prequisites will be treated as intermediate files but are not automatically deleted. |
| .PRECIOUS | make will not delete the precious files, even if the make process of those files are only half-way done |
| .DELETE_ON_ERROR | opposite of .PRECIOUS, target will be deleted if any command generated an error |

**Empty Targets**
Empty target refer to targets that is created as an empty file, usually have the following form:
```makefile
size: prog.o 
    size $^
    touch size
```
    
#### VPATH and vpath
- Make will only look in the current directory for its targets and prerequisites
- We can add search path to a make script by: `VPATH = ../src1 ../src2`  , which can be separated by space or colons. if multiple files have the same name, make will use the first one it encounter
vpath offer a pattern specific way to search for files, using the following syntax:
```makefile
vpath %.c src 
vpath %.l src 
vpath %.h include   
# different files are found in different folders
```

## Patterns and Pattern Rules
**Pattern**
- In make, `%` character represents any number of any character, similar to the wild card * in bash.
- A pattern with `%` is interpreted by make by finding the matching files.

**Pattern rules**
- a pattern rule looks like a normal rule but the stem of the file is represented by a % character. For example:
    ```makefile
    %.o: %.c
    	$(COMPILE.c) $(OUTPUT_OPTION) $<
    ```
- static pattern rules are pattern rule that only apply to a specific list of targets
    ```makefile
    $(OBJECTS): %.o: %.c
    	$(CC) -c $(CFLAGS) $< -o $@
    # $(OBJECTS) contain a list of targets, each will be made according to the 
    # given target rule: %.o: %.c i.e. the objects are matched with %.o and substituted
    ```

make contain many build-in implicit rules for C, C++, Fortran, TeX etc, which can be checked by: `make  --print-data-base` command. The build-in implicit rule applies when there is no command script supplied for a given rule, then make will search the built-in database to find suitable implicit rules.

## Managing libraries
Library can be linked into executable in different ways.
- List the library file on the command line: `cc count_words.o libcounter.a /lib/libfl.a -o count_words`
- `-l` option to omit the prefix and suffix: `-lfl`, in which case, compiler will search for libraries in the standard library directories. `-L` option indicate the directories to search and in what order, these directory will be added before system libraries and used for all `-l` options: `cc count_words.o -L. -lcounter -lfl -o count_words` will search library file: libfl.a in the current path

**Using libraries as prerequisites**
- Libraries can be referenced using standard filename or the `-l` syntax. With the `-l` syntax, *make* will search for libraries and substitute its value, as absolute path, into automatic variables related to prerequisites (such as `$^` or `$?`)
- For the `-l` syntax to work properly, the library file need to exist first. Make *will not* search rules to make the library file if it is supplied with the `-l` option.
    ```makefile
    # this will not work:
    count_words: count_words.o -lcounter -lfl 
    		$(CC) $^ -o $@
    
    libcounter.a: libcounter.a(lexer.o) libcounter.a(counter.o)
    ```
    
## Variables
**Workflow of make**
when *make* runs, it perform its job in two phases. 
1. In the first phase, make read the Makefile and any files that are included. At this time, variables are loaded into make’s internal database
2. make analyze the dependency graph the determines the target that need to be updated. Then, *make* execute command scripts needed

#### Variables, assignment and expansion

**Basic rules for make variables**
- The only characters that are not allowed in a variable name are `:, # and =` and they are **case-sensitive**.
- Variables are empty if they are not defined, which can be used as place holders for user customizations.
- Variables with more than a single character should be surrounded by `$()` or `${}`, both is equivalent but parenthesis is more common today, Single character variables names does not require parentheses.
- Variable values consist of all the words to the right of the assignment symbol. *Leading space are trimmed but trailing spaces are not trimmed*

**Simply expanded variables**
- simply expanded variables are defined with `:=` operator, such as `MAKE_DEPEND := $(CC) -M`.
- In this case, its righthand side is expanded immediately upon reading this line. The text is saved to the left.

**Recursively expanded variables**
- defined by the equal operator `=`, its righthand side is stored directly as the value of the variable without evaluating or expanding it. (**lazy expanded**).
- The evaluation is deferred until the variable is actually used. Therefore, assignment can be out of order:
    ```makefile
    MAKE_DEPEND = $(CC) -M 
    ...
    CC = gcc    # value of MAKE_DEPEND will be correct
    ```
- each time the recursive variable is used, its righthand size is re-evaluated

**Conditional variable assignment**
- Using assignment operator `?=`, the variable will be assigned only if the variable does not yet have a value.

**Append assignment** 
- += operator append text to the current existing variable (variable have empty value if they do not already exist)

#### Automatic variables and standard make variables

Automatic variables is local for command scripts of each rule). For more, see [Manual page of Make](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html)

The following Automatic variables are defined by Make:

|name| content |
| --- | --- |
| $@ | filename of the target |
| $% | filename element of an archive member specification |
| $< | filename of the first prerequisite |
| $? | name of all prerequisites that are newer than the target, separated by space |
| $^ | The filenames of all the prerequisites, separated by spaces but does not include duplicate filenames |
| $+ | Similar to $^, this is the names of all the prerequisites separated by spaces, except that $+ includes duplicates |
| $* | stem of the target, typically the filename without its suffix. (this can only be used in implicit rule, i.e., pattern rules) |

**Modifier**
- `D` symbol can be appended to the automatic variables to obtain only the *directory portion* of the filename: `$(<D), $(@D)`. ( Note that for variable with two character, `()` are necessary)
- `F` symbol obtain only the file portion of the filename

Automatic variables are set by Make after a rule has been matched with its target and prerequisites. *Therefore they are only available at the command part.* (variables are not wild cards, which is expanded at command execution)

**Standard make variables (make variables that are set by make)**

These variables are defined by make automatically during the make process:

|name | content |
| --- | --- |
| MAKE_VERSION | the version number of make |
| CURDIR | current working directory of the make process. -directory option will change the make directory before make search for Makefiles |
| MAKEFILE_LIST | contains a list of each file make has read, including the makefile, include directories |
| MAKECMDGOALS | contains a list of all the target specified on the commandline when current execution of make is started |
| .VARIABLES | contain a list of name of all variables defined in makefile that make read so far |

#### Macros

For duplicate command scripts, we can pack them in a *macro* created by *define* clause. Macro is similar to variables in usage, although variables are defined by assignment but macro is defined by “define”. The following script define a macro called create-jar
```makefile
define create-jar
	@echo Creating $@...
	$(RM) $(TMP_JAR_DIR)
	$(MKDIR) $(TMP_JAR_DIR)
	$(CP) -r $^ $(TMP_JAR_DIR)
	cd $(TMP_JAR_DIR) && $(JAR) $(JARFLAGS) $@ . 
	$(JAR) -ufm $@ $(MANIFEST)
	$(RM) $(TMP_JAR_DIR)
endef

$(UI_JAR): $(UI_CLASSES) 
	$(create-jar)         # create-jar is used as normal variable.
```

#### Target and Pattern specific variables
We can define target specific variables, which will only be effective inside a given rule for making the targets
```makefile
gui.o: CPPFLAGS += -DUSE_NEW_MALLOC=1 
gui.o: gui.h
    $(COMPILE.c) $(OUTPUT_OPTION) $<     # compile.c use CPPFLAGS
```

`CPPFLAGS` are build in variables and is meant to contain options for the C preprocessor. Using the target specific assignment, CPPFLAGS will have new values in addition to its original contents and nd when gui.o is finished, *CPPFLAGS will revert to its original value*.

#### When variables are expanded and where variables come from

**Expansion rules**
The expansion rules are summarized as follows (the left hand side is expanded immediately means that when they are used, they will be immediately expanded)
- For variable assignments, the left hand side of the assignment is always expanded immediately when make reads the line during its first phase.
- The righthand side of `=` and `?=` are deferred until they are used in the second phase (after all files are read by *make*).
- The righthand side of `:=` is expanded immediately.
- The righthand side of `+=` is expanded immediately if the lefthand side was originally defined as a simple variable. Otherwise, its evaluation is deferred.
- For macro definitions (those using define), the macro variable name is immediately expanded and the body of the macro is deferred until used.
- For rules, the targets and prerequisites are always immediately expanded while the commands are always deferred.

**Where variables come from** 
1. Makefile or any files that are loaded by *make.*
2. Command line. Variables can be supplied in the command line, when make in invoked. For example: `make CFLAGS=-g CPPFLAGS=’-DBSD’`. Assignment from command line override the values from the environment and in the make file. 
3. Environment. All variables from the environment are automatically defined as make variables. the variables here has low precedence. Environment variables can override makefile variables usi `--environment-overrides` option. 
4. Automatic variables are created before executing the command script of a rule.

## Conditional Processing
Parts of the makefile can be omitted or selected with **conditional processing directive**. The syntax is as following

```makefile
if-condition         
		lines            
[else]               
		other-lines     
[endif]               
										 
ifeq "a" "a"
		# These are equal
endif
```

if-condition can be one of the:
1. `ifdef variable-name or ifndef variable-name` which test if variables exist, or 
2. `ifeq test or ifneq test`, where test can be expressed as `"a" "b"` or `(a,b)` for two variables, to test if their values are equal.

## Include
- `include` statement will include other files (make header file or automatically generated file), for example:  `include definitions.mk`
- include directive can be given any number of files and wildcards, variables are also allowed.
- when make encounter an include, it expands the wildcards and variable references in the line, and then tries to read the include file.
- If the file does not exist, make will continue to read the rest of the file. then make will look at any rule to update the include file. If any match is found, make will produce the target and then completely restart: it will clear its internal database and rereads the entire makefile. Finally, if no match is found, make terminate with an error.
- Using an include directive before the first target might change the default goal. If the include file contain any targets, those targets will become the default goal for the makefile.