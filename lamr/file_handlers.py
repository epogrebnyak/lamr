import ast
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar

import yaml
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax

__all__ = ["CodeFile", "MarkdownFile", "print_md", "ls", "here"]


def print_md(text: str, header: str = "", use_pager=False):
    console = Console(width=80)
    if header:
        header = header.title()

        text = f"# {header}\n\n" + text
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


def print_code_text(text: str):
    console = Console(width=80)
    syntax = Syntax(text, lexer="py")
    console.print(syntax)


def here() -> Path:
    return Path(__file__).parent


def get_docstring(file_contents: str):
    module = ast.parse(file_contents)
    docstring = ast.get_docstring(module)
    return docstring if docstring else ""


def ls():
    for path in CodeFile("any").path.parent.iterdir():
        if path.is_file() and str(path).endswith(".py"):
            print(path.name + "\t" + get_docstring(path.read_text()))


@dataclass
class File:
    filename: str
    folder: ClassVar[str]

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
class YamlFile(File):
    filename: str
    folder: ClassVar[str] = "code"

    def load(self):
        return yaml.safe_load(self.contents)

    @property
    def excercises(self):
        return self.load()["excercises"]  # reinveting pydantic here


@dataclass
class CodeFile(File):
    filename: str
    folder: ClassVar[str] = "code"

    @staticmethod
    def no_comment(text: str) -> str:
        return "\n".join(
            [line for line in text.split("\n") if not line.startswith("#")]
        )

    def run(self):
        subprocess.run(["python", self.path.absolute()])

    def print(self):
        print_code_text(self.contents)

    def print_no_comment(self):
        print_code_text(self.no_comment(self.contents))

    def get_yaml(self):
        return YamlFile(self.filename.replace(".py", ".yml"))


@dataclass
class MarkdownFile(File):
    filename: str
    ext: ClassVar[str] = "md"
    folder: ClassVar[str] = "topics"

    def print(self, paginate: bool):
        print_md(self.post.content, self.post.get("title", ""), paginate)

    @property
    def post(self):
        import frontmatter  # type: ignore

        return frontmatter.load(self.path)
