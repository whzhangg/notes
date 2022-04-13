# Robust Python

Created: April 3, 2022 10:48 PM
Description: Reading notes for Patrick Viafore’s [Robust Python](https://www.oreilly.com/library/view/robust-python/9781098100650/) book.
> There should be one—and preferably only one—obvious way to do it
>\- Zen of Python

## Robustness

- In developing code, we have to accept change, our code will be split apart, stitched together and reworked, and embrace it.
- Writting clean and maintainable code is ultimately for communication, we need to be able to communicate our intent with future developers as well as future selves. Without a clear intent in our code, there is no communication to the future and productivity is lost.
- law of least surprise: a program should always respond to the user in the way that astonishes them the least: surprising behavior leads to confusion, which leads to misplaced assumptions and bugs.
- Necessary complexity and accidental complexity
Necessary complexity is the complexity that is inherit in the problem, but accidental complexity is the complexity in inefficient organization that produce wasteful or confusing code. 
If the following things happen, you have accidental complexity:
1. things that sound simple are non-trival to implement.
2. Difficulty to let others to understand your code

> You own it to feature maintainers to enable them to deliver value at the same speed that you can today, Otherwise, your codebase will get bloated, schedules will slip and complexity will grow. It is your job as a developer to mitigate that risk.
> 

Exmples of expressing intent:
1. Pick the right collection for the task at hand
- *List*: to be iterated over, rarely retrieving specific elements in the middle with duplicates allowed.    
- Generator: to be iterative over but never indexed into, with lazy access.
- Tuple: an immutable collection that rarely iterated over, and specific elements can be extracted easily.
- Set: iterable collection with no order and no duplicates
- Dictionary: mappers
2. Iteration: for loop, while loop and list comprehensions express different intent in the code.

## Part I. Annotating your code with types

Python types are strong and dynamic types

- Strong and dynamic typing
Strong typing language raise error if one type is provided but not expected. Weak typing is not restrictive and perform conversion automatically. **Python is a strong typed language**
Dynamic typing embeds type information with the variable itself and variables can change types at runtime quite easily. static typing language cannot change variable type at runtime. Python is a dynamic typed language. 
- Duck typing
> If it walks like a duct and quacks like a duck, and if you are looking for things that walk and quack like ducks, then you can treat it as if it were a duck.
> 
Duck typing is about **adhering to interface**, instead of a kind of robust typing system. If duck typing is overused, we start to break down assumptions that a developer can rely upon when updating code. 

### Type annotation

We can conclude two main reasons for using type annotations: 1) *complicated or unintuitive function to be called by future users* or 2) *encoding intent or assumptions*

Importing and using annotation functions or variables:

```python
from typing import Optional, Union, Literal, NewType, Final
# function
def find_workers(open_time: datatime.datetime) -> list[str]:
# variable
characters: Literal["tom", "jerry"] = tom
```

### Single variable type annotations

Optional[type]

- optional indicates that variable can be a *given type or None.*
- It make the intent clear that we *need to beware None and handle exceptions* for the function call.
- Returning None should be avoided
None is convenient to return an exception
However, returning None requires handling those exceptions with a cost. So returning None should be avoided if possible.

Union[typeA, typeB]

- A Union type indicates that multiple types maybe used with the same variable
- Optional[type] is a special case of Union and is equivalent to Union[type, None]

Literal[value1, value2, ..., valueN]

- A literal type *hints* that variables values are restricted to a very specific set given
```python
from typing import Literal
letter: Literal["a", "b"] = 10
print(letter) >>> 10           
# type annotation is completely ignored in executation, but is used by code editor, eg. VSCode
```

NewType

- NewType take an existing type and return a new type that has all the same property but are identified as a different type.
- we can convert the types to our newly defined types by calling it
```python
# this illustrate an usage for NewType, to express the intent that HotDog's state is changed
ReadyToServeHotDog = NewType("ReadyToServeHotDog", HotDog) 
def prepare_for_serving(hotdog: HotDog) -> ReadyToServeHotDog:
hotdog.put_on_plate()
return ReadyToServeHotDog(hotdog)   
print(type(hotdog))
>>> HotDog # again, only annotation purpose, in VScode editor, hotdog is interpreted as ReadyToServeHotDog
```

Type Aliases

- Type alias just provides another name for a type and is used interchangeably with the old type, so type aliases does not produce a new type, for example: `myunion = Union[int, str]`

