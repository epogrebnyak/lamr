# bootcamp
Accessible curriculum in programming and data analysis for non-tech students.

This text is generated at [retreat.py](retreat.py) and can be downloaded as a [JSON file](programming.json) too.
When writing about code, shouldn't this be code as well?  

Click [👍](https://poll.fizzy.wtf/vote?epogrebnyak.bootcamp.like=yes)
![](https://poll.fizzy.wtf/count?epogrebnyak.bootcamp.like=yes) if you like the idea,
otherwise [raise an issue](https://github.com/epogrebnyak/bootcamp/issues) to tell what may be wrong with it.


## Programming

### P0. Jump Into Programming
> Start learning Python syntax and usage.

* Where to run a Python program. Local vs online ([Google Colab](https://colab.research.google.com/), [repl.it](https://replit.com/)) installation. Jupyter notebooks vs plain code.
* Language syntax. A very minimal set of 10 things to learn to program: numbers, strings, lists, tuples, variables, operators, `for` loop, `if`/`else`, functions and methods.
* Sample toy projects (TBA)
* Reading documentation. Python standard library and popular packages.
* Effective search: what to expect on your first Google page?
* Asking questions right: 'this code doesn't work' vs an MWE.
* Using code generation assistants (Copilot, ChatGPT, and similar)
* Discussion: Is learning Python a good bet (looking from survey data)?
* Common pitfalls and workarounds in programming start.
* What are code practice sites (Leetcode, Codewars, and similar).


### P1. Designing Programs
> Learn programming concepts.

* Values and types
* Data structures, primitive and compound types
* Variables
* Expressions and statements
* Functions
* OOP and classes


### P2. Project as a Package
> Learn how to distribute your code as a package with modern tools.

* Package managers (pip, poetry and alternatives).
* Virtual environments.
* [Project packaging and utilities](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/).


### P3. Write better code

* Programming style, patterns and best practices.
* Refactoring: [Beyond PEP8 by Raymond Herringer](https://www.youtube.com/watch?v=wf-BqAjZb8M), [Refactor Like A Superhero by Alex Bespoyasov](https://github.com/bespoyasov/refactor-like-a-superhero), and [Refactoring: Improving the Design of Existing Code by Martin Fowler (with Kent Beck)](https://martinfowler.com/books/refactoring.html).


### P4. Testing

* Excercise: `assert` statement with a function call.
* Aims and types of testing. Unit tests. [JetBrains survey (2021) on testing](https://www.jetbrains.com/lp/devecosystem-2021/testing/).
* Unit-testing frameworks ([pytest](https://docs.pytest.org/en/7.1.x/getting-started.html#create-your-first-test), [unittest](https://docs.python.org/3/library/unittest.html)) and their [popularity](https://lp.jetbrains.com/python-developers-survey-2021/#FrameworksLibraries).
* Continious integration (CI).
* Test-driven development (TDD) and ['Where Did It All Go Wrong'](https://www.youtube.com/watch?v=EZ05e7EMOLM).


### P5. Docs-as-Code
> Writing and building documentation.

* Excercise: Writing a function docstring.
* [Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) and lightweight markup languages (rst, asciidoc).
* Excercise: Writing a good README.md - [but how?](https://github.com/matiassingers/awesome-readme#articles)
* Documentation and website builders: [sphinx-doc](https://www.sphinx-doc.org/en/master/), [mkdocs-material](https://squidfunk.github.io/mkdocs-material/), [Jupyter Book](https://jupyterbook.org/en/stable/intro.html)
* Genres of documentation ([text](https://documentation.divio.com/), [video](https://www.writethedocs.org/videos/eu/2017/the-four-kinds-of-documentation-and-why-you-need-to-understand-what-they-are-daniele-procida/)).


### P6. More Python Features

* Type annotations
* Context managers
* Decorators
* Iterators and generators
* Pattern matching
* Walrus operator
* Dataclasses
* Enumerations


### P7. Advanced Capabilities

* Asynchronous programming and multithreading
* Metaprogramming (ABC)
* Performance tuning


## Glossary

**MWE.** Minimal, workable example. A perished art of asking questions about code with just enough specific information. See [more here](https://stackoverflow.com/help/minimal-reproducible-example).
