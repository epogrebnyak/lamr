from bootcamp import Bootcamp

header = """# bootcamp
Accessible learning about IT, programming and data analysis for non-tech students.
"""

bootcamp = Bootcamp.from_file("bootcamp.json")
print(header, "\n", bootcamp.to_markdown(3), sep="")
