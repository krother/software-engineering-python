# The Modomics story

In March 2007 I inherited the [Modomics database](http://www.genesilico.pl/modomics) from Staszek, a MSc student in the lab. Staszek handed me the code and the server passwords. Then he moved to Germany. Although he did whatever he could to support me by email, a sackful of knowledge moved away with him.

![Modomics](modomics.jpg)

There was a hard deadline for publication in June. In May, the hard disk of the server crashed. I restored most of the code from the SVN repository and loaded the database dump. However, some features were lost on the way. I was determined to not only fully recover the project, but also to add enough value to submit the publication on time.

Working on the code was tough: *"What does this mean? How does this work? Why is this character on the web page three positions further to the left than it should?"*

When the deadline drew near, I worked literally every minute until the very last moment, including late evenings and weekends. I was constantly overslept and emotionally brittle to the point of resignation. It took me a year to realize the correct term for this: burnout.

I missed the deadline, or to be precise, my supervisor hit the **STOP** button. An extra year was the best thing that could happen to the project and its maintainer. First of all, I relaxed. Second, I spent more time talking to scientists using the website and understood what they needed better. I cleaned up many big and small issues and introduced a better structure of Python modules. In the end, I had rewritten most of the code. The site was working, the publication got accepted.

Finally, after two more years, it was time to hand over the project to my successors Sebastian and Kaja. The first thing Sebastian did was that he dumped most of my code and rewrote it in Django within two weeks. Kaja kept on maintaining the server diligently, and so the database lives on until the day I write these lines, with different code, but the same vision as when it was first created.

What I learned is that taking over a program from someone is difficult.

### Modomics: Project Overview

| Name | Modomics |
|------|----------|
| Summary | Web database of modified RNA nucleotides. |
| Duration | 2006 - 2014 |
| Developers | 2 coders (2009) |
| Stakeholders | 2 senior scientists, 4 data curators (2009) |
| Size | ~10000 Python LOC |
| Technologies used | TurboGears web server <br> PostGreSQL database <br> Biopython <br> PIL |
| Development tools used | bug tracker (TRAC) <br> automatic tests (partial) <br> SVN repository <br> User Stories <br> Entity-relationship diagram |
| Publications | Machnicka MA, Milanowska K, Osman Oglu O, Purta E, Kurkowska M, Olchowik A, Januszewski W, Kalinowski S, Dunin-Horkawicz S, Rother KM, Helm M, Bujnicki JM, Grosjean H. MODOMICS: a database of RNA modification pathways: 2012 update. Nucleic Acids Res 2013 Jan 1;41(D1): D262-D267<br><br>Czerwoniec A, Dunin-Horkawicz S, Purta E, Kaminska KH, Kasprzak J, Bujnicki JM, Grosjean H, Rother K. MODOMICS: a database of RNA modification pathways. 2008 update. Nucleic Acids Res 2009 Jan;37(Database issue):D118-21. [Epub 2008 Oct 14]<br><br>Dunin-Horkawicz S, Czerwoniec A, Gajda MJ, Feder M, Grosjean H, Bujnicki JM. MODOMICS: a database of RNA modification pathways. Nucleic Acids Res. 2006 Jan 1;34(Database issue):D145-9. |

