from pathlib import Path
from bootcamp import Bootcamp
from content import update

update()

README = """# bootcamp
Accessible curriculum in programming and data analysis for non-tech students.

""" + Bootcamp.from_file(
    "bootcamp.json"
).to_markdown(
    3
)

Path("README.md").write_text(README)
