from src.application.repositories.todo_repository import TodoRepository


class FileTodoRepository(TodoRepository):
    def save(self, todo) -> bool:
        return True