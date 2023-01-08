"""
P2  Designing programs: Values and types – Data structures (primitive and compound types) – Variables – Expressions and statements – Functions – OOP and classes.
Inspiration: intro to CS, functional flavor, but very simplified and based on Python, not Scheme.
"""

from pydantic import BaseModel
from typing import List

Theme = str


class Course(BaseModel):
    label: str
    title: str
    topics: List[Theme]
    tagline: str


topics = [
    t.strip()
    for t in "Values and types – Data structures, primitive and compound types – Variables – Expressions and statements – Functions – OOP and classes".split(
        "–"
    )
]
designing_programs2 = Course(
    label="P2",
    title="Designing programs",
    topics=topics,
    tagline="Introduction to programming with functional flavor, very simplified and based on Python.",
)


def to_text(course):
    return f"{course.label}. {course.title}: {' – '.join(course.topics)}.\n{course.tagline}"

def to_text2(course):
    return f"""{course.label}. {course.title}.
{course.tagline}
Topics: {' – '.join(course.topics)}"""

def to_markdown(course, header="##"):
    return f"""{header} {course.label}. {course.title}.
{course.tagline}  
Topics: {' – '.join(course.topics)}."""



def read_course(filename):
    return Course(**json.loads(pathlib.Path(filename, encoding="utf-8").read_text()))

import json
import pathlib 

header = """
# bootcamp
Accessible learning about IT, programming and data analysis for non-tech students.
"""

designing_programs = read_course("P2.json")
print(header)
print()
print(to_markdown(designing_programs))
