"""This a programmatic source of content. Change values here and use update() function to save to JSON file."""
from bootcamp import Course, Bootcamp

COURSES = [
    Course(
        label="P1",
        title="Jump into programming",
        topics=[
            "Where to run a Python program",
            "Language syntax",
            "Exercises",
            "Jupyter notebooks vs plain code",
            "Asking questions right (MVCE)",
            "Code practice at Leetcode, Codewars, and similar",
        ],
        tagline="Start learning Python syntax and usage.",
    ),
    Course(
        label="P2",
        title="Designing programs",
        topics=[
            "Values and types",
            "Data structures, primitive and compound types",
            "Variables",
            "Expressions and statements",
            "Functions",
            "OOP and classes",
        ],
        tagline="Introduction to programming concepts.",
    ),
    Course(
        label="P3",
        title="Advanced Python",
        topics=[
            "Installing Python locally",
            "Package managers and virtual environments",            
            "Project packaging and utilities",
            "Testing and continious integration (CI)",
            "Code refactoring",
            "Battle-tested and trending Python libraries",
            "Advanced language features (ABC, async/await, regex)"
        ],
        tagline="Inspired by Hypermodern Project Packaging by Claudio Jolowicz and 'Beyond PEP8' by Raymond Herringer.",
    ),

]

# TODO: extend list above using data below

"""
PP  Finding your itch: Small projects by domain and difficulty level (games, puzzles, small task automation, simulations, decision-making, product prototypes). Project idea and reachable scope (to be completed under a week). Data projects vs product projects.
Inspiration: build-your-own-x repo, Automate Boring Stuff book. 

P0  Preprogramming: Choose a text editor – Command line and OS basics – Version control (git) – Lightweight markup (markdown) – Collaborative workflows and etiquette – Network basics and using a remote machine – Goal setting and personal roadmaps – Peers and mentors.
Inspiration: various what-I-wish-I-knew posts and https://missing.csail.mit.edu, again simplified. 

DM  Working with data: local files and serialization (CSV/JSON/XML+pydantic), pandas and speedups (vaex, polars), mito and Excel, requests and httpx for querying APIs, web scraping (eg Beautifulsoup), visualization (matplotlib and js-based libraries), dashboards (Streamlit), databases and SQL (sqlite), overview of machine learning (scikit-learn), data workflows for advanced analytics and automated decisions.
Inspiration: data preparation for further analysis, exploratory data analysis (EDA), data charting, working databases, converting between formats (~data engineering).

ML  Mathy stuff: statistics and regressions (statmodels), “classic” machine learning (scikit-learn), deep learning (PyTorch and TensorFlow), optimisations (PuLP), causal inference, bayesian statistics (PyMC, JAX), working with text (spaCy, hugging face), AutoML.
Inspiration: “machine learning” at large.

S1  Economics and finance: Programming application in finance (eg. acquiring financial data, payments, credit scoring, trading algorithms, web3 and blockchain basics and Ethereum contracts, utilities for finance - eg OpenBB open source terminal).

E1  Software engineering and industrial practices: Modern software release cycle and DevOps – Insights into Software Architecture – Code quality: patterns, best practices and code refactoring – TDD – Waterfall vs Agile – Coding at startup vs enterprise – AWS and similar cloud infrastructure – Open source software. – Data governance.
Inspiration: just an idea SE is different from CS + industrial code practices + cloud.

Ex  Special topics: data structures and algorithms, tech interviews, systems design, databases/Hadoop/Spark, UI/UX, product management, information security and cryptography, web frameworks, history and comparison of programming languages.
"""


def update():
    Bootcamp(courses=COURSES).save_json("bootcamp.json")
