# pylint: disable=missing-class-docstring, missing-function-docstring

from typing import List
from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from pathlib import Path


@dataclass
class Slide:
    title: str
    content: str

    def __str__(self) -> str:
        return f"""# {self.title}
 
{self.content.strip()}    
"""


SEP = """
---

"""


class Deck(BaseModel):
    slides: List[Slide]

    def __str__(self) -> str:
        return SEP.join(map(str, self.slides))

    def write_markdown(self, filename: str):
        Path(filename).write_text(str(self), encoding="utf-8")

    def write_html(self, filename: str):
        pass


deck = Deck(
    slides=[
        Slide(
            "Markdown for presentations",
            """
Web presentations from markdown:

- https://github.com/slidevjs/slidev (24k)
- https://github.com/marp-team/marp (5k)
- https://github.com/hiroppy/fusuma (5k, last updated Nov 7, 2021)

Terminal-based presentations from markdown:

- [slides](https://github.com/maaslalani/)
- lookatme
- patat

Enhanced markdown frameworks:

- [MDX](https://github.com/mdx-js/mdx/)
- [Reveal.js](https://revealjs.com/)
""",
        ),
        Slide(
            "Formats supported from Pandoc",
            """
There are several presentation formats supported by `pandoc`.
""",
        ),
        Slide(
            "Some of code used in building this presentation",
            """
```python
@dataclass
class Slide:
    title: str
    content: str
```
""",
        ),
    ]
)

deck.write_markdown("slide.md")
