import logging

from todo.domain.todo import Todo
from ..repositories.todo_repository import TodoRepository


class GetTodoByTodoIdUseCase:
    def __init__(self, todo_repository: TodoRepository) -> None:
        self.logger = logging.getLogger('GetTodoByTodoIdUseCase')
        self.todo_repository = todo_repository

    def handle(self, todo_id: str) -> Todo:
        self.logger.info("getting todos by id")

        todo = self.todo_repository.get_by_todo_id(todo_id)

        return todo
