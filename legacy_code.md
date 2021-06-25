# How to work with legacy code?

## In this chapter you can learn:

* why problems with legacy code emerge
* how to quickly assess the complexity and engineering quality of a project
* strategies to overcome initial difficulties

## The Modomics story

In March 2007 I inherited the [Modomics database](http://www.genesilico.pl/modomics) from Staszek, a MSc student in the lab. Staszek handed me the code and the server passwords. Then he moved to Germany. Although he did whatever he could to support me by email, a sackful of knowledge moved away with him.

![Modomics](images/modomics.jpg)

There was a hard deadline for publication in June. In May, the hard disk of the server crashed. I restored most of the code from the SVN repository and loaded the database dump. However, some features were lost on the way. I was determined to not only fully recover the project, but also to add enough value to submit the publication on time.

Working on the code was tough: *"What does this mean? How does this work? Why is this character on the web page three positions further to the left than it should?"* I frequently found myself tracing Python & HTML code line by line. As a result, adding even small features and debugging became a daunting task.

When the deadline drew near, I worked literally every minute, including late evenings and weekends, until the very last moment. I was constantly overslept and emotionally brittle to the point of resignation. It took me a year to realize the correct term for this: burnout.

I missed the deadline, or to be precise, my supervisor hit the **STOP** button in time. He decided to postpone submission by one year. An extra year was the best thing that could happen to the project and its maintainer. First of all, I relaxed. Second, I spent more time talking to scientists using the website and understood better what they needed. Then, I cleaned up many big and small issues: I drew a data model for the database, refactored smaller components with descriptive names and wrote unit tests.

In the end, I had rewritten much of the code. The site was working, the publication got accepted.

Finally, after two more years, it was time to hand over the project to my successors Sebastian and Kaja. The first thing Sebastian did was that he dumped most of my code and rewrote the site in Django within two weeks. Kaja kept on maintaining the server diligently for years, and so the database lives on until the day I write these lines, with different code, but the same vision it was originally created with.

What I learned is that taking over a program from someone else is difficult.


#### Project summary

| Name | Modomics |
|------|----------|
| Summary | Web database of modified RNA nucleotides. |
| Duration | 2006 - 2014 |
| Developers | 2 coders (2009) |
| Stakeholders | 2 senior scientists, 4 data curators (2009) |
| Size | ~10000 Python LOC |
| Technologies used | TurboGears web server <br> PostGreSQL database <br> Biopython <br> PIL |
| Development tools used | bug tracker (TRAC) <br> automatic tests (partial) <br> SVN repository <br> User Stories <br> Entity-relationship diagram |
| Reference | Machnicka MA, Milanowska K, Osman Oglu O, Purta E, Kurkowska M, Olchowik A, Januszewski W, Kalinowski S, Dunin-Horkawicz S, Rother KM, Helm M, Bujnicki JM, Grosjean H. MODOMICS: a database of RNA modification pathways: 2012 update. Nucleic Acids Res 2013 Jan 1;41(D1): D262-D267 |

----

## Assessing a Legacy Project

When you take over a project, you need to find out first what you got yourself into. There are two aspects to consider before you can decide what to do:

1. How complex is the project?
2. How well-engineered is the code?

Intuitively, you would expect the according graph to look like this:

![Simple assessment graph](images/legacy_graph_simple.png)

In the section on **Code Metrics**, you will find questions to assess complexity and engineering quality in a project *before* you take it over.


## What you can do when you take over a project

Once you figured out what situation you got yourself into, you probably want to get to work. What can you do to get a firm hold on the code you inherited? Here you find eight options.

### 1. Abandon
There may be good reasons to jump ship while still in the harbour. A clean decision to stop a project altogether can save you months or even years of pain and struggle. If it turns out that the project is unmaintainable later, abandoning it immediately is much cheaper. Convincing others of this option will be difficult. Consider it a last resort.

### 2. Rewrite
Imagine you have built a small Cessna airplane, but figure out that you really need a Boeing 727. Nobody would say *"Oh, great, you have a pair of wings already."* You would need to build an entirely new plane. It is the same with programming. There is nothing bad about throwing away code. It does not take up space and does not pollute the environment. If the code works, but you can't work with it reasonably, write it from scratch.

Rewriting a program happens frequently, and often it is faster than fixing the old one. Fred Brooks (The Mythical Man-Month, 1982, p115ff.) recommends even to plan for throwing away the first design. Incorporating some parts from existing code into a new design is less risky than assuming all existing parts can be reused.

### 3. Reduce complexity
The trouble of maintaining a project successfully can be diminished by kicking out some features. Possibly the project does things that have a very low priority or turned out to be not important anyway.

One way to increase maintainability with a simple decision is to reduce the number of supported platforms to one. Maintaining a web-only or source-only version instead of three operating systems and a browser interface in parallel gets plenty of problems out of the way. Consider focusing on one platform until you feel familiar enough with the project to expand.

### 4. Cleanup time
Cleaning up improves the quality of your project. Increasing engineering quality takes time. You may consider spending at least some to add things that were missing from the engineering score. Create a repository. Create an installer. Write a few automated tests (this will pay off very quickly). Run **pylint** and improve your score. The latter is a great way to familiarize with the code while improving things.

### 5. Divide and conquer
Separate portions of your code and clean them up one by one. Create separate functions, classes, modules, libraries from larger blobs and test them. If done consequently, you can either isolate the messy parts or reduce them to small portions that you can handle with ease.

Michael Feathers proposes a five-step process to divide code into smaller chunks (*Feathers, Michael. Working Effectively With Legacy Code, Prentice Hall PTR, 2005*):

1. Find change points in the code (portions that can be separated).
2. Find test points.
3. Break dependencies.
4. Write tests.
5. Change the code and refactor.


### 6. Identify people who can support you

Code does not exist by itself; it is maintained by persons. When you start work on a legacy project, there are four main players who might be able to help you:

#### The former developer
Do you have a chance to meet the former developer once per week? Daily? Whenever you need? Is he able to support you directly during a transition period? Can you meet face-to-face?

#### Other developers
Are the more people who have worked with the code? Are they still actively involved? A co-developer is a valuable source of information, because often they view the code from a similar perspective as you.

#### Users
Does the program have active users? Can you talk to them on a regular basis? Do you need the program yourself? Real users help you to understand what matters and motivate you to keep going.

#### Your supervisor
Is your supervisor aware of the state of the project? Can you discuss technical issues with him or a trusted mentor? Do you receive a clear vision or next major step for the project? Maybe your supervisor has been in a similar spot before and give you some valuable hints.

----

### 7. Mission Impossible Game
The [Mission Impossible Game](http://www.gamestorming.com/games-for-design/mission-impossible/) is a brainstorming method. The art of brainstorming is to first ask the right question. Then take decisions.

In the Mission Impossible Game you collect actionable ideas to work with legacy code. Ask: *"How to prepare the next release of our program in one day?"*. Collect ideas for half an hour.

Then, choose the ideas most relevant for the project vision, discard the others and get working.

### 8. Change one thing at a time
How many of the main parameters of the project will change the moment you take over? Things that could change include the team composition, project size, goals, features and platforms. Ideally only one parameter should be changed at a time.

The moment you take over as main developer, the team composition changes in any case. That means, nothing else should change. Spend some time making yourself comfortable with the code, working on small issues. You may allocate a week or more to learn a technology crucial to the project which you don't know yet. Don't start revolutions on day one. When you feel the code has become *yours*, it is time to enter the next development stage.

## Things that help

* give an incoming programmer authority to change everything.
* give an outgoing programmer an incentive to contribute (publications, open-source)
* encourage other people to take side roles in the project early. --> you have a backup, they have a side project, and the main dev is forced to explain his code to someone else
* Change one parameter at a time (Vision, Features, Platform, Developers)
