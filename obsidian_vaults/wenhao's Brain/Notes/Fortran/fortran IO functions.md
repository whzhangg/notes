### File IO
##### Open  
Open connect an existing external file to a unit, or create a file and connect it
```fortran
open (u, parameters)
```
where u is a integer file identifier

```fortran
! parameters:
FILE 	 ! filename, character expression
IOSTAT 	 ! io state specifier, (positive integer if error occur, negative if EOF occur)
STATUS 	 ! NEW -> if file does not exist and is to be created
		 ! REPLACE -> overwrite an existing file or create file if not exist
		 ! SCRATCH -> the file is to be deleted at the end of the program or by CLOSE
		 ! OLD -> the file to be opened but not replaced
POSITION ! REWIND -> open in the begining
		 ! APPEND -> positioned at the EOF
		 ! ASIS -> position remain unchanged
BLANK
DELIM
ACCESS
FROM
```

##### Close
Disconnect a file from a stream number
```fortran
close(u [,STATUS=sta, IOSTAT=ios, ERR=s])
```
Parameters:
```fortran
u 		! identifier of the stream
sta 	! determine how file is disposed
		! KEEP -> the file will be kept
		! DELETE -> the file will be deleted
ios 	! I/O state specifier
s 		! error specifier
```

##### Read
```fortran
read (unit, [,fmt,iostat,rec,end,err] ) iolist
```
Parameters:
```fortran
fmt=f 	! format identifier
ios 	! io state specifier
rec 	! record number to be read
end 	! statement label for end of file processing
iolist 	! list of variables
```

##### Inquire
Inquire is an statment that return information about a file
```fortran
inquire(u, specifier)
inquire(filename, specifier)
```
Parameters
- `u` the file identifier
- `filename` the filename
- `specifier` a list of information that you inquire

Specifiers are one of the following:
```fortran
ERR 			! integer number
EXIST 			! logical
OPENED 			! logical
NAMED 			! logical
ACCESS 			! ‘DIRECT’ or ‘SEQUENTIAL’
SEQUENTIAL 		! ‘yes’, ‘no’ or ‘unknown’
DIRECT 			! ‘yes’, ‘no’ or ‘unknown’
FORM 			! ‘formatted’ or ‘unformatted’
FORMATTED 		! ‘yes’, ‘no’ or ‘unknown’
UNFORMATTED 	! ‘yes’, ‘no’ or ‘unknown’
NAME 			! name of the file
BLANK 			! ‘null’ or ‘zero’
IOSTAT 			! error number
NUMBER 			! unit number (identifier)
RECL 			! length
NEXTREC 			! next record number
```

  
