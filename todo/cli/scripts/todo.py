import click

from todo.domain.todo import Todo

from todo.infrastructure.data.file_todo_repository import FileTodoRepository

from todo.application.dtos.add_todo_dto import AddTodoDto
from todo.application.use_cases.add_todo_use_case import AddTodoUseCase

from todo.application.use_cases.get_todos_use_case import GetTodosUseCase


@click.command()
@click.option('--title', type=str, required=True, help='title of todo')
@click.option('--description', type=str, required=True, help='description of todo')
@click.option('--tags', multiple=True, type=str, default=[], required=False, help='tags for todo')
def add(title, description, tags):
    """Add new todo"""
    add_todo_dto = AddTodoDto(title, description, tags)

    success = AddTodoUseCase(FileTodoRepository()).handle(add_todo_dto)

    if success:
        click.echo("todo created!")


def print_todo(todo: Todo, detailed: bool) -> str:
    if detailed:
        return f"Id: {todo.id}. Status: {todo.status.name}. Title: {todo.title}. Description: {todo.description}. Tags {todo.tags}"

    return f"Status: {todo.status.name}. Title: {todo.title}. Description: {todo.description}"


@click.command()
@click.option('--detailed/-d', is_flag=True, default=False, help='Todo infos detailed')
def list_all(detailed) -> None:
    """List all todos"""
    todos = GetTodosUseCase(FileTodoRepository()).handle()

    if len(todos) == 0:
        click.echo('No todos found')
        return None

    for todo in todos:
        click.echo(print_todo(todo, detailed))


@click.group()
def setup_cli():
    """Commands to manipulate todos"""
    pass


setup_cli.add_command(add)
setup_cli.add_command(list_all)


if __name__ == '__main__':
    setup_cli()
