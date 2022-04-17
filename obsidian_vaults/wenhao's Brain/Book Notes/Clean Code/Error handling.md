Chapter 7 Error handling

### Error Handling
>Error handling is important, but if it obscures logic, it is wrong

##### Do not use error code
The problem of using error code is that it clutter the caller. The caller must immediately check and deal with the errors. For this reason, it is better to throw an exception when you encounter an error. Furthermore, the error handling and the normal execution flow are decoupled. 

##### Exceptions
When a piece of code require error handling, it is good practice to *start* with a try-catch-finally statement. This helps to define what the user of that code can expect consistently. 

Each exceptions we throw should provide enough context to determine the source and location of the error, using informative error messages.

There are two suggestions related to error handling:
1. Define the exception classes in terms of the *need of the caller*, so that the caller does not need to spend too much time dealing with errors generated. (This means that when using third party API, we should wrap the exceptions)
2. If possible, we should let class or objects handle the exception they have to encapsulate error handling. Ideally, the caller do not need to care about the detail of the error and deal with the exceptional behavior. This is called *Special case pattern*.

##### Don't return or pass Null
When we return Null, we are essentially creating work for ourselves and foisting problems upon the callers. If you are attempted to return a Null from a method, consider throwing an exception or returning a special case object instead. If a third part API return Null, wrap the method to throw an exception. 

Passing Null into methods is also a bad practice.If there is no good way to prevent passing Null from a caller, we can use *assertion*