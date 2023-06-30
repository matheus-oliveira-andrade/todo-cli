import click

from todo.domain.todo import Todo

from todo.infrastructure.data.file_todo_repository import FileTodoRepository

from ..todo.commands.list import list as list_command
from ..todo.commands.add import add as add_command

from todo.application.use_cases.get_todo_by_todo_id_use_case import GetTodoByTodoIdUseCase

from todo.application.use_cases.mark_todo_as_done_use_case import MarkTodoAsDoneUseCase


def print_detailed_todo(todo: Todo):
    click.secho(f'ID: {todo.id}', fg='green')
    click.secho(f'Title: {todo.title}', fg='green')
    click.secho(f'Description: {todo.title}')
    click.secho(f'Tags: {todo.tags}')
    click.secho(f'Status: {todo.status.name} {todo.modified_at if todo.is_done() else ""}')
    click.secho('')

    click.secho(f'Created at: {todo.created_at}')


@click.command()
@click.option('--todo-id', required=True, help='Todo id')
def details(todo_id: str) -> None:
    """Get details of todo"""
    todo = GetTodoByTodoIdUseCase(FileTodoRepository()).handle(todo_id)

    if todo is None:
        click.secho(f'Todo not found', fg='red')

    print_detailed_todo(todo)


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
setup_cli.add_command(details)
setup_cli.add_command(mark_as_done)


if __name__ == '__main__':
    setup_cli()
