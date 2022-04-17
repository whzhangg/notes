# C++

Created: September 28, 2021 9:08 PM
Description: notes for c++ primer
Tags: Programming, c++

## Chapter 1. Getting Started

**main function**
a c++ program must contain one or more functions, operating system runs c++ by calling main()

`int main() { return 1; }`

**standard I/O** 

c++ does not define any statements to do I/O, but includes a standard library for that "iostream"

- istream for input streams
- ostream for output streams

**include**

any program that use a library must include its header, for example

`#include <iostream>` 

iostream is the library name 

`#include` must written on a single line and name must appear at the same line

for a custom defined class, we include a header file.h, we enclose them with " ", if library are not standard (otherwise < >) 

`#include <iostream>` 

`#include "sales_item.h"` 

**using names from standard library** 

prefix `std::` indicates that names are defined inside "namespace" named "std", all names defined by standard library are in the std namespace 

`::` is the scope operator 

**Commenting in c++**

single line comment: `// comments`

multiple line: `/* comments */`

a commenting style for multiple line is:

```cpp
# / *
# * comment 1
# * comment 2
# * /
```

**statement block**

a block is a sequence of statements enclosed by `{ }`, it is a statement and can be used wherever a statement is required

**while**

```cpp
while (condition) {
		statements;
}
```

**for**

```cpp
for (int i = 1; i < 10; ++i) {
		sum += i;
}
```

each for statement has two parts: a header and a body. Header controls how the body is executed, consists of three parts:`(init-statement; condition; expression)`

the program initialize → check_condition → execute body → increment value

**if**

```cpp
if ( condition ) { 
		statements; 
} else { 
		otherwise; 
}
```

**using class**

every class defines a type

to create a variable, we can use: `sales_item item`, which define item to be of sales_item

member function is a function defined as part of a class

dot operator is used to access a member function

**std::endl**

endl end current line and flush buffer to write to the I/O stream

## Chapter 2. Variables and Basic Types

**Internal data types**

a list of interal types

- bool
- char, wchar_t, char16_t, char32_t
- short, int, long, long long
- float, double, double double

integer can be signed or unsigned, unsigned will never be less than 0, so (unsigned u=10, u>0, --u) will always give true

**type conversion**

- assign nonbool types to a bool give true unless the value=0
- assign bool to arithmetic type gives 1 or 0

**string literals** 

'a' => single quotation of a single character -> char

" " => zero or more character in double quotation -> string

compiler appends a null character '\0' to every string literal, so the actual size of a string literal is one more than its apparent size.

two string literal that appear adjacent to one another and separated only by spaces, tabs or newlines are automatically concatenated together:

```cpp
std::cout << " a long ..."
             " literal" << std::endl
```

**boolean literals**

words true and false are literals for bool

**pointer literals** 

nullptr is a pointer literal

**4 ways to initialize variables:**

```cpp
int u = 0 ;
int u = {0}; <= list initialization
int u{0}; 
int u(0);
```

**initialization and assignment is different**

initialization → happens when variable are given values when it is created

assignment → obliterates an object's current value and replace with new values

`int i = j; <- initialization` is different from `int i; i = j;`

**variable declaration vs. definition**

declaration => make a name known to the program ()

definition => creates the entity

a variable definition is a declaration and also allocate storage and initialize keyword "extern" without initializer is used to declare without define

```cpp
extern int i;     // declares i
int i;            // defines i
extern int i = 5; // definition
```

**identifiers**

identifier is the name of the variable, in c++, names are case sensitive, must begin with letter or underscore

**scope**

a scope is a part of the program in which a name has particular meaning

the same name can refer to different entities in different scope

names are visible from declaration until the end of the scope

most scopes are delimited by `{ }`

global scope -> names defined outside a function

block scope -> defined inside a function

scope of a statement, `for (int i=1; i<10; i++)` <- i is defined in the for statement scope -> it is a good idea to define variables where you first use them.

**nested scope**
scopes can contain scope, if a name is declared in a scope, it can be used by inner scope 

if a name is redefined in an inner scope, it will become local => in this case, to access the name in the global scope, use the scope operator  `scope::val`. The global scope has no name, so `::val` fatch the variable in the global scope

**COMPOUND TYPE**

it is important to understand the meaning of "compound" pointer/reference and the object they refer to are separate
when we define a pointer `const int *ptr`, we define pointer to point to a const int object.

therefore, when we use the `*ptr`, it is equivalent that we are using an `const int` but it does not matter if it is really pointing to a const int. it can point to a normal int but it does not matter.

compound type: a compound type is a type that defined in terms of another type

two compound types:  **references** and **pointers**

**reference:** alternative name

```cpp
int ival = 1024; 
int &ref_val = i;   // reference definition: type &name association
ref_val = 20;       // ival also become 20
```

1. reference defines an alternative name for an object ( alias ), they do not have address
2. a reference type is declared by writing declarator with &  `int &ref_val`
3. when defining a reference, we bind reference to its initializer, once initialized, a reference remain bound to its initial object (can not rebind to another)
4. a reference must to initialized, bound to an object, cannot bound to literal or expression
5. we cannot define reference to a reference
6. to use a reference, just in the same way as using a variable, but we are really using the object it reference to, since reference is merely a alias

**Pointer**

1. pointer is an object of its own, it has an address and can point to several different objects over its lifetime, unlike reference
2. pointer is declared by the form: `*d`
3. a pointer holds the address of an object, which is accessed by the "address of" operator `&`
    
    ```cpp
    int ival = 42;
    int *p = &ival;
    p = &another_val
    *p = 25;
    cout << *p
    ```
    
4. pointer value is one of the four states:
    
    point to an object
    
    point to an location that was an object
    
    null pointer, not bound to any object
    
    invalid pointer
    
5. the object that is pointed at is accessed by "dereference operator": `*`
6. to initialize a null pointer, we can initialize it by `nullptr` or literal `0`
    
    ```cpp
    int *p1 = nullptr;
    int *p1 = 0;
    //NULL can also be used but NULL is not defined by the language, but a preprocessor variable
    ```
    
7. a pointer can be of void type, it can hold the address of any object, but the type is unknown

**pointer in condition**

`if (p)` gives true if p is not zero (nullptr)

`p1 == p2` compars the address they point to

**declaration of compound types**

`int *p1, p2;`

`int* p1, p2;`

are equivalent, the `*` operator only applies to the next declarator, but the type in both expression are of int

**pointer to pointer**
point level is indicated by `*` , `**` for a pointer to a pointer, and so on

```cpp
int ival = 1024;
int *pi = &ival;
int **ppi = π;
cout << **ppi;  // dereference twice
```

dereferencing a pointer gives another pointer, to access ival, we must dereference twice

**reference to a pointer**
`int * &r = pi` defines a reference to a pointer
`cout << *r;` dereference r, equivalent to dereference pi

**CONST**

**const qualifier**

if we want to prevent code from giving new values to a variable, we can make a variable unchangable, such variable must be initialized eg, `const int buffersize = 512;`

**extern const**
by default, const type is local to a file, if we want to use const variable in another file, we need to use the "extern"
file_1.cpp:
`extern const int buffersize = get_buffersize();`
file_2.h:
`extern const int buffersize; // use buffersize`

reference to const

reference is not an object, it can not be const, it is always const a reference can be made to a const by:

```cpp
const int ci = 1024;
const int &r1 = ci; // ok, a reference to a const int
int &r2 = ci;       // error, reference to a int but ci is const.
```

note that the object defines the operation, so a reference to an int defines what we can do with the reference. but a reference to a const need to be restricted, we cannot use r2 to change ci, which is the logic for the error

**reference of a const to non const variable**

a reference that refer to a constant value restricts what we can do with the reference, not what we can do to the original variable.
(type defines what we can do with it. reference of a type defines what we can do with the reference)

```cpp
int i = 25;
const int &r1 = i ;
r1 = 24; -> error
i = 25; -> ok
```

**pointer to a const**
similar to reference to const

```cpp
const double pi = 3.14;
const double *cptr = π // ok, a pointer point to a const double
double *ptr = π // error, pointer is not const
```

**const pointer to a non const object**

```cpp
double dval = 3.14;
cptr = &dval; // ok, cptr now point to a non const object
```

-> cptr is a pointer point to const object, defined above

-> now we point it to another object that is not const. (pointer itself is non const)

-> we can not change value through the pointer, but can through the original variable

const pointer

we can define a const pointer, which must be initialized and the address (high level const) it holds can not be changed. 

it can be defined as follows:

```cpp
int err_numb = 0;
int *const cur_err = &err_numb; // defines a const ptr (*const) to an int
```

we can not change the pointer it self and what we can do with the pointer is determined by the type which the pointer points

**top-level and low-level const**

we can talk independently whether a pointer is const or whether the object it points to is const.

- top-level const <= pointer itself is const.
- low-level const <= the object it point to is const.

when copying, the top-level const are ignored

```cpp
const int ci = 42;
int i = ci; // top level const ci is ignored, i is not a const
```

**const expression**

a constant expression is an expression whose value is evaluated at compile time.

a literal is a constant expression

a const object initialized from a constant expression is also constant expression

we can declare a variable is a const expression by: `constexpr int mf = 20;`

**MORE on TYPE**

type aliases 

a type alias defines an aliase for type names

```cpp
typedef double wages; // define wages as an alias for double
typedef double * p;   // define p as an alias for pointer to double
```

another way is use "using": `using wages = double;`

**const and aliase**

if we define a pointer:

```cpp
type char *pstring;
const pstring cstr; // => we define a const pointer to a char
const char *cstr;   // => we define a pointer to a constant char
const pstring *ps;  // => we define a pointer to a constant pointer to a char
// const apply to the base type here, which is a pointer
```

**auto**

auto specifier tells the compiler to deduce the type from the initializer variable that use auto must have an initializer

`auto item = v1 + v2;`

**decltype**

using auto, we evalue the expression for the type and initial value. if we just want to the type, but not the initial value from the expression, we can use decltype:

