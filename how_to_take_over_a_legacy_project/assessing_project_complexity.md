## How complex is the project?
Is your role in the new project going to be that of a plumber (go down, fix it) or that of a librarian (keep an overview)? Before everything else, that depends on project size.

The complexity of a program depends on three variables:
* How much code is there?
* How many components need maintenance?
* How many platforms do you support?

### How much code is there?
More code means more work. The amount of code gives you a ballpark figure of how much you need to read and understand before getting to work.

You can count the total number of files on Unix:

    find . -name "*.py" | wc -l

A common measure are the **lines of code (LOC)**. The following command gives you the total number of LOC for all Python files in a Python directory tree:

    find . -name "*.py" | xargs wc -l

To identify unique lines, try:

    find . -name "*.py" | xargs cat | sort | uniq | wc -l

Empty lines, docstrings and comments are counted, too, as they are part of the source code.

For instance, in the ModeRNA project (https://github.com/lenarother/moderna), we found 154 Python files with 27000 lines, of which 16000 were unique (as of August 28th in the master branch on Github).

#### What the LOC number tells you?
The LOC number helps you to compare programs to each other. For our complexity metric, we assign a rough size in points using a logarithmic scale:

LOC     | example           | points
--------|-------------------|--------
&lt; 100    | script to sort data files | 0
&lt; 1000   | program implementing one algorithm with a simple command-line interface | 1
&lt; 10000  | scientific calculation pipeline with multiple modes of operation | 2
&lt; 100000 | software package (Biopython)  | 3

If you inherit a project with a LOC number one order of magnitude higher than your biggest project so far, expect difficulties.

### How many components need maintenance?
Your first Python programs probably contained Python code and not much else. However, when projects get more complex, other components need attention as well: SQL databases, HTML templates, JavaScript code, R scripts, C libraries etc. If the project consists of multiple Python libraries that are maintained separately. The more parts your system is built of, the more interactions need to be taken care of.

On one hand, having separate components in a bigger project is a good thing. Separate components means clean interfaces. On the other hand, there are more connections that can break.

To get a number for the complexity metric, count the number of components which you will need to maintain. Effectively that means the number of areas where you can introduce bugs:

| components | example        | points |
|------------|----------------|--------|
| 1          | Python package  | 0      |
| 2-3        | simple web app:Python, HTML, SQL | 1      |
| 4-5        | multi-language calculation pipeline: Python, C, R, shell script) | 2 |
| 6+         | fancy website with database and multiple calculation programs: SQL, HTML, JavaScript, Python (web framework), Python (separate package), Delphi | 3 |

For instance, in the Modomics database I was maintaining **three** components: There was a Python web server (TurboGears), a PostGreSQL database, and lots of HTML code. I did not count the JavaScript components, because they were imported as ready-made scripts that were never modified or even looked at.

### How many platforms do you support?
They said Python is platform-independent. That doesn't mean everything works on every platform automatically. You need to test it - especially if you are not familiar with the project. If your program supports Linux and MacOS, you need to test it on Linux and MacOS explicitly.

Platforms are not limited to operating systems. Different kinds of interfaces (command line, GUI, web) add to complexity as well:

| platforms | example        | points |
|------------|----------------|--------|
| 1          | Web interface only  | 0      |
| 2-3        | Command line on Linux/Win/Mac | 1      |
| 4-5        | Web interface, command line and GUI on two operating systems | 2 |
| 6+         | Web interface, command line and GUI on three OS's, mobile app | 3 |

In the Modomics project, there was only the web interface I had to take care of. That was a relief!

### Summary
Adding all three numbers of points, you can represent the complexity of your project:

    complexity = LOC + components + platforms

The complexity score ranges from 0 (very simple) to 9 (awfully complicated).

You might argue what is the correct formula to combine the values. The amount of work required might as well be exponential to the complexity. We don't know.

What we know is that the complexity allows you describe the size of the project in a straightforward way, without spending days on analyzing.

Next, we will consider the engineering side.

