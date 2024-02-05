# `code` and `run` commands

`lamr` provides a collection of Python code examples stored as plain text files.
You can use `lamr code` and `lamr run` to see the code listing and run the files.
`lamr code` also provides review questions, excercies and references
for the code example.

## Code collection

List the entire code collection:

```console
>>> lamr code --list
cal.py  Print today's date and a calendar for current month.
logo.py Turn a string into ASCII art using a font style.
text.py Manipulate a string.
x.py    A Twitter clone (maybe).
```

## Source file listing

Display the contents of `cal.py` file:

```console
lamr code cal.py
```

This command will show the following output:

```python
"""Print today's date and a calendar for current month."""

from calendar import TextCalendar
from datetime import date

t = date.today()
print("Today is", t)
print()  # prints empty line
TextCalendar().prmonth(t.year, t.month)
```

## Run code

The calendar utility:

```console
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

Make an ASCII art logo:

```console
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
```

You can achieve similar result py piping the `code` command output to interpreter:

```console
lamr code cal.py | python
lamr code logo.py | python
```

## Build project using resources

For a list of follow-up questions, excercises and references
run `lamr code` with one or more flags:

```console
lamr code logo.py --questions
lamr code logo.py --excercises
lamr code logo.py --references
lamr code logo.py --all
```
