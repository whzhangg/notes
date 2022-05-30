# Robust code
### Robustness
##### Clean code for communication
Writting clean and maintainable code is ultimately for communication, we need to be able to communicate our intent with future developers as well as future selves. Without a *clear intent* in our code, there is no communication to the future and productivity is lost.

##### Law of least surpriss
A program should always respond to the user in the way that astonishes them the least (WTFs): surprising behavior leads to confusion, which leads to misplaced assumptions and bugs.

##### Necessary and accidental complexity
*Necessary complexity* is the complexity that is inherit in the problem, but *accidental complexity* is the complexity in inefficient organization that produce wasteful or confusing code. 

If the following things happen, you have accidental complexity:
1. things that sound simple are non-trival to implement.
2. Difficulty to let others to understand your code

> You own it to feature maintainers to enable them to deliver value at the same speed that you can today, Otherwise, your codebase will get bloated, schedules will slip and complexity will grow. It is your job as a developer to mitigate that risk.

### Expressing intent with types
Pick the right collection for the task at hand:
##### List
To be iterated over, rarely retrieving specific elements in the middle with duplicates allowed.    
##### Generator
To be iterative over but never indexed into, with lazy access.
##### Tuple
An immutable collection that rarely iterated over, and specific elements can be extracted easily.
##### set
Iterable collection with no order and no duplicates
##### Dictionary
mappers