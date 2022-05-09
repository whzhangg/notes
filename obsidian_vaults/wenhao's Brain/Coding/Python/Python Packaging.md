### Convention of python testing
This is my convention for writing tests, gathered from a few different sources
Source 1: [Pragmatic AI Labs and Solutions, Testing in Python](https://paiml.com/docs/home/books/testing-in-python/)

##### Directories
Put the `tests` directory under the package folder, and organize the layout in the `tests` folder to mimic that of the project. For example:
```shell
├── setup.py
└── skeleton
    ├── __init__.py
	├── functional
	├── unit
	├── interface.py
    └── tests
        ├── test_imports.py
		├── test_interface.py
        ├── functional
        │   └── test_functional.py
        └── unit
            └── test_unit.py
```

##### Test functions
*Important functionality should be tested*, the results should be compared to the result that can be manually checked. 

*Data files that contain constants should be tested always*. They usually form the basis of the rest of the program and we cannot afford to contain mistakes in their values