Final

- Final type tells the typechecker that a variable should not be bound to another value. It only has annotation function.
```python
b: Final = 20
b = 30    # Pylance: 'b' is declared as Final and cannot be reassigned
```    

### Collection type annotations

- Homogeneous vs heterogeneous collections
homogenity does not mean single type, but types that common behaviors are expected from them.
lists, sets and dictionaries should nearly always be homogeneous

Annotation collections

we can annotate list, set, tuple, dictionaries etc. using the square bracket syntax:

- e.g. `list[str]`
- For dictionary, we have `dict[str, int]` which is a dictionary mapping string to int
- square bracket can be used over each other: `list[Union[int, str]]`
- TypedDict can be used to specific heterogeneous datatypes in a dictionary

Points to notice when modifying existing types:

- When inheriting from python types, do not inherit from those types directly since python types may have unexpected behavior. We should inherit from UserType: from collections import UserDict, UserList, UserString
- The other option is to inherit from abc

## Part II. Defining your own types

Defining our own types help to communicates intentions by building a shared vocabulary

### Enum

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

### Data classes

dataclass provide similar but more functionality over namedtuples, they are appropriate when the data members within the dataclass are independent of one another. Functions belong to the dataclass can also created.

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

A number of options can be passed to data classes, For example(for more, refer to the reference)

- `eq`: If true (the default), an `__eq__()` method will be generated. This method compares the class as if it were a tuple of its fields, in order. Both instances in the comparison must be of the identical type.
If the class already defines `__eq__()`, this parameter is ignored.
- `order`: If true (the default is `False`), `__lt__()`, `__le__()`, `__gt__()`, and `__ge__()` methods will be generated. These compare the class as if it were a tuple of its fields, in order. Both instances in the comparison must be of the identical type. If `order` is true and `eq` is false, a `[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` is raised.

Ref [https://docs.python.org/3/library/dataclasses.html](https://docs.python.org/3/library/dataclasses.html)

### Classes

It helps to define the characteristic of class and when to use class by thinking about it’s difference with just a gathering of relational data:

- the data in a class depend on each other
- Class offer controlled initialization
- Class offer encapsulation (with ‘_’)

**Design of the class interfaces:** 

To get the most initutive and immediate understanding of the class functionality, we should design our interface as “controls and their movements” and let them be natural. For example, the definition of a class should adhere to how it is represented in real life. 

There are two ways to help systematically design an interface:

- Test-driven development
In test-driven development, we first design the tests (how the code should behave in practice), and write just enough code to pass that test. This improve our interface by thinking about how future users will use our code.
- Readme-driven development
We write a readme document and develop our code based on the readme documents.

**Class Protocols**

Protocols define a set of behaviors that objects may implement as a type. We can use protocols to provide an intention and extraction of ideas. *But as with other typing, it is not enforced in the executation*.

[https://docs.python.org/3.8/library/typing.html?highlight=protocol#typing.Protocol](https://docs.python.org/3.8/library/typing.html?highlight=protocol#typing.Protocol)

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

It’s true that there is a cost in adding all these type hinting to our codes, but it clearly express our intent and make future maintaince easier. 

## Part III. Extensible Python

- Shotgun surgery
If a single change spreads out and impacting a variety of files, it usually indicate a **shotgun surgery** and a moment to redesign. 

Accidental complexity and necessary complexity

- We should identify the necessary complexity and limit the interactions between them. Sometimes code seems to be complex, but it may due to necessary complexity: If we try to remove the complexity here, we can only put them somewhere else.
- Accidental complexity is the complexity that we can solve.

Open-Close principle: code should be open for extension and closed for modification. 

### Managing dependency

We have three types of dependency:

1. Physical dependency: refer to directly calling and using modules, to make physical dependence more managable, it is important to separate responsibilities of pieces of code and prevent redundency. 
2. Logical dependency: with logical dependencies, we do not directly call dependent code, but use data or objects to exchange information between different functionalities. Since codes are not directly called, it is more *substitutable*: we can swap out one code to another without needing to change other code. However, the trade off is that the code is less straight forward to understand unless we follow that data.
3. Temporal dependency: Temporal dependencies refer to cases where functionality depend on each other by time: some functionality use the result of another functionality. To increase robustness, we can use typing system to indicate such temporal relationship

Visualization

- There are tools to help us visualize dependencies: pipdeptree, GraphViz, pydeps
- Interpreting dependency graphs:
Fan-in: if a piece of code that is depended upon on much more than it depend on other codes, it is called a fan-in code. We want fan-in dependencies to be leaves and we want it to be stable and robust. 
Fan-out: if piece of code that depend heavily on other code a lot but is not depended upon. We typically want them to be easily to be modified according to our need.

### Composability

Policy vs Mechanism:

*Mechanism* is the implementation of the each individual functionality and *policy* is organized flow of each mechanism. 

In the ideal case, when mechanism is not tied to policy, we can change freely what our code do without changing each implementation. One way to achieve this is to make mechanism *composable*: 1) Type composition, 2) function composition (functional programming) and 3) algorithm composition are good tools that help to make the code more reusable and easy to extend. 

