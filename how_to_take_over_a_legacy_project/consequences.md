# Consequences

What measures (MR actions/means) can you take to get a firm hold on the code you inherited? Here you find a few options.

### Terminate
A clean decision to stop the project altogether can save you months or even years of prolonged struggle. If it turns out that the project is unmaintainable, there may be no other way out. Because efforts invested will be lost, convincing others of choosing this option will be difficult. Consider it as a last resort.

### Rewrite
Imagine you have built a small Cessna airplane, but figure out what you really need is a Boeing 727. Nobody would say *"Oh, great, you have a pair of wings already."* It is the same with programming.

There is nothing bad about throwing away code. It does not take up space and does not pollute the environment. If the code does not work, write it from scratch.
MR: What if it works 'but only'?

Rewriting a program happens frequently, and often it is faster than fixing the old one. Fred Brooks (The Mythical Man-Month, 1982, p115ff.) recommends to even plan for throwing away the first design. Incorporating some parts from existing code into a new design is easier than assuming all existing parts can be reused.

#### Reduce scope
The trouble of maintaining a project successfully can be diminished by kicking out some features. Possibly the project does things that have a low priority or turned out to be not important anyway.

One way to increase maintainability with a simple decision is to reduce the number of supported platforms to one. Maintaining a web-only or source-only version instead of three gets plenty of problems out of the way.

### Divide and conquer
The idea of this technique is to separate and clean portions of your program one by one. Create separate functions, classes, modules, libraries of larger blobs and test them one by one.

Michael Feathers proposes a five-step process to divide code into smaller chunks (*Feathers, Michael. Working Effectively With Legacy Code, Prentice Hall PTR, 2005*):

1. Find change points in the code.
2. Find test points.
3. Break dependencies.
4. Write tests.
5. Change the code and refactor.

### Co-location
If you can, spend some time with your predecessor in the same room, working on the project together. Depending on the size of the project, this may take days or weeks. Coming to grips with the project this way can save plenty of time later. It requires the outgoing programmer to share his knowledge willingly and give away responsibility. As long as there is an incentive for all parties involved, this is one of the best ways to transfer a project.

### Mission Impossible Game
The [Mission Impossible Game](http://www.gamestorming.com/games-for-design/mission-impossible/) is a brainstorming method. The art of brainstorming is to first ask the right questions. Then take decisions.

In the Mission Impossible Game you collect actionable ideas to work with legacy code. Ask: *"How to prepare the next release of our program in one day?"*. Collect ideas for half an hour.

Then, choose the ideas most relevant for the project vision, discard the others and get working.

### Change one thing at a time
How many of the main parameters of the project will change the moment you take over? Things that could change include the team, project size, goals, features and platforms. It is generally a good idea to change only one parameter at a time.

That means, the moment you take over as main developer nothing else should change. Spend some time making yourself comfortable with the code, maybe fixing small issues. When you feel the code has become *yours*, it is time to enter the next development stage.

