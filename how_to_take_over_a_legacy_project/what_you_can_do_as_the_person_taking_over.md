# When you inherit a project

When you take over a project, there are four aspects to consider before you decide what to do:

1. How big is the project?
2. What infrastructure is there?
3. How well-maintained is the code?
4. Who is there to help you?

In the following, you find criteria for each question. In the end, the full checklist and a guideline help you to decide possible consquences.

## How big is the project?
Is your role in the new project going to be that of a plumber (go down, fix it) or that of a librarian (keep an overview)? Before everything else, that depends on project size.

### How much code do you have?
The amount of code gives you a ballpark figure of how much you need to readn and understand before getting to work.

You can count the total number of files on Unix:

    find . -name "*.py" | wc -l


The following command gives you the total number of lines of code (LOC) in all Python files in a Python directory tree:


    find . -name "*.py" | xargs wc -l

To identify unique lines, try:

    find . -name "*.py" | xargs cat | sort | uniq | wc -l

For instance, in the ModeRNA project, we found 154 Python files with 27000 lines, of which 16000 were unique.

#### What the LOC number tells you?
You can use LOC compare a project to other programs you wrote. For comparison, use a logarithmic scale:

LOC     | example           | points
--------|-------------------|--------
<100    | script to sort data files | 1
<1000   | program implementing one algorithm with a simple interface | 2
<10000  | calculation pipeline with multiple modes of operation | 3
<100000 | software package (Biopython)  | 4

If the size of the inherited project goes up by at least one order of magnitude compared to your biggest project so far, you will need help.

### How many components are there?
Your first Python programs probably contained Python code and not much else. However, when projects get more complex, you may need to take care of other components: SQL databases, HTML templates, JavaScript code, R scripts, C libraries etc. You also should take into account Python packages that are built and maintained separately (number of setup.py scripts). If there is more than one, your work gets more complex.

The number of components is a good metric to start with, because you will find out by looking at file extensions (with the exception of databases).

On one hand, having separate components in a bigger project is a good thing. Separate components means clean interfaces. On the other hand, there are more connections that can break.

You can count the number of components you will be directly responsible for:

| components | points |
|------------|--------|
| Python, JavaScript, HTML, SQL database, R, C, additional Python sub-projects | 1 each |

For instance, the Modomics database scored a **3** at the time I was maintaining it: There was a Python web server (TurboGears), a PostGreSQL database, and lots of HTML code. I did not count the JavaScript components, because they were imported as ready-made components that were never modified or even looked at.

### How many platforms do you support?
They said Python is platform-independent. That doesn't mean everything works everywhere. As a minimum, if your program supports Linux and Mac, you need to test it on Linux and Mac. That adds another dimension to complexity:

| platform     | points |
|--------------|--------|
| Linux        | 1      |
| Windows      | 1      |
| Mac          | 1      |
| binary distribution | 1    |
| Web version  | 1      |
| mobile app   | 1      |

In the Modomics project, there was only the web interface I had to take care of. That was a relief!

### Combined complexity

You can combine the three numbers from the sections above to a single complexity value ranging from 3-16 points.

    complexity = LOC + components + platforms

Some developers might argue what is the correct formula to combine the three values. The actual amount of work required might as well be exponential to the complexity. We don't know for sure.

What we know is that the comlexity lets you describe the size of the project: 5 is comfortable, 8 is challenging, and 12 means that it probably is going to be tough.


## What infrastructure is there?


## How well-maintained is the code?

## Who is there to help you?

### pylint
The **pylint** tool gives you a quick ballpark figure how bad the situation is. You can use it to analyze any Python file:


    pylint setup.py


In the output, there are multiple things to pay attenton to:

Link to PEP8

#### Code score
Smaller than zero means trouble, 1-4 needs cleanup, 5-7 is reasonable and above that someone did a great job.


| pylint score  | means              |
| --------------|--------------------|
| < 0.0         | trouble ahead      |
| 0.0 - 5.0     | needs cleanup      |
| 5.0 - 7.0     | reasonable quality |
| > 7.0         | great code!        |


#### Warnings about code structure
* pay attention to warnings about 'too many methods per class' / 'functions per module'.

#### Warnings you should ignore
EXAMPLE

Just don't try to push every Python file to a 10.0. It is OK to ignore warning messages you don't agree with. Use your reason.

We find working with pylint very rewarding. You can start to fix issues, re-run pylint and see your score improve.

### Tests
* example data
* automatic tests
* test coverage
If you have working tests, you can check what portions of the code they actually test:

    coverage run setup.py test

To

    coverage report

The HTML coverage report helps you to find problematic areas.

    coverage html
    firefox htmlcov/index.html &

* paper, reproduce results. If this is not possible,




### documentation
Yes it is usually bad. If there is good documentation usually everything else is in place.

Fortunately lack of documentation is easy to replace: You need the former contributor next to your desk at least for some time. If you simply get handed the code and your predecessor departs for vacations or forever, expect big trouble.

### deployment
..


# How the rx project started:
(MR 2012)
1. Access to repository.
2. What is the rxncon data model?
3. Where is the main page template?
4. Where is the production code:
e.g.
looking at the Quick – where is the code responsible for input parsing, creating output for each button?
where reactions and contingencies are interpreted?
5. How large is the project (how to distinguish your code and default code generated by web2py, have you deleted any default code)?
6. Is it possible to split the production code and web2py (what is your opinion – I think it would facilitate testing, but may be too much work)?
7. Which parts of the code would you advise to start working with to get to know the code. Are there any independent fragments?
8. How did you test your code?
9. Do you measure the traffic on the web?


### Check these factors before taking over
There is one argument why you should insist on inspecting the code: Your supervisor might not be aware of that the project is booby-trapped. A program that looks good from the outside (e.g. a shiny GUI or web interface) and has produced scientific results may seem flawless from a supervisors perspective. It may still be entirely rotten from the inside.

## Measures to take

### Divide and conquer
extract small parts, clean them up and test one by one.
This is very hard.

#### Make a separate library of some parts

#### Reduce scope
kick out deployment. Web-only or source-only are viable alternatives.

### Rewriting the code
There is no recycling bin for code. There is nothing bad about throwing away code. If it does not work, write it from scratch.
Reasons why many programmers don't is taking pride in someone's code. Also non-developers tend to interfere, because they think if part the code is already there, a part of the problem is already solved.

*Brooks: Prepare to throw one away*

### Change one thing at a time
How many of the main parameters of the project will change the moment you take over? (team, project size, goals, features, platform)
