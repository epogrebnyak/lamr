# pylint: disable=missing-class-docstring, missing-function-docstring

from typing import List
from pydantic import BaseModel
from pathlib import Path


class Slide(BaseModel):
   title: str
   content: str

   def __str__(self) -> str:
    return f"""
# {self.title}
 
{self.content.strip()}    
""".strip()

class SlideList(BaseModel):
    slides: List[Slide]

slide = Slide(title="Markdown for presentations",
content="""
Web presentations from markdown:

- https://github.com/marp-team/marp (5k)
- https://github.com/hiroppy/fusuma (5k)
- https://github.com/slidevjs/slidev (24k)

Terminal-based presentations from markdown:

- lookatme
- patat
- [slides](https://github.com/maaslalani/)

JS-enhanced markdown:

- [MDX](https://github.com/mdx-js/mdx/)
- [Reveal.js](https://revealjs.com/)
""")

Path("slide.md").write_text(str(slide), encoding = "utf-8")
