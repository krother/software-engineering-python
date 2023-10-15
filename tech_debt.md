
#  Technical Debt

## What is technical debt?

If refactoring is ignored a project may accumulate **Technnical debt**.
**Technical debt** is a frequent problem in projects evolving over time.
It includes:

* lack of documentation
* lack of structure
* badly written code
* code that breaks in special cases
* bugs
* .. and many more

This phenomenon has also been described as [**software entropy**](https://en.wikipedia.org/wiki/Software_entropy) and [**Lehmanns Laws**](https://en.wikipedia.org/wiki/Lehman%27s_laws_of_software_evolution).

----

## How does technical debt emerge?

There are at least six reasons why technical debt accumulates:

### 1. Haste

**Pressure to finish quickly** teases programmers to cut corners. Programmers under pressure try to get the code running, no matter what (*"I can clean this up later."*). Producing clean, transparent, well-tested code becomes a secondary issue. Small nodules of messy code will emerge, grow, accumulate, and if you rush from deadline to deadline, the program becomes a jungle.

Slowing down your pace of programming under pressure takes courage.

### 2. Misunderstanding the problem

When you first write a program, you are making assumptions about the real-world problem it solves. Almost inevitably, some of these assumptions turn out to be wrong. Every time you add new code to correct your wrong assumptions, they will lay a burden on the original design – unless you clean up properly.

Because of that, the milestone book *"the mythical man-month"* (Brooks, 1963) states: *"Be prepared to throw one away."*

### 3. Lack of experience

A programmer might write code that is difficult to maintain because he doesn't know better. An unexperienced programmer thinks that programming means writing code. An experienced programmer - like anyone interested in a book on software engineering - knows that sometimes programming means writing code, and sometimes it doesn't.

Lack of experience often results in code that is unnecessary long or complicated. This can happen even to experienced programmers switching from another language. Once, we stumbled upon the following Python code fragment written by a C programmer:

    i = 0; s = []
    f = open(filename,'r')
    while 1:
	    z = f.seek(i)
    	if z==None:
    		break
    	ch = f.read(1)
    	s.append(ch)
    	i = i+1

This code fragment can be written as:

    s = list(open(filename).read())

Even though Python is considered easy to learn, writing good Python code is not trivial.

### 4. Overabundant experience

Experienced programmers can create problematic code, too. In the first place, an experienced programmer is very good to have: They write sophisticated programs incredibly quickly, master new technologies and make them work. Such programmers are rare and valuable.

The problem is that sometimes it takes another experienced programmer to understand their code. One example of such code is called **code golf**. In code golf, the programmer tries to implement a program with as few key strokes as possible:

The moment an experienced programmer departs and leaves a lot of functional code that is hard to read, the project can suddenly go into debt.


### 5. Python

Python checks for SyntaxErrors and the most obvious exceptions at runtime. Unfortunately, Python does not notice much more.

Even a simple typo like the following could pass unnoticed:

	  idx = 3

    ...

    def get_modification_name(ids):
         return DATABASE.get(idx)    # should be ids

When you move this function to a separate module during a refactoring session, the code will break, thus revealing the bug.

### 6. Changes in the environment

Even if your program is written perfectly, it will slowly deteriorate. The libraries it uses may deprecate methods, new string encodings, display sizes, new customer wishes and other changes mean that your program is becoming less useful. To stay up to date technically, the code needs to adapt.
