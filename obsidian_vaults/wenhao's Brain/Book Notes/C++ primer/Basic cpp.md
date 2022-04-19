# Getting Started in cpp
### Basic grammar
##### main function
a c++ program must contain one or more functions, operating system runs c++ by calling main()
```cpp
int main() { return 1; }
```

##### standard I/O
c++ does not define any statements to do I/O, but includes a standard library for that "iostream"
- istream for input streams
- ostream for output streams

##### include
Any program that use a library must include its header, `#include` must written on a single line and name must appear at the same line. For example:
```cpp
#include <iostream>
#include "sales_item.h"
``` 

for a custom defined class, we include a header `file.h`, we enclose the custom defined files with `" "` if library are not standard (otherwise < >). 

##### using names from standard library
Prefix `std::` indicates that names are defined inside "namespace" named "std", all names defined by standard library are in the std namespace . The `::` is the scope operator 

##### Commenting in c++
Single line comment is done in this way: `// comments`
For multiple line: `/* comments */`. A commenting style for multiple line is:
```cpp
# / *
# * comment 1
# * comment 2
# * /
```

##### statement block
a block is a sequence of statements enclosed by `{ }`, it is a statement and can be used wherever a statement is required.

### Basic structures
##### while loop
```cpp
while (condition) {
	statements;
}
```

##### for loop
```cpp
for (int i = 1; i < 10; ++i) {
	sum += i;
}
```
Each for statement has two parts: a *header* and a *body*. Header controls how the body is executed, consists of three parts:`(init-statement; condition; expression)`

##### if statement 
```cpp
if ( condition ) { 
	statements; 
} else { 
	otherwise; 
}
```

##### using class
Every class defines a type. To create an instance of a class, we can use: `sales_item item`, which define item to be of sales_item.

Member function is a function defined as part of a class. The dot operator `.` is used to access a member function
