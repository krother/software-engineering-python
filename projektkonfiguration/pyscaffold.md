
# Starting a Python project with pyscaffold

When starting a small program from scratch, you probably don't need to worry much about organizing files and directories. It is OK to keep program and data files in the same place. But as the project grows you need to organize files differently. 

A good directory structure helps you to:

* separate data and code
* separate program and tests
* extract program releases easily
* keep huge files away from small ones

Generally, in a good directory structure there is one obvious place for every file.

Fortunately, there is a de-facto standard for Python projects. The **pyscaffold** tool creates this structure for you. In this text, you can learn about **pyscaffold**, the directories in a Python project and a few important files.

### Setting up a project with pyscaffold

The command-line-tool **pyscaffold** creates the directory structure for a Python project. To install and use **pyscaffold**, start from your main folder or wherever you keep your projects, and type:

    sudo pip install pyscaffold
    putup myproject

Where `myproject` is the name of your Python package. You should see that **pyscaffold** has created a `myproject/` directory with a couple of subdirectories and files:

    docs/   
    myproject/
    tests/
    AUTHORS.rst
    MANIFEST.in
    requirements.txt
    LICENSE.txt
    README.rst
    setup.py
    versioneer.py

Let's have a look what each of these does.

### Directories

#### docs/
This is the place to keep documentation. Initial files for use with the document generator **Sphinx** are already there. So if you have **Sphinx** installed, you can create and view your documentation with:

    cd docs
    make html
    firefox _build/html/index.html 

#### Python directory
Here your Python files have their home. You can add your own Python modules and packages here. The `__init__.py` file marks the directory as a Python package. The file `_version.py` helps with assigning versions, you don't have to edit it.

#### tests/
This is where automated tests are stored. Apart from an `__init__.py` file, the directory should be empty. Nevertheless you can already run the test suite with

    python setup.py test

#### Other directories
Sometimes, you will also find a `bin/` directory for binary files in a Python project. As soon as you start creating releases of your program, the directories `build/` and/or `dist/` will appear as well.

Of course, you can add your own directories. For instance, it is generally wise to have a separate directory for data, especially if you have a lot of it.

### Files

#### setup.py
The `setup.py` file is the heartpiece of your project. It contains instructions how to build your program, create releases, run tests. You can configure `setup.py` to release your program to the **Python Package Index** or to create an executable with **py2exe** on Windows.

The most common use is to build your program. The following command collects everything that is needed to run the program'in the `build/` directory:

    python setup.py build

You can also install the program alongside other Python libraries on your system:

    python setup.py install

Finally, you can create a `.tar.gz` archive for distributing the containing all files specified in the `MANIFEST.in` file:

    python setup.py sdist


#### README.rst
The `README.rst` file in the main project directory is the first thing most developers read if they consider installing the program or are simply curious. This file should contain a brief summary of what your program does, how a simple usage looks like and where to read more.

Having a README file in the ReStructuredText format (`.rst`) allows you to use markup language that is used by **github** or **bitbucket** to format your pitch nicely.

#### AUTHORS.rst
A simple list of developers and their contact info.

#### LICENSE.rst
A document covering the legal aspects. By default, you will find a copyright message and your username there. Feel free to paste any software license there. 

#### MANIFEST.in
The `MANIFEST.in` file contains a list of file names or file name patterns. This list is being used to identify fiĺes that should be included in builds and source code releases (e.g. by default, you won't find the tests there).

#### versioneer.py
A script that facilitates updating version numbers with git.

#### requirements.txt
This file is used by **pip** to resolve dependencies. If your program requires specific version numbers of libraries, you can write them into *requirements.txt*. The following commands installs all the dependencies:

    pip -r requirements.txt

### Benefits of using pyscaffold
Of course, you could set up most of the above with a few Linux commands as well. The benefit of using **pyscaffold** is that you ensure consistency over multiple projects from the very beginning. Also, starting with a cleanly written `setup.py` script allows you to create a software that can be built, installed and distributed over its entire life cycle.

