# Powershell
Created: October 3, 2021 2:42 PM

### Basics
Some basic points of powershell language is summarized here:
- Powershell is not case sensitive
- We separate command in the same line using " `;` ", same as bash

##### General utility method
Some of the general commands are listed as follows:

```powershell
Get-Help [command]
```
Get the help for the following command, we can also use `Update-Help` to download the help documents.

```powershell
Get-Member [[-Name] <string[]>] [-InputObject <psobject>] 
           [-MemberType <PSMemberTypes>] [-View <PSMemberViewTypes>] 
		   [-Static] [-Force] [<CommonParameters>]
```
All the return in powershell is *objects*, `get-member` *list what we can do with them*. For example, the command `(ls) | Get-Member` takes the output of the command "ls" and return the properties of the object.

```powershell
Get-Command [[-Name] <string[]>] [-CommandType <CommandTypes>] 
            [-TotalCount <int>] [-Syntax] [-ShowCommandInfo] [-All]
```
Return the details of the available commands

`-syntax` option shows the syntax of the specified command, for example `get-command get-childitem -syntax`

```powershell
().GetType()
```
Get the type of the object, For example: `(ls)[0].GetType()` returns "system.IO.FileSystemInfo"

`Get-Process / Stop-Process` as the name implies, get the process information and can stop process by specifing `-id`
```powershell
Get-Process n*     
PS> 239      16    11192      22896       0.42   9676   1 notepad++

Stop-Process -id 9676 
PS> stop the notepad++ process
```

`Get-Alias` get the alias

`clear-host (cls)` clean screen

### General Options
##### `-WhatIf/-Confirm` option
They are switch parameters of a command, meaning that they are used as a parameters that most commands support. 
- `-WhatIf`: shows the consequence of a command, without actually carrying out the action. For example: `Stop-Process -id 100 -Whatif`
- `-Confirm`: shows WhatIf, and *further let you choose if you want to continue or not*.

```powershell
# For example 
Stop-Process -id 100 -Confirm 
PS> Confirm: are you sure [Y] yes  [A] Yes to All  [N] No ...
```

##### `-ErrorAction (-ea)` option
This command parameter that specify what to do when there is error, We have the following choices:
```
Ignore - 4, Inquire - 3, Continue - 2, Stop - 1, SilentlyContinue - 0
```


**variables**

- By default, variables don't need to be declared before use, in all case variable is preceded by `$` sign
- Important special variables (automatic variables)
    
    ```powershell
    $^, $$               # the first/last token of the last line input
    $?                   # exit state of the last statement
    $Args                # the parameters passed to function and scripts
    $Error               # the error object saved if an error is occured
    $True, $False, $Null # the boolean object TRUE or FALSE, the NULL object
    $OFS                 # output field separator for converting array to string
    $_                   # current pipeline object, can be used in script blocks and filters
    $input               # input that is pipelined to a function
    ```
    
- Type of variable: use the form `[int]$a = 56` to asign type to variables
    
    ```powershell
    [int], [long]        # signed integer 32 / 64 bit long
    [bool]               # true / false
    [string]             # string of unicode characters
    [char]               # single unicode character 16 bit 
    										 # [char]$a=66 equivalent to [char]$a='B'
    [single], [double]   # floating point number 32 / 64 bit long
    [array]              # array
    ```
    
- Constants have value cannot be changed and they cannot be deleted, to create constants, use:
    
    `Set-Variable -name a -value b -option constant`
    

I**f statement**

condition is enclosed by parenthese (c style), action is closed by `{ }` (script block)

```powershell
if ( condition ) {
  action 
} elseif ( condition ) { 
  action
} else { 
  action 
}
```

Condition should be a boolean type, like `5 -lt 4`, `test-path C:/noneexsist` or `$True`, parathesis around condition is necessary

Comparsion operator used in condition is similar to python

```powershell
# Equality
		-eq, -ne, -gt, -ge, -lt, -le
# Matching
		-like, -notlike    # match wildcard pattern
		-match, -notmatch  # match regular expression
# containment
		-in / -notin       # test if the value is contained in a collection
    -contains/-notcontains  # the reverse of -in, test if a collection has the given value
# replacement
		-replace           # replace a string pattern
# type
		-is/-isnot         # return true if both object are the same type
```

**While**

```powershell
while ( condition )
{
		action
}
```

**For**

for is similar with the c++

```powershell
for ( init ; condition ; repeat ) {
		action
}
```

 **For each**

Foreach statement is similar to the bash style

```powershell
foreach ( $i in $args )
{
    action ($i ...)
}
```

`Break` statement finish current loop 

`Exit` statement end the script

**Foreach-object**

used to perform an operation on each item [ [https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/foreach-object?view=powershell-7](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/foreach-object?view=powershell-7) ]

when combining variable $_ it can treat the each object passing the pipline

