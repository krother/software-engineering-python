
# Introspection in Python: Looking into your toolbox

You can think of programming as a craftsmans' place of work: there is a set of tools that allow you to get things done. As an apprentice of Python, you might want to know at the beginning „Which tools are there?”. In the Python shell, it is easy to look into your toolbox and see what is inside:

    >>> dir()
    ['__builtins__', '__doc__', '__name__', '__package__'] 

Let's see what we have in our toolbox: There are apparently four different items here. We can type them one by one to see what they are:

    >>> __name__
    '__main__'
    >>> __doc__
    >>> __package__
    >>> __builtins__
    <module '__builtin__' (built-in)>

__name__ seems to be some kind of label for our toolbox. __doc__ and __package__ both seem to be empty. Not very helpful so far. How about __builtin__? This appears to be a 'module', some kind of box. Could we look into this box as well? We can:

    >>> dir(__builtins__)
    ['ArithmeticError', 'AssertionError', 'AttributeError',
    …
    'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']

Whoa! Thats a lot of things. Actually, all these items are built-in, so they can be used any time in Python by typing their names. You can e.g. try what print does:

    >>> print
    >>> 

This creates an empty line. Could be useful. 

Lets try something else:

    >>> cmp
    <built-in function cmp>

Isn't there something that tells us in human language what a given tool might be good for?

    >>> help(cmp)
    Help on built-in function cmp in module __builtin__:

    cmp(...)
        cmp(x, y) -> integer
    
        Return negative if x<y, zero if x==y, positive if x>y.

So eventually, we can use this to compare numbers (and maybe other things) later.
Summary:
Python is a set of tools that are grouped into boxes.
dir() shows all names of things (tools and toolboxes) available in Python.
dir(something) shows everything inside a box-like structure.
help(something) shows a description of a tool or toolbox.

Task 1: 
Read the text above and try the three comands described there.

Taks 2:
Import one of the standard modules random, math or time. 

    >>> import random

Examine them using dir and help and identify three functions that you are able to use. Explain to the group what they do and how to use them.

----

## Situations where introspection is useful

* explore a library
* experiment with 
* during debugging explore types of objects
* diagnose during post-mortem
* identify overlapping namespaces [EXAMPLE]

* compare object types [EXAMPLE]

Explanation: __methods__, operator overloading, alphabetical order (underscores, uppercase, lowercase)