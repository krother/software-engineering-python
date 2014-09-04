# Consequences

Once you figured out what situation you got yourself into, you probably want to get to work. What can you do to get a firm hold on the code you inherited? Here you find a few options.

### Abandon
There may be good reasons to jump ship while still in the harbour. A clean decision to stop a project altogether can save you months or even years of prolonged struggle. If it turns out that the project is unmaintainable later, abandoning it immediately is much cheaper. Convincing others of this option will be difficult. Consider it a last resort.

### Rewrite
Imagine you have built a small Cessna airplane, but figure out that you really need a Boeing 727. Nobody would say *"Oh, great, you have a pair of wings already."* It is the same with programming.

There is nothing bad about throwing away code. It does not take up space and does not pollute the environment. If the code works, but you can't work with it reasonably, write it from scratch.

Rewriting a program happens frequently, and often it is faster than fixing the old one. Fred Brooks (The Mythical Man-Month, 1982, p115ff.) recommends even to plan for throwing away the first design. Incorporating some parts from existing code into a new design is easier than assuming all existing parts can be reused.

### Reduce scope
The trouble of maintaining a project successfully can be diminished by kicking out some features. Possibly the project does things that have a very low priority or turned out to be not important anyway.

One way to increase maintainability with a simple decision is to reduce the number of supported platforms to one. Maintaining a web-only or source-only version instead of three operating systems and a browser interface gets plenty of problems out of the way.

### Divide and conquer
The idea of this technique is to separate portions of your code and clean them up one by one. Create separate functions, classes, modules, libraries form larger blobs and test them. If done consequently, you can either isolate the messy parts or reduce them to small portions that you can handle with ease.

Michael Feathers proposes a five-step process to divide code into smaller chunks (*Feathers, Michael. Working Effectively With Legacy Code, Prentice Hall PTR, 2005*):

1. Find change points in the code.
2. Find test points.
3. Break dependencies.
4. Write tests.
5. Change the code and refactor.


### Identify people who can support you

Code does not exist by itself; it is maintained by persons. When you start work on a legacy project, there are four main players who might be able to help you:

#### The former developer
Do you have a chance to meet the former developer once per week? Daily? All the time? Preferably face-to-face, or on-line. Is he able to support you directly during a transition period?

#### Other developers
Are the more people who have worked with the code? Are they still actively involved? A co-developer is a valuable source of information, because often they view the code from a similar perspective as you.

#### Users
Does the program have active users? Can you talk to them on a regular basis? Do you need the program yourself? Real users help you to understand what matters and motivate you to keep going.

#### Your supervisor
Is your supervisor aware of the state of the project? Can you discuss technical issues with him or a trusted mentor? Do you receive a clear vision or next major step for the project? Maybe your supervisor has been in a similar spot before and give you some valuable hints.

#### Co-location
The importance of co-location is frequently underestimated. Yes, there are companies where remote work is common. Some of them are even famous, like [37signals](http://www.37signals.com). As long as the work is easy, this is fine. However, taking over legacy code is not, and this is why we emphasize looking persons in the eye.

If you can, spend some time with your predecessor or stakeholders in the same room, working on the project together. Depending on the size of the project, this may take days or weeks. Coming to grips with the project by direct contact can save plenty of time later.

### Mission Impossible Game
The [Mission Impossible Game](http://www.gamestorming.com/games-for-design/mission-impossible/) is a brainstorming method. The art of brainstorming is to first ask the right question. Then take decisions.

In the Mission Impossible Game you collect actionable ideas to work with legacy code. Ask: *"How to prepare the next release of our program in one day?"*. Collect ideas for half an hour.

Then, choose the ideas most relevant for the project vision, discard the others and get working.

### Change one thing at a time
How many of the main parameters of the project will change the moment you take over? Things that could change include the team composition, project size, goals, features and platforms. Ideally only one parameter should be changed at a time.

The moment you take over as main developer, the team composition changes in any case. That means, nothing else should change. Spend some time making yourself comfortable with the code, working on small issues. You may allocate a week or more to learn a technology crucial to the project which you don't know yet. Don't start revolutions on day one. When you feel the code has become *yours*, it is time to enter the next development stage.
