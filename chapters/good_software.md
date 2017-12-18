
# How to recognize good scientific software?

With heaps of data to evaluate, scientific software has become increasingly relevant to create or evaluate results. Lots of software exists, but is it good enough for what you want to do? How can you tell whether you can trust a program to solve your problem? In the first place, you could treat an existing publication as a sign of quality. Unfortunately it is not a particularly reliable one. A publication does not tell you whether the authors are still developing their program further, whether they have stopped maintaining it, or whether the developers have switched fields altogether.

In this article, I introduce five criteria by which you can recognize good software:

![Criteria for good scientific software](images/software_qa.png)

### 1. What has the software been used for?

In the first place, scientific programs are written for a particular purpose or problem. When it is written, authors figure out that it might be useful to other scientists as well. So the authors decide to make ther program available. What is good about this kind of software is that it usually has been proven that it is good for something: you usually will find a reference reporting an experiment supported by the software.

However, sometimes software is published while such results are still being generated. Then, the program is a prototype and you might be test-driving it, which is not bad in itself, but you need to be prepared for surprises. Therefore, look out for hard data what the program has been used for. If a real research question has been answered, this is much harder evidence than a proof-of-concept or a statistical evaluation of an algorithm.

The most successful programs are the ones used over a long period of time. They are generally the most stable. If you find evidence like "Over the last two years, the program X has been used by an average of Y persons per month via our website.", you know you are on safe ground.

### 2. Are the authors responsive?

Field-testing a program is good and necessary. Scientific programmers cannot expect the same number of users as your average mobile app. Often enough, they have to do with a few dozen users, and sometimes it is just you and them. The good news is that they have time for your questions. Give the documentation a chance first, but as soon as you get stuck, write to the authors! If they care about their program, you should get a response within a couple of days. Usually, this provides both of you with useful information.

### 3. Where is the program available?

Of course, a program needs to be somewhere physically, so that you can download/install/execute it on your computer (unless you use it via a web interface). There is however more to it than putting a zip file on a web page. You can look out for instance, whether the authors have deposited their program in a public code repository like Sourceforge, Github, or Bitbucket. These havens for open-source software make it easier for someone else to join working on a project - actually, you can browse all the source code on the web pages. When you see them, it is a sign not only of collaborative spirit, but also the program is in a more neat, cleaned-up form than if it were just a collection of files. And you can be sure that it will still be there tomorrow.

### 4. How can the program be installed?

One step further, you can check whether there is an auto-installation procedure: Good signs are if the program is installable via any of PyPi, CPAN, CRAN, Maven or as an Ubuntu package. Also, if there is a separate Windows installer, a mobile app or similar thing that installs the program with a few clicks, it is a sign that the programmers made an effort for you: these things take a lot of time to build. All these tools are indicators of solid engineering practices, so if you see them it tells you the authors have thought about the sustainability of their software.

### 5. Can you prove the program works?

When you use a program, you need to be 100% sure that it does exactly what you think it does. You may very well be unforgiving in this point, especially when calculations are involved that you cannot simply double-check on a pocket calculator (which is probably why you want to use a computer in the first place). The authors are actually responsible of proving that their program does what is written in the manual. Because software changes within days or weeks, simply referring to the results section of a publication is not enough!

**How can you verify then that a program works?**

Each scientific program should include at least one set of sample data. There should be an instruction how to use the sample data and exactly what output it produces. Sometimes, this approach is broken down into small steps: a cookbook explaining small actions and their effect. Eventually, you will find an automatic test suite. This is a script that automatically checks whether different parts of the program work correctly. When you see a message like


    110 of 110 tests OK.

you know that at least everything the developers felt important to check works.

All of these methods have in common that some input data with a known output is used. They allow you to verify whether the program works now and on your computer, as opposed to 'A long time ago, far far away...'

### Conclusions

If a program fails several of the above quality indicators, it does not mean that the program is bad or that the authors can't program. Probably you are seeing only a tiny bit of all the work that went into the software. But it also means that your risk of usage is higher. If the software you are using is a prototype (and many projects never leave that stage), one of the best things you can do is to contact the authors directly. This is beneficial for both of you. 

The list in this post is incomplete. If you are an author and I missed your favorite engineering technique, or if you use scientific software and have a suggestion what would make your life easier, drop me a line.

### Acknowledgements
Thist text emerged from a discussion round at the GFZ Potsdam, with special support from Bernadette Fritsch, Björn Brembs, Dominik Reusser and Jens Klump.
