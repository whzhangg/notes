Chapter 6 of Clean Code, Martin Robert C.

### Objects and Data Structures

**Data abstraction**

We should not expose the implementation of an object. Hiding implemenation is about abstractions. Hiding implementation is *not* about wrapping its variables in getters or setters. Instead, we should only exposes abstract interfaces that all users to manipulate the essence of the data, without having to know its implementation. In the abstract case you have no clue at all about the form of the data. *This is really the purpose of abstraction*.
>Abstraction: the quality of dealing with ideas rather than events -- dictionary

**Choosing between Data structure and Objects**
Objects hide their data behind abstractions, while data structure expose their data but provide no meaningful functions. They are *virtual opposites*.
- With data structures, it is easy to add new functions that treat them without changing the existing datastructure. But hard to add new data structure since all functions related must be changed to consider the new data structure.
- With objects, it is easy to add new classes without changing existing functions (class methods), but it is difficult to add new functionalities because all classes must change.
- *Hybrids* that is half object and half data structure should be avoided since it is hard to add new functions or add new datastructures. They are the worst of both worlds.

In complex system, there are times when one is more suitable than the other. 

**Hiding structure**
Hiding internal structure means we should know how data is managed within the object. We should be telling the object to *do something*; we should not asking it about its internals. 
If we find ourself writting a piece of code that retrive information from an object, we should ask why do we need that information, and *ask object to do it for us*.

