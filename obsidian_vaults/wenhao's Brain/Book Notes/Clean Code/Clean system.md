### Systems
(here the author spend time focusing on Java, so I didn't write down much notes)

>Software systems should separate the startup process, when the application objects are constructed and the dependencies are "wired" together, from the runtime logic that takes over after startup

##### Dependencies
Following Single Responsibility Principle, an object should not take responsibility for instantiating dependencies itself. Instead, it should pass this responsibility to another mechanism, thereby inverting control. 

##### Decision making
It's a good strategy to postpone decision making until the last possible moment. It let's us to make more informed choices with the best possible information. 

### Emergence
(chapter 12)
##### Kent Beck's four rules of Simple Design:
A design is simple if it follows these rules, in order of importance:
1. Runs all the tests
2. Contains no duplication
3. Expresses the intent of  the programmer
4. Minimizes the number of classes and methods

Again, tests are important:
- Making the system testable pushes us towards a design where our classes are small and single purpose,
- The more tests we write, the more we need to use princples like SRP, DIP, interface etc. thereby minimizing coupling,

Expressing intent: 
>The most important way to be expressive is to try.

Minimizing system:
Our goal is to keep our overall system small, while we are also keeping the functions and classes small.