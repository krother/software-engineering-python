Testing
-------

#### The unittest framework

*unittest* is a Python framework for writing Unit, Integration and
Acceptance tests. It provides a class *TestCase *and a *main() *method.

from unittest import TestCase, main

#### Writing a test class

Test classes should extend *TestCase*, and contain at least one method
starting with test\_ that contains assertions. *TestCase* offers many
assertion methods (*assertEqual, assertAlmostEqual, assertTrue* etc.).
Optionally, the methods *setUp()* and *tearDown()* can be used to
prepare testing and clean up afterwards.

class AdditionTests(TestCase):\
 def test\_add(self):\
 self.assertEqual(add(3, 4), 7)

#### Running the tests

The *unittest.main* method will look for all classes derived from
*TestCase* that have been defined in imported modules. It runs all tests
inside them and reports. Typically, you will find *main()* called in a
separate code block:

if \_\_name\_\_ == '\_\_main\_\_':

 main()

#### Testing command-line scripts

To test a command-line script call it using a shell command and redirect
the output for further evaluation:

import os

os.system('python myprog.py &gt; out.txt')

#### Other test frameworks in Python

nose – similar to unittest but less code

py.test – similar to unittest but less code

**doctest** – tests written to documentation strings

**django.test** – web testing inside Django based on unittest

### Automatic tests
Ideally, you should be able to reproduce previous research results before producing your own. How can you verify that the program is working? Automatic tests help you do that quickly.

Questions you can ask include:
* Are there any automatic tests?
* Do all tests pass?
* Is there a test suite that lets you run tests with a single command?
* Do the tests contain example data?
* Is there a way to reproduce results from a related publication quickly?

To assess the quality of tests, we will have a closer look at test coverage.

### Advantages of Unit Testing

-   You have full certainty what a function returns.
-   Forces to have a well-structured program.
-   Always works for the tested cases.
-   Before coding you already know what the program should do.
-   You think about nasty examples.
-   Bugs you fixed once (with adding new tests do not repeat).
-   Code is more durable and easier to maintain.
-   Speeds up refactoring.

### Disadvantages of Unit Testing

-   Time consuming (the benefit comes during debugging, but only above a
    certain level of complexity)
-   Before writing a program, one needs to know what precisely the
    program should do (sometimes its better to write a prototype first).
-   One cannot be sure that the tests cover all nasty examples that
    appear in real life.
-   Additional code to write.
-   Quality depends on the test examples.
-   Some functions are difficult to test (web scripting, random numbers)
    or even impossible (graphical user interfaces).
