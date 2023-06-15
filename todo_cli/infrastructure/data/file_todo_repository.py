from todo_cli.application.repositories.todo_repository import TodoRepository
from todo_cli.domain.todo import Todo

class FileTodoRepository(TodoRepository):
    def save(self, todo: Todo) -> bool:
        return True