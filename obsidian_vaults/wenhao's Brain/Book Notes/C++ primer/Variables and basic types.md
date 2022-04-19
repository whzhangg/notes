# Variables and Basic Types

### Internal data types
##### Internal data types
cpp define the following internal data types:
- bool
- char, wchar_t, char16_t, char32_t
- short, int, long, long long
- float, double, double double

Integer can be signed or unsigned, unsigned will never be less than 0, so that 
```cpp
if (unsigned u=10, u>0, --u) { . }
``` 
will always give true

##### internal type conversion
We have the following type conversion to bool types:
- assign nonbool types to a bool give true unless the value=0
- assign bool to arithmetic type gives 1 or 0

### Literals
##### string literals
A single quotation of a single character is a *char*: `'a'`. Zero or more character in double quotation is a *string*.

Compiler appends a null character `'\0'` to every string literal, so the *actual size of a string literal is one more than its apparent size.*

Two string literal that appear adjacent to one another and separated only by spaces, tabs or newlines are automatically concatenated together:
```cpp
std::cout << " a long ..."
             " literal" << std::endl
```

##### boolean literals
Words `true` and `false` are literals for bool.

##### pointer literals
`nullptr` is a pointer literal

### Initialization, declaration and definition
##### Initialization
There are 4 ways to initialize variables:
```cpp
int u = 0 ;
int u = {0}; <= list initialization
int u{0}; 
int u(0);
```

##### initialization and assignment is different
`int i = j;` is an initialization and is different from `int i; i = j;`:
- Initialization: happens when variable are given values when it is created
- assignment: obliterates an object's current value and replace with new values

##### variable declaration vs. definition
A variable definition is a declaration and also allocate storage and initialize, i.e., creates the entity of the variable. On the contrary, a declaration simply *make a name known to the program*.

Keyword "extern" without initializer is used to declare a variable without defining it.
```cpp
extern int i;     // declares i
int i;            // defines i
extern int i = 5; // definition
```

##### Identifiers
*Identifier* is the name of the variable, In c++, names are:
1. case sensitive, 
2. must begin with letter or underscore

### scope
##### Definition of scope
A scope is a part of the program in which a name has particular meaning. The same name can refer to different entities in different scope. Names are visible from declaration until the end of the scope

Most scopes are delimited by `{}`, Typically, we can have three different scopes:
1. Global scope, names defined outside a function
2. Block scope, defined inside a function
3. Scope of a statement, For example, in this for statement, *i* is defined in the scope of the for statement. `for (int i=1; i<10; i++)` 

Typically, it is good practice to define variables where you use them.

##### Nested scope
Scopes can contain scope, if a name is declared in a scope, it can be used by inner scope 

if a name is redefined in an inner scope, it will become local. In this case, to access the name in the global scope, we need to use the scope operator  `scope::val`. The global scope has no name, so `::val` fatch the variable in the global scope

### Compound types
##### Object reference separation
A compound type is a type that defined in terms of another type.

It is important to understand the meaning of *compound*: pointer/reference and the object they refer to are separate. When we define a pointer `const int *ptr`, we define pointer to point to a const int object.

As a result, when we use the `*ptr`, it is equivalent that we are using an `const int`. *But it does not matter if it is really pointing to a const int. it can point to a normal int but it does not matter*.

We have two compound types available: *reference* and *pointers*

##### Reference
A reference is simply a alternative name (alias) for the object. Since it is merely an alias of the original variable, we can use reference in the same way as using the original variable. 

It is declared by writing declarator with `&`:  
```cpp
int ival = 1024; 
int &ref_val = i;   // reference definition: type &name association
ref_val = 20;       // ival also become 20
```

A reference has no address, Therefore:
1. when defining a reference, we bind reference to its initializer, once initialized, a reference remain bound to its initial object.  
2. It can not rebind to another object. 
3. Reference must to initialized, bound to an object, cannot bound to literal or expression
4. we cannot define reference to a reference

##### Pointer
Unlike reference, pointer is an object of its own, it has an address and can point to several different objects over its lifetime.

Pointer is declared by the form: `*d` and it holds the address of an object, which is accessed by the *address of* operator `&`. The object that the pointer is pointed at is accessed by the *dereference* operator `*`.
```cpp
int ival = 42;
int *p = &ival;
p = &another_val
*p = 25;
cout << *p
```
    
A point can be in one of the four states:
1. point to an object
2. point to an location that was an object
3. null pointer, not bound to any object
4. invalid pointer

To initialize a null pointer, we can initialize it by `nullptr` or literal `0`
```cpp
int *p1 = nullptr;
int *p2 = 0;
```
    
A pointer can be of void type, it can hold the address of any object, but the type is unknown

##### pointer in condition
`if (p)` gives true if p is not zero (nullptr). `p1 == p2` compars the address they point to

##### declaration of compound types
Two declaration:
```cpp
int *p1, p2;
int* p1, p2;
```
are equivalent, the `*` operator only applies to the next declarator, but the type in both expression are of int.

##### pointer to pointer
Point level is indicated by `*` , `**` for a pointer to a pointer, and so on
```cpp
int ival = 1024;
int *pi = &ival;
int **ppi = π;
cout << **ppi;  // dereference twice
```
Dereferencing a pointer gives another pointer, to access ival, we must dereference twice.

