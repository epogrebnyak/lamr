import ast
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax

from lamr.yaml_model import CodeMeta

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


def apparently_no_docstring(file_contents: str):
    return "\n".join(file_contents.split("\n")[2:])


def ls():
    for path in CodeFile("any").path.parent.iterdir():
        if path.is_file() and str(path).endswith(".py"):
            print(path.name + "\t" + get_docstring(path.read_text()))


@dataclass
class File:
    filename: str
    folder: str

    def assert_exists(self):
        if not self.path.exists():
            sys.exit("File not found " + str(self.path))
        return self

    @property
    def path(self):
        return here() / self.folder / self.filename

    @property
    def text(self):
        return self.path.read_text()


@dataclass
class YamlFile(File):
    filename: str
    folder: str = "code"

    @property
    def contents(self):
        return yaml.safe_load(self.text)

    @property
    def meta(self):
        return CodeMeta.from_yaml(self.path)


@dataclass
class CodeFile(File):
    filename: str
    folder: str = "code"

    def run(self):
        subprocess.run(["python", self.path.absolute()])

    def print(self):
        print_code_text(self.text)

    @property
    def yaml_file(self) -> YamlFile:
        return YamlFile(self.filename.replace(".py", ".yml"))

    @property
    def meta(self) -> CodeMeta:
        if self.yaml_file.path.exists():
            return self.yaml_file.meta
        else:
            return CodeMeta()


@dataclass
class MarkdownFile(File):
    filename: str
    folder: str = "topics"

    def print(self, paginate: bool):
        print_md(self.post.content, self.post.get("title", ""), paginate)

    @property
    def post(self):
        import frontmatter  # type: ignore

        return frontmatter.load(self.path)
