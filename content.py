"""This a programmatic source of content. Change values here and use update() function to save to a JSON file."""

from bootcamp import (
    Course,
    Module,
    Bootcamp,
    Term,
    T,
    Article,
    Video,
    OpenBook,
    PrintBook,
    Manual,
    Blog,
    Topic,
    LearningPoint,
    Link,
)


programming_topics = [
    Topic(
        "Testing",
        [
            LearningPoint(
                "Unit tests and types of testing",
                [
                    Link(
                        "State of Developper Ecosystem (2021). Testing.",
                        "https://www.jetbrains.com/lp/devecosystem-2021/testing/",
                    )
                ],
            ),
            LearningPoint(
                "Testing frameworks (pytest, unittest)",
                references=[
                    Link(
                        "State of Developper Ecosystem (2021). Python Frameworks and Libraries.",
                        "https://lp.jetbrains.com/python-developers-survey-2021/#FrameworksLibraries",
                    ),
                    Manual(
                        "pytest",
                        "https://docs.pytest.org/en/7.1.x/getting-started.html#create-your-first-test",
                    ),
                    Manual(
                        "unittest", "https://docs.python.org/3/library/unittest.html"
                    ),
                ],
            ),
            LearningPoint("Continious integration (CI)"),
            LearningPoint(
                "Test Driven Developent (TDD)",
                references=[
                    Video(
                        "TDD, Where Did It All Go Wrong",
                        "Ian Cooper",
                        "https://www.youtube.com/watch?v=EZ05e7EMOLM",
                    )
                ],
            ),
        ],
    ),
    Topic(
        "Writing and building documentation (Docs-as-Code)",
        [
            LearningPoint("Writing a function docstring"),
            LearningPoint("Markdown and lightweight markup. Writing a README.md"),
            LearningPoint(
                "Documentation and website builders (sphinx-doc, mkdocs-material, jupyterbook)"
            ),
        ],
    ),
    Topic(
        "More Python Features",
        [
            LearningPoint("Type annotations"),
            LearningPoint("Context managers"),
            LearningPoint("Decorators"),
            LearningPoint("Iterators and generators"),
        ],
    ),
    Topic(
        "Advanced Capabilities",
        [
            LearningPoint("Asynchronous programming and multithreading"),
            LearningPoint("Metaprogramming (ABC)"),
            LearningPoint("Performance tuning"),
        ],
    ),
]

GLOSSARY = [
    Term(
        word="MWE",
        meaning="Minimal, workable example. A perished art of asking questions about code with just enough specific information.",
        reference=Manual(
            "How to create a Minimal, Reproducible Example",
            "https://stackoverflow.com/help/minimal-reproducible-example",
        ),
    )
]

