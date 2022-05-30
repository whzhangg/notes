# Practice of the Python Pro

Created: November 1, 2021 2:59 PM

This note consider how to design the structure of the code in python, and is taken from the book *[Practice of the Python Pro](https://www.manning.com/books/practices-of-the-python-pro)*, By Dane Hillard

### Extensibility and flexibility

**Extensibility**
a code is said to be extensible if adding new behaviors to it has little or no impact on existing behaviors. In an ideal extensible system, adding new behavior involves adding new classes, methods, functions or data that encapsulate the new behavior without changing existing code

**Flexibility**
Flexibility measures the code's resistance to change, ideal flexibility means that any piece of your code can easily be swapped out for another implementation.

**Reducing Rigidity**

1. *Single responsibility* for method and functions
2. *Extracting configuration from impletation* and reducing the structure complexity 

**Cyclomatic complexity**
Cyclomatic complexity measures the number of execution paths through a function or methods: an if statement give 2 possible execution path. nested if statement lead to 4 execution path.
Consider the following code:
```python
def random_food(request):
	food = random.choice(FOODS)
	if request.headers.get('Accept') == 'application/json': 
		return json.dumps({'food': food})
	elif request.headers.get('Accept') == 'application/xml': 
		return f'<response><food>{food}</food></response>'
	else:
		return food
```
Its complexity is 3 for three possible path. However, we can reduce the complexity to 1 by putting the if statement into configurations:
```python
formats = {
'application/json': json.dumps({'food': food}), 
'application/xml': f'<response><food>{food}</food></response>',
}
def random_food(request):
	food = random.choice(FOODS)
	return formats.get(request.headers.get('Accept'), food)
```

**Composition instead of inheritance**
Instead of creating classes that depend on each other, we can pass the instance to the class as parameters.
Consider the following implementation of a bicycle:
```python
class Tire:
	def __repr__(self):
		return 'A rubber tire'

class Frame:
	def __repr__(self):
		return 'An aluminum frame'

class CarbonFiberFrame:
	def __repr__(self):
		return 'A carbon fiber frame'
	
class Bicycle:
	def __init__(self):
		self.front_tire = Tire() 
		self.back_tire = Tire() 
		self.frame = Frame()
	def print_specs(self):
		print(f'Frame: {self.frame}')
		print(f'Front tire: {self.front_tire}, back tire: {self.back_tire}')
```
This way of define a bicycle is OK, but if we want to change the components of the class "bicycle" with another kind of frame, we have to redefine a new class.
Now, consider passing instances of Tire and Frame as parameters:
```python
class Bicycle:
	def __init__(self, front_tire, back_tire, frame):
		self.front_tire = front_tire 
		self.back_tire = back_tire 
		self.frame = frame
	def print_specs(self):
		print(f'Frame: {self.frame}')
		print(f'Front tire: {self.front_tire}, back tire: {self.back_tire}')
```
Now we can construct bicycle object with different components. Different instance can have different components, but they are all bicycle class and provide the same methods.

**Interface**
Different types of objects can be swapped easily if they have the same interface. Sharing *agreed-upon interfaces between the high- and low- level code* gives flexibility.

**Breaking up class** 
when several methods in a class share a common prefix or suffix, especially one that does not match the name of the class, we can usually refactorize the code to create a new class

### Rules of inheritance

Inheritance is for *specialization behavior*. In this sense, subclasses should be treated as special case of the superclass: An instance of the subclass is an instance of the superclass

**Inheritance vs. Composition**
- If class B inherits from a class A, we say "B is an A"  (inheritance)
- If C used an instance of a class D, we say that "C has a D" (composition)

**Principle of substitutability of inheritance** (Barbara Liskov)
Any instance of a class must be replaceable by an instance of one of its subclasses without affecting the correctness of the program

**Ideal use case for inheritance**
- The problem need a shallow, narrow hierarchy (not too many layers of inheritance, not too many subclases)
- subclasses are at the leaves of the object graph: they should not make use of other objects
- subclasses should use all the behavior of their superclass


**Abstract base class**
An abstract base class is a way to use inheritance to provide an interface for the classes that provide common methods. The abstract base classes are provide in module ABC
```python
from abc import ABC, abstractmethod

class Predator(ABC):
	@abstractmethod
	def eat(self, prey):
		pass               # abstractmethod have no default implementation

	class Chameleon(Predator):
		def eat(self, prey):
		print(f'Shooting tongue at {prey}!')
```