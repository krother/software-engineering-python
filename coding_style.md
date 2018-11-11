Coding Style
------------

### Good function style

-   Arguments for input only.
-   Return statement for output only.
-   No global variables.
-   One function serves exactly one purpose.
-   Write documentation string first.
-   keep functions small (&lt;100 lines of code)
-   If you have too many parameters, make a new class.
-   Do not mix mutable types and return output.

### Bad Programming Style

1.  Not writing comments
2.  Writing unstructured code
3.  Using global variables
4.  Using jump commands (break, continue)
5.  Using private methods & nested functions
6.  Catching too many Exceptions
7.  Making cyclic references (also see \#8.)
8.  Also see \#7.
9.  Mixing TABs and whitespace for indentation (only use 4 spaces!)

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

# Codeanalyse

Einige Tools prüfen Programmcode auf stilistische Schwächen und verhindern dadurch oft Fehler. Wichtige Tools dazu in Python sind `pylint`, `mypy` und `isort`.


Coding guidelines
=================

-   Write lots of comments

    -   -   Each class, module and function needs a docstring.
        -   Write comments with \# in a separate line above the code you
            refer to
        -   All comments in English\

-   Use the **unittest** module for writing tests\
-   Use the **optparse** module for processing command-line arguments\
-   use for wrapper function (Marcin's getCommandOutput) ?\
-   Calling external programs by ...\
-   To avoid code duplication:

1.  Use standard classes for Sequences, Alignments,
    BLAST/PSI-BLAST/FASTA and NCBI parsers from the
    [PyCogent](https://www.genesilico.pl:8888/PyCogent) library
    whenever possible.
2.  Use other existing Python class<span id="anchor"></span>Use other
    existing Python classes, but not from BioPython
3.  Write your own

-   For external services

1.  Download something from the web
2.  Wrap a local non-Python tool. NCBI Eutils are in PyCogent already.
3.  Use a web service, unless it has to be called 1000+ times. <span
    id="anchor-1"></span>Use a web service, unless it has to be called
    1000+ times.

Code formatting:

-   Indent blocks using four spaces (No Tabs, do not use Gedit).
-   Keep lines less than 80 characters long
-   Separate functions with two blank lines
-   Separate logical chunks of long functions with a single blank line

<!-- -->

CONSTANTS\_IN\_CAPITALS = 'Spam'

class ClassNamesLikeInWiki:

def method\_names\_with\_underscores(self):

pass

def functions\_like\_methods():

variables\_with\_underscores = True

-   

Programming Tools
-----------------

**IDLE**Standard Python editor (comes with Python). Good for small
programs.

**Erik**Powerful development environment that helps managing big
projects with\
many files, as well as testing and debugging them.

**PyChecker**Checks Python source code for common errors.

**Rlcompleter**Tool for the Python command line that supports
Tab-expansion\
(like in the Unix shell).
