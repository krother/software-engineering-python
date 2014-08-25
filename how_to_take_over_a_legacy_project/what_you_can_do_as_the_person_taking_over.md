# What you can do as the person taking over

### pylint
* gives you a quick ballpark figure how bad the situation is
* pay attention to warnings about 'too many methods per class' / 'functions per module'.

### tests
* example data
* automatic tests
* test coverage
* paper, reproduce results. If this is not possible,

### documentation
Yes it is usually bad. If there is good documentation usually everything else is in place.

Fortunately lack of documentation is easy to replace: You need the former contributor next to your desk at least for some time. If you simply get handed the code and your predecessor departs for vacations or forever, expect big trouble.

### deployment
* unusual dependencies
* can you build/install the program without further information?

### Check these factors before taking over
There is one argument why you should insist on inspecting the code: Your supervisor might not be aware of that the project is booby-trapped. A program that looks good from the outside (e.g. a shiny GUI or web interface) and has produced scientific results may seem flawless from a supervisors perspective. It may still be entirely rotten from the inside.


### Rewriting the code
There is no recycling bin for code. There is nothing bad about throwing away code. If it does not work, write it from scratch.
Reasons why many programmers don't is taking pride in someone's code. Also non-developers tend to interfere, because they think if part the code is already there, a part of the problem is already solved.

*Brooks: Prepare to throw one away*


