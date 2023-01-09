"""Create README.md"""

from pathlib import Path
from bootcamp import Bootcamp
from content import update, GLOSSARY

update()
courses = Bootcamp.from_file("bootcamp.json").to_markdown(3)
glossary = "\n\n".join([term.to_markdown() for term in GLOSSARY])

README = f"""# bootcamp
Accessible curriculum in programming, data analysis and the business side of information technology for non-tech students.

{courses}

### Glossary

{glossary}
"""

Path("README.md").write_text(README)
