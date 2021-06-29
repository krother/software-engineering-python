
# Refactoring

**Refactoring means cleaning up a program and improving its structure.**


## Why should you refactor?

It is easy to scrap and rewrite a small program. With a bigger one, it is necessary to refactor it from time to time.

Refactoring makes code more readable, makes it easier to add new features or to change existing ones.
If you omit refactoring for a while, **tech debt** accumulates. This makes maintenance increasingly difficult. In the worst case a program might simply fall apart as soon as you try to change the code.

The bigger a program is, the more important refactoring becomes. In brief, it saves time, money and your mental energy.

----

## How to refactor?

You should refactor a program as soon as the program runs and you have a moment to clean up.
The basic refactoring workflow is:

1. Open the code in an editor
2. Pick something you would like to improve
3. Clean it up
4. Run the code to see if it still does the same thing

The refactoring workflow is the same for small and big programs.
But the bigger the program, the more you will need **automated tests**, so that you can check whether you accidentally broke anything.

----

## What refactoring strategies are there?

Refactoring means a lot of things. Here are a few basic strategies:

- rename variable names for clarity
- move a block of code into a function
- split a long function into smaller ones
- remove unnecessary code
- remove redundant code
- rewrite statements that are hard to read
- splitting a Python file into multiple modules
- eliminate global variables
- extract a clean data structure
- extract a class from the code
- move program logic to a data file (JSON, table or other)
- add a `__main__` section
- add docstrings to functions and classes

----

## Where can I learn more?

On [sourcemaking.com](https://sourcemaking.com/) you find a catalog of refactoring techniques.
