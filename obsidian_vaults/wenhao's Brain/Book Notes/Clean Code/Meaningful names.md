Chapter 2. Clean Code, Martin Robert C.

### Meaningful names
##### Variables names
1. Use intention-revealing names for variable, function or class, which should tell you why it exists, what it does and how it should be used. Bad naming make the code *implicity*.
2. We should avoid leaving false clues in function names that obscure the meaning of the code. Information exists in the patterns of our naming, while disinformation is the inconsistency that break these patterns. 
3. We should make meaningful distinctions between variables, and avoid using number series (a1, a2, ...) or noise words, for example, use "account" instead of "accountData".
4. Pronounceable names are more convenient to use because *programming is a social activity*.
5. We should try to use searchable names so that we can easily locate the variable anywhere is the body of the code. Short, single-letter names should only be used as local variables inside short functions.
6. The length of the variable name should correspond to the size of its scope.

##### Method names
1. Methods should have names corresponding to what they do. For example, methods should have verb or verb phrase names. 
2. Pick one word per concept. For example, choose one of "fetch", "retrieve" and "get" and use them consistently. 
3. Use domain specific names that others are instantly familiar with.
Adding meaningful context to names if these names are not meaningful by themselves. 
