import pathlib
from retreat import (
    Term,
    Glossary,
    Topic,
    Article,
    Repo,
    Video,
    Manual,
    Subtopic,
    URL,
    OpenBook,
    PrintBook, 
    Link,
    TopicList
)


terms = [
    Term(
        "MRE",
        "Minimal, reproducable example. A perished art of asking questions about code with just enough specific information. See [more here](^mre).",
        dict(
            mre=Manual(
                "How to create a Minimal, Reproducible Example",
                "https://stackoverflow.com/help/minimal-reproducible-example",
            )
        ),
    )
]
GLOSSARY = Glossary(terms=terms)

# %%
programming_topics = [
    Topic("Jump Into Programming", tagline="Start learning Python syntax and usage.")
    .add_learning_points(
        "Python Developper Survey: Is learning Python a good bet?",
        "Python ecosystem: language, libraries, tools.",
        Subtopic("Where to run a Python program.").add_learning_points(
            "Local vs online ([Google Colab](^colab), [repl.it](^replit)) installation.",
            "Jupyter notebooks vs plain code.",
            "Codespaces and Gitpod for Github repositories.",
            "PyDiode console <https://pyodide.org/en/stable/console.html>",
        ),
        Subtopic("Minimal Python syntax: values and operations.").add_learning_points(
            "Numbers and arithmetic operations.",
            "Strings and operations on strings." "Comparison and boolean values.",
            "Operators (assignment, arithmetic, comparison, membership).",
        ),
        Subtopic("Minimal Python syntax: the rest").add_learning_points(
            "Variables (naming, assignment, mutation).",
            "Sequences: lists and tuples.",
            "Iteration with `for` loops.",
            "Conditional execution with `if`/`else`.",
            "Functions and methods.",
            "Importing modules and packages.",
            "Input and output (console, command line, files and web requests).",
        ),
        Subtopic("More of basic Python syntax").add_learning_points(
            "Dictionaries.",
            "List comprehensions.",
            "`while` loops.",
            "Exceptions and `try`/`except` statement.",
        ),
        Subtopic("Read, talk and ask:").add_learning_points(
            "Describing what your program does as input, steps and output. "
            "Writing pseudocode.",
            "Reading documentation: core Python, standard library and popular packages.",
            "Search and evaluate: what to expect on first Google page?",
            "Asking help right: 'my code doesn't work' vs an [MRE](^mre).",
            "Code generation assistants (Copilot, ChatGPT, and similar).",
        ),
        "Common pitfalls and workarounds at programming start.",
        Subtopic("What can you do next").add_learning_points(
            "Tutorials (and escaping '[tutorial hell](^th)').",
            "Toy projects (open-end). Excercises (known result, eg replicate std library function).",
            "Finding your itch (a problem to solve).",
            "Code practice sites ([Leetcode](^leet), [Codewars](^codewars), and similar).",
            "Contributing to open source projects.",
            "Answering other people's questions.",
            "Excercise: what makes a good code problem?",
        ),
    )
    .add_references(
        th=URL(
            "https://www.reddit.com/r/learnprogramming/comments/qrlx5m/what_exactly_is_tutorial_hell/?utm_source=share&utm_medium=web2x&context=3"
        ),
        colab=URL("https://colab.research.google.com/"),
        replit=URL("https://replit.com/"),
        mre=URL("https://replit.com/"),  # FIXME
        leet=URL("https://leetcode.com/"),
        codewars=URL("https://www.codewars.com"),
    ),
    Topic(
        "Designing Programs", tagline="Learn programming concepts."
    ).add_learning_points(
        "Values and types",
        "Data structures, primitive and compound types",
        "Variables",
        "Expressions and statements",
        "Functions",
        "OOP and classes",
    ),
    Topic(
        "Project as a Package",
        tagline="Learn how to distribute your code as a package with modern tools.",
    )
    .add_learning_points(
        "Package managers (pip, poetry and alternatives).",
        "Virtual environments.",
        "[Project packaging and utilities](^hypermodern).",
    )
    .add_references(
        hypermodern=Article(
            "Hypermodern Project Packaging",
            "Claudio Jolowicz",
            "https://cjolowicz.github.io/posts/hypermodern-python-01-setup/",
        )
    ),
    Topic("Write Better Code")
    .add_learning_points(
        "Can code quality be measured?",
        "Programming style, patterns and best practices.",
        "Refactoring: @beyond_pep8, @refactor_superhero, and @fowler.",
    )
    .add_references(
        beyond_pep8=Video(
            "Beyond PEP8",
            "Raymond Herringer",
            "https://www.youtube.com/watch?v=wf-BqAjZb8M",
        ),
        refactor_superhero=OpenBook(
            "Refactor Like A Superhero",
            "Alex Bespoyasov",
            "https://github.com/bespoyasov/refactor-like-a-superhero",
        ),
        fowler=PrintBook(
            "Refactoring: Improving the Design of Existing Code",
            "Martin Fowler (with Kent Beck)",
            "https://martinfowler.com/books/refactoring.html",
        ),
    ),
    Topic("Testing")
    .add_learning_points(
        "Excercise: `assert` statement with a function call.",
        "Aims and types of testing. Unit tests. [JetBrains survey (2021) on testing](^sde_testing).",
        "Unit-testing frameworks (@pytest, @unittest) and their [popularity](^sde_libraries).",
        "Continious integration (CI).",
        "Test-driven development (TDD) and ['Where Did It All Go Wrong'](^tdd).",
    )
    .add_references(
        sde_testing=Link(
            "State of Developper Ecosystem (2021). Testing.",
            "https://www.jetbrains.com/lp/devecosystem-2021/testing/",
        ),
        sde_libraries=Link(
            "State of Developper Ecosystem (2021). Python Frameworks and Libraries.",
            "https://lp.jetbrains.com/python-developers-survey-2021/#FrameworksLibraries",
        ),
        pytest=Manual(
            "pytest",
            "https://docs.pytest.org/en/7.1.x/getting-started.html#create-your-first-test",
        ),
        unittest=Manual("unittest", "https://docs.python.org/3/library/unittest.html"),
        tdd=Video(
            "TDD, Where Did It All Go Wrong",
            "Ian Cooper",
            "https://www.youtube.com/watch?v=EZ05e7EMOLM",
        ),
    ),
    Topic("Docs-as-Code", tagline="Writing and building documentation.")
    .add_learning_points(
        "Excercise: Writing a function docstring.",
        "[Markdown](^gh_markdown) and lightweight markup languages (rst, asciidoc).",
        "Excercise: Writing a good README.md - [but how?](^how)",
        "Documentation and website builders: @sphinx, [mkdocs-material](^mkdocs), [Jupyter Book](^jb)",
        "Genres of documentation ([text](^divio), [video](^kinds4)).",
    )
    .add_references(
        iam_readme=Link("Hi, my name is README", "https://raphael.codes/talks/"),
        how=Link(
            "Awesome README - Articles",
            "https://github.com/matiassingers/awesome-readme#articles",
        ),
        gh_markdown=Link(
            "Start writing on GitHub / Basic formatting syntax.",
            "https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax",
        ),
        sphinx=Link("sphinx-doc", "https://www.sphinx-doc.org/en/master/"),
        mkdocs=Link("mkdocs-material", "https://squidfunk.github.io/mkdocs-material/"),
        jb=Link("jupyterbook", "https://jupyterbook.org/en/stable/intro.html"),
        kinds4=Video(
            "The four kinds of documentation, and why you need to understand what they are",
            "Daniele Procida",
            "https://www.writethedocs.org/videos/eu/2017/the-four-kinds-of-documentation-and-why-you-need-to-understand-what-they-are-daniele-procida/",
        ),
        divio=Manual(
            "The documentation system",
            "https://documentation.divio.com/",
        ),
    ),
    Topic("More Python Features").add_learning_points(
        Subtopic("Type annotations"),
        Subtopic("Higher-order functions, iteration and lazyness").add_learning_points(
            "Iterators and generators. `itertools` library.",
            "`functools` library: `filter`, `map`, `reduce`",
        ),
        Subtopic("Flow of execution and behaviours").add_learning_points(
            "Decorators",
            "Context managers",
            "Pattern matching",
            "Walrus assignent operator",
        ),
        Subtopic("Data stuctures").add_learning_points("Dataclasses", "Enumerations"),
    ),
    Topic("Advanced Capabilities").add_learning_points(
        "Asynchronous programming and multithreading",
        "Metaprogramming (ABC)",
        "Performance tuning",
    ),
]

