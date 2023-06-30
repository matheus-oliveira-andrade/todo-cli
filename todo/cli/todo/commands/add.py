import click

from todo.infrastructure.data.file_todo_repository import FileTodoRepository
from todo.application.dtos.add_todo_dto import AddTodoDto
from todo.application.use_cases.add_todo_use_case import AddTodoUseCase


@click.command()
@click.option('--title', type=str, required=True, help='title of todo')
@click.option('--description', type=str, required=True, help='description of todo')
@click.option('--tags', multiple=True, type=str, default=[], required=False, help='tags for todo')
def add(title: str, description: str, tags: list[str]):
    """Add new todo"""
    add_todo_dto = AddTodoDto(title, description, tags)

    success = AddTodoUseCase(FileTodoRepository()).handle(add_todo_dto)

    if success:
        click.echo("todo created!")
