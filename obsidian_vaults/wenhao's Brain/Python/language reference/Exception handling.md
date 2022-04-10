# Exception handling
Created: October 21, 2021 11:39 AM
### Try ... except
reference: https://docs.python.org/3/tutorial/errors.html

Standard use case
```python
try:
	normal()
except Error1:
	handle_specific_error()
except Error2:
	handle_error2()
```

Clean up with `else` in the case without error
```python
try:
	start_up()
except Error:
	handle_error()
else:
	clean_up()
```

Clean up with `finally`:
if a `finally` clause is present, the `finally` clause will execute as the last task before try statement completes. The `finally` clause will run whether or not try statement produces an exception, if an exception is occured, the `finally` will run first before the exception is raised.
```python
try:
		raise keyboardInterruption
finally: 
		print('Goodbye, world')

# will print in all cases
```

### Types of definied exceptions
reference: https://docs.python.org/3/library/exceptions.html#BaseException

- `AssertionError`: Raised when an `assert` statement fails.
- `AttributeError`: Raised when an attribute reference or assignment fails. (When an object does not support attribute references or attribute assignments at all, `TypeError` is raised.)
- `EOFError`: Raised when the `input()` function hits an end-of-file condition (EOF) without reading any data. (N.B.: the `io.IOBase.read()` and `io.IOBase.readline()` methods return an empty string when they hit EOF.)
- `ImportError`: Raised when the `import` statement has troubles trying to load a module. Also raised when the “from list” in `from ... import` has a name that cannot be found.
- `ModuleNotFoundError`: A subclass of `ImportError` which is raised by `import` when a module could not be located. It is also raised when `None` is found in `sys.modules`.
- `IndexError`: Raised when a sequence subscript is out of range. (Slice indices are silently truncated to fall in the allowed range; if an index is not an integer, `TypeError` is raised.)
- `KeyboardInterrupt`: Raised when the user hits the interrupt key (normally Control-C or Delete). During execution, a check for interrupts is made regularly. The exception inherits from `BaseException` so as to not be accidentally caught by code that catches `Exception` and thus prevent the interpreter from exiting.
- `NameError`: Raised when a local or global name is not found. This applies only to unqualified names. The associated value is an error message that includes the name that could not be found.
- `NotImplementedError`: This exception is derived from `RuntimeError`. In user defined base classes, abstract methods should raise this exception when they require derived classes to override the method, or while the class is being developed to indicate that the real implementation still needs to be added.