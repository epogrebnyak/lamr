# lamr

[![package](https://img.shields.io/pypi/v/lamr)](https://pypi.org/project/lamr/)
[![pytest](https://github.com/epogrebnyak/lamr/actions/workflows/python-package.yml/badge.svg)](https://github.com/epogrebnyak/lamr/actions/workflows/python-package.yml)

Python course for beginners, at command line and on the web (in the making).

To install: 

```pip install lamr```

To run:

```console 
>>> lamr learn variables
# prints a reader

>>> lamr code --list
cal.py  Print today's date and a calendar for current month.
x.py    A Twitter clone (maybe).

>>> lamr code cal
# shows cal.py code

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

See also [Development](development.md) section (accessible as `lamr about --dev`).