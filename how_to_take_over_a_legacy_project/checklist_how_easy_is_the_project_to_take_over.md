### Checklist: How easy is the project to take over?

Use the checklist to assess a project your are taking over before you start coding.

#### Project complexity
- [ ]  How many lines of code (LOC) do you have (1+ points)? MR: hard
- [ ]  How many separate components (languages, databases etc.) are there (1+ points)? MR: hard
- [ ]  How many different platforms will the program be deployed to (1+ points)? MR: hard

#### Code quality
- [ ]  Does pylint give an average score of &gt;5.0? MR: hard
- [ ]  Does pylint warn you about unknown variables? MR: hard
- [ ]  Do functions and classes have docstrings? MR: hard
- [ ]  Are variable names understandable? MR: soft [to make it hard: are the names consistent with pep8, Soes pylint worns about incorrect variable names, alternatively change to warning about too many arguments for function or branches i if/for]
- [ ]  Is the code divided into modules, classes and functions of reasonable size? MR: soft [to make it hard: do you have files >= 1000 LOC, is everage size of function larger than 30 LOC; is the division itself hard?]

#### Engineering infrastructure
- [ ]  Is there a repository? MR: hard
- [ ]  Are there any automatic tests? MR: hard
- [ ]  Can you install/deploy the program by yourself? MR: soft [to make it hard: is there a written down release instruction that says which steps to fallow to release?]
- [ ]  Is understandable documentation available? MR: soft
- [ ]  Is there a backlog or ticket system? MR: hard

#### People
- [ ]  Do you have a chance to meet the former developer regularly? MR: soft [what if you don't like each other] 
- [ ]  Are there other developers actively involved? MR: soft [is it good or bed? At the end of rxncon it helped, at the begining it was hard because our boss was menaging our work independantly so we were getting many conflicts in the repo all the time]
- [ ]  Are there users you can talk to on a regular basis? MR: soft
- [ ]  Are you going to use the program yourself? MR: hard
- [ ]  Do you know all languages / technologies used? MR: hard

## Using the checklist
MR: Could be more general not only about complexity.

You can combine the three numbers from the sections above to a single complexity value ranging from 3-16 points. MR: Why 16?

MR: Would be nice to have some comments on how to assign these points. e.g. something like: It means that, if you consider LOC, if you have 100-line script to debug, it will have score 1, if you have code with 30 000 lines that it will be 5, and evrything inbetween is your subjective evaluation of the program size.   

    complexity = LOC + components + platforms

Some developers might argue what is the correct formula to combine the three values. The actual amount of work required might as well be exponential to the complexity. We don't know for sure.

What we know is that the comlexity lets you describe the size of the project: 5 is comfortable, 8 is challenging, and 12 means that it probably is going to be tough.

