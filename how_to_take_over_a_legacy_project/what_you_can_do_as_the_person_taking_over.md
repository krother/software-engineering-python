# Assessing an inherited project

When you take over a project, there are four aspects to consider before you decide what to do:

1. How big is the project?
2. What engineering infrastructure is there?
3. How well-written is the code?
4. Who is there to help you?

In the following, you find criteria for each question. In the end, you get a full checklist to try on your own projects and possible consequnces.

## How big is the project?
Is your role in the new project going to be that of a plumber (go down, fix it) or that of a librarian (keep an overview)? Before everything else, that depends on project size.

### How much code do you have?
The amount of code gives you a ballpark figure of how much you need to read and understand before getting to work.

You can count the total number of files on Unix:

    find . -name "*.py" | wc -l

A common measure is the number of lines of code (LOC). The following command gives you the total number of LOC for all Python files in a Python directory tree:


    find . -name "*.py" | xargs wc -l

To identify unique lines, try:

    find . -name "*.py" | xargs cat | sort | uniq | wc -l

For instance, in the ModeRNA project, we found 154 Python files with 27000 lines, of which 16000 were unique.

#### What the LOC number tells you?
You can use the LOC to compare a project to other programs you wrote. For comparison, use a logarithmic scale:

LOC     | example           | points
--------|-------------------|--------
&lt;100    | script to sort data files | 1
&lt;1000   | program implementing one algorithm with a simple interface | 2
&lt;10000  | calculation pipeline with multiple modes of operation | 3
&lt;100000 | software package (Biopython)  | 4

If the size of the inherited project goes up by at least one order of magnitude compared to your biggest project so far, you will need help.

### How many components are there?
Your first Python programs probably contained Python code and not much else. However, when projects get more complex, you may need to take care of other components: SQL databases, HTML templates, JavaScript code, R scripts, C libraries etc. You also should take into account Python packages that are built and maintained separately (number of setup.py scripts). If there is more than one, your work gets more complex.

The number of components is a good metric to start with, because you will find out by looking at file extensions (with the exception of databases, servers and other machinery).

On one hand, having separate components in a bigger project is a good thing. Separate components means clean interfaces. On the other hand, there are more connections that can break.

You can count the number of components you will be directly responsible for:

| components | points |
|------------|--------|
| Python, JavaScript, HTML, SQL database, R, C, additional Python sub-projects | 1 each |

For instance, in the Modomics database I was maintaining **thre** components: There was a Python web server (TurboGears), a PostGreSQL database, and lots of HTML code. I did not count the JavaScript components, because they were imported as ready-made scripts that were never modified or even looked at.

### How many platforms do you support?
They said Python is platform-independent. That doesn`t mean everything works on any platform automatically. You need to test it. For instance, if your program supports Linux and MacOS, you need to test it on Linux and MacOS. That adds another dimension to complexity:

| platform     | points |
|--------------|--------|
| Linux        | 1      |
| Windows      | 1      |
| Mac          | 1      |
| binary distribution | 1    |
| web version  | 1      |
| mobile app   | 1      |

In the Modomics project, there was only the web interface I had to take care of. That was a relief!



## How well-written is the code?

Python has a standard style guide for code, known as [PEP8](https://www.python.org/dev/peps/pep-0008). Adhering to PEP8 is good, because it makes your code readable for others. It also helps you to write in a consistent style. Think of PEP8 as your font, if the text is your code.

### pylint
The **pylint** tool checks whether your code conforms to the PEP8 coding guidelines. pylint gives you a ballpark figure how good or bad the code is. You can use it to analyze any Python file:

    pylint modomics.py

In the output, there are two sections to pay attenton to:

### Code score
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

### Warnings
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

- [ ]  What is the depth of the most nested loop / if statement?

#### Code structure

    R: 19,0:Renumerator: Too many public methods (30/20)
    R: 32,4:Renumerator.letter_generator: Method could be a function
    R: 45,0:RNAResidue: Too many instance attributes (11/7)
    R:328,0:NucleotidePattern: Too few public methods (1/2)

Warnings about the number of classes / methods / functions indicate that the structure of the code needs improvement. You don't need to worry if you see a few warnings like these, but if you see them repeatedly, it may help readability to divide the code into units of more reasonable size.

### Summary
pylint is a powerful tool to analyze your code for readability and style. We find working with pylint very rewarding. You can start immediately to fix issues, re-run pylint and see your score improve.

Don't try to push every Python file to a score of 10.0. It is OK to ignore warning messages you don't agree with. Use your reason.


## What engineering infrastructure is there?

In this section, a number of engineering tools you can check for are enumerated briefly. All of them are explained in more detail in other chapters.

### Repository
Is there a repository with the latest version of all code? Are files kept there as well? Are there multiple branches? Do you know what they are for? Are past releases taged in the repository?

### Automatic tests
Are there any automatic tests? Do the tests pass? Is there a test suite that lets you run tests with a single command? Do the tests contain example data? Is there a way to reproduce results from a related publication quickly?

If not, how can you verify that the program is working?

#### Test coverage
If you have an automatic test suite, you can calculate test coverage with the **coverage** program.

If you have working tests, you can check what portions of the code they actually test:

    coverage run setup.py test

To

    coverage report

The HTML coverage report helps you to find problematic areas.

    coverage html
    firefox htmlcov/index.html &


### Installation / deployment
Can you install the program out-of-the box or deploy it on a server? Can you set up an environment for development only? Does the program have features that only work in production (e.g. on one specific server)?

### Documentation
Is understandable documentation available? Is the documentation up-to-date? Does the documentation contain code examples? Can the code examples be checked automatically (doctests)?

### Backlog or ticket system
How are tasks in the project tracked? Is there a backlog, a ticket system or a bug tracker? How old are the last entries? If there is an analog instead of and electronic system for tasks and bugs (whiteboard, pin board, notebook), this is fine as well.


## Who is there to help you?

Code does not exist by itself. It is maintained by persons. When you assess a project, there are five main players who might support you:

### The former developer
Do you have a chance to meet the former developer on a regular basis? Preferably face-to-face, or on-line. Do you have an agreement to get direct support during a transition period?

### Other developers
Are the more people who have worked with the code? Are they still actively involved? A co-developer is a valuable source of information, because often they view the code from a similar perspective as you.

### Users
Does the program have active users? Can you talk to them on a regular basis? Users help you to find out what matters and motivate you to keep going.

### Your supervisor
Is your supervisor aware of the state of the project? Can you discuss technical issues with him or a trusted mentor? Do you receive a clear vision or next major step for the project?

### You
After assessing the project, do you recall a similar situation you have been in before? Do you know all languages / technologies that the project contains? Are you going to use the program yourself?

