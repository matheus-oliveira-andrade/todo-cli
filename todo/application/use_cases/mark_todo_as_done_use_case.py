import logging

from ..repositories.todo_repository import TodoRepository
from typing import Tuple


class MarkTodoAsDoneUseCase:
    def __init__(self, todo_repository: TodoRepository) -> None:
        self.logger = logging.getLogger('MarkTodoAsDoneUseCase')
        self.todo_repository = todo_repository

    def handle(self, todo_id: str) -> Tuple[bool, str]:
        self.logger.info("marking todo as done")

        todo = self.todo_repository.get_by_todo_id(todo_id)

        if todo.is_done():
            return False, "already marked as done"

        todo.mark_as_done()

        return self.todo_repository.update(todo), ""
