Programming Style
-----------------

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

### Advantages of Object-oriented Programming

-   Encapsulation: data and code stick together
-   Code reuse: inherit and dont write all anew
-   Maintenance: errors are easier to find/less frequent
-   Structure: additional level of grouping things
-   consistency: People are used to think in objects (programmers too)
-   Polymorphism: similar objects do different things
-   Objects are good dimension for Unit testing
-   Disadvantages:

    -   Code is a little longer (for doing small tasks)
    -   Code is a little slower (when there are many instances)

### 

### What Exceptions to catch

-   File operations
-   web operations
-   big function calls
-   database operations
-   NEVER CATCH everything

### Writing a big Program

1.  List all kinds of things that a user wants to do with the program
    (Use Cases).
2.  Think of a smart representation of your data.
3.  Create classes containing the data, and create a diagram containing
    all classes.
4.  Determine which other modules your program will require.
5.  Write a flowchart for complex tasks/algorithms.
6.  For all Use Cases, create simple example data, and write a
    test function.
7.  Only after 1.-6., start writing the program.
8.  When all tests work, stop immediately programming and start testing.
9.  Every time you find a bug, write a new test.

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

**PyDoc**Creates HTML pages from the comments in a bunch of Python
modules.

**PyChecker**Checks Python source code for common errors.

**Pydb**Debugger that helps to find errors in Python programs. It allows
to interrupt a\
program at a given point, to examine and to change variables from a\
command line.

**Rlcompleter**Tool for the Python command line that supports
Tab-expansion\
(like in the Unix shell).

**Jython**A Python compiler that creates Java code. Useful to make Java
and Python\
programs work together, and to run Python programs from a web browser.

**Py2Exe**Creates Windows executables from Python programs. Requires
the\
*distutils* package.

### 
