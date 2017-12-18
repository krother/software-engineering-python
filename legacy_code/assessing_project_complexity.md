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

