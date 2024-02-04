from pathlib import Path
from lamr.yaml_model import CodeMeta, Reference

def test_CodeMeta_from_yaml(tmp_path):
    path = tmp_path / "test.yaml"
    path.write_text("""
    excercises:
    - Make `Earth()` class.
    questions:
    - Is Earth flat?
    - Beter planet that Earth?
    references:
    - title: Earth is our home.
      url: https://earth.org/home
    """)

    cm = CodeMeta(
        questions=["Is Earth flat?", "Beter planet that Earth?"],
        excercises=["Make `Earth()` class."],
        references=[Reference("Earth is our home.", "https://earth.org/home")],
    )
    assert CodeMeta.from_yaml(path) == cm 
