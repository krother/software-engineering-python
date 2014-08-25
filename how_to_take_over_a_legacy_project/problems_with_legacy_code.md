# Problems with legacy code

### Technical debt
cutting corners because of velocity:
* funding deadlines
* end of PhD thesis
* multiple projects
* papers

To illustrate what technical debt means, consider finding this in your code:


    def repair_chain(self, a, b, c=None):
        """
        struc - a Bio.PDB object
        threshold
        """
        #TODO: fix documentation
        ...


Looks bad enough in your own code. Now imagine finding these lines in a project you just inherited. What does it tell you about how well you will be able to work with the program?

### The genius hacker dilemma
A genius hacker is a person who is good at programming. Very good. They write sophisticated programs incredibly quickly, make them work and fulfill all requirements. These programmers are a rare breed and valuable to have.

The problem is that it takes another genius hacker to read their code. Reading and understanding code written by an average coder is demanding enough. The moment a genius coder departs, leaving a lot of functional but hardly maintainable code can spell disaster to a project.

As long as geniuses are in short supply, you need to have a workaround.

### Code golf


    return zip(nested, [str(x) for x in data[1:] if x.at < 1.5])


### Python is not the best language for legacy code
Pythons built-in way to check whether a program looks ok is importing. This gives you SyntaxErrors and the most crude exceptions that appear during import. Unfortunately, Python does not provide you with anything more.

Even a simple bug like the following will go unnoticed:

    modomics.py

    def get_modification_name(id):
         return DATABASE.get(idx)


Therefore, Python is not very good at telling whether the code you took over is working. Strictly typed languages like Java and C enfore more strict rules that can be checked automatically while compiling the program

Python good for rapid prototyping, but bad for legacy code.
