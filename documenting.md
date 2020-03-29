
# Documentation Tools

Although it sounds like a boring task at first, I like documenting software. I like writing about both my own programs and those of other people. Here is why:

* First, it makes the software a lot more usable - bad documentation is a good way to keep your users out.
* Second, it makes you think about the program from a new angle, helping you understand more deeply what it does.
* Third, as long as you are writing in your native tongue, it is not really difficult, even if you are a beginner.

That said, there are a number of good Python tools to build and maintain documentation. For this article, I selected six of them:

## Sphinx

[Sphinx](http://sphinx-doc.org/) is the most well-known documentation tool for Python. It uses files in the [reStructuredText](http://docutils.sourceforge.net/rst.html) markup format to create **HTML websites** and **PDF documents**. Running Sphinx could look like this:

    sphinx-build html

The strengths of Sphinx are that you can construct cross-references within your documentation easily, and that the Python syntax highlighting is one of the best. Finally, Sphinx runs **doctests** in your code. What I like less is the layout of the generated websites, which I found difficult to change. Building documentation with Sphinx reminds me of compiling my 150-page thesis with LaTeX - it feels a bit heavy.

### Also see

* [Talk on Sphinx](https://www.youtube.com/watch?v=hM4I58TA72g)


## Mkdocs

[Mkdocs](http://www.mkdocs.org/) is a very young Python project for writing documentation which is undergoing rapid development. It uses **Markdown** as a markup language. [Markdown](http://daringfireball.net/projects/markdown/basics) is almost ridiculously simple (see an [interactive tutorial](http://markdowntutorial.com)). With Mkdocs you can compile a static HTML website from a folder with Markdown files. There are many templates to choose from and you can create your own easily. A very cool feature is that you can run a local documentation server with

    mkdocs serve

and the local website is automatically updated as you edit the Markdown documents.

## pydoc

[pydoc](https://docs.python.org/2/library/pydoc.html) generates HTML pages directly from Python code. It utilizes the docstrings of modules, classes and functions. Although the look & feel of the resulting documentation is quite raw, pydoc scores by making documentation available instantly. With

    pydoc -b

you should get a browser window with documentation links to all modules currently installed. Of course you can export the pages to HTML for the modules of your choice.


## Public Code Repositories

All of [Github](https://github.com/), [Bitbucket](https://bitbucket.org/) and [Sourceforge](http://sourceforge.net/) have their own mechanisms to display pages with documentation. These include rendering of ReST and Markdown documents (e.g. README files) and simple Wiki sites. For non-technical users they may look a bit scary, and you may lack the possibility to use your own page design. They definitely work as a starting point.


## Readthedocs

[Readthedocs](https://readthedocs.org/) is a website hosting documentation for many programming projects. It can handle both the **Sphinx** and **Mkdocs** formats (ReST and Markdown, respectively). The nice thing about it is that you can connect Readthedocs to your Github or Bitbucket repository, so that every time you push new code to the repository, the documentation gets updated as well.

## Gitbook

If you want to publish your documentation as an e-book, [Gitbook](https://www.gitbook.com/) is the tool of choice. It uses Markdown files plus a file with the table of contents to build your book as HTML, PDF, EPUB and MOBY. Gitbook provides its own editor, so you can write a book without knowing anything about e-books, about git or about programming. Compared to *real* books, there are some disadvantages, most notably the page breaks often suck. On the other hand, this is the only service listed here that allows you to sell your books.

That said, Gitbook is a great way to publish free technical documentation and training material. For an example, see the fantastic [DjangoGirls Tutorial](https://www.gitbook.com/book/djangogirls/djangogirls-tutorial/details), my personal gold standard.


## Conclusion

Which of these tools is best depends a lot on who you are writing for, what kind of documentation you are writing (tutorial, full reference, cookbook or all three combined), and what it will be read with. In any case, you have a lot of options to cover some of the white space between the README file and a 100-page manual.
