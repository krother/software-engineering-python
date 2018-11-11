# Writing readable code with pylint

As a programmer, you probably need to read code more often than to write. Naturally, every programmer is interested in readable code. Your own code, of course, is always readable. Or is it? Is there a gold standard you can refer to?

Python has a standard style guide for code, known as [PEP8](https://www.python.org/dev/peps/pep-0008). Adhering to PEP8 is good, because it makes your code readable for others. It also helps you to write in a consistent style.

The **pylint** tool checks whether your code conforms to the PEP8 coding guidelines. pylint is a powerful tool to analyze your code for readability and style.

You can use it to analyze any Python file:

    pylint modomics.py

## The output of pylint
In the output of **pylint**, there are two sections to pay attenton to:

* Warning messages
* Code score

### Warning messages
At the top of the output from **pylint**, you find a section with warning messages. Each warning contains the line number the warning refers to:

    W:117,12:Template.prepare_identifiers: Unused variable 'x'
    C: 32,0: Line too long (88/80)
    C:134,16:Renumerator.get_identifiers_list: Operator not preceded by a space
    C:  1,0: Missing docstring
    C:114,8:Renumerator.prepare_identifiers: Invalid name "fn" (should match [a-z_][a-z0-9_]{2,30}$)

These warnings point you to the following issues:

#### Bugs and dead code

    W:117,12:Template.prepare_identifiers: Unused variable 'x'

This message indicates that line 117 either won't work or that the code has not been used at all.

#### Coding style

    C: 32,0: Line too long (88/80)
    C:134,16:Renumerator.get_identifiers_list: Operator not preceded by a space

Style issues regarding spaces, indentation and line lengths raised by pylint affect readability and are generally easy to fix.

#### Docstrings

    C:  1,0: Missing docstring

Functions and classes without docstrings are more difficult to understand. If you get a lot of docstring warnings your code may be hard to understand.

#### Variable names

    C:114,8:Renumerator.prepare_identifiers: Invalid name "fn" (should match [a-z_][a-z0-9_]{2,30}$)

Descriptive variable names are a big plus for code readability. Of course, it does not help much to replace **l** by **data_list** in order to satisfy pylint. But the name **fragment** tells you a lot more than **fn**.

#### Analyzing code modularization with pylint
Pylint helps to analyze modularization by printing warning messages:

    R: 19,0:Renumerator: Too many public methods (30/20)
    R: 32,4:Renumerator.letter_generator: Method could be a function
    R: 45,0:RNAResidue: Too many instance attributes (11/7)
    R:328,0:NucleotidePattern: Too few public methods (1/2)

Warnings about the number of classes / methods / functions indicate that the structure of the code needs improvement. These messages require some interpretation; don't try to fix all of them by force.

If you see a few warnings like these, don't worry. Only if you see them repeatedly, it may help readability to divide the code into units of more reasonable size.

To assess modularization of a program as a whole, pylint is not the right tool.

### Code score
In the third last paragraph of the pylint output you find a score of up to 10 points:

    Global evaluation
    -----------------
    Your code has been rated at 8.18/10

We find working with pylint very rewarding. You can start immediately to fix issues, re-run pylint and see your score improve. Just don't try to push every Python file to a score of 10.0. Usually a score above 7.0 is already good enough. It is OK to ignore warning messages you don't agree with. Use your reason, and see the table below:

| pylint score  | means              |
|---------------|--------------------|
| < 0.0         | trouble ahead      |
| 0.0 - 5.0     | needs cleanup      |
| 5.0 - 7.0     | reasonable quality |
| > 7.0         | great code!        |

Open source code metrics projects

    Radon is a tool for obtaining raw metrics on line counts, Cyclomatic Complexity, Halstead metrics and maintainability metrics.

    Pylint contains checkers for PEP8 code style compliance, design, exceptions and many other source code analysis tools.

    PyFlakes parses source files for errors and reports on them.

    Pyntch is a static code analyzer that attempts to detect runtime errors. It does not perform code style checking.

