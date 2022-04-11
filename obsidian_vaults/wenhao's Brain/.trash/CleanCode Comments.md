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