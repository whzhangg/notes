
# Inheritance
### Inheritance in python
##### Avoid inheriting the build in types
In the C implementation of python, *build-in types themselves (list, dict) are "not so pythonic"*, as their internal methods sometimes do not use the special functions ( For example, `__setitem__` is ignored by `__init__` methods of the build-in dict).

Therefore, We should *avoid* inheriting the build in types, such as `class CustomDict(dict)`. Instead, we should inherit these types from collections, `UserList`, `UserDict` and `UserString`

##### Multiple inheritance and Method resolution
Python can inherit from multiply classes. *Method resolution* specifies the order of lookups

Python class maintain an attributes (Class attributes) called `__mro__` (method resolution order), which hold a tuple of referneces to the superclasses. Python will follow the order in MRO when traversing the inheritance graph:
```python
hasattr(list, "__mro__")
>>> True
print(list.__mro__)
>>> (<class 'list'>, <class 'object'>)
import numbers
print(numbers.Integral.__mro__)
>>> (<class 'numbers.Integral'>, <class 'numbers.Rational'>, <class 'numbers.Real'>, <class 'numbers.Complex'>, <class 'numbers.Number'>, <class 'object'>)
```

In case of multiple inheritance `class c(a, b)` and if both a and b implemented a method of the same nam, `__mro__` determines uniquely which method to call when we call `super().method()`.

##### Invoking specific superclass methods directly
In the case of multiple inheritance, we can also invoke a method on the superclass directly
```python
class C(A, B):
	...
	def method1(self):
		super().method1()    # we rely on MRO to determine which method to call
		A.method1(self)      # we explicitly ask to use method defined in class A
```

##### Rules on multiple inheritance
- Distinguish interface inheritance (internal structure relationship) from implementation inheritance (avoid code duplication)
- Make interface explicit with ABC
- Using mixins for code reuse https://coderbook.com/@marcus/deep-dive-into-python-mixins-and-multiple-inheritance/
- Make Mixins explicit by naming, eg: PackMixin
- Don't subclass from more than one concrete class
- Favor Object composition over inheritance