```cpp
decltype(f()) sum = x;
decltype(a+b) sum = x;
// compiler will check the type of function f() to determine the type of x
```

**DATA STRUCTURE**

data structure

a data structure group together data elements and method, i.e. defines a type. c++ define data structure by defining a class

**defining a data structure**

begin with keyword struct

follow by the name of the class and a body `{ }`, which form a scope. The closing `}` must follow by a `;`

```cpp
struct sales_item{ 
		std::string booknumber; 
		unsigned int unit_sold = 0; 
};
// it is also possible to follow variable definition immediately after structure definition
struct sales_item{ .. } booka, bookb;
```

**including class from header files**

classes are usually defined in header files that has the same name

header files usually contain classes or constexpr variables that can only be defined once.

**preprocessor and header guards**

if we define a class vector in file vector.h

in point.h, we #included "vector.h" and defines another class point

in main, we #include "vector.h" and #include "point.h"

then, we would have included vector class twice. to prevent that, **preprocessor variables** can be used

- preprocessor is a program that run before the compiler and substitute texts. `#include` is a preprocessor facility, **which replaces the line #include with content from the header file**
- preprocessor can hold variables, which is in one of the two states: **defined** or **not defined**
    
    ```cpp
    #define 
    	  // take a name and defines the name as preprocessor variables
    #ifdef VAR ... #endif 
        // this part of code will only be executed if VAR is defined
    #ifndef VAR .. #endif 
        // opposite
    ```
    
- so the following way prevent including same code twice:
    
    ```cpp
    #ifndef DATA
    #define DATA
    ...
    #endif
    ```
    
- note that preprocessor variables do not have scope, we need to ensure uniqueness

## Chapter 3. Strings, Vectors and Arrays

**Using declaration**

`using` is declaration let us to use a name from a namespace without specifically refering to the namespace, for example: `using std::cin;`

- a separate `using` is needed for each name
- we should not use `using` declaration in header files. since header file will be copied into the c program and may introduce unexpected name conflicts. ( unless we use some form of pre-compile check)

**String**

- Initializing string
- Operations on strings:

```cpp
a.empty()   // return if a is empty
a.size()    // return the size of string
s[n]        // return a reference to the char at position n
s1 + s2     // concatenation

```

note that string literals (instead of variable) does not support the same operation as strings. For example, string literals can not be added together

**Indexing, or subscript**
`s[n]` if the index `n` has a signed type, its value will be converted to unsigned.

- Range of the subscript is unchecked, therefore it's better to defined as unsigned int

**Ranged for**

Ranged for statement iterates through the elements in a given sequence and perform operation on each value.

```cpp
for (declaration : expression)
    statement

// example, printing all characters in a string
for (auto c : str1 )
    cout << c << endl;
```

- Expression is a object that represents a sequence,
- Declaration defines the variable we use to access the elements

**Using reference to change the character in a string**

To change the characters in a string, we need to use a reference. For example:

- `for (auto c : str) c = toupper(c)` str is unchanged
- `for (auto &c : str) c = toupper(c)` str is changed to upper case

In the first case, we are copying each str to a character c, so that when we change c, we do not change the value of the string. But in the second case, c refer to the object itself, and when we are changing c, we really changed the object

**Vector**

vector usually refered to as a container because it contains other objects, it is a **class template**, instantized by suppling type in the `< >`

```cpp
vector<int> ivect;
vector<scales_item> sales_vect;
```

- vector is initialized to empty by default

vectors support operations:

```cpp
vector<int> v2;
v2.push_back(10); // append element onto the back of the vect
v.empty()         // return if v is empty
v.size()          // return the size
v[n]              // subscription
```

Range for is also available to iterative through vector, and similarly, we need to use reference to change elements

**Templates**

templated can be for class and function. They are not themselves functions or class, but they are instructuions to the compiler for generating classes or functions <= instantiation

**Iterators**

iterator is **a type that a class defines to iterate through its objects as pointer**, it does not hold the object, so **we need to dereference iterator to access the object it points to**.

A type (for example, vector) that support iterators have member method called `begin()` and `end()` that return the iterator, and we can use iterator operations to iterate through iterators.

```cpp
for ( auto it = s.begin(); it != s.end(); ++it ){
    *it = toupper(*it); 
	  // dereference it to access the element
}

s.begin()   // return a iterator object as the first element in the list
s.end()     // return a iterator type positioned **one past the end** of the list, not the last item
++it; --it  // increment (decrement) the iterator
*it         // return a reference to the element
```

If we do not want to change the element that we iterate through, we can use constant iterator `.cbegin()`

```cpp
auto it = s.cbegin(); <- refer to a const type
it != s.cend()
```

**Access the member of an iterator (pointer)**
if we want to access the method of the object iterator point to, we need to dereference it and than access using `.`, For example `(*it).empty()`, this is equivalent to: `it->empty()`

**Iterator arithmetic**

iterator for string and vector support additional operation:

- `iter +(-) n` return an iterator that move forward and backward n step
- `iter += n` assign iter to iter + n
- `iter1 - iter2` yield a number as the number of step between two iterator
- comparsion (> < = )

```cpp
// binary search
auto beg = text.begin(); end = text.end();
auto mid = text.begin() + (end-beg)/2;
while (mid != end && *mid != sought) {
    if (sought < *mid)
        end = mid;
    else
        beg = mid + 1;
    mid = beg + (end-beg)/2
} // keep in mind that mid, end, beg are all iterators

```

**Build in arrays**

array is a container of unnamed objects of a single type that we access by position `int a[4] = {0,1,2,3}`

- array is a compound type
- array has fixed size (or const expression) that must be specified at declaration
- we cannot use auto to sepcify an array

**note**: character array has an additional null character at the end, so its length is larger by the visual size by 1, for example: `char a[6] = 'Daniel';`  `Deniel\\0` is a 7 character array

**Arrays can not be copied** we cannot initialize an array as a copy of another array, it is also not legal to assign one array to another

```cpp
int a2[] = a; // error
a2 = a;       // error
```

A**rray of pointers or pointer of array**

```cpp
int *ptrs[10];            // defines a array of 10 pointers to int
int (*parray)[10] = &arr; // defines a pointer to an array of 10 int
int (&rarray)[10] = arr;  // reference
```

Type modifier bind from right to left, so in the first case, it is understood as *(ptrs[10])

**Pointer and arrays**

When we use an array, the compiler substitute a pointer to the first array elements

```cpp
int arr[] = {0,1,2,3,4};  // initializing an array
int *p = arr;             // arry is substituted by &arr[0]
int *p = &arr[3];         // obtain a pointer to an array element by taking the address
```

Pointer to array elements support the same operations as iterators on vectors

```cpp
int arr[] = {0,1,2,3,4};
int *p = arr;
p += 3;    // understood as pointer to array element arr[3]
```

we can obtain the pointer to the begin and end of a array by: `begin()` and `end()`

```cpp
int *beg = begin(arr);  // first
int *end = end(arr);    // one past last
while (beg != end) { ++beg; }
```

Adding an int to a pointer of an array gives another pointer to the same array

```cpp
int *p2 = p + 2;                // returns an array
auto n = end(arr) - begin(arr); // return an int
int i = *(p + 2);               // dereference the pointer
```

Subscripting an array `int i = arr[2];` equivalent to `int i = *(&arr[0] + 2);`

We can also subscript a pointer, treating it as an array:

```cpp
int *p = &ia[3];
int k1 = p[1];  // ia[4]
ink k2 = p[-2]; // ia[1], equivalent to *(&ia[3]-2)
```

**Multidimension arrays**
a multidimension array is understood as "array of arrays". For example `int ia[3][4];` is an array of size 3, each element is array of size 4

Initializing multidimensional array:

```cpp
int ia[3][4] = {
		{0,1,2,3},{4,5,6,7},{8,9,10,11}
}
```

Subscripting
if we provide less subscripts than dimensions, we get a array elements: `int (&row)[4] = ia[1];` is reference to a 4 dimension array point to the second element

Range for for loop over array elements

```cpp
for (auto &row : ia )
    for (auto &col : row) {
        ... (col is int & type)
    }
}
```

**Pointer with multidimension arrays**
if we use the name of multidimension array, it will converted to a pointer

```cpp
int ia[3][4];
int (*p)[4] = ia; // ia is used as &ia[0], p is an pointer to a array[4]

// in this case, it is easier to use auto:
auto p = ia;      
```

## Chapter 4. Expressions

**lvalue and rvalue expression**

- lvalues are the one that could appear on the left hand side of an expression
- rvalues are those that could not

in general, when we use an object as rvalue, we use its value (content); when we use object as an lvalue, we use its identities (location in memory)

- we can use an lvalue when an rvalue is required, but we can not do otherwise

**Operators**

There is unary operators ( &, * and so on), binary operator ( ==, *, so on)

- some symbol can both be used as a unary or binary operator, it is helpful to think they are two different symbols ( * )

**Order of evaluation**

In most case, the order of evaluation is unspecified: `int i = f1() * f2()`. we are guaranteed that the result of `f1` is multiplied to `f2`, but we do not know whether `f1` is called first of `f2` is called first. If the two function affect the same object, the expression will have undefined behavior.

Also, consider:

```cpp
int i = 0; 
cout << i << "" << ++i << endl; // the value of the output is undefined
```

The evaluation that **do have clear order** is: 

logical AND `&&`: we are guaranteed that it evaluates its right-hand operand only if left-hand side is true

logical or `||`

conditional operator `?:`

comma operator `,`

**Logical operators**

AND : `&&` ; NOT : `!`; OR : `||`

**Assignment and increment**

assignment is right associative

```cpp
int ival, jval; 
ival = jval = 0; // evaluated from left most assignment

while ( ival = get_value() != 42) {..} // assignment get_value() != 42 will be evaluated first
```

Two types of increment:

- prefix : `j = ++i;` increments its operand and yield the changed object as its result
- postfix : `j = i++;`  increments the operand but yield copy of the origin

