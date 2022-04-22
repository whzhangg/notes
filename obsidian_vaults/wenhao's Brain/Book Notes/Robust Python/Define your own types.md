# Defining your own types
>Defining our own types help to communicates intentions by building a shared vocabulary

### Light weight type definition
##### Enum
python enumeration can be used when we want to *communicate a static set of choices*. Usually, when using enumeration, we do not need to access the values, but only using the names

It also provide a type that can be used by type annotation
```python
>>> from enum import Enum
>>> class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 3
>>> print(type(Color.RED))
```
For detail, we can refer to [https://docs.python.org/3/library/enum.html](https://docs.python.org/3/library/enum.html)

##### Data classes
Dataclass provide similar but more functionality over namedtuples, they are appropriate when the data members within the dataclass are independent of one another. Functions belong to the dataclass can also created.

Basically, it provides a decorator and functions for *automatically adding generated special methods* such as `__init__()` and `__repr__()` to user-defined classes.
```python
from dataclasses import dataclass

@dataclass(eq = True, order = True)
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```
A number of options can be passed to data classes, For example([library reference](https://docs.python.org/3/library/dataclasses.html))
- `eq`: If true (the default), an `__eq__()` method will be generated. This method compares the class as if it were a tuple of its fields, in order. Both instances in the comparison must be of the identical type. If the class already defines `__eq__()`, this parameter is ignored.   
- `order`: If true (the default is `False`), `__lt__()`, `__le__()`, `__gt__()`, and `__ge__()` methods will be generated. These compare the class as if it were a tuple of its fields, in order. Both instances in the comparison must be of the identical type. If `order` is true and `eq` is false, a value error is raised.

##### dataclass to dictionary
It's easy to convert dataclass object to dictionary. This is achieved by importing the `asdict()` method. 
```python
from dataclass import asdict
dictionary = asdict(InventoryItem)
```
To load a dataclass object from dictionary, we can use expansion, [ref](https://1kara-hajimeru.com/2021/02/1691/):
```python
item = InventoryItem(**dictionary)
```

### Classes
It helps to define the characteristic of class and when to use class by thinking about it’s difference with just a gathering of relational data:
- the data in a class depend on each other
- Class offer controlled initialization
- Class offer encapsulation (with `_`)

##### Design of the class interfaces
To get the most initutive and immediate understanding of the class functionality, we should design our interface as “controls and their movements” and let them be natural. For example, the definition of a class should adhere to how it is represented in real life. 

There are two ways to help systematically design an interface:
1. Test-driven development (TDD)
	In test-driven development, we first design the tests (how the code should behave in practice), and write just enough code to pass that test. This improve our interface by thinking about how future users will use our code.
2. Readme-driven development (DDD)
    We write a readme document and develop our code based on the readme documents.

##### Class Protocols
Protocols define a set of behaviors that objects may implement as a type. We can use protocols to provide an intention and extraction of ideas. *But as with other typing, it is not enforced in the executation*. See https://docs.python.org/3.8/library/typing.html?highlight=protocol#typing.Protocol

```python
from typing import Protocol

class Name(Protocol):
    last: str
    first: str
    def print_name(self):
        """None"""

class EnglishName:
    def __init__(self, name:str) -> None:
        part = name.split()
        self.first = part[0]
        self.last = part[1]

    def print_name(self):
        print(f"english name: {self.first} {self.last}")
```

There is a cost in adding all these type hinting to our codes, but it clearly express our intent and make future maintaince easier. 