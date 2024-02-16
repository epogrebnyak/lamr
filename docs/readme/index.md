# About

`lamr` is a content manager to organise and display markdown files and run Python code snippets:

- `lamr code` command provides code listing for small Python projects, together with review questions, exercises and references for each project;
- `lamr manual` summarises programming concepts and provides links to useful resources.

## Quickstart

```console
pip install lamr
lamr --help
```

### Example: Learn about variable assignment: `=`, `:=` or `<-`?

```console
lamr manual variables
```

### Example: Make an ASCII art logo

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

