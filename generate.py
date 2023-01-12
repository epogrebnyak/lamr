"""Create README.md"""

from pathlib import Path
from bootcamp import Bootcamp, TopicList
from content import update, GLOSSARY

update()
courses = Bootcamp.from_file("bootcamp.json").to_markdown(3)
glossary = "\n\n".join([term.to_markdown() for term in GLOSSARY])

README = f"""# bootcamp
Accessible curriculum in programming, data analysis and the business side of information technology for non-tech students.

## Programming

{courses}

## Glossary

{glossary}
"""

Path("README.md").write_text(README)

from content import programming_topics

for i, topic in enumerate(programming_topics):
    print()
    print(f"### P{i}. " + topic.title)
    for lp in topic.learning_points:
        print("* " + lp.name)
        if lp.references:
            for ref in lp.references:
                print("- ", ref.to_markdown())

Path("programming.json").write_text(TopicList(topics=programming_topics).json(indent=4))

print()
glossary = "\n\n".join([term.to_markdown() for term in GLOSSARY])
print(glossary)
