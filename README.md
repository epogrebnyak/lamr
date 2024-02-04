# lamr

[![package](https://img.shields.io/pypi/v/lamr)](https://pypi.org/project/lamr/)
[![pytest](https://github.com/epogrebnyak/bootcamp/actions/workflows/python-package.yml/badge.svg)](https://github.com/epogrebnyak/bootcamp/actions/workflows/python-package.yml)
[![replit](https://img.shields.io/badge/replit-lamr-blue)](https://replit.com/@epogrebnyak/learnlamr?v=1)

`lamr` is a content manager to organise and display markdown files and run Python code snippets.

It is a programming manual with code and exercises to get you started
with small Python projects with high return on your time invested.

## Quickstart

```console
pip install lamr
lamr --help
```

In current version there are the following excercises and manuals available.

### The calendar utility

```console
>>> lamr show cal.py --all
...
>>> lamr run cal.py
Today is 2024-02-04

   February 2024
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 29
```

````

### Make an ASCII art logo

```console
>>> lamr show logo.py --all
>>> lamr run logo.py
Sample font: slant
Sample text: Python 3
ASCII art:
    ____             __     __                           _____
   / __ \   __  __  / /_   / /_   ____    ____          |__  /
  / /_/ /  / / / / / __/  / __ \ / __ \  / __ \          /_ <
 / ____/  / /_/ / / /_   / / / // /_/ / / / / /        ___/ /
/_/       \__, /  \__/  /_/ /_/ \____/ /_/ /_/        /____/
         /____/
````

### Learn about variable assignment: `=`, `:=` or `<-`?

```console
lamr learn variables
```

## Motivation

On the web you have [freecodecamp](https://www.freecodecamp.org/)
or another online course of your choice, but as a programmer
you are likely to deal with command line.
What if you wanted an early start with command line while learning Python?
`lamr` is a tool you can try for this.

> [!TIP]
> If you are new to command line read into
> [What is the Command Line][ds] in "Data Science at the Command Line" book
> and [Basics] section in "The Art of Command Line" guide.

[basics]: https://github.com/jlevy/the-art-of-command-line?tab=readme-ov-file#basics
[ds]: https://jeroenjanssens.com/dsatcl/chapter-1-introduction#what-is-the-command-line

Unlike many online courses `lamr` is an open-source Python package.
You can explore its own code and propose changes or enhancements
by [writing an issue on Github](https://github.com/epogrebnyak/bootcamp/issues)
and submitting a pull request.
This way you can practice how to work collaboratively on a Python project
and share something you know with others.

> [!TIP]
> This tutorial [suggests you can get started using GitHub in less than an hour][git].
> Sometimes it takes months and even years of practice, but totally useful.

[git]: https://github.com/skills/introduction-to-github

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
You can use `lamr show` and `lamr run` to see the code listing or run the files.

```console
>>> lamr show --list
cal.py  Print today's date and a calendar for current month.
logo.py Turn a string into ASCII art using a font style.
text.py Manipulate a string.
x.py    A Twitter clone (maybe).

>>> lamr run cal.py
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

For a list of follow-up questions, excercises and usefil references
run `lamr code` with one or more flags:

```console
lamr code logo.py --questions --references
lamr code logo.py --excercises
lamr code logo.py --all
```

## The manual

`lamr learn` is a small Python textbook aimed at beginners.
It is organaized by topic such as `string` or `variables`.

```console
>>> lamr learn
# prints available topics to study

>>> lamr learn variables
# prints beginner-friendly reader about variables
```

## Development

Check out separate [Development](development.md) section:

```console
>>> lamr about --dev
```
