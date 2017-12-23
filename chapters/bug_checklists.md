
# Bug Checklist

## SyntaxErrors

* Check the line in the error message
(and the line before).
* Check for missing colons or brackets.
* Check whether spaces and tabs for
indentation are mixed.
* Comment the line. Does the error
change?
* Check your Python version

### IO stuff

* wrong filename
* unreachable path

### Beginner traps

* multiple versions of the same python file - strange behaviour, you fix the bug but the program does not seem to change its behaviour at all. Confusing because the next one looks the same.
* mixed up return values; overlapping namespaces, you continue to use a name from within a function, assuming it is a different value.
* wrong assumptions about your code: You have a different opinion on what the computer should be doing than your computer. This is very common phenomenon among novice programmers. However, it is not a bug. In brief, you computer is right. You probably haven't decomposed the problem enough and shouldn't been coding yet. Refer to chapter 'planning'.

### Typos

* mixed parentheses - lead to weird syntax errors, 90% eliminated when you use a proper editor
* wrong indentation
* x = 3 instead of x == 3
* mismatched parenthesis or quote
* accidental monkeypatch a.value = len
* omitted function call
* omitted dereference
* explicit/implicit comparisons (if a: not the same as if a>0:)
* ternary operators, bugs with [] {} (see Python chapter in Joel Grus), x = x or 0
