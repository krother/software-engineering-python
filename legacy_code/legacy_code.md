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
## How complex is the project?
In a small project, you can simply roll up your sleeves and start fixing things. In a big project, however, you need to keep an overview what parts of a project local changes might affect. Whether your role is going to be that of a plumber or that of an architect depends mainly on project complexity.

The complexity of a program depends on three variables:
* How much code is there?
* How many components need maintenance?
* How many platforms do you support?

### How much code is there?
More code means more work. The amount of code gives you a ballpark figure of how much you need to read and understand before getting to work.

You can count the total number of files on Unix:

    find . -name "*.py" | wc -l

A common measure is the number of **lines of code (LOC)**. The following command gives you the total number of LOC for all Python files in a Python directory tree:

    find . -name "*.py" | xargs wc -l

Empty lines, docstrings and comments are counted, too, as they are part of the source code.

#### What the LOC number tells you?
The LOC number helps you to compare programs to each other. For our complexity metric, we assign a rough size in points using a logarithmic scale:

LOC     | example           | points
--------|-------------------|--------
&lt; 100    | script to sort data files | 0
&lt; 1000   | program implementing one algorithm with a simple command-line interface | 1
&lt; 10000  | scientific calculation pipeline with multiple modes of operation | 2
&lt; 100000 | software package (Biopython)  | 3

### How many components need maintenance?
Your first Python programs probably contained Python code and nothing else. However, when projects get more complex, other components need attention as well: SQL databases, HTML templates, JavaScript code, R scripts, C libraries etc. If the project consists of multiple Python libraries that are maintained separately. The more parts your system is built of, the more interactions need to be taken care of. On one hand, having separate components in a bigger project is a good thing. Separate components means clean interfaces. On the other hand, there are more connections that can break.

To get a number for the complexity metric of a project, count the number of languages or external components that you will need to maintain. Count only components in which you could introduce bugs:

| components | example        | points |
|------------|----------------|--------|
| 1          | Pure Python package  | 0      |
| 2-3        | simple web application: Python, HTML, SQL | 1      |
| 4-5        | multi-language calculation pipeline: Python, C, R, shell script) | 2 |
| 6+         | fancy website with database and multiple calculation programs: SQL, HTML, JavaScript, Python (web framework), Python (separate package), Delphi | 3 |

For instance, in the Modomics database I was maintaining **three** components: There was a Python web server (TurboGears), a PostGreSQL database, and lots of HTML code. I did not count the JavaScript components, because they were imported as ready-made scripts that were never modified or even looked at.

### How many platforms do you support?
Theoretically, Python is platform-independent. In practice that doesn't mean everything works on every platform automatically - especially if non-Python components are involved. You need to test the platform if you are not familiar with the project. If your program supports Linux and MacOS, you need to test it on Linux and MacOS explicitly.

Platforms are not limited to operating systems. Different kinds of interfaces (command line, GUI, web) add to complexity as well:

| platforms | example        | points |
|------------|----------------|--------|
| 1          | Web interface only  | 0      |
| 2-3        | Command line on Linux/Win/Mac | 1      |
| 4-5        | Web interface, command line and GUI on two operating systems | 2 |
| 6+         | Web interface, command line and GUI on three OS's, mobile app | 3 |

In the Modomics project, there was only the web interface I had to take care of. That was a relief!

### Calculating the complexity metric
Adding all three numbers of points, you can represent the complexity of your project:

    complexity = LOC + components + platforms

The complexity score ranges from 0 (very simple) to 9 (awfully complicated).

There are quite a few aspects the formula does not cover. For instance, if 90% of your code is made of static string data you get the same complexity value as for a collection of algorithms.
The complexity value allows you describe and compare a project in a straightforward way, without spending days on analyzing.

Next, let us consider the engineering quality.

## What you can do when you take over a project

Once you figured out what situation you got yourself into, you probably want to get to work. What can you do to get a firm hold on the code you inherited? Here you find eight options.

### 1. Abandon
There may be good reasons to jump ship while still in the harbour. A clean decision to stop a project altogether can save you months or even years of prolonged struggle. If it turns out that the project is unmaintainable later, abandoning it immediately is much cheaper. Convincing others of this option will be difficult. Consider it a last resort.

### 2. Rewrite
Imagine you have built a small Cessna airplane, but figure out that you really need a Boeing 727. Nobody would say *"Oh, great, you have a pair of wings already."* You would need to build an entirely new plane. It is the same with programming. There is nothing bad about throwing away code. It does not take up space and does not pollute the environment. If the code works, but you can't work with it reasonably, write it from scratch.

