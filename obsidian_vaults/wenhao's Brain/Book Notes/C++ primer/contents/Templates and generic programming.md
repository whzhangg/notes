# Templates and Generic Programming
### Defining function template
##### Function template
If the only difference betweem two function is the type of their parameter, we can use a template:
```cpp
template <typename T>
int compare(const T &v1, const T &v2) {
	if (v1 < v2) return -1;
	if (v2 < v1) return 1;
	return 0
}
```

A template definition start with the *template* keyword followed by a template parameter list, comma-separated bracketed by `< >`

When we use a template, we implicitly or explicitly specify template arguments to bind the template parameter. Normally, the compiler use the argument to deduce the template argument: For example, `cout << compare(1,0) << endl;`

##### Template parameter list
Each type parameter must precede by keyword *class* or *typename*, there is no distinction between "class" or "typename", "class" is old style.
For example: `template <typename T, class U> calc(const T&, const U&);`

##### instantiation of the template
When a compiler see the template function call, it will instantiate a specific version of the function with the actual type argument in place of template argument:
`cout << compare(1, 0) << endl;` 
will instantiate the template
`int compare(const int&, const int&)`

The compiler *will and only then* compile the int version of compare, the compiler does not generate code in template definition. To instantiate the code, the compiler need the function body, so we should normally define the function at the same time as declaration

### Class template
##### Define a class template
A class template can be defined as in the following example:
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

##### Initialize a class template
When we use a class template, we must explicitly supply template argument
```cpp
Blob<int> ia;
Blob<int> ia2 = {0,1,2,3,4};
```
When compiler instantiate a class from Blob, it replace T with the given template argument. By default, a member function of a class template is instantiated only if it is used.