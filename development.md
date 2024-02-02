# Development

Big goal:

- Get a student learn to use command line and Python at the same time.

Side goals:

- Organise my prior teaching notes, notebooks, repos and reddit/SO rumblings. 

Bets:

- Get a student to learn enough to be proficient in Python, git and 
  writing docs, so that he or she may contribute to this repo by providing 
  explainations, links, code snippets and telling about what was actually
  barrier to learn and how other learners may overcome it.

User scenarios:

- [x] `lamr show <md_file>` to demonstrate a markdown file
- [x] `lamr learn <topic>` for Python discovery by topic
- [ ] `lamr roadmap --beginner` for planning
- [x] `lamr code --list` and `lamr run <filename>` for runnable code examples
- [ ] `lamr resources` for good learning resources
- [ ] `lamr build-your-own-x` for project ideas and project scoping
- [x] patch `lamr` itself on Github as an excercise

Content:

- outline based on offline classroom course, learning outcomes by each topic
- recylce own repeated anwsers on Reddit (what is a loop, providing 'resources', etc)
- review questions and excercises to make learner do something practical
- contributors welcome: `lamr about --contributors`

Implementation:

- [x] command line tool with `Typer` and `rich`
- [ ] `beaupy` for selectors
- [ ] VitePress for static web site

Pytnon stack:

- `poetry` as package manager
- `pytest`, `mypy`, `black`, `isort`, `ruff`
- `prettier` for markdown formatting
- `just` command line runner [instead of `make`][^1]

[^1]: `just` is very cool, check it out here <https://github.com/casey/just>

More ideas:

- human language translations including Russian
- use `lamr` as context for better ChatGPT queries 

Policies:

- beginner-friendly, assumes no prior knowledge
- just human writing and reference to even better texts
- no AI generated content inside
- no videos unless for unique pieces

Benchmarks:

- rustlings
- roadmap.sh
- <https://github.com/cheat/cheat/>
