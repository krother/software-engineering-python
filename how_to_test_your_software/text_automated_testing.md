# Text: Automated Testing
How do you know that your program is working? Jacob Kaplan-Moss, one of the authors of the Django web framework said: “code without tests is broken by design” [1]. Testing software is a must-do. But manual testing is time-consuming and prone to errors. The solution we propose here is to automate the tests.

Automatic testing means writing a dedicated set of functions that check whether certain program features work or not. An automatic test set gives you an objective measure of how much of the program works. Over time, this accelerates development, because you can rely on a fast automatic procedure to test already existing features. The bigger your program grows, the more you profit from automatic testing.

## Testing in Python

In a dynamically typed language like Python, testing is even more important, because no errors will be caught during compilation (maybe with the exception of SyntaxError and ImportError). In Python, you can implement tests informally as a series of if and print statements, or using a testing framework, like unittest. The unittest framework gives you a clean object-oriented structure that lets you run all tests or select a few, and generates concise reports on-the-fly. Some Python applications in bioinformatics like Biopython [2], PyCogent [3] and ModeRNA [4] come with automatic test suites.

## Test-Driven-Development

Intuitively, one would first write a program and then test it. Many developers however, strongly recommend the inverse: Write a test first, and only then implement the according code. This approach is called Test-Driven-Development (TDD). TDD can help you to develop useful programs, because in order to write a test, you need to fully understand what that the program should do – funnily this is much less the case with operational code.

TDD also motivates programmers [5]; when you see your tests switching from “fails” to “OK”, this is much more enticing than “Oh my, do I need to write tests for all that code?” TDD works well even if you write a single test, and then add sufficient code for that test to pass. We found writing tests first particularly useful during debugging: Whenever we found a bug in the program, we added a test function for that bug and only then fixed it. This approach guarantees that you not only have fixed the bug, but you also will notice if the same problem re-occurs in the future.

Taken together, automatic testing proves whether your program works. Being technically cheaper than manual tests it saves you time as your project gets bigger. It is not by chance that both automatic tests and TDD are seen as a central best practice in Agile methodologies. Automated testing is a safety net that helps you to produce code that is working by design.

## Types of Tests

### Unit Tests
Tests for a single function, class or module. Unit tests allow quickly proving that a single piece of code fulfills its basic requirements. Unit tests may be detailed and nitpicky. A good Unit Tests covers border cases, such as empty input, long input, weird input etc.

### Acceptance Tests
Tests a feature from the users point of view. Acceptance tests check whether a program as a whole works “as advertised”. A typical acceptance test runs a program or application as a whole on sample input and checks key features of the output. Acceptance tests do not need to test every thinkable situation (this is what Unit tests are for).

### Integration Tests
Test collaboration between two or more functions/classes/modules. Conceptually they are between Unit and Acceptance tests.

### Performance Tests
Test whether a program runs as fast or memory-efficient as it should be. Because this can be time-consuming, it makes sense to keep performance tests separate from other tests.

### Regression Tests
Tests run after refactoring to check whether everything still works. Regression Testing ideally includes running all of the above.

## Benefits of automated testing
* You know exactly what a function/class/module is expected to do.
* You can actually prove it really does.
* After adding new features you can be sure that old features still work.
* Bugs that break existing features are easier to notice.
* Much faster than manual checking of program features.
* Combines well with pair programming.
* Writing tests before writing code forces you to formulate precise requirements.
* Testing prevents coding too much. When all test cases pass, you are done.
* When refactoring code, it assures you that the new version behaves the same way as the old version.
* unittest is installed by default.
* Testing covers your back when someone comes screaming that your latest change broke their code.

## Drawbacks of testing
* Takes more time at the beginning.
* It still doesn't guarantee that you will find or avoid all bugs.
* You can have bugs in your tests as well.
* Increases the program size (in LOC).
* unittest is a little more wordy than other Python testing frameworks.
* Web pages and graphics are hard to test with unittest alone.
