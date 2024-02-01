import pytest
from typer.testing import CliRunner

from lamr.show import lamr_app

commands = [
    ["--help"],
    ["about"],
    ["about", "--contributors"],
    ["cat", "x"],
    ["run", "x"],
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
