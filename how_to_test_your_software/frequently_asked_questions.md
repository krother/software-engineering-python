# Frequently Asked Questions

#### Q: Isn’t writing tests a waste of time?
Writing tests pays off after a few rounds of bug fixing and/or refactoring. The main benefit is that you never will have to worry about the same bug twice. However, the overall cost of testing depends on the size of the project and the abilities of the programming team. The project size a single experienced programmer can handle without automatic tests is bigger than that of a team with mixed skill levels.

#### Q: How can I add tests to an existing project in reasonable time?
The trick is to test just enough to keep on developing. Writing as much as one test should already help. To drive your development forward, aim at building tests that fail (for features you have not implemented yet, for bugs you still need to fix etc).

#### Q: Can (or should) you test everything with automatic tests?
You don't need to. Start with tests for new features and bugs. You can add more tests later. When you need a highly reliable component, though, it is useful to test close to everything. For an example how far you can go with testing, see [7] or http://www.diveintopython.net/unit_testing/index.html.

#### Q: What if there are bugs in my tests?
Of course both the program and the test code may contain bugs that cause an automatic test to fail. Thus, taking correct tests for granted may be a bad idea. Fortunately, test code is usually much simpler, so that it is easier to make sure that your tests work correctly.

#### Q: How can I test complicated output (e.g. a big string or text file)?
Try to decompose the tests in the same way as you decompose your code. Ideally, you test individual components of the program independently (Unit Tests). The smaller the components, the better. If feel that your output is monolithic and therefore hard to test (e.g. a big string) it might be a good time to refactor the code into more independent components.

#### Q: When requirements change, won’t your test set become obsolete?
If the requirements for the entire project change rapidly, testing may not worthwhile indeed. But some change is normal and editing tests can actually help you identify what you need to change. Generally, start writing tests for what you are sure will not change: That the program finishes without an error, that it produces an output file, that the output file is not empty, etc. Even if such tests may seem trivial, they will cover a lot of your operational code.

#### Q: Won’t my tests be redundant if I write tests for many different situations?
A test suite evolves like any program: it grows, changes, and needs to be refactored from time to time. To avoid testing too much, keep an eye on test coverage (calculated by the figleaf program). Test coverage is the number of code lines executed by your tests. 50% test coverage is a bare minimum, 75% is comfortable, 90% is good, 100% is a luxury (unless you are writing a language compiler - then 100% test coverage is the bare minimum).
