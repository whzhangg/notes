# Clean code
Robert C. Martin, started reading at April, 7th, 2022

### Writting clean codes
Introduction by [James O. Coplien](https://en.wikipedia.org/wiki/Jim_Coplien)
>Honesty in small things is not a small thing. 

Clean code emphasis on *maintenance* rather than one *production*. The roots of responsibile professionalism in a profession should concern the life cycle of a product. We should not wait for break down or bugs to surface. This should be the exception. Rather, we should inspect the machine every day and fix wearing parts before they break, and eventually replacing the old machine with the new ones. 

>A Poem is never done and bears continual rework, and to stop working on it is adandonment. Such preoccupation with detail is common to all endeavors of excellence. 

Style distinguishes excellence from mere competence. Quanlity is the result of a million selfless acts of care--not just of any great method that descends from heavens. That these acts are simple doesn't mean that they are simplistic, and it hardly means that they are easy. The are nonetheless the fabric of  greatness and of beauty in any human endeavor. 

>Neither architecture nor clean clean code insist on perfection, only on honesty and doing the best we can.

**Attitude**
This paragraph discussed the attitude towards writing clean code

>Have you ever waded through a mess so grave that it took weeks to do what should have taken hours? Have you seen what should have been a one-line change, made instead in hundreds of different modules? These symptoms are all too common.
>
>Why does this happen to code? Why does good code rot so quickly into bad code? We have lots of explanations for it. We complain that the requirements changed in ways that thwart the original design. We bemoan the schedules that were too tight to do things right. We blather about stupid managers and intolerant customers and useless marketing types and telephone sanitizers. *But the fault, dear Dilbert, is not in our stars, but in ourselves. We are unprofessional.*
>
>This may be a bitter pill to swallow. How could this mess be our fault? What about the requirements? What about the schedule? What about the stupid managers and the useless marketing types? Don’t they bear some of the blame?
>
>No. The managers and marketers look to us for the information they need to make promises and commitments; and even when they don’t look to us, we should not be shy about telling them what we think. The users look to us to validate the way the requirements will fit into the system. The project managers look to us to help work out the schedule. We are deeply complicit in the planning of the project and share a great deal of the responsibility for any failures; especially if those failures have to do with bad code!
>
>“But wait!” you say. “If I don’t do what my manager says, I’ll be fired.” Probably not. Most managers want the truth, even when they don’t act like it. Most managers want good code, even when they are obsessing about the schedule. *They may defend the schedule and requirements with passion; but that’s their job. It’s your job to defend the code with equal passion.*
>
>To drive this point home, what if you were a doctor and had a patient who demanded that you stop all the silly hand-washing in preparation for surgery because it was taking too much time? Clearly the patient is the boss; and yet the doctor should absolutely refuse to comply. Why? Because the doctor knows more than the patient about the risks of disease and infection. It would be unprofessional (never mind criminal) for the doctor to comply with the patient.
>
>So too it is unprofessional for programmers to bend to the will of managers who don’t understand the risks of making messes.

**Boy Scout Rule**
Leave the campground cleaner than you found it.

### Meaningful names
**Variables names**
1. Use intention-revealing names for variable, function or class, which should tell you why it exists, what it does and how it should be used. Bad naming make the code *implicity*.
2. We should avoid leaving false clues in function names that obscure the meaning of the code. Information exists in the patterns of our naming, while disinformation is the inconsistency that break these patterns. 
3. We should make meaningful distinctions between variables, and avoid using number series (a1, a2, ...) or noise words, for example, use "account" instead of "accountData".
4. Pronounceable names are more convenient to use because *programming is a social activity*.
5. We should try to use searchable names so that we can easily locate the variable anywhere is the body of the code. Short, single-letter names should only be used as local variables inside short functions.
6. The length of the variable name should correspond to the size of its scope.

**Method names**
1. Methods should have names corresponding to what they do. For example, methods should have verb or verb phrase names. 
2. Pick one word per concept. For example, choose one of "fetch", "retrieve" and "get" and use them consistently. 
3. Use domain specific names that others are instantly familiar with.
Adding meaningful context to names if these names are not meaningful by themselves. 

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
### Comments
>So when you find yourself in a position where you need to write a comment, think it through and see whether there isn't some way to turn the tables and express yourself in code. Every time you express yourself in code, you should pat yourself on the back. Every time you write a comment, you should grimace and feel the failure of your ability of expression.
>Truth can only be found in one place:  the code. Only the code can truly tell you what it does. It's the only source of truely accurate information. 

**Good comments**
- Legal information
- Informative comments
- Explanation of intent
- Clarifications
- Warning of consequences
- TODO comments
- Doc strings

**Bad comments**
- Mumbling without paying much attention
- Redundant comments
- Misleading comments
- Noise comments
- Journal comments (time stamps and history)
- Commented-out code, which cause confusion
- Nonlocal information
- Too much information
- Inobivous comments

Chapter 5.
### Formatting
>Code formatting is about communication, and communication is the professional developer's first order of business. 

A well written source file should has name, by itself, sufficient to tell us whether we are in the right module or not. The topmost parts should provide high-level concepts and algorithms. Details should increase as we move downward.

We can use one of the following formating rules:
1. Vertical openness: use blank lines to separate different concepts and throughts.
2. Tightly related code should appear vertically dense.
3. Vertical separtion between different lines should be a measure of how important each is to the understandability of the other. Following this principle, Variables should be declared as close to their usage as possible. 
4. If a function call another, they should be vertically close. The caller should be above the callee if possible.
5. Clear and consistent intentation, and clear horizontal openness. (use single white to accentuate order and relationship)