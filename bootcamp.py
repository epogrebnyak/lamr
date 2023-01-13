"""Bootcamp course primitives."""

import json
import pathlib
from typing import Dict, List, Optional, Union

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
class LearningPoint:
    text: str
    references: List[Reference] = Field(default_factory=list)

    def __le__(self, refs: List[Reference]):
        return LearningPoint(self.text, self.references + refs)


@dataclass
class LP:
    text: str
    refs: str = ""


@dataclass
class Theme:
    title: str
    learning_points: List[LP] = Field(default_factory=list)
    references: Dict[str, Reference] = Field(default_factory=dict)

    def add_learning_points(self, *learning_points):
        return Theme(
            self.title, self.learning_points + learning_points, self.references
        )

    def add_references(self, **ref_dict):
        return Theme(self.title, self.learning_points, {**self.references, **ref_dict})

    def __le__(self, lps: List[LearningPoint]):
        return Theme(self.title, self.learning_points + lps)

    def __lshift__(self, ref_dict: Dict[str, Reference]):
        return Theme(self.title, self.learning_points, {**self.references, **ref_dict})


import re

REGEX_UPTICK = r"\(\^(\w+)\)"
REGEX_AT = r"@([\w]+)"

assert re.findall(REGEX_UPTICK, "[JetBrain survey (2021) on testing](^sde)") == ["sde"]
assert re.findall(REGEX_AT, "Frameworks: @pytest @unittest") == ["pytest", "unittest"]

ref_dict = dict(
    sde=Link(
        "State of Developper Ecosystem (2021). Testing.",
        "https://www.jetbrains.com/lp/devecosystem-2021/testing/",
    ),
    pytest=Manual(
        "pytest lib",
        "https://docs.pytest.org/en/7.1.x/getting-started.html#create-your-first-test",
    ),
    unittest=Manual("unittest lib", "https://docs.python.org/3/library/unittest.html"),
)


string = "[JetBrain survey (2021) on testing](^sde) @pytest"


def substitute(text: str, ref_dict: Dict[str, Reference]) -> str:
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


assert (
    substitute(
        text="[JetBrain survey (2021) on testing](^sde)",
        ref_dict=dict(
            sde=Link(
                "State of Developper Ecosystem (2021). Testing.",
                "https://www.jetbrains.com/lp/devecosystem-2021/testing/",
            )
        ),
    )
    == "[JetBrain survey (2021) on testing](https://www.jetbrains.com/lp/devecosystem-2021/testing/)"
)
assert substitute(
    "Unit-testing frameworks. @pytest @unittest",
    ref_dict=dict(
        pytest=Manual(
            "pytest!",
            "https://docs.pytest.org/en/7.1.x/getting-started.html#create-your-first-test",
        ),
        unittest=Manual("unittest!", "https://docs.python.org/3/library/unittest.html"),
    ),
) == (
    "Unit-testing frameworks. [pytest!](https://docs.pytest.org/en/7.1.x/getting-started.html#create-your-first-test) "
    "[unittest!](https://docs.python.org/3/library/unittest.html)"
)


# Standalone line @pytest evaluates to str(reference)
# (^sde_libraries) evaluates to (reference.url)

ts = [
    Theme("Testing")
    .add_learning_points(
        "Unit tests and types of testing. [JetBrains survey (2021) on testing](^sde_testing)",
        "Unit-testing frameworks (pytest, unittest). "
        "Popularity: [JetBrains survey (2021)](^sde_libraries). Manuals: @pytest, @unittest.",
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
    )
]

programming = [
    Theme("Testing")
    <= [
        LP(
            "Unit tests and types of testing. [JetBrains survey (2021) on testing](^sde_testing)"
        ),
        LP(
            "Unit-testing frameworks (pytest, unittest). "
            "Popularity: [JetBrains survey (2021)](^sde_libraries). Manuals: @pytest, @unittest."
        ),
    ]
    << dict(
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
    ),
]

for theme in programming:
    print(theme.title)
    for lp in theme.learning_points:
        print("* " + substitute(lp.text, theme.references))


@dataclass
class Topic:
    title: str
    learning_points: List[LearningPoint] = Field(default_factory=list)

    def __le__(self, lps: List[LearningPoint]):
        return Topic(self.title, self.learning_points + lps)


class TopicList(BaseModel):
    topics: List[Topic]


@dataclass
class T:
    text: str
    translation: Optional[Dict[str, str]] = None


class Term(BaseModel):
    word: str
    meaning: str
    reference: Optional[Reference] = None

    def to_markdown(self):
        if self.reference:
            postfix = " [" + Link("link", self.reference.url).to_markdown() + "]"
        else:
            postfix = ""
        return f"**{self.word}.** {self.meaning}" + postfix


class Glossary(BaseModel):
    courses: List[Term]


@dataclass
class Module:
    topics: List[str]
    title: str = ""
    references: Optional[List[Union[Link, Publication]]] = None
    libraries: Optional[List[Repo]] = None

    def to_markdown(self):
        prefix = f"{self.title}: " if self.title else ""
        postfix = as_list(self.references, "-", "  ")
        return prefix + " – ".join(self.topics) + postfix


def as_list(items, bullet_char, offset="") -> str:
    if items:
        lines = [f"{offset}{bullet_char} {m.to_markdown()}" for m in items]
        return ":\n" + "\n".join(lines)
    return ""


class Course(BaseModel):
    label: str
    title: T
    tagline: str
    modules: List[Module]

    def to_markdown(self, header_level: int):
        title = self.title.text.title()
        return f"""{'#'*header_level} {self.label}. {title}.

> {self.tagline}

{self.as_list()}"""

    def as_list(self) -> str:
        if len(self.modules) == 1:
            m = self.modules[0]
            return m.to_markdown() + "."
        else:
            lines = [f"* {m.to_markdown()}." for m in self.modules]
            return "\n".join(lines)


class Bootcamp(BaseModel):
    courses: List[Course]

    def save_json(self, filename: str):
        json_obj = self.json(indent=4)
        pathlib.Path(filename).write_text(json_obj, encoding="utf-8")

    @staticmethod
    def from_file(filename: str):
        content = pathlib.Path(filename).read_text(encoding="utf-8")
        return Bootcamp(**json.loads(content))

    def to_markdown(self, header_level=2):
        return "\n\n".join(course.to_markdown(header_level) for course in self.courses)

    def __str__(self):
        return "\n\n".join(map(str, self.courses))
