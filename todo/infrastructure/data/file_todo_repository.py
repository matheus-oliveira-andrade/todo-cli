from todo.application.repositories.todo_repository import TodoRepository
from todo.domain.todo import Todo

class FileTodoRepository(TodoRepository):
    def save(self, todo: Todo) -> bool:
        return True