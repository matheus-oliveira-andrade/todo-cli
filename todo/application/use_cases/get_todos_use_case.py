import logging

from todo.domain.todo import Todo
from ..repositories.todo_repository import TodoRepository


class GetTodosUseCase:
    def __init__(self, todo_repository: TodoRepository) -> None:
        self.logger = logging.getLogger('GetTodosUseCase')
        self.todo_repository = todo_repository

    def handle(self) -> list[Todo]:
        self.logger.info("getting todos")

        todos = self.todo_repository.get_all()

        return [] if todos is None else todos
