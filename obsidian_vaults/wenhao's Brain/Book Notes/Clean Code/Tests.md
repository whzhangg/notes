Chapter 9 Unit Tests

### Unit Tests

##### Test driven design (TDD)
Tests should be written in a timely fashion, Unit tests should be written *just before* the production code that is going to make them pass. Furthermore, we may not write more production code than is sufficient to pass the test.
>One of the best ways to ruin a program is to make massive changes to its structure in the name of improvement. Some programs never recover from such "improvement". The problem is that it's very hard to get the program working the same way it worked before the "improvement"
>--Chapter 14. Successive refinement

We should keep the system working all the time. It is not allowed to make a change to the system that breaks that system. Every change I make must keep the system working as it worked before. To do this, it is important use tests.

Also, see [The three laws of TDD](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd)

##### Keeping tests clean
It maybe tempting to write "dirty and quick" tests. But *having dirty tests is equivalent to, if not worse than, having no tests*. The problem is that tests must change as the production code evolves. The dirtier the tests, the harder they are to change. The more tangled the test code, the more likely it is that we spent time cramming new tests, more than it takes to write the new production code. 

>Test code is just as important as production code. It is not a second-class citizen. It requires thought, design and care. It must be kept as clean as production code. 

If you don't keep your tests clean, you will lose them. And without them, you lose the very thing that keeps your production code flexible. Without tests every change is a possible bug. No matter how flexible your architecture is, no matter how nicely partitioned your design. Without tests you will be reluctant to make changes because of the fear that you will introduce undetected bugs.

##### Write clean tests
Readability is the most important aspect in unit tests. To make tests readable, we can use functions and utilities that are designed specially for tests (our testing language) to help coders write their tests and who read them later. 
- Duel standard: tests should be simple and expressive, but it need not be as efficient as production code. 
- Build-Operate-Check pattern [[Robust Python]]
- Given-When-Then convention for the function names [[Robust Python]]
- Single concept per test

##### F.I.R.S.T principle
The F.I.R.S.T principle for tests is "Fast, Independent, Repeatable, Self-Validating and Timely"