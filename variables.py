"""Section, topic, learning points and references for creating experiences from code."""

# pylint: disable=missing-class-docstring, missing-function-docstring
from typing import Dict, List
from pydantic import Field
from pydantic.dataclasses import dataclass

from retreat import Reference

@dataclass
class LearningPoint:
    title: str
    tldr: str = ""
    content: str = ""
    questions: List[str] = Field(default_factory=list)
    references: Dict[str, Reference] = Field(default_factory=dict)

from markdown import Header, Text, NumberedList, Quote

def _markdown_items(
    lp: LearningPoint, header_level: int, questions_header: str, continue_headers: bool
):
    yield Header(lp.title, header_level)
    if lp.tldr:
        yield Quote(lp.tldr)
    yield Text(lp.content)
    if lp.questions:
        _qh = questions_header
        yield Header(_qh, header_level + 1) if continue_headers else Paragraph(_qh)
        yield NumberedList(lp.questions)

def markdown_items(lp: LearningPoint):
    return _markdown_items(
        lp, header_level=2, questions_header="Questions and excercises", continue_headers=True
    )


def to_markdown(lp: LearningPoint) -> str:
    gen = map(lambda x: str(x).strip(), markdown_items(lp))
    return "\n\n".join(gen)


def from_toml(filename):
    import toml

    with open(filename, "r") as f:
        return toml.load(f)

print("# Variables\n")
sections = from_toml("variables.toml")["topics"]["Variables"]      
for section in sections:
    print(to_markdown(LearningPoint(**section)))
    print()