EXTRA_REFERENCES = dict(
    own_x=Repo(
        "Build your own X",
        "https://github.com/codecrafters-io/build-your-own-x",
    ),
    boring_stuff=OpenBook(
        "Automate the Boring Stuff with Python",
        "Al Sweigart",
        "https://automatetheboringstuff.com/#toc",
    ),
    missing_semester=OpenBook(
        "The Missing Semester of Your CS Education",
        "Anish Athalye and Jon Gjengset and Jose Javier Gonzalez Ortiz",
        "https://missing.csail.mit.edu",
    ),
)

PROGRAMMING = TopicList(Topics=programming_topics)

README = f"""## bootcamp 
Accessible curriculum in programming and data analysis for non-tech students.

Ideas and bets:

```
                                        |<-------  Focus area ---------->|  
                                <........                                ........>                                 
Subject ---> Course  ---> Topics and ---> Content ---> Delivery formats: ---> Activities  -----+
area         idea and     learning                     - handout              and assessment   |
             title        points                       - longread                              |   
                                                       - mobile site                           |
                                                       - code snippets and notebooks           V
                                                       - presentations                      Outcomes
                                                       - twitter threads                   and review  
                                                       - reading list / bibliography
```

1.  This text is generated by [readme.py](readme.py) and can be downloaded 
as a [JSON file](programming.json). When writing about code, shouldn't this be 
code as well?  Click a happy counter [👍![][count]][vote] if you like the idea.

[count]: https://poll.fizzy.wtf/count?epogrebnyak.bootcamp.like=yes 
[vote]: https://poll.fizzy.wtf/vote?epogrebnyak.bootcamp.like=yes


2. Now when we've got a JSON we can apply other skins and themes to our learning content:
    - [bootcamp.py](bootcamp.py) creates a VitePress website scaffold displayed at 
      [epogrebnyak.github.io/bootcamp](https://epogrebnyak.github.io/bootcamp/). 
    - [slides.py](slides.py) create presentations that can be converted to HTML 
      with Marp (or Slidev).

3. Current goal is to sync classes in `readme.py`, `bootcamp.py` and `slides.py`
   on balance of simolicity of writing prose in code (eg a topics list) and 
   data processing needs (eg creating a markdown file).
    
## Programming

{PROGRAMMING.to_markdown(3, "P")}


## Glossary

{GLOSSARY.to_markdown()}
"""

print(README)
PROGRAMMING.save("programming.json")
pathlib.Path("README.md").write_text(README, encoding="utf-8")
