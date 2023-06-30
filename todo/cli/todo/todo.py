import click

from todo.domain.todo import Todo

from todo.infrastructure.data.file_todo_repository import FileTodoRepository

from todo.application.dtos.add_todo_dto import AddTodoDto
from todo.application.use_cases.add_todo_use_case import AddTodoUseCase

from todo.application.use_cases.get_todos_use_case import GetTodosUseCase

from todo.application.use_cases.get_todo_by_todo_id_use_case import GetTodoByTodoIdUseCase

from todo.application.use_cases.mark_todo_as_done_use_case import MarkTodoAsDoneUseCase


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


setup_cli.add_command(add)
setup_cli.add_command(list)
setup_cli.add_command(details)
setup_cli.add_command(mark_as_done)


if __name__ == '__main__':
    setup_cli()
