"""Python course on the command line."""

import sys
from random import choice
from typing import Optional

import typer
from rich import print
from rich.markdown import Markdown
from typer import Typer
from typing_extensions import Annotated

from lamr.file_handlers import CodeFile, MarkdownFile, here, ls, print_md

lamr_app = Typer(
    add_completion=False,
    help="Python course on the command line.",
)


def print_from_root(filename):
    return print_md((here().parent / filename).read_text())


@lamr_app.command()
def about(contributors: bool = False, dev: bool = False):
    """Print a README file."""
    if contributors:
        print("""Contributors: ...""")
    elif dev:
        print_from_root("development.md")
    else:
        print_from_root("README.md")


def list_as_markdown(items) -> Markdown:
    strings = []
    for i, item in enumerate(items):
        strings.append(str(i + 1) + ". " + item)
    return Markdown("\n".join(strings))


def references_as_markdown(references) -> Markdown:
    strings = []
    for i, ref in enumerate(references):
        strings.append(str(i + 1) + ". " + f"{ref.title} URL: <{ref.url}>")
    return Markdown("\n".join(strings))


def bold(text) -> Markdown:
    return Markdown("**" + text.capitalize() + "**")


@lamr_app.command()
def code(
    filename: Annotated[Optional[str], typer.Argument()] = None,
    list_: Annotated[bool, typer.Option("--list")] = False,
    questions: bool = False,
    excercises: bool = False,
    references: bool = False,
    all_: Annotated[bool, typer.Option("--all")] = False,
):
    """Show code example (with questions, excercises or references)."""
    if filename is not None:
        code_file = CodeFile(filename).assert_exists()
        code_file.print()
        meta = code_file.meta
        if meta.questions and (questions or all_):
            print(bold("Review questions"))
            print(list_as_markdown(meta.questions))
            print()
        if meta.excercises and (excercises or all_):
            print(bold("Excercises"))
            print(list_as_markdown(meta.excercises))
            print()
        if meta.references and (references or all_):
            print(bold("References"))
            print(references_as_markdown(meta.references))
    if filename is None or list_:
        ls()


@lamr_app.command()
def run(filename: str):
    """Run code example."""
    CodeFile(filename).assert_exists().run()


# TRY: console.pager() loses color maybe use scrolling by section
#      with "Press any key to continue..." after each section
def show(md_file: str, paginate: bool = False):
    """Show page."""
    MarkdownFile(md_file).print(paginate)


topic_list = [
    "programming",
    "editors",
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
    topic: Annotated[Optional[str], typer.Argument()] = None,
    random: bool = False,
    tentative_topics: bool = False,
):
    """Learn or review a topic."""
    if topic in tree.keys():
        for md_file in tree[topic]:
            show(md_file)
        sys.exit(0)
    if random:
        learn(choice(list(tree.keys())))  # mypy wants it this way
    print_list("Available topics", list(tree.keys()))  # mypy wants it this way
    if tentative_topics:
        print_list("Tentative list of topics", topic_list)
