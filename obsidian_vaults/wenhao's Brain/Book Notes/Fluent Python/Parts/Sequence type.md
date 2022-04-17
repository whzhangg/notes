# An Array of Sequence
### Overview of Sequences
##### Container vs. Flat sequence
Container sequences *hold references* to the objects they contain, and can hold items of different types. While the flat sequences *store the value* of each item within its own memory space, not as distinct objects.

##### Mutable vs. Immutable*
An *Mutable object* can change their values but keep their ids. *Immutable object* cannot be altered and a new object has to be created if a different values has to be stored. 

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
Difference in special methods implemented by immutable sequence and mutable sequences:
![[immutable and mutable special methods.png|500]]

### List
##### List Comprehension
List Comprehension (listcomps) is a built-in method to generate a list. For example:
```python
ascii = [ ord(s) for s in symbols if ord(s) > 127 ]
```    
generate a list with a condition.

Listcomp also support multiply loops, The resulting list is arranged as if the for loops are nested:
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
    
##### Generator Expressions
Generator expression use the syntax as listcomps but are enclosed in parenthesis instead of `[ ]`. They return a *generator object* that yield values one by one:
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
##### Using tuples
Tuples hold data in sequence and the position of these items gives its meaning. Tuple is *immutable*: we cannot add or remove elements.
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

##### Unpacking
Tuple can be *unpacked* by its shape (*parallel assignment*). List can also be unpacked, but tuples are more suitable
```python
tokyo = ('Tokyo','JP',36.933,(35.689722,139.691667))    # nested tuple unpacking
metro_areas = [ tokyo, ... ]
for name, cc, pop, (latitude, longitude) in metro_areas:
		print(name, latitude, longitude)

(b, a) = (a, b)    # parallel assignment
```

##### Unpacking with `*`
We can use `*prefix` to exactly one variable in the parallel assignment and it can appear in any position. It will match and include all the remaining items
```python
a, *body, c, d = range(5)
>>> a, body, c, d
(0, [1, 2], 3, 4)
```

##### Named Tuples
*collections.namedtuple* function produce a subclass of tuple with field names and class name.
- To construct the instance, data must be passed as positional arguments to the constructor
- Data can be accessed by name or position

it support a few additional methods: `_fields` attributes, `_make(iterable)` class method (make a instance from an iterable) and `_asdict()` method which *return a dictionary*.
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
##### Slicing
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
Slicing with `s[a:b:c]` specifies a stride or step size c, stride can be negative, giving reversed result. This method is only valid within `[ ]` operator

Slice use `__getitem__` and `__setitem__` special methods that handle `[ ]` operator

We can also use ellipsis `...` as a short cut for "as many as `:, :, :` in slicing. `...` is a alias to an ellipsis object which is passed as parameters

##### Slice object
We can create a slice object: `slice(a,b,c)` https://docs.python.org/3/c-api/slice.html, which can be used to define a specific slice on data, as the previous example shown.

##### Inplace addition
Operator `+=` and `*=` modify the left size of the assignment, for example: `a += b`.

For `+=`, python will attempt to call `__iadd__` ( in place addition ). If it is not implemented, python will then call `__add__`. With `__iadd__` method, any change will happen in place, but if `__add__` is used, a += b will have the same effect as `a = a + b`, where the result is assigned to `a` as a new object ( the instance will be a different one)

In general, for mutable sequence, `__iadd__` would be implemented, while for immutable sequence, it it not.

For `*=`, the equivalence is `__imul__`

##### list sorting
`list.sort()` method sorts a list in place, which return None ( Return None is convention if the functions or methods change the object itself). Since it is a inplace method, immutable object do not support it.

`sorted()` method creates a new list and returns it.

Both method take two optional arguments:
1. *reverse [= False]*: specify if the order is reversed
2. *key*: a one-argument function passed as parameter giving a value for each item to sort
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

##### Inserting element in order
`bisect` package provide function `bisect` and `insort` that perform binary search for an ordered list. https://docs.python.org/3/library/bisect.html

`bisect(seq, item)` take a sorted list and an element and return the index which would be the position of that element when it is inserted to the sorted list [ biset_right() and biset_left() determined different behavior in the case of equal value ]

`insort(seq, item)` insert the item into the sequence directly
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
##### Arrays
Array is a more efficient iterable than a list (flat). it include all mutable sequence operation (pop, insert, extend) and additional methods for fast loading and saving (`.fromfile()`, `.tofile()`)

Array directly store the object, so creating an array require a typecode to determine the type of object. For example 'd' refer to double. For more on arrays, see https://docs.python.org/3/library/array.html.

##### Memory View

Memory view is a shared-memory sequence type that allow data to be used by different data-structure without copying(such as bits and integer). For more, see https://docs.python.org/3/c-api/memoryview.html.

##### Deques
*collections.deque* has the following features compare to a list, although both of they support similar method (.append, .pop)
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
For more, see https://docs.python.org/3/library/collections.html#collections.deque.
