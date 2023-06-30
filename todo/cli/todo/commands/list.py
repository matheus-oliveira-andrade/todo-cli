import click

from todo.domain.todo import Todo
from todo.infrastructure.data.file_todo_repository import FileTodoRepository
from todo.application.use_cases.get_todos_use_case import GetTodosUseCase


def print_todo(todo: Todo, detailed: bool) -> str:
    if detailed:
        return f"Id: {todo.id}. Status: {todo.status.name}. Title: {todo.title}. Description: {todo.description}. Tags {todo.tags}"

    return f"Status: {todo.status.name}. Title: {todo.title}. Description: {todo.description}"


@click.command()
@click.option('--detailed/-d', is_flag=True, default=False, help='Todo infos detailed')
def list(detailed: bool) -> None:
    """List all todos"""
    todos = GetTodosUseCase(FileTodoRepository()).handle()

    if len(todos) == 0:
        click.echo('No todos found')
        return None

    for todo in todos:
        click.echo(print_todo(todo, detailed))
