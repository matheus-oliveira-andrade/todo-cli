from src.domain.entities.todo import Todo


class AddTodoUseCase:

    def __init__(self, todo_repository):
        self.todo_repository = todo_repository

    def handle(self, add_todo_dto) -> bool:

        todo = Todo.create_new(add_todo_dto.title, add_todo_dto.description, add_todo_dto.tags)

        return self.todo_repository.save(todo)

