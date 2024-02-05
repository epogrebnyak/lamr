import subprocess

import pytest
from typer.testing import CliRunner

from lamr.show import lamr_app

commands = [
    ["--help"],
    ["about"],
    ["about", "--contributors"],
    ["code", "--list"],
    ["code", "x.py"],
    ["code", "cal.py", "--excercises", "--references"],
    ["code", "cal.py", "--all"],
    ["code", "logo.py", "--all"],
    ["run", "x.py"],
    ["run", "cal.py"],
    ["run", "logo.py"],
    ["manual", "variables"],
]


@pytest.mark.parametrize("args", commands)
def test_it_runs_with_cli_runner(args):
    runner = CliRunner()
    result = runner.invoke(lamr_app, args)
    assert result.exit_code == 0


subprocess_commands = [
    "lamr code cal.py | python",
]


@pytest.mark.parametrize("args", subprocess_commands)
def test_it_runs_with_subprocess(args):
    result = subprocess.getstatusoutput(args)
    assert result[0] == 0


def test_yaml_load():
    from lamr.file_handlers import CodeFile

    assert len(CodeFile("cal.py").meta.excercises) == 6


def test_front_matter(tmp_path):
    from pathlib import Path

    import frontmatter

    p = Path(tmp_path) / "a.txt"
    p.write_text("---\na: b\n---\nThis is text.")
    post = frontmatter.load(p)
    assert post["a"] == "b"
    assert post.content == "This is text."
