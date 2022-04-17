
# Building a safety Net
### Analysis
##### Statistic analysis
*Typechecker* and *linters* are the most easy tools to use for statistic analysis: they are the first defence for robust code. 

##### Complexity checkers
Reducing complexity help to make the code more maintainable. One measure of complexity is the “cyclomatic complexity”, or the number of possible paths for the program executation. https://en.wikipedia.org/wiki/Cyclomatic_complexity

Measuring complexity:
1. *mccabe* is a tool (python tool) that measures the cyclomatic complexity
2. As another simple measure, whitespace (indentations) can be used as an indicator for nested loops and branches.

### Code Testing
##### Test strategies
Before writting tests, we should decide the *test strategies* by listing questions about the problem to solve and how solution is achieved. Tests should serve as a way to verify that the code is doing what you are expecting it to do.

The “cost effective” tests should be run often, for example, tests for units that other codes depend on. The “less cost effective” tests can be run relatively less frequent, some test may not even worth to do.

*Tools*: pytest is a common library that provide testing functionalities

##### AAA testing pattern
A very common pattern of testing is the AAA test pattern, “Arrange-Act-Assert”, which can further follow annihilate, which clean up the some shared resource: file access, database, global variable, class variable etc.

For example, the following code shows AAA test pattern:
```python
def test_calorie_calculation_bacon_cheeseburger(): 
		add_base_ingredients_to_database()                             # arrange
		add_ingredient_to_database("Bacon", calories_per_pound=2400)   # arrange
		setup_bacon_cheeseburger(bacon="Bacon")                        # arrange      
		calories = get_calories("Bacon Cheeseburger w/ Fries")         # act (functionality that we test)
		assert calories == 1200                                        # assertion
		cleanup_database()                                             # annihilation
```
Another useful strategy in testing is to parameterize tests by letting test functions accept arguments that can be parameterized easily.

### Acceptance testing
While the above testing tests if the code is working without problem, acceptance testing checks if the code is *behaving as expected.* This is a process of “behavior-driven development” where we develop code aiming to achieve some certain desired behavior.  i.e. to reduce the mismatch between customer expectations and software behavior. 

##### GWT format
GWT (Given, when, then) format specifies a formal language to specift requirements of behavior. In GWT format, every requirement is organized as follows:
```
Feature: Vegan-friendly menu
Scenario: Can substitute for vegan alternative
  Given an order containing a cheeseburger with fries
  When  customer ask for vegan substitutions
  Then  customer receive meal with no animal products
```
This format formalize the requirement in a form that both customer and developer can understand, and can be easily translated to tests.

*Tools*: behave is a python library that organize tests for the acceptance testing.

### Property based testing
Property based testing is a form of *generative testing* where tools generate test cased for you. This is especially useful to find problems in boundary values. 

A useful tool in property based testing is hypothesis: Hypothesis library will automatically generate values for the test and carry out multiple tests with those automatic values and use searching tools (scheduling) to find which values lead to problems.

The benefit of such testing strategy is that tests are not conducted in deterministic ways (not biased) and there are much better chance at finding bugs.