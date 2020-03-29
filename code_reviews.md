
# Code Reviews

A **Code review** means that another person reads your code. This could be:

* a senior engineer
* a programmer with similar experience
* a junior developer

All three provide complementary feedback that is useful in many ways. Besides discovering bugs, they also expose general design weaknesses (that might become bugs in the future) or simply learn you alternative/better ways to solve the problem.

Because of that, many engineers see code reviews as the **number one technique to build high-quality software.**

## Example checklist for code reviewers

Sometimes, reviewers use a checklist or other formal protocol, especially when safety/security is important.

* Does the module header explain understandably what the code does?
* Does the module header contain a year and a copyright notice?
* Are all import statements listed right after the header
* Are constants listed right after the import statements?
* Are constants written in uppercase?
* Does each function have a docstring?
* Is the documentation understandable?
* Are the class and method names well-chosesn?
* Are the variable names well-chosen (no one-letter acronyms except for i in range(10):)?
* Is the code formatted in a consistent way?
* Are there code duplications?
* Are there code sections that should be replaced by calls to a standard module?
* Is there dead code that does nothing?
* Are there code sections that are unnecessarily long?
* Are there endless while loops?
* Are there break statements?
* Are there nested sections on the 4th level of indentation or deeper?
* Are recursive procedures described as such in the docstring?
* Do all methods/functions have one way to return data (EITHER by return value OR by modifying an object, not both).
* Is the order of methods/classes/functions bottom-up (small-scale classes first, and classes that use/wrap them after that).
* Does the module contain a __main__ section that is reasonably short?
