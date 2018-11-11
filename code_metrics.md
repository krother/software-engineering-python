
# Code Metrics

## How much code is there?

In a small project, you can simply roll up your sleeves and start fixing things. In a big project, however, you need to keep an overview what parts of a project local changes might affect. 

More code means more work. The amount of code gives you a ballpark figure of how much you need to read and understand before getting to work.

You can count the total number of files on Unix:

    find . -name "*.py" | wc -l

A common measure is the number of **lines of code (LOC)**. The following command gives you the total number of LOC for all Python files in a Python directory tree:

    find . -name "*.py" | xargs wc -l

Empty lines, docstrings and comments are counted, too, as they are part of the source code.


## Assessing engineering quality

Here we examine, how easy it is to work with the code. In our experience five criteria are good indicators of solid engineering:

* Are there at least five revisions of code stored in a version control system?
* Is there a one-line installer?
* Do you obtain test coverage &gt;= 50%?
* Does pylint return an average score &gt;= 5.0?
* Is the number code lines per modularization unit &lt;= 20?

Each of these criteria, if answered with 'YES', gives a point up to a maximum of five.

### 1. Version Control System
As a scientist, you know the importance of a lab notebook. A version control system achieves the same for programmers.

Questions you can ask include:
* Is there a repository with the latest version of all code?
* Are files kept there as well?
* Are there multiple branches?
* Do you know what the branches have been used for?
* Are past releases tagged in the repository?

Starting with a version control system in place from the very beginning will save you a lot of pain. All version control systems (SVN, Mercurial, git, etc.) allow you to check the first criterion:

### 2. Automatic installation / deployment
If you have a tool that releases the software on-the-fly, you can start building improved versions on day one. Build tools accelerate your development speed tremendously.

Questions you can ask include:
* How have previous versions been built?
* Can you install the program out-of-the box or deploy it on a server yourself?
* Can you set up a dedicated environment for development?
* Does the program have features that would only work in production (e.g. on one specific server)?

We emphasize one-line installers, also for setting up servers and virtual machines.

### 3. Automatic tests
Ideally, you should be able to reproduce previous research results before producing your own. How can you verify that the program is working? Automatic tests help you do that quickly.

Questions you can ask include:
* Are there any automatic tests?
* Do all tests pass?
* Is there a test suite that lets you run tests with a single command?
* Do the tests contain example data?
* Is there a way to reproduce results from a related publication quickly?

To assess the quality of tests, we will have a closer look at test coverage.


### 4. Code modularization
Now we will analyze, whether your legacy code is neatly organized or whether all code is in a single function.

#### Calculating lines per structural unit
Here we will analyze modularization by counting how many lines of code there are per unit of modularization. Python gives you a lot of freedom to choose how you modularize code. This is why we will treat packages, modules, classes and functions equivalently.

We deliberately ignore lambda functions and code blocks structured by *for*, *while*, *try* and *if*. The latter are control flow statements and have nothing to do with code modularization.

To assess the level modularization, you need to count the number of packages, modules, classes and functions.

##### Number of packages
You can count the number of packages with:

    find . -name "__init__.py" | wc -l

If you have more than 100 packages, this is not the right book for you.

##### Number of modules
To count how many Python modules there are in your program, type:

    find . -name "*.py" | wc -l

##### Number of classes
To count how many classes there are, type:

    find . -name "*.py" | xargs cat | grep "^\s*class\s.*\:"  | wc -l

##### Number of functions
Finally, the number of functions:

    find . -name "*.py" | xargs cat | grep "^\s*def\s.*\:"  | wc -l

##### Lines of code (LOC)
As in the previous section, the total number of code lines is given by:

    find . -name "*.py" | xargs wc -l

#### Lines per structural unit
Now you are ready to calculate the **lines per structural unit**. Divide the number of lines of code (LOC, see previous section) by the sum of modularization units:

    LOC / (#packages + modules + classes + functions)

In our experience, a value below 20 LOC / mod indicates a good program structure. With that said, you are ready to check the fifth and final criterion:



### Documentation
Questions you can ask include:
* Is understandable documentation available?
* Is the documentation up-to-date?
* Does the documentation contain code examples?
* Can the code examples be checked automatically (doctests)?

### Backlog and ticket systems
Questions you can ask include:
* How are tasks in the project tracked?
* Is there a backlog, a ticket system or a bug tracker?
* How old are the last entries?
* Are the entries meaningful and understandable?
* Is there an analog system for tasks and bugs (whiteboard, pin board, notebook). This is an alternative to electronic systems.

