# %%
from typing import List

from pydantic.dataclasses import dataclass


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
    char: str = "*"

    def line_item(self, line: str):
        return self.char + " " + line

    def __str__(self):
        lines = map(self.line_item, self.lines)
        return "\n".join(lines)


@dataclass
class NumberedList(BulletList):
    lines: List[str]
    char: str = "1."


@dataclass
class Text(Markdown):
    text: str

    def __str__(self):
        return self.text


@dataclass
class Quote(Markdown):
    text: str

    def __str__(self):
        return "> " + self.text


@dataclass
class Comment(Markdown):
    text: str

    def __str__(self):
        return "<!--" + self.text + "--!>"
