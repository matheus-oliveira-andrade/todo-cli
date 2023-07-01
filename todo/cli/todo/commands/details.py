import click

from todo.domain.todo import Todo
from todo.adapters.data.repositories.file_todo_repository import FileTodoRepository
from todo.application.use_cases.get_todo_by_todo_id_use_case import GetTodoByTodoIdUseCase


def print_detailed_todo(todo: Todo):
    click.secho(f'ID: {todo.id}', fg='green')
    click.secho(f'Title: {todo.title}', fg='green')
    click.secho(f'Description: {todo.title}')
    click.secho(f'Tags: {todo.tags}')
    click.secho(f'Status: {todo.status.name} {todo.modified_at if todo.is_done() else ""}')
    click.secho('')

    click.secho(f'Created at: {todo.created_at}')


@click.command()
@click.option('--todo-id', required=True, type=str, help='Todo id')
def details(todo_id: str) -> None:
    """Get details"""
    todo = GetTodoByTodoIdUseCase(FileTodoRepository()).handle(todo_id)

    if todo is None:
        click.secho(f'Todo not found', fg='red')

    print_detailed_todo(todo)
