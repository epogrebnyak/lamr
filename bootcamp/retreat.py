"""Topic and references primitives for creating curricula from code."""

# pylint: disable=missing-class-docstring, missing-function-docstring

# %%
import pathlib
import re
from typing import Dict, List, Union

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


class PrintBook(Book):
    """Book with ISBN, usually paper."""


class Video(Publication):
    pass


class Article(Publication):
    pass


class Blog(Publication):
    pass


@dataclass
class URL:
    url: str


Reference = Union[Publication, Link, URL]


@dataclass
class Subtopic:
    title: str
    learning_points: List[str] = Field(default_factory=list)

    def add_learning_points(self, *learning_points):
        return Subtopic(self.title, self.learning_points + list(learning_points))


def bullet(string: str, char="*", offset="") -> str:
    return offset + char + " " + string


def to_markdown(item: Union[str, Subtopic], ref_dict):
    if isinstance(item, str):
        s_ = substitute(item, ref_dict)
        return bullet(s_, "*", "")
    if isinstance(item, Subtopic):

        def fmt(text):
            text = substitute(text, ref_dict)
            return bullet(text, "-", "  ")

        title_str = to_markdown(item.title, ref_dict)
        return "\n".join([title_str] + [fmt(s) for s in item.learning_points])


@dataclass
class Topic:
    title: str
    learning_points: List[Union[str, Subtopic]] = Field(default_factory=list)
    references: Dict[str, Reference] = Field(default_factory=dict)
    tagline: str = ""

    def add_learning_points(self, *learning_points: List[str]):
        return Topic(
            self.title,
            self.learning_points + list(learning_points),
            self.references,
            self.tagline,
        )

    def add_references(self, **ref_dict: Dict[str, Reference]):
        return Topic(
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

    def to_markdown(self, header_level: int = 0, prefix=""):
        header = [self._make_title_md(header_level, prefix)]
        body = [to_markdown(lp, self.references) for lp in self.learning_points]
        return "\n".join(header + body)


class TopicList(BaseModel):
    Topics: List[Topic]

    def save(self, filename: str):
        pathlib.Path(filename).write_text(self.json(indent=4), encoding="utf-8")

    def to_markdown(self, header_level: int = 0, prefix="") -> str:
        def with_prefix(i: int) -> str:
            return prefix + str(i) if prefix else ""

        lines = [
            t.to_markdown(header_level, with_prefix(i))
            for i, t in enumerate(self.Topics)
        ]
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
