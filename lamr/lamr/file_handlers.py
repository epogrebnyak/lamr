import ast
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar

from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax

__all__ = ["CodeFile", "MarkdownFile", "print_md", "ls", "here"]


def print_md(text: str, use_pager=False):
    console = Console(width=80)
    md = Markdown(text)
    if use_pager:
        with console.pager():
            console.print(md)
    else:
        console.print(md)


def print_code(filename: str):
    console = Console(width=80)
    syntax = Syntax.from_path(filename)
    console.print(syntax)


def here() -> Path:
    return Path(__file__).parent


def get_docstring(file_contents: str):
    module = ast.parse(file_contents)
    docstring = ast.get_docstring(module)
    return docstring if docstring else ""


def ls():
    for path in CodeFile("any").path.parent.iterdir():
        if path.is_file():
            print(path.name + "\t" + get_docstring(path.read_text()))


@dataclass
class File:
    filename: str
    ext: ClassVar[str]
    folder: ClassVar[str]

    def __post_init__(self):
        if not self.filename.endswith(self.ext):
            self.filename += "." + self.ext

    def assert_exists(self):
        if not self.path.exists():
            sys.exit("File not found " + str(self.path))
        return self

    @property
    def path(self):
        return here() / self.folder / self.filename

    @property
    def contents(self):
        return self.path.read_text()


@dataclass
class CodeFile(File):
    filename: str
    ext: ClassVar[str] = "py"
    folder: ClassVar[str] = "code"

    def run(self):
        subprocess.run(["python", self.path.absolute()])

    def print(self):
        print_code(self.path)


@dataclass
class MarkdownFile(File):
    filename: str
    ext: ClassVar[str] = "md"
    folder: ClassVar[str] = "topics"

    def print(self, paginate: bool):
        print_md(self.contents, paginate)
