import subprocess

import pytest
from typer.testing import CliRunner

from lamr.show import lamr_app

commands = [
    ["--help"],
    ["about"],
    ["about", "--contributors"],
    ["code", "x"],
    ["code", "x.py"],
    ["code", "x", "--no-comments"],
    ["code", "--list"],
    ["run", "cal"],
    ["run", "cal.py"],
    ["learn", "variables"],
    #    ["resources"],
    #    ["book"],
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
