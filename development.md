# Development

## Contributing

```
git clone https://github.com/epogrebnyak/lamr.git
cd lamr
poetry install
npm add -D vitepress
```

## Notes

Content:

- data science cookiecutter
- OOP philosophy + bragilevsky
- python packaging poetry+pyenv+rye/uv
- scientific starter textbooks
- ml textbooks
- the clock in rustpython
- projects-pumped repo (links to projects advanced)

Current issues:

- [ ] two folders now contain markdown
- [ ] may want to add icons
- [ ] need json to manage topics
- [ ] https://polar.sh/epogrebnyak
- [ ] awesome font collection (which ssg?)
- [ ] something like `npm install` for the project

Previous issues:

- [ ] list number of topics and excercises as badges through JSON 
- [ ] fallback to `beaupy` for selection within a topic
- [ ] add link to https://www.reddit.com/r/python_with_lamr/

Done:

- [x] `lamr code cal.py --markdown --all > docs/code/cal.py.md` 
- [x] put excercises in YAML file and add a flag

Big goal:

- Get a student learn to use command line and Python at the same time.

Side goals:

- Organise my prior teaching notes, notebooks, repos and reddit/SO rumblings. 
- run `vitepress` + `rich` bunble

Bets:

- Get a student to learn enough to be proficient in Python, git and 
  writing docs, so that a student may contribute to this repo by providing 
  explainations, links, code snippets and telling about what was actually
  barrier to learn and how other learners may overcome it.

User scenarios:

- [x] `lamr learn <topic>` for Python discovery by topic
- [ ] `lamr roadmap --beginner` for planning
- [x] `lamr code --list` and `lamr run <filename>` for runnable code examples
- [ ] `lamr resources` for good learning resources
- [ ] `lamr build-your-own-x` for project ideas and project scoping
- [x] patch `lamr` itself on Github as an excercise
- [ ] `lamr book`
- [ ] `lamr glossary`

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
- `just` command line runner instead of `make`[^1]

[^1]: `just` is very cool, check it out here <https://github.com/casey/just>

More ideas:

- human language translations including Russian
- use `lamr` output as context for LLM queries

Policies:

- beginner-friendly, assumes no prior knowledge
- just human writing and reference to even better texts
- text preferred to videos as a reference

Benchmarks:

- rustlings
- roadmap.sh
- <https://cheat.sh/>
- <https://github.com/cheat/cheat/>
