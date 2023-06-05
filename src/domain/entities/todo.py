from src.domain.entities.entity import Entity
from src.domain.enums.todo_status import TodoStatus


class Todo(Entity):

    def __init__(self, title, description, status, tags):
        self.title = title
        self.description = description
        self.status = status
        self.tags = tags

    def mark_as_done(self) -> None:
        self.status = TodoStatus.DONE

    def is_done(self) -> bool:
        return self.status == TodoStatus.DONE
