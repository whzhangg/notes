# Fluent Python
Created: October 25, 2021 7:25 PM
Description: This is the reading notes on more advanced tips concerning the python language

**This notes covers the underlying python building blocks with emphasis on the object natural of python data and designing Pythonic objects following the python data model**

Useful references:
1. [[zen of python]]
2. [Python Glossary](https://docs.python.org/3/glossary.html#glossary)

[[The Data model]]
[[Sequence type]]
[[Dictionaries and sets]]
[[Text and bytes]]
[[Functions as objects]]
[[Object references and mutability]]
[[Pythonic Object]]
[[Inheritance]]
[[Interfaces, Protocols and ABCs]]
[[Operator Overloading]]
[[Iterables iterators and generators]]

### Decprecation warnings
```python
if normalization is not None:
	warnings.warn(
		"`normalization` is deprecated. Use `irrep_normalization` instead.",
		DeprecationWarning
	)
irrep_normalization = normalization
```