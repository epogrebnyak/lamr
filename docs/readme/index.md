# About

`lamr` is a content manager to organise and display markdown files and run Python code snippets:

- `lamr code` command provides code listing for small Python projects, together with review questions, exercises and references for each project;
- `lamr manual` summarises programming concepts and provides links to useful resources.

## Quickstart

```console
pip install lamr
lamr --help
```

## The calendar utility

```console
>>> lamr code cal.py --all
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

## Make an ASCII art logo

```console
>>> lamr code logo.py --all
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

## Learn about variable assignment: `=`, `:=` or `<-`?

```console
lamr manual variables
```
