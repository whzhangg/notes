# C++ primer
Created: September 28, 2021 9:08 PM

[[Basic cpp]]
[[Variables and basic types]]
[[Strings vectors and arrays ]]
[[cpp expressions]]
[[statements and exceptions]]
[[cpp Functions]]
[[cpp Classes]]


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