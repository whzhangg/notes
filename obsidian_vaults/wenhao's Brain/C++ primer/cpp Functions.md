
## Chapter 6. Functions

**Function basics**

- a function is a block of code with a name, its definition consists of:
    1. return type
    2. function name
    3. list of parameters
    4. function body
- call expression
    - we call a function through the "call operator" <- a pair of ( )
    - inside the ( ) is a comma separated list of arguments, used to initialize function
    - the type of the call expression is the return type of the function
- Function call does two things:
    1. initialize the function parameters from arguments, variables defined as parameter are created
    2. transfer control to that function

**Parameter and return type**

- arguments initialize the parameters, but we have no guarantee about the order of how arguments are evaluated
- parameter declaration must be separate
- parameter names are optional, but there is no way to use a unnamed parameter
- function **return type can not be array or function type**

**Local objects**

Parameter and variables defined inside a function is referred as local, and they "hide" declarations of the same name in outer scope. The body of a function is a statement block, which form a new scope

Automatic objects: object that exist only while a block is executing

**Local statistic object**

local variable whose lifetime continues across calls to function

initialized before the firt time execution defines the object and destroyed when the program terminate

( this is similar to save attributes in fortran)

**Function declaration**

- the name of the function must be declared before we can use it
- we can declare a function that is not defined as long as we do not use it
- a declaration only need three element: return type; function name; parameter type
- a function declaration has no function body, a **semicolon replaces** the function body
- there is no need for parameter names, but it can be used to help users
    
    For example: `void print(int i, int j);`
    
- function should be declared in header files and defined in a source file
- source file that defines a function should include the header of the declaration
- any source file that use the function need to include the function declaration

Funtion arguments

**Argument passing**

parameter are initialized in the same way that a variable is initialized, for example

```cpp
void func(int *i);
func(&j);             // initialized by int *i = &j;
```

Two types of parameter passing:

1. if parameter is a reference, then its bound to its argument. (passed by reference)
2. otherwise, parameter's value is copied. (including pointer) (passed by value)

if parameter is passed by value, then changes made to the vairable have no effect on the initializer

**Passing arguments by reference**

passing by reference is the prefered way to pass variables if it should not be changed inside a function, use **const**

**const parameters**

- top level const are ignored in the initialization
- we should use const reference when possible
- if we use reference, we cannot pass const, literal or any object that require conversion to a plain reference
    
    ```cpp
    int find_char(string &s, char c; int &occur);
    find_char("Hello World",'o',ctr);       // error, literal cannot convert to reference
    ```
    

**Array parameters**

we cannot copy an array, and when we use array, it is automatically converted to pointer Therefore, we cannot pass an array by value. **when we pass an array to function, we actually pass a pointer**

The following three array declaration are equivalent:

```cpp
void print(const int*);
void print(const int[]);
void print(const int[10]);
// all declares a function that take parameter as a const int*

int j[2] = {1, 2};
print(j);
```

As a result, **function don't know the size of the array, since they are seen as pointers**

We have three possible solutions (remember c++ does not check bound)

1. use a marker in the array to indicate the end of the array
2. pass pointer to the first and one past last element in the array
3. explicite passing a size parameter

**Vector as arguments**

