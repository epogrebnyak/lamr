# lamr

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

## Development

User scenarios:

- [x] `lamr show <md_file>` to demonstrate a markdown file
- [ ] `lamr learn <topic>` for Python discovery by topic
- [ ] `lamr roadmap --beginner` for planning
- [x] `lamr run <filename>` or `lamr code <filename> | python` for runnable code examples
- [ ] `lamr resources` for good learning resources
- [ ] `lamr build-your-own-x` for project ideas and project scoping
- [x] patch `lamr` itself on Github as an excercise

Content:

- outline based on offline classroom course, learning outcomes by each topic
- recylce own repeated anwsers on Reddit (what is a loop, providing 'resources', etc)
- review questions and excercises to make learner do something practical
- welcome `lamr about --contributors`

Implementation:

- command line tool with `Typer` and `rich`
- `beaupy` for selectors
- VitePress for static web site

More ideas:

- human language translations including Russian
- use `lamr` as context for ChatGPT queries 

Policies:

- just human writing anf reference to even better texts
- no videos unless for unique pieces
- beginner-friendly, assumes no prior knowledge

Benchmarks:

- rustlings
- roadmap.sh
- <https://github.com/cheat/cheat/>
