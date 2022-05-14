# Extensible Python
### Writting extensible python
##### Shotgun surgery and necessary complexity
If a single change spreads out and impacting a variety of files, it usually indicate a shotgun surgery and a moment to redesign. 
    
Identify necessary complexity
We should identify the necessary complexity and limit the interactions between them. Sometimes code seems to be complex, but it may due to necessary complexity: If we try to remove the complexity here, we can only put them somewhere else.

##### Open-Close principle
code should be open for extension and closed for modification. 

### Dependency
##### Managing dependency
We have three types of dependency:
1. Physical dependency: refer to directly calling and using modules, to make physical dependence more managable, it is important to separate responsibilities of pieces of code and prevent redundency. 
2. Logical dependency: with logical dependencies, we do not directly call dependent code, but use data or objects to exchange information between different functionalities. Since codes are not directly called, it is more *substitutable*: we can swap out one code to another without needing to change other code. However, the trade off is that the code is less straight forward to understand unless we follow that data.
3. Temporal dependency: Temporal dependencies refer to cases where functionality depend on each other by time: some functionality use the result of another functionality. To increase robustness, we can use typing system to indicate such temporal relationship

##### Visualization of dependence
There are tools to help us visualize dependencies: pipdeptree, GraphViz, pydeps

Different types of code dependence:
- Fan-in: if a piece of code that is depended upon on much more than it depend on other codes, it is called a fan-in code. We want fan-in dependencies to be leaves and we want it to be stable and robust. 
- Fan-out: if piece of code that depend heavily on other code a lot but is not depended upon. We typically want them to be easily to be modified according to our need.

### Design
##### Composability
Policy vs Mechanism:
*Mechanism* is the implementation of the each individual functionality and *policy* is organized flow of each mechanism. 

In the ideal case, when mechanism is not tied to policy, we can change freely what our code do without changing each implementation. One way to achieve this is to make mechanism *composable*: 1) Type composition, 2) function composition (functional programming) and 3) algorithm composition are good tools that help to make the code more reusable and easy to extend. 

##### Event-driven architecture
There are often a relationship between “producer” and “consumer” during the code executation. *Event driven architectures aim to decouple the producer from the consumer to achieve flexibility.*

PyPubSub is a tool that provide event driven architecture capcability by acting as a message broker: [https://pypubsub.readthedocs.io/en/v4.0.3/](https://pypubsub.readthedocs.io/en/v4.0.3/)

##### Pluggability
Pluggability refer to the ability to swap one object for another, this can be achieved using *templates*, *protocols* or *abcs*