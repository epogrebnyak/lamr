"""Bootcamp course listing primitives."""

import json
import pathlib
from typing import List
from dataclasses import dataclass

from pydantic import BaseModel

@dataclass
class Link:
    text: str
    url: str

    def __str__(self):
        return f"[[{self.text}]({self.url})]"

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
    # TODO - replicate Bootcamp methods


class Course(BaseModel):
    label: str
    title: str
    topics: List[str]
    tagline: str

    def __str__(self) -> str:
        return (
            f"{self.label}. {self.title} ({self.tagline}): {' – '.join(self.topics)}."
        )


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
        return "\n\n".join(to_markdown(c, header_level) for c in self.courses)

    def __str__(self):
        return "\n\n".join(map(str, self.courses))


def to_markdown(course: Course, header_level: int = 3):
    title = course.title.title()
    return f"""{'#'*header_level} {course.label}. {title}.

> {course.tagline}

{' – '.join(course.topics)}."""
