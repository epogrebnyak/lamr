"""Python course for beginners at your own command line."""

from random import choice

from rich import print
from typer import Typer
from rich.console import Console
from rich.markdown import Markdown
from pathlib import Path

def print_md(text: str):
    console = Console()
    md = Markdown(text)
    console.print(md)

lamr_app = Typer(
    add_completion=False,
    help="Python course for beginners at your own command line.",
)


@lamr_app.command()
def about(contributors: bool = False):
    """What is it? Who made this? Alternatives?"""
    print_md(
        """## Similar tools:
    - cheatsheets and [roadmaps](https://roadmap.sh/)
    - man pages
    - W3 Schools (not a CLI, but a local docker for web)    
"""
    )
    if contributors:
        print("Contributors: ...")


@lamr_app.command()
def cat(filename: str):
    """Show code example."""
    run(filename)

from rich.console import Console
from rich.syntax import Syntax

def print_code(filename: str):
    console = Console()
    syntax = Syntax.from_path(filename)
    console.print(syntax)


@lamr_app.command()
def run(filename: str):
    """Run code example."""
    path = Path(__file__).parent / "code" / filename
    print_code(path)
    

@lamr_app.command()
def resources():
    """List more learning resources."""

@lamr_app.command()
def show(md_file: str):
    path = Path(__file__).parent / "topics" / md_file
    print_md(path.read_text())


@lamr_app.command()
def learn(topic: str):
    """Learn a new topic. Type `lamr learn all` for list of topics.

    https://github.com/petereon/beaupy selector should fit here well.
    """
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
    try:
        print(topic_list.index(topic))
    except ValueError:
        print("Available topics:\n  ", "\n  ".join(topic_list), sep="")
        print(
            "\nHow to show a topic (example):\n  ",
            f"lamr learn {choice(topic_list)}",
            sep="",
        )

@lamr_app.command()
def wisedom():
    """Few things to remember."""

@lamr_app.command()
def book():
    """Create a single file."""