Combining dereference and increment

```cpp
auto pbeg = v.begin();
while (pbeg != v.end() && *beg >= 0)
		cout << *pbeg++ << endl;
// ++ has a higher precedence, so *pbeg++ is valued as *(pbeg++)
// which increment the iterator and yield the copy of the previous value, so
// it prints the original value of pbeg and increments pbeg
```

-Increment can occur in any order:

`*beg = toupper(*beg++);` will give undefined, beg appear in the same expression as beg++

**Member access operator**

- `.` give access for member of class type,
- `ptr->member` is equivalent to `(*ptr).member`
- member access has high precedence than `*` , so `*p.size()` will take `p.size()` first

**Conditional operator**

`cond ? expr1 : expr2;`

the operator evaluate condition, if cond are true, `expr1` is evaluated and returned, otherwise `expr2`

```cpp
string finalgrade = (grade < 60) ? "fail" : "pass"
// compound conditional operator
finalgrade = (grade > 90) ? "good" : (grade < 60) ? "fail" : "pass"
```

- Conditional operator is right associative, so in the above expression, right hand side conditional operator is evaluated first
- Conditional operator has a low precedence, so we sometime need to use ( ):  `cout << (grade < 60) ? "fail" : "pass" ;`

**Sizeof operator**

- it return a constant expression of the type in *bytes*
- takes two form:
    
    ```cpp
    sizeof(type);
    sizeof expr; // size of the expression
    ```
    
- sizeof operator does not evaluate its operand

**Comma operator** 

it takes two operands and evaluate from left to right, guarantees the order of the evaluation. The left-hand size expression is evaluated and its result is discarded. the result of comma expression is the value of its right-hand expression

```cpp
for (vector<int>::size_type ix = 0; ix!=ivec.size(); ++ix, --cnt)
		ivec[ix] = cnt
```

the loop increments ix and decrements cnt, both `++ix` and `--cnt` are evaluated, but no result is returned here

**Implicit type conversion**

c++ do some implicit conversion

1. array to pointer : `int *ip = ia;`  (ia is an array of int)
2. const conversion :

we can convert a pointer(reference) to a nonconst type to a pointer to a const type but we can not do the reverse

**Cast (explicit conversion)**

named cast `cast-name<type> (expression)`

where, type is the target type, expression is the value to be cast

cast-name is one of the follow:

1. static_cast
    
    any well defined type conversion, except involving low-level const, can be requested using static_cast
    
    ```cpp
    int j,i; 
    double slope = static_cast<double>(j)/i 
    // convert j from int to double in the expression
    ```
    
2. const_cast
    
    changes only a low level const in its operand, (low level here means the object that a pointer or reference points to)
    
    ```cpp
    const char *pc;*
    *char * p = const_cast<char*>(pc);
    // we convert a const to a nonconst type by const_cast
    ```
    
3. reinterpret_cast
    
    a low level reinterpretation of its operands
    
    ```cpp
    eg :: int *ip;*
    *char * pc = reinterpret_cast<char*>(ip);
    // reinterpret ip as a pointer of character and assign its value to pc
    ```
    

## Chapter 5. Statements

**Simple statements** 

most statement in c++ end with semicolon

1. expression statements an expression followed by `;`. expression statement cause expression to be evaluated and its result discarded
2. null statement an empty statement given by `;` useful when c++ require a statement but we don't need
    
    for example `while (cin>>s && s!=sought) ;`  where the ; at the end is a null statement.
    
3. compound statement `{ .. }` is used when language requires a single statement but we need more than one. For example, the body of a for loop must be a single statement, so we need to use `{ .. }`  to  include more statements. An empty block is equivalent to a null statement
    
    a block is a scope, names introduced in a block is accessible only in that block and in blocks nested inside
    

**Statement scope**

vairables defined inside the control structure of  if, switch, while and for are visible only within that statement and are out of scope  after the statement end.

```cpp
while (int i = 0; i<10; i++) cout << i << endl; 
i = 0; // error, i not defined
```

### Control sequence

**If statements**

```cpp
if (condition) // condition must be enclosed by ( ) 
    statement; 
else 
    statement2; 

// nested if
if (condition)  
    statement;  
else if (condition2)  
    statement;  
else 
    statement;
```

`else` is matched to the closest preceding unmatched `if` in the nested if above, the last else correspond to if (condition2) 

```cpp

```

if (i > 3) if (i > 3) { if (i > 7) if (i > 7) grade = '+'; -> grade = '+'; else } else <- use { } to control else matching grade = '-'; grade = '-';

**Switch**

switch check all the case labels, even after a match is found, we explicitly interrupt it by a `break` statement

```cpp
switch(ch) {
		case 'a':           // case label, must be constant expressions
			statements;
			break;            // break is included to jump out of switch

		case 'b'"
			statements;
			break;

		default:
			statement;
			break;
}
```

**While statement**

`while (condition) statement;`

variables defined in a while condition or body are created and destroyed on each iteration

**For statement**

```cpp
for (initializer; condition; expression)   // referred to as "for header"
		statement;
```

Execution flow in a for loop:

1. init statement is executed once at the start of the loop
2. condition is evaluated, if true, the body is executed, otherwise, the loop terminates
3. if body is executed, the expression is evaluated

We can omit parts of the header:

- omitting init-statement by a null statement if we want to use an variable outside
- omitting condition is equivalent to writing true as condition
- expression can be omitted if there is no need for it.

**Range for**

```cpp
for (declaration : expression)
		statement
```

- expression must be a sequence, such as an array or vector;
- declaration defined a variable

```cpp
vector<int> v = { ... };
for (auto &r : v)           // a pointer is defined
		r *= 2;                 // double each element in the vector
```

**Do while statement**

```cpp
do
		statement (or block)
while (condition);
```

- variables used in the condition must be defined outside
- the statement is executed before condition is evaluated

**Break statement**

break terminates the nearest enclosing while, do while, for or switch

**Continue statement**

continue terminates current iteration of the nearest loop and begin the next iteration

**goto statement**

`goto label;` labeled statment is any statement preceded by an identifer followed by `:`

```cpp
goto end;
...
end: return;
```

### Exception handling

**Throw expression**

`throw runtime_error("Data must be real number");`

we throw **an object of type runtime_error, which is initialized by "Data .."**

**Try block**

```cpp
try {
		statement
} catch (exception-declaration) {
		handler-statements
} catch (exception-declaration) {
		handler-statements
}
```

once a catch finished, execution continues with statement following the last catch

For example

```cpp
try { .. } 
catch (runtime_error err) { 
		cout << err.what() << endl; 
}
// note that we declared an except called err
```

**Standard exceptions**

exception are defined in the standard library. in <stdexcept>, the following is defined:

```cpp
exception           // most general exception
runtime_error       // problems detected at runtime
range_error         // runtime error
overflow_error      // runtime error
underflow_error     // runtime error
logic_error
domain_error
invalid_argument
length_error
out_of_range
```

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

## Chapter 7. Classes

**Data abstraction and encapsulation**

data abstraction is the separation of interface and implementation

- Interface is the operations uses can execute
- Implementation is the part that is hidden from user

encapsulation force class to hide its implementation

**Defining a class**

- member functions must be declared inside the class
- member functions maybe defined outside the class body
    
    ```cpp
    struct sales_data {
    
    		std::string isbn() const {return bookNo;}     // declared and defined here
    		sales_data& combine(const sales_data&);       // declared here, defined outside
    		double avg_price() const;
    		std::string bookNo;
    		double revenue = 0.0;
    		unsigned units_sold = 0;
    
    }
    ```
    
- the compiler process class first with declarations, then process the function body
- a function that defined outside the class must include the name of the class of which it is a member, using the **scope operator**
    
    ```cpp
    double sales_data::avg_price() const {
    		if (units_sold) return revenue/units_sold;
    		else  return 0;
    }
    ```
    
- once compiler see the function name, the rest of the code is seen as being inside the scope of the class, so revenue and units_sold is implicitly referring to the members of sales_data

**this**

- member function access the object on on which they were called through an **implicit parameter** named `this`
    
    when we call `total.isbn();` the compiler interpret as `sales_data::isbn(&total);` which pass the address of `total` object
    
- **`this` is a const pointer**
- Inside a member function, we can directly refer to the member of the object on which the function is called. i.e. It's unnecessary to use this→units_sold

**const member functions**

- `this` ****is an implicit parameter, if we want to indicate ****`this` ****to be a pointer to a const, i.e., we will not change the object itself through the member function, we put a **const after the parameter list**
    
    ```cpp
    std::string isbn() const {retrun bookNo;}
    // is interpreted as
    std::string sales_data::isbn(const sales_data *const this) {..}
    ```
    

**Function that return `this`**

we can usually return a reference of the object, as follows

```cpp
sales_data& sales_data::combine(const sales_data &rhs){
		..
		return *this;   //dereference and return the content of the object
}
// we return a reference by sales_data&
```

**nonmember functions**

functions that are conceptually a part of a class but not defined inside the class, should be declared in the same header as the class itself

CONSTRUCTOR

**constructors**

- constructors have the same name as the class, and does not have return type.
- a class can have multiple constructors
- constructors can not be declared as const. since, when we create an object, the object does not have its "constness" until after the constructor completes the initialization

As an example, we can create 4 constructor for sales_data:

```cpp
struct sales_data{
		sales_data() = default;                                     // default initializer
		sales_data(const std::string &s): bookNo(s) { }             // defined initializer
		sales_data(const std::string &s, unsigned n, double p):     // with initializer list
								bookNo(s),units_sold(n),revenue(p*n) { }
		sales_data(std::istream &);                                 <- declare initializer
		
		std::string bookNo;
		unsigned units_sold = 0;                                    // default member initialize
		double revenue = 0;
}
```

**default initialization**

