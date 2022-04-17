
# Interfaces, Protocols and ABCs
##### Protocols in python is informal
An interface (protocol) is the object's public methods that enable it to play its role. Python cooperate with essential protocols as much as possible and usually try to work with even the simplest implementation. 

For example, A sequence interface defined in abstract base class require the following method: `__getitem__`, `__contains__`, `__iter__` and `__reversed__` special methods. However, the following example shows that with only the implementation of `__getitem__`, python still perform the sequence operation correctly:
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

### ABCs
##### Concepts
*Abstract base class* (ABC) make interfaces explicit and verify the implementations for conformance. ABC present a different idea from the previous duck typing. ABC `require` its "concrete" class (as contrast to abstract class) to implement abstract methods.

Python will *check for the implementation* of abstract method not at import time, but *only at runtime* when we instantiate an instance. If we fail to implement any abstract method, interpreter will raise error.

##### collections.abc
In collections module, the following abcs are implemented.
![[ABCs.png|500]]

most of the classes inherit from Iterable(`__iter__`), Container(`__contains__`) and sized (`__len__`). The classes that are lower at the bottom require to implementation the abstract methods defined in the previous class. For example, A sequence  (`__getitem__`, `__contains__`, `__iter__` and `__reversed__`) contain the abstract method of iterable, container and sized.

Sequence, Mapping and Set are the main immutable collection, each has a mutable subclass.

To inherit from a particular abc, use:
```python
import collections
class FrenchDeck(collections.MutableSequence):
```

##### Defining an ABC
To define for an abstract base class for our purpose, we inherit abc.ABC (module abc). 

As a abstract class, we can define *abstract methods* and *concrete methods*. 
- Abstract methods has to be defined by the following implementation
- Concrete methods in an ABC are those that does not depend on the actual implementation. Furthermore, for concrete methods, we only need to pursue "correctness": we can expect the actual subclass implementation to overwrite it for optimization and efficiency.

As an example, we consider an abstract class that pick items at random
```python
import abc
class Tombola(abc.ABC):               # To define an abc, subclass abc.ABC
	@abc.abstractmethod
	def load(self, iterable):
		"""Add items from an iterable."""

	@abc.abstractmethod               # function body can be empty
	def pick(self):
		"""Remove item at random, returning it
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

Abstract class method: we can use compound decoration:
```python
class MyABC(abc.ABC): 
    @classmethod
    @abc.abstractmethod
    def an_abstract_classmethod(cls, ...):
    	pass
```
    

### Virtual Subclass and Goose typing
##### Virtual subclass
We can register class that implement the same methods but do not inherit the ABC as a "virtual subclass" of that ABC so that the object can be recognized by `issubclass()` or `isinstance()`

##### goose typing
Goose typing, Read [this](https://dgkim5360.github.io/blog/python/2017/07/duck-typing-vs-goose-typing-pythonic-interfaces/)
