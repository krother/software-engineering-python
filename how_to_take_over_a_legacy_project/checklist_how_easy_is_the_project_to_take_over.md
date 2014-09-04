### The Legacy Metric in real life
Your Legacy Metric should now consist of:

* A **complexity value** ranging from 0 (simple) to 9 (awfully complicated) .
* An **engineering quality value** ranging from 0 (messy) to 5 (well-kept).

You can use both values as coordinates:

![Engineering points over project complexity](engineering_points.png)

How can you interpret this graph?

We decided to give you a couple of examples how we would assess the situation.

#### Kristian
Bio: *Programming since 1988, Python since 1999, has also been in touch with Assembler, BASIC, JAVA, C,  PASCAL. No formal CS education, but lots of practical experience. Loves firefighting.*

#### Magdalena
Bio: TODO

### The Modomics project
estimate to the moment it was first handed over in 2007:

**Complexity: 6 points** (2 for LOC, 3 for components, 1 platform)
**Engineering: 1 points (repository)

**Kristian**: "*As I told, the project was challenging back in 2007. In a project like this, I would not expect anything technically challenging. It is structuring a project like this that makes adding even small features and debugging a daunting task. My approach would be to start with rigorous testing."*

### Twenty Characters
A small project to draw amino acid sequences with a calligraphic font.

346 LOC
Python only
Linux command line only
--> complexity 1

No repository until writing of this chapter
No installer script
Test coverage 31%
pylint score 6.27
24 modularization units
--> quality 2

**Kristian**: *This should be a piece of cake, simply because the program is so small. The code quality is more than sufficient for a quick start.*

