## How well-engineered is the code

Here we examine, how easy it is to work with the code. Well-written code is of course a factor, but in our experience other factors are an as good indicators of solid engineering.

There are five engineering tools you can try:

* Is the code stored in a version control system?
* Is there a one-line installer?
* Do you obtain test coverage &gt;= 50%?
* Does pylint return an average score &gt;= 5.0?
* Is the number code lines per modularization unit &lt;= 20?

Each of these criteria, if satisfied, contributes a point to the Legacy Metric, up to a total of five.

### 1. Version Control System
As a scientist, you know the importance of a lab notebook. A version control system achieves the same for programmers.

Questions you can ask include:
* Is there a repository with the latest version of all code?
* Are files kept there as well?
* Are there multiple branches?
* Do you know what the branches have been used for?
* Are past releases tagged in the repository?

Starting with a version control system in place from the very beginning will save you a lot of pain. All version control systems are good for checking the first criterion:

- [ ] **Tick this box, if you have the possibility to inspect at least five earlier versions of the code.**

### 2. Automatic installation / deployment
If you have a tool that releases the software on-the-fly, you can start building improved versions on day one. Build tools accelerate your development speed tremendously.

Questions you can ask include:
* Hoa have previous version been built?
* Can you install the program out-of-the box or deploy it on a server yourself?
* Can you set up a dedicated environment for development?
* Does the program have features that would only work in production (e.g. on one specific server)?

The following qualify as one-line installers:

Using distutils:

    python setup.py install

Using pip:

    sudo pip install genesilico-modomics

Using Ubuntu:

    sudo apt-get install genesilico-modomics

Using Docker:

    sudo docker run -d -P genesilico/modomics python modomics/manage.py runserver

We emphasize one-line installers, also for servers and virtual machines. They allow us to check the second criterion:

- [ ] tick this box if you can build/install the program on your computer with a single command.


### 3. Automatic tests
Ideally, you should be able to reproduce previous research results before producing your own. How can you verify that the program is working? Automatic tests help you do that quickly.

Questions you can ask include:
* Are there any automatic tests?
* Do all tests pass?
* Is there a test suite that lets you run tests with a single command?
* Do the tests contain example data?
* Is there a way to reproduce results from a related publication quickly?

#### Test coverage
If you have an automatic test suite, you can check what portions of the code they actually test. In Python, the **coverage** tool allows you to do that:

    coverage run setup.py test

or

    coverage run test_all.py

Afterwards, you can inspect a textual summary:

    coverage report

The HTML coverage report helps you to find problematic areas:

    coverage html
    firefox htmlcov/index.html &

Inspecting the coverage for the modules for your program allows you to check the third criterion:

- [ ] tick this box if the average test coverage of your program is greater than or equal 50%.


### 4. How well-written is the code?

Python has a standard style guide for code, known as [PEP8](https://www.python.org/dev/peps/pep-0008). Adhering to PEP8 is good, because it makes your code readable for others. It also helps you to write in a consistent style. Think of PEP8 as your font, if the text is your code.

#### pylint
The **pylint** tool checks whether your code conforms to the PEP8 coding guidelines. pylint gives you a ballpark figure how good or bad the code is. You can use it to analyze any Python file:

    pylint modomics.py

pylint is a powerful tool to analyze your code for readability and style. We find working with pylint very rewarding. You can start immediately to fix issues, re-run pylint and see your score improve.

Don't try to push every Python file to a score of 10.0. It is OK to ignore warning messages you don't agree with. Use your reason.

In the output, there are two sections to pay attenton to:
* Code score
* Warning messages


#### Code score
In the third last paragraph of the pylint output you find a score of up to 10 points:

    Global evaluation
    -----------------
    Your code has been rated at 8.18/10

Smaller than zero means trouble, 1-4 needs cleanup, 5-7 is reasonable and above means that someone did a great job.

| pylint score  | means              |
| --------------|--------------------|
| < 0.0         | trouble ahead      |
| 0.0 - 5.0     | needs cleanup      |
| 5.0 - 7.0     | reasonable quality |
| > 7.0         | great code!        |

The average pylint score allows you to check the fourth criterion:

- [ ] tick this box, if the averages pylint score of the modules you take over is greater than or equal 5.0.


#### Warning messages pylint produces:
At the top of the output, you find a section with warning messages. Each warning contains the line number the warning refers to:

    C: 32,0: Line too long (88/80)
    W: 30,0: TODO: same order of arguments as in ModernaStructure
    C:  1,0: Missing docstring
    R: 19,0:Renumerator: Too many public methods (30/20)

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

#### Code modularization
Pylint helps to analyze modularization as well:

    R: 19,0:Renumerator: Too many public methods (30/20)
    R: 32,4:Renumerator.letter_generator: Method could be a function
    R: 45,0:RNAResidue: Too many instance attributes (11/7)
    R:328,0:NucleotidePattern: Too few public methods (1/2)

Warnings about the number of classes / methods / functions indicate that the structure of the code needs improvement. These messages require some interpretation; don't try to fix all of them by force.

If you see a few warnings like these, don't worry. Only if you see them repeatedly, it may help readability to divide the code into units of more reasonable size.

To assess modularization of a program as a whole, pylint is not the right tool.


### 5. Code modularization

Certainly it makes a difference whether your legacy code is neatly organized or whether all code is in a single function.

Here we will analyze modularization by counting how many lines of code there are per unit of modularization. Python gives you a lot of freedom to choose how you modularize code. This is why we will treat packages, modules, classes and functions equivalently.

We deliberately ignore lambda functions and code blocks structured by *for*, *while*, *try* and *if*. These have nothing to do with code modularization.

To assess the level modularization, you need to count the number of packages, modules, classes and functions.

##### Number of packages
You can count the number of packages with:

    find . -name "__init__.py" | wc -l

If you have more than 100 packages, this is probably not the right book for you.

##### Number of modules
To count how many modules there are in your program, type:

    find . -name "*.py" | wc -l

##### Number of classes
To count how many classes there are, type:

    find . -name "*.py" | xargs cat | grep "^\s*class\s.*\:"  | wc -l

##### Number of functions
Finally, the number of functions:

    find . -name "*.py" | xargs cat | grep "^\s*def\s.*\:"  | wc -l

#### Lines of code (LOC)
As in the previous section, the total number of code lines is given by:

    find . -name "*.py" | xargs wc -l

#### Lines per Modularization score
Now you are ready to calculate the **lines per modularization unit (LM)**. Divide the number of lines of code (LOC, see previous section) by the sum of modularization units:

    LM = LOC / (#packages + #modules + #classes + #functions)

In our experience, a value of 20 LOC / mod indicates a good program structure. With that said, you are ready to check the fifth and final criterion:

- [ ] tick this box if the LM-score is greater than or equal 20.