##### reference to a pointer
`int * &r = pi` defines a reference to a pointer. The reference is to be used as alias of the original pointer. For example `cout << *r;` dereferences r, equivalent to dereference pi

### CONST
##### const qualifier
if we want to prevent code from giving new values to a variable, we can make a variable unchangable, such variable must be initialized eg, `const int buffersize = 512;`

##### extern const
By default, const type is local to a file, if we want to use const variable in another file, we need to use the `extern` keyword. For example:
```cpp
# file_1.cpp:
extern const int buffersize = get_buffersize();
# file_2.h:
extern const int buffersize; // use buffersize
```

##### Reference to const
Reference itself is not an object, it can not be const since it is always const.  

A reference can be made to refer to a const by:
```cpp
const int ci = 1024;
const int &r1 = ci; // ok, a reference to a const int
int &r2 = ci;       // error, reference to a int but ci is const.
```
*Note* that the *object defines the operation*, so a reference to an int defines what we can do with the reference. 

But a reference to a const need to be restricted, we cannot use r2 to change ci, which is the logic for the error

##### reference of a const to non const variable
A reference that refer to a constant value restricts what we can do with the reference, not what we can do to the original variable. The type of the reference defines what we can do with the reference. 
```cpp
int i = 25;
const int &r1 = i ;
r1 = 24; -> error
i = 25; -> ok
```

##### pointer to a const
The situation is similar to reference to const
```cpp
const double pi = 3.14;
const double *cptr = π // ok, a pointer point to a const double
double *ptr = π // error, pointer is not const
```

##### const pointer to a non const object
```cpp
double dval = 3.14;
cptr = &dval; // ok, cptr now point to a non const object
```
Here, `cptr` is a constent object so we cannot change the value of dval with the pointer, but we can through the original variable

##### Const pointer
we can define a *const pointer*, which must be initialized and the address (high level const) it holds can not be changed. 

It can be defined as follows:
```cpp
int err_numb = 0;
int *const cur_err = &err_numb; // defines a const ptr (*const) to an int
```

we can not change the pointer itself.  What we can do with the pointer is determined by the type which the pointer points

##### top-level and low-level const
we can talk independently whether a pointer is const or whether the object it points to is const:
- When a pointer itself is const, it is a *top-level const*,
- When the object a pointer points to is const, it is a *low-level const*.

When copying, the top-level const are ignored. This can be understood since copying transfer the data, not the object itself (and therefore its property). In the case of low-level const of pointer, copying transfer the address of the object, which can be a constant object and therefore, low-level const is transfered.
```cpp
const int ci = 42;
int i = ci; // top level const ci is ignored, i is not a const
```

##### const expression
A constant expression is an expression whose value is evaluated at compile time. For example:
- a literal is a constant expression
- a const object initialized from a constant expression is also constant expression

We can declare a variable is a const expression by: `constexpr int mf = 20;`

### More on type
##### type aliases 
A type alias defines an aliase for type names
```cpp
typedef double wages; // define wages as an alias for double
typedef double * p;   // define p as an alias for pointer to double
```

Another way of defining type alias is use "using" statement: `using wages = double;`

##### const and aliase
if we define a pointer
```cpp
typedef char *pstring;
const pstring cstr; // => we define a const pointer to a char
const char *cstr;   // => we define a pointer to a constant char
const pstring *ps;  // => we define a pointer to a constant pointer to a char
// const apply to the base type here, which is a pointer
```

##### auto
auto specifier tells the compiler to deduce the type from the initializer variable that use auto must have an initializer.
```cpp
auto item = v1 + v2;
```

##### decltype
Using auto, we evalue the expression for the type and initial value. If we *only want to know the type*, not the initial value from the expression, we can use `decltype`:
```cpp
decltype(f()) sum = x;
decltype(a+b) sum = x;
// compiler will check the type of function f() to determine the type of x
```

### Data structure
##### data structure
A data structure group together data elements and method, i.e. defines a type. c++ define data structure by defining a class

##### Defining a data structure
To define a structure:
1. begin with keyword struct
2. follow by the name of the class and a body `{ }`, which form a scope. 
3. The closing `}` must follow by a `;`

```cpp
struct sales_item{ 
		std::string booknumber; 
		unsigned int unit_sold = 0; 
};
// it is also possible to follow variable definition immediately after structure definition
struct sales_item{ .. } booka, bookb;
```

##### Including class from header files
Classes are usually defined in header files that has the same name. *header files* usually contain classes or constexpr variables that can only be defined once.

##### preprocessor and header guards
Suppose:
- If we define a class vector in file vector.h
- In point.h, we `#included "vector.h"` and defines another class point
- In main, we `#include "vector.h"` and `#include "point.h"`

Then, we would have included vector class twice. to prevent that, *preprocessor variables* can be used.

Preprocessor is a program that run before the compiler and substitute texts. `#include` is a preprocessor facility, *which replaces the line `#include` with content from the header file*.

Preprocessor can hold variables, which is in one of the two states: *defined* or *not defined*:    
```cpp
#define 
   	// take a name and defines the name as preprocessor variables
#ifdef VAR ... #endif 
    // this part of code will only be executed if VAR is defined
#ifndef VAR .. #endif 
    // opposite
```

Using preprocessor varialbes, we can prevent including same code twice:
```cpp
#ifndef DATA
#define DATA
...
#endif
```
*Note* that preprocessor variables do not have scope, we need to ensure uniqueness by ourselves.