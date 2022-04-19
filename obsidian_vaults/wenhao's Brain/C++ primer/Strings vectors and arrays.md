
# Strings, Vectors and Arrays
### Using declaration
##### Using declaration
`using` is declaration let us to use a name from a namespace without specifically refering to the namespace, for example: `using std::cin;`. A separate `using` is needed for each name

we *should not use `using` declaration in header files*. since header file will be copied into the c program and may introduce unexpected name conflicts. ( unless we use some form of pre-compile check)

### String
##### example
The following code initialize a string and perform operation:
```cpp
a.empty()   // return if a is empty
a.size()    // return the size of string
s[n]        // return a reference to the char at position n
s1 + s2     // concatenation
```
*Note* that string literals (instead of variable) does not support the same operation as strings. For example, string literals can not be added together

##### Indexing, or subscript
Strings can be indexed by `s[n]`. If the index `n` has a signed type, its value will be converted to unsigned.

Range of the subscript is unchecked, therefore it's better to defined as unsigned int

##### Ranged for
*Ranged for* statement iterates through the elements in a given sequence and perform operation on each value.
```cpp
for (declaration : expression)
    statement
```
Expression is a object that represents a sequence, and declaration defines the variable we use to access the elements. The following example print each character of the string:
```cpp
for (auto c : str1 )
    cout << c << endl;
```

##### Using reference to change the character in a string
To change the characters in a string, we need to use a reference. For example:
```cpp
for (auto c : str) c = toupper(c);
```
will not change the string. In this case, we are copying each str to a character c, so that when we change c, we do not change the value of the original string. 

To do so, we use a reference: `&c` refer to the object itself, and when we are changing c, we really changed the object
```cpp
for (auto &c : str) c = toupper(c)
```

### Vector
##### Using vectors
Vector usually refered to as a container because it contains other objects, it is a *class template*, instantized by suppling type in the `<>`. 
```cpp
vector<int> ivect;
vector<scales_item> sales_vect;
```
Vector is initialized to empty by default

The following code example shoes the basic operations of the vector type
```cpp
vector<int> v2;
v2.push_back(10); // append element onto the back of the vect
v.empty()         // return if v is empty
v.size()          // return the size
v[n]              // subscription
```

Range for is also available to iterative through vector, and similarly, we need to use reference to change elements

##### Templates
Templated can be for class and function. They are not themselves functions or class, but they are instructions to the compiler for generating classes or functions. This process is called  *instantiation*.

### Iterators
##### Basic definitions
Iterator is *a type that a class defines to iterate through its objects as pointer*, it does not hold the object, so we need to dereference iterator to access the object it points to.

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

##### constant iterators
If we do not want to change the element that we iterate through, we can use constant version of the iterator `.cbegin()`:
```cpp
auto it = s.cbegin(); <- refer to a const type
it != s.cend()
```

##### Access the member of an iterator (pointer)
if we want to access the method of the object iterator point to, we need to dereference it and than access using `.`, For example `(*it).empty()`, this is equivalent to: `it->empty()`

##### Iterator arithmetic
iterator for string and vector support additional operation:
- `iter +(-) n` return an iterator that move forward and backward n step
- `iter += n` assign iter to iter + n
- `iter1 - iter2` yield a number as the number of step between two iterator
- comparsion (> < = )

They are used in the following example:
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

### Build in arrays
##### Properties of array
Array is a container of unnamed objects of a single type that we access by position. It can be created by: 
```cpp
int a[4] = {0,1,2,3}
```
Array has the following properties:
- array is a compound type
- array has fixed size (or const expression) that must be specified at declaration
- we cannot use auto to sepcify an array

*Note*: character array has an additional null character at the end, so its length is larger by the visual size by 1, for example: `char a[6] = 'Daniel';`  `Deniel\\0` is a 7 character array

##### Array cannot be copied
We cannot initialize an array as a copy of another array, it is also not legal to assign one array to another.
```cpp
int a2[] = a; // error
a2 = a;       // error
```

##### Array of pointers or pointer of array
The following code example defines array of pointers
```cpp
int *ptrs[10];            // defines a array of 10 pointers to int
int (*parray)[10] = &arr; // defines a pointer to an array of 10 int
int (&rarray)[10] = arr;  // reference
```
Type modifier bind from right to left, so in the first case, it is understood as *(ptrs[10])

##### Pointer and arrays
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

Subscripting an array `int i = arr[2];` equivalent to `int i = *(&arr[0] + 2);`. We can also subscript a pointer, treating it as an array:
```cpp
int *p = &ia[3];
int k1 = p[1];  // ia[4]
ink k2 = p[-2]; // ia[1], equivalent to *(&ia[3]-2)
```

### Multidimension arrays
##### Initialization
A multidimension array is understood as "array of arrays". For example `int ia[3][4];` is an array of size 3, each element is array of size 4

Multidimension array can be initialized as:
```cpp
int ia[3][4] = {
		{0,1,2,3},{4,5,6,7},{8,9,10,11}
}
```

##### Subscripting
if we provide less subscripts than dimensions, we get a array elements: For example, `int (&row)[4] = ia[1];` is reference to a 4 dimension array point to the second element

Range for for loop over array elements
```cpp
for (auto &row : ia )
    for (auto &col : row) {
        ... (col is int & type)
    }
}
```

##### Pointer with multidimension arrays
if we use the name of multidimension array, it will converted to a pointer
```cpp
int ia[3][4];
int (*p)[4] = ia; // ia is used as &ia[0], p is an pointer to a array[4]

// in this case, it is easier to use auto:
auto p = ia;      
```