- if (and only if)we do not explicitly define any constructor, compiler will implicitly define default constructor called "synthesized default constructor", which default initialize the members.
- if we are defining other constructors but still want to keep the default, we can use `= default` after the parameter list to geneater the default constructor
    
    `sales_data() = default;` which generate a default constructor that take no parameter
    

**use constructor initializer list**

```cpp
sales_data(const std::string &s): bookNo(s) { }
sales_data(const std::string &s, unsigned n, double p):
					bookNo(s),units_sold(n),revenue(p*n) { }
```

- a list of member names after the colon and the {}
- each is followed by member's initial value
- multiple initialization are separated by `,`
- if a member is omitted from the list, it is implicitly default initialized
- if no further work to be done, the function body is empty

**Defining a constructor outside the class body**

`sales_data::sales_data(std::istream &is) { read(is, *this); }`

- a constructor have no return type, therefore start with name, which is in the scope of the class
- we do not have a initializer list (empty list), even though the initializer list is empty, **the members of this object are still initialized before the constructor body is executed**
- members that do not appear in initialized list are initialized by the corresponding default initializer and are defult initialized. so when the function body start to execute, the member already have default values

**Copy, assignment and destruction**

- class also control what happens when we copy, assign or destroy objects of the class.
- if we do not define these operations, the compiler will synthesize them for us, which will copy, assign or destroy each member of the object.

**Access control**

In c++, we use access specifiers to enforce encapsulation:

- members defined after a **public** specifier are accessible to all parts of the program
- members defined after a **private** specifier are accessible to the member functions of the class, but not to code uses the class
- a class may contain mulitple specifier, and there is no restriction on how often a specifier may appear, each specifier control the access level of the succeeding members. So, public and private can appear multiple times

```cpp
class sales_data {
public:
		sales_data() = default;

private:
		std::string bookNo;
}
```

**Struct and Class**

the only difference between struct and class is the default access level:

- struct : members defined before the first access control are public
- class  : members defined before the first access control are private

we use struct when we are intending for all its members to be public

**friend**

- a class can allow other class or function to access its nonpublic member by making them a **friend** , by including a declaration for that function preceded by the keyword friend
- friend declaration can only appear (anywhere) inside a class definition
- a friend declaration only specifies access, it is not a declaration of the function. If we want to use the function, we must also declaration it separately from the friend declaration.
    
    ```cpp
    class sales_data {
    friend sales_data add(const sales_data&, const sales_data&);  // declaration of friend
    public:
    		sales_data() = default;
    private:
    		std::string bookNo;
    }
    
    sales_data add(const sales_data&, const sales_data&);         // declaration of function
    ```
    

**additional class features**

- redefining type names in class
    
    ```cpp
    public:
    	typedef std::string::size_type pos;     // define pos as a name for a type
    	using pos = std::string::size_type;     // equivalent as above
    
    private:
    	pos cursor = 0;                         // using pos a a type
    ```
    
- mutable data member
    
    if we include mutable keyword in the member declaration, such a member will never be const, even if it is a member of a const object
    
    ```cpp
    private:
    		mutable size_t access_ctr;    // mutable
    		void some_function() const {  // const member function
    				++ access_ctr;            // still can change access_ctr
    		}
    ```
    
- class declaration
    
    we can declare a class without defining it, called "forward declaration". For example: `class screen;`. after declaration and before a definition, the class is an incomplete type. A type must be defined before we can write code that create objects of that type
    
- making a member function as friend
    
    we can make a class a friend
    
    ```cpp
    class screen {
    		friend class window_mgr;
    }
    ```
    
    we can also make only a member function a friend
    
    ```cpp
    class screen {
    		friend void window_mgr::clear(index);
    }
    ```
    
- function overload and friendship
    
    overload are different functions that share a same name. if we want to declare a overload function, we must declare each function in a set of overloaded functions
    

**Class scope**

- to access data and member function, we can only do through an object (reference or pointer)
- to access type members, we need to use the scope operator
    
    ```cpp
    screen::pos ht = 24;    // use type pos defined in screen
    screen scr(ht, wd, '');
    screen *p = &scr;
    c = p->get();           // access through a pointer
    ```
    
- function defined outside the class use scope operator: `void window_mrg::clear(screen_index i) {..}`. the following part, i.e., the paramter list and function body auotmatically be in the scope  of the class
- return type of member function
    
    the return type is before the function name, thus not in the scope of the class we need to add scope to the return type: `window_mgr::screen_index window_mgr::addscreen(const screen &s);`
    

**how compiler look up the name**

For a normal name, compiler look for:

1. declaration of the name in current block before usage
2. look in the outer scopes
3. error if nothing is found

for members in the class definition, compiler comiler all the declaration first, then the function bodies

name used in the **declaration**:  for member declaration or function declaration(outside function body), compiler look for names: 1) defined already; 2) names defined outside the class scope

The compiler look for names in member function body

1. declarations inside the member function
2. name declared inside the class
3. if not found in the class, look for name in the outer scope before the function definition

name in member function outside class definition

the outside scope include the code after class but before definition of member function

MORE CONSTRUCTOR

**using constructor initializer**

compare

```cpp
sales_data::sales_data(const string &s, unsigned cnt, double price) {
		bookNo = s; units_sold = cnt; revenue = cnt*price;
}   
// initializer is ommited initialize the members to default and do assignment
```

and

```cpp
sales_data(const std::string &s, unsigned n, double p):
								bookNo(s),units_sold(n),revenue(p*n) { }
// do the initialization
```

- sometimes, we have to initialize some members by initializer list. For example, `const` or `reference` must be initialized or members of a class type that must initialize with parameters

**sequence of initialization**

initializer list specifices the values, but not sequence, members are initialized in the order of which they appear in class definition

**Delegating constructors**

a delegating constructor use another constructor from its own class to perform initialization

```cpp
class sales_data {
	public:
		sales_data(const std::string &s, unsigned n, double p):
		bookNo(s),units_sold(n),revenue(p*n) { }                   // non delegating constructor
		sales_data(): sales_data("",0,0) {}                        // delegating constructors
		sales_data(std::string s): sales_data(s,0,0) { addition work; }
}
```

- a delegating function will do all the work of a constructor
- after delegating constructor complete their work, the body of the constructor will executed

**Using a default constructor**

`sales_data obj();` defines a function, instead of declaring a object. `sales_data obj;` declare an object

**Class-type conversion**

each constructor that is called with a single argument defines an implicit conversion For example, for sales_data, we can initialize it with string, so it defines an implicit conversion between string and sales_data:

```cpp
string book="0-123-123";
item.combine(book);         // combine require a sales_data type, which is converted from string
```

only one type conversion is allowed:

```cpp
item.combine("0-123-123");      // error, "0-123-123" is literal, but combine accept string
item.combine(string("0-123-123"));
```

we can prevent the implicit conversion by using **explicit** keyword in constructor declaration. For example: `explicit sales_data(const std::string &s): bookNo(s) {}` which disable the above type conversion. explicit can only used inside a class definition, not in member function definition outside class

**static class members**

- we can define some members (data, function) that is **associated with the class, not with the individual objects**
- this is specified by keyword "static"
- can be public or private
- the static member exist outside any object, so bank_account will only contain two data members: owner and amount
- a static member function also not bound to any object, so they **do not have this pointer**
- we can assess static member by scope operator, or by any object
    
    ```cpp
    double r; bank_account ac1;
    r = bank_account::rate();   // access using scope
    r = ac1.rate();             // direct access using object
    ```
    
- member function can use static members directly
    
    ```cpp
    class bank_account {
    public:
    		void calculate() { amount += amount * interest_rate; }
    		static double rate() {return interest_rate;}
    		static void rate(double);
    private:
    		std::string owner;
    		double amount;
    		static double interest_rate;  // static member
    }
    ```
    

**Defining static member**

- we can declare a static member function inside the class, but we do not need to repeat static keyword when we define the function outside the class
- static members are not initialized by constructor
- we maynot initialize static member inside the class, we should define and initialize static member outside class body

## Chapter 8. The IO Library

**IO classes**

- library defines the IO type (3 header, defines the IO classes):
    
    iostream (istream, ostream) : basic io type
    
    fstream  (ifstream, ofstream) : read and write from named files
    
    sstream  (istringstream, ostringstream) : read and write from a string
    
- Types defined in fstream and sstrean inherit from basic iostream, so the members of iostream are also fstream and sstream
- we cannot copy or assign objects of the IO type, we can pass it with non const reference
- In case of wide character, we add 'w' for the corresponding objects: `ifstream` -> `wifstream`  for wide char

**iostat**

read or write operation change the IO states of the IO type, **the easiest way to check a string is OK to use is to use:** 

```cpp
while (cin >> word)
		...                 // if the operation succeeded
```

**system dependent IOstat**

IO class defines function and class to access IO state:

- iostate is a class type, is used as collection of bits
    
    `iostream::iostate` a machine dependent integral type
    
- 4 constexpr values of type iostate, they represent bit patterns, they are used to test or set flags
    
    `iostream::badbit`        incidate if a stream is corrupted (machine specific value)
    
    `iostream::failbit`      IO operation failed
    
    `iostream::eofbit`        stream hit end of file
    
    `iostream::goodbit`      stream is not in an error state (guaranteed to be zero)
    
- member functions
    
    `s.good()`  return true if stream is valid
    
    `s.fail()`  true if failbit or badbit is set
    
    `s.bad()`  true if badbit is set
    
    `s.eof()`  true if eof is set
    
    `s.clear()`  reset all condition so the stream will be in a valid state
    
    `s.clear(flags)`  reset the given flag, flag is a iostate type
    
    `s.setstate(flags)`  add condition to the string
    
    `s.rdstate()`  return the current condition as a s.iostate value
    

```cpp
auto old_state = cin.rdstate();     // get the previous state
cin.clear();                        // we clear state informations
process_input(cin);
cin.setstate(old_state);            // add back the IO state attached
```

**flush the buffer**

system manage a stream buffer to hold data that is read or write there are several conditions that cause buffer to flush:

