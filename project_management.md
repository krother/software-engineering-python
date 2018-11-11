
# Software Project Management

**Managing software projects is difficult.**

## Uncertainty

**Do you know where you are going to be next week?** Probably, you do.

**Do you know where you are going to be in the summer three years from now?** Probably not.

There is a lot of uncertainty in the second question. You can't look ahead too far. When developing software it is the same: There is a lot of uncertainty, only the horizon begins to become blurred much earlier: within weeks, days or even hours.

Programming projects change and evolve for a multitude of reasons:

* your users request changes.
* bugs need to be fixed.
* the libraries you use evolve. 
* external requirements (e.g. regulations) change.
* you have ideas you want to implement.

Change is inevitable.

## Waterfall

Naively, one could try to structure a programming project as consecutive steps, known as the **Waterfall model**.

![Waterfall](waterfall.png)

Because of the nature of change, the waterfall model only works for projects where you know the problem *and* the technologies very well. Even then, the program will need to be maintained afterwards. 

In practice, there are no finished programs.

It is more helpful to think of programming as an ongoing activity, like gardening.


## Supervisors

One thing that makes software projects difficult for managers is that they cannot see a half-finished program. Many times, they will ask questions like:

    "When will the program be finished?"

It is very difficult for non-programmers to understand that this question is meaningless. You might as well

Therefore it is challenging to make managers happy and get them out of the way at the same time. The key to make managers contribute something useful is of course *communication*. Some things that might help you:

* learn what real-world problem you are solving.
* develop clear, specific goals together.
* write a specification. Split it into smaller steps (e.g. User Stories and Use Cases).
* do not discuss whether or not to use tools like testing. You wouldn't discuss whether to use `for` or `while` with your manager either.
* demonstrate a small working version early.
* learn about the Agile methodology, but do not become attached to it


## What does 'done' mean?

Have you encountered the following situation in a programming project? The project is divided into tasks, the tasks are placed in an electronic tracking system or as cards on a task board. After some time, programmers declare they are finished: Some come up with a basic solution very quickly and prefer to take care of special cases and cleanup work later. Others invest a lot of time into building a solid, maintainable structure. The former carries the risk that problems get swept under the rug and technical debt is accumulating, the latter that tasks linger in a half-done state forever. Moreover, your team may disagree to what extent a task needs to be implemented to count as “done”. How can you as a project manager know what your team means by “done”?

Historically excessively detailed specifications were used to describe what a program should do (and often still are). But in many programming projects this approach is too clumsy. User Stories, cards describing features in a few words, provide a short objective description, but they do not represent the engineering details. Methodologies like SCRUM admit that “done” in programming can be interpreted in many ways. They claim that an important prerequisite for productivity is that “done” means the same thing to all people involved. This has resulted in a pragmatic solution: the “definition of done”.

The “definition of done” is a convention the programming team creates. It is a list of simple, criteria a task must pass in order to count as 'done'. The definition could include “the code is in the repository”, “the code has been released on the server”, “automatic tests have been written” etc. All criteria must be objective and easy to check. The “definition of done” represents a quality standard and reflects the engineering practices used by the team.

Creating and agreeing on a “definition of done” may require intensive discussion among team members, but it is worth it: Once established, the team knows what everyone of them means when they say something is “done”, a quality standard is established, and the experience helps the team to grow together.
