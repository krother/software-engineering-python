## Stories we can tell

* all tests pass - how boooring.
* JMB "I want to build this!"
* Tomek "More tests are coming"
* KR "Lets have fun. Lets build software"

## References

* Nick Barnes. Publish your computer code: it is good enough. Nature 467, 2010, 753.
* Rother, Rother, Puton, Potrzebowski, Wywial, Bujnicki.
* Alyssa Goodman. Ten Simple Rules for the Care and Feeding of Scientific Data. PLOS CompBiol, 2014.
* How science goes wrong, The Economist, 2013.

## packages
After experimenting on several branches, some conclusions:
1. separate test packages with __main__.py, so you can do python test_modifications/
2. import functions/classes a package exports in __init__.py
3. if the number of inter-package dependencies shrinks, the package was thought up well.
4. try to have less lines than before withouth playing golf :-)

## Test Data


    Set an environment variable for your data directory

    Write a small module that you always import that has the sole purpose of having a fixed position relative to your data directory, then call __file__ from there

    Generate the data at runtime

    Store your data in a database rather than a file

    Store your data in a fixed location in the file system rather than a location relative to the package

    Don't run your test code directly

### Other factors to consider

There are several aspects of a project the metric introduced above does not cover. We found two more aspects hard to assess objectively. At least, we would like to give you questions:

#### Documentation
Questions you can ask include:
* Is understandable documentation available?
* Is the documentation up-to-date?
* Does the documentation contain code examples?
* Can the code examples be checked automatically (doctests)?

#### Backlog and ticket systems
Questions you can ask include:
* How are tasks in the project tracked?
* Is there a backlog, a ticket system or a bug tracker?
* How old are the last entries?
* Are the entries meaningful and understandable?
* Is there an analog system for tasks and bugs (whiteboard, pin board, notebook). This is an alternative to electronic systems.


## citable
Making Your Code Citable: https://guides.github.com/activities/citable-code/
http://zenodo.org/
