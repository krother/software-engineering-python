
# Counting Lines of Code

## How much code is there?

In a small project, you can simply roll up your sleeves and start fixing things. In a big project, however, you need to keep an overview what parts of a project local changes might affect.

More code means more work. The amount of code gives you a ballpark figure of how much you need to read and understand before getting to work.

You can count the total number of files on Unix:

    :::bash
    find . -name "*.py" | wc -l

A common metric is the number of **lines of code (LOC)**. The following command gives you the total number of LOC for all Python files in a Python directory tree:

    :::bash
    find . -name "*.py" | xargs wc -l

Empty lines, docstrings and comments are counted, too, as they are part of the source code.

----

### Writing a big Program

1.  List all kinds of things that a user wants to do with the program (Use Cases).
2.  Think of a smart representation of your data.
3.  Create classes containing the data, and create a diagram containing all classes.
4.  Determine which other modules your program will require.
5.  Write a flowchart for complex tasks/algorithms.
6.  For all Use Cases, create simple example data, and write a test function.
7.  Only after 1.-6., start writing the program.
8.  When all tests work, stop immediately programming and start testing.
9.  Every time you find a bug, write a new test.
