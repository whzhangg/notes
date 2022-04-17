# Object References and Mutability
### Referencing
##### Python use reference
Summary of practical consequences of referencing
- simple assignment create aliases
- augment assignment with `+=` or `*=` may create new objects to bound to left hand side or modify the left size in place, depending on the mutability and implementation.
- rebinding a new value to an existing variable does not change the object previously bound to it
- function *parameters are passed as aliases*
- using mutable object as default values for function parameters is dangerous

##### Variable names are labels
Python variables are like refernce, they are labels attached to objects. For example, in an assignment `a = b`, Python retrieve or create object on the right of the assignment, and *then* bound the left variable name to the object.

##### Identity, Equality and Alias
Every python object has *an identity*, *a type* and *a value*. An object's identity (`id()`) never changes once it has been created (memory in the address)
- `==` compare the object's value, using their `__eq__` implementation (therefore, == operator can be override by class implementation and behavior differently)
- `is` compare the itentity of the python object, it compare the object ID and cannot be overloaded.

##### Relative Immutability

Tuple is an immutable but can hold references to the objects that are mutable. The immutability of tuples refer to the immutability of physical contents of tuple datastructure (eg, number of elements), but does not extend to the refered objects.

### Copies
##### Aliasing
`a = b` creates an alias.
```python
charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
lewis == charles
>>> True
id(charles), id(lewis)
>>> (4300473992, 4300473992).  # memory address
```
    
##### Shallow Copy 
Shallow copy duplicate the outermost container, but copy is filled with reference to the same items held by the original container. `copy.copy()` return a shallow copy
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
l2[2] += (10, 11)   # ! += creates a new tuple and rebinds l2[2] to the new tuple 
print('l1:', l1) 
print('l2:', l2)
>>> l1: [3, [66, 44, 33, 22], (7, 8, 9), 100]
>>> l2: [3, [66, 44, 33, 22], (7, 8, 9, 10, 11)]
```

##### Deep Copy 
Deep copied objects do not copy embedded objects. `copy.deepcopy()` return a deep copy

##### Copy special methods
the behavior of copy and deepcopy can be controlled by implementing `__copy__()` and `__deepcopy__()` special methods.   

### Function parameters
The only way parameter passed in python is *sharing*, the parameters inside the function become aliases of the actual arguments. Therefore, *function can change mutable object passed as parameters, but cannot change their identity*: i.e. if inside function, the parameter is changed *in-place*, then its result will presist after the function finish.
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

Mutable types *should not be used* as parameter defaults
    
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
    
##### Defending against mutable parameters
When passing mutable objects as parameter, we should think twice, *when in doubt, always make a copy*
    
### Del() and weak reference
##### Del()
`Del()` perform Garbage Collection. `del()` statement deletes the name explicitly, not the object. An object is **garbaged** (deleted) only if all the variables holding reference to it are deleted or the object become unreachable.

Python keep track of the reference by reference counting (like smart pointer in c)

A class can define its behavior of del statement  by implementing `__del__` special method, which is invoked by python to execute some code before the object is destroyed. "You will seldom need to implement `__del__` in your own code for no good reason"

##### Weak References
A weak Reference to an object *do not increase its reference count*, an instance of weak reference can be called to return the object it's refering to, and return None if the object is destoryed.
```python
# using weak reference
import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref())
>>> {0, 1}
```
    
##### WeakValueDictionary
A weakvalue dictionary implements a mutable mapping where the values are weak references to objects, when a referred object is destoried, the corresponding key is automatically removed from the dictionary. It is commonly used for caching.
```python
import weakref
weakdict = weakref.WeakValueDictionary()
```
    
