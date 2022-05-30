### Smells and Heuristics
##### Comments
*Bad smell*: Inappropriate information
*Bad smell*: Obsolete comment
*Bad smell*: Redundant comment
*Bad smell*: Poorly written comment
*Bad smell*: Commented-out code
##### Environment
*Bad smell*: Build requires more than one step
*Bad smell*: Tests require more than one step
##### Funtions
*Bad smell*: Too many arguments
*Bad smell*: Output arguments
*Bad smell*: Flag arguments
*Bad smell*: Dead functions
##### General
*Bad smell*: Multiple languages in one source file
*Bad smell*: Obvious behavior is unimplemented
*Bad smell*: Incorrect behavior at the boundaries (don't rely on initions, test the boundaries)
*Bad smell*: Overridden safeties
*Bad smell*: Duplication
*Bad smell*: Code at wrong level of abstraction
*Bad smell*: Too much information (use small interface!)
*Bad smell*: Contain dead code
*Bad smell*: Bad vertical separation
*Bad smell*: Inconsistency (stick to your conventions)
*Bad smell*: Clutters (keep things short and clean)
*Bad smell*: Artificial Coupling for convenience
*Bad smell*: Feature Envy (a class is trying to use the internals of another class)
*Bad smell*: Selector arguments
*Bad smell*: Obscured intent
*Bad smell*: Misplaced responsibility (code should be where you expect to find it)
*Bad smell*: Inappropriate static
*Heuristics*: Use Exlanatory Variables
*Heuristics*: Function names should say what they do
*Heuristics*: Understand the algorithm (understand how code works)
*Heuristics*: Prefer polymorphism to If/Else statement
*Heuristics*: Follow standard convention
*Heuristics*: Repace magic numbers with named constants (bad idea to have raw numbers in code)
*Heuristics*: Be precise (be about the reason and consequency of your decision)
*Heuristics*: Structure over convention (use structure to enforce convention)
*Heuristics*: Encapsulate conditionals
*Heuristics*: Avoid negative conditionals
*Heuristics*: Functions should do one thing
*Heuristics*: Don't be arbitrary (structure code based on reasons)
*Heuristics*: Encapsulate boundary conditions
*Heuristics*: Functions should descend only one level of abstraction
*Heuristics*: Keep configurable data at high level (pass it as arguments)
*Heuristics*: Avoid transitiev navigation
##### Names
*Bad smell*: Unambiguous names
*Heuristics*: Choose descriptive names
*Heuristics*: Choose names at the appropriate level of abstraction
*Heuristics*: Use standard nomenclature where possible
*Heuristics*: Use long names for long scopes
*Heuristics*: Avoid encodings
*Heuristics*: Names should describe side-effects
##### Tests
*Bad smell*: Insufficient tests
*Heuristics*: Use a coverage tool
*Heuristics*: Don't skip trivial tests
*Heuristics*: An ignored test is a question about an ambiguity
*Heuristics*: Test boundary conditions
*Heuristics*: Exhaustively test near bugs
*Heuristics*: Patterns of failure are revealing
*Heuristics*: Test coverage patterns can be revealing
*Heuristics*: Test should be fast