
# Managing Python libraries with virtualenv

When developing a software, you often need a specific combination of Python libraries. Sometimes this is difficult, because you require a specific version of a library, want to test your program on both Python 2 and 3, or simply need to develop your program further, while a stable version is installed on the same machine. In these cases, *virtualenv* comes to the rescue.

## What is virtualenv?

Virtualenv manages multiple installations of Python libraries, so that you can switch between them. It creates a sandbox for each of your projects, in which Python libraries and scripts for that project are installed.

## How to install virtualenv?

There are two Python packages required for working conveniently with virtual environments. Both can be installed by *pip*. The first is *virtualenv* itself:

    sudo pip install virtualenv

The second, *virtualenvwrapper* is a collection of tools that make creating virtual environments and switching between them easier:

    sudo pip install virtualenvwrapper

You also need to add a few lines to your ~/.bashrc file to:

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/projects
    source /usr/local/bin/virtualenvwrapper.sh

Finally, you need an extra line for Python3 support:

    export VIRTUALENV_PYTHON=/usr/bin/python3


## How to set up a project with virtualenv?

I assume you have a project directory already and now want to use it with *virtualenv*. You set up a new *virtualenv* project with a single command:

    mkvirtualenv myproject

Or to specify a Python version (if you did not do that already):

    mkvirtualenv myproject -p /usr/bin/python3

Behind the scenes *virtualenv* creates a new subdirectory in *~/.virtualenvs* . This is where libraries for your project will be stored. In the *~/.virtualenvs/myproject/bin/* directory, you also find scripts that are run each time you start the sandbox, so that you can e.g. set environment variables.

Next, you connect the sandbox to your existing project:

    cd myproject/
    setvirtualenvproject ~/.virtualenvs/myproject/ .

## How to work with a virtualenv project?

To start working with your project, type:

    workon myproject

You should see a *(myproject)* appearing at your prompt. Now, whenever you use *pip* to install something, it will be installed only for *myproject*.

When you want to work on something different, type:

    deactivate

The virtual environment is specific for a terminal session. Thus, you can work on as many projects simultaneously as you have terminals open.

Other commands include, but are not limited to:

    lsvirtualenv
    rmvirtualenv
    cpvirtualenv

## Links

* [https://virtualenv.pypa.io/](https://virtualenv.pypa.io/)
* [https://virtualenvwrapper.readthedocs.org/](https://virtualenvwrapper.readthedocs.org/)
