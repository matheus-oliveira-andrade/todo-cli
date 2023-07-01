import click

from todo.adapters.data.repositories.file_todo_repository import FileTodoRepository
from todo.application.use_cases.mark_todo_as_done_use_case import MarkTodoAsDoneUseCase


@click.command()
@click.option('--todo-id', required=True, type=str, help='Todo id')
def mark_as_done(todo_id: str) -> None:
    """Update status for DONE"""
    success, message = MarkTodoAsDoneUseCase(FileTodoRepository()).handle(todo_id)

    if not success:
        click.secho(message, fg='red')
