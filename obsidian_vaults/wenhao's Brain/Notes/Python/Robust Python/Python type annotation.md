
# Annotating your code with types
### Python types
Python types are strong and dynamic types
- *Strong typing* language raise error if one type is provided but not expected. Weak typing is not restrictive and perform conversion automatically. *Python is a strong typed language*.
- *Dynamic typing* embeds type information with the variable itself and variables can change types at runtime quite easily. static typing language cannot change variable type at runtime. Python is a dynamic typed language. 

##### Don't overuse Duck typing
Duck typing is about *adhering to interface*, instead of a kind of robust typing system. If duck typing is overused, we start to break down assumptions that a developer can rely upon when updating code. 

> If it walks like a duct and quacks like a duck, and if you are looking for things that walk and quack like ducks, then you can treat it as if it were a duck.
    
### Using type annotation
We can conclude two main reasons for using type annotations: 
1. clarify complicated or unintuitive function to be called by future users,
2.  encoding intent or assumptions.

Importing and using annotation functions or variables:
```python
from typing import Optional, Union, Literal, NewType, Final
# function
def find_workers(open_time: datatime.datetime) -> list[str]:
# variable
characters: Literal["tom", "jerry"] = tom
```

### Single variable type annotations
##### Optional[type]
Optional indicates that variable can be a *given type or None*. It make the intent clear that we *need to beware None and handle exceptions* for the function call.

Returning None should be avoided:
- Returning None requires handling those exceptions with more cost. So returning None should be avoided if possible.

##### Union[typeA, typeB]
A Union type indicates that multiple types maybe used with the same variable. Optional[type] is a special case of Union and is equivalent to Union[type, None]

##### Literal[value1, value2, ..., valueN]
A literal type *hints* that variables values are restricted to a very specific set given
```python
from typing import Literal
letter: Literal["a", "b"] = 10
print(letter) 
>>> 10           
# type is used by code editor, not by python
```
    
##### NewType
NewType take an existing type and return a new type that has all the same property but are identified as a different type.

We can convert the types to our newly defined types by calling it
```python
# this illustrate an usage for NewType
ReadyToServeHotDog = NewType("ReadyToServeHotDog", HotDog) 
def prepare_for_serving(hotdog: HotDog) -> ReadyToServeHotDog:
    hotdog.put_on_plate()
    return ReadyToServeHotDog(hotdog)   
print(type(hotdog))
>>> HotDog # again, it only annotation purpose
```
    
##### Type Aliases
Type alias just provides another name for a type and is used interchangeably with the old type, so type aliases does not produce a new type, for example: `myunion = Union[int, str]`

##### Final
Final type tells the typechecker that a variable should not be bound to another value. It only has annotation function.
```python
b: Final = 20
b = 30    # Pylance: 'b' is declared as Final and cannot be reassigned
```    

### Collection type annotations
Homogeneous vs heterogeneous collections: Collections should be homogeneous. *Homogenity does not mean single type*, but types that common behaviors are expected from them. Lists, sets and dictionaries should nearly always be homogeneous

we can annotate list, set, tuple, dictionaries etc. using the square bracket syntax:
- e.g. `list[str]`
- For dictionary, we have `dict[str, int]` which is a dictionary mapping string to int
- square bracket can be used over each other: `list[Union[int, str]]`
- TypedDict can be used to specific heterogeneous datatypes in a dictionary

##### When modifying existing types
When inheriting from python types, *do not inherit from those types directly* since python types may have unexpected behavior. We should inherit from UserType: from collections import UserDict, UserList, UserString. We can also inherit from abcs
