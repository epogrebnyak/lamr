"""Python course for beginners at your own command line."""

from random import choice

from typer import Typer

lamr_app = Typer(
    add_completion=False,
    help="Python course for beginners at your own command line.",
)


@lamr_app.command()
def about(contributors: bool = False):
    """What is it? Who made this? Alternatives?"""
    print(
        """Similar :
    - cheatsheets and roadmaps
    - W3 Schools (not a CLI, but a local docker for web)    
"""
    )
    if contributors:
        print("Contributors: ...")


@lamr_app.command()
def cat(filename: str):
    """Show code example."""
    run(filename)


@lamr_app.command()
def run(filename: str):
    """Run code example."""
    print(
        """
from datetime import date
print(date.today())
""".strip()
    )


@lamr_app.command()
def resources():
    """List more learning resources."""


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
def book():
    """Read everything as an HTML page."""
