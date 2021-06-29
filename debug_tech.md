
Debugging Techniques

* read the code
* read the error message (message on bottom, line numbers, type of error on top)
* inspect variables
  - print(x) OR Variable explorer in Spyder
  - print(type(x))
  - print(x.shape)
  - print(x.isna().sum())
  - print(x.info())
* downsize the input data
* downsize the number of iterations (or similar parameters)
* isolate the bug
  - copy the suspicious lines
  - comment out parts of the program
* read the documentation
* search on Google/StackOverflow (last of error message)
* execute the code line by line
    make small chunks (Jupyter)
    blue buttons in Spyder, interactive debugger
* set breakpoints (F12 in Spyder)
* turn it off and on again
  - restart the Jupyter kernel
* talk to someone else
* take a break

3 Main Types of Problems:

1. SyntaxErrors
   Python does not execute code
   --> you know there is a problem and roughly where it is

2. Runtime errors
   Python executes some parts of the code
   but then it crashes.
   --> you know there is a problem

3. Semantic errors
   Python executes the code and does not complain
   but the program does not do what it should.
   --> you don't know that there is a problem
