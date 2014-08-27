# Problems with legacy code

### Technical debt

What would you think if you found this piece of code?

    def repair_chain(self, a, b, c=None):
        """
        struc - a Bio.PDB object
        threshold value
        """
        #TODO: fix documentation
        ...


Looks bad enough in your own code. Now imagine finding these lines in a project you just inherited. What does it tell you about how well you will be able to work with the program?

This is called **technical debt**.

### Reasons for technical debt

Why does technical debt emerge? There are at least four reasons:

#### 1. Deadlines
A deadline means that someone determines when a program has to be ready (whatever that means). A deadline could be a paper submission, the end of a funding period or the end of a PhD thesis. All kinds of deadlines create pressure.

Pressure teases programmers to cut corners. Programmers under pressure try to get the code running, no matter what (*"I can clean this up later."*). Producing clean, transparent, well-tested code becomes a secondary issue. Small nodules of messy code will emerge, and if you rush from deadline to deadline, they will accumulate over time.

Slowing down your pace of programming under pressure takes courage.


#### 2. Lack of experience
A programmer might write code that is difficult to maintain because he doesn't know better. An unexperienced programmer thinks that programming means writing code. An experienced programmer (like anyone interested in a book on software engineering) knows that sometimes programming means writing code, and sometimes it doesn't.

Lack of experience often results in code that is unnecessary long or complicated. This may happen even to experienced programmers switching from another language. Once, we stumbled upon the following Python code fragment written by a C programmer:

    i = 0; s = []
    f = open(filename,'r')
    while 1:
	    z = f.seek(i)
    	if z==None:
    		break
    	ch = f.read(1)
    	s.append(ch)
    	i = i+1

What this code fragment does is:

    s = list(open(filename).read())

Even though Python is considered easy to learn, writing good Python code is not trivial.

#### 3. Overabundant experience

Experienced programmers can create problematic code, too. In the first place, an experienced programmer is very good to have: They write sophisticated programs incredibly quickly, master new technologies and make them work. Such programmers are rare and valuable.

The problem is that sometimes it takes another experienced programmer to understand their code. One example of such code is called **code golf**. The programmer tried to make the program work with as few key strokes as possible:

    return zip(nested, [str(x) for x in data[1:] if x.at < 1.5])

The moment an experienced programmer departs and leaves a lot of functional but hardly maintainable code, the project can suddenly go into debt.

As long as great programmers are in short supply, you need to find a workaround.

### 4. Python
Python is not the best language to support legacy code.
Pythons built-in method to check whether a program looks ok is importing modules. Importing gives you SyntaxErrors and the most crude exceptions. Unfortunately, Python does not provide you with anything more.

Even a simple bug like the following will go unnoticed:

    def get_modification_name(id):
         return DATABASE.get(idx)

Strictly typed languages like Java and C are fundamentally different. They enforce strict rules on variable types and method signatures that are checked automatically while compiling a program.

Therefore, Python is not very good at telling whether the code you took over is working. You need to add tools to improve maintainability by yourself.

### Conclusion

Technical debt is a serious problem when taking over a project. It can slow down development or even lead to a standstill. To avoid that situation, you need to figure out what the pitfalls in a project are.

The next section gives you tools to analyze a project you just got on your desk.
