# lamr

[![package](https://img.shields.io/pypi/v/lamr)](https://pypi.org/project/lamr/)
[![pytest](https://github.com/epogrebnyak/bootcamp/actions/workflows/python-package.yml/badge.svg)](https://github.com/epogrebnyak/bootcamp/actions/workflows/python-package.yml)

`lamr` is a content manager to organise and display markdown files and Python code snippets.

You can think of it as a terminal-based textbook with a code collection that assists you to learn both Python and command line.

## Quickstart

```console
pip install lamr
lamr --help
```

## Rationale

On the web you have [freecodecamp](https://www.freecodecamp.org/)
or another online course of your choice, but as a programmer
you are likely to do a lot of work on command line.

What if you wanted to do parts of studies at command line from the start?
`lamr` is a tool you can try for this.

> [!TIP]
> If you are new to command line read into [What is the Command Line][ds] in
> Data Science at the Command Line book online and [Basics] section in
> The Art of Command Line guide.

[basics]: https://github.com/jlevy/the-art-of-command-line?tab=readme-ov-file#basics
[ds]: https://jeroenjanssens.com/dsatcl/chapter-1-introduction#what-is-the-command-line

## Installation

You should have a working installation of Python and a terminal, or console, open.

Install `lamr`:

```console
pip install lamr
```

Check it works:

```console
lamr --help
```

## Code examples

`lamr` provides a collection of Python code examples stored as plain text files.
You can use `lamr code` and `lamr run` to see the code listing or run the files.

```console
>>> lamr code --list
cal.py  Print today's date and a calendar for current month.
x.py    A Twitter clone (maybe).

>>> lamr run cal.py
Today is 2024-02-02

   February 2024
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 29
```

### Code listing

To get a code listing:

```console
lamr code cal.py
```

```python
"""Print today's date and a calendar for current month."""

from calendar import TextCalendar
from datetime import date

t = date.today()
print("Today is", t)
print()  # prints empty line
TextCalendar().prmonth(t.year, t.month)
```

For a list of excercises run `lamr code` with a flag:

```
lamr code cal.py --excercises
```

## The manual

`lamr learn` is a small Python textbook aimed at beginners.
It is organaized by topic such as `string` or `variables`.

```console
>>> lamr learn --list
# prints available topics to study

>>> lamr learn variables
# prints beginner-friendly reader about variables
```

## Development

Check out separate [Development](development.md) section:

```console
>>> lamr about --dev
```
