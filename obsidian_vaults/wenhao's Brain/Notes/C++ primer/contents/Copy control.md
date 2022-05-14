# Copy control
### copy control
A class can define five special member functions (apart from constructors)
1. copy constructor 
2. copy-assignment operator 
3. move constructor 
4. move-assignment operator
5. destructor 

If they are not defined, the compiler automatically generate missing operations

### Copy constructor
##### Define copy constructor
Default copy constructor can be synthesized by the compiler, it will memberwise copies the member of its argument into the object being created.

Copy constructor is a constructor whoes first parameter is a reference to the class type and any other parameters should have default values
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
```
This copy constructure use initializer list to initialize object, which is the default initializer

##### copy initialization
When we use direct constructor, the compiler select the constructor of the best match, when we use copy constructor, the copy the right-hand side into the object

For example: `string nines = string(100,'9');` 
In this example, *string nine is copy constructed from a string that is constructed directly*

##### copy construction is different from assignment
`int i = j;` 
copy initialization is different from 
`int i;  i = j;`

Copy initialization happens when
1. define variables by copying using =
2. pass an object as an argument to a parameter of nonreference type
3. return an object from a function that has a non-reference return type
4. brace initialize the elements in an array

### Copy assignment
##### Define a copy assignment
Copy assignment controls how classes are assigned, for example, when:
```cpp
sales_data trans, accum;
trans = accum;              // use copy assignment
```

Copy assignment overload `=` operator, the lefthand operand is bound implicit to this parameter, the rhs is passed as an explicit parameter.

To be consistent with assignment for the build in types, copy assignment operator usually return a reference to their left hand side (although left hand side is modifed by the function body using this)

```cpp
sales_data& sales_data::operator=(const sales_data &rhs) {
	bookNo = rhs.bookNo;
	units_sold = rhs.units_sold;
	revenue = rhs.revenue;
	return *this;
}
// **copy assignment should consider the case when an object is assigned to itself**
```

### Destructor
Destructor is a member function with the name of the class prefixed by a tilde `~`. Because destructor does not take argument, it cannot be overloaded. Destructor has no return value and take no argument. 

Destructor body does not directly destoryed the members themselves, destruction happens after the destructor body: `~sales_data(){}`.

Destructor are called when:
1. variables go out of scope 
2. members of an object are destroyed when the object that contain them are destroyed
3. element in a container are destroyed when the contain is destroyed
4. dynamically allocated object destoryed by delete
5. temporary objects destroyed at the end of the expression

destructor is *not* run when a reference or a pointer to an object goes out of scope.

### Copy control
##### Generating default copy controls
We can explicitly generate default function using `=default` option
```cpp
class sales_data{
public:
	sales_data() = default;
	sales_data(const sales_data&) = default;
	...
}
```

##### Preventing copy
`= delete` option after a function signals to the compiler that we are intentionally not defining the members. Destructor should not be deleted!

##### Designing copy control
Copy determines whether a class has *value-like* or *pointer-like* behavior:
- class behave like value: each have their own state, copy should be independent from the origin
- class behave like pointers: class share states, copy access the same underlying data as origin

##### Class that act like values
The following class act like value
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

##### Class act like a pointer
The following class act like a pointer
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

##### swap
Class that manage resource usually define a function named swap
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
The library provide swap for the build in type, but for our class, we should use its own swap, not `std::swap`
