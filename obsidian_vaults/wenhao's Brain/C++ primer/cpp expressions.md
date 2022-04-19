
# Expressions
### Expressions
##### lvalue and rvalue expression
- *lvalues* are the one that could appear on the left hand side of an expression,
- *rvalues* are those that could not.

In general, when we use an object as rvalue, we use its value (content); when we use object as an lvalue, we use its identities (location in memory). We can use an lvalue when an rvalue is required, but we can not do otherwise

##### Operators
There is unary operators ( &, * and so on), binary operator ( `==`, `*`, `+` and so on)

Some symbol can both be used as a unary or binary operator, it is helpful to think they are two different symbols. For example, ( * )

##### Order of evaluation
In most case, the order of evaluation is unspecified: `int i = f1() * f2()`. we are guaranteed that the result of `f1` is multiplied to `f2`, but we do not know whether `f1` is called first of `f2` is called first. If the two function affect the same object, the expression will have undefined behavior.

As a second example, consider:
```cpp
int i = 0; 
cout << i << "" << ++i << endl; // the value of the output is undefined
```

The evaluations that *do* have clear order are the following: 
1. logic AND: we are guaranteed that it evaluates its right-hand operand only if left-hand side is true
2. logic OR: similar to logic AND 
3. conditional operator `?:`
4. comma operator `,`

### Operators
##### Logical operators
```cpp
&& // logic AND
!  // logic NOT
|| // logic OR
```

##### Assignment and increment
Assignment is right associative
```cpp
int ival, jval; 
ival = jval = 0; // evaluated from left most assignment

while ( ival = get_value() != 42) {..} 
// assignment get_value() != 42 will be evaluated first
```

There are wwo types of increment:
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

Increment can occur in any order:
`*beg = toupper(*beg++);` will give undefined, beg appear in the same expression as `beg++`

##### Member access operator
Dot (`.`) give access for member of class type. We have:
- `ptr->member` is equivalent to `(*ptr).member`
- member access has high precedence than `*` , so `*p.size()` will take `p.size()` first

##### Conditional operator
A conditional expression is given by:
```cpp
cond ? expr1 : expr2;
```
The operator evaluate condition, if condition are true, `expr1` would be evaluated and returned, otherwise `expr2` would be evaluated and returned.
```cpp
string finalgrade = (grade < 60) ? "fail" : "pass"
// compound conditional operator
finalgrade = (grade > 90) ? "good" : (grade < 60) ? "fail" : "pass"
```

Conditional operator is right associative, so in the above expression, right hand side conditional operator is evaluated first

Conditional operator has a low precedence, so we sometime need to use ( ):  `cout << (grade < 60) ? "fail" : "pass" ;`

##### Sizeof operator
`sizeof()` return a constant expression of the type in *bytes*. It takes two form:
```cpp
sizeof(type);
sizeof expr; // size of the expression
```
    
sizeof operator does not evaluate its operand

##### Comma operator
It takes two operands and evaluate from left to right, guarantees the order of the evaluation. The left-hand size expression is evaluated and its result is discarded. the result of comma expression is the value of its right-hand expression
```cpp
for (vector<int>::size_type ix = 0; ix!=ivec.size(); ++ix, --cnt)
		ivec[ix] = cnt
```
In this example, the loop increments ix and decrements cnt, both `++ix` and `--cnt` are evaluated, but no result is returned here.

### Implicit type conversion
##### Implicit conversion
c++ does some implicit type conversions:
1. array to pointer : `int *ip = ia;`  (ia is an array of int)
2. const conversion: we can convert a pointer(reference) to a nonconst type to a pointer to a const type but we can not do the reverse

### Cast (explicit conversion)
##### named cast
Explicit type conversion is given by *named cast*: 
```cpp
cast-name<type> (expression)
```
Where  type is the target type and the expression is the value to be cast.

Cast-name is one of the follow:
##### static_cast
Any well defined type conversion, except involving low-level const, can be requested using static_cast
```cpp
int j,i; 
double slope = static_cast<double>(j)/i 
// convert j from int to double in the expression
```
    
##### const_cast
Changes only a low level const in its operand, (low level here means the object that a pointer or reference points to)
```cpp
const char *pc;*
*char * p = const_cast<char*>(pc);
// we convert a const to a nonconst type by const_cast
```
    
##### reinterpret_cast
A low level reinterpretation of its operands  
```cpp
eg :: int *ip;*
*char * pc = reinterpret_cast<char*>(ip);
// reinterpret ip as a pointer of character and assign its value to pc
```
    