chapter 8. Boundaries

### Boundaries
>Code at the boundaries needs clear separation and tests that define expections. We should avoid letting too much of our code know about the third-party APIs. It's better to depend on something you control than on something you don't control, least it end up controlling you.

##### Third party API
We should realized the tension between provider of an interface, for board application, and our own particular need. To get around the conflict, the best practice is to wrap the third party code using our own interfaces. A good indication for the need of an interface is when we have to write the same post treatment after calling the API, over and over through the code. 

Learning tests:
A good way to learn the behavior of the third party API is to write behavior tests for the APIs. Not only it help us to learn behavior of the API, it also help us go through the version change and updates by checking if there are any hehavorial difference.

##### Using code that does not yet exist
When there are some part of code, or subsystem, that is completely unknown to us (boundary between known and unknown), a good idea is to *write down the interface that we wish to have* and define our code according to these interfaces, so that the interface is in our control. When the API was defined, we can then write adapters to bridge the gap.