Rewriting a program happens frequently, and often it is faster than fixing the old one. Fred Brooks (The Mythical Man-Month, 1982, p115ff.) recommends even to plan for throwing away the first design. Incorporating some parts from existing code into a new design is less risky than assuming all existing parts can be reused.

### 3. Reduce complexity
The trouble of maintaining a project successfully can be diminished by kicking out some features. Possibly the project does things that have a very low priority or turned out to be not important anyway.

One way to increase maintainability with a simple decision is to reduce the number of supported platforms to one. Maintaining a web-only or source-only version instead of three operating systems and a browser interface in parallel gets plenty of problems out of the way. Consider focusing on one platform until you feel familiar enough with the project to expand.

### 4. Cleanup time
Cleaning up improves the quality of your project. Increasing engineering quality takes time. You may consider spending at least some to add things that were missing from the engineering score. Create a repository. Create an installer. Write a few automated tests (this will pay off very quickly). Run **pylint** and improve your score. The latter is a great way to familiarize with the code while improving things.

### 5. Divide and conquer
Separate portions of your code and clean them up one by one. Create separate functions, classes, modules, libraries from larger blobs and test them. If done consequently, you can either isolate the messy parts or reduce them to small portions that you can handle with ease.

Michael Feathers proposes a five-step process to divide code into smaller chunks (*Feathers, Michael. Working Effectively With Legacy Code, Prentice Hall PTR, 2005*):

1. Find change points in the code (portions that can be separated).
2. Find test points.
3. Break dependencies.
4. Write tests.
5. Change the code and refactor.


### 6. Identify people who can support you

Code does not exist by itself; it is maintained by persons. When you start work on a legacy project, there are four main players who might be able to help you:

#### The former developer
Do you have a chance to meet the former developer once per week? Daily? Whenever you need? Is he able to support you directly during a transition period? Can you meet face-to-face?