COURSES = [
    Course(
        label="P1",
        title=T("Jump into programming"),
        modules=[
            Module(
                topics=[
                    "Where to run a Python program",
                    "Language syntax",
                    "Exercises",
                    "Standard library and popular packages",
                    "Jupyter notebooks vs plain code",
                ]
            ),
            Module(
                topics=["Asking questions right (MWE)"],
                references=[
                    Manual(
                        "How to create a Minimal, Reproducible Example",
                        "https://stackoverflow.com/help/minimal-reproducible-example",
                    ),
                    Blog(
                        "How to debug small programs",
                        "Eric Lippert",
                        "https://ericlippert.com/2014/03/05/how-to-debug-small-programs/",
                    ),
                ],
            ),
            Module(topics=["Code practice at Leetcode, Codewars, and similar"]),
        ],
        tagline="Start learning Python syntax and usage.",
    ),
    Course(
        label="P2",
        title=T("Designing programs"),
        modules=[
            Module(
                topics=[
                    "Values and types",
                    "Data structures, primitive and compound types",
                    "Variables",
                    "Expressions and statements",
                    "Functions",
                    "OOP and classes",
                ]
            )
        ],
        tagline="Introduction to programming concepts.",
    ),
    Course(
        label="P3",
        title=T("Packaging"),
        modules=[
            Module(
                topics=[
                    "Installing Python locally",
                    "Package managers (pip, poetry and alternatives)",
                    "Virtual environments",
                ]
            ),
            Module(
                topics=[
                    "Project packaging and utilities",
                ],
                references=[
                    Article(
                        "Hypermodern Project Packaging",
                        "Claudio Jolowicz",
                        "https://cjolowicz.github.io/posts/hypermodern-python-01-setup/",
                    )
                ],
            ),
        ],
        tagline="Learn how to distribute your code as a package with modern tools.",
    ),
    Course(
        label="P4",
        title=T("Write better code"),
        tagline="Patterns, refactoring, tests, documentation.",
        modules=[
            Module(
                topics=[
                    "Programming style and patterns",
                ],
                references=[
                    Video(
                        "Beyond PEP8",
                        "Raymond Herringer",
                        "https://www.youtube.com/watch?v=wf-BqAjZb8M",
                    )
                ],
            ),
            Module(
                topics=["Refactoring"],
                references=[
                    OpenBook(
                        "Refactor Like A Superhero",
                        "Alex Bespoyasov",
                        "https://github.com/bespoyasov/refactor-like-a-superhero",
                    ),
                    PrintBook(
                        "Refactoring. Improving the Design of Existing Code.",
                        "Martin Fowler, with Kent Beck",
                        "https://martinfowler.com/books/refactoring.html",
                    ),
                ],
            ),
            Module(
                topics=[
                    "Unit-testing and continious integration (CI)",
                ],
                references=[
                    Video(
                        "TDD, Where Did It All Go Wrong",
                        "Ian Cooper",
                        "https://www.youtube.com/watch?v=EZ05e7EMOLM",
                    )
                ],
            ),
            Module(
                topics=[
                    "Writing and building documentation (sphinx, mkdocs-material, jupyterbook)",
                ]
            ),
        ],
    ),
    Course(
        label="P5",
        title=T("More Python Features"),
        tagline="Not the first things to learn.",
        modules=[
            Module(
                topics=[
                    "Type annotations",
                    "Decorators",
                    "Iterators",
                ],
            ),
            Module(
                topics=[
                    "Asynchronous programming and multithreading",
                    "Metaprogramming (ABC)",
                    "Performance tuning",
                ],
            ),
        ],
    ),
]

# TODO: extend list above using data below

"""
PP  Finding your itch: Small projects by domain and difficulty level (games, puzzles, small task automation, simulations, decision-making, product prototypes). Project idea and reachable scope (to be completed under a week). Data projects vs product projects.
Inspiration: build-your-own-x repo, Automate Boring Stuff book. 

P0  Preprogramming: Choose a text editor – Command line and OS basics – Version control (git) – Lightweight markup (markdown) – Collaborative workflows and etiquette – Network basics and using a remote machine – Goal setting and personal roadmaps – Peers and mentors.
Inspiration: various what-I-wish-I-knew posts and https://missing.csail.mit.edu, again simplified. 

DM  Working with data: local files and serialization (CSV/JSON/XML+pydantic), pandas and speedups (vaex, polars), mito and Excel, requests and httpx for querying APIs, web scraping (eg Beautifulsoup), visualization (matplotlib and js-based libraries), dashboards (Streamlit), databases and SQL (sqlite), overview of machine learning (scikit-learn), data workflows for advanced analytics and automated decisions.
Inspiration: data preparation for further analysis, exploratory data analysis (EDA), data charting, working databases, converting between formats (~data engineering).
Regex.


ML  Mathy stuff: statistics and regressions (statmodels), “classic” machine learning (scikit-learn), deep learning (PyTorch and TensorFlow), optimisations (PuLP), causal inference, bayesian statistics (PyMC, JAX), working with text (spaCy, hugging face), AutoML.
Inspiration: “machine learning” at large.

S1  Economics and finance: Programming application in finance (eg. acquiring financial data, payments, credit scoring, trading algorithms, web3 and blockchain basics and Ethereum contracts, utilities for finance - eg OpenBB open source terminal).

E1  Software engineering and industrial practices: Modern software release cycle and DevOps – Insights into Software Architecture – Code quality: patterns, best practices and code refactoring – TDD – Waterfall vs Agile – Coding at startup vs enterprise – AWS and similar cloud infrastructure – Open source software. – Data governance.
Inspiration: just an idea SE is different from CS + industrial code practices + cloud.

Ex  Special topics: data structures and algorithms, tech interviews, systems design, databases/Hadoop/Spark, UI/UX, product management, information security and cryptography, web frameworks, history and comparison of programming languages.
"""


def update():
    Bootcamp(courses=COURSES).save_json("bootcamp.json")
