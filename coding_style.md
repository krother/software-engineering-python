# PEP8 Code Style

As a programmer, you probably need to read code more often than to write. Naturally, every programmer is interested in readable code. Your own code, of course, is always readable. Or is it?

Fortunately, there a gold standard you can refer to. Python has a standard style guide for code, known as [PEP8](https://www.python.org/dev/peps/pep-0008). Adhering to PEP8 is good, because it makes your code readable for you and for others.

----

## pylint

The **pylint** tool checks whether your code conforms to the PEP8 coding guidelines. `pylint` is a powerful tool to analyze your code for readability and style.

Install it with

    pip install pylint

Then you can analyze any Python file:

    pylint my_program.py

Or all the files in a folder:

    pyling *.py

----

### The output of pylint

In the output of `pylint`, there are two sections to pay attention to:

* warning messages
* a code score at the very end

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

Functions and classes without docstrings are more difficult to understand. If you get a lot of docstring warnings your code may be hard to understand for someone else.

#### Variable names

    C:114,8:Renumerator.prepare_identifiers: Invalid name "fn" (should match [a-z_][a-z0-9_]{2,30}$)

Descriptive variable names are a big plus for code readability. Of course, it does not help much to replace **l** by **data_list** in order to satisfy pylint. But the name **fragment** tells you a lot more than **fn**.

#### Code modularization

Pylint helps to analyze modularization by printing warning messages:

    R: 19,0:Renumerator: Too many public methods (30/20)
    R: 32,4:Renumerator.letter_generator: Method could be a function
    R: 45,0:RNAResidue: Too many instance attributes (11/7)
    R:328,0:NucleotidePattern: Too few public methods (1/2)

Warnings about the number of classes / methods / functions indicate that the structure of the code needs improvement. These messages require some interpretation; don't try to fix all of them by force.

If you see a few warnings like these, don't worry. Only if you see them repeatedly, it may help readability to divide the code into units of more reasonable size.

To assess modularization of a program as a whole, pylint is not the right tool.

#### Code score

At the end of the pylint output you find a score of up to 10 points:

    Your code has been rated at 8.18/10

When you have fixed some of the issues, re-run pylint and see your score improve. The score directly measures your success and makes working with pylint very rewarding. 
You should generally aim to fix all the style issues so that your score becomes 10.0.
You don't need to fix every issue though. You may choose to ignore types of warnings that your team is not committed to. 

#### Ignore warnings

If you want to run `pylint` in a Continuous Integration system (e.g. in GitHub Actions), it must finish without warnings. 
Otherwise the CI will treat the style check as failed.
A good practice is to disable some types of warnings (those you and your team agree not to adhere to).

To ignore PEP8 warnings, create a file `.pylintrc` in your project directory. `pylint` finds it automatically. There you can list the types of warnings you would like to disable:

    [pylint]
      disable=C0103,C0111,line-too-long,too-few-public-methods

You can refer to the disabled messages either by their name or by a code. Both are in the `pylint` output.


## Some PEP8 guidelines

-   Indent blocks using four spaces (no tabs)
-   keep lines less than 80 characters long
-   separate functions with two blank lines
-   separate logical chunks of long functions with a single blank line
-   write constants in `UPPER_CASE`
-   write other variable and function names in `snake_case`
-   write classes in `CamelCase`
-   every function, class and module has a docstring

PEP8 is a *guideline*, not a lawbook.

----

## Also see:

* [How to write Pythonic Code](https://github.com/PyLadiesBerlin/materials/tree/master/12_how_to_write_pythonic_code)
* [Black](https://github.com/psf/black) - a program that converts your code to conform with PEP8
* [isort](https://github.com/timothycrosley/isort) - sorts your imports
