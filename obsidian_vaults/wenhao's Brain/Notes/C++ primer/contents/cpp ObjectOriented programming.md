# ObjectOriented Programming
### Overview
##### Three key ideas
Three key ideas in object oriented programming
1. Data abstraction
2. Inheritance
3. Dynamic binding

##### inheritance
Derived classes defined from on base classes: Base class defines virtual functions it expect the derived class to define. 

Derived class specify the class it inferit from in *derivation list*.

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

##### Dynamic binding
We can use the same code to process *either base type or derived type interchangeable*.
```cpp
double print_total(ostream &os, const quote &item, size_t n) {
	double ret = item.net_price(n);
	os << "ISBN: " << item.isbn() << " total:" << ret << endl;
	return ret;
}
```

We can call this function *with either quote or bulk_quote object* the decision is made at run-time.

### Using inheritance
##### Defining base classes
The following example defines a base classes:
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
Points to note:
- *virtual* keyword to specify which member will be overrided
- class define as a base class should always define a *virtual destructor*. so that each derived class will use its default destructor to override the virtual destructor. Otherwise, derived class will use the destructor of base class, which may be problematic.

##### Access control
1. public: members that can be accessed by all derived class and outside calls.
2. private: private to current type only, cannot be directly accessed from derived class.
3. protected: can be accessed in derived class but not outside

we can use "`final`" specifier to prevent inherit. 
For example, `class Noderived final { .. };`

##### defining derived class
The following codes defines an derived class:
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
Points to note:
- *Class derivation list* is a colon followed by a comma separated list of name, each preceded by an access specifier of public, protected or private.
- A derived class may access the public or protected member of its base
- A derived class may include virtual keyword on functions it overrides, but not required
- we can use *constructor of base class in the initializer list*, which initializes the base-class part

Derived class is declared like any other class: `class bulk_quote;` ← do not need derivation list

##### static type and dynamic type
*Static type* is known at compile time, while *dynamic type* is the object that expression represent that is not known until run-time. In the print_total functioin, static type is the base type, but we can pass derived type to it. so that the dynamic type depend on the run time argument passed.

##### derived to base conversion
Derived object contains:
1. A subobject containing members defined in the derived class itself
2. Subobjects corresponding to each base class it inherits

Furthermore, 
- we can use a pointer to the base type to point to a derived object,
- we can pass such pointer to where a base type is required.

```cpp
Quote item;         // object of base type
Bulk_quote bulk;    // object of derived type
Quote *p = &item;   // p points to a Quote object
p = &bulk;          // p points to the Quote part of bulk, OK
Quote &r = bulk;    // r bound to the Quote part of bulk
```

We can bind a base-class reference or pointer to the base class part of a derived object called "derived-to-base conversion". There is no reverse conversion, we cannot pass a pointer to the base type to where a derived type is required
    
```cpp
Bulk_quote bulk;
Quote *itemP = &bulk;       // ok
Bulk_quote *bulkP = itemP;  // error: can't convert base to derived
```
Such conversion only applies to reference or pointer type

##### virtual function
*Dynamica binding* happens when a virtual member function is called through a reference or pointer at run time. When we call a virtual function on an expression on a non-reference or nonpointer type, that call is bound at compile time
- once a function declared as virtual, it remains virtual in all derived classes
- a derived class function that overrides an virtual function must have exactly the same parrameters as the base-class function that it overrides
- we can explicitly use *override* keyword to make the intention clear. we cal use *final* to prevent further override

##### prevent dynamic binding
We can prevent dynamic binding of a call to virtual function by forcing the call of a particular version:
For example: `double undiscounted = basePtr->Quote::net_price(42);` calls the version from the base class.

##### Abstract base classes
We can define member function as "pure virtual function" that does not have to be defined, a class containing a pure virtual function is an abstract base class

We specify a pure virtual function by adding = 0 in place of function body `double net_price(std::size_t) const = 0;`

### Access control and inheritance
##### Access control specifier
Access is controlled by the *specifier in base class* and *access specifier in derivation list*, 
1. Access to the member of a base class is controlled by the access specifier in the base class
2. Derivation access specifier control the access that of the members of base type to the users of the class

The following example illustrate the access control
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
- Users of the derived class based on priv_derv do not have access to member in base class
- *protected* members are inaccessible to the user but are accessible to members derived from this class.
- A derived class member of friend may only access protected member through the derived object

##### Changing the access level of a name
We can use "using" declaration and scope operator to give access to specific names:
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

##### class scope under inheritance
tThe scope of a derived class is *nested inside the scope of its base classes*, therefore, if a name is unresolved in the scope of the derived class, the enclosing scope of the base class will be searched.

The name lookup happens at compile time. The static type will determine which name is used
```cpp
Bulk_quote bulk;  // (discount_policy is a function of the derived member)
Bulk_quote *bulkP = &bulk;
Quote *itemP = &bulk;
bulkP->discount_policy();       // name can be found, bulkP has static type of bulk_quote
itemP->discount_policy();       // error: itemP has type Quote*, cannot find the name
```
 
##### name collision
A derived class member with the *same name* as member of the base type *hides direct use of the base class member*. we can use scope operator to use hidden base class member.

The ordinary scope concept also applied to class inheritence, eg : so inner function will cover the outer function, do not overload

##### virtual function and scope
A virtual function and its override must have the same parameter, virtual function will be called dynamically

Nonvirtual function with the same name will hide outside function and resolve at compile time
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

##### Virtual destructor
Destructor needs to be virtual to allow objects in inheritance hierarchy to be dynamically allocated (when the object is dynamically allocated objects)

##### Container that hold objects related by inheritance
We define the container to hold pointers to the base type, which can also point to the derived type