The importance of face-to-face conversation is frequently underestimated. There are companies where remote work is ubiquitous, like [37signals](http://www.37signals.com). As long as the work is easy, this is fine. However, taking over legacy code is easy. This is why we emphasize looking the other person in the eye.

#### Other developers
Are the more people who have worked with the code? Are they still actively involved? A co-developer is a valuable source of information, because often they view the code from a similar perspective as you.

#### Users
Does the program have active users? Can you talk to them on a regular basis? Do you need the program yourself? Real users help you to understand what matters and motivate you to keep going.

#### Your supervisor
Is your supervisor aware of the state of the project? Can you discuss technical issues with him or a trusted mentor? Do you receive a clear vision or next major step for the project? Maybe your supervisor has been in a similar spot before and give you some valuable hints.

### 7. Mission Impossible Game
The [Mission Impossible Game](http://www.gamestorming.com/games-for-design/mission-impossible/) is a brainstorming method. The art of brainstorming is to first ask the right question. Then take decisions.

In the Mission Impossible Game you collect actionable ideas to work with legacy code. Ask: *"How to prepare the next release of our program in one day?"*. Collect ideas for half an hour.

Then, choose the ideas most relevant for the project vision, discard the others and get working.

### 8. Change one thing at a time
How many of the main parameters of the project will change the moment you take over? Things that could change include the team composition, project size, goals, features and platforms. Ideally only one parameter should be changed at a time.

The moment you take over as main developer, the team composition changes in any case. That means, nothing else should change. Spend some time making yourself comfortable with the code, working on small issues. You may allocate a week or more to learn a technology crucial to the project which you don't know yet. Don't start revolutions on day one. When you feel the code has become *yours*, it is time to enter the next development stage.
### Other factors to consider

There are several aspects of a project the metric introduced above does not cover. We found two more aspects hard to assess objectively. At least, we would like to give you questions:

#### Documentation
Questions you can ask include:
* Is understandable documentation available?
* Is the documentation up-to-date?
* Does the documentation contain code examples?
* Can the code examples be checked automatically (doctests)?

#### Backlog and ticket systems
Questions you can ask include:
* How are tasks in the project tracked?
* Is there a backlog, a ticket system or a bug tracker?
* How old are the last entries?
* Are the entries meaningful and understandable?
* Is there an analog system for tasks and bugs (whiteboard, pin board, notebook). This is an alternative to electronic systems.
## Problems with legacy code

### Technical debt

The main problem with legacy code is the so-called technical debt. To illustrate the concept, consider the following example:

What would you think if you found this piece of code?

    def repair_chain(self, a, b, c=None):
        """
        struc - a Bio.PDB object
        threshold value
        """
        #TODO: fix documentation
        ...



Looks bad enough in your own code. Now imagine you find these lines in a project you just inherited. What do you think, will working with the code be easy?

When existing code is hard to work with, this is called **technical debt**.

#### Reasons for technical debt

How does technical debt emerge? There are at least four reasons:

#### 1. Time pressure
Generally, it is a good thing if someone wants to have a program working (because they need it). Generally, sooner is better than later. In scientific projects, this is often expressed by deadlines. A deadline could be a paper submission, the end of a funding period or the end of a PhD thesis. Although many deadlines in science are soft and negotiable, they create time pressure.

Pressure teases programmers to cut corners. Programmers under pressure try to get the code running, no matter what (*"I can clean this up later."*). Producing clean, transparent, well-tested code becomes a secondary issue. Small nodules of messy code will emerge, grow, accumulate, and if you rush from deadline to deadline, the program becomes a jungle.

Slowing down your pace of programming under pressure takes courage.


#### 2. Lack of experience
A programmer might write code that is difficult to maintain because he doesn't know better. An unexperienced programmer thinks that programming means writing code. An experienced programmer - like anyone interested in a book on software engineering - knows that sometimes programming means writing code, and sometimes it doesn't.

Lack of experience often results in code that is unnecessary long or complicated. This can happen even to experienced programmers switching from another language. Once, we stumbled upon the following Python code fragment written by a C programmer:

    i = 0; s = []
    f = open(filename,'r')
    while 1:
	    z = f.seek(i)
    	if z==None:
    		break
    	ch = f.read(1)
    	s.append(ch)
    	i = i+1

This code fragment can be written as:

    s = list(open(filename).read())

Even though Python is considered easy to learn, writing good Python code is not trivial.

#### 3. Overabundant experience

Experienced programmers can create problematic code, too. In the first place, an experienced programmer is very good to have: They write sophisticated programs incredibly quickly, master new technologies and make them work. Such programmers are rare and valuable.

The problem is that sometimes it takes another experienced programmer to understand their code. One example of such code is called **code golf**. In code golf, the programmer tries to implement a program with as few key strokes as possible:

    return max([(d.count(x),x) for x in set(d)])[1]

This line returns the most frequent element from a list. It is a moderate example, we have seen much worse.

The moment an experienced programmer departs and leaves a lot of functional code that is hard to read, the project can suddenly go into debt.

As long as great programmers are in short supply, you need to find alternatives.

#### 4. Python
Python itself is not the best language to support legacy code.
Pythons built-in method to check program code before execution gives you SyntaxErrors and the most crude exceptions. Unfortunately, Python does not provide you with anything more.

Even a simple bug resulting from a typo like the following will go unnoticed:

    def get_modification_name(id):
         return DATABASE.get(idx)

Strictly typed languages like Java and C are fundamentally different in this aspect. They enforce strict rules on variable types and method signatures that are checked automatically while compiling a program. Without additional tests, Java and C code that compiles is much more reliable than Python code.

Summarizing, Python is not very good at telling whether the code you took over is working. You need to add engineering tools to improve maintainability by yourself.

#### Conclusion

Technical debt is a serious problem when taking over a project. It can slow down development or even lead to a standstill. To avoid pitfalls, you need to figure out the strenghts and weaknesses of the code you are taking over.

The next section gives you tools to assess a project you just got on your desk.
# How to take over a legacy project?

## In this chapter you can learn:

* why problems with legacy code emerge
* how to quickly assess the complexity of a project
* how to quickly assess the engineering quality of a project
* strategies to overcome initial difficulties

## The Modomics story

In March 2007 I inherited the [Modomics database](http://www.genesilico.pl/modomics) from Staszek, a MSc student in the lab. Staszek handed me the code and the server passwords. Then he moved to Germany. Although he did whatever he could to support me by email, a sackful of knowledge moved away with him.

![Modomics](modomics.jpg)

There was a hard deadline for publication in June. In May, the hard disk of the server crashed. I restored most of the code from the SVN repository and loaded the database dump. However, some features were lost on the way. I was determined to not only fully recover the project, but also to add enough value to submit the publication on time.

Working on the code was tough: *"What does this mean? How does this work? Why is this character on the web page three positions further to the left than it should?"* I frequently found myself tracing Python & HTML code line by line. As a result, adding even small features and debugging became a daunting task.

When the deadline drew near, I worked literally every minute, including late evenings and weekends, until the very last moment. I was constantly overslept and emotionally brittle to the point of resignation. It took me a year to realize the correct term for this: burnout.

I missed the deadline, or to be precise, my supervisor hit the **STOP** button in time. He decided to postpone submission by one year, but to the same journal. An extra year was the best thing that could happen to the project and its maintainer. First of all, I relaxed. Second, I spent more time talking to scientists using the website and understood better what they needed. Then, I cleaned up many big and small issues:

* I drew a data model for the database.
* I refactored smaller functions with descriptive names.
* I created a separate unit-tested Python package for internal logic, thus making the web interface slimmer.
* I wrote a separate tool filling the database.

In the end, I had rewritten much of the code. The site was working, the publication got accepted.

Finally, after two more years, it was time to hand over the project to my successors Sebastian and Kaja. The first thing Sebastian did was that he dumped most of my code and rewrote the site in Django within two weeks. Kaja kept on maintaining the server diligently for years, and so the database lives on until the day I write these lines, with different code, but the same vision it was originally created with.

What I learned is that taking over a program from someone else is difficult.


#### Project summary

| Name | Modomics |
|------|----------|
| Summary | Web database of modified RNA nucleotides. |
| Duration | 2006 - 2014 |
| Developers | 2 coders (2009) |
| Stakeholders | 2 senior scientists, 4 data curators (2009) |
| Size | ~10000 Python LOC |
| Technologies used | TurboGears web server <br> PostGreSQL database <br> Biopython <br> PIL |
| Development tools used | bug tracker (TRAC) <br> automatic tests (partial) <br> SVN repository <br> User Stories <br> Entity-relationship diagram |
| Publications | Machnicka MA, Milanowska K, Osman Oglu O, Purta E, Kurkowska M, Olchowik A, Januszewski W, Kalinowski S, Dunin-Horkawicz S, Rother KM, Helm M, Bujnicki JM, Grosjean H. MODOMICS: a database of RNA modification pathways: 2012 update. Nucleic Acids Res 2013 Jan 1;41(D1): D262-D267<br><br>Czerwoniec A, Dunin-Horkawicz S, Purta E, Kaminska KH, Kasprzak J, Bujnicki JM, Grosjean H, Rother K. MODOMICS: a database of RNA modification pathways. 2008 update. Nucleic Acids Res 2009 Jan;37(Database issue):D118-21. [Epub 2008 Oct 14]<br><br>Dunin-Horkawicz S, Czerwoniec A, Gajda MJ, Feder M, Grosjean H, Bujnicki JM. MODOMICS: a database of RNA modification pathways. Nucleic Acids Res. 2006 Jan 1;34(Database issue):D145-9. |

# The Modomics story

In March 2007 I inherited the [Modomics database](http://www.genesilico.pl/modomics) from Staszek, a MSc student in the lab. Staszek handed me the code and the server passwords. Then he moved to Germany. Although he did whatever he could to support me by email, a sackful of knowledge moved away with him.

![Modomics](modomics.jpg)

There was a hard deadline for publication in June. In May, the hard disk of the server crashed. I restored most of the code from the SVN repository and loaded the database dump. However, some features were lost on the way. I was determined to not only fully recover the project, but also to add enough value to submit the publication on time.

Working on the code was tough: *"What does this mean? How does this work? Why is this character on the web page three positions further to the left than it should?"*

When the deadline drew near, I worked literally every minute until the very last moment, including late evenings and weekends. I was constantly overslept and emotionally brittle to the point of resignation. It took me a year to realize the correct term for this: burnout.

I missed the deadline, or to be precise, my supervisor hit the **STOP** button. An extra year was the best thing that could happen to the project and its maintainer. First of all, I relaxed. Second, I spent more time talking to scientists using the website and understood what they needed better. I cleaned up many big and small issues and introduced a better structure of Python modules. In the end, I had rewritten most of the code. The site was working, the publication got accepted.

Finally, after two more years, it was time to hand over the project to my successors Sebastian and Kaja. The first thing Sebastian did was that he dumped most of my code and rewrote it in Django within two weeks. Kaja kept on maintaining the server diligently, and so the database lives on until the day I write these lines, with different code, but the same vision as when it was first created.

What I learned is that taking over a program from someone is difficult.

## Assessing a legacy project

When you take over a project, you need to find out first what you got yourself into. There are two aspects to consider before you can decide what to do:

1. How complex is the project?
2. How well-engineered is the code?

Intuitively, you would expect the according graph to look like this:

![Simple assessment graph](legacy_graph_simple.png)

In this section, you will find a method to locate your project in this graph. We introduce a simple metric for complexity and engineering quality. The purpose of the metric is to give you a rough assessment quickly.

We chose few but rigorous, objective criteria for both complexity and engineering quality, that you can use to compare a legacy project to projects you are already familiar with.
