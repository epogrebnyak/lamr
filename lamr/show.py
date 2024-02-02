"""Python course for beginners - the command line part."""

import sys
from random import choice
from typing import Optional

import typer
from rich import print
from typer import Typer
from typing_extensions import Annotated

from lamr.file_handlers import CodeFile, MarkdownFile, here, ls, print_md

lamr_app = Typer(
    add_completion=False,
    help="Python course for beginners, on the command line.",
)


def from_root(filename):
    return (here().parent / filename).read_text()


@lamr_app.command()
def about(contributors: bool = False, dev: bool = False):
    """What is it? How do I use it? Who made this?"""
    if contributors:
        print("""Contributors: ...""")
    elif dev:
        print_md(from_root("development.md"))
    else:
        print_md(from_root("README.md"))


@lamr_app.command()
def code(
    filename: Annotated[Optional[str], typer.Argument()] = None,
    list_: Annotated[bool, typer.Option("--list")] = False,
):
    """Show code example."""
    if filename is not None:
        CodeFile(filename).assert_exists().print()
    if filename is None or list_:
        ls()


@lamr_app.command()
def run(filename: str):
    """Run code example."""
    CodeFile(filename).assert_exists().run()


# TRY: console.pager() loses color maybe use scrolling by section
#      add Press any key to continue...
@lamr_app.command()
def show(md_file: str, paginate: bool = False):
    MarkdownFile(md_file).print(paginate)


topic_list = [
    "what-is-a-program",
    "run-your-code",
    "print",
    "value",
    "numbers",
    "strings",
    "bools",
    "expression",
    "variables",
    "input",
    "if-else",
    "lists",
    "for-loop",
    "while-loop",
    "functions",
    "types",
]

tree = dict(variables=["variable-assignment.md"])


def print_list(header: str, items: list[str]):
    eol = "\n  "
    print(header + ":" + eol, eol.join(items), sep="")


@lamr_app.command()
def learn(
    topic: Annotated[Optional[str], typer.Argument()] = None, random: bool = False
):
    """Learn or review a topic in Python."""
    if topic in tree.keys():
        for md_file in tree[topic]:
            show(md_file)
        sys.exit(0)
    if random:
        learn(choice(list(tree.keys())))  # mypy wants it this way
    print_list("Available topics", list(tree.keys()))  # mypy wants it this way
    print_list("Tentative topics", topic_list)


# @lamr_app.command()
# def notes():
#     """Few things to remember."""


# @lamr_app.command()
# def book():
#     """Create a single file."""

# @lamr_app.command()
# def resources():
#     """List more learning resources."""
