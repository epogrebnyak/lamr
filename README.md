# lamr

[![package](https://img.shields.io/pypi/v/lamr)](https://pypi.org/project/lamr/)
[![pytest](https://github.com/epogrebnyak/bootcamp/actions/workflows/python-package.yml/badge.svg)](https://github.com/epogrebnyak/bootcamp/actions/workflows/python-package.yml)

`lamr` is a content manager to organise and display markdown files and Python code snippets.

You can think of it as a terminal-based textbook with a code collection and exercises that assist you to learn both Python and command line.

## Quickstart

```console
pip install lamr
lamr --help
```

In current version (0.1.6) the following commands should work:

```
lamr learn variables
lamr code --list
lamr code cal.py --excercises
lamr run cal.py
lamr about
```

## Motivation

On the web you have [freecodecamp](https://www.freecodecamp.org/)
or another online course of your choice, but as a programmer
you are likely to do a lot of work on command line.
What if you wanted an early start with command line while learning Python?
`lamr` is a tool you can try for this.

> [!TIP]
> If you are new to command line read into
> [What is the Command Line][ds] in "Data Science at the Command Line" book
> and [Basics] section in "The Art of Command Line" guide.

[basics]: https://github.com/jlevy/the-art-of-command-line?tab=readme-ov-file#basics
[ds]: https://jeroenjanssens.com/dsatcl/chapter-1-introduction#what-is-the-command-line

Unlike many online courses `lamr` is open-source software written in Python.
You can explore its own code and propose changes or enhancements
by [writing an issue](https://github.com/epogrebnyak/bootcamp/issues)
and submitting a pull request.
This way you can practice how to work collaboratively on a Python project
and share something you know with others.

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

You should get an output similar to this:

![screenshot](https://private-user-images.githubusercontent.com/9265326/302034409-15e2c2dc-811a-4bf6-aab6-389934d827cb.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY5NjI2ODMsIm5iZiI6MTcwNjk2MjM4MywicGF0aCI6Ii85MjY1MzI2LzMwMjAzNDQwOS0xNWUyYzJkYy04MTFhLTRiZjYtYWFiNi0zODk5MzRkODI3Y2IucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI0MDIwMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNDAyMDNUMTIxMzAzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NDJjZTkxODJlMTlhNDE5OWU3ODNhYzkyMDI3NTk4M2ExNjRiMmQzZmE3MWZhYjllOThhOGE1Nzc1MGFkMzhiOCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.cAYeOLC5Cw8syl924KAfU3RZKj6rt6vJ59mpYEzakiE)

## Code examples

`lamr` provides a collection of Python code examples stored as plain text files.
You can use `lamr code` and `lamr run` to see the code listing or run the files.

```console
>>> lamr code --list
cal.py  Print today's date and a calendar for current month.
x.py    A Twitter clone (maybe).

>>> lamr run cal.py
Today is 2024-02-03

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
