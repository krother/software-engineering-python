
# Exercises

## Part 1: Version control

We will use the **Version Control System git**.

### Exercise 1.1: Explore the git homepage

### Exercise 1.2: Clone a repository

Open a terminal (on Windows search for *git bash*) and copy the repository from GitHub to your computer:

    git clone https://github.com/lenarother/ProfesjonalneProgramowanie.git

and
 
    cd ProfesjonalneProgramowanie

See which files appear on your computer.

### Exercise 1.3: Run the program

Execute the program `emo1.py`. On Windows, open the program by right-clicking and selecting IDLE. Then press `F5`.

### Exercise 1.4: Change the program

Edit the program, so that it converts one additional word to an emoticon.

Afterwards, type in the terminal

    git status

and

    git diff

Explain what you see.

### Exercise 1.5: Add changes to version control.

First, inform `git` that you want to record changes in one file

    git add emo1.py

See what has changed when running

    git status

Write changes to the internal journal of `git`:

    git commit -m "added new emoticon"

and
  
    git status

### Exercise 1.6: Examine project history

You can see what other people have done before you with

    git log


## Part 2: Automated Testing

### Exercise 2.1: Run a test

Open the file `test_emo.py`. Execute it by pressing `F5`. What does it do?

### Exercise 2.2: Write a test

Write another test for the emoticon you added. Run the tests again. 

Why does the test fail?

### Exercise 2.3: Implement the code

Add some code to `emo2.py` to make the test work.

Run the test again.

### Exercise 2.4: What does a test tell you?

Discuss the following questions:

* What information do you get when a test passes?
* What information do you get when a test fails?

