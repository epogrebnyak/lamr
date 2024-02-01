# lamr

Python course for beginners available both as a command line tool and a web site
(in the making).

User scenarios:

- [x] `lamr learn <topic>` for Python discovery by topic
- [ ] `lamr roadmap --beginner` for planning
- [x] `lamr code <filename> | python` for runnable code examples
- [x] `lamr resources` for good learning resources
- [ ] `lamr build-your-own-x` for project ideas and project scoping
- [x] patch `lamr` itself on Github when you can

Content:

- outline based on classroom courses, learning outcomes by each topic
- recylce own repeated anwsers on Reddit (what is a loop, providing 'resources', etc)
- review questions and excercises to make you do something
- contributors to topics welcome `lamr about --contributors`

Implementation:

- command line tool with `Typer` and `rich`
- `beaupy` for selectors
- VitePress for static web site
- possible language translations including Russian

Policies:

- no ChatGPT content, human writing
- no videos unless for unique pieces
- beginner-friendly, assumes no prior knowledge

Benchmarks:

- rustlings
- roadmap.sh
- https://github.com/cheat/cheat/
