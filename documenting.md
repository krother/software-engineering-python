
# Documentation Tools

Although it sounds like a boring task at first, I like documenting software. I like writing about both my own programs and those of other people. Here is why:

* First, it makes the software a lot more usable - bad documentation is a good way to keep your users out.
* Second, it makes you think about the program from a new angle, helping you understand more deeply what it does.
* Third, as long as you are writing in your native tongue, it is not really difficult, even if you are a beginner.
* Fourth, the first person who is going to benefit from good documentation is **yourself** – in a couple of weeks or months.

That said, there are a number of good Python tools to build and maintain documentation. For this article, you will find my favourite selection:

## Sphinx

[Sphinx](http://sphinx-doc.org/) is the most well-known documentation tool for Python. It uses files in the [reStructuredText](http://docutils.sourceforge.net/rst.html) markup format to create **HTML websites** and **PDF documents**. Sphinx is what many big Python libraries and Python itself use for their documentation.

Running Sphinx could look like this:

    :::bash
    sphinx-build html

Sphinx has its strengths in:

* building documents with cross-references
* integrating docstrings
* running tests from code examples (**doctests**) to see if your documentation is up to date

Sometimes I find the layout of the generated websites difficult to change, but the available templates are very good. In conclusion, I would recommend Sphinx for documentation that consists of 20+ pages. For smaller projects it may feel a bit heavy.

If you like to know more, check out this **[Talk by Eric Holscher](https://www.youtube.com/watch?v=hM4I58TA72g)**

----

## Mkdocs

[Mkdocs](http://www.mkdocs.org/) is a Python documentation tool using **Markdown** as a markup language. [Markdown](http://daringfireball.net/projects/markdown/basics) is almost ridiculously simple (see an [interactive tutorial](http://markdowntutorial.com)). With Mkdocs you can compile a static HTML website from a folder with Markdown files. There are many templates to choose from and you can create your own easily.

A very cool feature is that you can run a local documentation server with

    :::bash
    mkdocs serve

and the local website is automatically updated as you edit the Markdown documents.

Personally, I find Mkdocs much easier to get started with than Sphinx, but you have less control over things. Even changing the order of the table of contents requires an effort.

----

## GitHub Pages

[Github](https://github.com/) offers a neat mechanism to create your own pages at zero cost. It renders ReST and Markdown documents (e.g. README files). You can configure GitHub pages from the **Settings** tab of your repository. There is nothing Python-specific about GitHub pages, so it is totally up to you to make sure your documentation works.

Personally, I find the templates not that easy to edit. But GitHub pages are a great option for publishing a web page that goes beyond a README file. It is also a great tool to set up your first personal web page.

----

## Readthedocs

[Readthedocs](https://readthedocs.org/) is a website hosting documentation for many programming projects. It can handle both the **Sphinx** and **Mkdocs** formats (ReST and Markdown, respectively). The nice thing about it is that you can connect Readthedocs to your Github or Bitbucket repository, so that every time you push new code to the repository, the documentation gets updated as well. As long as the repository is public, no additional cost is involved.

My personal opinion: Great, go for it!

----

## Conclusion

Which of these tools is best depends a lot on who you are writing for, what kind of documentation you are writing (tutorial, full reference, cookbook or all three combined), and what it will be read with. In any case, you have a lot of options to cover some of the white space between the README file and a 100-page manual.
