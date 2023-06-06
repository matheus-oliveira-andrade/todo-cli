from src.application.use_cases.ports.todo_repository import TodoRepository


class FileTodoRepository(TodoRepository):
    def save(self, todo) -> bool:
        return True