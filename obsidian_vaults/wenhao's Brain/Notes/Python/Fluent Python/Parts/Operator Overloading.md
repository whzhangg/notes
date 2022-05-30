# Operator overloading
### Operator overloading
##### Overview
Operator overloading in python is done by *implementing the corresponding special methods*. We have the following rules:
- We cannot overload operators for build-in types
- We cannot create new operators
- A few operators cannot be overloaded: *is*, *and*, *or* and *not*

As convention, for operator overloading, we should not modify any of the operands, we should return a new object

##### Unary Operators
Python has the following unary operators:
```python
__neg__()   # negative -v
__pos__()   # positive +v
__abs__()   # abs(v)
```

### Overloading addition
##### `__add__` and `__radd__`
With only `__add__` defined for the Vector class, we will receive the error:
```python
vector + (1, 2, 3)
>>> OK
(1, 2, 3) + vector
>>> TypeError: can only concatenate tuple (not "Vector") to tuple 
```

##### Resultion steps for additions
When we write an expression `a + b`, python perform the following steps:
1. If a has `__add__`, call `a.__add__(b)` and return results
2. If a doesn't have `__add__` or calling it return NotImplemented, check if b has `__radd__`, if so, call `b.__radd__(a)` and return results
3. if b doesn't have `__radd__`, raise error
Therefore, to properly define addition (when a and b are of different class), *we should define both `__add__` and `__radd__` method*.

##### `__iadd__`
+= operator default to a = a + b, which use `__add__` and return an new object. To perform inplace addition, we need to implement `__iadd__` special methods.

Example
```python
def __add__(self, other): 
	try:
		pairs = itertools.zip_longest(self, other, fillvalue=0.0) 
		return Vector(a + b for a, b in pairs)     # properly return a new object
	except TypeError:
		return NotImplemented                # catching error as NotImplemented
                                             # is the expected behavior 
def __radd__(self, other):  
	return self + other          # use the __add__ method

def __iadd__(self, other):       # a += b
	if isinstance(other, Tombola):
		other_iterable = other.inspect() 
	else:
		try:
			other_iterable = iter(other)     # obtain an iterator
		except TypeError:
			self_cls = type(self).__name__
			msg = "right operand in += must be {!r} or an iterable" 
			raise TypeError(msg.format(self_cls))
	self.load(other_iterable)   # add the other type
	return self                 # result of the inplace operation return self

def __eq__(self, other):
	if isinstance(other, Vector):
		return (len(self) == len(other) and
			all(a == b for a, b in zip(self, other)))
	else:
		return NotImplemented   # check type
```

### Operators that can be overloaded
##### List of special method for operator overloading:
| Operator | forward | reverse | in place |
| -- | -- | -- | -- |
|`+`          | `__add__`         | `__radd__`      |     `__iadd__`
|`-`           |`__sub__`         | `__rsub__`       |    `__isub__`
| `*`          | `__mul__`         | `__rmul__`     |      `__imul__`
|`/`           |`__truediv__`     | `__rtruediv__`    |   `__itruediv__`
|`//`      | `__floordiv__`    | `__rfloordiv__`    |  `__ifloordiv__`
|`v%`          | `__mod__`         | `__rmod__`    |       `__imod__`
|`divmod()`    |`__divmod__`      | `__rdivmod__`   |     `__idivmod__`
|`**`, `pow()`  | `__pow__`         | `__rpow__`     |      `__ipow__`
|`@`          | `__matmul__`      | `__rmatmul__`   |     `__imatmul__`
|`&`          | `__and__`         | `__rand__`       |    `__iand__` |
|`or`      |    `__or__`          | `__ror__`       |     `__ior__` |
|`^`          | `__xor__`         | `__rxor__`       |    `__ixor__`
|`<<`       |   `__lshift__`      | `__rlshift__`      |  `__ilshift__`
|`>>`       |   `__rshift__`      | `__rrshift__`     |   `__irshift__`

##### Comparsion Operators
| Operator | forward | reverse | 
| -- | -- | -- | 
|a == b   |  `a.__eq__(b)`    | `b.__eq__(a)`      
|a != b   | `a.__ne__(b)`    | `b.__ne__(a)`   
|a > b    | `a.__gt__(b)`    | `b.__lt__(a)`  
|a < b    | `a.__lt__(b)`    | `b.__gt__(a)`  
|a >= b   | `a.__ge__(b)`    | `b.__le__(a)`
|a <= b   | `a.__le__(b)`    | `b.__ge__(a)`
