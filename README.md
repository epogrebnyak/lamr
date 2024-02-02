# lamr

[![package](https://img.shields.io/pypi/v/lamr)](https://pypi.org/project/lamr/)
[![pytest](https://github.com/epogrebnyak/bootcamp/actions/workflows/python-package.yml/badge.svg)](https://github.com/epogrebnyak/bootcamp/actions/workflows/python-package.yml)

Python course for beginners, on command line.

## Rationale

For learning on the web you have [freecodecamp](https://www.freecodecamp.org/)
or an online course of your choice,
but what if you wanted to study and practice Python at your own computer
and do it on the command line?

## How to start

You should have a working installation of Python on your computer and a terminal,
or console, open.

Install `lamr`:

```console
pip install lamr
```

Check it works:

```console
lamr --help
```

## Code examples

`lamr` provides a collection of code examples, stored as plain text files.
You can use `lamr code` and `lamr run` to see the code listing or run the files.

```console
>>> lamr code --list
cal.py  Print today's date and a calendar for current month.
x.py    A Twitter clone (maybe).

>>> lamr run cal
Today is 2024-02-02

   February 2024
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29
```

`lamr code cal --no-comment` will provide you a code listing:

```python
"""Print today's date and a calendar for current month."""

from calendar import TextCalendar
from datetime import date

t = date.today()
print("Today is", t)
print()  # prints empty line
TextCalendar().prmonth(t.year, t.month)
```

You can also run `lamr code cal` for code with comments, excercises and references.

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