1. program complete (not when program crashes)
2. full buffer
3. flush the buffer explicitly
4. change the behavior of stream by "unitbuf"

flushing the buffer

```cpp
cout << "hi" << endl;   // write hi and newline, flush buffer
cout << "hi" << flush;  // write hi, and flush, nothing is added
cout << "hi" << ends;   // write hi and add a null, flush buffer
```

unitbuf

we can use unitbuf to tell stream to do a flush after every write by cout << unitbuf;

```cpp
cout << unitbuf;    // 
cout << "ssss";     // flush immediately
cout << nounitbuf;  // return to normal buffering
```

**tie IO stream**

if istream is tied to an ostream, then any attempt to read will flush the output first, this is usefull in interactive IO. To tie stream: `cin.tie(&cout)`

**File IO**

in addition to inherited method, fstream defines more operation:

`ifstream input;`                  creates the file stream object (also for ofstream)

`ifstream input(s);`            create object and opens a file named s

`ifstream input(s,mode);`   open in a given mode

`input.open(s);`

`input.open(s, mode);`        open a file in a given mode

`input.close();`                   close the file

`input.is_open();`                return bool indicating if the file is open

For example:

```cpp
ifstream in(file);
ofstream out;
out.open(file+".copy");
if (out)                    // check if out is succeeded, out is converted to bool
in.close();
in.open(file2);             // associate it with another file
```

file IO in scope

```cpp
for (auto p = argv+1; p!= argv+argc; ++p) {
		ifstream input(*p);
		if (input) process(input);
		else cerr << "cannot open "+string(*p);
}   // input is in the block, and is destroyed at each iteration
// when fstream object go out of scope, the file it associated is closed automatically
```

**mode**

- `in`
- `out` : by default, discard the contents of the file
- `app` : open to the output mode and append to last (seek the end first)
- `trunc` : truncate the file (discard the content of the file) out mode also truncate file by default
- `ate` : seek the end immediately after open
- `binary` : binary mode

For example:

```cpp
ofstream out("f1", ofstream::out)
out.open("fo",ofstream::app)
```

**string streams**

inherit from the basic iostream with additional members:

`sstream strm;` : create an unbound stringstream object

`sstream strm(s);` : object hold a string s

`strm.str();` : return a copy of the string

`strm.str(s);` : copy string s into strm

istringstream is useful when we need to process strings line by line, For example:

```cpp
string line, word;
vector<personInfo> people;

while (getline(cin,line)) {
		personInfo info;
		istringstream record(line);
		record >> info.name;
		while (record >> word)
				info.phones.push_back(word);
		people.push_back(info);
}
```

ostring is useful to format without write

```cpp
for (const auto &entry : people) {
		ostringstream formatted, badNums;
		for (const auto &nums : entry.phones) {
				if (!valid(nums))
						badNums << " " << nums;
				else
						formatted << " " << format(nums);
		}
		
		if (badNums.str().empty())
				os << entry.name << " " << formatted.str() << endl;
		else
				cerr << "input error:" << entry.name << "invalid: " << badNums.str() << endl;
}
```

## Chapter 9. Sequential Containers

**sequential containers**

- the standard library provide several sequential containers
- in general, each container is **defined in a header file with the same name as the type**
- they all provide sequential access to the elements, but offer different performance of 1) cost to add or remove elements, 2) cost to perform nonsequential access

**Different sequential containers**

- vector : flexible size, fast access. elements are hold in contiguous memory, adding elements sometime require movement of the whole object
- string : similar to vector
- list, forward_list : fast add or remove anywhere in the container, do not support random access
- deque : fast random access; fast insert/delete at front or back, but not at middle
- array (this array type is different from the build in array)

**Some operations are provided by all containers**

```cpp
types:
		iterator
		const_iterator
		size_type
		difference_type
		value_type
		reference
		const_reference
constructure:
		Container c;
		Container c1(c2);           <- copy construction
		Container c(begin,end);     <- constructe by iterators
Assignment and swap
		c1 = c2;
		a.swap(b);                  <- swap elements
		swap(a,b);
Size
		c.size()
		c.max_size()
		c.empty()                   <- true if container is empty
Adding elements
		( when we insert an object t, the object is copied, we do not insert the object itself )
		c.push_back(t)              <- create an element with value t (object) at the end
		c.emplace_back(args)        <- initialize a new element at the end of c
		c.push_front(t)
		c.emplace_front(args)
		c.insert(p,t)               <- create an element with value t before the iterator p,
																	 return an iterator of the element that is added
		c.emplace(p,args)           <- initialize new element by args before iterator p
		c.insert(p,il)              <- il is a { } list of element values, insert before iterator p
		c.insert(p,begin,end)       <- insert the elements given by a iterator range, before p
Accessing elements
		c.back()                    <- return a ***reference*** to the last elements in c
		c.front()                   <- return a reference to the first elements
		c[n]                        <- return a reference to element indexed by n
		c.at(n)                     <- return a reference to element indexed by n, check range
Erasing elements
		c.pop_back()                <- return void, remove the last element
		c.pop_front()
		c.erase(p)                  <- remove the element denoted by an iterator, or a range
		c.erase(begin, end)            return the location after the last element that is removed
		c.clear()
Resize
		c.resize(n)                 <- resize c to have n elements, discard excess elements
Manage capacity (vector and string)
		capacity -> how many elements we can hold in the current memory space
		c.shrink_to_fit()           <- reduce capacity to equal to current size
		c.capacity()                <- return number of elements c can have before reallocation is necessary
		c.reserve()                 <- allocate space for at least n elements
Obtain iterators
		c.begin(), c.end()          <- return iterators to the end and one pass end
		c.cbegin(), c.cend()        <- return const_iterator
```

**iterator ranges**

- an iterator range is denoted by a pair of iterators refer to elements in the same container
- iterator range is left-inclusive : `[ begin, end )`

**Reverse iterators**

most container provide reverse iterators that go backward through a container `++` on a reverse iterator yields previous element

**Container initialization**

- except array, most default constructor creates an empty container
- we can create a container by copy initialize or passing an iterator range
    
    ```cpp
    list<string> authors = {"A","B","C"};                       <- list initialization
    list<string> list2(authors);                                <- copy initialization
    forward_list<string> words(authors.begin(),authors.end());  <- range initialization
    ```
    
- array must be fixed size, array elements will be default initialized

**Relational operators on containers**

comparing two containers as follows, similar to string comparsion

- if both container are the same size and all elements are equal, they are equal
- container are of different size but all element of the smaller one is equal to the corresponding element of the larger container, then smaller one is smaller
- if the smaller container is not the initial subsequence of the other, then comparsion depends on comparing the first unequal elements

**Container adoptor**

an adaptor is a mechanism for making one thing act like another, a contain adaptor take an existing container and make it act like a different type

library define three adaptor: stack, queue and priority_queue

## Chapter 10. Generic Algorithms

**Generic algorithms**

- library provide a set of algorithms, independent of any particular container type
- most are defined in the algorithm header
- iterator make the algorithm container-independent
- algorithm need operators of the container elements, eg :: < or == operators

**Read-only algorithm**

`find(begin, end, val)` : return an iterator to the first element that == val, return end if no match

`accumulate(begin, end, init)` : ( **numeric **header) sum the elements in the given iterator range using +, with the provided initial value. summing a string concatenates each element, since + is concatenate for string

`equal(begin1,end1,begin2)` : assume second sequence is at least as big as the first. looks all element given in the first sequence, use == to compare element with the second sequence

**back inserter**

- insert iterator is an iterator that adds elements to a container
- insert is an iterator adaptor
- when we assign to the element of a insert iterator, a new element equal to the right hand side is added to the container
- defined in the **iterator **header

```cpp
vector<int> vec;
auto it = back_insert(vec);
*it = 42;                       // insert an new element 42
```

**Write algorithm**

**algorithm do not perform container operation, they cannot change the container**

`fill(begin, end, 0)` : fill in each element in the given range with given value

`copy(begin, end, a2)` : copy the element of the input range to another sequence denoted as a2

`replace(begin, end, v1, v2)` : replace each element equal to the first value with second value in the given range

`replace_copy(begin, end, p, v1, v2)` : (copy version) p is the destination in which we write the adjusted sequence, origin sequence is unchanged

**Algorithm that reorder container elements**

`sort(begin, end)` : sort the elements in the range given

`unique(begin, end)` : reorder the sequence so that the unique elements appear in the first part of the vector/ return one past the last unique elements

For example:

```cpp
we input a list with elements:
	 fox | fox | jump | the | jump | tree | fox

-> fox | jump | the | tree | xxx | xxx | xxx      (unique elements are in the first half)
```

**Customizing operations**

we can customize operation with which we perform the algorithm

For example: `stable_sort(word.begin(), word.end(), is_shorter);` is_shorter is a function that compare two elements

**lambda expression**

lambda expression is a callable object which we can pass to functions

the structure of a lambda expression is : `[capture list](parameter list) -> return type {function body}`

- "->" is needed for the return type
- capture list is a list of local variables defined in the enclosing function
- parameter list, return type and function body are as ordinary functions
- lambda function is defined like an expression

For example:

```cpp
auto f = [] {return 42;};   // r.h.s. is an expression
cout << f() << endl;        // call by () operator
// eg2
auto f = [](const string &a, const string &b) {return a.size() < b.size();};
// eg3
auto f = [sz](const string &a) {return a.size() >= sz;};
capture list specifize which variables will be used within the lambda, here it captures sz
```

**lambda capture**

`[]` : empty capture list, lambda do not use any variable from the enclosing body

`[names]` : capture by value (copied)

`[&names]` : capture by reference

`[&]` : implicit by reference (compiler infer which variables we use in the lambda body)

`[=]` : implicit by value

`[&,names]` : default by reference, with the one specified by names is value captured

`[=,names]` : reverse

