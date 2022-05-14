# Overloaded Operations and Conversions
### Overload operator function
##### Overloading operators
An overloaded operator function has the same number of parameters as operator has operands:
- unary operator has one parameter
- binary operator has two (left hand side is passed to the first parameter)

##### Properties of overload operator function
- An overloaded operator may not have default arguments
- if overload function is a member function, the lefthand side is bound implicit to "this"
- we cannot change the meaning of an operator when applied to build-in type
- overload operator has the same precedure and associativity as the corresponding build-in operator

##### Calling a overload operator
We can either direct use the operator: `data1 + data2`, or use explicit call: `operator+(data1, data2)`

##### member or non-member implementation
we should consider if we make an operator a member function or not
- assignment `=`, subscript `[]`, call `()`, and `->` must be defined as members
- compound assignment should be members
- operators that change the state of the object, such as increment, should be members
- symmetric operator that require conversion should be defined non-member ( typeA + typeB should behavior the same as typeB + typeA, but the member function definition will implicit relate l.h.s. to the current type)

### Example of operator overload
##### overload `>>`
Normally, the first parameter of an output operator is a reference to a nonconst ostream object. since we ostream cannot be copied.
```cpp
ostream & operator<< (ostream &os, const sales_data &item){
	os << item.isbn()<< " " << item.units_sold << " "
	   << item.revenue << " " << item.avg_price() ;
	return os;
}
```
IO operator must be nonmember function. since for a member function, l.h.s. would have to be an object of class type.

##### overload `<<`
The first parameter is a reference to the stream to read from, the second parameter is a reference to the nonconst object into which to read

We usually return a reference to its given stream
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

##### overload arithmetic and relational operators
Usually defined as non-member functions to allow conversion, parameters should be reference to const.

##### overload `+`
```cpp
sales_data operator+ (const sales_data &lhs, const sales_data &rhs) {
	sales_data sum = lhs;
	sum += rhs;
	return sum;
}
```

##### overload `==` and `!=`
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

##### assignment operator
Assignment operator should be member function, and should return a reference to its left-hand operand.

A class can define additional assignment operators that assign object of other type to this object
```cpp
strvec &strvec::operator= (initializer_list<string> il) {
	auto data = alloc_n_copy(il.begin(), il.end());
	free();
	elements = data.frist;
	first_free = cap = data.second;
	return *this;
} // this is implicitly the l.h.s. object
```

##### compound assignment `+=`
```cpp
sales_data& sales_data::operator+=(const sales_data &rhs) {
	units_sold += rhs.units_sold;
	revenue += rhs.revenue;
	return *this;
}
```

##### subscript operator []
It should return a reference to the element that is fatched. We usually define both const and nonconst version of this operator
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

##### increment and decrement
They are defined as member function

##### prefix operator (eg `++`)
A prefix operator should return a reference to the incremented object
```cpp
StrBlobPtr& StrBlobPtr::operator++() {
	check(curr, "increment past end of StrBlobPtr");
	++curr;
	return *this;
}
```

##### postfix operator
Postfix operator accept an extra unused parameter of type int, and should return a reference to the object before incrementing.
```cpp
StrBlobPtr StrBlobPtr::operator++(int) {
	StrBlobPtr ret = *this;
	++*this;        // call the prefix version
	return ret;
}
```

Calling the prefix or postfix operator explicitly:
- prefix: `p.operator++();` 
- postfix: `p.operator++(0);`

##### function call operator `()`
Overloading function call operator allow the object to be used as they were functions
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
*Note* lambdas are function objects

##### library function type
library provide a function type that represent a callable (is a template class)
```cpp
function<int(int,int)> f1 = add;
f1(4,2);
// f1 is a callable that take two int and return an int
```

##### conversion operators
Conversion operator is a special member function that converts a value of a class type to a value of some other type general form: `operator type() const;`
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
