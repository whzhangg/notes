# Iterables, Iterators and Generators
### Iterables
##### Iterable
*Every collection in Python is iterable*. 

Whenever interpreter needs to iterate over an object (iterable) it automatically call the `iter()` built-in function, which does the following things:
1. call `__iter__` if this specical method is implemented, which should return an iterator
2. If not, and the `__getitem__` is implemented, python creates an iterator that attempts to fetch items starting from 0
3. if all failed, raise TypeError, "object is not iterable"

A class implementing `__iter__` is recognized as iterable, without subclassing or registration
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

##### Definition of iterable and iterator
- *Iterable*: any object upon which `iter()` built-in can be called.
- *Iterator*: the object that is returned by calling `iter()` on an iterable.

Iterators are also iterables, but iterables are not iterators    
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

##### For loop with an iterable
A for loop is interpreted as the following code by python:
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

### Iterator
##### Standard iterator
A standard iterator implementing two special methods:
1. `__next__` return the next available item, raising `StopIteration` when there are no more items, used by `next()`
2. `__iter__` returns itself. (note that for an iterable implementing `__iter__` method, it need to return a iterator. This requirement here enforce the same behavior for consistence)

The following example define an iterable which return an iterator:
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
    

##### Generator function
A python function that has `yield` keyword in its body, when called, will *return a generator object*.

A generator object, when invoked with `next()`, will execute the code and advance to the next yield in the function body. And `next()` return the value yielded. When the *function body returns*, the enclosing generator object raise StopIteration.

As shown below, generator object also implement __iter__ method. Therefore, a generator object behaviors as an iterator. Using generator function, we can return an iterator from __iter__() by making it a generator function
```python
class Sentence:
    ...
	def __iter__(self):
		for word in self.words:
			yield word      
		return              
# any function that include yield will return a generator object (iterator)
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

##### Execution of the generator object
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