### Event-driven architecture

There are often a relationship between “producer” and “consumer” during the code executation. *Event driven architectures aim to decouple the producer from the consumer to achieve flexibility.*

PyPubSub is a tool that provide event driven architecture capcability by acting as a message broker: [https://pypubsub.readthedocs.io/en/v4.0.3/](https://pypubsub.readthedocs.io/en/v4.0.3/)

### Pluggability

Pluggability refer to the ability to swap one object for another, this can be achieved using *templates*, *protocols* or *abcs*

## Part IV. Building a safety Net

### statistic analysis

*Typechecker* and *linters* are the most easy tools to use for statistic analysis: they are the first defence for robust code. 

### Complexity checkers

Reducing complexity help to make the code more maintainable. One measure of complexity is the “cyclomatic complexity”, or the number of possible paths for the program executation. ([https://en.wikipedia.org/wiki/Cyclomatic_complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity))

Measuring complexity:

1. *mccabe* is a tool (python tool) that measures the cyclomatic complexity
2. As another simple measure, whitespace (indentations) can be used as an indicator for nested loops and branches.

### Testing

Test strategy

- Before writting tests, we should decide the *test strategies* by listing questions about the problem to solve and how solution is achieved. Tests should serve as a way to verify that the code is doing what you are expecting it to do.
- The “cost effective” tests should be run often, for example, tests for units that other codes depend on. The “less cost effective” tests can be run relatively less frequent, some test may not even worth to do.

Tools: pytest is a common library that provide testing functionalities

AAA testing pattern

A very common pattern of testing is the AAA test pattern, “Arrange-Act-Assert”, which can further follow annihilate, which clean up the some shared resource: file access, database, global variable, class variable etc.

For example, the following code shows AAA test pattern:

```python
def test_calorie_calculation_bacon_cheeseburger(): 
add_base_ingredients_to_database()                             # arrange
add_ingredient_to_database("Bacon", calories_per_pound=2400)   # arrange
setup_bacon_cheeseburger(bacon="Bacon")                        # arrange      
calories = get_calories("Bacon Cheeseburger w/ Fries")         # act (functionality that we test)
assert calories == 1200                                        # assertion
cleanup_database()                                             # annihilation
```

Another useful strategy in testing is to parameterize tests by letting test functions accept arguments that can be parameterized easily.

### Acceptance testing

While the above testing tests if the code is working without problem, acceptance testing checks if the code is *behaving as expected.* This is a process of “behavior-driven development” where we develop code aiming to achieve some certain desired behavior.  i.e. to reduce the mismatch between customer expectations and software behavior. 

GWT format

GWT (Given, when, then) format specifies a formal language to specift requirements of behavior. In GWT format, every requirement is organized as follows:

```
Feature: Vegan-friendly menu
Scenario: Can substitute for vegan alternative
Given an order containing a cheeseburger with fries
When  customer ask for vegan substitutions
Then  customer receive meal with no animal products
```

This format formalize the requirement in a form that both customer and developer can understand, and can be easily translated to tests.

Tools: behave is a python library that organize tests for the acceptance testing.

### Property based testing

Property based testing is a form of *generative testing* where tools generate test cased for you. This is especially useful to find problems in boundary values. 

- A useful tool in property based testing is hypothesis: Hypothesis library will automatically generate values for the test and carry out multiple tests with those automatic values and use searching tools (scheduling) to find which values lead to problems.
- The benefit of such testing strategy is that tests are not conducted in deterministic ways (not biased) and there are much better chance at finding bugs.

### Mutation testing