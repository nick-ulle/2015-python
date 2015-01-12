# Python for Data Mining

[Python][] is a programming language designed to have clear, concise, and
expressive code.
An extremely popular general-purpose language, Python has been used for tasks
as diverse as web development, teaching, and systems administration.
This mini-course provides an introduction to Python for data mining.

Messy data has an inconsistent or inconvenient format, and may have missing
values.
Noisy data has measurement error.
*Data mining extracts meaningful information from messy, noisy data.*
This is a start-to-finish process that includes gathering, cleaning,
visualizing, modeling, and reporting.

Programming and research best practices are a secondary focus of the 
mini-course, because [Python is a philosophy][zen] as well as a language.
Core concepts include: writing organized, well-documented code; being a
self-sufficient learner; using version control for code management and
collaboration; ensuring reproducibility of results; producing concise,
informative analyses and visualizations.

We will meet for four weeks during the Winter 2015 quarter at the
University of California, Davis.

[zen]: http://legacy.python.org/dev/peps/pep-0020/
[Python]: https://www.python.org/

## Target Audience
The mini-course is open to undergraduate and graduate students from all
departments.
We recommend that students have prior programming experience
and a basic understanding of statistical methods,
so they can follow along with the examples.
For instance, completion of STA 108 and STA 141 is sufficient
(but not required).

## Topics

### Core Python
The mini-course will kick off with a quick introduction to the syntax of
Python, including operators, data types, control flow statements, function
definition, and string manipulation.
Slower, in-depth coverage will be given to uniquely Pythonic features such as
built-in data structures, list comprehensions, iterators, and docstrings.

Authoring packages and other advanced topics may also be discussed.

### Scientific Computing
Support for stable, high-performance vector operations is provided by the NumPy
package.
NumPy will be introduced early and used often, because it's the foundation for
most other scientific computing packages.
We will also cover SciPy, which extends NumPy with functions for
linear algebra, optimization, and elementary statistics.

Specialized packages will be discussed during the final week.

### Data Manipulation
The pandas package provides tabular data structures and convenience functions
for manipulating them.
This includes a two-dimensional data frame similar to the one found in R.
Pandas will be covered extensively, because it makes it easy to

+ Read and write many formats (CSV, JSON, HDF, database)
+ Filter and restructure data
+ Handle missing values gracefully
+ Perform group-by operations (`apply` functions)

### Data Visualization

Many visualization packages are available for Python, but the mini-course will
focus on Seaborn, which is a user-friendly abstraction of the venerable 
matplotlib package.

Other packages such as ggplot2, Vincent, Bokeh, and mpld3 may also be covered.

## Programming Environment
Python 3 has syntax changes and new features that break compatibility with
Python 2.
All of the major scientific computing packages have added support for Python 3
over the last few years, so it will be our focus.
We recommend the [Anaconda][] Python 3 distribution,
which bundles most packages we'll use into one download.
Any other packages needed can be installed using `pip` or `conda`.

Python code is supported by a vast array of editors.

+ [Spyder IDE][Spyder], included in Anaconda, 
  is a Python equivalent of RStudio, 
  designed with scientific computing in mind.
+ [PyCharm IDE][PyCharm] and [Sublime][] provide good user interfaces.
+ Terminal-based text editors, such as [Vim][] and [Emacs][], are a great
  choice for ambitious students. They can be used with any language. 
  See [here][Text Editors] for more details. Clark and Nick both use Vim.

[Anaconda]: http://continuum.io/downloads
[Spyder]: https://code.google.com/p/spyderlib/
[PyCharm]: https://www.jetbrains.com/pycharm/
[Sublime]: http://www.sublimetext.com/
[Vim]: http://www.vim.org/
[Emacs]: https://www.gnu.org/software/emacs/
[Text Editors]: http://heather.cs.ucdavis.edu/~matloff/ProgEdit/ProgEdit.html

## References

No books are required, but we recommend Wes McKinney's book:

+ McKinney, W. (2012). _Python for Data Analysis: Data Wrangling with Pandas, 
  NumPy, and IPython_. O'Reilly Media.

Python and most of the packages we'll use have excellent documentation, which
can be found at the following links.

+ [Python 3](https://docs.python.org/3/)
+ [NumPy](http://docs.scipy.org/doc/numpy/)
+ [SciPy](http://docs.scipy.org/doc/scipy/reference/)
+ [pandas](http://pandas.pydata.org/pandas-docs/stable/)
+ [matplotlib](http://matplotlib.org/contents.html)
+ [Seaborn](http://stanford.edu/~mwaskom/software/seaborn/tutorial.html)
+ [scikit-learn](http://scikit-learn.org/stable/documentation.html)
+ [IPython](http://ipython.org/documentation.html)

Due to Python's popularity, a large number of general references are available.
While these don't focus specifically on data analysis, they're helpful for
learning the language and its idioms.
Some of our favorites are listed below, many of which are free.

+ Swaroop, C. H. (2003). _[A Byte of Python][]_. ([PDF][ABoP PDF])
+ Reitz, K. _[Hitchhiker's Guide to Python][Hitchhiker's Guide]_. 
  ([PDF][HGoP PDF])
+ Lutz, M. (2014). _Python Pocket Reference_. O'Reilly Media. 
+ Beazley, D. (2009). _Python Essential Reference_. Addison-Wesley.
+ Pilgrim, M., & Willison, S. (2009). _[Dive Into Python 3][]_. Apress.
+ [Non-programmer's Tutorial for Python 3][Non]
+ [Beginner's Guide to Python][Beginner's Guide]
+ [Five Lifejackets to Throw to the New Coder][New Coder]
+ [Pyvideo][Pyvideo]\*
+ [StackOverflow][]. Please be conscious of the [rules][SO Rules]!

\* Videos featuring Guido Van Rossum, Raymond Hettinger, Travis Oliphant, 
Fernando Perez, David Beazley, and Alex Martelli are suggested.


[A Byte of Python]: http://www.swaroopch.com/notes/python/
[ABoP PDF]: http://files.swaroopch.com/python/byte_of_python.pdf

[Hitchhiker's Guide]: http://docs.python-guide.org/en/latest/
[HGop PDF]: https://media.readthedocs.org/pdf/python-guide/latest/python-guide.pdf

[Dive Into Python 3]: http://www.diveintopython3.net/
[Non]: http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3
[Beginner's Guide]: https://wiki.python.org/moin/BeginnersGuide
[New Coder]: http://newcoder.io/
[Pyvideo]: http://pyvideo.org/
[StackOverflow]: http://stackoverflow.com/questions/tagged/python
[SO Rules]: http://stackoverflow.com/tour

