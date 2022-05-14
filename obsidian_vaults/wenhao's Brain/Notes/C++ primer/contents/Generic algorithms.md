# Generic Algorithms
### Generic algorithms
Library provide a set of algorithms, *independent of any particular container type*. Most are defined in the algorithm header. 

Most of the algorithm use *iterator* make the algorithm container-independent and require us to define operators of the container elements, eg, `<` or `==` operators

### Read-only algorithm
##### Find
`find(begin, end, val)` return an iterator to the first element that has the same value as `val`, return `end` if no match.

##### Sum
`accumulate(begin, end, init)`  (in the *numeric* header) 
Sum the elements in the given iterator range using `+` operator, with the provided initial value. Summing a string concatenates each element, since + is concatenate for string.

##### equivalence
`equal(begin1,end1,begin2)` 
Assuming that *second sequence is at least as big as the first*. It looks all element given in the first sequence, use `==` to compare element with the second sequence.

##### back inserter
*Insert iterator* is an iterator that adds elements to a container, which is called an *iterator adaptor*. It is defined in the `<iterator>` header.

When we assign to the element of a insert iterator, a new element equal to the right hand side is added to the container.
```cpp
vector<int> vec;
auto it = back_insert(vec);
*it = 42;                       // insert an new element 42
```

### Write algorithm
Write algorithm are algorithms that do not perform container operation. They can the value o the elements but they cannot change the container.

##### fill
`fill(begin, end, 0)`
Fill in each element in the given range with given value

##### copy
`copy(begin, end, a2)` 
Copy the element of the input range to another sequence denoted as `a2`

##### replace
`replace(begin, end, v1, v2)` 
Replace each element equal to the first value with second value in the given range

`replace_copy(begin, end, p, v1, v2)` (copy version) 
`p` is the destination in which we write the adjusted sequence, `origin` sequence is unchanged.

### Algorithm that reorder container elements
##### sort
`sort(begin, end)` 
Sort the elements in the range given.

#####
`unique(begin, end)` 
Reorder the sequence so that the unique elements appear in the first part of the vector, it return one past the last unique elements

For example:
```cpp
we input a list with elements:
	 fox | fox | jump | the | jump | tree | fox

-> fox | jump | the | tree | xxx | xxx | xxx      (unique elements are in the first half)
```

### Customizing operations
We can customize operation with which we perform the algorithm. For example, if we want to sort words by its length, we can use: `stable_sort(word.begin(), word.end(), is_shorter);`. *is_shorter* is a function that compare two elements

### Lambda expression
##### lambda expression
lambda expression is a *callable object* which we can pass to functions.

The structure of a lambda expression is as follows: 
```cpp
[capture list](parameter list) -> return_type {function body}
```
- *capture list* is a list of local variables defined in the enclosing function
- *parameter list*, *return type* and *function body* are as ordinary functions
- lambda function is defined like an expression
- `->` is needed for the return type

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

##### lambda capture
We have the following different ways to capture lambda inputs:
1. `[]`: empty capture list, lambda do not use any variable from the enclosing body
2. `[names]`: capture by value (copied)
3. `[&names]`: capture by reference
4. `[&]`: implicit by reference (compiler infer which variables we use in the lambda body)
5. `[=]`: implicit by value
6. `[&,names]`: default by reference, with the one specified by names is value captured
7. `[=,names]`: reverse

```cpp
void fcn1(){
		size_t v1 = 42;
		auto f=[v1] {return v1;}        // lambda is initialized here, it capture v1 here
		v1 = 0;                         // v1 is copied to lambda and that copy store with f
		auto j = f();
}
// f gets destroyed when going out of scope, since it is value capture
```

### bind function
##### Bind
Library provide a `bind` function, which is defined in the functional header
```cpp
auto newCallable = bind(callable, arg_list)
```

*arg_list* may include names of the form `_n`, which is called a *place holders*. They are defined in a namespace *placeholders*, in the std namespace. To use place holders, we must make the names known to our program, using, for example, *using namespace std::placeholders*

##### Binding a function
For example, assume `f` is a callable that has 5 parameter, we can bind f to another function g:
```cpp
auto g = bind(f, a, b, _2, c, _1);
```
This will generate a *new callable g that take 2 arguments*, represented by place holder `_2` and `_1`. Arguments to g are bound positionally to place holders: `g(X,Y)` will map g to `f(a, b, Y, c, X)`

Typically, we can use bind to reorder parameter: `bind(isShorter, _2, _1)` exchange the paremter to `isShorter`.
