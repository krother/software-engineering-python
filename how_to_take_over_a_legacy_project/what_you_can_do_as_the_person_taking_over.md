# What you can do as the person taking over

### Goal
This chapter gives you metrics that you can use to evaluate code that you inherit from someone else. The metrics help you to make educated decisions on how to proceed.

### pylint
* gives you a quick ballpark figure how bad the situation is


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

### tests
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


### How big is the program?

You can count the total number of files:

    find . -name "*.py" | wc -l


The following Unix command gives you the total number of lines in all Python files in a Python directory tree:


    find . -name "*.py" | xargs wc -l

To identify unique lines, try:

    find . -name "*.py" | xargs cat | sort | uniq | wc -l

In the ModeRNA project, we found 154 Python files with 27000 lines, of which 16000 were unique.

If the size of the project goes up by one order of magnitude or more compared to your biggest project so far, you will need help.

### How complex is the project?

Another factor to consider is the number of protocols that are being used: Python, SQL, HTML, CSS, JavaScript, C, R, etc.
* on one hand: more protocols - bad, because more to learn
* on the other hand: more protocols can mean you have clean interfaces.

### documentation
Yes it is usually bad. If there is good documentation usually everything else is in place.

Fortunately lack of documentation is easy to replace: You need the former contributor next to your desk at least for some time. If you simply get handed the code and your predecessor departs for vacations or forever, expect big trouble.

### deployment
* unusual dependencies
* can you build/install the program without further information?

### Check these factors before taking over
There is one argument why you should insist on inspecting the code: Your supervisor might not be aware of that the project is booby-trapped. A program that looks good from the outside (e.g. a shiny GUI or web interface) and has produced scientific results may seem flawless from a supervisors perspective. It may still be entirely rotten from the inside.

### Divide and conquer
extract small parts, clean them up and test one by one.
This is very hard.

#### Make a separate library of some parts

### Rewriting the code
There is no recycling bin for code. There is nothing bad about throwing away code. If it does not work, write it from scratch.
Reasons why many programmers don't is taking pride in someone's code. Also non-developers tend to interfere, because they think if part the code is already there, a part of the problem is already solved.

*Brooks: Prepare to throw one away*


