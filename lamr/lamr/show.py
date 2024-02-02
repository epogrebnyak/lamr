"""Python course for beginners at your own command line."""

from random import choice
from typing import Optional

import typer
from rich import print
from typer import Typer
from typing_extensions import Annotated

from lamr.file_handlers import CodeFile, MarkdownFile, here, ls, print_md

lamr_app = Typer(
    add_completion=False,
    help="Python course for beginners at your own command line.",
)


@lamr_app.command()
def about(contributors: bool = False):
    """What is it? Who made this? Any alternatives?"""
    if contributors:
        print("""Contributors: ...""")
    else:
        readme = here().parent / "README.md"
        print_md(readme.read_text())


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


@lamr_app.command()
def resources():
    """List more learning resources."""

# TRY: console.pager() loses color maybe use scrolling by section 
#      add Press any key to continue...
@lamr_app.command()
def show(md_file: str, paginate: bool = False):
    MarkdownFile(md_file).print(paginate)


topic_list = [
    "what-is-a-program",
    "where-to-run-your-code",
    "how-to-run-your-code",
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


@lamr_app.command()
def learn(
    topic: Annotated[Optional[str], typer.Argument()] = None, random: bool = False
):
    """Learn or review a topic in Python."""
    if topic in topic_list:
        print(topic_list.index(topic))
    if random:
        learn(choice(topic_list))
    print("Available topics:\n  ", "\n  ".join(topic_list), sep="")


@lamr_app.command()
def notes():
    """Few things to remember."""


@lamr_app.command()
def book():
    """Create a single file."""
