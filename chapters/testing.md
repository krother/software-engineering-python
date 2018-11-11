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
