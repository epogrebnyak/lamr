# lamr

[![package](https://img.shields.io/pypi/v/lamr)](https://pypi.org/project/lamr/)
[![pytest](https://github.com/epogrebnyak/bootcamp/actions/workflows/python-package.yml/badge.svg)](https://github.com/epogrebnyak/bootcamp/actions/workflows/python-package.yml)
[![replit](https://img.shields.io/badge/replit-lamr-blue)](https://replit.com/@epogrebnyak/learnlamr?v=1)

`lamr` is a content manager to organise and display markdown files and run Python code snippets.

It is a programming manual with code and exercises to get you gradually started with Python projects.

## Documentation

<https://epogrebnyak.github.io/lamr/readme/>

## Quickstart

```console
pip install lamr
lamr --help
```

In current version there are the following excercises and manuals available.

### The calendar utility

```console
>>> lamr show cal.py --all
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
```

### Learn about variable assignment: `=`, `:=` or `<-`?

```console
lamr learn variables
```

## Development

Check out separate [Development](development.md) section:

```console
>>> lamr about --dev
```
