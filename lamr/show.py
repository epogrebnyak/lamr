"""Python course on the command line."""

import sys
from random import choice
from typing import Optional

import typer
import rich
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
        rich.print("""Contributors: ...""")
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
    markdown: bool = False,
):
    """Show code example with follow-up questions, excercises and references."""
    if filename is not None:
        code_file = CodeFile(filename).assert_exists()
        if not markdown:
            print_to_screen(code_file, questions, excercises, references, all_)
        else:
            print(markdownify(code_file, questions, excercises, references, all_))
    if filename is None or list_:
        ls()


def h2(s):
    return "## " + s


from lamr.file_handlers import get_docstring, apparently_no_docstring


def markdownify(code_file, questions, excercises, references, all_):
    runner = f"> Run ```lamr code {str(code_file.path.name)} --all``` to get this code with excercises."
    docstring = get_docstring(code_file.text)
    source = apparently_no_docstring(code_file.text)
    strings = [docstring, "```python\n" + source + "```", runner]
    meta = code_file.meta
    if all_:
        questions = True
        excercises = True
        references = True
    if meta.questions and questions:
        strings.append(h2("Review questions"))
        strings.append(list_as_markdown(meta.questions).markup)
    if meta.excercises and excercises:
        strings.append(h2("Excercises"))
        strings.append(list_as_markdown(meta.excercises).markup)
    if meta.references and references:
        strings.append(h2("References"))
        strings.append(references_as_markdown(meta.references).markup)
    return "\n\n".join(strings)


def print_to_screen(code_file, questions, excercises, references, all_):
    code_file.print()
    meta = code_file.meta
    if all_:
        questions = True
        excercises = True
        references = True
    if meta.questions and questions:
        rich.print(bold("Review questions"))
        rich.print(list_as_markdown(meta.questions))
        rich.print()
    if meta.excercises and excercises:
        rich.print(bold("Excercises"))
        rich.print(list_as_markdown(meta.excercises))
        rich.print()
    if meta.references and references:
        rich.print(bold("References"))
        rich.print(references_as_markdown(meta.references))


@lamr_app.command()
def run(filename: str):
    """Run code example."""
    CodeFile(filename).assert_exists().run()


# TRY: console.pager() loses color maybe use scrolling by section
#      with "Press any key to continue..." after each section
def to_screen(md_file: str, paginate: bool = False):
    """Show page from file."""
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

tree = dict(
    programming=["programming.md"],
    variables=["variable_assignment.md", "variable_naming.md"],
    datascience=["data_science_projects.md"],
)


def print_list(header: str, items: list[str]):
    eol = "\n  "
    rich.print(header + ":" + eol, eol.join(items), sep="")


@lamr_app.command()
def manual(
    topic: Annotated[Optional[str], typer.Argument()] = None,
    random: bool = False,
    tentative_topics: bool = False,
):
    """Learn or review a topic."""
    if topic in tree.keys():
        for md_file in tree[topic]:
            to_screen(md_file)
        sys.exit(0)
    if random:
        manual(choice(list(tree.keys())))  # mypy wants it this way
    print_list("Available topics", list(tree.keys()))  # mypy wants it this way
    if tentative_topics:
        print_list("Tentative list of topics", topic_list)


@lamr_app.command()
def learn(
    topic: Annotated[Optional[str], typer.Argument()] = None,
    random: bool = False,
    tentative_topics: bool = False,
):
    """Same as `manual` command."""
    manual(topic, random, tentative_topics)


publisher_app = typer.Typer(
    add_completion=False, help="Publish code and markdown files to website."
)


@publisher_app.command()
def code(folder: str):
    """Publish code files."""
    # This should do same as below, but for all .py files:
    # `lamr code cal.py --markdown --all > docs/code/cal.py.md`
    # `lamr publish code docs/code`
    print("I did nothing yet.")


@publisher_app.command()
def manual(folder: str):
    """Publish markdown files."""
    print("I did nothing yet.")
