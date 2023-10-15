
# Environment Variables

Environment Variables are like Python variables, but for the entire operating system. They are useful to transport short pieces of information from one program to another.
In software engineering, you will see environment variables used ubiquitously for things like:

* paths
* language settings
* passwords
* server names
* switching debugging mode on or off

In this article, you can learn how to set and read environment variables on a Unix system (Linux, MacOS)

----

## How to create an environment variable?

Type into the terminal:

    export MY_TEXT=hello

Note the following:

* do not put spaces around the assignment operator `=`
* all environment variables have the same data type. They are **strings**
* `MY_TEXT` is the name of the variable. You choose it
* `hello` is the content of the variable
* add single quotes if your text contains spaces: `'hello world'`

----

## How to read an environment variable?

Type into a terminal:

    echo $MY_TEXT

The Unix `echo` command is the equivalent of `print()` in Python.
The `$` symbol dereferences the variable.

If you want to see *all* environment variables that are defined, try the command:

    env

The output is usually quite a mess.

----

## Are the environment variables global?

No. Each environment has a local *scope*. Each program has its own variables. That means that typing

    echo $MY_TEXT

in two terminals may yield different results.

More precisely, when one program starts another program the current environment variables are copied to the new program.
E.g. when you start a Python program from a Unix command line, it receives the current state of `$MY_TEXT` .

----

## How can I make environment variables permanent?

If you want **all** programs to have a certain environment variable, add the `EXPORT` statement to a configuration file in your home directory.
Open the file `.bashrc` (Linux) or `.bash_profile` (MacOS) and add the same line as above:

    export MY_TEXT=hello

The changes are applied as soon as you start a new terminal.
You can update your environment with:

    source ~/.bashrc

**Note: Restart your Python editor, if you want it to see the new environment variables.**

----

## How to read environment variables from Python?

You can read an environment variable in two lines:

    import os

    text = os.getenv('MY_TEXT')

The `os.getenv()` function returns an empty string if the variable is not defined.

----

## Are there any environment variables I should know?

Here are a few common ones:

| name | description |
|------|-------------|
| PATH | directories in which your terminal is looking for executable programs |
| PYTHONPATH | directories in which Python is looking for importable modules  |
| USER | unix username |
| HOME | absolute path to your home directory |
| LANG | language setting |

If you want to append a directory to an existing `PATH` or `PYTHONPATH`, this expression is useful:

    export PATH=$PATH:/my/new/dir/
