**Basic Rules**
- `#` lines are ignored
- patterns can start with `/` to avoid recursivity
- directory can be specified by ending the pattern with `/`
- negate a pattern by starting it with `!`

**Regular expressions**
- \* match zero or more characters
- [...] match any character inside the brackets, [0-9] [a-z] is applicable
- ? matches a single character
- two asterisks ** match nested directory

**Example of .gitignore file**

```bash
# ignore all .a files 
*.a
# but do track lib.a, even though you're ignoring .a files above 
!lib.a 
# only ignore the TODO file in the current directory, not subdir/TODO
/TODO
# ignore all files in any directory named build
build/
# ignore doc/notes.txt, but not doc/server/arch.txt 
doc/*.txt
# ignore all .pdf files in the doc/ directory and any of its subdirectories 
doc/**/*.pdf
```
