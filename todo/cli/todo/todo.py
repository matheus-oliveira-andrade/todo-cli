import click

from ..todo.commands.list import list as list_command
from ..todo.commands.add import add as add_command
from ..todo.commands.details import details as details_command
from ..todo.commands.mark_as_done import mark_as_done as mark_as_done_command


@click.group()
def setup_cli() -> None:
    """Commands to manipulate todos"""
    pass


setup_cli.add_command(add_command)
setup_cli.add_command(list_command)
setup_cli.add_command(details_command)
setup_cli.add_command(mark_as_done_command)


if __name__ == '__main__':
    setup_cli()
