"""Create README.md"""

from pathlib import Path
from bootcamp import Bootcamp
from content import update, GLOSSARY

update()

# fmt: off
README = """# bootcamp
Accessible curriculum in programming and data analysis for non-tech students.

""" + Bootcamp.from_file("bootcamp.json").to_markdown(3) + \
"""

### Glossary

""" + "\n\n".join([term.to_markdown() for term in GLOSSARY])
# fmt: on

Path("README.md").write_text(README)
