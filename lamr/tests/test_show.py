import pytest
from typer.testing import CliRunner
import subprocess

from lamr.show import lamr_app

commands = [
    ["--help"],
    ["about"],
    ["about", "--contributors"],
    ["cat", "print_date.py"],
    ["run", "print_date.py"],
    ["learn", "all"],
    ["learn", "why-python"],
    ["resources"],
    ["book"],
]
@pytest.mark.parametrize("args", commands)
def test_it_runs_with_cli_runner(args):
    runner = CliRunner()
    result = runner.invoke(lamr_app, args)
    assert result.exit_code == 0


subprocess_commands = [ 
  "lamr run print_date.py | python",
  "lamr cat print_date.py | python"
]


@pytest.mark.parametrize("args", subprocess_commands)
def test_it_runs_with_subprocess(args):
    result = subprocess.getstatusoutput(args)
    assert result[0] == 0 