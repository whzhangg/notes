

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