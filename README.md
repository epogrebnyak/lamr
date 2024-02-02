# lamr

[![package](https://img.shields.io/pypi/v/lamr)](https://pypi.org/project/lamr/)
[![pytest](https://github.com/epogrebnyak/bootcamp/actions/workflows/python-package.yml/badge.svg)](https://github.com/epogrebnyak/bootcamp/actions/workflows/python-package.yml)

Python course for beginners, at command line.

To install:

```console
pip install lamr
```

To run:

```console
>>> lamr --help
│ about    Print a README file.
│ code     Show code example.
│ learn    Learn or review a topic.
│ run      Run code example.

>>> lamr learn --list
# prints available topics to study

>>> lamr learn variables
# prints beginner-friendly reader about variables

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

>>> lamr code cal
# shows cal.py code
```

See also notes in the [Development](development.md) section:

```console
>>> lamr about --dev
```
