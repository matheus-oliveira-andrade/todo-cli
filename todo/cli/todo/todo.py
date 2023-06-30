import click

from todo.infrastructure.data.file_todo_repository import FileTodoRepository

from ..todo.commands.list import list as list_command
from ..todo.commands.add import add as add_command
from ..todo.commands.details import details as details_command

from todo.application.use_cases.mark_todo_as_done_use_case import MarkTodoAsDoneUseCase


@click.command()
@click.option('--todo-id', required=True, help='Todo id')
def mark_as_done(todo_id: str) -> None:
    """Update status for DONE"""
    success, message = MarkTodoAsDoneUseCase(FileTodoRepository()).handle(todo_id)

    if not success:
        click.secho(message, fg='red')


@click.group()
def setup_cli() -> None:
    """Commands to manipulate todos"""
    pass


setup_cli.add_command(add_command)
setup_cli.add_command(list_command)
setup_cli.add_command(details_command)
setup_cli.add_command(mark_as_done)


if __name__ == '__main__':
    setup_cli()
