
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

## What does the LOC number tell me?

Some implications of the LOC:

#### Small (<100 LOC)

Small Python programs such as standalone scripts do not require a lot of structure.
The may or may not contain functions or other structural elements.
In case the code proliferates beyond control, a small program is easy to throw away or rewrite.

#### Medium (<1000 LOC)

In a medium-sized program, more structure is necessary.
You will need to use some of the structuring options Python offers.
Most likely these will be functions.
But if you want to mix in a few classes or split the code over multiple modules that is fine as well.
If you have not started using version control yet, it will be hard to move beyond 1000 LOC without.

#### Large  (<10000 LOC)

In a large program, you will need classes to manage complexity.
Unless you are a fan of large source files, distributing the code over multiple files/folders is a good idea.
To maintain a source code of that size, automated tools for testing and linting are indispensible, especially during refactoring. Consider using a build tool.

#### Very Large (<100000 LOC)

Very large programs are structured into multiple folders with modules. Sometimes you will find a very large program divided into several pip-installable packages.
In a very large program, it is crucial to have a clean build/release process, and probably some continuous integration.
You might also want to maintain documentation for a program in this size. You shouldn't be surprised to see many configuration files appear in addition to Python files.

#### Huge (100000+ LOC)

Python software of this size does exist, mostly in the form of well-known libraries.
Usually, these evolve over years and involve dozens or hundreds of developers.
In other cases, a huge software might consists of multiple sub-packages or even programming languages so that the LOC number is not easy to determine. Also, at this size the lack of strong typing and strict encapsulation in Python may get in the way a lot, so that other languages may be a better choice.