```cpp
void fcn1(){
		size_t v1 = 42;
		auto f=[v1] {return v1;}        // lambda is initialized here, it capture v1 here
		v1 = 0;                         // v1 is copied to lambda and that copy store with f
		auto j = f();
}
// f gets destroyed when going out of scope, since it is value capture
```

**bind function**

library provide a bind function, which is defined in the functional header

`auto newCallable = bind(callable, arg_list)`

arg_list may include names of the form `_n`, which is called a **place holders**

- `_n` is defined in a namespace *"*placeholders", in the std namespace
- we must make the names known to our program, using, for example, using namespace std::placeholders

For example, assume `f` is a callable that has 5 parameter, we can bind f to g:

`auto g = bind(f, a, b, _2, c, _1);`

which generate a new callable g that take 2 arguments, represented by place holder `_2` and `_1`. arguments to g are bound positionally to place holders: `g(X,Y)` will map g to `f(a, b, Y, c, X)`

- we can use bind to reorder parameter: `bind(isShorter, _2, _1)` exchange the paremter to isShorter

## Chapter 11. Associative Containers

**associative containers**

- elements in an associative container are stored and retrieved by a key, instead by positions
- they support efficient lookup and retrival by a key
- 8 associative containers, as a combination of:
    
    set or key
    
    unique keys or multiple keys (a key can appear multiple times)
    
    order or unorder
    
- a set only have keys

**associative container defined in library**

```cpp
map             multimap            // map header
set             multiset            // set header
unordered_map   unordered_multimap  // unordered_map header
unordered_set   unordered_multiset  // unordered_set header
```

**define map or set**

`map<string, size_t> word_count;` : define two types as a pair

`set<string> exclude = {"the","and"};` : define type

`map<string, string> authors = { {"joyce","james"}, {"Austen","Jane"} };` : list initialize

- a key value pair is given inside curly braces { }

**Requirement on key type:**

key type of ordered type must be able to compare using operator <

**pair type**

type "pair" is defined in the utility header, which hold two public data member

```cpp
pair<string, size_t> word_count;                // a pair
pair<string, string> author{"James", "Joyce"};  // pair with initialization
author.first    // "James"
author.second   // "second"
```

make_pair(v1,v2) return a pair initialized from v1 and v2, type is inferred from v1 and v2

**operations on associative containers**

iterators

- iterator of a map point to a pair: auto map_it = word_count.begin(); cout << map_it->first
- iterator of a set are const. we cannot change the key in a set

adding elements

- insert only when the element with the given key is not already in c
    
    ```cpp
    c.insert(v)             // insert an elements
    c.emplace(args)         // insert by initialization
    c.insert(b,e)           // insert by iterators
    c.insert(il)            // insert by list
    c.insert(p,v)
    c.emplace(p,argus)
    
    // For example   
    word_count.insert({word,1});        // insert a pair
    word_count.insert(make_pair(word,1));
    ```
    
- the return of insert is a pair, the first member is an iterator to that element inserted, or where is already is. The second member is a bool indicating whether the element was inserted
- adding elements to a multiset or multimap keys in multi-container is not unique, insert always insert an element so they act like a vector of pairs

Removing elements

`c.erase(k)` : remove every element with key k from c, return the number of elements removed

`c.erase(p)` : remove the element denoted by the iterator

`c.erase(begin,end)` : remove element in the range

Accessing elements

- map contain subscript operator and a "at" function:
    
    `c[key]` access the element with key k, or `c.at(key)`
    
- **if the key is not already present, a new element is created and inserted for that key**
    
    `word_count["Anna"] = 1` : create a default initialized element with key "Anna" and assign 1 to its value
    
- The following method do not add elements automatically
    
    ```cpp
    c.find(key)             // return an iterator to the first element with key, or off-the-end if not found
    c.count(key)            // number of elements with key k
    c.lower_bound(key)      // iterator to first element with key not less than k
    c.upper_bound(key)      // iterator to first element with key greater than k
    c.equal_range(key)
    ```
    
    when a multiset has multiple elements of a given key, those elements will be adjacent, we can use find and count to get all elements
    

**Unordered containers**

unordered containers use has function and == operator of the keys to find elements which is useful when we can not give order to the keys

## Chapter 12. Dynamic Memory

**program use dynamic memory for one of the three purposes**

1. they don't know how many objects they will need (we do not allocate if we do not need it)
2. don't know the type of objects they will need
3. share data between several objects

**dynamic objects**

c++ let us allocate objects dynamically, which exist **until freed explicitly**

- **static memory**: local static objects, variables defined outside any function
- **stack memory**: nonstatic objects defined inside functions (in a block) stack memory are automatically created and destoryed by compiler
- **heap** (free store): dynamically allocated objects

**manging memory directly**

language defines two operator that allocates memory

`new` : allocate memory;  `delete` : frees memory

- **new** : ****objects allocated on the free store are unnamed, new allocattes the memory and returns a pointer to the object it allocates
    
    ```cpp
    int *pi = new int;
    int *pi = new int();        // new with some initial value, it is good idea to initialize
    auto p1 = new auto(obj);    // use auto to infer object type directly
    ```
    
- **delete :** we return the memory through delete expression (**pointer itself is not destroyed**). `delete` destorys the object to which its given pointer points and frees the corresponding memory
    
    delete do not check if the pointer points to a dynamically allocated memory, it is our responsibility to make sure it's correct. For example: `delete p1;`
    

**memory management**

dynamically allocated objects exist until they are freed

```cpp
void use(T arg){
		foo *p = new T(arg);
		... use p
}   // p goes out of scope and is deleted but the allocated memory is not freed

// we need to delete p inside the block
```

when we free memory by deleting a pointer, for example, `delete p;` the pointer itself is not deleted, but it become undefined until it goes out of scope

```cpp
auto q = p;
delete p;
q = nullptr;    // q point to the same place as p, so we should prevent it being used
```

**Allocating dynamic arrays**

we can ask new to allocate an array of objects by specifying a number

```cpp
int *pi_a = new int[size];
int *pi_a = new int[size]( initializer );
```

`new` do not return a object of an array type, we get a **pointer to the element type** of the array as a consequence, we cannot use array member such as iterator or ranged for

it is possible to allocate an empty array, in which case the pointer act as a off-the-end pointer

**Freeing dynamic arrays**

to free a dynamic array, we use delete that include an empty pair of square brackets

```cpp
delete p;
delete[] p_a;
// [] indicates to the compiler that pointer addresses the first element of an array objects
```

**smart pointer**

- a smart pointer act like a regular pointer but it automatically deletes the object to which it points
- smart pointer cannot convert with ordinary pointers

```cpp
shared_ptr      // we can make multiple different pointer to point to the same object
unique_ptr      // opposite to shared_ptr
weak_ptr        // weakly related to an object managed by shared_ptr
```

**shared_ptr class**

created like templates:

```cpp
shared_ptr<int> p1;
shared_ptr<list<int>> p2;
// default initialization create a smart pointer holds a null pointer
```

- we can use smart pointer in the way similar to using a pointer
- `make_shared()` is defined in the memory header. It allocates and initializes an object in dynamic memory and return a shared_ptr. we must specify the type of object we want to create
    
    make_shared use argument to construct an object of the given type, like `emplace()`
    
    ```cpp
    shared_ptr<int> p3 = make_shared<int>(42);
    auto p4 = make_shared<vector<string>>();        // default initialized dynamic memory
    // p3 points to an int with value 42
    ```
    
- shared_ptr keep track of how much other shared_ptr point to the same object (reference count)
    
    copy or assign shared_ptr → the count is incremented (more shared_ptr pointing to the object)
    
    assign new value to shared_ptr or when it is destroyed (eg. go out of scope) → the count is decremented (less shared_ptr pointing to the object)
    
    when reference_counter goes to zero, the ptr automatically frees the object
    
    ```cpp
    void process(shared_ptr<int> ptr) {
    		use ptr;
    }
    shared_ptr<int> p(new int(42));
    process(p);
    ```
    
    In this example, smart pointer p is passed to process by value (copy), ptr is a copy of p and the reference counter of ptr increase by 1. after function execution, ptr go out of scope and is destroyed, reference counter automatically decrement by 1
    

**operation common to shared_ptr and unique_ptr**

```cpp
shared_ptr<T> sp    <- create shared_ptr
unique_ptr<T> up
p                   <- using a smart pointer name as a condition, true if it points to an object
*p                  <- dereference
p.get()             <- return a normal pointer
swap(p,q)           <- swap two pointers
make_shared<T>(args)<- create a shared object initialized with args
shared_ptr<T> p(q)  <- create a copy of shared_ptr
p = q               <- assignment, decrement p's reference count (for other shared pointers
associated with p) and increment q's count
p.unique()          <- if p is the only pointer pointing to its object
p.use_count()       <- return reference count
```

**shared_ptr with new**

- we can initialize a smart pointer from a pointer returned by new
    
    ```cpp
    shared_ptr<double> p1;
    shared_ptr<int> p2(new int(43));    // initialize the smart pointer with new
    shared_ptr<int> p2 = new int(43);   // but this result in error because we cannot directly convert
    ```
    
    by default, we need to supply a pointer to the dynamic memory to initialize shared_ptr because shared_ptr will free the object afterward. if we supple a pointer to other resourse we must supply our own deletion code.
    
- mixing shared_ptr with pointer may cause the memory to be deleted:
    
    ```cpp
    int *x = new int(42);
    process(shared_ptr<int>(x));    // we make a shared pointer and pass it to a function
    int j = *x;                     // x become undefined because shared_ptr deleted the memory
    ```
    

smart pointer define a function named .get() which return a normal pointer to the object: `int *p = smart_p.get()`

**dynamic object with exception**

- if an exception happens between new and delete and is not caught by the code, this memory will never be freed and there is no pointer to this memory
- smart pointer will still able to automatically deleter the memory in the case of exception

**other smart pointer**

**unique_ptr** : a unique_ptr owns the object to which it points, only one unique_ptr can pointer to a given object