[https://www.geeksforgeeks.org/passing-vector-function-cpp/](https://www.geeksforgeeks.org/passing-vector-function-cpp/)

Directly passing Vector object as function arguments will produce a copy of the vector. Therefore, we should pass the vector objects by reference:

```cpp
void func(std::vector<int> &vect)
{
   vect.push_back(30);
}

// calling the function:
std::vector<int> vect;
func(vect);
```

**Arguments of function main()**

command line options are passed to main in two parameters: `int main(int argc, char *argv[]) {...}`

argc: number of parameter passed

argv: an array of pointers to character strings

argv is an array, so it is also seen as a pointer, we can also use: `int main(int argc, char **argv) {...}`

with argv now a pointer to char 

For example: 

```cpp
> prog -d o ofile data1     // command line input
we have: argc = 5,

argv will be an array of 6 elements:
argv[0]="prog"      // main of the program
argv[1]="-d"
argv[2]="o"
argv[3]="ofile"
argv[4]="data1"
argv[5]=0           // one pass last, guaranteed to be 0
```

RETURN

**void**

a return without value is only used in void return type

a void function is not required to contain a return (an implicit return)

**Return value**

- every function that has a return type other than void must return a value, that is the same type, or can be converted to the return type
- values are returned the same way as parameters are initialized **return value is used to initialize a temporary at the call site**

**Return a reference or pointer**

a reference return type is given as:

```cpp
const string & shorter_string(const string &s1, const string &s2) {
		return s1.size() <= s2.size() ? s1 : s2;
}   // return is a reference to s1 and s2, no variables are copied
```

After function completes, its storage are freed, therefore **any reference or pointer that point to a local objects will become invalid**

```cpp
const string & manip() {
		if (...) return "Empty";        // error, "Empty" is a local temporary
}                                   // but return type is a reference
```

A function that return a reference can be lvalues

```cpp
char & get_val(string &str, string::size_type ix) {
		return str[ix];
}

get_val(s,1) = 'A';               // get_val return a reference
```

**Return from main**

main function can terminate without a return, in which case the compiler implicitly inserts a return of 0

**Returning a pointer to an array**

remember to define a pointer to an array, we use syntax:

```cpp
int (*p1)[10] = &arr;   // pointer to an array of ten int, we are defining a pointer
int *p1[10];            // a array of 10 pointers
```

if we want to define a function, we need `type (*function(parameter))[dimension]` For example:  `int (*func(int i))[10];`

**OVERLOAD**

**overload functions**

- functions that have the same name but different parameter lists and **appear in the same scope** are overloaded
- when we call those functions, the compiler will deduce which function to call
- overload function must differ in the number or types of their parameters
- it is an error if two function only differ by the return type

```cpp
record lookup(const account&);
record lookup(const phone&);     // note here acount are data types, not names
```

- there are three possible outcome when calling overloaded function:
    1. compiler find the best math
    2. no match         -> error
    3. ambiguous call   -> error

**Overloading with const**

- a top level const is ignored, so will not be considered as overload
    
    ```cpp
    record lookup(phone*);          // parameter is a pointer to phone
    record lookup(phone* const);    // a top level const pointer to int, const is ignored
    // the two definition is the same
    // (remember: int *const cur_err = &err_numb;     -> defines a const ptr )
    ```
    
- a low level const is distinguishable
    
    ```cpp
    record lookup(phone*);
    record lookup(const phonon *);  // a new function, take a pointer to a const
    ```
    
- we can pass a const object, or pointer to const, only to a const. the same is true for reference

**overloading and scope**

function is a name, it will be hiden if the same name is declared in a inner scope:

```cpp
string read();                // define read in the outer scipe
void print(const string &);
void print(double);           // overload print in the outer scope

void foobar(inv ival) {
		bool read = false;        // this defines read in the new scope, read() is hidden
		string s = read();        // so read() here is considered a bool variable, error
		void print(int);          // declares print, not a overload function
		print("value:");          // error, can not see the overload version
		print(3.14);              // ok, but 3.14 is converted to int
}
```

- overload function can be considered as a **single name**
- program search the current scope first for names

**Determining function matching**

this is done with the following steps:

1. identify the set of overloaded function              <- candidate functions
2. discard those that does not match the number of parameters or can not be converted        <- viable functions
3. program decide the best match, if not an exact one

There will be an overall best match if

- the match for each argument is not worse than other viable function
- at least one argument that match better than other viable function

**Function pointer**

we can define a pointer that points to a function, called function pointer

- For example: `bool length_compare(const string &, const string &);`
- To define a pointer that can point at this function, we declare a pointer in place of the function name: `bool (*pf) (const string &, const string &);` pf points to a function that take two const string & parameters and return a bool and is not initialized
- the `( )` is necessary, `bool *pf(const string &, const string &);` will define a function that return a pointer to bool type

**Using function pointer**

- when we use function name as a value, it is automatically converted to a pointer
    
    ```cpp
    pf = length_compare;    // pf now points to length_compare
    pf = &length_compare;   // equivalent
    ```
    
- to call the function pointed by the pointer, we can directly use
    
    ```cpp
    bool b1 = pf("sss","gggg");     // same as length_compare
    bool b1 = (*pf)("sss","gggg");  // equivalent
    ```
    
- Function pointer as parameters
    
    we can define parameter that is pointer to function, for example:
    
    ```cpp
    void use_bigger(const string &s1, const string &s2,
    bool pf(const string &, const string &));
    
    //is equivalent to
    
    void use_bigger(const string &s1, const string &s2,
    bool (*pf)(const string &, const string &));
    ```
    
    in the first case, pf is a function type and is automatically treated as pointer 
    
    To call the function `use_bigger(s1,s2,length_compare);`      convert to a pointer
    
- Returning a pointer type (skipped, refer p450)

**Inline function**

inline function is a function that is expanded "inline at each call"

For example:  `cout << (s1.size() < s2.size() ? s1:s2 ) << endl;` can be replaced by an inline function `cout << shorterstring(s1,s2) << endl;`

with the function defined by **putting the inline keyword before the return type**

`inline const string &shorterstring (const string &s1, const string &s2) {..}`

**Separate compilation**

a separate compile will be:

```bash
cc -c main.cpp                  # produce an object file
cc -c funct.cpp                 # produce an object file
cc main.o funct.o -o main       # linking, create executable main
```