`(ls).name | foreach-object { echo "* $_" }  or (ls) | foreach-object { echo "* $_.name" }`

**Script block**

a statement block `{ }` is treated as a unit of code, and returns the output of all the commands in the block, either as a single object or as an array

[ [https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_script_blocks?view=powershell-7](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_script_blocks?view=powershell-7) ]

Notice

- a script block can accept arguments and return values, it can also accepting parameter
- Example
    
    ```powershell
    $a ={ param($p1, $p2)
          "p1: $p1"
          "p2: $p2"
        }
    
    &$a -p2 "First" -p1 "Second"
    ```
    

**Double / single quotation, escape character**

- In powershell enviorment, the escape character is ` (backtick)
- Expanding string " " in which variables are expanded, literial string ' '

**Function**

Begin with the function keyword, followed by the name of the function

```powershell
function verb-noun
{
    action
}
```

Parameter can be specified by the positional arguments `$args` or several other ways

```powershell
Function verb-noun ($para1, [int]$para2) { 
	action 
}

# or

Function verb-noun {
	Param($para1, [int]$para2)
	action
}
```

**Filter**

- Filter is a special purpose function to operate on each object in a pipeline, can be defined as:
    
    ```powershell
    filter filtername {
    	action ($_ ...)
    }
    ```
    
- action can specify the setup process and the process
    
    ```powershell
    filter filternane {
    	begin { setting up }
    	process { action }
    }
    ```
    

Example

```powershell
filter IsToday
{
	begin {$dte = (get-date).date}
	process { $_ | where-object {$_.lastwritetime -ge $dte } }
} # where-object return the part satisfying the condition
```

`**$(command)**`

excuate this command and treat the result as a variable

**call operator "`&`"**

- allows you to execute a command, script or function
    
    Many times you can execute a command by just typing its name, but this will only run if the command is in the environment path. Also if the command (or the path) contains a space then this will fail. Surrounding a command with quotes will make PowerShell treat it as a string, so in addition to quotes, use the & call operator to force PowerShell to treat the string as a command to be executed.
    
    `& "C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"`
    
- Priority of execution: Alias > Function > Filter > Cmdlet > Application > ExternalScript > Script

**where-object (Alias ? )**

- Example: A filter to take out certain parts
    
    `ls | where-object {$_.lastwritetime -ls (get-date).date}`
    
- There are two different ways to construct where-object
    1. Use script block, as above. The `{ }` here act as script block, inside the script block, supply property name, operator and value, example as above
    2. Use property_name operator and value: `ls | where-object lastwritetime -ls (get-date).date`

**Global variable**

- If not specified, the variables are local and do not go into functions. to specify a global variable, we can use global prefix (similar to namespace in c): `$global:time = 2020`
- To refer it, both `$global:time` or `$time` is the same.

**Determine if given path is a file or directory**

`(Get-Item $path) -is [System.IO.DirectoryInfo]`

**Measure the execution time of command**

use get-history command

```powershell
PS> .\do_something.ps1
PS> $command = Get-History -Count 1
PS> $command.EndExecutionTime - $command.StartExecutionTime
```

**Path variable**

- path is stored in `$env:PATH` variable.
- The directory path is separated by `;`, to append a directory: `$env:path = "$env:path;C:/wenhao"`

**Robocopy**

- Robocopy is an solution for fast copy and backup, copy using multithread
    
    `robocopy original target [/options]`
    
- Options
    
    options start with '`/`'
    
    ```powershell
    /mir        # mirror a directory, the same files with same timestamp are skipped, 
    					  # modified files will be copyed, new directory will be created, 
    						# files in the target folder that no longer in the original folder will be deleted. 
    				    # i.e. it mirrors the directory correctory
    /e          # copy include subdirectory
    /purge      # delete folders/files that no longer exist in the source folder
    /log:filename  # write log to file
    /log+:filename # append log to file
    /xo         # do not overwrite if destination file exist and is the same or newer than the source
    /xn         # do not overwrite if destination file exist and is the same or older than the source
    ```
    

Ref [ [https://adamtheautomator.com/robocopy/#:~:text=Robocopy has a option](https://adamtheautomator.com/robocopy/#:~:text=Robocopy%20has%20a%20option%20) ]

**`().replace("string_to_replace","new_string")`**

Replace text string, as similar to `sed` in bash

For example `(get-content "text.txt").replace("one","two")`

note that the file is not modified, as it operates on the object, not the file itself

**powershell $args**

arbitrary arguements can be passed to powershell functions

```powershell
function test_args()
{
	Write-Host "here's arg 0: $($args[0])"
	Write-Host "here's arg 1: $($args[1])"
}

test_args foo bar
```

**Note** when you use a PowerShell variable in a string, PowerShell only substitutes the variable's value. You can't directly use an expression like $args[0]. However, you can put the expression within a $() sub-expression group inside a double-quoted string to get PowerShell to evaluate the expression and then convert the result to a string.