
# Classes
### Data abstraction and encapsulation
Data abstraction is the separation of interface and implementation
- Interface is the operations uses can execute
- Implementation is the part that is hidden from user

Encapsulation force class to hide its implementation

### Member functions
##### Declare member functions
We have the following rule for declaring member functions:
- member functions must be declared inside the class
- member functions maybe defined outside the class body
- the compiler process class first with declarations, then process the function body
    
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

A function that defined outside the class must include the name of the class of which it is a member, using the *scope operator* (::). Once compiler see the function name, the rest of the code is seen as being inside the scope of the class, so revenue and units_sold is implicitly referring to the members of sales_data

```cpp
double sales_data::avg_price() const {
    if (units_sold) return revenue/units_sold;
    lse  return 0;
}
```

##### this
Member function access the object on on which they were called through an *implicit parameter* named `this`. When we call `total.isbn();` the compiler interpret as `sales_data::isbn(&total);` which pass the address of `total` object
    
`this` is a *const pointer*. Inside a member function, we can directly refer to the member of the object on which the function is called. i.e. It's unnecessary to use `this→units_sold`

##### const member functions
`this` is an implicit parameter, if we want to indicate `this` to be a pointer to a const, i.e., we will not change the object itself through the member function, we put a *const* after the parameter list:
```cpp
std::string isbn() const {retrun bookNo;}
// is interpreted as
std::string sales_data::isbn(const sales_data *const this) {..}
```
    
##### Function that return `this`
To return the object itself, we can usually return a reference of the object, as follows
```cpp
sales_data& sales_data::combine(const sales_data &rhs){
	..
	return *this;   //dereference and return the content of the object
}
// we return a reference by sales_data&
```

##### nonmember functions
Functions that are conceptually a part of a class but not defined inside the class, should be declared in the same header as the class itself

### Constructors
##### constructors
Constructors have the same name as the class, and does not have return type, a class can have multiple constructors

Constructors can not be declared as const. since, when we create an object, the object does not have its "constness" until after the constructor completes the initialization

As an example, we can create 4 constructor for sales_data:
```cpp
struct sales_data{
	sales_data() = default;           // default initializer
	sales_data(const std::string &s): bookNo(s) { }   // defined initializer
	sales_data(const std::string &s, unsigned n, double p):   // with initializer list
				bookNo(s),units_sold(n),revenue(p*n) { }
	sales_data(std::istream &);                         <- declare initializer
		
	std::string bookNo;
	unsigned units_sold = 0;            // default member initialize
	double revenue = 0;
}
```

##### default initialization
If (and only if)we do not explicitly define any constructor, compiler will implicitly define default constructor called *synthesized default constructor*, which *default initialize* the members.

If we are defining other constructors but still want to keep the default, we can use `= default` after the parameter list to geneater the default constructor `sales_data() = default;` which generate a default constructor that take no parameter, as the example above.

##### use constructor initializer list
Constructor initializer list is a list of member names after the colon and before the function body ({}). 
```cpp
sales_data(const std::string &s): bookNo(s) { }
sales_data(const std::string &s, unsigned n, double p):
					bookNo(s),units_sold(n),revenue(p*n) { }
```

Each member are followed by member's initial value. Multiple initialization are separated by `,`.
If a member is omitted from the list, it is implicitly default initialized. If no further work to be done, the function body can be empty, but not required to.

##### Defining a constructor outside the class body
```cpp
sales_data::sales_data(std::istream &is) { read(is, *this); }
```

A constructor have no return type, therefore function definition start with name, which is in the scope of the class. 

If we do not have a initializer list (empty list), the members of this object are still initialized *before* the constructor body is executed. Members that do not appear in initialized list are initialized by the corresponding default initializer and are defult initialized. *So when the function body start to execute, the member already have default values*.

##### Copy, assignment and destruction
Class also control what happens when we copy, assign or destroy objects of the class. If we do not define these operations, the compiler will synthesize them for us, which will copy, assign or destroy each member of the object.

### Access control
##### Public, Private
In c++, we use access specifiers to enforce encapsulation:
- members defined after a *public* specifier are accessible to all parts of the program,
- members defined after a *private* specifier are accessible to the member functions of the class, but not to code uses the class.

A class may contain mulitple specifier, and there is no restriction on how often a specifier may appear, each specifier control the access level of the succeeding members. So, public and private can appear multiple times.
```cpp
class sales_data {
public:
	sales_data() = default;

private:
	std::string bookNo;
}
```

##### Struct and Class
The only difference between struct and class is the default access level:
- struct: members defined before the first access control are public,
- class: members defined before the first access control are private.

We use struct when we are intending for all its members to be public.

##### friend
A class can allow other class or function to access its nonpublic member by making them a *friend*, by including a declaration for that function preceded by the keyword friend. Friend declaration can only appear (anywhere) inside a class definition.

A friend declaration only specifies access, *it is not a declaration of the function*. If we want to use the function, we must also declaration it separately from the friend declaration.
```cpp
class sales_data {
friend sales_data add(const sales_data&, const sales_data&);  
public:
    sales_data() = default;
private:
    std::string bookNo;
}
// declaration of function
sales_data add(const sales_data&, const sales_data&);         
```
    
