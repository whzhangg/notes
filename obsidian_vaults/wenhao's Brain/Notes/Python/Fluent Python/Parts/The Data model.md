# Data Model
### The python data model
##### Special Methods
The consistency of python is achieve by the data model. For example: `len(object)` will return the length, we do not need to call a specific member function. This behavior is called *Pythonic* and is achieved by python's *data model*:
- The data model formalize the interfaces of the objects of the language itself. Such as sequences, iterators etc.
- The python interpreter invokes *special methods* of the object to perform the actual operations. The name of the special methods are always written with leading and trailing double underscores, i.e., `__getitem__`
    
For example, the index operation `obj[key]` is supported  by the `obj.__getitem__()` special method. Special methods can also be called *dunder methods*.

The following example illustrate using two special methods, where:
- `namedtuple` construct a simple class with only attributes without custom methods
- with `__len__`, and `__getitem__` defined, the Deck object can be accessed just like a list, can be iterated through and sliced.
- The special methods *should be directly called only by the python interpreter, not by the users*. And most of the time, the special method call is implicit.
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

##### Special methods for a Numeric types
We have a few other simple special methods:

`__repr__` method is called to get a *string representation* of the object for inspection. The string returned should be unambiguous and give enough information for re-construction the object being represented.

`__str__` method convert the object into a *suitable string for printing*, and is called by `str()` method, and implicitly used by the print function.

`__add__` and `__mul__` overload the operator `+` and `*`. In both case, the method return a new instance of the object without modify either the operand. For example:
```python
def __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return Vector(x, y)      # return a new instance
```

`__bool__` method convert any object in a boolean context, such as in an if statement, it is also called by `bool()` method, which implicitly perform the conversion. If `__bool__` is not implemented, python tries to invoke `.__len__()` method and return true if length > 0. 
    
