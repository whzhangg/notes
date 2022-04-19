### Classes
>But for all the attention to the expressivemess of code statements and functions they comprise, we still don't have clean code until we've pay attention to higher levels of code organization, Let's talk about clean classes.

##### Public variables are not good!
There should seldom a good reason to have a public variable, because we don't want to expose the internals of the objects for *encapsulation*

##### Single responsibilities rule for classes
The name of the class should describe what responsibilities it fulfills. Name should be the first way to help determine the class size. The more ambiguous the class name, the more likely it has too many responsiblities. 

We should be able to write a brief description of the class in short words, without using the words *if*, *and*, *or* or *but*. Existance of any these words suggest that the class has too many responsibilities. 

##### Class should be small
If we follow the single responsibility rule for classes, we would end up with many small classes. 
>Many developers fear that a larger number of small, single-purpose classes make it more difficult to understand the bigger picture. ...
>
>However, a system with many smaller classes has no more moving parts than a system with a few large classes. There is just as much to learn in the system with a few large classes. ...
>
>Every sizable system will contain a large amount of logic and complexity. The primary goal in managing such complexity is to organize it so that a developer knows where to look to find things ...

##### Cohersion
In general, the more variables a method manipulates, the more cohesive that method is with respect to its class. A class is maximally cohesive if each method manuipulate all variables.

Following the single responsibility rule, we have the following method to break large class into small ones:
1. If a subset of class variables are repeatedly used together by class functions, it is likely that we can extract a class from them.
2. If then a few functions solely operate this object, it means that the class lose cohesion and we should split these function into a separate class.

##### Organizing for change
Class design should follow open-closed principle (OCP)

To be robust against changes, we should write our code depending upon abstract classes, depending upon concrete details is risky when these details change. We should introduce interfaces or abstract classes to help isolate the impact of those details. This is *Dependency Inversion Principle(DIP)*: abstraction should not depend on details. Details should depend on abstraction.


