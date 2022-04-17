# Functions as Objects
### Functions
##### Overview
>Functions in Python are objects themselves, further more, they are first class objects.

A *first class object* is an entity that can be dynamically created, destroyed, passed to a function, returned as a value, and have all the rights as other variables in the programming language have.

*Higher order functions* are functions that take a function as argument or return a function, For example, `sorted(a, key = len)` is a higher order function, that take an one argument function len() to sort the `a`.
    
##### Anonymous Functions
lambda keyword creates an anonymous function (a function with no name)
```python
sorted(fruits, key=lambda word: word[::-1])
``` 
which take an argument `word` and return `work[::-1]`
    
We can also use lambda to define simple functions: 
```python
last = lambda word: word[::-1]
``` 
which can be called by `last()`
    
##### Callable types in Python
A callable can be one of the following:
1. User-defined functions & Build-in functions
2. Methods & Build-in methods
3. Generator functions
4. Classes: in python calling a class (create an instance) is like calling a function
5. Class instances: if a class defines a `__call__` method, then its instnace is callable 

##### User defined Callable
A class implementing `__call__` is an easy way to create *function-like objects that have internal state*
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
##### Arguments
Consider the following parameter list:
```python
def tag(name, *content, cls=None, **attrs):
```
- name is a *normal positional argument*,
- `*content` capture any number of arguments after the first (name), as *tuple*
- cls is a *keyword argument* that can only be passed by giving `cls = " "`, it is different from normal positional argument with default types.
- `**attrs` capture all arguments that are given by keyword but not in the argument list *as dict*.
- Prefixing a dictionary with `**` and pass it as argument *will pass all its items as separate named arguments* (reverse of the above step)

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

##### Keyword only argument
Keyword only argument are not positional argument, To specify a keyword only argument, we need to put them after argument prefixed with `*`, if we do not need argument prefixed with `*`, we can put a `*` by it self.

Compare  `def f(a, b = None)` and `def f(a, *, b = None)`.
In the first case, b is a positional argument with default value, but in the second case of keyword only argument, b can only be passed if we use keyword b = "" specifically.

Keyword only argument do not need to have a default value, they can be mandatory

### Function inspection
##### Function attributes
Function objects have many attributes. For example, `__doc__` attributes generate the help text of an object. `__defaults__` attributes store default value for formal parameters
```python
def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)
    
factorial.__doc__
>>> 'returns n!'
```

##### annotation attributes
`__annotations__` attributes store the metadata related to the parameters of a function declaration. For example
```python
def clip(text:str, max_len:'int > 0'=80) -> str:
```
define a function with [[Python type annotation|annotation]]. The information of annotations are stored in `__annotations__` but is `not processed by python at all`.
```python
clip.__annotations__
>> {'text': <class 'str'>, 'max_len': 'int > 0', 'return': <class 'str'>}
```    

##### Modules inspection
*Modules in Python are also first-class objects*, and the standard library provides several functions to handle modules, just as they provide tools to handle functions.
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
    
### Support for functional Programming
Operator Module provides a few tools that can replace simple oneline functions:

##### itemgetter()
`itemgetter` *returns a function that, given a sequence, returns the item at an index*. If several index are passed, it will return tuples with the extracted values. Therefore, `itemgetter(1)` is thus the same as `lambda fields: fields[1]`

Since itemgetter use `[ ]` operator, it can also be used on mappings.
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

##### attrgetter()
attrgetter is similar to itemgetter but *receive attribute name and return the attributes of the given objecs.*

##### methodcaller()
methodcaller will create a function that call a method of the object by the name given by the arguments 
```python
s = "hello world"
upcase = methodcaller('upper')
upcase(s)
>>> "HELLO WORLD"
```
    
##### Functools.Partial methods
Given a function, a partial application produce a new callable with some of its arguments of the original function fixed.

Partial takes a callable as first argument, followed by an arbitrary number of positional and keyword arguments to bind.
```python
from functools import partial
triple = partial(mul, 3)
triple(7)
>>> 21
```

### Function Decorators and Closures
##### Decorators
A *Decorator is a callable* that takes another function as argument and return another function. *Decorations are executed immediately when a module is loaded* (import time), the *decorated functions runs only when they are invoked* (run time)
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

##### Stacked Decorators
When two decorators `@d1` and `@d2` are applied to a function f, as in:
```python
@d1
@d2
def f():
		print('f')
```
The result is the same as `f = d1(d2(f))`

### Examples of using decorators
##### Using decorator to track functions**
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

##### Using decorator to time functions**
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

##### Parameterized Decorators
Python only take the decorated function and pass it as argument to the decorator function. 

To make a decorator that can accept a parameter, we *define a function that take arguments and return a decorator*, For example
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
    
### Decorator in standard library
Python has three standard decorate methods: *@property*, *@classmethod* and *@staticmethod*

In functools, there are other decorators, we show two of them:
##### lru_cache
`functools.lru_cache` decorator that will *save the result of the previous invocation and return the result directory if the inputs are the same*.

It accept two parameters: `functools.lru_cache(maxsize=128, typed=False)`. Where maxsize determine how many previous call to store, typed will check if the input type as well as input values ( if 1.0 and int(1) is the same )
```python
@functools.lru_cache() # the repeated calls will not be executed again
@clock #
def fibonacci(n):
    if n<2: 
    	return n
    return fibonacci(n-2) + fibonacci(n-1)
```

##### Single Dispatch
In python, it is not possible to overload functions, we cannot therefore create variations of function with different result for different input ( we can implement if elif structure, but they are not easy to maintain)

`@singledispatch` can decorate a plain function to be a generic function, as the example shows:
- singledispatch decorate a base function that handles a abstract type
- each specialized function is decorated by `@basefunction.register(type)`. The name of the specialized function does not matter
- Several register decorators can be stacked together
- When possible, use boarder class, such as `abs.MutableSequence`, instead of `list`
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
