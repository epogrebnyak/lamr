"""Section, topic, learning points and references for creating experiences from code."""

# pylint: disable=missing-class-docstring, missing-function-docstring


# %%
import pathlib
from typing import Dict, List, Union
import re

from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass

from retreat import Reference


class Markdown:
    pass


@dataclass
class Header(Markdown):
    text: str
    level: int

    def __str__(self):
        return "#" * self.level + " " + self.text


@dataclass
class BulletList(Markdown):
    lines: List[str]
    char: str
    offset: int = 0

    def __str__(self):
        lines = [(" " * self.offset + self.char + " " + line) for line in self.lines]
        return "\n".join(lines)


@dataclass
class Paragraph(Markdown):
    text: str

    def __str__(self):
        return self.text


@dataclass
class LearningPoint:
    text: str

    def __str__(self):
        return self.text

class Writer:

    @classmethod
    def write_text(cls, content: str, path: str):
        pathlib.Path(path).write_text(content, encoding="utf-8")

    @classmethod
    def dump_json(cls, content, path: str):
        from json import dumps
        cls.write_text(dumps(content, indent=4), path)



@dataclass
class Topic(Writer):
    title: str
    learning_points: List[LearningPoint] = Field(default_factory=list)
    references: Dict[str, Reference] = Field(default_factory=dict)
    content: str = ""
    filename: str = ""

    def add_learning_points(self, *learning_points):
        self.learning_points += list(learning_points)
        return self

    @property
    def _filename(self):
        return self.filename if self.filename else self.title.lower().replace(" ", "_")

    def sidebar_dict(self):
        return dict(text=self.title, link=f"\\{self._filename}")

    def get_filename(self, extension: str):
        return self._filename + (
            extension if not self.filename.endswith(extension) else ""
        )

    def markdown_items(self, header_level: int):
        return [
            Header(self.title, header_level),
            BulletList([str(lp) for lp in self.learning_points], "*"),
            Paragraph(self.content),
        ]

    def to_markdown(self, header_level: int):
        return "\n\n".join(map(str, self.markdown_items(header_level)))

    def __str__(self):
        return self.to_markdown(header_level=1)

    def write_markdown(self, directory="."):
        path = pathlib.Path(directory) / self.get_filename(".md")
        self.write_text(str(self), str(path))


@dataclass
class Section:
    title: str  # this is a sidebar section
    topics: List[Topic]

    def sidebar_dict(self):
        return dict(text=self.title, items=[t.sidebar_dict() for t in self.topics])


class Course(BaseModel, Writer):
    title: str  # This is a sidebar title
    sections: List[Section]

    def write_markdown(self, directory: str):
        for s in self.sections:
            for t in s.topics:
                t.write_markdown("./vitepress/docs")

    def sidebar(self):
        return [s.sidebar_dict() for s in self.sections]

    def write_sidebar_json(self, path: str):
        self.dump_json(self.sidebar(), path)

LP = LearningPoint

s1 = Section(
    "Minimal Python",
    [
        Topic(
            "Values and operators",
            learning_points=[
                LP("Numbers and arithmetic operators"),
                LP("Strings and operations on strings"),
                LP("Comparison operators and boolean values"),
            ],
        ),
        Topic(
            "Variables",
            learning_points=[LP("Naming"), LP("Assignment"), LP("Mutation")],
        ),
        Topic(
            "Sequences",
            learning_points=[
                LP("Lists and tuples"),
                LP("Strings as sequences"),
                LP("Iteration with `for` loops"),
                LP("Membership operator"),
            ],
        ),
        Topic(
            "Control flow",
            filename="flow",
            learning_points=[LP("Loops"), LP("Conditional execution with `if`/`else`")],
        ),
        Topic("Functions and methods", filename="functions"),
        Topic("Modules and packages", filename="import"),
        Topic(
            "Input and output",
            filename="io",
            learning_points=[
                LP("Console"),
                LP("Command line"),
                LP("Files"),
                LP("Database"),
                LP("Web requests"),
                LP("Bots"),
            ],
        ),
    ],
)

s2 = Section(
    "Learn next",
    [
        Topic("Dictionaries"),
        Topic("Comprehensions"),
        Topic("`while` loops", filename="while"),
        Topic("Exceptions"),
        Topic("OOP and classes", filename="OOP"),
    ],
)


def lp(*strings):
    return [LP(s) for s in strings]


course = Course(title="Jump Into Programming", sections=(s1, s2))
course.write_markdown("./vitepress/docs")
course.write_sidebar_json("./vitepress/sidebar.json")