**weak_ptr** : does not control the lifetime of the object to which it points. weak_ptr can points to an object that is managed by shared_ptr, which does not change the reference count of that shared_ptr

## Chapter 13. Copy control

**copy control**

- a class can define five special member functions (apart from constructors)
    1. copy constructor 
    2. copy-assignment operator    -> assign
    3. move constructor            -> move
    4. move-assignment operator
    5. destructor                  -> destroy

if they are not defined, the compiler automatically generate missing operations

**copy constructor**

- synthesized copy constructor (default): memberwise copies the member of its argument into the object being created
- copy constructor is a constructor whoes first parameter is a reference to the class type and any other parameters should have default values

```cpp
class sales_data {
		public:
				sales_data(const sales_data &);
		private:
				std::string bookNo;
				int units_sold;
				double revenue = 0.0;
}

sales_data::sales_data(const sales_data &orig):
bookNo(orig.bookNo), units_sold(orig.units_sold), revenue(orig.revenue) { }

// this copy constructor use initializer list to initialize object, with a reference to orig
// this is also the default initializer
```

**copy initialization**

- when we use direct constructor, the compiler select the constructor of the best match
- when we use copy constructor, the copy the right-hand side into the object

For example: `string nines = string(100,'9');` In this example, string nine is copy constructed from a string that is constructed directly

**copy construction is different from assignment**

`int i = j;` copy initialization is different from `int i;  i = j;`

- copy initialization happens when
    1. define variables by copying using =
    2. pass an object as an argument to a parameter of nonreference type
    3. return an object from a function that has a non-reference return type
    4. brace initialize the elements in an array

**copy assignment**

copy assignment controls how classes are assigned

```cpp
sales_data trans, accum;
trans = accum;              // use copy assignment
```

- copy assignment overload `=` operator, the lefthand operand is bound implicit to this parameter, the rhs is passed as an explicit parameter
- To be consistent with assignment for the build in types, copy assignment operator usually return a reference to their left hand side (although left hand side is modifed by the function body using this )

```cpp
sales_data& sales_data::operator=(const sales_data &rhs) {
		bookNo = rhs.bookNo;
		units_sold = rhs.units_sold;
		revenue = rhs.revenue;
		return *this;
}
// **copy assignment should consider the case when an object is assigned to itself**
```

**Destructor**

- member function with the name of the class prefixed by a tilde `~`
- can not be overloaded
- has no return value and take no argument
- destructor body does not directly destoryed the members themselves, destruction happens after the destructor body: `~sales_data(){}`
- destructor are called when:
    1. variables go out of scope 
    2. members of an object are destroyed when the object that contain them are destroyed
    3. element in a container are destroyed when the contain is destroyed
    4. dynamically allocated object destoryed by delete
    5. temporary objects destroyed at the end of the expression

destructor is **not** run when a reference or a pointer to an object goes out of scope

**Generating default copy controls**

we can explicitly generate default function using `=default` option

```cpp
class sales_data{
public:
		sales_data() = default;
		sales_data(const sales_data&) = default;
		...
}
```

**Preventing copy**

`= delete` option signals to the compiler that we are intentionally not defining the members, But **destructor should not be deleted**

**Designing copy control**

copy determines whether a class has **value-like** or **pointer-like** behavior

- class behave like value: each have their own state, copy should be independent from the origin
- class behave like pointers: class share states, copy access the same underlying data as origin

**Class that act like values**

the following class act like value

```cpp
class HasPtr {
public:
		HasPtr(const std::string &s = std::string()): ps(new std::string(s)), i(0) { }
		HasPtr(const HasPtr &p): ps(new std::string(*p.ps)), i(p.i) { }
		HasPtr& operator=(const HasPtr &);
		~HasPtr() { delete ps; }
private:
		std::string *ps;
		int i;
}

HasPtr& HasPtr::operator=(const HasPtr &rhs) {
		auto newp = new string(*rhs.ps);    // we initialize a new string from rhs
		delete ps;
		ps = newp;
		i = rhs.i;
		return *this;
}
```

**Class act like a pointer**

```cpp
class HasPtr {
		public:
				HasPtr(const std::string &s = std::string()):
				ps(new std::string(s)), i(0), use(new std::size_t(1)) {}
				HasPtr(const HasPtr &p): ps(p.ps), i(p.i), use(p.use) { ++*use; }
				HasPtr& operator=(const HasPtr&);
				~HasPtr();
		private:
				std::string *ps;
				int i;
				std::size_t *use; // our own reference counter, shared between copied objects
}

HasPtr::~HasPtr() {
		if (--*use == 0) {
				delete ps; delete use;
		}
}

HasPtr& HasPtr::operator=(const HasPtr &rhs) {
		++*rhs.use;
		if (--*use == 0) {      // use is the counter of the left hand side, decrement
				delete ps;          // if no one use the original resource, it is freed
				delete use;
		}
		
		ps = rhs.ps;            // assign pointers
		i = rhs.i;
		use = rhs.use;
		return *this;
}
```

**swap**

class that manage resource usually define a function named swap

```cpp
class HasPtr {
		friend void swap(HasPtr&, HasPtr&);
}

inline
void swap(HasPtr &lhs, HasPtr &rhs) {
		std::swap(lhs.ps, rhs.ps);  // swap the pointers, not the string data
		std::swap(lhs.i, rhs.i);    // swap the int members
}
```

the library provide swap for the build in type, but for our class, we should use its own swap, not `std::swap`

## Chapter 14. Overloaded Operations and Conversions

**overload operator function**

- an overloaded function has the same number of parameters as operator has operands
- unary operator has one parameter
- binary operator has two (left hand side is passed to the first parameter)
- may not have default arguments
- if overload function is a member function, the lefthand side is bound implicit to "this"
- we cannot change the meaning of an operator when applied to build-in type
- overload operator has the same precedure and associativity as the corresponding build-in operator

**calling a overload operator**

direct call: `data1 + data2`

explicit call: `operator+(data1, data2)`

**member or non-member implementation**

we should consider if we make an operator a member function or not

- assignment `=`, subscript `[]`, call `()`, and `->` must be defined as members
- compound assignment should be members
- operators that change the state of the object, such as increment, should be members
- symmetric operator that require conversion should be defined non-member ( typeA + typeB should behavior the same as typeB + typeA, but the member function definition will implicit relate l.h.s. to the current type)

**overload `>>`**

normally, the first parameter of an output operator is a reference to a nonconst ostream object. since we ostream cannot be copied

```cpp
ostream & operator<< (ostream &os, const sales_data &item){
		os << item.isbn()<< " " << item.units_sold << " "
			 << item.revenue << " " << item.avg_price() ;
		return os;
}
```

IO operator must be nonmember function. since for a member function, l.h.s. would have to be an object of class type

**overload `<<`**

the first parameter is a reference to the stream to read from, the second parameter is a reference to the nonconst object into which to read

we usually return a reference to its given stream

```cpp
istream & operator>> (istream &is, sales_data &item) {
		double price;
		is >> item.bookNo >> item.units_sold >> price;
		if (is)
				item.revenus = item.units_sold * price;
		else
				item = sales_data();
		return is;
}
```

**overload arithmetic and relational operators**

- usually defined as non-member functions to allow conversion
- parameters should be reference to const.

**overload `+`**

```cpp
sales_data operator+ (const sales_data &lhs, const sales_data &rhs) {
		sales_data sum = lhs;
		sum += rhs;
		return sum;
}
```

**overload `==`**

```cpp
bool operator== (const sales_data &lhs, const sales_data &rhs) {
		return lhs.isbn() == rhs.isbn() &&
		lhs.units_sold == rhs.units_sold &&
		lhs.revenue == rhs.revenue ;
}

bool operator!= (const sales_sata &lhd, const sales_data &rhs) {
		return !(lhs == rhs);
}
```

**assignment operator**

- should be member function
- a class can define additional assignment operators that assign object of other type to this object
- assignment should return a reference to its left-hand operand

```cpp
strvec &strvec::operator= (initializer_list<string> il) {
		auto data = alloc_n_copy(il.begin(), il.end());
		free();
		elements = data.frist;
		first_free = cap = data.second;
		return *this;
} // this is implicitly the l.h.s. object
```

**compound assignment**

```cpp
sales_data& sales_data::operator+=(const sales_data &rhs) {
		units_sold += rhs.units_sold;
		revenue += rhs.revenue;
		return *this;
}
```

**subscript []**

- return a reference to the element that is fatched
- usually define both const and nonconst version of this operator

```cpp
class StrVec {
public:
		std::string& operator[](std::size_t n) {
				return elements[n];
		}
		const std::string& operator[](std::size_t n) const {
				return elements[n];
		}
}
```

**increment and decrement**

- they are defined as member function

**prefix operator**

- should return a reference to the incremented object

```cpp
StrBlobPtr& StrBlobPtr::operator++() {
		check(curr, "increment past end of StrBlobPtr");
		++curr;
		return *this;
}
```

**postfix operator**

- postfix operator accept an extra unused parameter of type int
- return a reference to the object before incrementing

```cpp
StrBlobPtr StrBlobPtr::operator++(int) {
		StrBlobPtr ret = *this;
		++*this;        // call the prefix version
		return ret;
}
```

calling the prefix or postfix operator explicitly

prefix: `p.operator++();` 

postfix: `p.operator++(0);`

**function call operator `()`**

overloading function call operator allow the object to be used as they were functions

```cpp
struct absInt {
		int operator() (int val) const {
				return val < 0 ? -val : val;
		}
}
```

which defines a function object, but such class can also store states, so they can be flexible. we can use as:

```cpp
int i = -42;
absInt absObj;
int ui = absObj(i);     // similar as calling a function
```

- lambdas are function objects

**library function type**

library provide a function type that represent a callable (is a template class)

```cpp
function<int(int,int)> f1 = add;
f1(4,2);
// f1 is a callable that take two int and return an int
```

**conversion operators**

conversion operator is a special member function that converts a value of a class type to a value of some other type general form: `operator type() const;`

