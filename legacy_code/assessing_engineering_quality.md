## How well-engineered is the code

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

- [ ] **Tick this box, if you have the possibility to inspect at least five earlier versions of the code.**

### 2. Automatic installation / deployment
If you have a tool that releases the software on-the-fly, you can start building improved versions on day one. Build tools accelerate your development speed tremendously.

Questions you can ask include:
* How have previous versions been built?
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

We emphasize one-line installers, also for setting up servers and virtual machines. All one-line installers allow you to check the second criterion:

- [ ] tick this box if you can build/install the program on your computer with a single command.


### 3. Automatic tests
Ideally, you should be able to reproduce previous research results before producing your own. How can you verify that the program is working? Automatic tests help you do that quickly.

Questions you can ask include:
* Are there any automatic tests?
* Do all tests pass?
* Is there a test suite that lets you run tests with a single command?
* Do the tests contain example data?
* Is there a way to reproduce results from a related publication quickly?

To assess the quality of tests, we will have a closer look at test coverage.

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

Of course, the higher the test coverage, the better. However, you don't need to aim for 100% coverage - if a program changes frequently that might impede development. In our experience, you can start working reasonably with tests above 50% coverage already.

Inspecting the coverage for the modules of your program allows you to check the third criterion:

- [ ] tick this box if the average test coverage of your program is greater than or equal 50%.


### 4. Code modularization
For the fifth criterion we will analyze, whether your legacy code is neatly organized or whether all code is in a single function.

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

- [ ] tick this box if there are less than or equal 20 lines per structural unit.

To complete the metric, count the number of ticked boxes (from 0 to 5).
