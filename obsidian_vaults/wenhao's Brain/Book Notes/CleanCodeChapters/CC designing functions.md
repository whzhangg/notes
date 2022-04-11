Chapter 3 of Clean Code, Martin Robert C.

### Rules for designing functions
**small**
>The first rule of functions is that they should be small. The second rule of functions is that they should be smaller than that.

Functions should be transparently obvious in their functions: functions should not be large enough to hold nested structures. (small complexity)

Each function should *do one thing* in the sense that they are a single level of abstraction. Since the reason we write function is to decompose a larger concept into a set of steps next level abstraction. 
- If a function can be divided into sections such as 'initializations', 'operations' etc. This function is trying to do too much things. A function that do one thing cannot be reasonably divided into sections.
- Mixing levels of abstraction within a function is always confusing in the logic. There should be a strong sense of hierarch in functions. 
- Don't repeat functionality.
- Follow Open Closed Principle so that functions are closed for future changes.
- Function should either do something or answer something, but not both (*command query separation*). Either a function should change the state of an object, or it should return some information about that object. Doing both leads to confusion. For example, this function is confusing: `boolean set(String attribute, String value)`

**No side effect**
Having side effects means that while your function seems to do one thing, it actually does hidden things. Having side effects breaks the *single responsibility principle*.
If we have to include side effects in an function, we should indicate it in the function name. 

**Function arguments design**

> the ideal number of arguments for a function is zero (niladic). Next comes one (monadic), followed closely by two (dyadic). Three arguments should be avoided when possible and more than three requires very special justification and shouldn't be used anyway. 

The point is that the more we have arguments, the more we have to remember them and the less clear our intention becomes.
- We should take the advantage of object oriented approach and reduce the number of arguments for function by making the function a method: For example, use `stream.writeField(name)` instead of `writeField(Stream, name)` 
- Two common situations to use single argument is 1) ask a question that argument or 2) using the function as an event.
- We should never pass boolean argument into function, which loudly proclaiming that this function is doing more than one thing.
- When a function seems to need more than two or three arguments, it is likely that some of these arguments ought be wrapped into a class of their own, or as a collection.

**Output arguments**
We should reduce using output arguments as much as we can. The need for output arguments disappears in OO languages because `this` is intended to act as output argument.

**Prefer exceptions to returning error codes**
There are two problems with returning error codes:
1. Returning error codes from functions is a violation of command query separation. 
2. Using error code forces caller to deal with the error immediately after the call, while using exceptions let error processing code separate from the normal code path. 

Error handling is one thing, so it should be handled by a single function.

**How to write good functions?**
>When I write functions, they come out long and complicated, ..., But I also have a suite of unit tests that cover every one of these clumsy lines of code.
> Then I massage and refine that code, splitting out functions, changing names, elimiating duplications. I shrink the methods and reorder them. Sometimes I break out whole classes, all the while keeping the tests passing.
> In the end, I wind up with functions that follow the rules. I don't write them the way to start, I don't think anyone could.

Clean code, Robert C. Martin, Chapter 4.