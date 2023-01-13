"""Theme and references primitives."""

# pylint: disable=missing-class-docstring, missing-function-docstring

# %%
import pathlib
from typing import Dict, List, Union
import re

from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass


@dataclass
class Link:
    text: str
    url: str

    def __str__(self):
        return f"[{self.text}]({self.url})"

    def to_markdown(self):
        return str(self)


class Manual(Link):
    pass


class Repo(Link):
    pass


# Note: Publication class is similar to Link class, may inherit from same base class
#        that has __str__ and to_markdown() defined.
@dataclass
class Publication:
    title: str
    author: str
    url: str

    @property
    def link(self):
        return Link(self.title + " by " + self.author, self.url)

    def __str__(self):
        return str(self.link)

    def to_markdown(self):
        return str(self)


class Book(Publication):
    pass


class OpenBook(Book):
    """Book with free and open content, usually electronic."""

    pass


class PrintBook(Book):
    """Book with ISBN, usually paper."""

    pass


class Video(Publication):
    pass


class Article(Publication):
    pass


class Blog(Publication):
    pass


Reference = Union[Publication, Link]


@dataclass
class Theme:
    title: str
    learning_points: List[str] = Field(default_factory=list)
    references: Dict[str, Reference] = Field(default_factory=dict)
    tagline: str = ""

    def add_learning_points(self, *learning_points):
        return Theme(
            self.title,
            self.learning_points + list(learning_points),
            self.references,
            self.tagline,
        )

    def add_references(self, **ref_dict):
        return Theme(
            self.title,
            self.learning_points,
            {**self.references, **ref_dict},
            self.tagline,
        )

    def _make_title_md(self, header_level: int, prefix: str) -> str:
        prefix = prefix + ". " if prefix else ""
        header = "#" * header_level + " " if header_level else ""
        title = header + prefix + self.title
        if self.tagline:
            subtitle = "> " + self.tagline
            title = title + "\n" + subtitle
        return title + "\n"

    def _make_body_md(self) -> List[str]:
        def bullet(string: str) -> str:
            return "* " + string

        return [bullet(substitute(lp, self.references)) for lp in self.learning_points]

    def to_markdown(self, header_level: int = 0, prefix=""):
        lines = [self._make_title_md(header_level, prefix)] + self._make_body_md()
        return "\n".join(lines)


class ThemeList(BaseModel):
    themes: List[Theme]

    def save(self, filename: str):
        pathlib.Path(filename).write_text(self.json(indent=4), encoding="utf-8")

    def to_markdown(self, header_level: int = 0, prefix="") -> str:
        def with_prefix(i: int) -> str:
            return prefix + str(i) if prefix else ""

        lines = [t.to_markdown(header_level, with_prefix(i)) for i, t in enumerate(self.themes)]
        return "\n\n\n".join(lines)


REGEX_UPTICK = r"\(\^(\w+)\)"
REGEX_AT = r"@([\w]+)"


def substitute(text: str, ref_dict: Dict[str, Reference]) -> str:
    """In *text* evaluate standalone line @pytest to str(ref_dict["pytest"])
    (^sde_libraries) evaluates to "(" + reference.url + ")"
    """
    _s = substitute_upticks(text, ref_dict)
    return substitute_at(_s, ref_dict)


def substitute_upticks(text: str, ref_dict: Dict[str, Reference]) -> str:
    for key in re.findall(REGEX_UPTICK, text):
        pattern = "\^" + key
        replacement = ref_dict[key].url
        text = re.sub(pattern, replacement, text)
    return text


def substitute_at(text: str, ref_dict: Dict[str, Reference]) -> str:
    for key in re.findall(REGEX_AT, text):
        pattern = "@" + key
        replacement = str(ref_dict[key])
        text = re.sub(pattern, replacement, text)
    return text


@dataclass
class Term:
    word: str
    meaning: str
    references: Dict[str, Reference] = Field(default_factory=dict)

    @property
    def _meaning(self):
        return substitute(self.meaning, self.references)

    def __str__(self) -> str:
        return f"**{self.word}.** {self._meaning}"

    def to_markdown(self):
        return str(self)


class Glossary(BaseModel):
    terms: List[Term]

    def save(self, filename: str):
        pathlib.Path(filename).write_text(self.json(indent=4), encoding="utf-8")

    def to_markdown(self) -> str:
        # TODO: add sort by self.word
        lines = [str(t) for t in self.terms]
        return "\n".join(lines)


terms = [
    Term(
        "MWE",
        "Minimal, workable example. A perished art of asking questions about code with just enough specific information. See [more here](^mre).",
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
programming_themes = [
    Theme(
        "Jump Into Programming", tagline="Start learning Python syntax and usage."
    ).add_learning_points(
        "Where to run a Python program. Local vs online (Colab, repl.it) installation. Jupyter notebooks vs plain code.",
        "Language syntax.",
        "Exercises.",
        "Python standard library and popular packages.",
        "Reading documentation. Effective search.",
        "Asking questions: 'this code doesn't work' vs an MRE.",
        "New: code generation assistant (Copilot, ChatGPT, and similar)",
        "Code practice at Leetcode, Codewars, and similar.",
    ),
    Theme(
        "Designing Programs", tagline="Learn programming concepts."
    ).add_learning_points(
        "Values and types",
        "Data structures, primitive and compound types",
        "Variables",
        "Expressions and statements",
        "Functions",
        "OOP and classes",
    ),
    Theme(
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
    Theme("Write better code")
    .add_learning_points(
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
    Theme("Testing")
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
    Theme("Docs-as-Code", tagline="Writing and building documentation.")
    .add_learning_points(
        "Excercise: Writing a function docstring.",
        "[Markdown](^gh_markdown) and lightweight markup languages.",
        "Excercise: Writing a good README.md - [but how?](^how)",
        "Documentation and website builders: @sphinx, [mkdocs-material](^mkdocs), [Jupyter Book](^jb)",
        "Genres of documentation ([text](^divio), [video](^kinds4)).",
    )
    .add_references(
        how = Link("Awesome Readme - Articles",
        "https://github.com/matiassingers/awesome-readme#articles"),
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
    Theme("More Python Features").add_learning_points(
        "Type annotations",
        "Context managers",
        "Decorators",
        "Iterators and generators",
        "Pattern matching",
        "Walrus operator",
        "Dataclasses",
        "Enumerations",
    ),
    Theme("Advanced Capabilities").add_learning_points(
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


PROGRAMMING = ThemeList(themes=programming_themes)

README = f"""# bootcamp
Accessible curriculum in programming and data analysis for non-tech students.

## Programming

{PROGRAMMING.to_markdown(3, "P")}


## Glossary

{GLOSSARY.to_markdown()}
"""

print(README)
PROGRAMMING.save("programming.json")
pathlib.Path("README.md").write_text(README, encoding="utf-8")

# %%
