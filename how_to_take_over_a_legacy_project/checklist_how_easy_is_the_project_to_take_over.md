### Checklist: How easy is the project to take over?

Use the checklist to assess a project your are taking over before you start coding.

#### Project complexity
- [ ]  How many lines of code (LOC) do you have (1+ points)?
- [ ]  How many separate components (languages, databases etc.) are there (1+ points)?
- [ ]  How many different platforms will the program be deployed to (1+ points)?

#### Code quality
- [ ]  Does pylint give an average score of &gt;5.0?
- [ ]  Does pylint warn you about unknown variables?
- [ ]  Do functions and classes have docstrings?
- [ ]  Are variable names understandable?
- [ ]  Is the code divided into modules, classes and functions of reasonable size?

#### Engineering infrastructure
- [ ]  Is there a repository?
- [ ]  Are there any automatic tests?
- [ ]  Can you install/deploy the program by yourself?
- [ ]  Is understandable documentation available?
- [ ]  Is there a backlog or ticket system?

#### People
- [ ]  Do you have a chance to meet the former developer regularly?
- [ ]  Are there other developers actively involved?
- [ ]  Are there users you can talk to on a regular basis?
- [ ]  Are you going to use the program yourself?
- [ ]  Do you know all languages / technologies used?

## Using the checklist
MR: Could be more general not only about complexity.

You can combine the three numbers from the sections above to a single complexity value ranging from 3-16 points. MR: Why 16?

MR: Would be nice to have some comments on how to assign these points. e.g. something like: It means that, if you consider LOC, if you have 100-line script to debug, it will have score 1, if you have code with 30 000 lines that it will be 5, and evrything inbetween is your subjective evaluation of the program size.   

    complexity = LOC + components + platforms

Some developers might argue what is the correct formula to combine the three values. The actual amount of work required might as well be exponential to the complexity. We don't know for sure.

What we know is that the comlexity lets you describe the size of the project: 5 is comfortable, 8 is challenging, and 12 means that it probably is going to be tough.

