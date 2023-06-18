import logging

from todo.domain.todo import Todo
from ..dtos.add_todo_dto import AddTodoDto


class AddTodoUseCase:

    def __init__(self, todo_repository):
        self.logger = logging.getLogger()
        self.todo_repository = todo_repository

    def handle(self, add_todo_dto: AddTodoDto) -> bool:
        self.logger.info(f"adding todo {add_todo_dto.title}")

        todo = Todo.create_new(add_todo_dto.title, add_todo_dto.description, add_todo_dto.tags)

        return self.todo_repository.save(todo)

