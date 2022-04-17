# A Pythonic Object
### Pythonic objects
##### Inspecting an objects
dir() return the list of attributes of the object, if it is called without argument, it return the names in the current scope.

For example: `dir(int)` gives the following output:
```python
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', 
     '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', 
     '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', 
     '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', 
     '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', 
     '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', 
     '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', 
     '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', 
     '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', 
     '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 
     'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 
     'imag', 'numerator', 'real', 'to_bytes']
```
    
##### Duck typing
>"If it walks like a duck and it quacks like a duck, then it must be a duck" 

See [[Python type annotation#Don't overuse Duck typing]]

### Define a pythonic object
##### Special methods of a pythonic object

| special methods | what they do |
| -- | -- |
| `__new__` | creates the object, this is done before `__init__`. [Ref](https://python.ms/new/#_2-new-は、いつ使うの)
| `__repr__` | used by repr() to return a string representing the object as **developers** wants to see it
| `__str__` | used by str() to return a string representing the object as **users** wants to see it 
| `__iter__` | make the object iterable, which can support, for example, unpacking and convert it to other iterable
| `__eq__` | value comparsion accessed by == operator
| `__bool__`  | determines how the object is converted to bool value, when a bool value is needed
| `__bytes__` | used by byte() to convert the object to bytes
| `__format__` | used by format() function to format display
| `__hash__` | make the object hashable with hash(), The object need to be immutable
| `__int__` | convert objects to int value with int(), similar, we have __float__ method
| `__len__` | return the length of an object
| `__getitem__` | return an item given a position as parameter

A Pythonic vector class implementing these methods    
```python
# A pythonic class
from array import array 
import math
class Vector2d: 
    typecode = 'd'                   # class attributes
    
    def __init__(self, x, y): 
    	self.__x = float(x) 
    	self.__y = float(y)
    
    @property
    def x(self):                     # using property to make x and y
    	return self.__x              # immutable
    
    @property
    def y(self): 
    	return self.__y
    
    def __iter__(self):              # make the object iterable: x, y = vector1
    	return (i for i in (self.x, self.y))
    
    def __repr__(self):
    	class_name = type(self).__name__
    	return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
    	return str(tuple(self))
    
    def __bytes__(self):
    	return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))) 
    
    def __eq__(self, other):
    	return tuple(self) == tuple(other) 
    
    def __hash__(self):
    	return hash(self.x) ^ hash(self.y) 
    
    def __abs__(self):
    	return math.hypot(self.x, self.y)
    
    def __bool__(self): 
    	return bool(abs(self))                   # if vector1:
    
    def angle(self):
    	return math.atan2(self.y, self.x)
    
    def __format__(self, fmt_spec=''):           # format(vector1, "p")
    	if fmt_spec.endswith('p'):               # "{:p}".format(vector1)
    		fmt_spec = fmt_spec[:-1]
    		coords = (abs(self), self.angle())   # p print the vector 
    		outer_fmt = '<{}, {}>'
    	else:
    		coords = self
    		outer_fmt = '({}, {})'
    	components = (format(c, fmt_spec) for c in coords) 
    	return outer_fmt.format(*components)
    
    @classmethod
    def frombytes(cls, octets):
    	typecode = chr(octets[0])
    	memv = memoryview(octets[1:]).cast(typecode) 
    	return cls(*memv)
```

##### Classmethod and statistic method
`@classmethod` decorator define a method that operates on class and not on instance: `Vector.frombyte()` (on class) instand of `vector1.frombyte()` (on instance)

The first argument passed to a classmethod is the class itself (Vector.frombyte(), Vector is passed as the first argument). By convention, the first parameter of a class method should be named cls.

Classmethod usually return an instance of the class
```python
class Person:

def __init__(self, name, age):
	self.name = name
	self.age = age
@classmethod
def fromBirthYear(cls, name, year):
	return cls(name, date.today().year - year)

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
```

By contrast, `@staticmethod` decorates a method to be just like a plain function that live in a class body. Calling a staticmethod by Vector.static() do not pass Vector class as the first argument.

##### Formatting
format() and str.format() method format each type of objects by calling their `.__format__(spec)` method. 

`spec` is a format specifier used by: `format(obj, spec)` or `"{:spec}".format(obj)` (after a colon in a replacement field {}), Spec should be a string and each class can define its own format code (Format Specification Mini Language) and interprete format code in `__format__` method, as the format in the Vector class example shows.

##### Private and Protected Attributes in python
An attributes with a single `_` prefixing, eg `self._x` does not have special meaning to python interpreter, although it is an convention that these attributes are *private*

An attributes with double `__` prefixing is automatically "mangled": python stores the attributes' name by adding a leading underscore and a class name
```python
class Cls:
    def __init__(self):
        self.__x = "x"
        self._y = "y"
    
cls = Cls()
print(cls.__dict__)
>>> {'_Cls__x': 'x', '_y': 'y'}      # python automatically modified the name
print(cls._y)
>>> "y"
print(cls.__x)
>>> Traceback (most recent call last):
>>>  File "try.py", line 9, in <module>
>>>    print(cls.__x)
>>> AttributeError: 'Cls' object has no attribute '__x'
```
It is suggested to use single underscore, as *single underscore is transparent where double underscore obscures*.

##### The `__slots__` class attribute
*Python store instances attributes in a per-instance dictionary attributes* named `__dict__`, which take space. We can require python to store them in tuple instead, which save space.

To do so, we can create a class attributes `__slots__` and assign it an iterable of str with names for the instance attributes
```python
class Vector2d:
  	__slots__ = ('__x', '__y')
    def __init__(self, x, y):
    	self.__x = x
    	self.__y = y
```

##### Class Attributes can be override
A python class attributes (defined in class, not in `__init__()`) can be used as default values for instance attributes of the same name. They are different from the instance attributes. We can define the attributes for each individual instance:
```python
class Cls:
	att = 1.0                     # class attributes
	def __init__(self):
		self.val = self.att       # instance attributes
```

The difference between class attribute and instance attributes are shown as follows:
```python
v1 = Vector2d(1.1, 2.2)
print(v1.typecode)            # typecode attribute use default value from Vector2d attributes
>>> 'd'
v1.typecode = 'f'
print(v1.typecode)
>>> 'f'
print(Vector2d.typecode)
>>> 'd'
Vector2d.typecode = 'f'       # to change a class attributes, we must set it on class
print(Vector2d.typecode)      # directly, not through an instance, which change the 
>>> 'f'                       # default typecode for all instance
```

##### Slicing as a sequence
*A sequence object in python require just the `__len__` and `__getitem__` methods*. Slicing, len() and in would work properly.

For slicing, an slice object will be passed to the `__getitem__` method. If we want to change the behavior, we can implement the `__getitem__` method to treat slicing specifically by detecting the slice object. Slicing need special treatment because in the case of slicing, `__getitem__` should return a object instead of value.

The following example define a sequence object:
```python
class Vector: 
    typecode = 'd'
    def __init__(self, components):
    	self._components = array(self.typecode, components)
    
    def __len__(self):
    	return len(self._components)
    
    def __getitem__(self, index):        # cls store the classname of itself
    	cls = type(self)
    	if isinstance(index, slice):     # if a slice object is passed, we 
    		return cls(self._components[index])   # slice on the components
    	elif isinstance(index, numbers.Integral): # and return an Vector object build
    		return self._components[index]        # from it.
    	else:
    		msg = '{cls.__name__} indices must be integers' 
    		raise TypeError(msg.format(cls=cls))
```

##### Dynamic Attribute Access and assigment
When an attributes is required, Python first check if the instance contain the attribute named. If not, the search go to class (class attribute) and up to the superclass.

If the given attributes is not found, Python will try to use the `__getattr__` method with argument self and the name of the attribute as string:
- If `__getattr__` is called, Python will create the attributes and then use the return value of this special method as the value of that newly created attributes
- `__setattr__` provide a way to handle attributes setting, here, we use `__setattr__` to prevent assignment of readonly values and dynamicly creately attributes

```python
shortcut_names = 'xyzt'

def __getattr__(self, name): 
	cls = type(self)
	if len(name) == 1:
		pos = cls.shortcut_names.find(name) 
	if 0 <= pos < len(self._components):
		return self._components[pos]
	msg = '{.__name__!r} object has no attribute {!r}' 
	raise AttributeError(msg.format(cls, name))

def __setattr__(self, name, value): 
	cls = type(self)
	if len(name) == 1:
		if name in cls.shortcut_names:
			error = 'readonly attribute {attr_name!r}' 
		elif name.islower():
			error = "can't set attributes 'a' to 'z' in {cls_name!r}" 
		else:
			error = '' 
	if error:
		msg = error.format(cls_name=cls.__name__, attr_name=name)
		raise AttributeError(msg) 
	super().__setattr__(name, value)  # use the __setattr__ from the superclass
```

##### zip()
zip() returns a generator that produce tuples on demand, zip() can take multiply input arguments. zip stops without warning when one of the iterables is exhausted.
```python
for (a, b) in zip(lista, listb)
```