### additional class features
##### Redefining type names in class
We can use typedef in class:
```cpp
public:
    typedef std::string::size_type pos;     // define pos as a name for a type
    using pos = std::string::size_type;     // equivalent as above
    
private:
    pos cursor = 0;                         // using pos a a type
```
    
##### mutable data member
If we include mutable keyword in the member declaration, such a member will never be const, even if it is a member of a const object
    
```cpp
private:
    mutable size_t access_ctr;    // mutable
    void some_function() const {  // const member function
    	++ access_ctr;            // still can change access_ctr
    }
```
    
##### class declaration
We can declare a class without defining it, called "forward declaration". For example: `class screen;`. after declaration and before a definition, the class is an incomplete type. A type must be defined before we can write code that create objects of that type
    
##### making a member function as friend
We can make a class a friend 
```cpp
class screen {
    friend class window_mgr;
}
```
    
We can also make only a member function a friend
```cpp
class screen {
    friend void window_mgr::clear(index);
}
```
    
Function overload and friendship:
Overload are different functions that share a same name. if we want to declare a overload function, we must declare each function in a set of overloaded functions
    

### Class scope
##### Scope operator
To access data and member function, we can only do through an object (reference or pointer). To access defined type members, we need to use the scope operator.
```cpp
screen::pos ht = 24;    // use type pos defined in screen
screen scr(ht, wd, '');
screen *p = &scr;
c = p->get();           // access through a pointer
```
    
If function is defined outside the class using scope operator: 
```cpp
void window_mrg::clear(screen_index i) {..}
```
The paramter list and function body auotmatically be in the scope of the class

##### Return type of member function
The return type is before the function name, thus not in the scope of the class we need to add scope to the return type: 
```cpp
window_mgr::screen_index window_mgr::addscreen(const screen &s);
```

##### How compiler look up the names
For a normal name, compiler look for:
1. declaration of the name in current block before usage
2. look in the outer scopes
3. error if nothing is found

The compiler look for names in member function body
1. declarations inside the member function
2. name declared inside the class
3. if not found in the class, look for name in the outer scope before the function definition

Name in member function outside class definition: the outside scope include the code after class but before definition of member function

### More about constructors
##### using constructor initializer
Compare the two code.
```cpp
sales_data::sales_data(const string &s, unsigned cnt, double price) {
		bookNo = s; units_sold = cnt; revenue = cnt*price;
}   
```
and
```cpp
sales_data(const std::string &s, unsigned n, double p):
								bookNo(s),units_sold(n),revenue(p*n) { }
// do the initialization
```
In the first example, initializer is ommited and all members *are initialized to default* and then assigned value. 

Sometimes, we have to initialize some members by initializer list. For example, `const` or `reference` must be initialized or members of a class type that must initialize with parameters.

##### sequence of initialization
Initializer list specifices the values, but not sequence, *members are initialized in the order of which they appear in class definition*.

##### Delegating constructors
A delegating constructor use another constructor from its own class to perform initialization
```cpp
class sales_data {
	public:
		sales_data(const std::string &s, unsigned n, double p):
		bookNo(s),units_sold(n),revenue(p*n) { }                   // non delegating constructor
		sales_data(): sales_data("",0,0) {}                        // delegating constructors
		sales_data(std::string s): sales_data(s,0,0) { addition work; }
}
```

A delegating function will do all the work of a constructor, after delegating constructor complete their work, the body of the constructor will executed.

##### Using a default constructor
`sales_data obj();` defines a function, instead of declaring a object. `sales_data obj;` declare an object

##### Class-type conversion
Each constructor that is called with a single argument defines an implicit conversion For example, for sales_data, we can initialize it with string, so it defines an implicit conversion between string and sales_data:
```cpp
string book="0-123-123";
item.combine(book);   
// combine require a sales_data type, which is converted from string
```

Only one type conversion is allowed:
```cpp
item.combine("0-123-123");   
// error, "0-123-123" is literal, but combine accept string
item.combine(string("0-123-123"));  // OK
```

We can prevent the implicit conversion by using *explicit* keyword in constructor declaration. For example: 
```cpp
explicit sales_data(const std::string &s): bookNo(s) {}
```
This disable the above type conversion. explicit can only used inside a class definition, not in member function definition outside class

### Static class members
##### Static members
We can define some members (data, function) that is *associated with the class, not with the individual objects*.
- this is specified by keyword "static"
- can be public or private
- Static members are not initialized by constructor, normally, we initialize the static member outside the class body.
- the static member exist outside any object, so bank_account will only contain two data members: owner and amount
- A static member function also not bound to any object, so they *do not have `this` pointer*. 

##### Access
We can assess static member by scope operator, or by any object
```cpp
double r; bank_account ac1;
r = bank_account::rate();   // access using scope
r = ac1.rate();             // direct access using object
```
    
Member function can use static members directly
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