```cpp
class SmallInt {
public:
		SmallInt(int i = 0): val(i) {
				if (i < 0 || i > 255)
				throw std::out_of_range("Bad SmallInt value");
		}
		
		operator int() const { return val; }
private:
		std::size_t val;
};
// int() will explicitly convert smallint to an int object
```

## Chapter 15. ObjectOriented Programming

Three key ideas in object oriented programming

- data abstraction
- inheritance
- dynamic binding

**inheritance**

- base class → derived classes
- base class defines virtual functions it expect the derived class to define
- derived class specify the class it inferit from in derivation list

```cpp
class quote {
public:
		std::string isbn() const;
		virtual double net_price(std::size_t) const;
}

class bulk_quote : public quote {
public:
		double net_price(std::size_t) const override;
}
```

**dynamic binding**

we can use the same code to process either base type or derived type interchangeable

```cpp
double print_total(ostream &os, const quote &item, size_t n) {
		double ret = item.net_price(n);
		os << "ISBN: " << item.isbn() << " total:" << ret << endl;
		return ret;
}
```

we can call this function **with either quote or bulk_quote object** the decision is made at `run-time` which is called  **dynamic binding**

**defining base classes**

```cpp
class Quote {
public:
		Quote() = default;
		Quote(const std::string &book, double sales_price):
				bookNo(book), price(sales_price) { }
		std::string isbn() const { return bookNo; }
		virtual double net_price(std::size_t n) const
				{ return n * price; }
		virtual ~Quote() = default;
private:
		std::string bookNo;
		protected:
		double price = 0.0;
};
```

- virtual keyword to specify which member will be overrided
- class define as a base class should always define a virtual destructor. so that each derived class will use its default destructor to override the virtual destructor. otherwise, derived class will use the destructor of base class, which may be problematic
- public → can be accessed by all derived class and outside calls
- private → private to current type only, cannot be directly accessed from derived class
- protected → can be accessed in derived class but not outside
- we can use "`final`" specifier to prevent inherit. For example, `class Noderived final { .. };`

**defining derived class**

```cpp
class Bulk_quote : public Quote {
		Bulk_quote() = default;
		Bulk_quote(const std::string&, double, std::size_t, double);
		double net_price(std::size_t) const override;
private:
		std::size_t min_qty = 0;
		double discount = 0.0;
};

// constructor, we use the constructor of the base class : Quote(book,p)
Bulk_quote::Bulk_quote(const std::string& book, double p,
std::size_t qty, double disc) : Quote(book,p), min_qty(qty), discount(disc) { }
```

- class derivation list: a colon followed by a comma separated list of name, each preceded by an access specifier of public, protected or private
- a derived class may access the public or protected member of its base
- a derived class may include virtual keyword on functions it overrides, but not required
- derived class is declared like any other class: `class bulk_quote;` ← do not need derivation list
- we can use constructor of base class in the initializer list, which initializes the base-class part

**static type and dynamic type**

- static type is known at compile time
- dynamic type is the object that expression represent that is not known until run-time

in the print_total functioin, static type is the base type, but we can pass derived type to it. so that the dynamic type depend on the run time argument passed

**derived to base conversion**

derived object contains:

1. a subobject containing members defined in the derived class itself
2. subobjects corresponding to each base class it inherits
- we can use a pointer to the base type to point to a derived object
- we can pass such pointer to where a base type is required

```cpp
Quote item;         // object of base type
Bulk_quote bulk;    // object of derived type
Quote *p = &item;   // p points to a Quote object
p = &bulk;          // p points to the Quote part of bulk, OK
Quote &r = bulk;    // r bound to the Quote part of bulk
```

- we can bind a base-class reference or pointer to the base class part of a derived object called "derived-to-base conversion"
- there is no reverse conversion, we cannot pass a pointer to the base type to where a derived type is required
    
    ```cpp
    Bulk_quote bulk;
    Quote *itemP = &bulk;       // ok
    Bulk_quote *bulkP = itemP;  // error: can't convert base to derived
    ```
    
- conversion only applies to reference or pointer type

**virtual function**

- dynamica binding happens when a virtual member function is called through a reference or pointer at run time.
- but when we call a virtual function on an expression on a non-reference or nonpointer type, that call is bound at compile time
- once a function declared as virtual, it remains virtual in all derived classes
- a derived class function that overrides an virtual function must have exactly the same parrameters as the base-class function that it overrides
- we can explicitly use "override" keyword to make the intention clear. we cal use "final" to prevent further override

**prevent dynamic binding**

we can prevent dynamic binding of a call to virtual function by forcing the call of a particular version:

For example: `double undiscounted = basePtr->Quote::net_price(42);` → calls the version from the base class

**Abstract base classes**

we can define member function as "pure virtual function" that does not have to be defined

- we specify a pure virtual function by adding = 0 in place of function body `double net_price(std::size_t) const = 0;`
- a class containing a pure virtual function is an abstract base class

**Access control and inheritance**

- access is controlled by the specifier in base class and access specifier in derivation list
- access to the member of a base class is controlled by the access specifier in the base class
- derivation access specifier control the access that of the members of base type to the users of the class

```cpp
class Base {
public:
		void pub_mem();
protected:
		int prot_mem;
private:
		char priv_mem;
};

struct Pub_Derv : public Base {
		int f() { return prot_mem; }            // ok
		char g() { return priv_mem; }           // error, canno access private
};

struct Priv_Derv : private Base {           // make base member private to user
		int f1() const { return prot_mem; }
};

Pub_Derv d1;
Priv_Derv d2;
d1.pub_mem(); // ok: pub_mem is public in the derived class
d2.pub_mem(); // error: pub_mem is private in the derived class
```

- users or the derived class based on priv_derv do not have access to member in base class
- "protected" members are inaccessible to the user but are accessible to members derived from this class.
- a derived class member of friend may only access protected member through the derived object

**Changing the access level of a name**

we can use "using" declaration and scope operator to give access to specific names

```cpp
class Base {
public:
		std::size_t size() const { return n; }
protected:
		std::size_t n
};

class Derived : private Base {
public:
		using Base::size;       // make size a public member
protected:
		using Base::n;          // make n a protected member
};
```

**class scope under inheritance**

**the scope of a derived class is nested inside the scope of its base classes,** therefore, if a name is unresolved in the scope of the derived class, the enclosing scope of the base class will be searched

- name lookup happens at compile time. The static type will determine which name is used
    
    ```cpp
    Bulk_quote bulk;  // (discount_policy is a function of the derived member)
    Bulk_quote *bulkP = &bulk;
    Quote *itemP = &bulk;
    bulkP->discount_policy();       // name can be found, bulkP has static type of bulk_quote
    itemP->discount_policy();       // error: itemP has type Quote*, cannot find the name
    ```
    
- name collision
    
    a derived class member with the same name as member of the base type hides direct use of the base class member. we can use scope operator to use hidden base class member
    
- the ordinary scope concept also applied to class inheritence, eg : so inner function will cover the outer function, do not overload

**virtual function and scope**

- virtual function and its override must have the same parameter
- virtual function will be called dynamically
- nonvirtual function with the same name will hide outside function and resolve at compile time

```cpp
class Base {
public:
virtual int fcn();
};

class D1 : public Base {
public:                     // D1 has 2 fcn, one is virtual fcn(), dynamical binding
		int fcn(int);           // another is a non-virtual fcn(int), statically bound
		virtual void f2();      // new virtual function
};

class D2 : public D1 {
public:
		int fcn(int);           // nonvirtual function hides D1::fcn(int)
		int fcn();              // overrides virtual fcn from Base
		void f2();              // overrides virtual f2 from D1
};
```

**Virtual destructor**

destructor needs to be virtual to allow objects in inheritance hierarchy to be dynamically allocated (when the object is dynamically allocated objects)

**Container that hold objects related by inheritance**

we define the container to hold pointers to the base type, which can also point to the derived type

## Chapter 16. Templates and Generic Programming

**Define function template**

if the only difference betweem two function is the type of their parameter, we can use a template:

```cpp
template <typename T>
int compare(const T &v1, const T &v2) {
		if (v1 < v2) return -1;
		if (v2 < v1) return 1;
		return 0
}
```

- a template definition start with the "template" keyword followed by a template parameter list, comma-separated bracketed by `< >`
- when we use a template, we implicitly or explicitly specify template arguments to bind the template parameter
- normally, the compiler use the argument to deduce the template argument: For example, `cout << compare(1,0) << endl;`

**Template parameter list**

each type parameter must precede by keyword class or typename, there is no distinction between "class" or "typename", "class" is old style

For example: `template <typename T, class U> calc(const T&, const U&);`

**instantiation of the template**

when a compiler see the template function call, it will instantiate a specific version of the function with the actual type argument in place of template argument:

`cout << compare(1, 0) << endl;` instantiate `int compare(const int&, const int&)`

- the compiler will and only then compile the int version of compare, the compiler does not generate code in template definition
- to instantiate the code, the compiler need the function body, so we should normally define the function at the same time as declaration

**define class template**

```cpp
template <typename T> class Blob {
public:
		typedef T value_type;       <- make alias for T as value_type
		typedef typename std::vector<T>::size_type size_type;
		Blob();
		Blob(std::initializer_list<T> il);
		size_type size() const { return data->size(); }
		bool empty() const { return data->empty(); }
		void push_back(const T &t) {data->push_back(t);}
		void push_back(T &&t) { data->push_back(std::move(t)); }
		void pop_back();
		T& back();
		T& operator[](size_type i);
private:
		std::shared_ptr<std::vector<T>> data;
		void check(size_type i, const std::string &msg) const;
};
```

**Initialize a class template**

when we use a class template, we must explicitly supply template argument

```cpp
Blob<int> ia;
Blob<int> ia2 = {0,1,2,3,4};
```

when compiler insstatiates a class from Blob, it replace T with the given template argument

- by default, a member function of a class template is instantiated only if it is used