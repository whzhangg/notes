# Fluent Python
Created: October 25, 2021 7:25 PM
Description: This is the reading notes on more advanced tips concerning the python language

**This notes covers the underlying python building blocks with emphasis on the object natural of python data and designing Pythonic objects following the python data model**

Useful references:
1. [[zen of python]]
2. [Python Glossary](https://docs.python.org/3/glossary.html#glossary)

## Chapter 1. The Data Model

**Special Methods**

The consistency of python is achieve by the data model

For example: `len(object)` will return the length, we do not need to call a specific member function. This behavior is called **Pythonic** and is achieved by python's **data model:**

- The data model formalize the interfaces of the objects of the language itself. Such as sequences, iterators etc.
- The python interpreter invokes **special methods** of the object to perform the actual operations. The name of the special methods are always written with leading and trailing double underscores, i.e., `__getitem__`
    
    For example, the index operation `obj[key]` is supported  by the `obj.__getitem__()` special method. Special methods can also be called "**dunder methods**"
    

The following example illustrate using two special methods:

```python
import collection

Card = collections.namedtuple('Card', ['rand','suit'])

class FrenchDeck:
		ranks = [str(n) for n in range(2,11)] + list('JQKA')
		suits = 'spades diamonds clubs hearts'.split()

		def __init__(self):
				self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

		def __len__(self):                           # French behavior like a list
				return len(self._card)

		def __getitem__(self, position):
				return self._cards[position]

>>> deck = FrenchDeck()
>>> len(deck)
52
>>> deck[0]
Card(rank = '2', suit = 'spades')
>>> deck[-1]
Card(rank = 'A', suit = 'hearts')
>>> deck[0:2]
[Card(rank = '2', suit = 'spades'), Card(rank = '3', suit = 'spades')]
>>> from random import choice
>>> choice(deck)
Card(rank = '3', suit = 'clubs')

>>> Card('Q', 'hearts') in deck
True
```

- `namedtuple` construct a simple class with only attributes without custom methods
- with `__len__`, and `__getitem__` defined, the Deck object can be accessed just like a list, can be iterated through and sliced.
- The special methods **should be directly called only by the python interpreter, not by the users**. And most of the time, the special method call is implicit.

**Further Example: Defining a Numeric types**

We have a few other simple special methods:

- `__repr__` method is called to get a **string representation** of the object for inspection. The string returned should be unambiguous and give enough information for re-construction the object being represented.
- `__str__` method convert the object into a **suitable string for printing**, and is called by `str()` method, and implicitly used by the print function.
- `__add__` and `__mul__` overload the operator `+` and `*`. In both case, the method return a new instance of the object without modify either the operand. For example:
    
    ```python
    def __add__(self, other):
    		x = self.x + other.x
    		y = self.y + other.y
    		return Vector(x, y)      # return a new instance
    ```
    
- `__bool__` method convert any object in a boolean context, such as in an if statement, it is also called by `bool()` method, which implicitly perform the conversion.
    
    [ If `__bool__` is not implemented, python tries to invoke `.__len__()` method and return true if length > 0 ]
    

## **Chapter 2. An Array of Sequence**

---

### Overview of Sequences

**Container vs. Flat**

- Container sequences: **hold references** to the objects they contain, and can hold items of different types
- Flat sequences: **store the value** of each item within its own memory space, not as distinct objects

**Mutable vs. Immutable** 

An **Mutable object** can change their values but keep their ids. **Immutable object** cannot be altered and a new object has to be created if a different values has to be stored. 

Immutables include numerical values, strings and tuples. List are mutable objects

```python
>>> a = (1,2,3)
>>> type(a)
<class 'tuple'>

>>> a[0] = 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

>>> sorted(a)
[1, 2, 3]
>>> a.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'sort'
```

- Difference in special methods implemented by immutable sequence and mutable sequences
    
    ![Untitled](Fluent%20Pyt%20773a1/Untitled.png)
    

### List

**List Comprehension**

- List Comprehension (listcomps) is a built-in method to generate a list. For example:
    
                             `ascii = [ ord(s) for s in symbols if ord(s) > 127 ]` 
    
    generate a list with a condition.
    
- List comprehension only works for lists
- Listcomp also support multiply loops, The resulting list is arranged as if the for loops are nested:
    
    ```python
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    
    >>> tshirts
    [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'),
    ('white', 'M'), ('white', 'L')]
    
    # is equivalent to:
    for color in colors:
        for size in sizes:
    			  tshirts.append( (color, size) )
    ```
    

**Generator Expressions**

Generator expression use the syntax as listcomps but are enclosed in parenthesis instead of [ ]. They return a **generator object** that yield values one by one

```python
tuple(ord(symbol) for symbol in symbols)
# generator as a single argument in a function call, duplicating ( ) can be omitted

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
		print(tshirt)
# the whole ( ) after in is a generator expression, different from list
```

### Tuple

**Using tuples**

- Tuples hold data in sequence and the position of these items gives its meaning.
- Tuple is **immutable**: we cannot add or remove elements.

```python
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# the sequence determine the meaning of the data

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for country, _ in traveler_ids:    # unpack a tuple
		print(country)                 # a dummy variable "_" is used for the second item
>>> USA
>>> BRA
>>> ESP
```

**Unpacking**

Tuple can be **unpacked** by its shape (**parallel assignment).** list can also be unpacked, but tuples are more suitable

```python
tokyo = ('Tokyo','JP',36.933,(35.689722,139.691667))    # nested tuple unpacking
metro_areas = [ tokyo, ... ]
for name, cc, pop, (latitude, longitude) in metro_areas:
		print(name, latitude, longitude)

(b, a) = (a, b)    # parallel assignment
```

Unpacking with `*`

We can use **`* prefix`** to exactly one variable in the parallel assignment and it can appear in any position. It will match and include all the remaining items

```python
a, *body, c, d = range(5)
>>> a, body, c, d
(0, [1, 2], 3, 4)
```

**Named Tuples**

collections.namedtuple function **produce a subclass of tuple** with field names and class name

- To construct the instance, data must be passed as positional arguments to the constructor
- Data can be accessed by name or position

it support a few additional methods: `_fields` attributes, `_make(iterable)` class method (make a instance from an iterable) and `_asdict()` method which return a dictionary

```python
>>> from collections import namedtuple
>>> City = namedtuple('City', 'name country population coordinates')
>>> tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

>>> tokyo.coordinates
(35.689722, 139.691667)
>>> tokyo[1]
'JP'

>>> delhi._asdict()
OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population', 21.935), 
						 ('coordinates', LatLong(lat=28.613889, long=77.208889))])
```

### Methods for sequences

**Slicing**

slicing is a general method supported by iterables. 

```python
s = 'bicycle'
s[::-1]          # reverse with stride
>>> 'elcycib'

# slicing with slice object
#       0.....6.................................40........52...55........
line = "1909  Pimoroni PiBrella                    $17.50   4      $52.50"

Desription = slice(6,40)
line[Description]
>>> "Pimoroni PiBrella                 "
```

- slicing with `s[a:b:c]` specifies a stride or step size c, stride can be negative, giving reversed result. This method is only valid within `[ ]` operator
- We can also create a slice object: `slice(a,b,c)` [https://docs.python.org/3/c-api/slice.html](https://docs.python.org/3/c-api/slice.html), which can be used to define a specific slice on data, as the previous example shown.
- Slice use `__getitem__` and `__setitem__` special methods that handle `[ ]` operator
- We can also use ellipsis `...` as a short cut for "as many as `:, :, :` in slicing. `...` is a alias to an ellipsis object which is passed as parameters

**Inplace addition**

operator `+=` and `*=` modify the left size of the assignment, for example: `a += b`

- For `+=`, python will attempt to call `__iadd__` ( in place addition ). If it is not implemented, python will then call `__add__`.
- With `__iadd__` method, any change will happen in place, but if `__add__` is used, a += b will have the same effect as `a = a + b` and assign a to a new object ( the instance will be a different one)
- In general, for mutable sequence, `__iadd__` would be implemented, while for immutable sequence, it it not.

For `*=`, the equivalence is `__imul__`

**list sorting**

- `list.sort()` method sorts a list in place, which return None ( Return None is convention if the functions or methods change the object itself). Since it is a inplace method, immutable object do not support it
- `sorted()` method creates a new list and returns it

Both method take two optional arguments:

1. **reverse [= False]**: specify if the order is reversed
2. **key**: a one-argument function passed as parameter giving a value for each item to sort

```python
fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)
>>> ['apple', 'banana', 'grape', 'raspberry']

sorted(fruits, key=len, reverse=True) 
>>> ['raspberry', 'banana', 'grape', 'apple']
# which we short by len(item) in reverse order, len() is the name of the function

l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19] 
sorted(l, key=int)
>>> [0, '1', 5, 6, '9', 14, 19, '23', 28, '28']
# we use key to perform type conversion

# if we want to sort list of dictionary, we can use
sorted(elements, key=itemgetter("count"), reverse=True) ]
# from operator import itemgetter
```

**Inserting element in order**

`bisect` package provide function `bisect` and `insort` that perform binary search for an ordered list. [https://docs.python.org/3/library/bisect.html](https://docs.python.org/3/library/bisect.html)

- `bisect(seq, item)` take a sorted list and an element and return the index which would be the position of that element when it is inserted to the sorted list [ biset_right() and biset_left() determined different behavior in the case of equal value ]
- `insort(seq, item)` insert the item into the sequence directly

```python
import bisect
# use biset to determin the range
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
		i = bisect.bisect(breakpoints, score)
		return grades[i]

[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]] 
>>> ['F', 'A', 'C', 'C', 'B', 'A', 'A']

my_list = []
for i in range(SIZE):
		new_item = random.randrange(SIZE*2) 
		bisect.insort(my_list, new_item)
# create an ordered random list
```

### Other types of sequences

**Arrays**

Array is a more efficient iterable than a list (flat). it include all mutable sequence operation (pop, insert, extend) and additional methods for fast loading and saving (`.fromfile()`, `.tofile()`)

array directly store the object, so creating an array require a typecode to determine the type of object. For example 'd' refer to double

For more on arrays, see [https://docs.python.org/3/library/array.html](https://docs.python.org/3/library/array.html)

**Memory View**

Memory view is a shared-memory sequence type that allow data to be used by different data-structure without copying(such as bits and integer)

For more, see [https://docs.python.org/3/c-api/memoryview.html](https://docs.python.org/3/c-api/memoryview.html)

**Deques** 

collections.deque has the following features compare to a list, although they support similar method (.append, .pop)

1. inserting and removing items from both end is very efficient
2. The append and popleft operations are atomic, thus is safe to use when being accessed multithreading
3. maxlen parameter will bound the deque to a certain size (dropping items from the opposite end when full)
    
    ```python
    from collections import deque
    dq = deque(range(10), maxlen=10)
    print(dq)
    >>> deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
    
    dq.appendleft(-1)
    >>> deque([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], maxlen=10)
    ```
    

For more, see [https://docs.python.org/3/library/collections.html#collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)

## Chapter 3. Dictionaries and Sets

---

python dictionaries are highly optimized. The mapping type in python are mutable

- Class diagram of Mapping types
    
    ![Screen Shot 2021-10-29 at 00.16.13.png](Fluent%20Pyt%20773a1/Screen_Shot_2021-10-29_at_00.16.13.png)
    

### Hashable

An object is hashable if it has a hash value `hash()` ( from `__hash__()` method ), which is unique and comparable by `__eq__()` method. 

- Most of the python (atomic) immutable build-in objects are hashable

## Dictionary

**Dictionary comprehensions**

A dictcomp builds a dictionary instance by producing `{key:value}` pair from iterable

```python
>>> DIAL_CODES = [
... (86, 'China'),
... (91, 'India'),
... (1, 'United States'),
... (62, 'Indonesia'),
... (55, 'Brazil'),
... (92, 'Pakistan')
... ]
>>> country_code = {country: code for code, country in DIAL_CODES}

# which build a dictionary with country as key and code as values
```

**Missing keys with setdefault()**

There are several methods to get default value from a dictionary

1. `dict.get(key, default)` is a method to obtain values with an default values, however, **it does not give this default value to key if the key does not exist**
2. `dict.setdefault(key, default)`: if key in dict, return dict[key], otherwise, set dict[key] = default and return it
3. `defaultdict`: we can **instantiate a defaultdict by provide a callable** that will produce a default value as default value, whenever `__getitem__()` is passed a non-existent key (similar to an implicit `getdefault()` method)
    
    ```python
    from collections import defaultdict
    
    index = defaultdict(list)
    index[word].append(location)
    # if word not in index, defaultdict create a list as value to the key
    ```
    

**Variations of dictionary**

- collections.OrderedDict
    
    Note: from python 3.7, the build in dict class is able to remember insertion order [ [ref](https://docs.python.org/3/library/collections.html#collections.OrderedDict) ]
    
    the keys in ordered dict will be maintained in insertion order, ensuring iteration over items in a certain order. `popitem()` method can pop the first item (`popitem(last = True)` pop the last item)
    
- Counter
    
    Counter accept a multiset and count the instances of hashable objects. It provide some method related to counting.
    
    ```python
    ct = collections.Counter('abracadabra')
    print(ct)
    >>> Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}) 
    ct.update('aaaaazzz')
    print(ct)
    >>> Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1}) 
    print(ct.most_common(2))
    >>> [('a', 10), ('z', 3)]
    
    # it also implemented "+" and "-" operators to combine counters
    ```
    

### Set

- set type implement the essential set operations
    
    ```python
    a |  b   # return union of a and b
    a |= b   # update a with union of a and b 
    a &  b   # return intersection of a and b
    a &= b   # update a with intersection of a and b
    a -  b   # return a substract b
    a -= b   # update a by substracting b from a
    
    e in b   # element e is in set b
    a <  b   # a is a proper subset of b
    a <= b   # a is a subset of b
    a >  b   # a is a proper superset of b
    a >= b   # a is a superset of b
    ```
    
- Using set operation, some operation become straight forward, For example:
    
    `found = len( set(smaller_set) & set(larger_set) )`
    
- Class diagram of set
    
    ![Screen Shot 2021-10-29 at 00.44.19.png](Fluent%20Pyt%20773a1/Screen_Shot_2021-10-29_at_00.44.19.png)
    

### Mechanism of fast searching for dict and set (hash)

- Speed of set operation
    
    ![Screen Shot 2021-10-29 at 00.45.56.png](Fluent%20Pyt%20773a1/Screen_Shot_2021-10-29_at_00.45.56.png)
    

**Hash table method** 

[https://en.wikipedia.org/wiki/Hash_table](https://en.wikipedia.org/wiki/Hash_table)

Dictionary and set use a **hash table** to implement searching

- A hash table is a sparse array that is mostly empty. Each datapoint in the sparse array "buckets" contains two fields: a reference to the key and a reference to the value of the item ( in terms of set, it only keep a single reference to the key )
- For each key, the dictionary calculate the hash value (`hash()` function)
- To find a value of a key, python first obtain the hash value and use the least significant bits (first bits) of that number to find the position of the point in the sparse array.
- If the founded position is empty, keyerror is raised. If the key of founded point in the sparse array but does not match the input key, a hash collision happens. In such case, python check the next bits in the hash value and use the result to look up again a point in the sparse array, until the keys match. Then the item value is returned.
- Python will automatically manage the sparseness of the hash table, so that the size in memory of mapping object is dynamic

![Screen Shot 2021-10-29 at 00.58.24.png](Fluent%20Pyt%20773a1/Screen_Shot_2021-10-29_at_00.58.24.png)

For a sparse hash table, most search happen with no collisions, and average number of collision is very few ( one or two )

### **Consequences of hashing for mapping types**

1. keys must be hashable objects
2. dictionarys and sets have large memory overhead
3. key search is very fast with a sparse array
4. key ordering will depends on insertion order, and adding items to a dict or set may change the key order, since python will rebuild the hashtable when the size grow.

## Chapter 4. Text vs. Byte

---

**String and encoding**

- `str` in Python 3 store Unicode characters
- A **character** is defined by its code point according to the unicode standard U+Num, where num is a 4 - 6 hexadecimal digits reranging from 0 to 1114111. For example, the letter A has a Unicode U+0041 (hexadecimal)
    
    ![Screen Shot 2021-11-01 at 23.52.27.png](Fluent%20Pyt%20773a1/Screen_Shot_2021-11-01_at_23.52.27.png)
    
- The **actual bytes** that represent a character, however, depend on the encoding used. Encoding converts the code pointed into actual byte that represent characters (in a text documents). 'uft-8' is the most common encoding method

In short, a character can have different byte representations. We can **create bytes by encoding a string**, similarly, we can decode a bytes object to recover the string As an example, we can encode str:

```python
for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t') 

>>> latin_1 b'El Ni\xf1o'
>>> utf_8   b'El Ni\xc3\xb1o'
>>> utf_16  b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'

#To recover string from bytes
b.decode('utf_8')
```

**Detecting the encoding of a Byte Sequence**

It is not possible to tell apart what coding is used to parse the bytes in a text file. In some protocols or file formats, text file contain **header information** on how the content is encoded. 

For a string of plain text without encoding information, we can usually only gauss, for example, using statistics. Python package **Chardet** provide such utility to identify encoding. It also provide a command line tool:

```bash
which chardetect
>>> /Users/wenhao/myapp/miniconda3/envs/pymat/bin/chardetect

chardetect make.sh
>>> make.sh: ascii with confidence 1.0
```

### **Handling Text files**

The best practice of handling text files is to handle text exclusively on str objects. 

Python's file reading and writing perform necessary decoding and encoding. **However, we should take care to use the same encoding for writting and reading file.** 

```python
>>> open('cafe.txt', 'w', encoding='utf_8').write('café') 4
>>> open('cafe.txt').read()
'cafÃ©'
```

If no encoding arguments are specific, read() and write() use default encoding that vary across systems. **We should not rely on default encoding**

Use `open(filename, 'w', encoding = 'utf_8')`

- **Points touched in the book but not included here in this note:**
    - String normalization for comparsion (Unicode provide different ways to represent the same characters, See page 117)
    - Sorting unicode with non-ASCII characters
    - str vs. bytes in functions and regular expressions
    

## Chapter 5 - 7. Functions as Objects

---

### Overview

**Functions in Python are objects themselves**, further more, they are **first class objects**

- A first class object is an entity that can be dynamically created, destroyed, passed to a function, returned as a value, and have all the rights as other variables in the programming language have.
- Higher order functions are functions that take a function as argument or return a function,
    
    `sorted(a, key = len)` 
    
    is a higher order function, that take an one argument function len() to sort the `a`
    
- Anonymous Functions
    
    lambda keyword creates an anonymous function (a function with no name)
    
    `sorted(fruits, key=lambda word: word[::-1])` which take an argument `word` and return `work[::-1]`
    
    We can also use lambda to define simple functions
    
    `last = lambda word: word[::-1]` which can be called by `last()`
    

**Callable types in Python**

1. User-defined functions & Build-in functions
2. Methods & Build-in methods
3. Generator functions
4. Classes: in python calling a class (create an instance) is like calling a function
5. Class instances: if a class defines a __call__ method, then its instnace is callable 

**User defined Callable**

A class implementing `__call__` is an easy way to create **function-like objects that have internal state**

```python
class BingoCage:
		def __init__(self, items): 
				self._items = list(items) 
				random.shuffle(self._items)

		def pick(self): 
				try:
						return self._items.pop() 
				except IndexError:
						raise LookupError('pick from empty BingoCage') 
		
		def __call__(self):
				return self.pick()

bingo = BingoCage(range(3))
bingo()
>>> 0
callable(bingo)
>>> True
```

### Positional arguments to keyword only arguments

Consider the following parameter list:

`def tag(name, *content, cls=None, **attrs):`

- name is a **normal positional argument**
- *content capture any number of arguments after the first (name), as **tuple**
- cls is a **keyword argument** that can only be passed by giving `cls = " "`
- **attrs capture all arguments that are given by keyword but not in the argument list, **as dict**
- **Prefixing a dictionary with **** and pass it as argument **will pass all its items as separate named arguments** (reverse of the above step)

Example:

```python
def tag(name, *content, cls=None, **attrs): 
		"""Generate one or more HTML tags""" 
		if cls is not None:
				attrs['class'] = cls 
		
		if attrs:
				attr_str = ''.join(' %s="%s"' % (attr, value) 
											for attr, value in sorted(attrs.items()))
		else:
				attr_str = ''
		if content:
				return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content) 
		else
				return '<%s%s />' % (name, attr_str)
```

**Keyword only argument**

Keyword only argument are not positional argument, To specify a keyword only argument, we need to put them after argument prefixed with *, [ if we do not need argument prefixed with *, we can put a * by it self ]

Compare  `def f(a, b = None)` and `def f(a, *, b = None)`

In the first case, b is a positional argument with default value, but in the second case of keyword only argument, b can only be passed if we use keyword b = "" specifically.

Keyword only argument do not need to have a default value, they can be mandatory

### **Function inspection**

Function objects have many attributes 

- __doc__ attributes generate the help text of an object
    
    ```python
    def factorial(n):
        '''returns n!'''
        return 1 if n < 2 else n * factorial(n-1)
    
    factorial.__doc__
    >>> 'returns n!'
    ```
    
- __defaults__ attributes store default value for formal parameters
- __annotations__ attributes store the metadata related to the parameters of a function declaration
    
    `def clip(text:str, max_len:'int > 0'=80) -> str:`
    
    define a function with annotations. They are preceded by : for the arguments and -> for the return values. The expression can be of any types, most commonly class names, or strings
    
    They are stored in __annotations__ but is `not processed by python at all`.
    
    ```python
    clip.__annotations__
    >> {'text': <class 'str'>, 'max_len': 'int > 0', 'return': <class 'str'>}
    ```
    

**Modules inspection**

Modules in Python are also first-class objects, and the standard library provides several functions to handle modules, just as they provide tools to handle functions.

- `globals()` return a dictionary representing the current global symbol table.
- `locals()` return a dictionary representing local symbols
    
    ```python
    import math
    globals()
    >>> {'__name__': '__main__', '__doc__': None, '__package__': None, 
    		 '__loader__': <class '_frozen_importlib.BuiltinImporter'>, 
    		 '__spec__': None, '__annotations__': {}, 
    		 '__builtins__': <module 'builtins' (built-in)>, 
         'math': <module 'math' from '/Users/wenhao/myapp/miniconda3/envs/ML/lib/python3.8/lib-dynload/math.cpython-38-darwin.so'>
    		}
    ```
    

### **Support for functional Programming**

Operator Module provides a few tools that can replace simple oneline functions:

**itemgetter()**

- `itemgetter` **returns a function** that, given a sequence, returns the item at an index. If several index are passed, it will return tuples with the extracted values.
- `itemgetter(1)` is thus the same as `lambda fields: fields[1]`
- Since itemgetter use [ ], it can also be used on mappings
    
    ```python
    from operator import itemgetter
    metro_data = [
    		('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
    ]
    
    for city in sorted(metro_data, key=itemgetter(1)):
        print(city)
    >>> ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)) 
    >>> ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
    ```
    

**attrgetter()**

- attrgetter is similar to itemgetter but receive attribute name and return the attributes of the given objecs.
- methodcaller will create a function that call a method of the object by the name given by the arguments
    
    ```python
    s = "hello world"
    upcase = methodcaller('upper')
    upcase(s)
    >>> "HELLO WORLD"
    ```
    

**Functools.Partial methods**

- given a function, a partial application produce a new callable with some of its arguments of the original function fixed.
- Partial takes a callable as first argument, followed by an arbitrary number of positional and keyword arguments to bind.
    
    ```python
    from functools import partial
    triple = partial(mul, 3)
    triple(7)
    >>> 21
    ```
    

### Function Decorators and Closures

**Decorators** 

- A **Decorator is a callable** that takes another function as argument and return another function
- Decorators are **executed immediately when a module is loaded** (import time), the decorated functions runs only when they are invoked (run time)

```python
def deco(func):
		"""we define a decorator that return a function, in this case
		it does not use the original function
		"""
		def inner():
				print('running inner()')
		return inner

@deco
def target():
		print('running target()')
# this is the same as target = deco(target)

target()
>>> running inner()
```

**Stacked Decorators**

When two decorators @d1 and @d2 are applied to a function f, as in:

```python
@d1
@d2
def f():
		print('f')
```

The result is the same as `f = d1(d2(f))`

**Example 1: Using decorator to track functions**

Using the fact that decoration are executed when the module is loaded, here show an example to use decorators to keep track of functions defined

Any function decorated with `@promotion` will be added to list `promos`

```python
promos = []
def promotion(promo_func):      # a function to be used as decorato
		promos.append(promo_func) 
		return promo_func
		
@promotion
def fidelity(order):
		"""5% discount for customers with 1000 or more fidelity points"""
		return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
		"""10% discount for each LineItem with 20 or more units""" discount = 0
		for item in order.cart:
				if item.quantity >= 20:
						discount += item.total() * .1
		return discount
```

**Example 2: Using decorator to time functions**

```python
import time
import functools

def clock(func): 
		@functools.wraps(func)   # a decorator that copy origin the doc or annotation to the decorated function
		def clocked(*args, **kwargs):
				t0 = time.time()
				result = func(*args, **kwargs) 
				elapsed = time.time() - t0 
				name = func.__name__
				arg_lst = []
				if args:
						arg_lst.append(', '.join(repr(arg) for arg in args)) 
				if kwargs:
						pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
						arg_lst.append(', '.join(pairs))
				arg_str = ', '.join(arg_lst)
				print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result)) 
				return result
		return clocked

@clock
def snooze(seconds): 
		time.sleep(seconds)

snooze(2.0)
>>> "[2.0000s] snooze(2.0) -> None"
```

**Parameterized Decorators**

Python only take the decorated function and pass it as argument to the decorator function. 

- To make a decorator that can accept a parameter, we **define a function that take arguments and return a decorator,** For example
    
    ```python
    registry = set()
    
    def register(active=True): 
    		def decorate(func):
    				print('running register(active=%s)->decorate(%s)' % (active, func))
    				if active: 
    						registry.add(func)
    				else: 
    						registry.discard(func)
    				return func 
    		return decorate         # return a decorator
    
    @register(active=False)     # using the returned decorator
    def f1():
    		print('running f1()')
    
    @register()      # if no parameters are passed
    def f2():        # register must still be called as function!
    		print('running f2()') 
    
    def f3():
    		print('running f3()')
    f3 = register()(f3)   # f3 = register(active=False)(f3)
    ```
    

**Decorator in standard library**

Python has three standard decorate methods: **@property**, **@classmethod** and **@staticmethod**

In functools, there are other decorators, we show two of them:

**lru_cache**

- functools.lru_cache decorator that will **save the result of the previous invocation and return the result directory if the inputs are the same**.
- It accept two parameters: `functools.lru_cache(maxsize=128, typed=False)`
    
    maxsize determine how many previous call to store, typed will check if the input type as well as input values ( if 1.0 and int(1) is the same )
    
    ```python
    @functools.lru_cache() # the repeated calls will not be executed again
    @clock #
    def fibonacci(n):
    		ifn<2: 
    				return n
    		return fibonacci(n-2) + fibonacci(n-1)
    ```
    

**Single Dispatch**

- In python, it is not possible to overload functions, we cannot therefore create variations of function with different result for different input ( we can implement if elif structure, but they are not easy to maintain)
- @singledispatch can decorate a plain function to be a generic function, as the example shows:
    
    ```python
    from functools import singledispatch 
    from collections import abc
    import numbers
    import html
    
    @singledispatch
    def htmlize(obj):
    		content = html.escape(repr(obj)) 
    		return '<pre>{}</pre>'.format(content)
    
    @htmlize.register(str) 
    def _(text):
    		content = html.escape(text).replace('\n', '<br>\n') 
    		return '<p>{0}</p>'.format(content)
    
    @htmlize.register(tuple) 
    @htmlize.register(abc.MutableSequence) 
    def _(seq):
    		inner = '</li>\n<li>'.join(htmlize(item) for item in seq) 
    		return '<ul>\n<li>' + inner + '</li>\n</ul>'
    ```
    
- singledispatch decorate a base function that handles a abstract type
- each specialized function is decorated by `@basefunction.register(type)`. The name of the specialized function does not matter
- Several register decorators can be stacked together
- When possible, use boarder class, such as `abs.MutableSequence`, instead of `list`

## Chapter 8. Object References, Mutability

---

**Summary of practical consequences of referencing**

- simple assignment create aliases
- augment assignment with += or *= may create new objects to bound to left hand side or modify the left size in place, depending on the mutability and implementation
- rebinding a new value to an existing variable does not change the object previously bound to it
- function **parameters are passed as aliases**
- using mutable object as default values for function parameters is dangerous

**Variable names as labels**

Python variables are like refernce, they are labels attached to objects

In an assignment `a = b`, Python retrieve or create object on the right of the assignment, and **then** bound the left variable name to the object.

Identity, Equality and Alias:

Every python object has **an identity**, **a type** and **a value**. An object's identity (`id()`) never changes once it has been created (memory in the address)

- `==` compare the object's value, using their `__eq__` implementation (therefore, == operator can be override by class implementation and behavior differently)
- `is` compare the itentity of the python object, it compare the object ID and cannot be overloaded.

**Relative Immutability** 

Tuple is an immutable but can hold references to the objects that are mutable. The immutability of tuples refer to the immutability of physical contents of tuple datastructure (eg, number of elements), but does not extend to the refered objects.

**Copies**

- **Aliasing**: `a = b` creates an alias.
    
    ```python
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    lewis = charles
    lewis == charles
    >>> True
    id(charles), id(lewis)
    >>> (4300473992, 4300473992).  # memory address
    ```
    
- **Shallow Copy**: shallow copy duplicate the outermost container, but copy is filled with reference to the same items held by the original container.
    
    ```python
    l1 = [3, [66, 55, 44], (7, 8, 9)] 
    l2 = list(l1)       # using constructor create a shallow copy
    l1 == l2
    >>> True
    l1 is l2
    >>> False
    
    l1.append(100) 
    l1[1].remove(55) 
    print('l1:', l1)
    print('l2:', l2)    # l2 is a shallow copy
    >>> l1: [3, [66, 44], (7, 8, 9), 100]
    >>> l2: [3, [66, 44], (7, 8, 9)]
    l2[1] += [33, 22]  
    l2[2] += (10, 11)   # ! += on tuple creates a new tuple and rebinds l2[2] to the new tuple 
    print('l1:', l1) 
    print('l2:', l2)
    >>> l1: [3, [66, 44, 33, 22], (7, 8, 9), 100]
    >>> l2: [3, [66, 44, 33, 22], (7, 8, 9, 10, 11)]
    ```
    
    `copy.copy()` return a shallow copy
    
- **Deep Copy**: deep copied objects do not copy embedded objects
    
    `copy.deepcopy()` return a deep copy
    

the behavior of copy and deepcopy can be controlled by implementing `__copy__()` and `__deepcopy__()` special methods.   

**Function parameters**

- the only way parameter passed in python is **sharing**, the parameters inside the function become aliases of the actual arguments. Therefore, **function can change mutable object passed as parameters, but cannot change their identity**
    
    ```python
    # consider the following example
    def f(a, b):
        a+=b
        return a
    
    x=1, y=2 
    f(x, y) 
    >>> 3
    x,y
    >>> (1, 2) 
    
    a=[1,2], b=[3,4] 
    f(a, b) 
    >>> [1, 2, 3, 4] 
    a,b
    >>> ([1, 2, 3, 4], [3, 4]) 
    
    t=(10,20)                     # tuples 
    u=(30,40)                     # for tuples, since they are immutable, 
    f(t, u)                       # a += b is not inplace, and is equivalent to a = a + b
    >>> (10, 20, 30, 40)          # which create a new tuple and associate it to
    t,u                           # the local variable of the function "a"
    >>> ((10, 20), (30, 40))      # therefore, the input is not changed
    ```
    

- Mutable types **should not be used** as parameter defaults
    
    if we define a class
    
    ```python
    class Bus:
    		"""A bus model haunted by ghost passengers"""
    		def __init__(self, passengers=[]):
    				self.passengers = passengers
    
    bus1 = Bus()
    bus1.passengers.append('Ben')
    bus1.passengers.append('Alice')
    print(Bus.__init__.__defaults__)
    >>> (['Ben', 'Alice'],)               # the default parameters are modified
    bus2 = Bus()
    print(bus2.passengers)
    >>> ['Ben', 'Alice']
    ```
    
    The default empty list is evaluated when the function is defined at import time. The default value become attributes of the function object, stored in memory with the function. So if the default value is mutable and is changed, this change will affect every future call of the function
    
- Defending against mutable parameters
    
    When passing mutable objects as parameter, we should think twice, **when in doubt, always make a copy**
    

**`Del()`, Garbage Collection and Weak Reference**

- `del()` statement deletes the name explicitly, not the object. An object is **garbaged** (deleted) only if all the variables holding reference to it are deleted or the object become unreachable.
- Python keep track of the reference by reference counting (like smart pointer in c)
- a class can define its behavior of del statement  by implementing __del__ special method, which is invoked by python to execute some code before the object is destroyed. "You will seldom need to implement __del__ in your own code for no good reason"

**Weak References**

- **Weak References**: a weak reference to an object do not increase its reference count, an instance of weak reference can be called to return the object it's refering to, and return None if the object is destoryed.
    
    ```python
    # using weak reference
    import weakref
    a_set = {0, 1}
    wref = weakref.ref(a_set)
    print(wref())
    >>> {0, 1}
    ```
    
- **WeakValueDictionary**: a weakvalue dictionary implements a mutable mapping where the values are weak references to objects, when a referred object is destoried, the corresponding key is automatically removed from the dictionary. It is commonly used for caching.
    
    ```python
    import weakref
    weakdict = weakref.WeakValueDictionary()
    ```
    

## Chapter 9 ~ 10. A Pythonic Object

---

**checking the names defined in an object**

dir() return the list of attributes of the object, if it is called without argument, it return the names in the current scope

- `dir(int)`
    
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
    

**Duck typing**

"If it walks like a duck and it quacks like a duck, then it must be a duck" 

→ what an object can do (with their implementation of specific methods) make an object what they are.

**Special methods of a pythonic object**

- `__new__` creates the object, this is done before `__init__`. [Ref](https://python.ms/new/#_2-new-は、いつ使うの)
- `__repr__` used by repr() to return a string representing the object as **developers** wants to see it
- `__str__` used by str() to return a string representing the object as **users** wants to see it
- `__iter__` make the object iterable, which can support, for example, unpacking and convert it to other iterable
- `__eq__` value comparsion accessed by == operator
- `__bool__`  determines how the object is converted to bool value, when a bool value is needed
- `__bytes__` used by byte() to convert the object to bytes
- `__format__` used by format() function to format display
- `__hash__` make the object hashable with hash(), The object need to be immutable
- `__int__` convert objects to int value with int(), similar, we have __float__ method
- `__len__` return the length of an object
- `__getitem__` return an item given a position as parameter
- **Example** A Pythonic vector class implementing these methods
    
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
    				return (bytes([ord(self.typecode)]) +
    								bytes(array(self.typecode, self))) 
    
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
    						coords = (abs(self), self.angle())   # p print the vector in polar coordinates
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
    

**Classmethod**

- @classmethod define a method that operates on class and not on instance:
    
    `Vector.frombyte()` (on class) instand of `vector1.frombyte()` (on instance)
    
- The first argument passed to a classmethod is the class itself (Vector.frombyte(), Vector is passed as the first argument). By convention, the first parameter of a class method should be named cls, (just a naming convention)
- Classmethod usually return an instance of the class

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

By contrast, **@staticmethod** decorates a method to be just like a plain function that live in a class body. Calling a staticmethod by Vector.static() do not pass Vector class as the first argument.

**Formatting** 

format() and str.format() method format each type of objects by calling their .__format__(spec) method. 

- spec is a format specifier used by: `format(obj, spec)` or `"{:spec}".format(obj)` (after a colon in a replacement field {})
- spec should be a string and each class can define its own format code (Format Specification Mini Language) and interprete format code in __forma__ method, as the format in the Vector class example shows.

**Private and Protected Attributes in python**

- an attributes with a single _ prefixing, eg self._x does not have special meaning to python interpreter, although it is an convention that these attributes are private
- an attributes with double __ prefixing is automatically "mangled": python stores the attributes' name by adding a leading underscore and a class name
    
    ```python
    class Cls:
        def __init__(self):
            self.__x = "x"
            self._y = "y"
    
    cls = Cls()
    print(cls.__dict__)
    >>> {'_Cls__x': 'x', '_y': 'y'}          # python automatically modified the name
    print(cls._y)
    >>> "y"
    print(cls.__x)
    >>> Traceback (most recent call last):
    >>>  File "try.py", line 9, in <module>
    >>>    print(cls.__x)
    >>> AttributeError: 'Cls' object has no attribute '__x'
    ```
    
- It is suggested to use single underscore, as ***single underscore is transparent where double underscore obscures***

**The "__slots__" class attribute**

- Python store instances attributes in a **per-instance dictionary attributes** named __dict__, which take space. We can require python to store them in tuple instead, which save space.
- To do so, we can create a class attributes __slots__ and assign it an iterable of str with names for the instance attributes
    
    ```python
    class Vector2d:
    		__slots__ = ('__x', '__y')
    		def __init__(self, x, y):
    				self.__x = x
    				self.__y = y
    ```
    

**Class Attributes can be override**

A python class attributes (defined in class, not in __init__()) can be used as default values for instance attributes of the same name. They are different from the instance attributes. We can define the attributes for each individual instance

```python
class Cls:
		att = 1.0                     # class attributes
		def __init__(self):
				self.val = self.att       
				# self.att is an instance attributes that default to class attributes
```

Which is shown through the next example:

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

**Slicing as a sequence**

- a sequence object in python require just the __len__ and __getitem__ methods. Slicing, len() and in would work properly.
- For slicing, an slice object will be passed to the __getitem__ method. If we want to change the behavior, we can implement the __getitem__ method to treat slicing specifically by detecting the slice object
- In the case of slicing, __getitem__ should return a object instead of value
- The following example define a sequence object:
    
    ```python
    class Vector: 
    		typecode = 'd'
    		def __init__(self, components):
    				self._components = array(self.typecode, components)
    
    		def __len__(self):
    				return len(self._components)
    
    		def __getitem__(self, index):                   # cls store the classname of itself
    				cls = type(self)
    				if isinstance(index, slice):                # if a slice object is passed, we 
    						return cls(self._components[index])     # perform the slice on the components
    				elif isinstance(index, numbers.Integral):   # and return an Vector object build
    						return self._components[index]          # from it.
    				else:
    						msg = '{cls.__name__} indices must be integers' 
    						raise TypeError(msg.format(cls=cls))
    ```
    

**Dynamic Attribute Access and assigment**

- When an attributes is required, Python first check if the instance contain the attribute named. If not, the search go to class and up to the superclass.
- If the given attributes is not found, Python will try to use the __getattr__ method with argument self and the name of the attribute as string
- If __getattr__ is called, Python will create the attributes and then use the return value of this special method as the value of that newly created attributes
- __setattr__ provide a way to handle attributes setting, here, we use __setattr__ to prevent assignment of readonly values and dynamicly creately attributes

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
		super().__setattr__(name, value)     # use the __setattr__ from the superclass for 
																				 # standard behavior
```

**zip()**

- zip() returns a generator that produce tuples on demand, zip() can take multiply input arguments
- zip stops without warning when one of the iterables is exhausted.
- 

## Chapter 11 Interfaces, Protocols and ABCs

---

**Protocols in python is informal**

**abstract base class** (ABC) make interfaces explicit and verify the implementations for conformance

An interface is the object's public methods that enable it to play its role.

**Python cooperate with essential protocols as much as possible**

Python usually try to work with even the simplest implementation. 

- A sequence interface defined in ABC require the following method: __getitem__, __contains__, __iter__ and __reversed__ special methods.
- However, the following example shows that with only the implementation of __getitem__, python still perform the sequence operation correctly:
    
    ```python
    class Foo:
    		def __getitem__(self, pos): 
    				return range(0, 30, 10)[pos]
    
    f[1]
    >>> 10
    20 in f                 # in operature use getitem to check all the elements, 
    >>> True                # when __contains__ is not found
    for i in f: print(i)    # similarly, we can still iterate the object when 
    >>> 0 10 20             # python use getitem method and start calling it with indexes
    ```
    

**ABCs** 

- ABC present a different idea from the previous duck typing. ABC require its "concrete" class (as contrast to abstract class) to implement abstract methods.
- Python will check for the implementation of abstract method not at import time, but only at runtime when we instantiate an instance. If we fail to implement any abstract method, interpreter will raise error

**collections.abc**

In collections module, the following abcs are implemented.

![Screen Shot 2021-11-07 at 20.33.18.png](Fluent%20Pyt%20773a1/Screen_Shot_2021-11-07_at_20.33.18.png)

- most of the classes Iterable(__iter__), Container(__contains__) and sized (__len__). The classes that are lower at the bottom require to implementation the abstract methods defined in the previous class. For example, A sequence  (__getitem__, __contains__, __iter__ and __reversed__ ) contain the abstract method of iterable, container and sized.
- Sequence, Mapping and Set are the main immutable collection, each has a mutable subclass.
- To inherit from a particular abc, use:
    
    ```python
    import collections
    class FrenchDeck(collections.MutableSequence):
    ```
    

### **Defining an ABC**

to define for an abstract base class for our purpose, we inherit abc.ABC (module abc). 

- As a abstract class, we can define **abstract methods** and **concrete methods**.
- abstract methods has to be defined by the following implementation
- Concrete methods in an ABC are those that does not depend on the actual implementation. Furthermore, for concrete methods, we only need to pursue "correctness": we can expect the actual subclass implementation to overwrite it for optimization and efficiency.

As an example, we consider an abstract class that pick items at random

```python
import abc
class Tombola(abc.ABC):               # To define an abc, subclass abc.ABC
		@abc.abstractmethod
		def load(self, iterable):
				"""Add items from an iterable."""

		@abc.abstractmethod               # for abstract methods, function body can be empty
		def pick(self):
				"""Remove item at random, returning it"
					 This method should raise `LookupError` when the instance is empty. """

		def loaded(self):
				"""Return `True` if there's at least 1 item, `False` otherwise.""" 
				return bool(self.inspect())

		def inspect(self):
				"""Return a sorted tuple with the items currently inside.""" 
				items = []
				while True:
						try: 
								items.append(self.pick())     # concrete method should only rely
						except LookupError:               # on interfaces defined by ABC 
								break
				self.load(items)
				return tuple(sorted(items))
```

- Abstract class method: we can use compound decoration:
    
    ```python
    class MyABC(abc.ABC): 
    		@classmethod
    		@abc.abstractmethod
    		def an_abstract_classmethod(cls, ...):
    				pass
    ```
    

**Virtual Subclass and Goose typeing**

we can register class that implement the same methods but do not inherit the ABC as a "virtual subclass" of that ABC so that the object can be recognized by `issubclass()` or `isinstance()`

Goose typing, Read this: [https://dgkim5360.github.io/blog/python/2017/07/duck-typing-vs-goose-typing-pythonic-interfaces/](https://dgkim5360.github.io/blog/python/2017/07/duck-typing-vs-goose-typing-pythonic-interfaces/)

## Chapter 12. Inheritance

---

**Avoid inheriting the build in types**

In the C implementation of python, build-in types themselves (list, dict) are "not so pythonic", as their internal methods sometimes do not use the special functions ( For example, `__setitem__` is ignored by `__init__` methods of the build-in dict).

- Therefore, We should **avoid** inheriting the build in types, such as `class CustomDict(dict)`
- Instead, we should inherit these types from collections, **UserList**, **UserDict** and **UserString**

**Multiple inheritance and Method resolution**

Python can inherit from multiply classes. Method resolution specifies the order of lookups

- Python class maintain an attributes (Class attributes) called `__mro__` (method resolution order), which hold a tuple of referneces to the superclasses.
- Python will follow the order in MRO when traversing the inheritance graph.
    
    ```python
    hasattr(list, "__mro__")
    >>> True
    print(list.__mro__)
    >>> (<class 'list'>, <class 'object'>)
    import numbers
    print(numbers.Integral.__mro__)
    >>> (<class 'numbers.Integral'>, <class 'numbers.Rational'>, <class 'numbers.Real'>, <class 'numbers.Complex'>, <class 'numbers.Number'>, <class 'object'>)
    ```
    
- In case of multiple inheritance `class c(a, b)` and if both a and b implemented a method of the same name. __mro__ determines uniquely which method to call when we call `super().method()`

**Invoking specific superclass methods directly**

In the case of multiple inheritance, we can also invoke a method on the superclass directly

```python
class C(A, B):
		...
		def method1(self):
				super().method1()    # we rely on MRO to determine which method to call
				A.method1(self)      # we explicitly ask to use method defined in class A
													   # here, A is class, instance is passed as argument (self)
```

**Rules on multiple inheritance**

- Distinguish interface inheritance (internal structure relationship) from implementation inheritance (avoid code duplication)
- Make interface explicit with ABC
- Using mixins for code reuse [(Mixins are small classes that focus on providing a small set of specific features that you can later combine with code that live in other classes)](https://coderbook.com/@marcus/deep-dive-into-python-mixins-and-multiple-inheritance/)
- Make Mixins explicit by naming, eg: PackMixin
- Don't subclass from more than one concrete class
- Favor Object composition over inheritance

## Chapter 13. Operator overloading

---

**Overview**

Operator overloading in python is done by **implementing the corresponding special methods.** We have the following rules:

- We cannot overload operators for build-in types
- We cannot create new operators
- A few operators cannot be overloaded: **is**, **and**, **or** and **not**

**For operator overloading, we should not modify the operands, we should return a new object**

**Unary Operators**

```python
__neg__()   # negative -v
__pos__()   # positive +v
__abs__()   # abs(v)
```

### **Overloading addition**

**__add__ and __radd__**

With only __add__ defined for the Vector class, we will receive the error:

```python
vector + (1, 2, 3)
>>> OK
(1, 2, 3) + vector
>>> TypeError: can only concatenate tuple (not "Vector") to tuple 
```

Resultion steps for additions:

When we write an expression a + b, python perform the following steps:

1. If a has __add__, call a.__add__(b) and return results
2. If a doesn't have __add__ or calling it return NotImplemented, check if b has __radd__, if so, call b.__radd__(a) and return results
3. if b doesn't have __radd__, raise error

Therefore, to properly define addition (when a and b are of different class), **we should define both __add__ and __radd__ method.** 

**__iadd__**

+= operator default to a = a + b, which use __add__ and return an new object. To perform inplace addition, we need to implement __iadd__ special methods.

**Example**

```python
def __add__(self, other): 
		try:
				pairs = itertools.zip_longest(self, other, fillvalue=0.0) 
				return Vector(a + b for a, b in pairs)      # properly return a new object
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

- **List of special method for operator overloading**
    
    ```python
    Operator    Forward          Reverse            In place
    +           __add__          __radd__           __iadd__
    -           __sub__          __rsub__           __isub__
    *           __mul__          __rmul__           __imul__
    /           __truediv__      __rtruediv__       __itruediv__
    //.         __floordiv__     __rfloordiv__      __ifloordiv__
    %           __mod__          __rmod__           __imod__
    divmod()    __divmod__       __rdivmod__        __idivmod__
    **, pow()   __pow__          __rpow__           __ipow__
    @           __matmul__       __rmatmul__        __imatmul__
    &           __and__          __rand__           __iand__
    |           __or__           __ror__            __ior__
    ^           __xor__          __rxor__           __ixor__
    <<          __lshift__       __rlshift__        __ilshift__
    >>          __rshift__       __rrshift__        __irshift__
    ```
    

### **Comparsion Operators**

```python
Operator   Forward         Reverse
a == b     a.__eq__(b)     b.__eq__(a)      
a != b     a.__ne__(b)     b.__ne__(a)    # default will fall back to not __eq__
a > b      a.__gt__(b)     b.__lt__(a)    # therefore, we do not generally need to
a < b      a.__lt__(b)     b.__gt__(a)    # implement __ne__
a >= b     a.__ge__(b)     b.__le__(a)
a <= b     a.__le__(b)     b.__ge__(a)
```

## Chapter 14. Iterables, Iterators and Generators

---

**Iterable**

Every collection in Python is iterable. 

- As stated above, as soon as a class implement __getitem__ method, python is able to iterate over the class by getting all the elements from 0. As an iterable, the class can be used as input to build lists and other iterable types.

Whenever interpreter needs to iterate over an object (iterable) it automatically calls iter() built-in function. Which does the following things:

1. call __iter__ if this specical method is implemented, which should return an iterator
2. If not, and the __getitem__ is implemented, python creates an iterator that attempts to fetch items starting from 0
3. if all failed, raise TypeError, "object is not iterable"

A class implementing __iter__ is recognized as iterable, without subclassing or registration

```python
class Foo:
    def __iter__(self):
    pass

from collections import abc 
print(issubclass(Foo, abc.Iterable))    # Goose typing
>>> True
print(isinstance(f, abc.Iterable)) 
>>> True
```

**Definition of iterable and iterator**

- **Iterable**: any object which iter() built-in can be called upon (__iter__ and sequences, etc.)
- **Iterator**: the object that is returned by calling iter() on an iterable
- Iterators are also iterables, but iterables are not iterators
    
    ```python
    >>> a = list(range(10))
    >>> a
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> b = iter(a)
    >>> repr(a)
    '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'    # list
    >>> repr(b)
    '<list_iterator object at 0x7fe16eb09430>'
    >>> dir(b)
    ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
     '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
     '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', 
    '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', 
    '__str__', '__subclasshook__']
    ```
    

**For loop with an iterable** 

a for loop is interpreted as the following code by python

```python
for char in s: 
		print(char)
# is interpreted as:
it = iter(s) 
while True:
		try:
				print(next(it))      # next take the next item from the iterator
		except StopIteration:
				del it
				break
```

**A standard iterator implementing two special methods**

- __next__ return the next available item, raising `StopIteration` when there are no more items, used by next()
- __iter__ returns itself. (note that for an iterable implementing __iter__ method, it need to return a iterator. This requirement here enforce the same behavior for consistence)
    
    ```python
    class Sentence:
    		def __init__(self, text): 
    				self.text = text
    				self.words = RE_WORD.findall(text) 
    		def __repr__(self):
    				return 'Sentence(%s)' % reprlib.repr(self.text) 
    		def __iter__(self):
    				return SentenceIterator(self.words)   # return a generator, defined as below
    
    class SentenceIterator:             # an standard iterator that return words
    		def __init__(self, words): 
    				self.words = words 
    				self.index = 0
    		
    		def __next__(self): 
    				try:
    						word = self.words[self.index]     # as stated in the book, Iteratables are 
    				except IndexError:                    # not iterators, we should not put 
    						raise StopIteration()             # __next__() into Sentence directly
    				self.index += 1                       # to separate purpose
    				return word 
    		
    		def __iter__(self):
    				return self
    ```
    

**Generator function**

- A python function that has `yield` keyword in its body, when called, will **return a generator object**.
- A generator object, when invoked with next(), will execute the code and advance to the next yield in the function body. And next() return the value yielded. When the **function body returns**, the enclosing generator object raise StopIteration.
- As shown below, generator object also implement __iter__ method. Therefore, a generator object behaviors as an iterator.

Using generator function, we can return an iterator from __iter__() by making it a generator function

```python
class Sentence:
    ...
		def __iter__(self):
				for word in self.words:
						yield word      # any function that include yield will 
				return              # return a generator object (iterator)
                            # therefore, we do not need to implement an additional iterator
>>> repr(Sentence.__iter__())
'<generator object f1 at 0x7fe16eb6e740>'
>>> dir(Sentence.__iter__())
['__class__', '__del__', '__delattr__', '__dir__', '__doc__', 
 '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
 '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', 
 '__lt__', '__name__', '__ne__', '__new__', '__next__', '__qualname__', 
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
 '__str__', '__subclasshook__', 'close', 'gi_code', 'gi_frame', 
 'gi_running', 'gi_yieldfrom', 'send', 'throw']
```

**Execution of the generator object**

To illustrate the point of how generator object excute the function body, consider the following example:

```python
def gen():
    numbers = list(range(1,11))
    for n in numbers:
        nn = n * n
        yield(nn)                 # next() only stop at yield 
    yield("last one")             # or all yield is passed and when function finish,
    print("DONE!")                # at which time it raise StopIteration
                                  # therefore, the next next() call
for item in gen():                # after the last yield("last one") will
    print(item)                   # execute print("DONE") and then raise error
		print("--------")             # therefore, the loop body is not entered
# output:                         # after print "last one"
1
---------
4
---------
...
81
---------
100
---------
last one
---------
DONE!
```

## Appendix

### typing

here I include some example of using the typing library:

```python
from typing import Union, List, Any
def __init__(
        self,
        param1: Union[int, List[int], str, o3.Irreps],
        param2: str = 'integral',
        param3: Any = None,
    ):
```

### Decprecation warnings

```python
if normalization is not None:
		warnings.warn(
        "`normalization` is deprecated. Use `irrep_normalization` instead.",
		    DeprecationWarning
	  )
    irrep_normalization = normalization
```