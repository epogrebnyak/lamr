"""Bootcamp course primitives."""

import json
import pathlib
from typing import Dict, List, Optional, Union

from pydantic import BaseModel
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


@dataclass
class Publication:
    title: str
    author: str
    url: str

    def to_markdown(self):
        return str(Link(self.title + " by " + self.author, self.url))


class Book(Publication):
    pass


class OpenBook(Book):
    """Book with free and open content, usually electronic."""

    pass


class PrintBook(Book):
    """Book with ISBN, usually dead-tree (paper)."""

    pass


class Video(Publication):
    pass


class Article(Publication):
    pass


class Blog(Publication):
    pass


libraries = [
    Repo(
        "Build your own X",
        "https://github.com/codecrafters-io/build-your-own-x",
    ),
]

references_dict = dict(
    boring_stuff=OpenBook(
        "Automate the Boring Stuff with Python",
        "Al Sweigart",
        "https://automatetheboringstuff.com/#toc",
    ),
    hypermodern=Article(
        "Hypermodern Project Packaging",
        "Claudio Jolowicz",
        "https://cjolowicz.github.io/posts/hypermodern-python-01-setup/",
    ),
    beyond_pep_8=Video(
        "Beyond PEP8",
        "Raymond Herringer",
        "https://www.youtube.com/watch?v=wf-BqAjZb8M",
    ),
    refactor_superhero=OpenBook(
        "Refactor Like A Superhero",
        "Alex Bespoyasov",
        "https://github.com/bespoyasov/refactor-like-a-superhero",
    ),
    missing_semester=OpenBook(
        "The Missing Semester of Your CS Education",
        "Anish Athalye and Jon Gjengset and Jose Javier Gonzalez Ortiz",
        "https://missing.csail.mit.edu",
    ),
)


@dataclass
class T:
    text: str
    translation: Optional[Dict[str, str]] = None


class Term(BaseModel):
    word: str
    meaning: str = ""
    url: str = ""

    def to_markdown(self):
        if self.url:
            postfix = " " + str(Link("link", self.url))
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
